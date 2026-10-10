# Synchronization: 同步 (synchronization)

- **来源**: `Lec/Lec08 synchronization.pdf` (34 页)
- **课程**: COMP3230B Principles of Operating Systems
- **学习成果**: ILO 2c (并发与同步原理); ILO 4 (系统工具)
- **必读**: OSTEP Ch.28 Locks (除 §28.10, §28.11, §28.15, §28.16); Ch.30 Condition Variables; Ch.31 Semaphores
- **对齐阅读讲义**: `OSTEP 28 locks 讲义.md` / `OSTEP 30 condition variables 讲义.md` / `OSTEP 31 semaphores 讲义.md` (待生成)

> 本讲在 Lec07 竞态/临界区基础上, 给出三类同步原语: 锁 (lock), 条件变量 (condition variable), 信号量 (semaphore), 并用生产者-消费者 (producer-consumer) 与读者-写者 (readers-writers) 两个经典问题演示用法. 术语首次标英文.

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| 互斥 (mutual exclusion) | 临界区 (critical section) 至多一个线程; 用锁保护 |
| 硬件原子指令 | Test-and-Set / Compare-and-Swap; 可在多核共享内存上实现 spin-lock |
| 自旋锁 (spin-lock) | 忙等 (busy waiting), 浪费 CPU, 无公平保证 |
| OS 支持: Pthread mutex | `pthread_mutex_t` + `lock`/`unlock`; 不可用时阻塞 (blocked) |
| 条件变量 (condition variable, CV) | 等待某条件成立; `wait` 阻塞, `signal`/`broadcast` 唤醒; 配合 mutex |
| 信号量 (semaphore) | 整数 + `sem_wait`/`sem_post`; 二值当锁, 计数管资源池, 也可做顺序同步 |
| 生产者-消费者 (bounded buffer) | CV 版用 `while` + `notFULL`/`notEMPTY`; 信号量版用 `empty`/`full`/`mutex` |
| 读者-写者 (readers-writers) | 读者并发, 写者独占; 用 `readcount` + 两把二值信号量 |
| 顺序同步 (order of execution) | 信号量初始化为 0, 完成方 `post`, 等待方 `wait` |

---

## 1. 互斥与锁的概念 (p.5–6)

### 1.1 为什么需要锁

竞态 (race condition) 的根因是 **不受控调度 (uncontrolled scheduling)**: 多线程进入同一临界区 (critical section, CS) 修改共享数据, 结果依赖交错次序。需要一个机制告诉 OS 线程即将进入 CS, 让系统提供保护。

### 1.2 锁 (lock)

**锁 (lock)**: 一种数据结构, 标记临界区的开始与结束, 指示共享数据即将被访问并请求系统保护。

- 锁有两种状态: **可用 (available / free / unlocked)** 或 **被持有 (held / locked / acquired)**
- 线程想访问共享数据 → 调 `acquire(lock)` (即 `lock`):
  - 若锁空闲 → 获得锁, 成为 owner, 进入 CS
  - 若锁被他人持有 → 不返回, 等到锁释放后再获得并进入 CS
- owner 退出 CS 时调 `unlock(lock)` 释放

```
Thread 1              Thread 2
acquire LOCK()        acquire LOCK()
  x++                   (等待)
unlock LOCK()         (获得锁)
  x += 5              unlock LOCK()
```

---

## 2. 构造锁: 关中断与原子指令 (p.7–8)

### 2.1 关中断 (disabling interrupts)

思路: 在 CS 内关掉中断, 调度器就不会被触发, 当前线程不会被抢占。

```c
/* lock() */    disable interrupts
/* unlock() */  enable interrupts
```

**局限**:
- **只在单核 (single core) 有效** — 多核下另一核上的线程仍可进入 CS
- 用户态程序不应也不能随意关中断; 多用于内核特权态
- 关中断时间过长会导致系统无法响应外部事件

### 2.2 硬件原子指令 (atomic instructions)

现代 CPU 提供特殊的 **原子硬件指令 (atomic hardware instruction)**, 保证整条指令执行期间不被中断。本讲介绍两条:

#### Test-and-Set

