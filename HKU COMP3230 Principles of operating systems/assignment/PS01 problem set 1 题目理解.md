# Problem Set #1 — 题目理解

- **来源**: `assignment/PS01 problem set 1.pdf`
- **Due**: 2026-10-09 10:29 am
- **分值**: 课程分 6 pts (题面「虚拟分」合计 100, 再映射到 6)
- **版本**: 1.0
- **完整解答**: [`PS01 problem set 1 解答.md`](PS01%20problem%20set%201%20解答.md)
- **说明**: 本文件为逐题理解与思路提示; 完整可交写法见解答. 交稿前自行演算.

---

## 总览

| 题 | 虚拟分 | 主题 | 对齐材料 |
|---|---|---|---|
| Q1 | 20 | OS 概念: mode switch 与 cache | Lec05 Virtualize CPU |
| Q2 | 25 | Mode/Context switch 时间线填空 | Lec05 + blocking `read` |
| Q3 | 25 | `fork` / `exec` / `wait` / zombie | Lec04 / OSTEP Ch.5 |
| Q4 | 30 | RR vs MLFQ 手算 + Lottery 设计 | Lec06 / OSTEP Ch.7–9 |

---

## Question 1 — OS Concept (20)

### (a) (10%) Mode switching 为何也会有显著 cache miss?

**题意**: Context switch 导致换进程后 cache 冷很直观; 问 **mode switch** (同进程 user⇄kernel) 为何也有类似开销.

**理解要点**:

- Mode switch 进入内核后执行的是 **内核代码与内核数据**, 与用户程序工作集不同 → 挤占 / 污染 CPU cache (及可能的 TLB 行为差异)
- 返回用户态后, 用户工作集可能被部分换出 → **显著 cache miss**
- 不必整进程换地址空间也会有指令/数据 cache 扰动

**答题方向**: 强调「内核与用户工作集不同 + cache 污染/冷启动」, 而非「换了另一个用户进程」.

### (b) (10%) 专核跑内核, 其余核跑用户 — 能否减上述 cache 开销? 是否整体有益?

**题意**: 一核专供 kernel, 其他核只跑 user.

**理解要点**:

- **可能减轻**: 用户核少跑内核代码 → 用户工作集少被内核污染; 内核核上内核热
- **代价**: 系统调用/中断可能要跨核协作或把请求转到专核 → **延迟, 同步, 负载不均**; 少一核给用户; 现代 OS 并未普遍采用「整核专供内核」作为通用方案
- **结论倾向**: 对「同核 mode switch 污染」有局部好处, **整体未必值得** (需权衡吞吐/延迟/实现复杂度). 言之成理即可

---

## Question 2 — Mode/Context Switch (25)

### 场景摘要

单核; P running user; Q ready. P 调阻塞 `read` → `sys_read` 无数据 → P blocked, 调度 Q. 之后设备中断, handler 唤醒 P, 调度器 **立即** 跑 P.

### (a) (15%) 填执行历史中的 P/Q, user/kernel, mode/context switch

**建议逐步标:**

1. P user → 调 `read` 库 → **syscall** → **mode switch** → P kernel 执行 `sys_read`
2. 无数据 → P **blocked** → **context switch** → (return-from-trap 路径上换到 Q) → Q user
3. 设备 **interrupt** → **mode switch** → (当时跑 Q) Q kernel 跑 handler
4. 唤醒 P, 调度立即跑 P → **context switch** → P kernel 继续原 `sys_read`
5. `return-from-syscall` → **mode switch** → P user 回到 `read` 包装函数后续

**易错**: 阻塞时不仅 mode switch, 必有 **context switch** 到 Q; 中断进入时 CPU 上是 Q, handler 在 **Q 的 kernel 上下文** 中跑, 再 switch 到 P.

### (b1) (5%) 若 `read` 时数据已就绪, Q 在 ready — 还要不要 context switch?

**要点**: 不必. `sys_read` 可在 P 的内核路径直接完成并 return-from-trap 回 P user; 调度器无义务此时切换到 Q (非抢占点或策略未抢占).

