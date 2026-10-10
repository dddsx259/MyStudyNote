# 题集 — Lec01 Introduction

> 对齐: `Lec/Lec01 introduction slides 讲义.md`.
> 含: (1) 课件证明 (2) 练习题 (作业/Tut/课件例).

## 课件证明

### P1. 最大化改最小化 (maximization as minimization)

- **陈述**: 对可行域 $C$ 与 $f:C\to\mathbb{R}$, 有 $\max_{x\in C} f(x)=-\min_{x\in C}(-f(x))$.
- **证明**: 设 $M=\max_{x\in C} f(x)$ (若不存在则两边均为 $+\infty$, 同理处理 $-\infty$). 对任意 $x\in C$, $f(x)\le M$ 当且仅当 $-f(x)\ge -M$. 故 $-M$ 是 $-f$ 在 $C$ 上的最大下界, 且存在 $x^*$ 达到 $f(x^*)=M$ 当且仅当 $-f(x^*)=-M$ 达到 $-f$ 的最小值. 因此 $\max f=-\min(-f)$.
- **来源**: Lec01 §1 / 讲义

### P2. 魏尔斯特拉斯定理 (Weierstrass theorem)

- **陈述**: $C\subseteq\mathbb{R}^d$ 非空**紧**, $f$ 在 $C$ 上连续 $\Rightarrow$ 存在 $x^*\in C$ 为 $f$ 的全局极小点.
- **证明**: 连续映射将紧集映为紧集, 故 $f(C)\subseteq\mathbb{R}$ 紧, 即闭且有界. 闭集包含其最小值, 故 $m:=\min f(C)$ 存在. 取 $x^*\in C$ 使 $f(x^*)=m$, 则 $f(x^*)\le f(x)$ 对所有 $x\in C$, 即 $x^*$ 为全局极小点. (等价证法: 取极小化序列 $f(x_n)\to\inf_{x\in C}f(x)$; 紧性抽收敛子列 $x_{n_j}\to\bar x\in C$, 连续性得 $f(\bar x)=\inf f$.)
- **来源**: Lec01 §2 / 讲义

### P3. $\mathbb{R}^d$ 中紧 $\Leftrightarrow$ 闭且有界 (Heine–Borel)

- **陈述**: $C\subseteq\mathbb{R}^d$ 紧当且仅当 $C$ 闭且有界.
- **证明**: 超出本课已授范围; 讲义直接使用 Heine–Borel (开覆盖有限子覆盖等价于闭有界). 本课在 $\mathbb{R}^d$ 中判紧性时用「闭 + 有界」即可.
- **来源**: Lec01 §2 / 讲义

### P4. Sigmoid 与对数几率 (log-odds)

- **陈述**: 若 $\log\frac{P(y=1\mid a)}{P(y=-1\mid a)}=a^T x$, 则对 $y\in\{+1,-1\}$, $P(y\mid a)=\sigma(y a^T x)=\frac{1}{1+e^{-y a^T x}}$.
- **证明**: 令 $p=P(y=1\mid a)$, 则 $\log\frac{p}{1-p}=a^T x$, 故 $\frac{p}{1-p}=e^{a^T x}$, 解得 $p=\frac{e^{a^T x}}{1+e^{a^T x}}=\sigma(a^T x)$. 当 $y=+1$, $P(y\mid a)=\sigma(a^T x)=\sigma(y a^T x)$; 当 $y=-1$, $P(y=-1\mid a)=1-\sigma(a^T x)=\sigma(-a^T x)=\sigma(y a^T x)$.
- **来源**: Lec01 §3 / 讲义

### P5. 负对数似然 $\Rightarrow$ $\log(1+e^{-z})$ (NLL)

- **陈述**: $\sigma(z)=\frac{1}{1+e^{-z}}$ 时, $-\log\sigma(z)=\log(1+e^{-z})$; 独立样本下 ERM 目标为 $\frac{1}{n}\sum_i\log(1+e^{-y_i a_i^T x})$.
- **证明**: $-\log\sigma(z)=-\log\frac{1}{1+e^{-z}}=\log(1+e^{-z})$. 单样本 NLL 为 $-\log P(y_i\mid a_i)=\log(1+e^{-y_i a_i^T x})$. 独立样本联合似然 $\prod_i P(y_i\mid a_i)$, 取负对数并平均即得讲义目标.
- **来源**: Lec01 §3 / 讲义

### P6. 链式法则 (chain rule)

- **陈述**: $F(x)=g(h(x))$, $h:\mathbb{R}^d\to\mathbb{R}^m$ 可微, $g$ 在 $h(x)$ 可微 $\Rightarrow$ $\nabla F(x)=J_h(x)^T\nabla g(h(x))$, $J_h$ 行为 $\nabla h_j(x)^T$.
- **证明**: 可微给出 $h(x+s)=h(x)+J_h(x)s+o(\lVert s\rVert)$, $g(h(x+s))=g(h(x))+\nabla g(h(x))^T(h(x+s)-h(x))+o(\lVert h(x+s)-h(x)\rVert)$. 代入一次项: $F(x+s)-F(x)=\nabla g(h(x))^T J_h(x)s+o(\lVert s\rVert)$. 由梯度定义 $\nabla F(x)^T s$ 等于 $s$ 的一次系数, 故 $\nabla F=J_h^T\nabla g$.
- **来源**: Lec01 §5 / 讲义

### P7. 线性回归 MSE 梯度

