# Problem Set #1 — 解答

- **来源**: `assignment/PS01 problem set 1.pdf`
- **Due**: 2026-10-09 10:29; 课程分 6 pts (题面虚拟分 100)
- **范围**: Q1–Q2 → Lec05 / Virtualize CPU; Q3 → Lec04 / OSTEP Ch.5; Q4 → Lec06 / OSTEP Ch.7–9
- **说明**: 完整解答稿. **中文 = 说明** (给你看思路/易错); **English = Answer** (可粘贴交稿). 一问多解处全部列出. 交稿前自行核对时间线与数字.

---

## Question 1 — OS Concept (20)

### (a) Mode switching 为何也有显著 cache miss?

**说明**: 题在考「不必换进程也会污染 cache」. 关键点: 同进程 user⇄kernel 仍换了**工作集** (内核代码/数据 vs 用户代码/数据), 私有 cache 被挤掉, 回用户态就 miss. 别写成「一定换了地址空间」.

**Answer**:

> A mode switch does not change the process address space, but the CPU immediately begins executing kernel code and accessing kernel data. The kernel working set differs from the user program's working set, so it displaces / pollutes private caches (L1/L2) and possibly shared caches. After returning to user mode, much of the previous user working set has been evicted, so subsequent user accesses incur significant cache misses. The cost is therefore similar in spirit to switching to another user process: the root cause is a working-set change, which does not require a full context switch.

### (b) 专核跑内核能否减上述开销? 整体是否有益?

**说明**: 分两层答: (1) 对 (a) 的 cache 污染**可能减轻**; (2) **整体未必值得**. 下面 Answer A 推荐交稿; Answer B 更偏「能减 miss」但仍要写代价.

**Answer A** (recommended):

> Dedicating a core to the kernel may reduce the user/kernel cache pollution described in (a), because top-level caches are often private per core: user cores would run less kernel code and keep the user working set warmer, while kernel code stays hot on the dedicated core. Overall, however, this is not necessarily beneficial: (1) under light kernel load the dedicated core wastes capacity; (2) under heavy load all syscalls/interrupts queue on one core and latency rises; (3) entering the kernel from other cores needs IPI / remote calls / shared queues and extra synchronization; (4) general-purpose OSes rarely permanently dedicate a whole core to the kernel by default. So the idea can help locally with cache pollution, but throughput, latency, and complexity usually make it unattractive.

**Answer B** (more affirmative on miss reduction):

> Yes, it can reduce the cache-miss cost in (a) by keeping the user working set in private L1/L2 on user cores. Even so, cross-core entry into the kernel and load imbalance mean the design is not clearly beneficial overall; the conclusion remains: fewer user-side misses, but not necessarily a better system.

---

## Question 2 — Mode/Context Switch (25)

### (a) 填空时间线

**说明**: 约定: 阻塞 `read` 无数据 → 调度 Q; 设备中断唤醒后**立即**调度回 P. Mode = 同进程 user/kernel 切换; context = 换进程. 填空按题面顺序 1–13.

**Answer**:

| # | Blank | Answer |
|---|---|---|
| 1 | process/mode before syscall | **P**, **user** |
| 2 | first switch | **mode** switch |
| 3 | executing `sys_read` | **P**, **kernel** |
| 4 | switch after block (no data) | **context** switch |
| 5 | before return-from-trap | **Q**, **kernel** |
| 6 | that switch | **mode** switch |
| 7 | before device interrupt | **Q**, **user** |
| 8 | that switch | **mode** switch |
| 9 | executing interrupt handler | **Q**, **kernel** |
| 10 | that switch | **context** switch |
| 11 | resuming original `sys_read` | **P**, **kernel** |
| 12 | switch after return-from-syscall | **mode** switch |
| 13 | continuing in `read()` wrapper | **P**, **user** |

> Timeline summary:
>
> ```text
> P user
>   → mode switch
> P kernel  (executing sys_read; no data → blocked)
>   → context switch
> Q kernel
>   → mode switch  (return-from-trap)
> Q user
>   → mode switch  (device interrupt)
> Q kernel  (interrupt handler; wake P; schedule P)
>   → context switch
> P kernel  (resume sys_read; return-from-syscall)
>   → mode switch
> P user  (back in libc read wrapper)
> ```

### (b1) 数据已就绪时还要不要 context switch?

**说明**: 数据立即可用 → P 不进 blocked → 不必换到 Q. 只有进核/出核的 mode switch.