```c
int TestAndSet(int *ptr, int new) {
    int old = *ptr;     // 取当前值
    *ptr = new;         // 设为新值
    return old;         // 返回旧值
}
```

整条指令 **原子地** 完成「读旧值 + 写新值 + 返回旧值」。

#### Compare-and-Swap (CAS)

```c
void CompareAndSwap(int *ptr, int expected, int new) {
    int temp = *ptr;    // 取当前值
    if (temp == expected)
        *ptr = new;     // 仅当等于期望值时才更新
    return temp;        // 返回当前值
}
```

仅当变量当前值等于 `expected` 时才更新为 `new`; 否则不动。整条原子。Intel IA-32/IA-64 上对应 `CMPXCHG` 指令。

---

## 3. 自旋锁 (Spin-Lock) (p.9–11)

### 3.1 用 Test-and-Set 实现互斥

```c
int flag = 0;                          // flag=0 表示锁空闲
while (TestAndSet(&flag, 1) == 1)      // lock(): 自旋等待
    ;                                  // 返回旧值=1 说明他人持有, 继续转
// 进入临界区
flag = 0;                              // unlock()
```

**工作原理**:
- 无人持锁时 `flag=0`, `TestAndSet` 返回 0 并原子地置 `flag=1` → 获锁进入 CS
- 有人持锁时 `flag=1`, `TestAndSet` 返回 1 → 继续自旋

**互斥保证**: 只有一个线程能把 `flag` 从 0 原子地改成 1 并进入 CS; 其余线程看到 `flag=1` 只能自旋等其变回 0。

### 3.2 用 Compare-and-Swap 实现

```c
int flag = 0;                          // 锁空闲
while (CompareAndSwap(&flag, 0, 1))    // 期望 0, 想设 1
    ;                                  // 返回非 0 (即当前=1) 说明他人持有
// 临界区
flag = 0;                              // 释放
```

### 3.3 自旋锁的问题

- **忙等 (busy waiting / spin-wait)**: 处理器空转执行 `while` 循环, **浪费 CPU 时间**; 自旋线程可能就把时间片耗尽
- **无公平保证**: 不能避免 **无限期推迟 (indefinite postponement)** — 两线程 T1, T2 争锁时, 调度器若总偏向 T1, T2 可能永远拿不到锁 (饥饿)
- 多核共享内存上可用; 单核上自旋会死锁 (持锁线程没 CPU 跑不完 CS)

### 3.4 原子指令不够 (Crux)

**Crux**: 如何构造一把 **不浪费 CPU 自旋** 且 **保持公平** 的锁? 答案: **需要 OS 支持** — 让等待线程进入阻塞状态, 释放 CPU, 由锁的持有者在解锁时唤醒。

---

## 4. Pthread 互斥锁 (p.13)

POSIX Pthreads 提供 OS 支持的锁, 类型 `pthread_mutex_t` (mutex = mutual exclusion)。

```c
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;  // 静态初始化
pthread_mutex_lock(&mutex);     // 获锁; 不可用时调用线程被阻塞 (blocked)
// 临界区
pthread_mutex_unlock(&mutex);   // 释放; 唤醒一个等待者
pthread_mutex_destroy(&mutex); // 用完销毁
```

**关键**: 当锁不可用时, OS 把调用线程转为 **阻塞状态 (blocked)**, 不再占用 CPU; 解锁时由 OS 唤醒一个等待线程。这解决了自旋锁浪费 CPU 的问题。

---

## 5. 控制同步与条件变量 (p.14–17)

### 5.1 控制同步 (control synchronization)

另一类线程交互: 线程 A 必须在 **其他线程完成特定动作或检测到某条件** 之后才能继续。A 要 **等待**, 他线程要 **通知 (signal)** A。

简单做法: A 自旋等条件变真 — 但 **低效且浪费 CPU** (busy wait on condition)。

### 5.2 条件变量 (condition variable, CV)

**条件变量 (condition variable)**: 专为线程间同步设计的数据类型, 不浪费 CPU:
- 内部维护一个 **等待队列 (queue)**, 等待某条件/事件的线程在此排队
- 某线程检测到条件成立后, 调 `signal` 唤醒一个等待线程 (或 `broadcast` 唤醒全部)
- 每个条件变量关联一个 **特定的条件/事件**