### (b2) (5%) 中断唤醒 P 但调度器让 Q 继续跑 — 发生哪些 switch? P 状态?

**要点**: 中断仍有 **mode switch** 进内核跑 handler; 若选 Q 继续, **无** 换到 P 的 context switch (或 switch 完又回到 Q, 视实现). P 被唤醒后在 **ready** (不是 running, 也不是继续 blocked).

---

## Question 3 — Process Control (25)

Shell S: `fork` → 子 C `execve("/bin/echo", …)` → 父 `waitpid` → echo 退出 0.

### (a) (10%) `fork` 后、`exec` 前: 2 个逻辑共享属性 + 3 个不同属性

**共享例**: 打开文件描述符表副本/相同 fd 视图; 内存映射内容起初相同 (COW); 信号处理 disposition; cwd/umask 等 (任选符合课上的 2 个「逻辑共享」).

**不同例**: PID; `fork` 返回值; 各自地址空间副本 (写时复制后物理页可分); 运行状态/寄存器上下文; 堆栈内容独立演化.

### (b) (10%) `execve` 后: ≥3 被替换; ≥2 保持同一进程身份相关

**替换**: 代码段, 数据/堆/栈内容, 堆布局, 入口/PC, 多数原用户映射 — 换成 `echo` 映像.

**保持**: PID; 父 PID; 打开的 fd (默认, 除非 close-on-exec); 进程身份相关凭证等.

### (c) (5%) 父从不 `waitpid` → 可见什么抽象产物?

**僵尸进程 (zombie)**: 子已终止但 PCB/退出状态仍保留直到被 wait 回收.

---

## Question 4 — Process Scheduling (30)

### 设定

- P1 交互: (CPU 1ms + I/O 5ms)×5, 再 CPU 1ms; 总 CPU 6ms
- P2 CPU-bound: 连续 CPU 30ms
- \(t=0\) 两者 ready, **P1 在队前**

### (a-i) (8%) RR, quantum = 4ms — P1 的周转时间

**思路**:

- 时间线按 1ms 粒度或事件点画
- P1 每次只要 1ms CPU 就去 I/O; quantum=4 **不会** 在一次 burst 内抢占 P1 的 1ms
- P1 在 I/O 时 P2 可跑; P1 每次 I/O 完成回 ready 时与 P2 的 RR 次序要小心
- 周转 = P1 全部完成时刻 − 0

建议列表仿真: 记录 P1 完成 6 次 CPU burst 的时刻.

### (a-ii) (8%) MLFQ 三队列 q=2,4,10; 用尽片降级; 无 boost — P1 周转

**思路**:

- P1 每次 CPU 只需 1ms < 各层 quantum → **不会因用尽片而降级** (自愿 I/O 让出, 留同层; 与课件/OSTEP 规则一致)
- P1 倾向留在最高队列; P2 长跑会沉到低队列
- 因此 P1 应比在 RR 下更快反复获得 CPU

### (a-iii) (4%) 谁对 P1 更好?

比较两问算出的周转; 通常 **MLFQ 更好** (P1 保持高优先级). 用你的数字说话.

### (b) (10%) 如何用 Lottery 近似「总是跑最久没跑过的作业」(近似 LRU/最长等待)

**思路提示** (设计题):

- 给「等待更久 / 最近获得 CPU 更少」的作业 **更多票** 或随等待时间增加票
- 或: 每次被抽中后减少其票 / 增加他者票, 使长期没中奖者票权上升
- 说明如何随时间调整票数, 使调度偏好最长未运行者

---

## 提交提醒

- 看清虚拟分 vs 课程 6 分映射只是题面玩笑式说明; 按题面作答即可
- Q2 填空建议画时间线再填, 避免 mode/context 混用
- Q4 必须写出关键时间点, 否则难拿满
- 数字与填空表见 [`PS01 problem set 1 解答.md`](PS01%20problem%20set%201%20解答.md)