**Answer**:

> No context switch is needed under the problem setting. If the data are immediately available, `sys_read` finishes the copy in the kernel and returns to user mode. Process P remains runnable and never blocks, so the scheduler need not switch to Q. Only mode switches (enter/leave the kernel) occur. Q may be Ready, but that does not force a preemption.

### (b2) 中断唤醒 P 但调度器继续跑 Q

**说明**: 中断仍要 mode switch 进 handler; 若策略是继续跑 Q, 则**没有**换到 P 的 context switch; 出核再一次 mode switch. P 的状态是 Ready (已醒未跑).

**Answer**:

> On the interrupt: a **mode switch** occurs (Q: user → kernel); the handler runs and marks P Ready. If the scheduler chooses to continue running Q, there is **no context switch** to P. Returning to user mode is another **mode switch** (Q: kernel → user). Process P's state is **Ready** (woken but not Running).

---

## Question 3 — Process Control (25)

Shell S: `fork` → child C `execve("/bin/echo",…)` → parent `waitpid` → echo exits 0.

### (a) `fork` 后、`exec` 前: 2 共享 + 3 不同

**说明**: 交稿任选达标个数即可. 下面是合格选项池, **全部列出**. 示例答法见 Answer 末段.

**Answer** — shared (pick any 2 from the pool):

1. Logical view of the open file-descriptor table (same fds refer to the same open-file descriptions)
2. Memory contents initially identical (physical pages shared via copy-on-write)
3. Current working directory / umask
4. Signal dispositions (handler settings)
5. Credentials (UID/GID, etc.)
6. Initial environment-variable contents

**Answer** — different (pick any 3 from the pool):

