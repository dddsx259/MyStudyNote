# Review04 — Sample Test 1 解答

- **题面**: `docs/archives/previous/test&quiz/Sample Test01.pdf`
- **官方解答**: `docs/archives/previous/test&quiz/Sample Test01 solution.pdf`
- **范围**: 第 3(c) 题用到 $\liminf$, 讲义没写, 本次 Test 1 可跳过. 其余都在 Ch1 + Ch2.
- **与官方稿的差别**: 第 5(a) 题官方反例写了 $n=1/3$, 不是正整数. 下面用同一个集合, 取 $n=2$. 结论不变.

---

## 1. $\lim a_n=0$, 其中 $a_n=(n-1)/(n^2-3)$

**结论**: $\displaystyle\lim_{n\to\infty}a_n=0$.

$n\ge 2$ 时 $n^2-3>0$ 且 $n-1>0$, 故 $a_n>0$. ($n=1$ 时 $a_1=0$, 不影响极限.)

设 $\varepsilon>0$. 取 $N=\lceil 3+1/\varepsilon\rceil$. 则 $N>3$. 当 $n\ge N$ 时 $n>3$, 且

$$
0<a_n=\frac{n-1}{n^2-3}<\frac{1}{n-3}.
$$

后一步等价于 $(n-1)(n-3)<n^2-3$. 展开是 $n^2-4n+3<n^2-3$, 即 $n>3/2$, 在 $n>3$ 时成立. 又 $N\ge 3+1/\varepsilon$, 故 $N-3\ge 1/\varepsilon$,

$$
\frac{1}{n-3}\le\frac{1}{N-3}\le\varepsilon.
$$

因此 $n\ge N$ 时 $|a_n-0|<\varepsilon$. 由 $\varepsilon$-$N$ 定义, $a_n\to 0$.

---

## 2. 逐点被 $Y$ 压住时的确界

设 $X,Y\subseteq\mathbb{R}$ 非空有界, 且对每个 $x\in X$ 都存在 $y\in Y$ 使 $x\le y$.

### (a) $\sup X\le\sup Y$

**结论**: 成立.

任取 $x\in X$. 存在 $y\in Y$ 使 $x\le y$. 又 $y\le\sup Y$, 故 $x\le\sup Y$. 这对一切 $x\in X$ 成立, 所以 $\sup Y$ 是 $X$ 的上界. $\sup X$ 是最小上界, 于是 $\sup X\le\sup Y$.

### (b) $\inf X\le\inf Y$ 不必成立

**结论**: 不总成立.

取 $X=\{1,3\}$, $Y=\{0,4\}$. 对 $x=1$ 和 $x=3$ 都可以选 $y=4\in Y$, 且 $x\le 4$. 但是

$$
\inf X=1>0=\inf Y.
$$

---

## 3. 前 $k$ 项的下确界

$c_k=\inf\{b_1,\ldots,b_k\}$.

### (a) $c_k$ 是实数

$\{b_1,\ldots,b_k\}$ 是有限非空集, 最小值存在. 有限集的下确界就是这个最小值, 所以 $c_k\in\mathbb{R}$.

### (b) $(b_n)$ 有界 $\Rightarrow$ $(c_k)$ 收敛

$\{b_1,\ldots,b_k\}\subseteq\{b_1,\ldots,b_{k+1}\}$, 集合变大, 下确界不增, 故 $c_{k+1}\le c_k$. $(c_k)$ 递减.

$(b_n)$ 有界, 每个 $c_k$ 都等于某个 $b_i$, 所以 $(c_k)$ 也有界. 递减且有下界, 由单调收敛定理, $(c_k)$ 收敛.

### (c) $\lim c_k=\liminf b_n$ 不必成立

**本次可跳过.** 讲义没有 $\liminf$. 官方反例如下, 先补定义

$$
\liminf_{n\to\infty}b_n=\lim_{n\to\infty}\Bigl(\inf_{k\ge n}b_k\Bigr)
$$

(有界时右边的极限存在).

**结论**: 不总成立.

取 $b_1=0$, $n\ge 2$ 时 $b_n=1$. 则每个有限前段都含 $0$, 故 $c_k=0$, $\lim c_k=0$.

尾部下确界: $n=1$ 时为 $0$; $n\ge 2$ 时 $\inf_{k\ge n}b_k=1$. 所以 $\liminf b_n=1\neq 0$.

