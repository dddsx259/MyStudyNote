# Tutorial 3 — Pthread: 讲义

- **来源**: `tut/Tut03 pthread.pdf` (26 页)
- **Tutor**: Pei Yuxing (课程材料)
- **课程**: COMP3230B Principles of Operating Systems
- **对齐**: `Lec/Lec07 thread concept`; `Lec/Lec08 synchronization`; OSTEP Ch.26–28, 30; MiniLab4
- **短摘要**: 同目录 `Tut03 pthread 总结.md`

---

## 0. 本 Tut 要解决什么

从「多进程」进入「同进程多线程」, 并掌握同步两件套: **mutex** 与 **condition variable**.

| Part | 内容 |
|---|---|
| I | Pthread API: create / join / self / exit / cancel |
| II | Mutex: 丢失更新; lock / unlock / trylock |
| III | Condition variables: `done` + `while` + wait / signal |
| Ref | C11 atomics; local vs static; cancellation |

编译链接: `#include <pthread.h>`, 链接加 **`-pthread`**.

---

## 1. Part I — The Pthread API

### 1.1 Thread vs Process (对比 Tut02)

| | 多进程 (`fork`) | 多线程 (`pthread_create`) |
|---|---|---|
| 地址空间 | 各自一份 (COW 后独立) | **共享** code / 全局 / heap / 打开文件等 |
| 栈 / 寄存器 / PC | 每进程一份 | **每线程一份** |
| 交换数据 | IPC / 显式共享内存 | 直接传**指针**指向共享对象 |
| 崩溃影响 | 一进程崩通常不直接毁掉他进程用户内存 | 一线程野指针可毁掉**整个进程** |

口诀: **线程是「轻量并发单位」, 共享堆与全局, 各有栈.**

### 1.2 生命周期对照表

| 任务 | Process | Pthread |
|---|---|---|
| 创建 | `fork()` | `pthread_create()` |
| 标识 | `getpid()` → `pid_t` | `pthread_self()` / `pthread_t` |
| 结束自己 | `exit()` | `return` 从 start 例程 / `pthread_exit()` |
| 等待并收结果 | `waitpid()` | `pthread_join()` |
| 交换数据 | IPC | 指向共享对象的指针 |

### 1.3 `pthread_create` / `pthread_join`

```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine)(void *), void *arg);
int pthread_join(pthread_t thread, void **retval);
```

典型模式:

```c
pthread_t t1, t2;
pthread_create(&t1, NULL, worker, &arg1);
pthread_create(&t2, NULL, worker, &arg2);
pthread_join(t1, NULL);
pthread_join(t2, NULL);
```

- **先都 create, 再都 join**: 才能真正并行
- 若 create–join–create–join 串起来, 第二个 worker 要等第一个完全结束, **假并行**

### 1.4 返回值与局部变量 (高频坑)

`pthread_join` 拿到的 `retval` 是线程 start 例程 `return` 的指针.

**不要** `return &local;` — join 时该栈帧已销毁, 悬空指针.

正确思路:

- 返回堆上 `malloc` 的结果 (由 join 方 `free`), 或
- 通过 `arg` 指向的共享结构写结果, `return NULL`

### 1.5 `pthread_cancel` (了解)

- 请求取消另一线程; 默认在 **cancellation point** (如 `pthread_testcancel`, 某些阻塞调用) 才真正退出
- PA/考试以课件范围为准; MiniLab4 重点在 race + mutex, 不在 cancel 细节

---

## 2. Part II — Mutexes

### 2.1 丢失更新 (lost update)

两线程各执行 `counter++` 一百万次, 期望 `2000000`, **无锁时常更少**.

原因: `counter++` 在机器上通常是

```text
read  counter → reg
add   1
write reg → counter
```

交错例:

```text
T1 read 0
T2 read 0
T1 write 1
T2 write 1   ← 丢了一次增加
```

这是 **data race** / 临界区无互斥.

### 2.2 `pthread_mutex_lock` / `unlock`

```c
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER; // 或 pthread_mutex_init

pthread_mutex_lock(&m);
// 临界区: 读写共享数据
pthread_mutex_unlock(&m);
```