1. **PID** (and PPID relation: child's PPID is S)
2. **`fork` return value** (parent gets child PID; child gets 0)
3. **Address space** physically separates after writes; registers / PC / stack pointer evolve independently
4. **Process state** / scheduling entity are independent
5. **Pending signal set** and other per-process kernel state
6. Resource-usage statistics (CPU time, etc.) accumulate separately

> Example submission: shared = open-file table view + COW memory; different = PID, `fork` return value, independent address-space copies.

### (b) `execve` 之后: ≥3 被替换; ≥2 保持身份相关

**说明**: exec 换的是映像与用户内存布局; PID/多数 fd 等身份相关属性保持. 至少写满题面个数.

**Answer** — replaced (write at least 3; all below are valid):

1. Program image / text (replaced by `/bin/echo`)
2. Data / BSS / heap
3. User stack contents and layout
4. Entry point / PC and user register context (starts at the new program's `_start`)
5. Most prior user mappings (replaced by new mappings)
6. Original argv/env replaced by the arguments passed to `execve`

**Answer** — preserved (write at least 2; all below are valid):

1. **PID** (same process identity)
2. **PPID** (parent is still S)
3. Open **file descriptors** by default (unless close-on-exec)
4. Process credentials (UID/GID, etc., unless a setuid binary changes effective IDs)
5. Controlling terminal / session / process group (usually kept)
6. Some attributes such as the signal mask (implementation-dependent; PID + fds suffice for class answers)

> Example submission: replaced = code, stack/heap, entry point; preserved = PID, open fds.

### (c) 父从不 `waitpid` 的可见产物

**说明**: 子已死但退出状态仍占进程表 → zombie (`Z` in `ps`).

**Answer**:

> A **zombie process**. The child has terminated, but its exit status remains in the process table / PCB until some parent reaps it with `wait*`. In `ps` this commonly appears as state `Z`.

---

## Question 4 — Process Scheduling (30)

**说明** (仿真约定, 建议写进答卷以免歧义):

- P1: `(CPU 1ms + I/O 5ms)×5`, then `CPU 1ms`. Total CPU 6ms.
- P2: continuous CPU 30ms.
- At \(t=0\) both Ready; **P1 at the front of the queue**.
- Single CPU. Turnaround = finish time − 0.
- Each dispatch gets a **fresh** time quantum; exhausting quantum → Ready queue tail; I/O completion → Ready queue.
- RR does **not** preempt mid-quantum merely because another process becomes Ready.
- MLFQ: demote only after using a **full** quantum; voluntary I/O yield does **not** demote; higher queues preempt lower; **no boost**.

### (a-i) RR, quantum = 4ms — P1 周转

**说明**: 模式是前 4 次「P1 的 1ms CPU」都在 P2 某片结束后; P2 先在 t=34 结束, P1 还要再一轮 I/O + 最后 1ms → **41**.

**Answer**:

> P1's turnaround time is **41 ms**.

> Key timeline (ms):

| Interval | Event |
|---|---|
| 0–1 | P1 CPU #1, then I/O until 6 |
| 1–9 | P2 runs (quantum expires at 5; alone Ready so takes another slice until 9) |
| 6 | P1 I/O done → Ready, waits for P2's slice |
| 9–10 | P1 CPU #2, I/O until 15 |
| 10–18 | P2 runs |
| 15 | P1 Ready |
| 18–19 | P1 CPU #3, I/O until 24 |
| 19–27 | P2 |
| 24 | P1 Ready |
| 27–28 | P1 CPU #4, I/O until 33 |
| 28–34 | P2 finishes remaining CPU; **P2 done at t=34** |
| 33 | P1 Ready |
| 34–35 | P1 CPU #5, I/O until 40 |
| 35–40 | only P1 in I/O; CPU idle |
| 40–41 | P1 last 1ms CPU; **P1 done at t=41** |

### (a-ii) MLFQ (q = 2, 4, 10) — P1 周转

**说明**: P1 每次 CPU 只有 1ms < 任一层 quantum → **永不降级**, 一直在 Queue 1; P2 沉到低队列后, P1 每次 I/O 结束立刻抢占 → 周转 **31**.

**Answer**:

> P1's turnaround time is **31 ms**.

> Reasoning: P1's every CPU burst is 1ms, smaller than any queue quantum, so P1 **never demotes** and stays in Queue 1. P2 exhausts 2ms in Queue 1 → Queue 2, then demotes again to Queue 3. Whenever P1 returns from I/O, it has higher priority than P2 and **preempts immediately**.

> Timeline:

| Interval | Event |
|---|---|
| 0–1 | P1 CPU #1 (still Q1), I/O until 6 |
| 1–3 | P2 runs full 2ms in Q1, demotes to Q2 |
| 3–6 | P2 runs in Q2 |
| 6–7 | P1 wakes (Q1), preempts, CPU #2, I/O until 12 |
| 7–12 | P2 in lower queues; preempted again at 12 |
| 12–13 | P1 CPU #3, I/O until 18 |
| 18–19 | P1 CPU #4, I/O until 24 |
| 24–25 | P1 CPU #5, I/O until 30 |
| 30–31 | P1 last CPU; **done at t=31** |

> Equivalently, P1's finish time is \(6\times 1 + 5\times 5 = 31\) (almost no wait except its own I/O).

### (a-iii) 谁对 P1 更好?

**说明**: 比数字: RR 41 vs MLFQ 31.

**Answer**:

> **MLFQ is better for P1.** Under RR, P1's turnaround is **41 ms**; under MLFQ it is **31 ms**. MLFQ keeps the interactive short-CPU job at high priority while the long job P2 sinks to lower queues, so P1 waits less.

### (b) Lottery 如何近似「总是跑最久没跑过的作业」

**说明**: 题意是近似最长等待 / LRU 式 CPU 公平. 交稿写清一种并说明票数如何随时间变即可; 下列设计都合格.

**Answer A** — tickets grow with wait:

> Give each Ready job tickets. Every time unit (or scheduling tick), increase tickets for jobs that are **not** running, proportional to waiting time. When a job is chosen and runs, reset its tickets to a base value (or reduce them sharply). At draw time the longest waiter has the most tickets and the highest win probability, approximating always running the job that has not run for the longest time.

**Answer B** — tickets from last-run time:

> Record each job's last CPU time \(t_{\mathrm{last}}\). Set tickets \(\propto (t_{\mathrm{now}}-t_{\mathrm{last}})\) (or a monotone function of that). Update \(t_{\mathrm{last}}\) after each run.

**Answer C** — compensation / decay:

> All jobs start with a base ticket count. Decay tickets after being scheduled; issue compensation tickets each round to jobs that did not run. Jobs that lose for a long time gain weight — same qualitative effect.

**Answer D** — near-deterministic bias (weaker but acceptable):

> Conceptually give almost all tickets to the current longest waiter and very few to others, still using the lottery interface so behavior is close to deterministic longest-wait scheduling.

> One-line summary: **make tickets larger for jobs that have waited / not run longer**, then clear or decay them after they win.
