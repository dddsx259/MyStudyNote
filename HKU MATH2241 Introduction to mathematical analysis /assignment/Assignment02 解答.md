# Assignment 2 — 解答 (连分数子列与聚点)

- **来源**: `assignment/Assignment02.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis, Fall 2026
- **说明**: 按题、按小问分开的完整解答. 交稿前自行核对.

---

## 1. 连分数型序列

设 $(a_n)_{n\ge 1}$ 为正整数列. 定义
$$
x_n=[a_1;a_2,\ldots,a_n]
=a_1+\cfrac{1}{a_2+\cfrac{1}{\ddots+\cfrac{1}{a_n}}},\qquad n\ge 1.
$$

### 渐近分数递推 (证明 (a) 用)

**引理 1.0** (渐近分数的 $p_n,q_n$ 表示). 存在正整数列 $(p_n),(q_n)$ 使
$$
x_n=\frac{p_n}{q_n},\qquad n\ge 1,
$$
且满足
$$
p_1=a_1,\ q_1=1;\qquad
p_2=a_1a_2+1,\ q_2=a_2;
$$
对 $n\ge 3$,
$$
p_n=a_n p_{n-1}+p_{n-2},\qquad q_n=a_n q_{n-1}+q_{n-2}.
$$

**证明**. 对 $n$ 归纳. $n=1,2$ 直接通分验证.

设 $n\ge 3$. 记 $y=[a_2;\ldots,a_n]$. 由归纳 (部分商平移), $y=\tilde p_{n-1}/\tilde q_{n-1}$, 其中 $(\tilde p_k,\tilde q_k)$ 满足同一递推, $\tilde p_1=a_2$, $\tilde q_1=1$. 于是
$$
x_n=a_1+\frac{1}{y}=a_1+\frac{\tilde q_{n-1}}{\tilde p_{n-1}}
=\frac{a_1\tilde p_{n-1}+\tilde q_{n-1}}{\tilde p_{n-1}}.
$$
**断言**: 对 $n\ge 2$, $q_n=\tilde p_{n-1}$ 且 $p_n=a_1\tilde p_{n-1}+\tilde q_{n-1}$.

对 $n$ 归纳. $n=2$: $\tilde p_1=a_2=q_2$, $p_2=a_1\tilde p_1+\tilde q_1=a_1a_2+1$. 成立.

设 $n\ge 3$ 且断言对 $n-1$ 成立. 则
$$
q_n=a_n q_{n-1}+q_{n-2}=a_n\tilde p_{n-2}+\tilde p_{n-3}=\tilde p_{n-1},
$$
$$
p_n=a_n p_{n-1}+p_{n-2}
=a_n\bigl(a_1\tilde p_{n-2}+\tilde q_{n-2}\bigr)+\bigl(a_1\tilde p_{n-3}+\tilde q_{n-3}\bigr)
=a_1\tilde p_{n-1}+\tilde q_{n-1}.
$$
故 $x_n=p_n/q_n$. $\square$

**引理 1.1**. 对一切 $n\ge 1$, $q_n>0$.

**证明**. $q_1=1>0$, $q_2=a_2\ge 1$. 若 $q_{n-1},q_{n-2}>0$, 则 $q_n=a_n q_{n-1}+q_{n-2}>0$ (因 $a_n\in\mathbb{N}$). 归纳即得. $\square$

**引理 1.2** (相邻渐近分数差). 对 $n\ge 2$,
$$
p_n q_{n-1}-p_{n-1}q_n=(-1)^{n-1}.
$$

**证明**. 对 $n$ 归纳. $n=2$:
$$
p_2 q_1-p_1 q_2=(a_1a_2+1)\cdot 1-a_1\cdot a_2=1=(-1)^{1}.
$$
设 $n-1$ 时成立. 用 $p_n=a_n p_{n-1}+p_{n-2}$, $q_n=a_n q_{n-1}+q_{n-2}$:
$$
\begin{aligned}
p_n q_{n-1}-p_{n-1}q_n
&=(a_n p_{n-1}+p_{n-2})q_{n-1}-p_{n-1}(a_n q_{n-1}+q_{n-2})\\
&=p_{n-2}q_{n-1}-p_{n-1}q_{n-2}=-\bigl(p_{n-1}q_{n-2}-p_{n-2}q_{n-1}\bigr).
\end{aligned}
$$
由归纳假设 $p_{n-1}q_{n-2}-p_{n-2}q_{n-1}=(-1)^{n-2}$, 故
$$
p_n q_{n-1}-p_{n-1}q_n=-(-1)^{n-2}=(-1)^{n-1}.
$$
$\square$

**引理 1.3** (单调性与交错). 对 $n\ge 2$,
$$
x_n-x_{n-1}=\frac{(-1)^{n-1}}{q_n q_{n-1}}.
$$
从而:
- $n$ 为奇数时 $x_n>x_{n-1}$; $n$ 为偶数时 $x_n<x_{n-1}$;
- 奇数项子列 $x_1<x_3<x_5<\cdots$ 严格递增;
- 偶数项子列 $x_2>x_4>x_6>\cdots$ 严格递减;
- 对一切 $n$, $x_{2n-1}<x_{2n}$.

**证明**. 由引理 1.2,
$$
x_n-x_{n-1}=\frac{p_n}{q_n}-\frac{p_{n-1}}{q_{n-1}}
=\frac{p_n q_{n-1}-p_{n-1}q_n}{q_n q_{n-1}}
=\frac{(-1)^{n-1}}{q_n q_{n-1}}.
$$
符号与 $q_n q_{n-1}>0$ (引理 1.1) 给出单调结论. 又
$$
x_{2n}-x_{2n-1}=\frac{(-1)^{2n-1}}{q_{2n}q_{2n-1}}=\frac{1}{q_{2n}q_{2n-1}}>0.
$$
$\square$

**引理 1.4** (有界性). 对一切 $n\ge 1$,
$$
a_1\le x_n\le a_1+\frac{1}{a_2}.
$$

**证明**. 下界: $x_1=a_1$; 奇子列递增, 故 $x_{2n-1}\ge x_1=a_1$; 又 $x_{2n}>x_{2n-1}\ge a_1$.

上界: $x_2=a_1+1/a_2$; 偶子列递减, 故 $x_{2n}\le x_2=a_1+1/a_2$; 又 $x_{2n-1}<x_{2n}\le a_1+1/a_2$. $\square$

---

### (a)

**题意**: 证明 $(x_{2n})$ 与 $(x_{2n-1})$ 收敛.

**解答**.

由引理 1.3, $(x_{2n-1})_{n\ge 1}$ 严格递增; 由引理 1.4, $x_{2n-1}\le a_1+1/a_2$, 故有上界. 由 **单调有界定理**, $(x_{2n-1})$ 收敛.

同理, $(x_{2n})_{n\ge 1}$ 严格递减且 $x_{2n}\ge a_1$, 有下界, 故 $(x_{2n})$ 收敛.

**结论**: 两子列均收敛. $\square$

---

### (b)

**题意**: 设 $a_n=1\ (\forall n)$. 判断 $(x_n)$ 是否收敛; 若存在则求极限.

**解答**.

此时 $x_1=1$, $x_2=2$, $x_3=3/2$, $x_4=5/3$, $x_5=8/5$, $\ldots$

**Fibonacci 表示**. 令 $F_1=F_2=1$, $F_{n+2}=F_{n+1}+F_n$ ($n\ge 1$). 用引理 1.0 的递推与 $a_n\equiv 1$ 归纳得
$$
p_n=F_{n+1},\qquad q_n=F_n,\qquad x_n=\frac{F_{n+1}}{F_n}.
$$
(基例 $n=1,2$ 直接; 归纳步: $p_n=p_{n-1}+p_{n-2}=F_n+F_{n-1}=F_{n+1}$, 同理 $q_n=F_n$.)

**子列极限**. 记 $\varphi=(1+\sqrt5)/2$, $\psi=(1-\sqrt5)/2$ ( $\psi=-1/\varphi$ ).

**引理 1.5** (Binet / 特征根, 标准). 对 $n\ge 1$,
$$
F_n=\frac{\varphi^n-\psi^n}{\sqrt5}.
$$

**证明思路**: 递推特征方程 $t^2=t+1$ 的根为 $\varphi,\psi$; 解 $F_n=A\varphi^n+B\psi^n$ 并由初值定 $A,B$. (BS 3.4 Ex 6 亦讨论此列.) $\square$

由引理 1.5,
$$
\frac{F_{n+1}}{F_n}
=\frac{\varphi^{n+1}-\psi^{n+1}}{\varphi^n-\psi^n}
=\varphi\cdot\frac{1-(\psi/\varphi)^{n+1}}{1-(\psi/\varphi)^n}.
$$
因 $|\psi/\varphi|<1$, 有 $(\psi/\varphi)^n\to 0$, 故
$$
\lim_{n\to\infty}\frac{F_{n+1}}{F_n}=\varphi.
$$

因此
$$
\lim_{n\to\infty}x_{2n}=\varphi,\qquad \lim_{n\to\infty}x_{2n-1}=\varphi.
$$

**全序列收敛**. 设 $\varepsilon>0$. 取 $N$ 使 $n\ge N\Rightarrow |x_{2n}-\varphi|<\varepsilon$ 且 $|x_{2n-1}-\varphi|<\varepsilon$. 对任意 $m\ge 2N$, 若 $m$ 为偶数则 $m=2k$, $k\ge N$, 故 $|x_m-\varphi|<\varepsilon$; 若 $m$ 为奇数则 $m=2k-1$, $k\ge N+1\ge N$, 同样 $|x_m-\varphi|<\varepsilon$. 故 $(x_n)$ 收敛且
$$
\lim_{n\to\infty}x_n=\varphi=\frac{1+\sqrt5}{2}.
$$

**结论**: $(x_n)$ **收敛**, 极限为 $\varphi=(1+\sqrt5)/2$. $\square$

---

## 2. 聚点

### (a)

**题意**: 证明 $x\in\mathbb{R}$ 是 $A\subset\mathbb{R}$ 的聚点 $\Leftrightarrow$ 存在 $A$ 中序列 $(x_n)$ 使 $|x_n-x|<1/n$ 对一切 $n$ 成立.

**解答**.

**($\Rightarrow$)** 设 $x$ 为 $A$ 的聚点. 则存在 $(s_k)_{k\ge 1}\subset A$ 使 $s_k\to x$.

对每个 $n\in\mathbb{N}$, 因 $s_k\to x$, 存在 $k_n$ 使 $|s_{k_n}-x|<1/n$. 取 $x_n:=s_{k_n}\in A$, 则 $|x_n-x|<1/n$.

**($\Leftarrow$)** 设 $(x_n)\subset A$ 且 $|x_n-x|<1/n$ ($\forall n$). 则对任意 $\varepsilon>0$, 取 $N>\lceil 1/\varepsilon\rceil$, 则 $n\ge N$ 时
$$
|x_n-x|<\frac{1}{n}\le\frac{1}{N}<\varepsilon,
$$
故 $x_n\to x$. 因此 $x$ 为 $A$ 的聚点.

**结论**: 等价性成立. $\square$

---

### (b)

**题意**: $A\subset\mathbb{R}$ 非空有界; $M=$ $A$ 的全体聚点. 证明 $\max M$ 存在.

**解答**.

**第一步: $M$ 有界.**

因 $A$ 有界, 存在 $B>0$ 使 $A\subset[-B,B]$. 若 $x\in M$, 由 (a) 存在 $(x_n)\subset A$ 使 $|x_n-x|<1/n$, 故 $x_n\to x$. 对固定 $n$, $x_n\in[-B,B]$, 取极限得 $x\in[-B,B]$. 故 $M\subset[-B,B]$, $M$ 有界.

**第二步: $M\neq\emptyset$.**

$A$ 非空. 若 $A$ 为有限集, 取 $a\in A$, 常值列 $x_n\equiv a\in A$ 收敛到 $a$, 故 $a\in M$.

若 $A$ 为无穷集, 由 **Bolzano-Weierstrass 定理**, 有界无穷集 $A$ 存在收敛子列 $(a_{n_k})\subset A$, 记其极限为 $L$. 则 $L$ 为 $A$ 的聚点, $L\in M$.

故 $M\neq\emptyset$.

**第三步: $M$ 闭.**

设 $(y_m)_{m\ge 1}\subset M$ 且 $y_m\to y$. 需证 $y\in M$.

对每个 $m$, 因 $y_m\in M$, 由 (a) 存在 $z_m\in A$ 使
$$
|z_m-y_m|<\frac{1}{m}.
$$
则
$$
|z_m-y|\le |z_m-y_m|+|y_m-y|<\frac{1}{m}+|y_m-y|.
$$
给定 $\varepsilon>0$, 取 $M$ 使 $m\ge M\Rightarrow |y_m-y|<\varepsilon/2$; 再取 $m\ge \max\{M,\lceil 2/\varepsilon\rceil\}$, 则 $|z_m-y|<\varepsilon/2+1/m\le\varepsilon$. 故存在 $A$ 中子列 (例如沿 $m$) 收敛到 $y$, 即 $y\in M$. 所以 $M$ 闭.

**第四步: $\max M$ 存在.**

令 $s:=\sup M$ ( $M$ 非空有界, 故 $s$ 存在). 对每个 $n\in\mathbb{N}$, 因 $s-1/n$ 不是 $M$ 的上界, 存在 $m_n\in M$ 使 $s-1/n<m_n\le s$. 则 $m_n\to s$. 因 $M$ 闭, 极限 $s\in M$. 故 $s=\max M$.

**结论**: $\max M$ 存在. $\square$

---

## 附: 与 BS 3.4 Ex 6 的对应 (题 1(b))

BS 3.4 Exercise 6 讨论 Fibonacci 比 $F_{n+1}/F_n$ 的极限. 本题 $a_n\equiv 1$ 时 $x_n$ 恰为该比, 故 $\lim x_n=\varphi$. 讲义 Sep 17 亦将全 1 连分数与黄金比联系: 奇渐近分数从下逼近 $\varphi$, 偶渐近分数从上逼近 $\varphi$, 故全序列收敛于 $\varphi$.
