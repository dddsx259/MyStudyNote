# 题集 — Ch05 Poisson Processes

> 对齐: `Lec/Lec05 probability theory lecture notes Ch05 讲义.md`.
> 含: (1) 练习题 (2) 课件证明.

## 课件证明

### P1. 指数尾概率与矩 (Exp moments)

- **陈述**: **假设** $X\sim\mathrm{Exp}(\lambda)$; **结论** $P(X>x)=e^{-\lambda x}$, $EX=1/\lambda$, $\mathrm{Var}(X)=1/\lambda^2$, $M(u)=\lambda/(\lambda-u)$ ($u<\lambda$).
- **证明**: 直接积分; $EX^2=2/\lambda^2$.
- **来源**: `Lec/Lec05 probability theory lecture notes Ch05 讲义.md` §5.1

### P2. 指数无记忆

- **陈述**: **结论** $P(X>s+t\mid X>s)=P(X>s)$.
- **证明**: 比值为 $e^{-\lambda(s+t)}/e^{-\lambda s}$.
- **来源**: 同上 §5.1

### P3. 泊松过程边际 $N(t)\sim\mathrm{Poisson}(\lambda t)$

- **陈述**: **假设** 定义 A (独立增量, $N(s+t)-N(s)\sim\mathrm{Poisson}(\lambda t)$); **结论** $EN(t)=\mathrm{Var}(N(t))=\lambda t$.
- **证明**: 取 $s=0$.
- **来源**: 同上 §5.2

### P4. 两定义等价 (Thm. 5.2.6)

- **陈述**: 定义 A (Poisson 增量) 与定义 B (无穷小) 等价.
- **证明**: 超出本课已授范围; 讲义给出微分方程 / MGF 思路, 未逐步展开. B$\Rightarrow$A: $p_0'=-\lambda p_0\Rightarrow p_0=e^{-\lambda t}$, 归纳 $p_k=e^{-\lambda t}(\lambda t)^k/k!$.
- **来源**: 同上 §5.2

### P5. 间隔时间 i.i.d. Exp($\lambda$) (Thm. 5.3.1)

- **陈述**: **假设** 齐次泊松速率 $\lambda$; **结论** $T_1,T_2,\ldots$ i.i.d. $\sim\mathrm{Exp}(\lambda)$.
- **证明**: $P(T_1>t)=P(N(t)=0)=e^{-\lambda t}$; 无记忆 / 强马尔可夫于跳跃 $\Rightarrow$ 重启后仍 Exp 且独立, 归纳.
- **来源**: 同上 §5.3

### P6. 到达时间 Gamma 与计数等价

- **陈述**: **结论** $S_n\sim\mathrm{Gamma}(n,\lambda)$, $\{S_n\le t\}=\{N(t)\ge n\}$.
- **证明**: i.i.d. Exp 和; 事件等价由定义.
- **来源**: 同上 §5.3

### P7. 泊松叠加

- **陈述**: **假设** 独立速率 $\lambda_1,\lambda_2$ 的泊松过程; **结论** 和过程速率 $\lambda_1+\lambda_2$, 合并点来自源 1 的概率 $\lambda_1/(\lambda_1+\lambda_2)$.
- **证明**: 独立 Poisson 和; 给定 $dt$ 内恰一事件, 条件概率 $\lambda_1 dt/((\lambda_1+\lambda_2)dt)$.
- **来源**: 同上 §5.4

### P8. 指数竞赛

- **陈述**: **假设** $X_i\sim\mathrm{Exp}(\lambda_i)$ 独立; **结论** $\min_i X_i\sim\mathrm{Exp}(\sum_i\lambda_i)$, $P(X_i=\min)=\lambda_i/\sum_j\lambda_j$.
- **证明**: $P(\min>t)=\prod_i e^{-\lambda_i t}$; 两变量时积分 $P(X_1<X_2)=\lambda_1/(\lambda_1+\lambda_2)$.
- **来源**: 同上 §5.5

### P9. 条件 $N(t)=1$ 时 $S_1$ 均匀

- **陈述**: **结论** $S_1\mid(N(t)=1)\sim\mathrm{Unif}[0,t]$.
- **证明**: $P(S_1\le s\mid N(t)=1)=(\lambda s e^{-\lambda s})e^{-\lambda(t-s)}/(\lambda t e^{-\lambda t})=s/t$.
- **来源**: 同上 §5.6

### P10. 次序统计量联合密度

- **陈述**: **假设** i.i.d. 密度 $f$; **结论** 有序样本 $(Y_{(1)},\ldots,Y_{(n)})$ 联合密度 $n!\prod f(y_i)$ (有序区域).
- **证明**: 无序联合密度 $\prod f(y_i)$, $n!$ 个排列原像 (连续几乎必然无结).
- **来源**: 同上 §5.6

### P11. 条件到达 = 均匀次序统计 (Thm. 5.6.4)

- **陈述**: **假设** 齐次 Poisson; **结论** 给定 $N(t)=n$, $(S_1,\ldots,S_n)$ 同分布于 $n$ 个 i.i.d. $\mathrm{Unif}[0,t]$ 的次序统计量.
- **证明**: 写出无序间隔联合概率, 除以 $P(N(t)=n)$, 得条件密度 $n!/t^n$ on 有序单纯形.
- **来源**: 同上 §5.6

### P12. 非齐次均值函数

- **陈述**: **假设** 强度 $\lambda(t)$, $m(t)=\int_0^t\lambda(s)\,ds$; **结论** $N(t)-N(s)\sim\mathrm{Poisson}(m(t)-m(s))$, $EN(t)=m(t)$.
- **证明**: 超出本课已授范围; 讲义仅陈述 / $p_0'= -\lambda(t)p_0$ 或时间变换 $\tau=m(t)$.
- **来源**: 同上 §5.7

## 练习题

### 1. 两定义互通

- **题目**: 用小 $h$ 展开验证 Poisson 过程 infinitesimal 定义与独立增量 + Poisson 计数等价.
- **思路**: $P(N(h)=1)=\lambda h+o(h)$ 等.
- **来源**: Lec Ch05 例题要点

### 2. 移民 Poisson 计数

- **题目**: (讲义) 4 周 $\times$ 10 人, 强度 $1/12$ $\Rightarrow$ 某段到达 $\mathrm{Poisson}(10/3)$.
- **思路**: 独立 Poisson 叠加, 参数相加.
- **来源**: Lec Ch05 例题要点

### 3. 指数竞赛

- **题目**: 独立 Exp 率 $\lambda_i$, 求类型 $i$ 最先完成概率.
- **思路**: $P_i=\lambda_i/\sum_j\lambda_j$.
- **来源**: Lec Ch05 例题要点

### 4. 条件到达均匀

- **题目**: 齐次 Poisson, $N(t)=n$ 条件下 $n$ 个到达时刻分布.
- **思路**: 等价 $n$ 个 i.i.d. $\mathrm{Unif}[0,t]$ 次序统计量.
- **来源**: Lec Ch05 例题要点

### 5. 非齐次均值

- **题目**: 强度 $\lambda(s)$, 求 $E[N(t)-N(s)]$.
- **思路**: $\int_s^t\lambda(u)\,du$; 非常值勿用 $\lambda(t)(t-s)$.
- **来源**: Lec Ch05 例题要点
