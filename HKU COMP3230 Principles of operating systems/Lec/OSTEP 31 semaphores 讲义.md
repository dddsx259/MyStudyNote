# OSTEP Ch.31 — Semaphores: 信号量 (semaphores)

- **来源**: `Lec/OSTEP 31 semaphores.pdf` (20 页, Ch.31)
- **课程**: COMP3230B Principles of Operating Systems
- **对齐 slides**: `Lec/Lec08 synchronization 讲义.md`

> Dijkstra 引入的单一同步原语, 既可当锁也可当条件变量。本章用信号量重解生产者/消费者、读者-写者、哲学家就餐, 并用锁+CV 实现信号量 (Zemaphore)。教材代码全部入库并附注释。术语首次标英文。

---

## 0. 一页速览

| 节 | 主题 | 要点 |
|---|---|---|
| §1 | 定义 | 整数 + `sem_wait`(减1, <0 睡) + `sem_post`(加1, 唤醒一个); 初值决定行为 |
| §2 | 二值信号量 = 锁 | 初值 1; 0/1 状态 |
| §3 | 顺序同步 | 初值 0; parent `wait` child `post` (join) |
| §4 | 生产者/消费者 | `empty`(MAX)/`full`(0); 加 `mutex` 互斥; **顺序错则死锁** |
| §5 | 读者-写者锁 | `readers` 计数 + `writelock`; 首读者锁写, 末读者释写 |
| §6 | 哲学家就餐 | 全拿左叉 → 死锁; 一人反序拿 → 破环 |
| §7 | 线程节流 | 信号量限制并发进入某区域的最大线程数 |
| §8 | 用锁+CV 实现信号量 | Zemaphore: value + lock + cond; `while(value<=0) wait` |

---

## 1. Semaphores: A Definition (§31.1)

**信号量 (semaphore)**: 一个含整数值的对象, 经两条原子操作访问:

```c
#include <semaphore.h>
sem_t s;
sem_init(&s, 0, 1);    // 第二参数 0 = 线程间共享; 第三参数 = 初值

int sem_wait(sem_t *s) {
    decrement s by 1;
    if s < 0          // 负值 = 等待线程数
        wait;         // 阻塞
}

int sem_post(sem_t *s) {
    increment s by 1;
    if 有等待者
        wake one;     // 唤醒一个
}
```

- `sem_wait` 旧名 **P()** (prolaag/probeer); 也叫 `down`
- `sem_post` 旧名 **V()** (verhoog); 也叫 `up`
- **不变量**: 信号量值为负时, 其绝对值 = 等待线程数 (Dijkstra 原版); Linux 实现中值不低于 0 (见 §8)

**初值的意义** (TIP): 初值 = 初始化后「愿意立刻发放的资源数」。锁用 1 (可立刻被一人拿走); 顺序同步用 0 (起初无资源, 等 child 完成才 post 出来)。

---

## 2. Binary Semaphores (Locks) (§31.2)

```c
sem_t m;
sem_init(&m, 0, 1);    // 初值 1

sem_wait(&m);
// 临界区
sem_post(&m);
```

**两线程 trace** (Figure 31.5): T0 `wait` → 值 0, 进 CS; T1 `wait` → 值 -1, 睡; T0 `post` → 值 0, 唤醒 T1; T1 醒来进 CS; T1 `post` → 值 1。

初值 1 → 状态 {0, 1} → 行为同互斥锁, 故称 **二值信号量 (binary semaphore)**。

---

## 3. Semaphores for Ordering (§31.3)

用信号量约束事件先后 (Figure 31.6, join 例):

```c
sem_t s;
sem_init(&s, 0, 0);    // 初值 0

void *child(void *arg) {
    printf("child\n");
    sem_post(&s);       // 通知: child 完成
    return NULL;
}

int main(int argc, char *argv[]) {
    sem_init(&s, 0, 0);
    printf("parent: begin\n");
    pthread_t c;
    Pthread_create(&c, NULL, child, NULL);
    sem_wait(&s);       // 等 child 完成
    printf("parent: end\n");
    return 0;
}
```

**两种执行顺序**:
- parent 先 `wait`: 值 -1, 睡; child 后 `post`: 值 0, 唤醒 parent
- child 先 `post`: 值 1; parent 后 `wait`: 值 0, 直接返回不睡

