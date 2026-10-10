# Processor Scheduling: 处理器调度 (processor scheduling)

- **来源**: `Lec/Lec06 scheduling.pdf` (47 页)
- **课程**: COMP3230B Principles of Operating Systems
- **学习成果**: ILO 2a (进程/线程与 CPU 共享的机制与策略); ILO 3 (算法与性能)
- **必读**: OSTEP Ch.7, Ch.8; 参考 Ch.9 (比例份额), Ch.10 (多处理器)
- **对齐阅读讲义**: `OSTEP 7 scheduling 讲义.md`, `OSTEP 8 mlfq 讲义.md`, `OSTEP 9 lottery 讲义.md`

> 本讲覆盖 slides 全部知识点, 并用同一 workload 手算 FIFO/SJF/HRRN/STCF/RR (与课件表一致). Linux CFS 标「Not for examination」但仍摘要. 术语首次标英文.

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| 调度是什么 | 选下一个由处理器服务的进程/线程 |
| 三级调度 | 长/中/短 (job / swap / short-term) |
| 指标 | 周转时间 (turnaround), 等待时间 (waiting), 响应时间 (response), 吞吐 (throughput), 公平 (fairness) |
| 非抢占 | FIFO, SJF, HRRN |
| 抢占 | STCF, RR, MLFQ, 彩票 (lottery) |
| Crux | 既要好响应又要好周转, 且事先不知 burst |
| 多核 | 单队列 vs 每核队列 + 工作窃取 (work stealing) |

---

## 1. 何谓 Processor Scheduling (p.5)

**处理器调度 (processor scheduling)**: 选择下一个由处理器服务的进程/线程的活动.

策略影响:

1. **对用户的 QoS / 体感性能**
2. **资源有效利用** (切换昂贵, 决策影响 CPU 利用)
3. **系统性能** (单位时间完成的进程数 → 吞吐)

---

## 2. Scheduling Levels (p.6)

| 层级 | 别名 | 管什么 |
|---|---|---|
| High-level | Job / Long-term | 是否创建新进程; 控制多道程度 (degree of multiprogramming) |
| Intermediate | Medium-term | 哪些进程可争用 CPU; 与换入换出 (swapping) 相关 |
| Low-level | Short-term | **下一步跑谁** (本讲重点) |

---

## 3. 术语与指标 (p.7–8)

### 3.1 CPU-bound vs I/O-bound

- **CPU-bound (compute-bound) 进程**: 跑起来倾向于吃光分给它的处理器时间
- **I/O-bound 进程**: 跑起来只短暂用 CPU 就发 I/O 并让出处理器

另一定义 (课件旁注): 若 CPU 更快则程序明显变快 → CPU-bound; 若 I/O 子系统更快则变快 → I/O-bound.

### 3.2 性能指标 (定义, 无需证明)

设作业到达时刻 $T_{\mathrm{arrival}}$, 首次运行时刻 $T_{\mathrm{firstrun}}$, 完成时刻 $T_{\mathrm{completion}}$.

| 指标 | 公式 | 目标 |
|---|---|---|
| **周转时间 (turnaround time)** | $T_{\mathrm{turnaround}} = T_{\mathrm{completion}} - T_{\mathrm{arrival}}$ | 最小化 |
| **等待时间 (waiting time)** | 在就绪队列 (ready queue) 中等待的时间 | 最小化 |
| **响应时间 (response time)** | $T_{\mathrm{response}} = T_{\mathrm{firstrun}} - T_{\mathrm{arrival}}$ | 最小化 (交互任务关键) |
| **吞吐 (throughput)** | 单位时间完成的进程数 | 最大化 |
| **公平 (fairness)** | 同类作业同等对待; 不同优先级也不应无限推迟 (starvation) | 避免饿死 |

> 课件注: 在若干非抢占设定下, response time 与 wait time 数值可相同; RR 等抢占下二者通常不同.

---

## 4. When to Schedule (p.9)

调度器可在这些时刻做决策:

1. 新进程创建
2. 进程退出
3. 进程因 I/O 或其他事件阻塞 (block)
4. 进程发起系统调用 (system call)
5. 中断 (interrupt) 发生: I/O 中断使阻塞进程变 ready; **时钟中断 (clock interrupt)** 周期性唤醒调度器

---

## 5. Workload Assumptions (p.10)

评估用简化假设 (与 OSTEP Ch.7 对齐):

