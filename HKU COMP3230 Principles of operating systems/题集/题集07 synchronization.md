# 题集 — Synchronization

> 对齐: `Lec/Lec08 synchronization 讲义.md` 与 OSTEP Ch.28, Ch.30, Ch.31.

---

## 课件证明

### P1. Test-and-Set 实现互斥的正确性

- **陈述**: `int flag=0; while (TestAndSet(&flag,1)==1); /* CS */ flag=0;` 实现了互斥.
- **证明**: `TestAndSet` 原子地读旧值并置新值。无人持锁时 `flag=0`, `TestAndSet` 返回 0 且置 `flag=1` → 获锁进入 CS。有人持锁时 `flag=1`, 返回 1 → 继续自旋。只有一个线程能把 `flag` 从 0 原子地改成 1, 故至多一个线程在 CS。
- **来源**: 讲义 §3.1

### P2. Compare-and-Swap 实现互斥的正确性

- **陈述**: `while (CompareAndSwap(&flag,0,1)); /* CS */ flag=0;` 实现了互斥。
- **证明**: CAS 仅当 `flag==0` (expected) 时才置为 1, 整条原子。`flag=0` 时 CAS 返回 0 (假) → 退出循环获锁; `flag=1` 时 CAS 返回 1 (真) → 继续循环。互斥性同 P1。
- **来源**: 讲义 §3.2

### P3. 自旋锁在单核上会死锁 (自拟)

- **假设**: 单核; 线程 T1 持锁进入 CS, T2 自旋等锁。
- **结论**: T1 持锁但被调度器切走 (时间片到), T2 获得 CPU 但只能自旋等 T1 释放; T1 永远拿不回 CPU → T2 永远自旋 → 死锁。
- **来源**: 讲义 §3.3

### P4. `pthread_cond_wait` 必须用 `while` 而非 `if` (Mesa 语义)

- **假设**: 多消费者; CV `notEMPTY`; `cond_wait` 醒来后到重新获 mutex 返回之间, 其他消费者可能抢先取走数据。
- **结论**: 醒来后条件不一定仍成立, 须用 `while (count==0) cond_wait(...)` 重新检查; 若用 `if`, 会在池空时错误地执行 `take`。
- **来源**: 讲义 §6.3; 2023 Final Q5

### P5. 信号量解生产者-消费者: 先 wait 资源信号量再 wait mutex

- **陈述**: 正确顺序是 `sem_wait(&empty); sem_wait(&mutex);` 而非 `sem_wait(&mutex); sem_wait(&empty);`。
- **证明 (反例)**: 缓冲池满时 `empty=0, mutex=1`。若先 `sem_wait(&mutex)` 成功 (`mutex=0`) 再 `sem_wait(&empty)` 阻塞, 此时 Producer 持 mutex 等 empty。Consumer 想取数据须 `sem_wait(&mutex)` 但被 Producer 持有 → Consumer 也阻塞 → 循环等待 → 死锁。正确顺序: 先 `sem_wait(&empty)` (满时直接阻塞但不持 mutex), 再 `sem_wait(&mutex)`, 这样等资源时不锁住缓冲池。
- **来源**: 讲义 §11; Lec09 死锁四条件

### P6. 二值信号量等价于互斥锁

- **陈述**: 初值 1 的二值信号量行为等价于互斥锁。
- **证明**: `sem_wait` 减 1, 从 1→0 获锁; 他人 `sem_wait` 减到 -1 入队阻塞。`sem_post` 加 1, 从 0→1 并唤醒一个等待者。状态空间 {0,1}, 同 mutex 的 {held, available}。
- **来源**: 讲义 §7.2

---

## 练习题

### 1. 课件 Follow-up: 交换 sem_wait 顺序的后果

- **题目**: 生产者-消费者信号量解法中, 把 `sem_wait(&empty); sem_wait(&mutex);` 换成 `sem_wait(&mutex); sem_wait(&empty);` 会怎样?
- **思路**: 缓冲池满时死锁。Producer 持 mutex 等 empty; Consumer 等 mutex; 循环等待。见 P5。
- **来源**: `Lec08 synchronization` p.32–34

### 2. 读者-写者: 写者饥饿

- **题目**: 课件 §8 的读者优先解法中, 写者何时饥饿?
- **思路**: 只要不断有新读者到来, `readcount` 永不归 0, `semMutex` 永不释放, 写者永远等。
- **来源**: 讲义 §8

### 3. 顺序同步: Thread1 等 Thread2 与 Thread3

- **题目**: 用一个信号量让 Thread1 在 Thread2, Thread3 都完成后才执行 computation1。
- **思路**: `sem_t order; sem_init(&order,0,0);` Thread1 `sem_wait` 两次; Thread2/3 各完成计算后 `sem_post` 一次。
- **来源**: 讲义 §9

### 4. CV 解法中 `signal` vs `broadcast`

- **题目**: 一次放/取 k 个的有界缓冲, 为何 `signal` 不够须 `broadcast`?
- **思路**: 一次放 k 个后, 可能需要唤醒多个等待者 (如多个消费者); `signal` 只唤醒一个, 其余仍等; 用 `broadcast` 唤醒全部, 各自用 `while` 重新判断能否行动。
- **来源**: 2023 Final Q5; 讲义 §6.3

### 5. 关中断为何多核无效

- **题目**: 为何关中断只在单核有效?
- **思路**: 关中断只阻止本核调度; 多核下他核线程仍可进入同一 CS。
- **来源**: 讲义 §2.1