初值 0 保证 parent 在 child 完成前不会通过。

---

## 4. Producer/Consumer (Bounded Buffer) (§31.4)

### 4.1 单 slot 版 (Figure 31.9–31.10)

```c
int buffer[MAX];
int fill = 0;
int use = 0;

void put(int value) {
    buffer[fill] = value;
    fill = (fill + 1) % MAX;
}

int get() {
    int tmp = buffer[use];
    use = (use + 1) % MAX;
    return tmp;
}

sem_t empty;
sem_t full;

void *producer(void *arg) {
    int i;
    for (i = 0; i < loops; i++) {
        sem_wait(&empty);    // P1: 等空位
        put(i);              // P2
        sem_post(&full);     // P3: 通知有数据
    }
}

void *consumer(void *arg) {
    int tmp = 0;
    while (tmp != -1) {
        sem_wait(&full);     // C1: 等数据
        tmp = get();          // C2
        sem_post(&empty);     // C3: 通知有空位
        printf("%d\n", tmp);
    }
}

int main(...) {
    sem_init(&empty, 0, MAX);   // MAX 个空位
    sem_init(&full,  0, 0);     // 0 个已填
}
```

MAX=1 时单 producer 单 consumer 工作正常。但 MAX>1 且多 producer/consumer 时, `put`/`get` 的 `fill`/`use` 自增是竞态 → 须加互斥。

### 4.2 错误加锁 (Figure 31.11, 死锁)

```c
void *producer(void *arg) {
    for (i = 0; i < loops; i++) {
        sem_wait(&mutex);    // P0: 先拿 mutex
        sem_wait(&empty);     // P1
        put(i);              // P2
        sem_post(&full);      // P3
        sem_post(&mutex);    // P4
    }
}
// consumer 同理: 先 wait(&mutex) 再 wait(&full)
```

**死锁场景**: consumer 先跑, `wait(&mutex)` 成功, `wait(&full)` (值 0) 阻塞, 但 **仍持 mutex**; producer 跑, `wait(&mutex)` (被 consumer 持) 阻塞 → 互相等 → 死锁。

### 4.3 正确版 (Figure 31.12)

```c
void *producer(void *arg) {
    for (i = 0; i < loops; i++) {
        sem_wait(&empty);    // P1: 先等空位
        sem_wait(&mutex);    // P1.5: 再拿 mutex (仅包住 CS)
        put(i);
        sem_post(&mutex);   // P2.5
        sem_post(&full);     // P3
    }
}
void *consumer(void *arg) {
    for (i = 0; i < loops; i++) {
        sem_wait(&full);     // C1: 先等数据
        sem_wait(&mutex);    // C1.5: 再拿 mutex
        int tmp = get();
        sem_post(&mutex);   // C2.5
        sem_post(&empty);    // C3
        printf("%d\n", tmp);
    }
}
```

**关键**: mutex 只包住 `put`/`get` (CS), 不包住 `empty`/`full` 的 wait/post → 等资源时不持 mutex → 不会死锁。这正是 Lec08 §11 的「先 wait 资源信号量, 再 wait mutex」。

---

## 5. Reader-Writer Locks (§31.5)

```c
typedef struct _rwlock_t {
    sem_t lock;          // 二值, 保护 readers 计数
    sem_t writelock;     // 二值, 写者独占 / 多读者共享
    int readers;
} rwlock_t;

void rwlock_init(rwlock_t *rw) {
    rw->readers = 0;
    sem_init(&rw->lock, 0, 1);
    sem_init(&rw->writelock, 0, 1);
}

void rwlock_acquire_readlock(rwlock_t *rw) {
    sem_wait(&rw->lock);
    rw->readers++;
    if (rw->readers == 1)           // 首读者: 锁住写
        sem_wait(&rw->writelock);
    sem_post(&rw->lock);
}

void rwlock_release_readlock(rwlock_t *rw) {
    sem_wait(&rw->lock);
    rw->readers--;
    if (rw->readers == 0)           // 末读者: 释放写
        sem_post(&rw->writelock);
    sem_post(&rw->lock);
}

void rwlock_acquire_writelock(rwlock_t *rw)  { sem_wait(&rw->writelock); }
void rwlock_release_writelock(rwlock_t *rw) { sem_post(&rw->writelock); }
```