- 同时只有一个线程能持锁进入临界区
- 另一线程在 `lock` 处阻塞等待
- **多相关变量** (如 `processed` 与 `remaining`) 应用**同一把锁**保护, 否则仍可能看到不一致快照

### 2.3 `pthread_mutex_trylock`

- 拿不到锁 → **立即返回错误**, 不阻塞
- 用途: 锁忙时先去做无关工作 B, 稍后再试

### 2.4 生命周期

`init` (或静态初始化) → 使用 → **所有线程都不再用该锁之后** → `pthread_mutex_destroy`.

---

## 3. Part III — Condition Variables

### 3.1 问题设定 (课件典型)

main 要等两个 worker 各自写完数组切片, **且**可能还有「后续还有没有工作」之类状态.  busy-wait 空转浪费 CPU; 需要「条件不满足就睡, 满足再醒」.

### 3.2 三件套

1. **共享状态**: 如 `bool done[2]`
2. **mutex**: 保护对 `done` (及任何相关共享量) 的读写
3. **condition variable**: `pthread_cond_t`

### 3.3 `pthread_cond_wait` 语义

```c
pthread_cond_wait(&cv, &mutex);
```

原子地:

1. **释放** mutex
2. 线程睡眠, 等待被 signal/broadcast
3. 被唤醒后 **重新获取** mutex, 再返回

因此: **调用 wait 前必须已持有该 mutex**; wait 返回后仍持有 mutex.

### 3.4 Worker / Main 典型写法

Worker 写完切片:

```c
pthread_mutex_lock(&m);
done[i] = true;
pthread_cond_signal(&cv);   // 或 broadcast
pthread_mutex_unlock(&m);
```

Main:

```c
pthread_mutex_lock(&m);
while (!(done[0] && done[1])) {
    pthread_cond_wait(&cv, &m);
}
pthread_mutex_unlock(&m);
```

### 3.5 为什么必须是 `while` 而不是 `if`

1. **虚假唤醒 (spurious wakeup)**: 可能「醒了但条件仍假」
2. **只完成一半**: 一个 worker signal 时, 另一个 `done` 仍为 false
3. 醒来后应用**最新**共享状态再判断

规则: **`wait` 一定包在 `while (!条件)`` 里.**

`signal` vs `broadcast`:

- `signal`: 至少唤醒一个等待者 (够用时更轻)
- `broadcast`: 唤醒所有等待者 (多个 waiter 等同一条件变化时常用)

---

## 4. Recap 速查

| 目标 | 调用 |
|---|---|
| 启动 worker | `pthread_create` |
| 结束自己 | `return` / `pthread_exit` |
| 等待并收结果 | `pthread_join` |
| 保护共享读写 | `pthread_mutex_lock` / `unlock` |
| 等到状态就绪 | `while (!cond) pthread_cond_wait` + `signal`/`broadcast` |

检查每个 pthread 调用的返回值; **参数与共享对象在所有使用者结束前保持存活**.

---

## 5. 参考附录 (slides)

### A. C11 atomics

`<stdatomic.h>` 的 `atomic_fetch_add` 等可保护**单个计数器**增减, 与 Pthread mutex API 独立. 复杂不变量仍常用锁.

### B. local vs static

- 函数内普通 `int i`: 每次调用一份 (多线程各调各的 → 各有栈上 `i`)
- `static int total`: 函数间共享**同一**全局寿命对象 → 多线程读写必须同步

### C. Cancellation

默认 enabled; 在 cancellation point 处理. 细节见 man `pthread_cancel`.

---

## 6. 与 Lec / Lab / 后续作业

| 材料 | 关系 |
|---|---|
| Lec07 Thread | 线程抽象, 共享地址空间 |
| Lec08 Synchronization | 锁, 条件变量, 临界区 |
| OSTEP Ch.26–27 | threads intro / API |
| OSTEP Ch.28 / 30 | locks / CV |
| MiniLab4 | pthread race → 加锁 |
| PA2 (预期) | 多线程计算 + 同步 |

---

## 7. 建议自测

1. 两线程无锁各 `++` 一百万次, 观察最终值是否总是 2000000.
2. 给 `counter++` 加 mutex, 再跑, 确认正确.
3. 用 `done[]` + CV 让 main 等到两个 worker 都完成再打印, 确认用的是 `while` 不是 `if`.
