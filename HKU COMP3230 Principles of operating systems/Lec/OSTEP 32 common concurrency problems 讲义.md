# OSTEP Ch.32 — Common Concurrency Problems: 常见并发 bug

- **来源**: `Lec/OSTEP 32 common concurrency problems.pdf` (16 页, Ch.32)
- **课程**: COMP3230B Principles of Operating Systems
- **对齐 slides**: `Lec/Lec08 synchronization 讲义.md` / `Lec/Lec09 deadlock 讲义.md`

> 基于 Lu et al. [L+08] 对 MySQL / Apache / Mozilla / OpenOffice 共 105 个并发 bug 的实证研究。分非死锁 (74) 与死锁 (31) 两类。本章是 Lec08/Lec09 的「为什么」与 bug 模式归纳。术语首次标英文。

---

## 0. 一页速览

| 类别 | 子类 | 占比/特征 | 修复 |
|---|---|---|---|
| 非死锁 (74) | 原子性违反 (atomicity violation) | 97% 中的 ~一半 | 加锁包住 CS |
| 非死锁 | 顺序违反 (order violation) | 97% 中的 ~一半 | 用 CV/信号量强制顺序 |
| 死锁 (31) | 循环等待 | 四条件全成立 | 全序/偏序锁; 一次性获取; trylock; 无锁; 调度避免; 检测恢复 |

---

## 1. Bug 类型分布 (§32.1, Figure 32.1)

| 应用 | 非死锁 | 死锁 | 总 |
|---|---|---|---|
| MySQL | 14 | 9 | 23 |
| Apache | 13 | 4 | 17 |
| Mozilla | 41 | 16 | 57 |
| OpenOffice | 6 | 2 | 8 |
| **总** | **74** | **31** | **105** |

非死锁占多数 (~70%)。

---

## 2. Non-Deadlock Bugs (§32.2)

### 2.1 原子性违反 (atomicity violation)

**定义** (Lu et al.): 「多个内存访问之间期望的可串行化 (serializability) 被破坏 — 即一段代码本应原子, 但执行时未强制原子。」

**MySQL 例** (Figure 32.2):

```c
// Thread 1
if (thd->proc_info) {                 // 检查非 NULL
    fputs(thd->proc_info, ...);        // 使用
}
// Thread 2
thd->proc_info = NULL;                 // 置空
```

Bug: T1 检查后, fputs 前被中断; T2 置 NULL; T1 恢复 fputs(NULL) → 崩溃 (NULL 解引用)。

**修复** (Figure 32.3): 加锁包住「检查 + 使用」:

```c
pthread_mutex_t proc_info_lock = PTHREAD_MUTEX_INITIALIZER;

// Thread 1
pthread_mutex_lock(&proc_info_lock);
if (thd->proc_info) {
    fputs(thd->proc_info, ...);
}
pthread_mutex_unlock(&proc_info_lock);

// Thread 2
pthread_mutex_lock(&proc_info_lock);
thd->proc_info = NULL;
pthread_mutex_unlock(&proc_info_lock);
```

所有访问 `proc_info` 的代码都须持同一锁。

### 2.2 顺序违反 (order violation)

**定义**: 「两组内存访问之间期望的顺序被颠倒 — 即 A 应在 B 之前执行, 但执行时未强制。」

**Mozilla 例** (Figure 32.4):

```c
// Thread 1: init()
void init() {
    mThread = PR_CreateThread(mMain, ...);   // 创建 T2
}
// Thread 2: mMain() (T2 入口)
void mMain(...) {
    mState = mThread->State;     // 假设 mThread 已初始化
}
```

Bug: T2 一创建就跑, 可能在 T1 把 `mThread` 赋值前就执行 `mMain`, 解引用未初始化的 `mThread` (假设初值 NULL) → 崩溃。

**修复** (Figure 32.5): 用条件变量 + 状态变量强制顺序:

