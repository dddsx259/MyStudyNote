# OSTEP Ch.26 Concurrency: An Introduction — 阅读讲义

- **来源**: `Lec/OSTEP 26 threads intro.pdf` (16 页)
- **对齐课件**: `Lec/Lec07 thread concept.pdf`
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/threads-intro.pdf
- **代码**: 官方 `ostep-code/threads-intro/` (`t0.c`, `t1.c`)

---

## 0. 为何在 OS 课

OS 是最早的大型并发程序; 应用多线程普及后, 同样问题摆到用户程序员面前.

---

## 1. Why Use Threads? (§26.1)

1. **并行 (parallelism)**: 多核上同时推进
2. **避免阻塞整程序**: 一活动等待 I/O 时另一活动可继续 (相对单线程进程)

相对多进程: 线程共享地址空间, 通信更轻; 但共享带来正确性难题.

---

## 2. Thread Creation Example (§26.2) — `t0.c` (Figure 26.2)

完整程序 (官方 `ostep-code/threads-intro/t0.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "common.h"
#include "common_threads.h"   // Pthread_create / Pthread_join 包装 (检查返回值)

void *mythread(void *arg) {                   // 线程入口: 参数是 void*
    printf("%s\n", (char *) arg);             // 打印传入的字符串 "A" 或 "B"
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 1) {
        fprintf(stderr, "usage: main\n");
        exit(1);
    }

    pthread_t p1, p2;
    printf("main: begin\n");
    Pthread_create(&p1, NULL, mythread, "A"); // 创建线程, 入口 mythread, 参数 "A"
    Pthread_create(&p2, NULL, mythread, "B");
    // join: 等待工人线程结束, 否则 main 可能先退出带走整个进程
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("main: end\n");
    return 0;
}
```

| 要点 | 说明 |
|---|---|
| 输出 | `main: begin` 后, `A`/`B` 打印 **次序不确定**, 最后 `main: end` |
| `join` | 同步点: 保证工人跑完再结束 main |
| 相对 `fork` | 同进程内多控制流; 共享地址空间 (本例几乎不共享可变数据) |

---

## 3. Shared Data Makes It Worse (§26.3) — `t1.c` (Figure 26.6)

完整程序 (官方 `ostep-code/threads-intro/t1.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include "common.h"
#include "common_threads.h"

int max;
volatile int counter = 0;                     // 共享全局变量; 两线程都会写

void *mythread(void *arg) {
    char *letter = arg;                       // "A" 或 "B"
    int i;                                    // 栈上局部变量: 每线程私有
    printf("%s: begin [addr of i: %p]\n", letter, &i);
    for (i = 0; i < max; i++) {
        counter = counter + 1;                // 读-改-写非原子 → race
    }
    printf("%s: done\n", letter);
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: main-first <loopcount>\n");
        exit(1);
    }
    max = atoi(argv[1]);

    pthread_t p1, p2;
    printf("main: begin [counter = %d] [%x]\n", counter,
           (unsigned int) &counter);
    Pthread_create(&p1, NULL, mythread, "A");
    Pthread_create(&p2, NULL, mythread, "B");
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    printf("main: done\n [counter: %d]\n [should: %d]\n",
           counter, max*2);                   // 期望 2*max; 大循环时常更小
    return 0;
}
```

| 观察 | 含义 |
|---|---|
| `&i` 不同 | 每线程私有栈 |
| `&counter` 相同 | 共享全局 |
| `counter` 终值 | 常 **小于** `2*max` → classic **lost update** / race |

---

## 4. Uncontrolled Scheduling (§26.4)

调度器可在任意指令边界切换 (或真并行) → 交错空间巨大. 示例: 两线程各执行 load-inc-store, 一种交错只 +1.

---

## 5. Wish For Atomicity (§26.5)

若有办法让「三指令序列」作为 **原子** 执行, race 消失. 支持同步是后续章节主题.

**Crux**: 如何支持同步 (synchronization)?

---

## 6. Waiting For Another (§26.6)

除互斥外还要 **等待条件** (如生产者-消费者). 忙等浪费 CPU; 需要睡眠/唤醒类原语 (条件变量等).

---

## 7. Summary (§26.7)

线程 = 新并发维度; 共享内存 + 不受控交错 = race; OS/硬件须提供互斥与等待机制. Homework 中的 `x86.py` 模拟器用于观察交错 (课上可不跑, 知道用途即可).

---

## 与课件对照

| 课件 | 本章 |
|---|---|
| `x++` 交错图 | §26.3–26.4 / `t1.c` |
| Race / CS / Mutex 定义 | §26.3–26.5 |
| Crux 同步 | §26.5–26.6 |
| `pthread_create` / join | `t0.c` |
