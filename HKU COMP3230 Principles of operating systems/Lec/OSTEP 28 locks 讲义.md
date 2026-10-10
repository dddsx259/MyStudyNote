# OSTEP Ch.28 — Locks: 锁 (locks)

- **来源**: `Lec/OSTEP 28 locks.pdf` (22 页, Ch.28, 跳过 §28.10 / §28.11 / §28.15 / §28.16)
- **课程**: COMP3230B Principles of Operating Systems
- **必读范围**: §28.1–§28.9, §28.12–§28.14, §28.17 (按 `docs/给AI-final考点与生成约定.md`)
- **对齐 slides**: `Lec/Lec08 synchronization 讲义.md`

> 本章从「想原子地执行一串指令」出发, 逐步构造锁: 关中断 → 失败的 load/store → Test-and-Set 自旋锁 → CAS → yield → 队列+park。教材代码全部入库并附注释。术语首次标英文。

---

## 0. 一页速览

| 节 | 主题 | 要点 |
|---|---|---|
| §1 | 锁的基本思想 | `lock()`/`unlock()` 包住临界区; 锁状态 available/held |
| §2 | Pthread 锁 | `pthread_mutex_t`; 粗粒度 vs 细粒度锁 |
| §4 | 评估锁 | 正确性 (互斥) / 公平性 (无饥饿) / 性能 (无争用·单核·多核) |
| §5 | 关中断 | 简单; 多核无效; 信任问题; 中断丢失 |
| §6 | 失败的 load/store | flag 方案: 交错可双线程都进 CS; 自旋浪费 |
| §7 | Test-and-Set 自旋锁 | 原子「读旧+写新」; 正确; 无公平; 单核差多核好 |
| §8 | 评估自旋锁 | 单核持锁被抢占 → N−1 时间片全自旋; 多核短 CS 好 |
| §9 | Compare-and-Swap | 仅当 == expected 才更新; 比 TAS 更强 (后续 lock-free 用) |
| §12 | 自旋太多怎么办 | 硬件不够, 须 OS 支持 |
| §13 | yield | 自旋时让出 CPU; 比 spin 好; 100 线程仍开销大; 不解决饥饿 |
| §14 | 队列 + park/unpark | Solaris `park()`/`unpark()`; guard 自旋锁保护 flag+queue; `setpark()` 防 wakeup/waiting race |
| §17 | 总结 | 硬件原语 + OS 支持 = 现代锁 |

---

## 1. Locks: The Basic Idea (§28.1)

### 1.1 问题

并发编程的根本问题: 想原子地执行一串指令, 但单处理器上的中断 (或多核并行) 使其不可能。**锁 (lock)** 直接解决: 程序员在临界区 (critical section) 周围加锁, 使该段执行「如同单条原子指令」。

### 1.2 锁的语义

```c
lock_t mutex;              // 全局分配的锁变量
// ...
lock(&mutex);              // 获锁
balance = balance + 1;     // 临界区
unlock(&mutex);            // 释放
```

锁是一个 **变量**, 保存锁的状态:
- **available (unlocked / free)**: 无线程持有
- **acquired (locked / held)**: 恰一个线程持有, 该线程称 **owner**, 应在 CS 内

`lock()` 语义:
- 锁空闲 → 调用线程获锁, 成为 owner, 进入 CS
- 锁被他人持有 → `lock()` 不返回, 直到锁释放; 阻止其他线程进入 CS

`unlock()` 语义:
- 锁变回 free; 若无线程等待, 状态直接改 free
- 若有等待线程 (卡在 `lock()`), 其中一个会 (最终) 注意到状态变化, 获锁进入 CS

锁把调度的一部分控制权还给程序员: 包住一段代码就保证至多一个线程活跃其中。

---

## 2. Pthread Locks (§28.2)

POSIX 库把锁叫 **mutex** (mutual exclusion)。

```c
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
Pthread_mutex_lock(&lock);    // wrapper; 失败则退出
balance = balance + 1;
Pthread_mutex_unlock(&lock);
```

**粗粒度 vs 细粒度锁 (coarse-grained vs fine-grained locking)**:
- 粗粒度: 一把大锁管所有 CS → 简单但并发低
- 细粒度: 不同数据/结构用不同锁 → 并发高, 但须小心死锁与一致性