课件比喻 (p.16): 你有牛排但没刀叉 → 在「等刀叉」队列排队 → 服务员备好刀叉 → 唤醒你 → 享用。

### 5.3 Pthread CV 接口

```c
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
pthread_cond_wait(&cond, &mutex);       // 阻塞等待 (须持锁; 见下)
pthread_cond_signal(&cond);             // 唤醒一个等待者
pthread_cond_broadcast(&cond);          // 唤醒全部等待者
pthread_cond_destroy(&cond);
```

**`pthread_cond_wait(&cond, &mutex)` 的关键语义** (课件未展开, 但 Final 常考):
- 调用时必须 **持有 `mutex`**
- 调用原子地: 释放 `mutex` + 把当前线程加入 `cond` 等待队列 + 阻塞
- 被 `signal` 唤醒时: 重新获取 `mutex` 后返回 (因此 `wait` 返回后仍持锁)
- 醒来后 **条件不一定仍成立** (Mesa 语义, 见下), 故须用 `while` 重新检查

---

## 6. 生产者-消费者问题 (Producer-Consumer / Bounded Buffer) (p.18–21)

### 6.1 问题设定

**生产者-消费者问题 (producer-consumer problem)**, 又称 **有界缓冲问题 (bounded-buffer problem)**:
- 有限缓冲池 (finite buffer pool) 被多个生产者与多个消费者共享
- 每个缓冲区容纳一个数据单元
- **生产者 (producer)** 生成数据放入下一个可用缓冲区
- **消费者 (consumer)** 从缓冲区取出数据处理

### 6.2 同步要求

- 缓冲池是共享资源, 须协调访问
- 缓冲池满时, 生产者 **不能覆盖** (要等有空位)
- 缓冲池空时, 消费者 **不能取空** (要等有数据)
- 互斥: 同一时刻至多一个线程操作缓冲池
- FIFO: 信息按先进先出消费

### 6.3 CV 解法 (p.20–21)

```c
buffer[sizeofbuffer];
mutex_t mv;
cond_t notFULL, notEMPTY;
count = 0;

Producer() {
    while (1) {
        d = generating_data();
        lock(mv);
        while (count == sizeofbuffer)        // 池满
            cond_wait(notFULL, mv);          // 等空位 (释放 mv, 阻塞)
        append(d, buffer);                   // 入缓冲, count++
        cond_signal(notEMPTY);               // 通知「有数据」
        unlock(mv);
        remaining_work();
    }
}

Consumer() {
    while (1) {
        lock(mv);
        while (count == 0)                    // 池空
            cond_wait(notEMPTY, mv);          // 等数据 (释放 mv, 阻塞)
        d = take(buffer);                     // 出缓冲, count--
        cond_signal(notFULL);                 // 通知「有空位」
        unlock(mv);
        consume_data(d);
        remaining_work();
    }
}
```

**为什么用 `while` 而非 `if` (Mesa 语义 / spurious wakeup)**:
- 被 `signal` 唤醒后, 在重新获取 `mutex` 并返回前, 另一个消费者可能已抢先取走最后一个数据 → 条件 `count > 0` 不再成立
- 故必须 **重新检查** 条件, 用 `while` 循环再判断; 若用 `if` 则会在池空时错误地继续执行 `take`
- 这正是 2023 Final Q5 改代码题要的 `while` + `broadcast` 模式 (一次放/取 k 个时, 单个 `signal` 不够, 须 `broadcast` 唤醒所有等待者重新判断)

---

## 7. 信号量 (Semaphore) (p.22–26)

### 7.1 定义

**信号量 (semaphore)**: 另一种同步工具, 既可当锁, 也可做控制同步。是一个含 **受保护整数变量 (protected integer variable)** 的对象, 只能通过两条 **原子操作** 访问:

