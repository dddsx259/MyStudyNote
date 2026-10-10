# Thread Abstraction & Concurrency: 线程抽象与并发 (thread abstraction and concurrency)

- **来源**: `Lec/Lec07 thread concept.pdf` (25 页)
- **课程**: COMP3230B Principles of Operating Systems
- **学习成果**: ILO 2a (进程/线程管理); ILO 2c (并发问题成因); ILO 4 (系统工具开发)
- **必读**: OSTEP Ch.26, Ch.27
- **对齐阅读讲义**: `OSTEP 26 threads intro 讲义.md`, `OSTEP 27 threads api 讲义.md`

> 本讲建立线程与竞态基础; 锁/CV/信号量细节在后续 slides. 含课件选择题讲解. 术语首次标英文.

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| 线程 (thread) | 进程内可调度的指令序列; 多线程共享地址空间 |
| 为何用 | 表达并行; 创建开销小于进程; 一线程阻塞他线程可继续; 多核 |
| Pthreads | `pthread_create` / `exit` / `join` |
| Linux | pthread ≈ 轻量进程 (lightweight process, LWP); `clone()` |
| 竞态 (race condition) | 共享数据并发修改 + 结果依赖交错次序 |
| 临界区 / 互斥 | critical section; mutual exclusion; 原子操作不够覆盖复杂 CS |
| Crux | 硬件+OS 如何支持互斥与同步 (synchronization) |

---

## 1. 为何在 OS 课学并发 (p.2)

一句话: **历史**. OS 是最早的并发程序; 多数同步技术先在内核长成, 后被多线程应用复用.

---

## 2. What are threads? (p.6–8)

### 2.1 定义

- **执行线程 (thread of execution)**: 在应用进程内完成某任务的指令序列
- 传统进程可看成 **只有一个执行线程** 的进程
- **多线程进程 (multithreaded process)**: 一个进程内多个线程; 线程是进程内实体
- 同进程线程可 **并发执行**, 并 **共享** 该进程地址空间与其他全局信息

课件示意: 单线程 `main` 顺序调 A,B,C,D; 多线程则 Thread1 跑 A,C, Thread2 跑 B,D, 经 `Join` 汇合.

### 2.2 每线程私有 vs 共享

为支持多线程, 系统须给每线程:

| 私有 | 共享 (同进程) |
|---|---|
| 程序计数器 (program counter, PC) | 地址空间 (code/data/heap 等) |
| 私有寄存器组 | 打开文件等多数「进程级」资源 |
| 用户栈 (+ 内核栈) | 全局变量 |
| **线程控制块 (Thread Control Block, TCB)** | |

线程状态机类似进程: new, running, ready, blocked, terminated.

---

## 3. Why Multithreading? (p.9)

1. **更自然表达本征并行任务**
2. **性能**:
   - 创建/终止线程通常比进程便宜 (更少设置)
   - 一线程阻塞 (blocking syscall) 时, **同进程其他线程仍可跑** (传统单线程进程整进程进 blocked)
   - 可利用多核: 一进程多线程, 各核跑一线程
   - **同进程线程切换** 通常比跨进程切换开销小 (地址空间不变)

---

## 4. POSIX Threads / Pthreads (p.10–16)

**POSIX 线程 (POSIX Threads, Pthreads)**: IEEE 1003.1c 标准 API, 规定行为, 库实现自定. 常见于 Linux/Solaris/macOS.

POSIX 要求: 每线程独立维护处理器寄存器, 栈, 信号掩码 (signal mask); 并规定信号投递与取消模式等.

### 4.1 `pthread_create`

```c
#include <pthread.h>
int pthread_create(pthread_t *thread,
    const pthread_attr_t *attr,
    void *(*thrfunc)(void *),
    void *args);
```

四参数: 线程句柄指针; 属性 (常 `NULL`); 入口函数; 单一 `void*` 参数.

通常从 `main` 内创建.

### 4.2 `pthread_exit`

```c
void pthread_exit(void *retval);
```

结束调用线程; `retval` 可由 `pthread_join` 取回. **不** 自动关文件: 线程内打开的文件在线程结束后仍保持打开 (进程级资源).

### 4.3 `pthread_join`

```c
int pthread_join(pthread_t thread_id, void **value_ptr);
```

