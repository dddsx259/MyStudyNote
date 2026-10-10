# Tutorial 3 — 总结

- **来源**: `tut/Tut03.pdf` (题面; 原名 `TUT3-Q.pdf`) + `tut/Tut03 sol.pdf` (官方解)
- **课程**: MATH2241 Introduction to Mathematical Analysis
- **对齐**: Ch2 序列 / 子列 / Cauchy / 级数判别 (含条件收敛, Ratio/Root)

> 下列为题意 + 官方 sol 要点.

---

## Question 1 — 子列极限与发散

$$
x_n=\cos\Bigl(\frac{n\pi}{2}\Bigr)+\frac1n.
$$

### (a)

按模 4 残类:

| 子列 | 极限 |
|---|---|
| $x_{4k}$ | $1$ |
| $x_{4k+1}$, $x_{4k+3}$ | $0$ |
| $x_{4k+2}$ | $-1$ |

### (b)

$(x_{4k})$ 与 $(x_{4k+2})$ 极限不同 $\Rightarrow$ $(x_n)$ **不收敛**.

### (c)

子列极限集 $=\{-1,0,1\}$. 任一收敛子列必落入上述四类之一的无穷多项, 故极限只能是三者之一.

**直觉**: $1/n\to0$, 长程行为由 $\cos(n\pi/2)$ 的周期值决定.

---

## Question 2 — 有界 + 子列极限唯一 $\Rightarrow$ 收敛

**假设**: $(x_n)$ 有界, 且每个收敛子列极限都是 $L$.

**结论**: $x_n\to L$.

**证明思路**: 反证 $x_n\not\to L$ $\Rightarrow$ 存在 $\varepsilon>0$ 与子列 $|x_{n_k}-L|\ge\varepsilon$. 有界 $\Rightarrow$ BW 得收敛子子列 $\to M$; 由假设 $M=L$, 与 $|x_{n_{k_j}}-L|\ge\varepsilon$ 矛盾.

---

## Question 3 — Cauchy vs 相邻差 $\to0$

### (a)

假设 $|x_{k+1}-x_k|\le 1/k^2$ ($k\ge2$). 则
$$
|x_m-x_n|\le\sum_{k=n}^{m-1}\frac1{k^2}\le\sum_{k=n}^{m-1}\Bigl(\frac1{k-1}-\frac1k\Bigr)=\frac1{n-1}-\frac1{m-1}<\frac1{n-1}.
$$
故 Cauchy.

### (b)

反例 $x_n=\sqrt n$: $x_{n+1}-x_n\to0$, 但取 $m=4n$ 得 $|x_m-x_n|=\sqrt n$, **非** Cauchy.

**要点**: 相邻步小 $\ne$ 多步总位移小; 需可和尾 (如 $1/k^2$).

---

## Question 4 — 级数比较 / 通项

### (a)

$0<\dfrac{n+4}{n^3+2n+1}\le\dfrac{5}{n^2}$; $\sum 5/n^2$ 收敛 $\Rightarrow$ 原级数收敛 (Comparison).

### (b)

$a_n=\dfrac{\sqrt{n^2+1}}{n+2}\to1\ne0$ $\Rightarrow$ 发散 ($n$-th term test).

### (c)

$0<\dfrac1{n^2+\sqrt n}\le\dfrac1{n^2}$ $\Rightarrow$ 收敛.

---

## Question 5 — 条件收敛与加括号

$$
\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n^{2/3}}.
$$

### (a)

AST: $b_n=n^{-2/3}\searrow0$ $\Rightarrow$ 收敛; 绝对值是 $p=2/3<1$ 的 $p$-级数 $\Rightarrow$ 发散. 故 **条件收敛**.

### (b)

两两分组 $t_m=s_{2m}$; 原级数收敛 $\Rightarrow$ $t_m\to$ 同极限. 分组级数收敛到同样的和.

### (c)

分组只加括号, **不改顺序**; 真重排会改顺序, 条件收敛时可改变行为.

---

## Question 6 — Ratio 无结论, Root 判收敛

$$
a_n=\begin{cases}3\cdot2^{-n},&n\text{ 奇}\\ 2^{-n},&n\text{ 偶.}\end{cases}
$$

### (a)

$\dfrac{a_{n+1}}{a_n}=\frac16$ (奇) 或 $\frac32$ (偶) $\Rightarrow$ 比值极限不存在, Ratio Test **inconclusive**.

### (b)

$\sqrt[n]{a_n}\to1/2<1$ $\Rightarrow$ Root Test 得收敛.

### (c)

「测试 inconclusive」只说明该测试帮不上忙, **不**等于级数发散.

---

## 易错点 (备考)

1. 子列极限集可用模 $m$ 残类穷尽周期型振荡.
2. 「有界 + 所有收敛子列同极限」是收敛的充要条件之一 (本 Tut Q2).
3. $x_{n+1}-x_n\to0$ **推不出** Cauchy.
4. AST 只给条件收敛; 绝对收敛另查.
5. Ratio inconclusive 时改用 Root / 比较等.
