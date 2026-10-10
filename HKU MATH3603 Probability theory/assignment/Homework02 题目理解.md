# Homework 2 题目理解: 离散/连续 RV, 极值 CDF, 生日, 单位圆盘

- **来源**: `assignment/Homework02.pdf`
- **课程**: MATH3603 Probability Theory
- **Due**: 2026-10-08
- **参考**: Lecture notes Ch.2 (RV, PMF/PDF, expectation, variance); 指示函数 / 示性随机变量技巧

---

## 总目标

1. 抛硬币 $n$ 次, $X=$ 正面数减反面数: 取值集与 $n=3$ 公平币的 PMF.
2. 给定密度形状求归一化常数 $c$, 区间概率, $E(X)$, $\mathrm{Var}(X)$.
3. i.i.d. 同分布 $F$ 的样本, 求 $\max$ / $\min$ 的 CDF.
4. 100 人生日 (365 天均匀独立), $X=$ 不同生日个数; 用示性变量求 $EX$, $\mathrm{Var}(X)$.
5. 单位圆盘上均匀点: 求密度常数 $C$ 与 $X$ 的边缘密度.

---

## 第 1 题 — 正反面差

**设定**: 抛 $n$ 次; $X=$ (#heads) $-$ (#tails).

### (i) 可能取值

**理解**: 若 $H$ 次正面, 则反面 $n-H$, $X=H-(n-H)=2H-n$. $H\in\{0,\ldots,n\}$ $\Rightarrow$ $X\in\{-n,-n+2,\ldots,n-2,n\}$ (与 $n$ 同奇偶).

### (ii) $n=3$ 公平币 PMF

**理解**: $H\sim\mathrm{Bin}(3,1/2)$, $X=2H-3$. 列出 $X=-3,-1,1,3$ 对应概率.

---

## 第 2 题 — 二次型密度

$f(x)=c(4x-2x^2)$ 于 $0<x<2$, 否则 $0$.

### (a)(b)(c)

- (a) $\int_0^2 f=1$ 定 $c$.
- (b) $P(1/2<X<3/2)=\int_{1/2}^{3/2}f$.
- (c) $E(X)=\int xf$, $E(X^2)=\int x^2f$, $\mathrm{Var}=E(X^2)-(EX)^2$.

---

## 第 3 题 — max / min 的 CDF

$X_1,\ldots,X_n$ i.i.d., 共同 CDF $F$.

**理解**:
$$
P(\max\le x)=F(x)^n,\qquad P(\min>x)=(1-F(x))^n,
$$
故 $F_{\max}(x)=F(x)^n$, $F_{\min}(x)=1-(1-F(x))^n$.

---

## 第 4 题 — 不同生日个数

**提示**: $X=\sum_{j=1}^{365} I_j$, $I_j=\mathbf{1}\{\text{至少一人在第 }j\text{ 天生日}\}$.

**理解**: $P(I_j=1)=1-(364/365)^{100}$; $EX=\sum E I_j$. 方差用 $I_j$ 两两相关: $\mathrm{Var}(X)=\sum\mathrm{Var}(I_j)+2\sum_{j<k}\mathrm{Cov}(I_j,I_k)$.

---

## 第 5 题 — 单位圆盘均匀

$f(x,y)=C$ 当 $x^2+y^2\le 1$, 否则 $0$.

### (i)(ii)

- (i) $\iint_{x^2+y^2\le 1} C\,dx\,dy=1$ $\Rightarrow$ $C=1/\pi$.
- (ii) $f_X(x)=\int f(x,y)\,dy$, 对 $|x|\le 1$ 积分 $y$ 在 $[-\sqrt{1-x^2},\sqrt{1-x^2}]$.

---

## 提交提醒

- 五题均应交; 第 4 题示性变量写法是评分关键.
- 计算题写出积分/求和中间步骤.
