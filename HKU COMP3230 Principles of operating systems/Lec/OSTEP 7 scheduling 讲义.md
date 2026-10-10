# OSTEP Ch.7 Scheduling: Introduction — 阅读讲义

- **来源**: `Lec/OSTEP 7 scheduling.pdf` (13 页; 原名 `cpu-sched.pdf`)
- **对齐课件**: `Lec/Lec06 scheduling.pdf` (共用编号 **06**)
- **原书**: OSTEP Ch.7 v1.10; http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched.pdf

> 覆盖全章主线: workload 假设 → 指标 → FIFO/SJF/STCF/RR → I/O 重叠 → 不知长度的问题. 与课件共用算例思想; 课件另有 HRRN/MLFQ/Lottery 细节见对应讲义.
>
> **本章无教材 `.c` 示例程序** (调度用时间线图与算例说明); 算法步骤见各节. 仿真代码在 homework (`scheduler.py` 一类), 非章内 Figure.

---

## 0. Crux

如何建立思考调度策略的框架? 关键假设? 哪些指标? 早期系统用过哪些基本方法?

---

## 1. Workload Assumptions (§7.1)

简化作业 (job) 假设 (随后逐步放松):

1. 各作业运行时间相同
2. 同时到达
3. 一旦开始跑到完成
4. 只用 CPU (无 I/O)
5. 运行时间已知

---

## 2. Metrics (§7.2)

**周转时间**: $T_{\mathrm{turnaround}} = T_{\mathrm{completion}} - T_{\mathrm{arrival}}$.

另可谈公平 (如 Jain's index); **性能与公平常冲突**.

---

## 3. FIFO / FCFS (§7.3)

简单易实现. 等长作业同时到: 平均周转尚可.

放松「等长」: 长作业在前 → **护航效应 (convoy effect)** (短作业堵在长作业后). 例: A=100, B=C=10 → 平均周转 110.

---

## 4. SJF (§7.4)

**最短作业优先 (Shortest Job First)**: 先短后长. 上例平均周转可降至 50.

Tip: 超市「少于十件」通道即 SJF 思想.

非抢占 SJF: 若长作业已开始, 后到短作业仍须等 → 仍可能护航.

**证明思路**: 同时到达时 SJF 对平均周转最优 (交换论证); 系统课不要求形式证明.

---

## 5. STCF (§7.5)

**最短完成时间优先 (Shortest Time-to-Completion First)**: 抢占版 SJF. 新作业到时选剩余时间最短者.

例: A 跑到 $t=10$ 时 B,C 到 (各 10) → 抢占 A, 先跑完 B,C.

---

## 6. Response Time (§7.6)

$T_{\mathrm{response}} = T_{\mathrm{firstrun}} - T_{\mathrm{arrival}}$.

STCF/SJF 对周转好, 对交互响应可能差 (第三个同时到达的作业要等前两个跑完才首次得到 CPU).

---

## 7. Round Robin (§7.7)

按 **时间片 (time slice / quantum)** 轮转. 响应好; 周转常很差 (把作业拉长).

量子权衡: 太短 → 切换开销 (含缓存/TLB 冷启动); 太长 → 像 FIFO. **摊销 (amortization)**: 加长量子以摊薄切换固定成本.

公平的短尺度均分 CPU 策略, 天生不利于周转.

---

## 8. Incorporating I/O (§7.8)

作业做 I/O 时阻塞, CPU 可切去跑别的 → **重叠 (overlap)** 提高利用率. 把每次 CPU burst 视作调度单位; I/O 完成时作业重回 ready.

---

## 9. No More Omniscience (§7.9) → 通向 MLFQ

现实中不知道作业长度 → 不能直接 SJF/STCF. 下一章用 MLFQ **从历史学习**.

---

## 10. Summary

| 目标 | 倾向策略 |
|---|---|
| 周转 | SJF / STCF |
| 响应 | RR |
| 不知长度 + 两者兼顾 | MLFQ (Ch.8) |