```c
sem_t k;
sem_init(&k, 0, x);    // 初始化为 x

sem_wait(&k) {          // P() / wait / down
    decrement k by 1;
    if k < 0
        place thread in k's waiting queue;   // 阻塞
}

sem_post(&k) {          // V() / signal / up
    increment k by 1;
    if any threads waiting on k's queue
        wake up one thread;
}
```

- `sem_wait` 也叫 **P()** (proberen, 荷兰语「测试」) / `wait` / `down`
- `sem_post` 也叫 **V()** (verhogen, 荷兰语「增加」) / `signal` / `up`

### 7.2 二值信号量 = 互斥锁 (p.24)

**二值信号量 (binary semaphore)**: 只能取 0 或 1, 行为像互斥锁, 同一时刻只允许一个线程进入 CS。

```c
sem_t lock;
sem_init(&lock, 0, 1);                  // 初始为 1 (空闲)

// Thread 1 / 2 / 3 同构:
while (1) {
    sem_wait(&lock);                     // 获锁 (lock=0)
    // 临界区
    sem_post(&lock);                     // 释放 (lock=1, 或唤醒队列中一个)
}
```

课件图示三线程争用: `lock=1` → `lock=0` (一人获) → 其余 `lock=0 (q=1)` / `lock=0 (q=2)` 排队 → 释放后唤醒一个。

### 7.3 计数信号量 (counting / general semaphore) (p.29)

**计数信号量 (counting semaphore)**: 初值设为资源池大小, 用于管理 **同类多个资源**:
- 取资源: `sem_wait(&pool)` (减 1; 若 <0 排队)
- 还资源: `sem_post(&pool)` (加 1; 若有等待者唤醒一个)
- 无资源时线程阻塞, 直到有资源归还

### 7.4 信号量解生产者-消费者 (p.25–26)

```c
sem_t empty;  sem_init(&empty,  0, MAX);   // 空位数
sem_t full;   sem_init(&full,   0, 0);     // 已填数
sem_t mutex;  sem_init(&mutex, 0, 1);      // 互斥锁

Producer() {
    while (1) {
        d = generating_data();
        sem_wait(&empty);                  // 占一个空位
        sem_wait(&mutex);                  // 进 CS
        append(d, buffer);
        sem_post(&mutex);                  // 出 CS
        sem_post(&full);                   // 增一个已填
        remaining_work();
    }
}

Consumer() {
    while (1) {
        sem_wait(&full);                   // 占一个已填
        sem_wait(&mutex);                  // 进 CS
        d = take(buffer);
        sem_post(&mutex);                  // 出 CS
        sem_post(&empty);                  // 增一个空位
        remaining_work();
    }
}
```

三信号量分工: `empty`/`full` 管空位数/已填数 (计数信号量), `mutex` 保护对 buffer 的修改 (二值信号量)。

---

## 8. 读者-写者问题 (Readers-Writers Problem) (p.27–28)

### 8.1 问题设定

**读者-写者问题 (readers-writers problem)**: 另一个经典同步问题。一组线程访问共享数据:
- **读者 (readers)**: 只读数据
- **写者 (writers)**: 修改数据

典型场景: 数据库访问, 链表更新与查找。

### 8.2 同步要求

- 多个读者可 **并发读**
- 写者更新时, **禁止读**
- 任意时刻 **至多一个写者**

### 8.3 二值信号量解法 (p.28)

```c
Semaphore semMutex = 1;    // 保护对共享数据的访问
Semaphore readMutex = 1;  // 保护对 readcount 的修改
int readcount = 0;

Writer() {
    StartWrite();
    do_writing();
    EndWrite();
}
Reader() {
    StartRead();
    do_reading();
    EndRead();
}

StartRead() {
    P(readMutex);           // 独占 readcount
    readcount++;
    if (readcount == 1)     // 第一个读者要锁住数据
        P(semMutex);
    V(readMutex);           // 释放 readcount
}
EndRead() {
    P(readMutex);
    readcount--;
    if (readcount == 0)    // 最后一个读者解锁数据
        V(semMutex);
    V(readMutex);
}
StartWrite() { P(semMutex); }
EndWrite()   { V(semMutex); }
```