---

## 4. Evaluating Locks (§28.4)

评估一把锁的三个标准:

1. **正确性 (correctness)**: 是否提供互斥? 阻止多线程进入 CS?
2. **公平性 (fairness)**: 争用线程是否都有公平机会? 是否会 **饥饿 (starve)**?
3. **性能 (performance)**:
   - 无争用 (单线程反复加解锁): 开销多大?
   - 单 CPU 多线程争用: 开销?
   - 多 CPU 多线程争用: 开销?

---

## 5. Controlling Interrupts (§28.5)

最早期的方案: 在 CS 内 **关中断 (disable interrupts)**。

```c
void lock()   { DisableInterrupts(); }
void unlock()  { EnableInterrupts(); }
```

单处理器上, 关中断后 CS 不会被中断打断, 执行如同原子。

**优点**: 简单。

**缺点**:
1. **信任问题**: 允许任意调用线程执行特权操作 (开关中断); 贪婪程序 `lock()` 后垄断 CPU; 恶意程序 `lock()` 后死循环 → OS 永远拿不回控制, 只能重启
2. **多核无效**: 他核线程仍可进同一 CS
3. **中断丢失**: 长时间关中断会导致设备完成信号被错过 (如磁盘读完成), 系统出问题

**用途**: 仅在 OS 内部有限场景使用 (OS 信任自己); 不作通用同步方案。

---

## 6. 失败的尝试: 仅用 load/store (§28.6)

用单个 `flag` 变量指示锁是否被持有 (Figure 28.1):

```c
typedef struct __lock_t { int flag; } lock_t;

void init(lock_t *mutex) {
    mutex->flag = 0;                    // 0=可用, 1=持有
}

void lock(lock_t *mutex) {
    while (mutex->flag == 1)             // TEST: 测试 flag
        ;                                // spin-wait (空转)
    mutex->flag = 1;                     // SET: 置 1
}

void unlock(lock_t *mutex) {
    mutex->flag = 0;
}
```

### 6.1 正确性问题: 无互斥

交错 (Figure 28.2): `flag=0` 起始。

```
Thread 1                         Thread 2
call lock()
while (flag == 1)  // flag=0, 退出循环
interrupt: switch to Thread 2
                                 call lock()
                                 while (flag == 1)  // flag=0, 退出循环
                                 flag = 1           // 设 1
interrupt: switch to Thread 1
flag = 1;  // 也设 1 (两个都进了 CS!)
```

`test` 与 `set` 不是原子的 → 两线程都看到 `flag==0` 都设 1 → 都进 CS → **互斥失败**。

### 6.2 性能问题: 自旋浪费

等待方不断检查 `flag` (spin-waiting), 浪费 CPU; 单核上持锁线程没 CPU 跑不完 CS → 自旋者空耗整个时间片。

---

## 7. 用 Test-and-Set 构造自旋锁 (§28.7)

### 7.1 Test-and-Set 指令

```c
int TestAndSet(int *old_ptr, int new) {
    int old = *old_ptr;    // 取旧值
    *old_ptr = new;        // 写新值
    return old;            // 返回旧值
}
```

整条指令 **原子地** 完成上述三步。各架构叫法不同: SPARC `ldstub`, x86 `xchg`。

### 7.2 自旋锁实现 (Figure 28.3)

```c
typedef struct __lock_t {
    int flag;
} lock_t;

void init(lock_t *lock) {
    lock->flag = 0;                       // 0=可用, 1=持有
}

void lock(lock_t *lock) {
    while (TestAndSet(&lock->flag, 1) == 1)
        ;                                // spin-wait
}

void unlock(lock_t *lock) {
    lock->flag = 0;
}
```

### 7.3 正确性分析

- **场景 1 (锁空闲)**: `flag=0`, `TestAndSet(flag,1)` 返回旧值 0 → 不进 while → 获锁; 同时原子置 `flag=1`
- **场景 2 (锁被持有)**: `flag=1`, `TestAndSet` 返回旧值 1 → 进 while 自旋; 同时置 `flag=1` (无变化); 直到他人 `unlock` 置 `flag=0`, 本线程下次 `TestAndSet` 返回 0 → 获锁并置 1

