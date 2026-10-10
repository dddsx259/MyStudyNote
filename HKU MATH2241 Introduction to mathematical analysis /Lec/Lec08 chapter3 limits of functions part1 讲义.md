# Lec08 — Chapter 3 Limits of Functions (Part 1)

- **源**: `Lec/Lec08 chapter3 limits of functions part1.pdf` (手写 slides, 31 页)
- **范围**: 聚点, 函数极限, 序列准则, 发散准则, 有界性, 四则与夹逼, 单侧 / 无穷极限
- **注**: Test1 **不考** Ch3; 考后阅读

---

## 1. Cluster points (聚点)

### Definition 1.1 — Cluster point / 聚点

设 $A\subseteq\mathbb{R}$. 称 $c\in\mathbb{R}$ 是 $A$ 的**聚点** (cluster point), 若对每个 $\delta>0$, 存在 $x\in A$ 使
\[
0<|x-c|<\delta
\]
(即 $(c-\delta,c+\delta)\cap(A\setminus\{c\})\neq\emptyset$).

**等价说法** (slides):

1. $c$ 是聚点
2. 每个空心邻域交 $A$ 非空
3. 对每个 $\delta>0$, $(c-\delta,c+\delta)\cap A\setminus\{c\}\neq\emptyset$

**例子**

- $A=[1,3]$: 聚点集 $=A$ (闭区间内每点都是聚点)
- $A=\{3, 3.1, 6, 7\}$ (有限集): 聚点集 $=\emptyset$ (取 $\delta$ 小于到最近点距离)

**证明思路 (有限集无聚点)**: 对候选 $c$, 取 $\delta=\inf\{|c-a|:a\in A, a\neq c\}>0$ (有限非空), 则空心邻域不含 $A$ 中点.

### Theorem 1.5 — Sequential criterion for cluster points / 聚点的序列刻画

**假设**: $A\subseteq\mathbb{R}$, $c\in\mathbb{R}$.

**结论**: $c$ 是 $A$ 的聚点 $\Leftrightarrow$ 存在序列 $(x_n)$ 满足

- $x_n\in A\setminus\{c\}$ (或 $x_n\in A$, $x_n\neq c$)
- $x_n\to c$

**证明思路**

- ($\Rightarrow$) 对每个 $n$, 取 $x_n\in A\cap(c-1/n,c+1/n)\setminus\{c\}$, 则 $x_n\to c$.
- ($\Leftarrow$) 若 $x_n\to c$ 且 $x_n\neq c$, 则任意 $\delta>0$ 有 $N$ 使 $n>N\Rightarrow 0<|x_n-c|<\delta$.

---

## 2. Limit of a function (函数极限)

### Definition 1.6 — Limit of $f$ at a cluster point

设 $A\subseteq\mathbb{R}$, $c$ 是 $A$ 的聚点, $f:A\to\mathbb{R}$. 称 $\lim_{x\to c}f(x)=L$, 若对每个 $\varepsilon>0$, 存在 $\delta>0$, 使得
\[
x\in A,\quad 0<|x-c|<\delta \implies |f(x)-L|<\varepsilon.
\]

**定义, 无需证明.** 注意: $c$ **不必**属于 $A$; 只要求它是聚点 (以便「任意接近」有意义).

### 例子

1. **常值** $f(x)=b$: $\lim_{x\to c}f=b$. 任取 $\delta>0$ 即可.
2. **分段**在一点附近等于常数: 如在某空心邻域 $f\equiv 1$, 则极限为 $1$.
3. **有理/无理** (Thomae 型简化): $f(x)=x$ 若有理, $f(x)=0$ 若无理, 则 $\lim_{x\to 0}f(x)=0$ (因 $|f(x)|\le|x|$).

---

## 3. Sequential criterion (序列准则)

### Theorem 2.1 — Sequential criterion for functional limits

**假设**: $A\subseteq\mathbb{R}$, $f:A\to\mathbb{R}$, $c$ 为 $A$ 的聚点.

**结论**: 以下等价:

1. $\lim_{x\to c}f(x)=L$
2. 对任意序列 $(x_n)$ 满足 $x_n\in A\setminus\{c\}$, $x_n\to c$, 都有 $f(x_n)\to L$

**证明思路**

- (1)$\Rightarrow$(2): $\varepsilon$-$\delta$ 给出 $\delta$; 序列收敛给出 $N$ 使 $n>N\Rightarrow 0<|x_n-c|<\delta$, 故 $|f(x_n)-L|<\varepsilon$.
- (2)$\Rightarrow$(1): 反证. 若极限不是 $L$, 则 $\exists\varepsilon>0$ 使对每个 $n$ 有 $x_n\in A$, $0<|x_n-c|<1/n$, 但 $|f(x_n)-L|\ge\varepsilon$. 则 $x_n\to c$ 但 $f(x_n)\not\to L$, 矛盾.

### Theorem 2.2 — Uniqueness of limits / 极限唯一性

若 $\lim_{x\to c}f=L$ 且 $\lim_{x\to c}f=M$, 则 $L=M$.