**要点**:
- `readcount` 记录当前读者数; `readMutex` 保护对它的修改
- **第一个读者** (`readcount==1`) 调 `P(semMutex)` 锁住数据, 之后来的读者只需更新计数即可并发读
- **最后一个读者** (`readcount==0`) 调 `V(semMutex)` 释放数据, 让写者能进
- 写者只需对 `semMutex` 做 P/V, 与「第一个/最后一个读者」互斥

**潜在问题 (课件未展开, 但 Final 易考)**: 此解法 **偏向读者** — 只要不断有新读者到来, `readcount` 永不归 0, 写者会饥饿。OSTEP/标准课会讨论写者优先变体。

---

## 9. 顺序同步 (Synchronization between threads) (p.30)

### 9.1 用信号量约束执行顺序

信号量也可用于通知「某事件/条件已发生」, 从而控制线程间的 **执行顺序 (order of execution)**。

例: Thread1 须等 Thread2 与 Thread3 都完成各自任务后才能继续。

```c
sem_t order;
sem_init(&order, 0, 0);   // 初始化为 0

Thread1:                   Thread2:                  Thread3:
    :                          :                        :
    sem_wait(&order);          computation2();          computation3();
    sem_wait(&order);          sem_post(&order);         sem_post(&order);
    computation1();           :                        :
    :                          :                        :
```

**机制**: `order` 初始为 0。Thread2, Thread3 各完成自己的计算后 `post` (各加 1)。Thread1 须 `wait` 两次 (各减 1, 减到 0 才通过), 即等两个 `post` 都发生后才执行 `computation1()`。这把「Thread1 在 Thread2/3 之后」的顺序约束用信号量表达出来。

---

## 10. Summary (p.31)

- 避免竞态, 临界区至多一个线程 → 用 **互斥原语 (mutual exclusion primitive)**: mutex lock 或 binary semaphore
- 自旋锁在单核上忙等代价高 → 用 OS 支持的锁让线程 **阻塞** 释放 CPU
- 条件变量提供 **非忙等 (non-busy waiting)** 机制: 线程睡眠等他人唤醒
- 信号量既支持 **同步 (synchronization)** 又支持 **互斥 (mutual exclusion)**, 灵活强大

---

## 11. Follow-up: 交换 sem_wait 顺序的后果 (p.32–34)

课件末尾给出一个 **Follow-up Question**: 如果把生产者/消费者中 `sem_wait` 的顺序交换, 会怎样?

### 11.1 原始 (正确) 顺序

```c
// Producer
sem_wait(&empty);    // 先占空位
sem_wait(&mutex);    // 再进 CS
append(d, buffer);
sem_post(&mutex);
sem_post(&full);
```

### 11.2 交换后 (危险) 顺序

```c
// Producer (交换后)
sem_wait(&mutex);    // 先进 CS
sem_wait(&empty);   // 再占空位
append(d, buffer);
sem_post(&full);
sem_post(&mutex);
```

### 11.3 后果: 死锁 (deadlock)

考虑缓冲池已满 (`empty=0, full=MAX, mutex=1`) 时:
- Producer 调 `sem_wait(&mutex)` → 成功, `mutex=0`
- Producer 调 `sem_wait(&empty)` → `empty=0`, 阻塞, 但 **仍持有 `mutex`**
- 此时 Consumer 想取数据: `sem_wait(&full)` 成功, 但 `sem_wait(&mutex)` → `mutex=0` 被 Producer 持有 → Consumer 也阻塞
- Producer 等 `empty` (要 Consumer 取走一个), Consumer 等 `mutex` (要 Producer 释放) → **循环等待 (circular wait)** → **死锁**

**关键教训**:
- **先获取资源信号量 (`empty`/`full`), 再获取互斥锁 (`mutex`)** — 这样在等资源时不会占住 CS 锁
- 若反过来先拿 `mutex` 再等资源, 就会在等资源时「锁住」整个缓冲池, 阻止他人释放资源 → 死锁
- 这正是 Lec09 Deadlock 的伏笔: 信号量顺序错用会产生死锁的四条件之一 (hold-and-wait / circular wait)

> 详细死锁四条件与银行家算法见 `Lec/Lec09 deadlock 讲义.md`。