1. 作业只使用 CPU (无 I/O); 有 I/O 时可将各 **CPU burst** 当作独立作业
2. 每个进程的运行时长 (CPU burst) **事先已知** (为分析方便; 现实中往往未知 → MLFQ)

---

## 6. Algorithm Evaluation: Deterministic Modeling (p.11)

**确定性建模 (deterministic modeling)**: 给定预定 workload, 比较各算法性能.

### 本讲统一例子 (后续算法共用)

| Process | Arrival Time | CPU burst |
|---|---|---|
| A | 0 | 3 |
| B | 2 | 6 |
| C | 4 | 4 |
| D | 6 | 5 |
| E | 8 | 2 |

约定: 新进程总在时钟滴答 **刚开始前** 到达 (课件: *just before the clock tick*).

---

## 7. First-In-First-Out / FCFS (p.12–14)

**先来先服务 (First-In-First-Out, FIFO; 亦称 First Come First Served, FCFS)**:

- 按到达时间排队
- **非抢占 (non-preemptive)**: 一旦获得 CPU, 跑到完成或自愿让出

**优点**: 公平 (同等对待), 易实现.

### 7.1 手算 (课件 p.13)

时间线 (CPU 上跑谁):

| Time | Ready Queue (示意) | CPU |
|---|---|---|
| 0 | — | A |
| 2 | B | A |
| 3 | B | B |
| 4 | C | B |
| 6 | C, D | B |
| 8 | C, D, E | B |
| 9 | D, E | C |
| 13 | E | D |
| 18 | — | E |
| 20 | — | (空) |

完成时刻: A=3, B=9, C=13, D=18, E=20.

$$
\begin{align*}
T_A &= 3-0=3,\quad T_B=9-2=7,\quad T_C=13-4=9,\\
T_D &= 18-6=12,\quad T_E=20-8=12
\end{align*}
$$

**平均周转**: $(3+7+9+12+12)/5 = 8.6$.

Response (本例 = 首次运行前等待): A=0, B=1, C=5, D=7, E=10; 平均 $4.6$.

### 7.2 缺点

- 短作业排在长 CPU-bound 后面 → **护航效应 (convoy effect)** 直觉
- 对交互作业不友好

---

## 8. Shortest-Job-First / SJF (p.15–17)

**最短作业优先 (Shortest Job First, SJF; 亦称 Shortest Process First)**: 非抢占; 选预计 CPU burst **最短** 的就绪进程.

**优点**: 平均等待通常优于 FIFO; 已知可证明在「同时到达 + 已知长度」下对平均周转最优 (OSTEP; 系统课不要求形式证明).

**证明思路 (最优性直觉)**: 若调度违反 SJF (先跑较长的 $L$ 再跑较短的 $S$), 交换二者后, $S$ 完成更早且总体等待/周转之和不增; 反复交换得到 SJF.

### 8.1 手算 (p.16)

| Time | 说明 |
|---|---|
| 0–3 | 只有 A → 跑 A |
| 3 | B 已到, 跑 B (唯一 ready) |
| 8 | B 仍在跑时 E 到达; B 非抢占继续到 9 |
| 9 | ready: C(4), D(5), E(2) → 选 **E** |
| 11 | 选 C(4) |
| 15 | 选 D |

完成: A=3, B=9, E=11, C=15, D=20.

周转: A=3, B=7, C=11, D=14, E=3; **平均 $7.6$**.

Response: A=0, B=1, C=7, D=9, E=1.

### 8.2 缺点

- 非抢占 → 新到的短/交互作业可能等长 CPU-bound 跑完
- 长作业可能 **饿死 (starvation)** (总有更短作业)
- 等待时间方差可能大; 交互场景不佳

---

## 9. Highest-Response-Ratio-Next / HRRN (p.18–19)

**最高响应比优先 (Highest Response Ratio Next, HRRN)**: 非抢占; 改进 SJF, 把已等待时间纳入优先级, 用 **老化 (aging)** 防无限推迟.

$$
\mathrm{priority} = \frac{\mathrm{time\ waiting} + \mathrm{service\ time}}{\mathrm{service\ time}} = \frac{\mathrm{time\ waiting}}{\mathrm{service\ time}} + 1
$$

短作业仍被偏好 (分母小); 久等的长作业比值升高.

### 9.1 手算要点 (p.19)

前段与 SJF 类似跑完 A,B 后到 $t=9$, ready: C,D,E.

算响应比 (课件): C: $(5+4)/4=2.25$; D: $(3+5)/5=1.6$; E: $(1+2)/2=1.5$ → 选 **C**.