```c
pthread_mutex_t mtLock = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t  mtCond = PTHREAD_COND_INITIALIZER;
int mtInit = 0;

// Thread 1: init()
void init() {
    mThread = PR_CreateThread(mMain, ...);
    pthread_mutex_lock(&mtLock);
    mtInit = 1;
    pthread_cond_signal(&mtCond);     // 通知已初始化
    pthread_mutex_unlock(&mtLock);
}

// Thread 2: mMain()
void mMain(...) {
    pthread_mutex_lock(&mtLock);
    while (mtInit == 0)
        pthread_cond_wait(&mtCond, &mtLock);   // 等初始化
    pthread_mutex_unlock(&mtLock);
    mState = mThread->State;
}
```

`while (mtInit == 0)` 防虚假唤醒; 信号量也可达同样效果。

### 2.3 小结

Lu et al. 研究中 **97%** 非死锁 bug 是原子性或顺序违反。自动检查工具应聚焦这两类。

---

## 3. Deadlock Bugs (§32.3)

**典型场景** (Figure 32.6):

```c
// Thread 1            // Thread 2
lock(L1);              lock(L2);
lock(L2);              lock(L1);
```

T1 持 L1 等 L2, T2 持 L2 等 L1 → 循环等待 → 死锁。资源分配图 (Figure 32.7) 出现环 = 死锁。

### 3.1 为什么会发生

- **大代码库复杂依赖**: 如 VM 子系统调 FS 换页, FS 又调 VM 分配内存 → 锁协议须处理循环依赖
- **封装 (encapsulation) 反作用**: Java `Vector.AddAll(v2)` 内部锁 v1 再锁 v2; 若另一线程调 `v2.AddAll(v1)` → 死锁, 调用方完全看不见

### 3.2 死锁四条件 (Coffman et al. 1971)

死锁发生须 **四条同时成立**:

1. **互斥 (mutual exclusion)**: 资源独占 (如锁)
2. **持有并等待 (hold-and-wait)**: 持已有资源等新资源
3. **不可抢占 (no preemption)**: 资源不能被强制夺走
4. **循环等待 (circular wait)**: 线程链形成环

破坏任一即不能死锁。下述预防策略各破坏一条。

### 3.3 预防 (Prevention) — 各破一条

#### (a) 破坏循环等待: 锁全序/偏序

最实用。所有锁赋全局全序, 始终按序获取:

```c
// 总是先 L1 后 L2
lock(L1); lock(L2); ... unlock(L2); unlock(L1);
```

复杂系统可用 **偏序** (partial ordering): Linux mm/filemap.c 注释列出 10 个锁组顺序 (如 `i_mutex before i_mmap_rwsem`; `i_mmap_rwsem before private_lock before swap_lock before i_pages lock`)。

**TIP — 按锁地址排序**: 当函数收两把锁 `do_something(m1, m2)`, 调用方可能传 `(L1,L2)` 或 `(L2,L1)`。按地址高低统一获取顺序:

```c
if (m1 > m2) { lock(m1); lock(m2); }
else         { lock(m2); lock(m1); }   // 假设 m1 != m2
```

保证不论传入顺序都按同一序获取 → 无死锁。

**缺点**: 须全局理解调用关系; 一处疏忽即死锁; 封装隐藏了锁获取, 难维护。

#### (b) 破坏持有并等待: 一次性原子获取所有锁

```c
pthread_mutex_lock(prevention);   // 全局预防锁
pthread_mutex_lock(L1);
pthread_mutex_lock(L2);
...
pthread_mutex_unlock(prevention);
```

`prevention` 保证获取多锁期间不被切换 → 不会有人部分持有再等。

**缺点**: 须预先知道所有要拿的锁 (封装矛盾); 早期一次性拿全降低并发度。

#### (c) 破坏不可抢占: `trylock` + 回退

```c
top:
pthread_mutex_lock(L1);
if (pthread_mutex_trylock(L2) != 0) {   // L2 被占则不阻塞
    pthread_mutex_unlock(L1);           // 释放 L1
    goto top;                            // 重试
}
```

`pthread_mutex_trylock`: 成功返回 0, 失败返回错误码 (不阻塞)。失败则释放已有锁重试。

**新问题 — 活锁 (livelock)**: 两线程可能反复同时失败重试, 都在跑但无进展。缓解: 重试前加随机延迟, 降低同步干扰。