**关键**: test 与 set 合为一条原子操作 → 只有一个线程能把 `flag` 从 0 原子地改成 1 → 互斥成立。

### 7.4 ASIDE: Peterson 算法 (历史)

不用硬件原子指令, 仅用 load/store 的两线程互斥算法 (Peterson, 1981):

```c
int flag[2];
int turn;

void init() {
    flag[0] = flag[1] = 0;
    turn = 0;
}

void lock() {
    flag[self] = 1;                       // 表示想持锁
    turn = 1 - self;                     // 让对方先
    while ((flag[1-self] == 1) && (turn == 1 - self))
        ;                                // 等轮到自己
}

void unlock() {
    flag[self] = 0;
}
```

`flag[i]` 表示线程 i 想进 CS; `turn` 决定两线程都想进时谁先。现代硬件的松散内存模型使这类纯 load/store 算法失效, 故实际都用硬件原子指令。

---

## 8. 评估自旋锁 (§28.8)

- **正确性**: ✅ 提供互斥
- **公平性**: ❌ 无公平保证, 可能饥饿
- **性能**:
  - 单 CPU: 持锁线程被抢占 → 其余 N−1 线程各自耗尽一个时间片自旋 → 浪费严重
  - 多 CPU (线程数 ≈ CPU 数): 自旋者在他核空转, CS 通常很短 → 锁很快释放 → 性能合理

自旋锁在单核上需 **抢占式调度** (timer 中断), 否则持锁线程永不释放 CPU, 自旋者永远等不到。

---

## 9. Compare-and-Swap (§28.9)

```c
int CompareAndSwap(int *ptr, int expected, int new) {
    int original = *ptr;
    if (original == expected)
        *ptr = new;
    return original;
}
```

仅当 `*ptr == expected` 时才更新为 `new`; 整条原子。SPARC 叫 `compare-and-swap`, x86 叫 `compare-and-exchange`。

用 CAS 构造锁:

```c
void lock(lock_t *lock) {
    while (CompareAndSwap(&lock->flag, 0, 1) == 1)
        ;                                // spin
}
```

检查 `flag==0` (expected) 时原子地置 1 → 获锁; 否则自旋。

**CAS 比 TAS 更强**: CAS 能做条件更新, 后续 lock-free 同步 (如无锁链表/队列) 用得上; 但只做简单自旋锁时行为与 TAS 版相同。

> §28.10 (Load-Linked/Store-Conditional) 与 §28.11 (Fetch-And-Add/ticket lock) 按课程约定跳过。

---

## 12. 自旋太多怎么办 (§28.12)

硬件自旋锁简单且正确, 但效率可能很差: 两线程单 CPU, T0 持锁被中断, T1 自旋整个时间片; N 线程时 N−1 时间片全浪费在自旋上。

**Crux**: 如何构造不浪费 CPU 自旋的锁? 硬件不够, 须 **OS 支持**。

---

## 13. 简单方案: yield (§28.13)

自旋时改调 `yield()` 让出 CPU (Figure 28.8):

```c
void init()  { flag = 0; }

void lock() {
    while (TestAndSet(&flag, 1) == 1)
        yield();                          // 让出 CPU
}

void unlock() { flag = 0; }
```

`yield()` 把调用线程从 running 转 ready, 调度另一个线程。

**分析**:
- 两线程单 CPU: 持锁线程能跑完 CS → 比自旋好
- 100 线程: 持锁者被抢占, 其余 99 各 `lock()` → `yield()` 一轮 → 99 次上下文切换开销仍大
- **不解决饥饿**: 某线程可能一直 yield 而他人反复进出 CS

---

## 14. 队列: 睡眠而非自旋 (§28.14)

真正问题: 之前方案把太多事交给调度器。须 **显式控制** 谁下一个获锁。用 **队列** 跟踪等待者 + OS 提供睡眠/唤醒原语。

Solaris 提供 `park()` (让调用线程睡眠) 与 `unpark(threadID)` (唤醒指定线程)。

### 14.1 锁实现 (Figure 28.9)