之后 D vs E: D: $(7+5)/5=2.4$; E: $(5+2)/2=3.5$ → 选 **E**, 再 D.

平均周转 **$8$**; Response: A=0, B=1, C=5, D=9, E=5.

---

## 10. Shortest Time-to-Completion First / STCF (p.20–22)

**最短完成时间优先 (Shortest Time-to-Completion First, STCF)**: SJF 的 **抢占** 版 (亦称 Preemptive SJF, PSJF).

- 新到达触发: 比较 **剩余运行时间** $\mathrm{remaining} = \mathrm{CPU\ burst} - \mathrm{elapsed}$
- 选 remaining 最短者; 须维护已服务时间

### 10.1 手算 (p.21)

| Time | 事件 | CPU |
|---|---|---|
| 0 | A 到 | A |
| 2 | B 到; A remaining=1 < B=6 | A 继续 |
| 3 | A 完 | B |
| 4 | C 到, rem=4 < B rem=5 | **抢占** → C |
| 6 | D 到, rem=5; C rem=2 | C 继续 |
| 8 | E 到 rem=2; C 恰跑完? 课件: $t=8$ 时 C 已用 4, 完于 8; 选 E(2) | E |
| 10 | E 完; B rem=5, D rem=5 | 课件选 B |
| 15 | B 完 | D → 20 |

课件平均周转 **$7.2$**; Waiting: A=0,B=7,C=0,D=9,E=0; Response: A=0,B=1,C=0,D=9,E=0.

### 10.2 缺点

- 长作业等待方差更大 (可被多次抢占)
- 快完成的作业可被新到短作业打断 → 更多上下文切换 (context switch)
- 未必总「最优」于一切指标

---

## 11. Round-Robin / RR (p.23–25)

**时间片轮转 (Round Robin, RR)**:

- Ready 队列 FIFO; 新到的进队尾
- 每进程只跑 **时间片 / 量子 (time slice / quantum)**
- 时钟中断时若量子用尽 → 入队尾, 取下一 ready

**优点**: 公平; 对交互友好 (响应好).

### 11.1 手算: Quantum = 1 (p.24)

课件给出平均周转 **$10.8$**; Waiting 平均 $6.8$; Response 平均 **$0.8$** (各算法中最好之一).

Response: A=0, B=0, C=1, D=1, E=2.

### 11.2 Quantum 取舍

| Quantum | 效果 |
|---|---|
| 过大 | 退化成 FIFO |
| 过小 | 上下文切换开销主导 |
| 适中 | 够交互作业发 I/O; 长作业仍拿大部分 CPU |

课件另给 Quantum=2 时周转约 $10$, 等待 $6$, 响应 $1.8$ (与表对照).

**对比表 (课件汇总, 本 workload)**:

| 算法 | Avg Turnaround | Avg Waiting | Avg Response |
|---|---|---|---|
| FIFO | 8.6 | 4.6 | 4.6 |
| SJF | 7.6 | 3.6 | 3.6 |
| HRRN | 8 | 4 | 4 |
| STCF | 7.2 | 3.2 | 2 |
| RR (q=1) | 10.8 | 6.8 | 0.8 |

**直觉**: 优化周转 ↔ 对短作业偏心 (可能对响应不公); 优化响应 ↔ 公平分片 (周转变差).

---

## 12. The Crux (p.26)

如何设计调度器, 同时:

1. **最小化交互作业响应时间** (像 RR)
2. **在事先不知 CPU burst 时仍近似 SJF/STCF 的周转**

→ 引出优先级与 **多级反馈队列 (Multi-Level Feedback Queue, MLFQ)**.

---

## 13. Priority Scheduling (p.27)

- 每进程/线程一个优先级号; 调度器偏爱高优先级
- **静态优先级 (static priority)**: 一生不变 — 实现简单, 但不适应环境; 低优先级易饿死
- **动态优先级 (dynamic priority)**: 可随行为变 — 更灵敏, 但每次决策开销更大

---

## 14. Multilevel Feedback Queues / MLFQ (p.28–34)

历史: Corbató 等 CTSS (1962); 与 Multics 工作相关, 获图灵奖 (Turing Award, 1990).

### 14.1 结构

- 多个 ready 队列, **不同优先级**
- 总是先跑最高非空队列中的进程
- **同队列内 Round Robin**
- **动态** 按运行时行为改优先级: 用历史预测未来 (learn from history)

### 14.2 赋优先级规则 (课件 Attempt)

