# Tutorial 2 — 总结

- **来源**: `tut/Tut02.pdf` (题面; 原名 `TUT2-Q.pdf`) + `tut/Tut02 sol.pdf` (官方解; 原名 `TUT2-S.pdf`)
- **课程**: MATH2241 Introduction to Mathematical Analysis
- **对齐**: Ch2 Sequences (`Lec/05`–`07`); 极限运算 / 夹逼 / MCT / 根式极限

> 下列为题意 + 官方 sol 要点 (已整理); **Problem 1(d) 官方结论有误**, 见该题注.

---

## Problem 1 — 求极限

### (a) $\displaystyle\lim_{n\to\infty}\Big(\frac12+\frac1{2\cdot3}+\cdots+\frac1{n(n+1)}\Big)$

- **思路**: 裂项 $\frac1{k(k+1)}=\frac1k-\frac1{k+1}$; 望远镜和 $=1-\frac1{n+1}$.
- **结论**: 极限 $=1$.

### (b) $\displaystyle\lim_{n\to\infty}\sqrt[n]{1-\frac1n}$

- **思路**: $1-\frac1n\le\sqrt[n]{1-\frac1n}\le1$; 夹逼.
- **结论**: 极限 $=1$.

### (c) $\displaystyle\lim_{n\to\infty}\Big(\frac1{n^2}+\frac1{(n+1)^2}+\cdots+\frac1{(2n)^2}\Big)$

- **思路**: $n$ 项, 每项 $\le\frac1{n^2}$, $\ge\frac1{(2n)^2}$ $\Rightarrow$ $\frac1{4n}\le\text{和}\le\frac1n\to0$.
- **结论**: 极限 $=0$.

### (d) $\displaystyle\lim_{n\to\infty}\Big(\frac1{\sqrt{n^2+1}}+\cdots+\frac1{\sqrt{n^2+n}}\Big)$

- **夹逼**: $\dfrac{n}{\sqrt{n^2+n}}\le\sum_{k=1}^n\dfrac1{\sqrt{n^2+k}}\le\dfrac{n}{\sqrt{n^2+1}}$; 左右均 $\to1$.
- **写法注意**: $\frac1{\sqrt{n^2+k}}=\frac1{n\sqrt{1+k/n^2}}$ (是 $k/n^2$ 不是 $k/n$), 故不是「$1/\sqrt{1+x}$」型 Riemann 和.
- **结论**: 极限 $=1$.
- **注**: 官方 sol 上下界写法正确, 但把左右极限误写成 $0$; 应为 **1**.

---

## Problem 2 — $\sqrt[n]{a_1^n+\cdots+a_m^n}\to\max a_i$

- **假设**: $a_1,\ldots,a_m>0$; $A=\max\{a_i\}$.
- **证明要点**: $A=\sqrt[n]{A^n}\le\sqrt[n]{\sum a_i^n}\le\sqrt[n]{m A^n}=A\sqrt[n]{m}$; $\sqrt[n]{m}\to1$ (Thm 5.2 型).
- **结论**: 极限 $=A$.

---

## Problem 3 — 零序列 × 有界

### (a)

- **假设**: $a_n\to0$, $\{b_n\}$ 有界 ($|b_n|\le M$).
- **结论**: $a_nb_n\to0$.
- **证明**: $|a_nb_n|\le M|a_n|$; 对 $\varepsilon$ 取使 $|a_n|<\varepsilon/M$ 的 $N$.

### (b)

- **假设**: $a_n\to L\neq0$, $\{b_n\}$ 有界.
- **结论**: **无法判定** $\{a_nb_n\}$ 是否收敛.
- **反例**: $a_n\equiv1$, $b_n\equiv1$ 收敛; $a_n\equiv1$, $b_n=(-1)^n$ 发散.

---

## Problem 4 — 递推 $x_1=\sqrt2$, $x_{n+1}=\frac1{x_n+2}$

- **目标**: 证收敛并求极限.
- **关键**: 阈值 $L=1/(L+2)\Rightarrow L^2+2L-1=0\Rightarrow L=\sqrt2-1$ (取正).
- **官方路线**: 奇项 $> \sqrt2-1$, 偶项 $\in(0,\sqrt2-1)$; 奇子列递减有下界, 偶子列递增有上界 (用二步递推与 MCT); 两子列极限皆为 $\sqrt2-1$.
- **结论**: $\lim x_n=\sqrt2-1$.

---

## Problem 5 — 比值判零 + 例

### (a)

- **假设**: $a_n>0$, $\lim\frac{a_n}{a_{n+1}}=l>1$.
- **结论**: $a_n\to0$.
- **证明**: 取 $r\in(1,l)$, 大 $n$ 时 $a_{n+1}\le a_n/r$; 迭代得几何衰减, 夹逼到 0.

### (b)

- **结论**: $\lim\frac{n^2}{3^n}=0$ (因 $\frac{a_n}{a_{n+1}}\to3>1$).

### Food for Thought

比较 $n^a$, $b^n$, $n!$, $n^n$ ($a,b>1$) 的「最终增长」: 典型链 $n^a\ll b^n\ll n!\ll n^n$; 可算 $\frac{3^n}{n!}\to0$, $\frac{n!}{n^n}\to0$.

---

## Problem 6 — 再求极限

### (a) $\displaystyle\lim_{n\to\infty}\sum_{p=1}^n\frac{p!}{n!}$

- **思路**: 和 $=1+\frac1n+\frac{1}{n(n-1)}+\cdots$; 上界 $1+\frac{2n-3}{n(n-1)}$ (官方估计), 夹逼得 1.
- **结论**: 极限 $=1$.

### (b) $\displaystyle\lim_{n\to\infty}\big((n+1)^\alpha-n^\alpha\big)$, $0<\alpha<1$

- **思路**: $0<(n+1)^\alpha-n^\alpha<n^{\alpha-1}\to0$ (官方不等式).
- **结论**: 极限 $=0$.

---

## 易错点 (备考)

1. 多项和的极限: 优先 **项数 × 上下界** 或裂项/望远镜, 不要盲目「每项→0 故和→0」(项数也在变).
2. $\sqrt[n]{\sum a_i^n}$ 由 **最大项** 主导.
3. 「$a_n\to L\neq0$ + 有界」**推不出** $a_nb_n$ 收敛.
4. 递推收敛常拆奇偶子列 + MCT, 再解不动点.
5. $\frac{a_n}{a_{n+1}}\to l>1$ $\Rightarrow$ $a_n\to0$ (等比衰减).