```c
typedef struct __lock_t {
    int flag;
    int guard;
    queue_t *q;
} lock_t;

void lock_init(lock_t *m) {
    m->flag = 0;
    m->guard = 0;
    queue_init(m->q);
}

void lock(lock_t *m) {
    while (TestAndSet(&m->guard, 1) == 1)
        ;                                // 自旋获 guard 锁
    if (m->flag == 0) {
        m->flag = 1;                     // 获锁
        m->guard = 0;
    } else {
        queue_add(m->q, gettid());       // 入队
        m->guard = 0;
        park();                           // 睡眠
    }
}

void unlock(lock_t *m) {
    while (TestAndSet(&m->guard, 1) == 1)
        ;                                // 自旋获 guard 锁
    if (queue_empty(m->q))
        m->flag = 0;                     // 无人等, 释放锁
    else
        unpark(queue_remove(m->q));       // 唤醒队首, 把锁直接传给它
    m->guard = 0;
}
```

### 14.2 关键设计点

1. **guard**: 一把自旋锁, 保护对 `flag` 与 `queue` 的操作 (临界区极短, 自旋代价可接受)
2. **获锁路径**: `guard` 内看 `flag==0` → 置 1 获锁; 否则入队 → 释放 `guard` → `park()` 睡眠
3. **释放路径**: `guard` 内看队列空 → `flag=0` 释放; 否则 `unark(队首)` 把锁直接传给队首 (不重置 `flag`, 因为被唤醒线程不在 `guard` 内, 无法设 `flag`)
4. **flag 不在唤醒时清 0**: 被唤醒线程从 `park()` 返回时不在 `guard` 内, 无法安全改 `flag`; 故把锁「直接传递」给下一个线程, `flag` 保持 1

### 14.3 wakeup/waiting race 与 setpark()

**问题**: 线程 A 即将 `park()` 前被切换; 持锁线程 B 此时 `unlock` 调 `unpark(A)`; A 回到 CPU 后调 `park()` → 但 `unpark` 已发生过 → A 永远睡下去。

**Solaris 解法**: `setpark()` — 在 `park()` 前调, 表示即将睡; 若期间有 `unpark` 到达, 后续 `park()` 立即返回:

```c
queue_add(m->q, gettid());
setpark();                              // 新增
m->guard = 0;
```

**另一解法**: 把 `guard` 传入内核, 让内核原子地「释放锁 + 让线程入队睡」。

### 14.4 ASIDE: 优先级反转 (priority inversion)

避免自旋锁的另一理由: **正确性**。T2 高优先级, T1 低优先级。T1 持自旋锁进 CS, T2 解阻塞后抢占 T1, 想获锁但 T1 持有 → T2 自旋永远等 (T1 没机会跑完 CS 释放)。三线程版更复杂: T3 最高, T1 最低, T1 持锁, T3 等 T1, 但 T2 (中) 抢占 T1 → T3 永远等。

**对策**: 避免 (自旋) 锁; **优先级继承 (priority inheritance)** (高优先级等低优先级时临时提升低者优先级让跑完 CS); 或所有线程同优先级。Mars Pathfinder 曾因优先级反转挂死。

> §28.15 (Linux futex) 与 §28.16 (两阶段锁) 按课程约定跳过。

---

## 17. Summary (§28.17)

现代锁 = **硬件原语** (Test-and-Set / CAS 等) + **OS 支持** (`park`/`unpark` on Solaris, `futex` on Linux)。细节高度调优, 见 Solaris/Linux 源码。单一通用锁难满足所有场景, 故有不同变体 (自旋锁、队列锁、两阶段锁等)。

---

## Homework 要点 (x86.py 模拟)

- `flag.s`: 单 flag 锁 (§6 失败方案); 中断频率 `-i` 改变可观察到双线程都进 CS
- `test-and-set.s`: 用 `xchg` 实现自旋锁 (§7); 单核上持锁被抢占会自旋浪费
- `peterson.s`: Peterson 算法 (§7 ASIDE); 用 `-a bx=0,bx=1` 设线程 ID
- `ticket.s`: ticket lock (§11, 跳过); 观察自旋时间
- `yield.s`: yield 方案 (§13); 与 `test-and-set.s` 对比节省的指令
- `test-and-test-and-set.s`: test 后才 test-and-set, 减少写争用
