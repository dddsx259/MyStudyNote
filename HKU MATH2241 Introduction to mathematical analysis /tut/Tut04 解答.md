# Tut04 — 解答

- **来源**: `tut/Tut04.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis, Fall 2026
- **范围**: Ch2 Part 3 (比较 / 极限比较 / 通项检验 / 交错级数 / Cauchy 凝聚 / $p$-级数)
- **说明**: 官方 sol 尚未入库. 下面是按题的完整自写解答. 题 1 的 hint 按 $2^n>n$ 使用 (用来证明 $n^{1/n}<2$).

---

## 1. $\sum 1/n^{1+1/n}$ 发散

**结论**: 级数发散. 陈述成立.

**证明**:

先证 $2^n>n$ ($\forall n\in\mathbb{N}$). $n=1$ 时 $2>1$. 设 $2^k>k$. 则
$$
2^{k+1}=2\cdot 2^k>2k.
$$
又 $k\ge 1$ 时 $2k\ge k+1$, 故 $2^{k+1}>k+1$.

因此 $n<2^n$. 若 $n^{1/n}\ge 2$, 则 $n=(n^{1/n})^n\ge 2^n$, 矛盾. 故 $n^{1/n}<2$, 从而
$$
n^{1+1/n}=n\cdot n^{1/n}<2n,
$$
$$
\frac{1}{n^{1+1/n}}>\frac{1}{2n}.
$$
$\sum 1/(2n)$ 是调和级数的常数倍, 发散. 通项为正, 由比较检验 (Ch2 P3 Thm 2.8), $\sum 1/n^{1+1/n}$ 发散.

---

## 2. 极限比较检验

设 $a_n>0$, $b_n>0$, 且 $\lim a_n/b_n=L$ 存在, $L\ge 0$.

### (a) $L>0$ 时同敛散

存在 $N$ 使 $n>N$ 时
$$
\Bigl|\frac{a_n}{b_n}-L\Bigr|<\frac L2,
$$
故
$$
\frac L2\, b_n<a_n<\frac{3L}2\, b_n.
$$
有限项不影响敛散.

- 若 $\sum b_n$ 收敛, 则 $\sum (3L/2)b_n$ 收敛. 由 $0<a_n<(3L/2)b_n$ 与比较检验, $\sum a_n$ 收敛.
- 若 $\sum a_n$ 收敛, 则由 $b_n<(2/L)a_n$ 与比较检验, $\sum b_n$ 收敛.

因此 $\sum a_n$ 收敛 $\Leftrightarrow$ $\sum b_n$ 收敛.

### (b) $L=0$ 且 $\sum b_n$ 收敛 $\Rightarrow$ $\sum a_n$ 收敛

取 $\varepsilon=1$. 存在 $N$ 使 $n>N$ 时 $0<a_n/b_n<1$, 即 $0<a_n<b_n$. 由比较检验, $\sum a_n$ 收敛.

### (c) $L=0$ 时反向不成立

取 $a_n=1/n^2$, $b_n=1/n$. 二者为正,
$$
\frac{a_n}{b_n}=\frac1n\to 0.
$$
$\sum 1/n^2$ 收敛 (Ch2 P3 例 2.6), $\sum 1/n$ 发散.

### (d) 该级数收敛

记
$$
a_n=\frac{n^2+n-1}{27n^5-n^4+9n^3-2n+6},\qquad b_n=\frac1{n^3}.
$$
$n\ge 1$ 时分子 $n^2+n-1\ge 1>0$. 分母
$$
27n^5-n^4+9n^3-2n+6\ge 27n^5-n^4-2n\ge 27n^5-n^5-2n^5=24n^5>0,
$$
其中用了 $n^4\le n^5$ 与 $2n\le 2n^5$. 故 $a_n>0$. 又
$$
\frac{a_n}{b_n}=\frac{n^5+n^4-n^3}{27n^5-n^4+9n^3-2n+6}=\frac{1+n^{-1}-n^{-2}}{27-n^{-1}+9n^{-2}-2n^{-4}+6n^{-5}}\to\frac1{27}>0.
$$
$\sum 1/n^3$ 收敛 ($p=3\ge 2$, 讲义 Exercise 2.7). 由 (a), $\sum a_n$ 收敛.

---

## 3. $\displaystyle\sum_{n=0}^{\infty}\frac{(n+1)^2}{n!}=5e$

级数即
$$
\frac{1^2}{0!}+\frac{2^2}{1!}+\frac{3^2}{2!}+\frac{4^2}{3!}+\cdots.
$$
已知 $\sum_{n=0}^{\infty} 1/n!=e$.

**恒等式**: $(n+1)^2=n^2+2n+1=n(n-1)+3n+1$, 故
$$
\frac{(n+1)^2}{n!}=\frac{n(n-1)}{n!}+\frac{3n}{n!}+\frac{1}{n!}.
$$
$n\ge 2$ 时 $n(n-1)/n!=1/(n-2)!$; $n\ge 1$ 时 $n/n!=1/(n-1)!$.

对 $N\ge 2$, 部分和
$$
\begin{aligned}
s_N
&=\sum_{n=0}^{N}\frac{(n+1)^2}{n!}
=\sum_{n=2}^{N}\frac{1}{(n-2)!}+3\sum_{n=1}^{N}\frac{1}{(n-1)!}+\sum_{n=0}^{N}\frac{1}{n!}\\
&=\sum_{k=0}^{N-2}\frac{1}{k!}+3\sum_{k=0}^{N-1}\frac{1}{k!}+\sum_{k=0}^{N}\frac{1}{k!}.
\end{aligned}
$$
三项分别趋于 $e$, $3e$, $e$, 故 $s_N\to 5e$. 级数收敛, 和为 $5e$.

---

## 4. $\cos$ 与 $\sin$

用标准不等式: 对一切实数 $x$, $|\sin x|\le |x|$.

由此得半角估计: $1-\cos x=2\sin^2(x/2)$, 故
$$
0\le 1-\cos x=2\sin^2(x/2)\le 2\Bigl(\frac{|x|}{2}\Bigr)^2=\frac{x^2}{2}.
$$

### (a) $\sum a_n$ 收敛 $\Rightarrow$ $\sum\cos a_n$ 发散

由通项检验 (Ch2 P3 Thm 2.1), $a_n\to 0$. 取 $N$ 使 $n>N$ 时 $|a_n|<1$. 则
$$
\cos a_n\ge 1-\frac{a_n^2}{2}>1-\frac12=\frac12.
$$
于是 $\cos a_n\not\to 0$. 再由通项检验, $\sum\cos a_n$ 发散.

### (b) $\sum a_n$ 绝对收敛 $\Rightarrow$ $\sum\sin a_n$ 绝对收敛

$|\sin a_n|\le |a_n|$. $\sum |a_n|$ 收敛, 通项非负, 由比较检验 $\sum |\sin a_n|$ 收敛.

---

## 5. 绝对 / 条件 / 发散

### (a) $\sum (-1)^{n+1}/(n+\sqrt n)$ 条件收敛

令 $x_n=1/(n+\sqrt n)>0$.

**不绝对收敛**: $n\ge 1$ 时 $\sqrt n\le n$, 故 $n+\sqrt n\le 2n$,
$$
x_n\ge\frac{1}{2n}.
$$
$\sum 1/(2n)$ 发散, 比较检验给出 $\sum x_n$ 发散.

**收敛**: $n+\sqrt n$ 严格递增, 故 $(x_n)$ 严格递减. 又 $n+\sqrt n\ge n\to\infty$, 所以 $x_n\to 0$. 由交错级数判别 (Ch2 P3 Thm 3.13),
$$
\sum_{n=1}^{\infty}(-1)^{n+1}x_n
$$
收敛.

因此该级数条件收敛.

### (b) $\sum (-1)^{n+1} n/(n+\sqrt n)$ 发散

$$
\frac{n}{n+\sqrt n}=\frac{1}{1+n^{-1/2}}\to 1\neq 0.
$$
通项的绝对值趋于 $1$, 不通项趋于 $0$. 由通项检验, 级数发散 (既非绝对收敛, 也非条件收敛).

---

## 6. Cauchy 凝聚与 $p$-级数

### (a) 凝聚判别

**假设**: $a_n\ge 0$, 且 $(a_n)$ 递减 ($a_{n+1}\le a_n$).

**结论**: $\sum_{n=1}^{\infty} a_n$ 收敛 $\Leftrightarrow$ $\sum_{n=0}^{\infty} 2^n a_{2^n}$ 收敛.

记 $s_m=\sum_{k=1}^{m} a_k$, $t_N=\sum_{n=0}^{N} 2^n a_{2^n}$. 两项级数的通项都非负, 故各自收敛 $\Leftrightarrow$ 部分和有界 (Ch2 P3 Thm 2.5).

**($\Rightarrow$)**. 设 $\sum a_n$ 收敛, 记其和为 $s$, 则 $s_m\le s$.

$n\ge 1$ 时, 从 $k=2^{n-1}+1$ 到 $k=2^n$ 共 $2^{n-1}$ 项, 且这些 $k\le 2^n$, 递减给出 $a_k\ge a_{2^n}$. 故
$$
\sum_{k=2^{n-1}+1}^{2^n} a_k\ge 2^{n-1}a_{2^n}=\frac12\cdot 2^n a_{2^n},
$$
即 $2^n a_{2^n}\le 2\sum_{k=2^{n-1}+1}^{2^n} a_k$. 对 $n=1,\ldots,N$ 求和,
$$
\sum_{n=1}^{N} 2^n a_{2^n}\le 2\sum_{k=2}^{2^N} a_k\le 2s.
$$
又 $2^0 a_1=a_1\le s$, 所以 $t_N\le 3s$. $(t_N)$ 有界, 凝聚级数收敛.

**($\Leftarrow$)**. 设凝聚级数收敛, 记其和为 $t$, 则 $t_N\le t$.

$n\ge 1$ 时, 同一段里每个 $a_k\le a_{2^{n-1}}$, 共 $2^{n-1}$ 项, 故
$$
\sum_{k=2^{n-1}+1}^{2^n} a_k\le 2^{n-1}a_{2^{n-1}}.
$$
于是
$$
s_{2^N}=a_1+\sum_{n=1}^{N}\sum_{k=2^{n-1}+1}^{2^n} a_k\le a_1+\sum_{n=1}^{N} 2^{n-1}a_{2^{n-1}}.
$$
后一和里令 $m=n-1$,
$$
\sum_{n=1}^{N} 2^{n-1}a_{2^{n-1}}=\sum_{m=0}^{N-1} 2^m a_{2^m}\le t.
$$
故 $s_{2^N}\le a_1+t$. 对任意 $M$, 取 $N$ 使 $2^N\ge M$. 非负项部分和递增, $s_M\le s_{2^N}\le a_1+t$. $(s_M)$ 有界, $\sum a_n$ 收敛.

### (b) $p$-级数

设 $p>0$, $a_n=1/n^p$. $p>0$ 时 $n\mapsto n^p$ 在正整数上严格递增, 故 $(a_n)$ 递减且非负. 由 (a), $\sum 1/n^p$ 收敛 $\Leftrightarrow$ $\sum_{n=0}^{\infty} 2^n a_{2^n}$ 收敛.

$$
2^n a_{2^n}=2^n\cdot (2^n)^{-p}=2^{n(1-p)}=(2^{1-p})^n.
$$
令 $r=2^{1-p}>0$. 几何级数 $\sum_{n=0}^{\infty} r^n$ 的部分和为 $(1-r^{N+1})/(1-r)$ ($r\neq 1$).

- 若 $p>1$, 则 $0<r<1$, $r^{N+1}\to 0$, 几何级数收敛. 故 $p$-级数收敛.
- 若 $p=1$, 则 $2^n a_{2^n}=1\not\to 0$, 凝聚级数发散. 故调和级数发散.
- 若 $0<p<1$, 则 $r>1$, $(2^{1-p})^n\not\to 0$, 凝聚级数发散. 故 $p$-级数发散.

因此 $\sum_{n=1}^{\infty} 1/n^p$ 收敛当且仅当 $p>1$.