阻塞调用者直至目标线程终止; `value_ptr` 可 `NULL` 若不要返回值. **Join** 是主线程等待工人线程的常用方式.

### 4.4 课件例子 (p.15)

`main` 建线程跑 `func1`, 传入 `int` 的地址; 线程打印参数与 `getpid()`; `main` 也打印 PID 后 `join`. 预期: **父子线程同 PID** (同一进程).

### 4.5 Pthreads in Linux (p.16)

- 每个 pthread 实现为标准进程式实体 — **轻量进程 (LWP)**
- 同应用 LWP **共享** 地址空间, 打开文件, 全局变量, 堆等
- 用 **`clone()`** 而非单纯 `fork()`: 参数指定与父任务共享哪些资源
- 调度器可 **不区分** 「线程 vs 进程」标签, 统一按可调度实体处理

---

## 5. Concurrency Issue (p.17–20)

### 5.1 `x++` 不是原子的

`x++` 常编译为: 读 x → 寄存器自增 → 写回. 两线程交错可得到 11 而非 12 (丢失更新).

单核也可因 **线程切换 (thread switch)** 在中间插入; 多核可真并行执行三条指令序列.

### 5.2 根因: 不受控调度 (uncontrolled scheduling)

无法预测线程何时、跑多久 → 交错不确定.

### 5.3 Race Condition (定义)

**竞态条件 (race condition)**: 多个线程 **并发访问并修改** 同一共享数据, 且执行结果依赖访问的 **特定次序 (a race)** → **非确定性计算 (non-deterministic computation)**, 多次运行结果可能不同.

---

#### Exercise / 选择题 (课件 p.20)

两线程共享 `x`, 初值 0. A 对 `x` 增 10 次, B 减 25 次, 并发. 下列哪项正确?

- A. 终值必为 $-15$
- B. 终值可为任意整数
- C. 终值在 $[-25,10]$ (含端点)
- D. 终值不会是 0
- E. 终值最小约 $-20$, 最大约 $5$, 不会越界

**讲解**: 每次 `++`/`--` 若非原子, 交错可丢失更新, 但每次操作仍是「读-改-写一个整数」, 不可能把 `x` 改成与「增/减计数」无关的任意值. 极端: 几乎所有更新丢失时, 终值仍落在「只成功部分增减」的范围内. 正确选项是 **C**: 最坏可接近「A 的 10 次全生效且 B 全丢」→ $10$, 或「B 的 25 次全生效且 A 全丢」→ $-25$; 中间任意整数可达 (在合理交错模型下). A 错 (非确定性); B 过宽; D/E 过窄或错界.

> 严格模型下「可达集合」讨论可更深; 课件意图是强调 **丢失更新使结果 ∈ [min 净效应, max 净效应]**, 而非单一 $-15$.

---

## 6. Critical Sections & Mutual Exclusion (p.21–22)

- 多线程中 **多数代码** 可不碰共享数据, 可安全并发
- 修改特定共享数据的代码块须保护 → **临界区 (critical section, CS)**
- 希望 **同一时刻至多一个线程** 处于访问该共享数据的 CS; 且 CS 应尽快执行完

**互斥 (mutual exclusion)**: 共享数据以互斥方式访问 — 胜者相当于 **锁住 (lock)** 数据, 他者等待解锁. 亦称 **串行化访问 (serialized access)**.

---

## 7. Atomic Operation (p.23)

解决 `x++` 竞态的一种方式: 使操作 **原子 (atomic)** — 不可中途打断, 硬件保证「全做完或没做」.

但 CS 可能含链表遍历等复杂逻辑 → **仅有原子指令不够**, 需要更一般的互斥与同步原语.

---

## 8. Synchronization Crux (p.24)

另一常见交互: 一线程须 **等待** 另一线程完成某动作再继续 (worker 等 boss 派活).

**Crux**: 如何为互斥与同步提供支持? 硬件与 OS 需要提供什么?

(后续讲: locks, condition variables, semaphores 等.)

---

## 9. Summary (p.25)

- 线程又名轻量进程: 进程内可独立调度的代码片段
- 自有 PC/寄存器/栈; 共享进程地址空间
- OS 用 TCB 抽象线程
- 多进程/多线程带来并发问题; OS 须提供同步协调机制