1. **新作业进最高优先级队列**
2. **用尽本层 quantum** → 降到下一层队尾
3. **在 quantum 用尽前自愿让出 CPU** (如 I/O) → **留在同层** (不惩罚交互)
4. 长作业逐渐沉到底层

### 14.3 课件动作例子 (p.31)

- P0: 长作业, $t=0$ 到达
- P1: 交互, $t=200$ 到; CPU 20 后 I/O 100, 循环
- 每层 quantum = 50

直觉: P0 逐步沉底; P1 因频繁让出而保持高优先级, 穿插在 P0 低优先级运行之间.

### 14.4 缺陷 (p.32)

1. **饿死**: 太多交互吃光 CPU, 底层长作业不跑
2. **作弊 (gaming)**: 故意在 quantum 结束前 yield/I/O, 假装短作业
3. **行为相位变化**: CPU-bound 变交互后可能已沉底, 得不到正确待遇

### 14.5 调整 (p.33–34)

| 问题 | 对策 |
|---|---|
| 饿死 / 行为变化 | 周期 **优先级提升 (priority boost)**: 每周期 $S$ 把所有进程移回顶层 |
| 下层量子 | 越低层 quantum 越大 (如翻倍): 高优先级短片, 低优先级长片 |
| 作弊 | **按累计 allotment 记账**: 不论几次短跑, 某层 CPU 配额用尽就降级 (OSTEP Rule 4) |

配置问题 (voo-doo constants): 几层? 每层片长? 多久 boost? 例: Solaris 约 60 队列, 20ms 片, ~1s boost.

**MLFQ 是自适应机制 (adaptive mechanism)** 的好例子: 随交互/批处理行为在队列间移动.

---

## 15. Fair Share / Lottery (p.35–37)

**公平份额调度 (Fair Share Scheduling, FSS)**: 决策基于 **用户/组** 权重, 而非仅单个进程 (防「多开进程霸占」).

**彩票调度 (Lottery Scheduling)**: 用随机实现比例份额 (proportional share).

- 按份额发 **彩票 (tickets)** (如 10% → 100 张中 10 张)
- 每次抽随机赢家 → 跑对应进程
- 长期: 持有比例 $f$ 的票 ≈ 得比例 $f$ 的 CPU
- 例: A 75 票 (0–74), B 25 票 (75–99); 随机序列 → 调度串 (课件 p.37)

---

## 16. Multiprocessor Scheduling (p.38–41)

### 16.1 单队列 (Single-Queue Scheduling)

所有核共享一个 ready 队列.

**问题**:

1. **可扩展性差**: 队列须加锁 → 核多 → 争用
2. **缓存亲和 (cache affinity)**: 作业在核间乱跳 → 反复冷缓存/TLB

### 16.2 多队列 (Multi-Queue Scheduling)

**每核一个队列**; 入队用启发式 (随机或选较短队列).

**优点**: 少锁争用; 保持亲和.

**问题**: **负载不均 (load imbalance)** → **工作窃取 (work stealing)**: 空闲/轻载队列偷看并偷走重载队列作业. 「多空算 low」阈值仍是艺术.

---

## 17. Case Study: Linux Scheduler (p.42–46, *Not for examination*)

摘要备查 (考试非重点):

- 抢占 + 优先级; 实时类 vs 普通类
- 实时: `SCHED_FIFO`, `SCHED_RR`; 普通用户通常不能建实时进程
- **完全公平调度器 (Completely Fair Scheduler, CFS)** (2.6.23+): 用 **虚拟运行时 (virtual runtime)**; 选 vruntime 最小者; 红黑树 (red-black tree) $O(\log n)$; nice 映射权重

---

## 18. Summary (p.47)

- 策略决定何时、跑多久; 涉及抢占性, 量子, 优先级, 周转, 公平
- MLFQ: 用过去预测未来的典范
- FSS/Lottery: 保证份额
- 现代多核: 每核队列保亲和, 须做负载均衡

---

## 易错点

1. **Response ≠ Turnaround**: 前者看「何时第一次跑」, 后者看「何时完成」
2. **SJF 非抢占 / STCF 抢占**: 新到短作业能否打断正在跑的长作业, 是二者分水岭
3. **RR 周转常最差之一**: 把每个作业「拉长」完成
4. **MLFQ 留同层 vs 降级**: 自愿让出 ≠ 用尽 quantum; 防作弊靠累计配额
5. **Mode/context switch 开销** 与调度量子权衡: 片太短切换吃 CPU