- **陈述**: $F(x)=\frac{1}{2n}\lVert Ax-y\rVert^2$ $\Rightarrow$ $\nabla F(x)=\frac{1}{n}A^T(Ax-y)$.
- **证明**: $F=\frac{1}{2n}(Ax-y)^T(Ax-y)$. 微分 $\mathrm{d}F=\frac{1}{n}(Ax-y)^T A\,\mathrm{d}x$, 故 $\nabla F=\frac{1}{n}A^T(Ax-y)$. (等价: $F=\frac{1}{2n}\sum_i(a_i^T x-y_i)^2$, 对 $x_j$ 求导得 $\frac{1}{n}\sum_i(a_i^T x-y_i)a_{ij}$, 合成即 $A^T(Ax-y)/n$.)
- **来源**: Lec01 §5 / 讲义

### P8. 正规方程 (normal equation)

- **陈述**: 若 $A^TA$ 可逆, $F(x)=\frac{1}{2n}\lVert Ax-y\rVert^2$ 的唯一极小点为 $x^*=(A^TA)^{-1}A^T y$.
- **证明**: 由 P7, $\nabla F(x)=0$ $\Leftrightarrow$ $A^TAx=A^Ty$. $A^TA$ 可逆时解唯一为 $x^*=(A^TA)^{-1}A^Ty$. 系数 $\frac{1}{2n}$ 不改变梯度零点.
- **来源**: Lec01 附录 A / 讲义

### P9. 沿直线段的微积分基本定理 (FTC along a line)

- **陈述**: 对 $f$ 可微, $u,v\in\mathbb{R}^d$,
  $$f(v)-f(u)=\int_0^1 \nabla f\bigl(u+t(v-u)\bigr)^T(v-u)\,dt.$$
- **证明**: 令 $\phi(t)=f(u+t(v-u))$, $t\in[0,1]$. 链式法则 $\phi'(t)=\nabla f(u+t(v-u))^T(v-u)$. 一维 FTC: $\phi(1)-\phi(0)=\int_0^1\phi'(t)\,dt$, 即结论.
- **来源**: Lec01 §6 / 讲义

### P10. 一阶泰勒展开 (first-order Taylor)

- **陈述**: $f$ 在 $x$ 可微 $\Rightarrow$ $f(x+s)=f(x)+\nabla f(x)^T s+o(\lVert s\rVert)$ ($s\to 0$).
- **证明**: 可微的定义即: 存在线性映射 $s\mapsto\nabla f(x)^T s$ 使余项 $o(\lVert s\rVert)$. 等价地, 沿方向 $s/\lVert s\rVert$ 的方向导数极限为 $\nabla f(x)^T s$.
- **来源**: Lec01 §6 / 讲义

### P11. 二阶泰勒展开 (second-order Taylor)

- **陈述**: $f$ 在 $x$ 附近 $C^2$ $\Rightarrow$ $f(x+s)=f(x)+\nabla f(x)^T s+\frac{1}{2}s^T\nabla^2 f(x)s+o(\lVert s\rVert^2)$.
- **证明**: 令 $\phi(t)=f(x+ts)$, $t\in\mathbb{R}$. 一维二阶 Taylor: $\phi(1)=\phi(0)+\phi'(0)+\frac{1}{2}\phi''(0)+o(1)$. 计算 $\phi'(0)=\nabla f(x)^T s$, $\phi''(0)=s^T\nabla^2 f(x)s$, 代入即得 ($s$ 固定, $t\to 0$ 时余项 $o(\lVert s\rVert^2)$).
- **来源**: Lec01 §6 / 讲义

## 练习题

### 1. 最大化改最小化

- **题目**: 说明为何 $\max_{x\in C}f(x)=-\min_{x\in C}(-f(x))$.
- **思路**: $f(x)\le M\Leftrightarrow -f(x)\ge -M$; 最优值差一个负号.
- **来源**: Lec01 §1 / `Lec/Lec01 introduction slides 讲义.md`

### 2. Weierstrass: 缺紧性时无极小

- **题目**: 给出连续 $f$ 在非紧 $C$ 上无全局极小的例子 (缺有界或缺闭).
- **思路**: 如 $C=\mathbb{R}$, $f(x)=e^x$ (有下界无极小); 或 $C=(0,1]$, $f(x)=x$ (inf 在边界外).
- **来源**: Lec01 Weierstrass 讨论 / HW1 Q1(a) 同类

### 3. T/F: $C^1$ 有下界 $\Rightarrow$ 有全局极小

- **题目**: 判断真假并说明: 若 $f\in C^1(\mathbb{R}^d)$ 且有下界, 则必有全局极小.
- **思路**: **假**. 反例 $e^x$ (或 $e^{\lVert x\rVert}$): 有下界无达到.
- **来源**: HW1 Q1(a) / `assignment/Assignment01 题目理解.md`

### 4. 典型模型写出目标

- **题目**: 写出线性回归 / 逻辑回归 / 硬间隔 SVM / Lasso 的优化形式 (决策变量, 目标, 约束若有).
- **思路**: 回归 MSE $\frac1{2n}\lVert Ax-y\rVert^2$; 逻辑 NLL $\frac1n\sum\log(1+e^{-y_ia_i^Tx})$; SVM $\min\frac12\lVert x\rVert^2$ s.t. $y_ia_i^Tx\ge 1$; Lasso 加 $\lambda\lVert x\rVert_1$.
- **来源**: Lec01 模型节 / cheatsheet「典型模型」
