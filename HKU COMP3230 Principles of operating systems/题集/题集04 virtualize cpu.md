# 题集 — Virtualize CPU

> 对齐: `Lec/Lec05 virtualize cpu 讲义.md`. 含 Mini-Lab 4 (Pthread 竞态) 与 LDE 机制题.
> 含: (1) 课件证明 (2) 练习题.

---

## 课件证明

### P1. 上下文切换须保存再恢复 (正确性)

- **陈述**: **Context switch** 把 CPU 上正在跑的进程 A 换成进程 B 时, 必须 **先保存 A 的完整执行上下文, 再装入 B 的上下文**, 否则 B 无法从上次停处继续, A 也无法被再次调度时恢复.
- **证明**: 执行上下文含 PC, 通用寄存器, 栈指针等 (存于 PCB / 内核栈). 若切换时不保存 A, 这些值被 B 覆盖即丢失 → A 再次 running 时指令地址与数据错乱. 装入 B 前须从其 PCB 恢复先前快照. 讲义 §3.2 将此列为逻辑正确性的必要条件.
- **来源**: `Lec/Lec05 virtualize cpu 讲义.md` §3.2–3.4

### P2. Mode switch 不必伴随 context switch

- **陈述**: 经 **system call** 或 **interrupt** 进入内核 (mode switch) 后, 调度器 **可以** 让 **同一进程** 返回用户态继续跑, 不必换进程.
- **证明**: Mode switch 只改变特权级与内核栈等, **地址空间仍属当前进程**. Context switch 额外切换 **另一进程的内存信息与寄存器快照**. 讲义对照表: syscall 处理完毕若调度器选「当前进程」, 则仅 mode switch; 仅当调度器选就绪队列中 **另一** PCB 时才完整 context switch.
- **来源**: `Lec/Lec05 virtualize cpu 讲义.md` §3.3; Summary 易错点 1

### P3. 仅靠被动等 syscall 无法对付死循环

- **陈述**: 若进程在用户态 **busy loop** 且从不触发 syscall/ fault, OS **无法** 夺回 CPU 做调度.
- **证明**: **被动** 夺回路径依赖进程自愿 trap (syscall) 或同步异常. 死循环不 trap → 内核无入口 → 调度器无法运行 → **非协作** 进程可独占 CPU. 故需 **timer interrupt** 周期性强制进内核 (讲义 §4 **主动** 路径).
- **来源**: `Lec/Lec05 virtualize cpu 讲义.md` §4; 易错点 3

---

## 练习题

## Mini-Lab

### 1. Pthread 竞态与同步

- **题目**: 在 `lab/Mini-lab/Lab04 pthread.c` 中: 4 线程各对共享 `counter` 执行 $10^6$ 次 `++`; 用 `pthread_create` / `pthread_join`; 用 **mutex** (或题面允许的 CV/semaphore) 保护 `counter++`, 使终值恒为 $4\times 10^6$. 无保护时为何偏小且不稳定? 编译加 `-pthread`.
- **思路**: 非原子 RMW 交错丢更新 (同 Intro OS **P1**). `pthread_mutex_init/lock/unlock/destroy` 串行化临界区.
- **来源**: `lab/Mini-lab/Lab04 pthread race condition 题目理解.md` (与 OSTEP `threads.c` 同族)

---

## 机制 / Crux

### 2. Process control 三问

- **题目**: 虚拟化 CPU 主题下, 对应机制: (1) 受限操作? (2) 多 CPU 幻觉? (3) OS 如何夺回 CPU (自愿 vs 非自愿)?
- **思路**: (1) system call; (2) context switching 轮流跑; (3) 自愿 syscall, 非自愿 interrupt (如 timer). 见 **P3**.
- **来源**: `Lec/Lec05 virtualize cpu 讲义.md` §1

### 3. 为何用 API 而非直接 syscall

- **题目**: 应用为何通常调用 POSIX/glibc API 而不是自己写 trap 指令?
- **思路**: 隐藏 OS/CPU 差异; 统一参数/返回值; 编号与寄存器约定由库封装.
- **来源**: 讲义 §2.1

### 4. Context switch 的 Crux

- **题目**: **直接执行**下, OS 如何 **透明** 暂停进程 A 并恢复 B? 进程是否感知被切走?
- **思路**: 保存 A 寄存器/PC 等到 PCB, 加载 B 上下文 (见 **P1**); **transparency** — 用户进程一般不感知调度时刻.
- **来源**: 讲义 §3

### 5. System call 与 mode switch

- **题目**: 一次 syscall 从 user 到 kernel 再返回, 与「进程地址空间归属」关系如何? (内核代表谁执行?)
- **思路**: trap 进内核 = mode switch; 内核仍代表 **该进程** 执行, 返回用户态继续同一地址空间 (见 **P2**).
- **来源**: 讲义 §2.3
