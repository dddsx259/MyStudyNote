# OSTEP Ch.27 Interlude: Thread API — 阅读讲义

- **来源**: `Lec/OSTEP 27 threads api.pdf` (12 页)
- **对齐课件**: Pthreads API 页
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/threads-api.pdf
- **代码**: 官方 `ostep-code/threads-api/`

> 本章是 API 插曲: 会用 `create/join/lock/CV` 接口; 实现原理在后续锁/CV 章.

---

## 1. Thread Creation (§27.1)

原型:

```c
int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void *(*start_routine)(void *),
                   void *arg);
```

- 成功返回 0; 失败返回错误码 (**不** 像 `fork` 用负值)
- `start_routine` 签名 `void *func(void *)`
- 属性对象可配栈大小等; 入门用 `NULL`

### 例子: 用结构体传多个参数 (仓库 `thread_create.c`)

```c
#include <assert.h>
#include <stdio.h>
#include <pthread.h>

typedef struct {
    int a;
    int b;
} myarg_t;                                    // 打包多个参数 (单 void* 不够用时)

void *mythread(void *arg) {
    myarg_t *args = (myarg_t *) arg;
    printf("%d %d\n", args->a, args->b);      // 读调用者传入的结构
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p;
    myarg_t args = { 10, 20 };                // 注意: args 须在 join 前保持有效

    int rc = pthread_create(&p, NULL, mythread, &args);
    assert(rc == 0);                          // 0 = 成功
    (void) pthread_join(p, NULL);
    printf("done\n");
    return 0;
}
```

| 陷阱 | 说明 |
|---|---|
| 参数寿命 | 勿把「即将离开作用域的栈对象地址」传给线程后立刻返回 (本例在 `join` 前 `args` 仍活着, 安全) |
| 返回值 | `pthread_create` 成功是 **0**, 与 `fork` 习惯不同 |

---

## 2. Thread Completion (§27.2)

- `pthread_join(tid, &retval)`: 等待 tid 结束并取返回值
- 不 join 且非 detached → 资源可能泄漏 (类似小 zombie)
- `pthread_exit` / 从入口函数 `return` 结束线程
- **勿** 把指向线程栈上局部变量的指针当返回值 (栈回收后悬空)

### 例子: 用整型参数 / 返回值 (仓库 `thread_create_simple_args.c`)

```c
#include <stdio.h>
#include <pthread.h>
#include "common_threads.h"

void *mythread(void *arg) {
    long long int value = (long long int) arg;  // 小整数可经指针位宽「偷渡」
    printf("%lld\n", value);
    return (void *) (value + 1);                // 返回值同样经 void* 传回
}

int main(int argc, char *argv[]) {
    pthread_t p;
    long long int rvalue;
    Pthread_create(&p, NULL, mythread, (void *) 100);
    Pthread_join(p, (void **) &rvalue);         // 取线程返回值 → 101
    printf("returned %lld\n", rvalue);
    return 0;
}
```

---

## 3. Locks (§27.3)

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;  // 静态初始化

pthread_mutex_lock(&lock);        // 进入临界区前加锁; 拿不到则阻塞
/* critical section */            // 访问共享数据的代码
pthread_mutex_unlock(&lock);      // 离开时解锁; 与 lock 成对
```

- 保护共享数据; **加锁粒度与持锁时间** 影响性能与死锁风险
- 动态初始化用 `pthread_mutex_init` / `destroy` 成对
- 书中常再包一层 `Pthread_mutex_lock` 做错误检查 (见 `common_threads.h`)

---

## 4. Condition Variables (§27.4)

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;

pthread_mutex_lock(&lock);
while (!ready) {                              // Mesa: 用 while 再检查条件, 不用 if
    pthread_cond_wait(&cond, &lock);          // 原子: 释放 lock 并睡眠; 醒来前重新持锁
}
/* 条件已满足, 仍持有 lock */
pthread_mutex_unlock(&lock);

/* 另一线程: */
pthread_mutex_lock(&lock);
ready = 1;
pthread_cond_signal(&cond);                   // 唤醒至少一个等待者
/* 或 pthread_cond_broadcast(&cond); 唤醒全部 */
pthread_mutex_unlock(&lock);
```

| API | 含义 |
|---|---|
| `wait` | 必须与 mutex **一起** 用; wait 期间释放锁 |
| `signal` / `broadcast` | 唤醒; 通常在持锁时改状态再 signal |
| `while` | Mesa 语义下防伪唤醒 / 被抢跑; Final Q5 风格题常用 |

---

## 5. Compiling (§27.5)

链接需 `-pthread` (或平台等价). 数据竞争可用 helgrind 等工具辅助 (homework).

---

## 6. Summary

记住最小集合: create, join, mutex lock/unlock, cond wait/signal. 正确性细节 (自旋, futex, 伪唤醒) 见后续章.
