# OSTEP Ch.30 — Condition Variables: 条件变量 (condition variables)

- **来源**: `Lec/OSTEP 30 condition variables.pdf` (19 页, Ch.30)
- **课程**: COMP3230B Principles of Operating Systems
- **对齐 slides**: `Lec/Lec08 synchronization 讲义.md`

> 锁不够: 很多场景线程要等某条件成立再继续 (如 parent 等 child 完成)。本章引入 **条件变量 (condition variable, CV)**, 用 `wait`/`signal` 让线程睡眠/唤醒而非自旋。教材代码全部入库并附注释。术语首次标英文。

---

## 0. 一页速览

| 节 | 主题 | 要点 |
|---|---|---|
| §1 | CV 定义与例程 | `pthread_cond_t`; `wait` 原子释放锁+睡, 醒来重获锁; `signal` 唤醒一个 |
| §1 | join 例 | 状态变量 `done` 必要; 持锁 signal; `while` 非 `if` |
| §2 | 生产者/消费者 v1 (单 CV + if) | Mesa 语义: 醒来后状态可能已变 → 互斥失败 |
| §2 | v2 (单 CV + while) | 修了 if, 但单 CV 会唤醒同类线程 → 全体睡死 |
| §2 | v3 (两 CV + while) | `empty`/`fill` 分别给 producer/consumer; 正确 |
| §2 | 最终版 (多 slot buffer) | `fill_ptr`/`use_ptr` 环形; `count` 判满/空 |
| §3 | 覆盖条件 | `broadcast` 唤醒所有等待者; 各自 `while` 重判 |
| §4 | 总结 | CV = 锁之外的另一重要原语 |

---

## 1. Definition and Routines (§30.1)

### 1.1 问题: 等待条件

线程常需等某条件成立再继续 (parent 等 child 完成 = `join()`)。自旋等 (Figure 30.2) 浪费 CPU, 且有时不正确。

### 1.2 条件变量定义

**条件变量 (condition variable, CV)**: 一个显式队列, 线程在条件不满足时把自己挂上去等 (wait); 他线程改变状态后唤醒一个等待者 (signal)。源自 Dijkstra 的「私有信号量」与 Hoare 的 monitor。

```c
pthread_cond_t c;                    // 声明 (须初始化)
pthread_cond_wait(pthread_cond_t *c, pthread_mutex_t *m);
pthread_cond_signal(pthread_cond_t *c);
```

### 1.3 `wait` 的关键语义

`wait(c, m)` 调用时 **必须持锁 `m`**; 调用原子地:
1. 释放锁 `m`
2. 把调用线程挂到 `c` 的等待队列并睡眠

被 `signal` 唤醒后:
3. 重新获取锁 `m`
4. 返回 (返回时仍持锁)

### 1.4 join 例 (Figure 30.3)

```c
int done = 0;
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t c = PTHREAD_COND_INITIALIZER;

void thr_exit() {
    Pthread_mutex_lock(&m);
    done = 1;
    Pthread_cond_signal(&c);
    Pthread_mutex_unlock(&m);
}

void *child(void *arg) {
    printf("child\n");
    thr_exit();
    return NULL;
}

void thr_join() {
    Pthread_mutex_lock(&m);
    while (done == 0)
        Pthread_cond_wait(&c, &m);    // 释放 m, 睡; 醒来重获 m
    Pthread_mutex_unlock(&m);
}

int main(int argc, char *argv[]) {
    printf("parent: begin\n");
    pthread_t p;
    Pthread_create(&p, NULL, child, NULL);
    thr_join();
    printf("parent: end\n");
    return 0;
}
```

**两种执行顺序**:
- parent 先到 `thr_join`: 获锁, `done==0`, `wait` 释放锁睡; child 后跑 `thr_exit`: 获锁, `done=1`, `signal` 唤醒 parent; parent 醒来重获锁, 退出
- child 先到 `thr_exit`: `done=1`, `signal` (无人等, 直接返回); parent 后到 `thr_join`: `done==1`, 不 `wait`, 直接返回

### 1.5 状态变量 `done` 必要

去掉 `done` (Figure 30.4): child 先跑 `signal` 时无人等; parent 后到 `wait` 永远睡。**状态变量记录线程关心的值**, 睡眠/唤醒/加锁都围绕它。

### 1.6 不持锁 signal/wait 的竞态 (Figure 30.5)

```c
void thr_exit() {
    done = 1;                       // 不持锁
    Pthread_cond_signal(&c);
}
void thr_join() {
    if (done == 0)
        Pthread_cond_wait(&c);      // 不持锁 (假设接口允许)
}
```