(这个序列本身收敛到 $1$, 因此 $\liminf$ 等于极限 $1$.)

---

## 4. 三个陈述等价

$a_1>0$, $b_1>0$, 且

$$
a_{n+1}=a_n+b_n,\qquad b_{n+1}=a_n b_n.
$$

三个陈述:

- (i) $(a_n)$ 收敛;
- (ii) $(b_n)$ 收敛;
- (iii) 对一切 $n$, $a_n\le 1$.

**结论**: (i), (ii), (iii) 等价.

先归纳: $a_n>0$, $b_n>0$. 于是

$$
a_{n+1}-a_n=b_n>0,
$$

$(a_n)$ 严格递增. 递增序列收敛当且仅当有上界 (单调收敛定理).

**(iii) $\Rightarrow$ (i)**. $a_n\le 1$ 给出上界 $1$. 递增且有上界, 故 $(a_n)$ 收敛.

**(i) $\Rightarrow$ (ii)**. $b_n=a_{n+1}-a_n$. 若 $a_n\to L$, 则 $b_n\to L-L=0$, 故 $(b_n)$ 收敛.

**(ii) $\Rightarrow$ (iii)**. 反设 $(b_n)$ 收敛, 但存在 $N$ 使 $a_N>1$. 递增给出 $n\ge N$ 时 $a_n\ge a_N>1$. 于是

$$
b_{n+1}-b_n=(a_n-1)b_n>0\quad(n\ge N),
$$

$(b_n)_{n\ge N}$ 严格递增, 且 $b_n\ge b_N>0$. 它的极限 $L'$ 满足 $L'\ge b_N>0$. 又 $b_n\neq 0$, 故

$$
a_n=\frac{b_{n+1}}{b_n}\to\frac{L'}{L'}=1.
$$

但 $n\ge N$ 时 $a_n\ge a_N>1$, 且 $(a_n)$ 递增, 极限至少是 $a_N>1$. 与极限等于 $1$ 矛盾.

因此不存在这样的 $N$, 即对一切 $n$ 都有 $a_n\le 1$.

三条围成一圈, 故等价.

---

## 5. 判断

### (a) 假

命题: 有界无穷集 $S$ 满足, 对每个正整数 $n$ 都存在 $a\in S$ 使 $\sup S-1/n<a<\sup S$.

**反例**: $S=\{1/m:m\in\mathbb{N}\}$. 它无穷, 且 $0<1/m\le 1$, 有界. $1\in S$ 是最大元, 故 $\sup S=1$.

取 $n=2$. 要找的是满足 $1/2<a<1$ 的 $a\in S$. $S$ 里小于 $1$ 的元素最大是 $1/2$, 开区间 $(1/2,1)$ 里没有 $S$ 的点.

(官方解答写 $n=1/3$. 题目要求 $n$ 是正整数, $1/3$ 不合格. 同一个 $S$ 用 $n=2$ 即可; $(2/3,1)$ 同样是空的, 但不必用到.)

### (b) 假

命题: $(a_n)$ 有子列趋于 $L_1$, $(b_n)$ 有子列趋于 $L_2$, 则 $(a_n+b_n)$ 有子列趋于 $L_1+L_2$.

**反例**: $a_n=(-1)^{n+1}$, $b_n=(-1)^n$. 奇数项子列 $a_{2k-1}=1\to 1$. 偶数项子列 $b_{2k}=1\to 1$. 但

$$
a_n+b_n=0
$$

对一切 $n$ 成立, 它的任何子列都趋于 $0$, 没有趋于 $1+1=2$ 的子列.

两条子列的下标不必相同, 所以极限不能相加.

### (c) 真

命题: 值域 $C=\{c_1,c_2,\ldots\}$ 在 $\mathbb{R}$ 中稠密, 则 $(c_n)$ 发散.

**证明**: 反设 $c_n\to L\in\mathbb{R}$. 收敛序列有界, 故存在 $M$ 使对一切 $n$ 有 $c_n\le M$. 于是开区间 $(M,M+1)$ 里没有 $C$ 的点. 这与稠密矛盾 (取 $x=M$, $y=M+1$).

因此 $(c_n)$ 发散.

这样的序列存在: $\mathbb{Q}$ 可数, 把有理数排成 $c_1,c_2,\ldots$, 则 $C=\mathbb{Q}$ 稠密, 而这个序列无界, 因而发散.