**证明思路**: 用序列准则取同一 $x_n\to c$, 则 $f(x_n)$ 既 $\to L$ 又 $\to M$.

---

## 4. Divergence criterion (发散准则)

### Theorem 2.3 — Divergence via two sequences

**假设**: $c$ 是 $A$ 的聚点, $f:A\to\mathbb{R}$.

**结论**: 若存在两序列 $(x_n),(y_n)$ 在 $A\setminus\{c\}$ 中都趋于 $c$, 但 $\lim f(x_n)\neq\lim f(y_n)$ (或其中一个极限不存在), 则 $\lim_{x\to c}f$ **不存在**.

**例子**

- $f(x)=1$ ($x\ge 0$), $f(x)=-1$ ($x<0$): 取 $x_n=1/n$, $y_n=-1/n$, 极限分别为 $1$ 与 $-1$.
- $f(x)=\sin(1/x)$ ($x\neq 0$): 取使 $\sin=1$ 与 $\sin=-1$ 的点列都 $\to 0$.

---

## 5. Boundedness near the limit (极限邻域有界)

### Theorem 3.1 — Boundedness of a limit

**假设**: $\lim_{x\to c}f(x)$ 存在.

**结论**: 存在 $\delta>0$ 与 $M$ 使 $0<|x-c|<\delta$, $x\in A$ $\Rightarrow$ $|f(x)|\le M$ (在 $c$ 的某个空心邻域上有界).

**证明思路**: 取 $\varepsilon=1$, 得 $\delta$ 使 $|f(x)-L|<1$, 故 $|f(x)|<|L|+1$.

**反例提示**: $f(x)=1/x$ 在 $0$ 处极限不存在且任何空心邻域无界 — 与「有极限 $\Rightarrow$ 局部有界」一致 (逆否: 局部无界 $\Rightarrow$ 极限不存在).

---

## 6. Arithmetic of limits (极限四则)

### Definition 4.1 — Pointwise operations

对 $f,g:A\to\mathbb{R}$: $(f+g)(x)=f(x)+g(x)$, $(fg)(x)=f(x)g(x)$, 以及常数倍, 商 (分母非零处).

### 基本结论 (由序列准则 + 数列极限运算)

若 $\lim f=L$, $\lim g=M$, 则

1. $\lim(f+g)=L+M$
2. $\lim(fg)=LM$
3. $\lim(bf)=bL$
4. 若 $M\neq 0$ 且在某空心邻域 $g\neq 0$, 则 $\lim(f/g)=L/M$

**证明**: 任取 $x_n\to c$, $x_n\neq c$; 用数列的四则运算.

### Theorem 4.6 — Squeeze theorem / 夹逼定理 (函数版)

**假设**: $f\le g\le h$ 在 $A$ 上 (靠近 $c$ 的空心邻域), 且 $\lim_{x\to c}f=\lim_{x\to c}h=L$.

**结论**: $\lim_{x\to c}g=L$.

**证明思路**: 序列准则化为数列夹逼.

#### Exercise (slides)

求 $\lim_{x\to 0} x^2\bigl(1+\sin(1/x^2)\bigr)$ (在 $x\neq 0$).

对任意 $x\neq 0$,
\[
0\le x^2\bigl(1+\sin(1/x^2)\bigr)\le 2x^2.
\]
因 $\lim x^2=0=\lim 2x^2$, 夹逼得极限为 $0$.

---

## 7. One-sided limits (单侧极限)

### Definition 5.1

- **右极限** $\lim_{x\to c^+}f=L$: $c$ 是 $A\cap(c,\infty)$ 的聚点; 对 $\varepsilon>0$ 有 $\delta>0$ 使 $c<x<c+\delta$, $x\in A$ $\Rightarrow$ $|f(x)-L|<\varepsilon$.
- **左极限** $\lim_{x\to c^-}f=L$: 类似, 用 $(c-\delta,c)$.

**关系**: $\lim_{x\to c}f$ 存在 $\Leftrightarrow$ 左右极限存在且相等.

**例子**: $\mathrm{sgn}(x)$ 在 $0$: 右极限 $1$, 左极限 $-1$, 双边极限不存在.

---

## 8. Infinite limits / limits at infinity

### Definition 5.5 — $\lim_{x\to c}f=\infty$

对任意 $M\in\mathbb{R}$, 存在 $\delta>0$ 使 $0<|x-c|<\delta$, $x\in A$ $\Rightarrow$ $f(x)>M$ ($-\infty$ 类似).

### Limit at infinity

若 $(a,\infty)\subseteq A$, 称 $\lim_{x\to\infty}f=L$ 若对 $\varepsilon>0$ 存在 $K$ 使 $x>K\Rightarrow |f(x)-L|<\varepsilon$.

**例子**: $f(x)=1/x$ ($x>0$), $\lim_{x\to\infty}f=0$. 对 $\varepsilon>0$ 取 $K>1/\varepsilon$.

---

## 自检

- 聚点 vs 内点 / 孤立点
- 函数极限必须先确认 $c$ 是定义域的聚点
- 证「极限不存在」: 两序列法最常用
- 夹逼与四则: 优先化到序列准则