**缺点**: 封装下回退到起点复杂 (须释放沿途已分配资源); 适用面有限 (如 Java Vector 那种局部场景)。

#### (d) 破坏互斥: 无锁 (lock-free / wait-free) 数据结构

Herlihy [H91, H93]: 用硬件原子指令 (如 compare-and-swap) 构造无锁数据结构。

**compare-and-swap (CAS)**:

```c
int CompareAndSwap(int *address, int expected, int new) {
    if (*address == expected) {
        *address = new;
        return 1;   // success
    }
    return 0;       // failure
}
```

**原子自增**:

```c
void AtomicIncrement(int *value, int amount) {
    do {
        int old = *value;
    } while (CompareAndSwap(value, old, old + amount) == 0);
}
```

**链表头插 (lock-free)**:

```c
void insert(int value) {
    node_t *n = malloc(sizeof(node_t));
    n->value = value;
    do {
        n->next = head;                       // 读当前头
    } while (CompareAndSwap(&head, n->next, n) == 0);   // 失败重试
}
```

CAS 失败说明期间有人改了 head → 用新 head 重试。无锁 → 无死锁 (但仍有活锁可能)。

**缺点**: 删除/查找的无锁实现极复杂; 通用性受限。详见 Herlihy 综述 [H01, H91, H93]。

### 3.4 死锁避免 (Avoidance) — via Scheduling

需全局知识: 各线程执行中可能获取哪些锁。调度器据此安排, 保证不并发的线程不重叠。

**例 1** (2 CPU, 4 线程):

| | T1 | T2 | T3 | T4 |
|---|---|---|---|---|
| L1 | ✓ | ✓ | | |
| L2 | ✓ | ✓ | ✓ | |

只要 T1 与 T2 不同时跑, 就无死锁 (T3 只持一把锁不会引环; T4 无锁)。调度: CPU1 跑 T1→T2, CPU2 跑 T3→T4。

**例 2** (高竞争): T1/T2/T3 都需 L1+L2。只能把 T1/T2/T3 全排到同一 CPU 串行跑, T4 在另一 CPU。安全但牺牲并发。

**Dijkstra 银行家算法 (Banker's Algorithm)** [D64] 属此类。**缺点**: 仅适用于嵌入式等完全已知任务集的环境; 限制并发; 通用性差。

### 3.5 检测与恢复 (Detect and Recover)

允许死锁偶尔发生, 周期性检测, 发现则重启/修复。

- OS 一年死锁一次 → 重启即可 (Tom West's Law: 「不是所有值得做的事都值得做好」; 代价低则不必过度工程)
- 数据库系统常用: 死锁检测器周期构建资源图查环; 有环则重启, 必要时人工修复数据

---

## 4. Summary (§32.4)

- 非死锁 bug 更常见, 多为原子性/顺序违反, 修复相对直接 (加锁 / 用 CV)
- 死锁自古存在; 实践最佳解是 **小心设计 + 锁全序预防**
- 无锁/无等待 (wait-free) 数据结构有前景 (Linux 已用), 但通用性与开发复杂度受限
- 终极方向: 新并发编程模型 (如 MapReduce), 让程序员不写锁

---

## 5. 与本课 slides 的对应

| OSTEP § | Lec08/Lec09 对应 |
|---|---|
| §2.1 原子性违反 | Lec08 §3 临界区 / §4 Peterson 互斥动机 |
| §2.2 顺序违反 | Lec08 §9 条件变量 join 例 |
| §3.2 四条件 | Lec09 §2 死锁四条件 |
| §3.3(a) 全序/偏序 | Lec09 §3.1 预防-全序; §5.2 哲学家破环 |
| §3.3(b) 一次性获取 | Lec09 §3.2 预防-持有并等待 |
| §3.3(c) trylock | Lec09 §3.3 预防-不可抢占 (含活锁) |
| §3.3(d) 无锁 CAS | Lec08 §5.2 CAS / 自旋锁 |
| §3.4 调度避免 | Lec09 §4.2 银行家算法 (Banker's) |
| §3.5 检测恢复 | Lec09 §5 检测与恢复 |