parent 检查 `done==0` 后, 调 `wait` 前, 被中断; child 跑 `thr_exit`: `done=1`, `signal` (无人等); parent 回到 CPU 调 `wait` → 永远睡。

**TIP: 持锁 signal, 持锁 wait** — `wait` 的语义本就要求持锁 (释放+睡+重获); signal 也建议持锁, 简单且正确。

### 1.7 为何用 `while` 非 `if`

逻辑上 join 例中 `while` 看似不必要 (只有两个线程), 但始终是好习惯: 醒来后条件可能已变 (Mesa 语义, 见 §2), 须重新检查。

---

## 2. Producer/Consumer (Bounded Buffer) (§30.2)

### 2.1 单 slot buffer 的 put/get (Figure 30.6)

```c
int buffer;
int count = 0;                       // 0=空, 1=满

void put(int value) {
    assert(count == 0);
    count = 1;
    buffer = value;
}

int get() {
    assert(count == 1);
    count = 0;
    return buffer;
}
```

producer 放数据前须 `count==0` (空); consumer 取前须 `count==1` (满)。违反则 assertion 触发。

### 2.2 v1: 单 CV + if (Figure 30.8, 错误)

```c
int loops;
cond_t cond;
mutex_t mutex;

void *producer(void *arg) {
    int i;
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);          // p1
        if (count == 1)                       // p2
            Pthread_cond_wait(&cond, &mutex); // p3
        put(i);                              // p4
        Pthread_cond_signal(&cond);          // p5
        Pthread_mutex_unlock(&mutex);        // p6
    }
}

void *consumer(void *arg) {
    int i;
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);          // c1
        if (count == 0)                      // c2
            Pthread_cond_wait(&cond, &mutex); // c3
        int tmp = get();                      // c4
        Pthread_cond_signal(&cond);          // c5
        Pthread_mutex_unlock(&mutex);        // c6
        printf("%d\n", tmp);
    }
}
```

**单 producer 单 consumer 时工作; 两 consumer 时出错** (Figure 30.9 trace):
- Tc1 等 (c3 睡), Tp 放数据 `signal` 唤醒 Tc1 (Tc1 转 ready 但未运行), Tp 继续到满后睡
- **Tc2 抢入** (c1, c2 见 `count==1` 不 wait, c4 取走数据, c5 `signal` 唤醒 Tp, c6 释放锁)
- Tc1 终于运行, 从 `wait` 返回 (重获锁), 调 `get()` → **`count==0`, assertion 触发!**

**根因 (Mesa 语义)**: `signal` 只是「状态可能变了」的提示, 不保证醒来运行时状态仍如愿。Tc1 被唤后到真正运行前, Tc2 已抢走数据。

**Hoare 语义** 对比: 唤醒后立即切换到被唤线程运行, 保证状态不变; 但难实现, 几乎所有系统都用 Mesa 语义。

### 2.3 v2: 单 CV + while (Figure 30.10, 仍错)

把 `if` 改 `while`:

```c
void *producer(void *arg) {
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);
        while (count == 1)                    // while 非 if
            Pthread_cond_wait(&cond, &mutex);
        put(i);
        Pthread_cond_signal(&cond);
        Pthread_mutex_unlock(&mutex);
    }
}
// consumer 同理: while (count == 0) wait
```

**修了 v1 的问题**, 但仍有第二 bug (Figure 30.11 trace):
- 两 consumer Tc1, Tc2 都 `count==0` 睡; Tp 放数据 `signal` 唤醒 Tc1; Tp 继续到满后睡
- Tc1 醒来 `while` 重判 `count==1`, 取走数据, `signal` 唤醒 **一个** — 但可能唤到 Tc2 (而非 Tp)
- Tc2 醒来 `count==0` 再睡; Tp 仍睡; Tc1 也已睡 → **三个线程全睡, 死锁**

**根因**: 单 CV 让 consumer 可能唤 consumer, producer 可能唤 producer; 应 **定向** signal。

### 2.4 v3: 两 CV + while (Figure 30.12, 正确)

```c
cond_t empty, fill;                   // 两个 CV

void *producer(void *arg) {
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);
        while (count == 1)
            Pthread_cond_wait(&empty, &mutex);   // 等「空」
        put(i);
        Pthread_cond_signal(&fill);             // 通知「有数据」
        Pthread_mutex_unlock(&mutex);
    }
}
void *consumer(void *arg) {
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);
        while (count == 0)
            Pthread_cond_wait(&fill, &mutex);    // 等「有数据」
        int tmp = get();
        Pthread_cond_signal(&empty);            // 通知「有空」
        Pthread_mutex_unlock(&mutex);
        printf("%d\n", tmp);
    }
}
```