**机制**:
- 首读者 `sem_wait(&writelock)` 阻止写者; 末读者 `sem_post(&writelock)` 放行写者
- 写者直接对 `writelock` 做 wait/post, 与首/末读者互斥
- 多读者可并发读

**缺点**: 偏向读者, 写者可能饥饿 (读者不断来则 `readers` 永不归 0)。更复杂解法可让写者等待时阻止新读者进入。

**TIP (Hill's Law)**: 简单 dumb 的方案常比花哨的好。读写锁开销大, 有时不如直接用普通自旋锁。先试简单方案。

---

## 6. Dining Philosophers (§31.6)

五哲学家围圆桌, 五叉, 吃面需左右两叉。

```c
int left(int p)  { return p; }
int right(int p) { return (p + 1) % 5; }   // 模 5 处理 P4 的右叉 = f0

sem_t forks[5];   // 每叉一把二值信号量 (初值 1)
```

### 6.1 错误解 (Figure 31.15, 死锁)

```c
void get_forks(int p) {
    sem_wait(&forks[left(p)]);    // 先拿左
    sem_wait(&forks[right(p)]);   // 再拿右
}
void put_forks(int p) {
    sem_post(&forks[left(p)]);
    sem_post(&forks[right(p)]);
}
```

五人同时拿左叉 → 每人持一叉等右叉 → 循环等待 → 死锁。

### 6.2 正解: 破环 (Figure 31.16)

让 P4 (最高号) **反序**拿:

```c
void get_forks(int p) {
    if (p == 4) {
        sem_wait(&forks[right(p)]);   // P4 先拿右
        sem_wait(&forks[left(p)]);
    } else {
        sem_wait(&forks[left(p)]);    // 其余先拿左
        sem_wait(&forks[right(p)]);
    }
}
```

P4 先拿 f0 (右), 其余先拿左; 环被打破: 不存在每人持一叉等下一人的情形。这对应 Lec09 §5.1「全序资源申请破坏循环等待」。

---

## 7. Thread Throttling (§31.7)

用信号量限制同时进入某区域的线程数 (准入控制 / admission control):

```c
sem_t throttle;
sem_init(&throttle, 0, MAX_CONCURRENT);

// 进入内存密集区前:
sem_wait(&throttle);
// ... 内存密集区 ...
sem_post(&throttle);
```

场景: 数百线程, 某段需大量内存; 全进会 thrash (换页)。信号量限制同时进入数, 防止物理内存超用。

---

## 8. 用锁+CV 实现信号量 (Zemaphore) (§31.8)

```c
typedef struct __Zem_t {
    int value;
    pthread_cond_t cond;
    pthread_mutex_t lock;
} Zem_t;

void Zem_init(Zem_t *s, int value) {
    s->value = value;
    Cond_init(&s->cond);
    Mutex_init(&s->lock);
}

void Zem_wait(Zem_t *s) {
    Mutex_lock(&s->lock);
    while (s->value <= 0)
        Cond_wait(&s->cond, &s->lock);    // 释放锁睡, 醒来重获
    s->value--;
    Mutex_unlock(&s->lock);
}

void Zem_post(Zem_t *s) {
    Mutex_lock(&s->lock);
    s->value++;
    Cond_signal(&s->cond);                // 唤醒一个
    Mutex_unlock(&s->lock);
}
```

**与 Dijkstra 原版差异**: Zemaphore 的 `value` 不低于 0 (不靠负值记等待者数), 与 Linux 实现一致; Dijkstra 原版允许负值, 其绝对值 = 等待者数。

**反向**: 用信号量实现 CV 较难 (Birrell 2004 记录了 Windows 上的多次 bug), 因为 CV 的 `wait` 须原子释放锁+睡, 而信号量没有直接的「原子两步」语义。

---

## 9. Summary (§31.9)

信号量是强大灵活的原语, 可当锁也可当 CV。本章解了: 二值锁、顺序同步、生产者/消费者、读者-写者、哲学家就餐、线程节流。但 **泛化要小心** (Lampson: 「别泛化, 泛化通常错」) — 用信号量当 CV 通用接口未必比锁+CV 直接更简单。

**Homework 要点**: fork-join, rendezvous (两线程会合点), barrier (N 线程屏障), reader-writer (含无饥饿版), no-starve mutex — 见 Downey *The Little Book of Semaphores*。
