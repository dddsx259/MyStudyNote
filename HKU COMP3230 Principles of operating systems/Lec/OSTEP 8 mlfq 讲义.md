# OSTEP Ch.8 Scheduling: The Multi-Level Feedback Queue — 阅读讲义

- **来源**: `Lec/OSTEP 8 mlfq.pdf` (12 页)
- **对齐课件**: `Lec/Lec06 scheduling.pdf` MLFQ 部分
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-mlfq.pdf

> **本章无教材 `.c` 示例程序**; 规则与升降级用文字/时间线说明. 配套仿真见 OSTEP homework, 非章内源码 Figure.

---

## Crux

如何在 **事先不知作业长度** 时, 既降低交互响应, 又近似缩短周转?

Tip: **从历史学习 (learn from history)** 预测未来 (相位行为可预测时有效).

---

## 基本规则

- Rule 1: $\mathrm{Priority}(A)>\mathrm{Priority}(B)$ → 跑 A
- Rule 2: 同优先级 → RR
- Rule 3: 新作业进 **最高** 优先级队列
- Rule 4 (最终版): 某层 **累计 CPU allotment 用尽** → 降一级 (不论是否中途 I/O)
- Rule 5: 每隔周期 $S$, **所有作业 boost 回顶层**

早期 Rule 4a/4b: 用尽片才降级; 自愿让出则留同层 — 易被 **gaming** (快到期就 I/O).

---

## 例子直觉

1. **长作业**: 从顶层逐步沉底, 之后在底层跑
2. **短作业插入**: 进顶层, 很快完成 → 近似 SJF
3. **交互 + I/O**: 频繁让出 → 保持高优先级 (在未改成累计记账前)

---

## 问题与对策

| 问题 | 对策 |
|---|---|
| 饿死 | Rule 5 priority boost |
| Gaming | 累计 allotment 记账 (Rule 4) |
| 行为从 CPU-bound 变交互 | boost 后重新「证明」自己 |
| 参数 ($S$, 层数, 片长) | Ousterhout: 避免 voo-doo constants 很难; 常靠经验/配置 |

下层常给 **更长 quantum** (高优先级短片切换快).

---

## Summary

MLFQ ≈ 不知长度时的 SJF/RR 折中; 课件与 Final 风格题常考降级规则与手算交互 vs CPU-bound.