producer 等 `empty` 通知 `fill`; consumer 等 `fill` 通知 `empty` → consumer 永不唤 consumer, producer 永不唤 producer → v2 的死锁消除。

### 2.5 最终版: 多 slot 环形 buffer (Figure 30.13–30.14)

```c
int buffer[MAX];
int fill_ptr = 0;
int use_ptr = 0;
int count = 0;

void put(int value) {
    buffer[fill_ptr] = value;
    fill_ptr = (fill_ptr + 1) % MAX;       // 环形
    count++;
}
int get() {
    int tmp = buffer[use_ptr];
    use_ptr = (use_ptr + 1) % MAX;         // 环形
    count--;
    return tmp;
}

// 同步逻辑 (Figure 30.14):
void *producer(void *arg) {
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);
        while (count == MAX)                // 满才睡
            Pthread_cond_wait(&empty, &mutex);
        put(i);
        Pthread_cond_signal(&fill);
        Pthread_mutex_unlock(&mutex);
    }
}
void *consumer(void *arg) {
    for (i = 0; i < loops; i++) {
        Pthread_mutex_lock(&mutex);
        while (count == 0)                 // 空才睡
            Pthread_cond_wait(&fill, &mutex);
        int tmp = get();
        Pthread_cond_signal(&empty);
        Pthread_mutex_unlock(&mutex);
        printf("%d\n", tmp);
    }
}
```

多 slot 让单 producer/consumer 减少上下文切换; 多 producer/consumer 可并发存取 (互斥锁仍串行化对 buffer 的修改)。

**TIP: 用 `while` 非 `if`** — Mesa 语义下醒来后条件可能已变; `while` 也处理 **spurious wakeup** (某些实现中一次 `signal` 可能唤起两个线程)。

---

## 3. Covering Conditions (§30.3)

### 3.1 问题: 该唤谁?

多线程内存分配库 (Figure 30.15):

```c
int bytesLeft = MAX_HEAP_SIZE;
cond_t c;
mutex_t m;

void *allocate(int size) {
    Pthread_mutex_lock(&m);
    while (bytesLeft < size)
        Pthread_cond_wait(&c, &m);
    void *ptr = ...;                       // 从堆取
    bytesLeft -= size;
    Pthread_mutex_unlock(&m);
    return ptr;
}

void free(void *ptr, int size) {
    Pthread_mutex_lock(&m);
    bytesLeft += size;
    Pthread_cond_signal(&c);              // 唤谁??
    Pthread_mutex_unlock(&m);
}
```

场景: 0 字节空闲; Ta `allocate(100)` 睡, Tb `allocate(10)` 睡; Tc `free(50)`。`signal` 可能唤 Ta (要 100, 不够) 而 Tb (要 10, 够了) 仍睡 → Ta 醒来重判不够再睡, Tb 永不被唤。

### 3.2 解法: broadcast

把 `signal` 换 `pthread_cond_broadcast(&c)` 唤醒 **所有** 等待者; 各自 `while` 重判, 不够的再睡, 够的取走。

**代价**: 可能唤起很多不该醒的线程 (它们重判后立刻再睡), 性能损失。

**Lampson–Redell** 称此为 **覆盖条件 (covering condition)** — 保守地覆盖所有该醒的情况。

**警示**: 若你的程序「只有改成 broadcast 才工作」但你认为不该需要, 多半有 bug, 去修。生产者/消费者单 CV 那种就该用两 CV 而非 broadcast; 但内存分配器这类「各线程等不同阈值」的场景, broadcast 是最直接的解。

---

## 4. Summary (§30.4)

CV 是锁之外的重要同步原语: 让线程在状态不满足时睡眠, 状态改变时被唤。解决了 join、生产者/消费者、覆盖条件等经典问题。

**规则汇总**:
1. 持锁调 `wait`/`signal`
2. 用状态变量记录条件
3. `while` 非 `if` 检查条件 (Mesa 语义 + spurious wakeup)
4. 用多个 CV 区分不同条件 (定向 signal)
5. 无法定向时用 `broadcast` (覆盖条件)

---

## Homework 要点 (main-*.c)

- `main-two-cvs-while.c`: 正确版 (两 CV + while); 调 buffer 大小 / consumer sleep 观察
- `main-one-cv-while.c`: 单 CV + while; 两 consumer 时可构造死锁 (v2 bug)
- `main-two-cvs-if.c`: 两 CV + if; 单 consumer 即可出错 (v1 bug)
- `main-two-cvs-while-extra-unlock.c`: 在 put/get 前 `unlock` 会引入竞态 (assertion 触发)
