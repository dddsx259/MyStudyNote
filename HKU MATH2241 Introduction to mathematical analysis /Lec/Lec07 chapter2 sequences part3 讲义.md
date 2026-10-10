# Chapter 2: 序列 (Sequences) Part 3 — 级数 (Series)

- **来源**: `Lec/Lec07 chapter2 sequences part3.pdf` (8 页)
- **课程**: MATH2241, Fall 2026, K.Y. Chan
- **前置**: Part 1–2 (收敛, MCT, BW, Cauchy)
- **本章目标**: 级数与部分和; 收敛判别 (n-th / 比较 / 极限比较); 绝对收敛与重排; 条件收敛与交错级数判别; Root / Ratio 检验
- **说明**: 凡非定义公式/定理均附 **证明** / **证明思路**; slides 内嵌 Exercise 按出现顺序讲解.

---

## 本节在课程中的位置

Part 1–2 讨论序列 $(x_n)$. Part 3 把无穷和 $\sum x_k$ 定义为**部分和序列**的极限. 许多序列极限工具 (MCT, 比较) 直接翻译成级数判别法; 绝对收敛保证可重排, 条件收敛则不然.

---

## 1. 级数 (Series)

### 定义 1.1 (部分和与级数收敛)

**假设**: $(x_n)$ 为 $\mathbb{R}$ 中序列.

**定义**: 对每个 $k\in\mathbb{N}$, 令
$$
s_k=\sum_{n=1}^k x_n=x_1+\cdots+x_k.
$$
称 $(s_k)$ 为级数 $\sum_{k=1}^\infty x_k$ 的 **部分和序列 (sequence of partial sums)**.

称级数 $\sum_{k=1}^\infty x_k$ **收敛 (converges)**, 若 $\lim_{k\to\infty}s_k$ 存在 (为实数); 否则称级数 **发散 (diverges)**.

(定义, 无需证明.) 部分和也可从较后指标起, 如 $\sum_{k=5}^n x_k$.

### 例 1.1 (几何级数, geometric series)

对 $r>0$, 考虑 $\sum_{k=1}^\infty r^k$.

**(i)** 若 $0<r<1$, 则级数收敛, 且
$$
\sum_{k=1}^\infty r^k=\frac{r}{1-r}.
$$

**证明**: 有限和公式
$$
\sum_{k=1}^n r^k=\frac{r-r^{n+1}}{1-r}.
$$
因 $0<r<1$ 时 $r^{n+1}\to 0$ (Part 1 几何序列), 故
$$
s_n=\frac{r-r^{n+1}}{1-r}\to\frac{r}{1-r}.
$$

**(ii)** 若 $r\ge 1$, 则 $\sum r^k$ 发散.

**证明**: 若 $r>1$, $r^n\to\infty$, $s_n$ 无界故发散. 若 $r=1$, $s_n=n\to\infty$. 亦可用下节 n-th test: $\lim r^n\neq 0$.

### 例 1.2 (调和级数, harmonic series)

令 $x_n=1/n$, $s_n=\sum_{k=1}^n 1/k$. $(s_n)$ 递增. 证明其**无界** (从而发散).

考虑子列项 $s_{2^k-1}$:

1. $s_1=1$;
2. $s_3=1+\frac12+\frac13>1+\frac14+\frac14=1+\frac12$;
3. $s_7=1+\bigl(\frac12+\frac13\bigr)+\bigl(\frac14+\cdots+\frac17\bigr)>1+\frac12+\frac12$.

一般地, 对 $k\ge 1$,
$$
s_{2^{k+1}-1}-s_{2^k-1}=\sum_{j=2^k}^{2^{k+1}-1}\frac{1}{j}>\sum_{j=2^k}^{2^{k+1}-1}\frac{1}{2^{k+1}}=\frac{2^k}{2^{k+1}}=\frac12.
$$
故 $s_{2^k-1}>1+\frac{k-1}{2}$ (对 $k$ 归纳). 因此 $(s_n)$ 无界, 由 MCT 的「收敛 $\Leftrightarrow$ 有界」对单调列, $(s_n)$ 发散. 即 $\sum 1/n$ **发散**.

---

## 2. 若干收敛判别法 (Convergence Tests)

### 定理 2.1 (n-th 项检验 / Term test / n-th series test)

**假设**: 级数 $\sum x_n$ 收敛.

**结论**: $\lim_{n\to\infty}x_n=0$.

**证明**: 令 $s_n=\sum_{k=1}^n x_k$. 收敛 $\Rightarrow$ $\lim s_n$ 存在. 对 $n\ge 2$, $x_n=s_n-s_{n-1}$, 故
$$
\lim x_n=\lim(s_n-s_{n-1})=\lim s_n-\lim s_{n-1}=0.
$$

**用途**: 常用于证**发散**: 若 $\lim x_n\neq 0$ (或不存在), 则级数发散.

### 例 2.2

$x_n=n/(n+1)$, $\lim x_n=1\neq 0$, 故 $\sum n/(n+1)$ 发散.

#### Exercise 2.3

**题目**: $x_n=(-1)^n n$. 判断 $\sum x_n$ 是否收敛.

**讲解**: $\lim x_n$ 不存在 (更谈不上为 0; $|x_n|=n\to\infty$). 由 Thm 2.1 的逆否, 级数发散.

#### Exercise 2.4

**题目**: Thm 2.1 的逆命题是否成立?

**讲解**: **不成立**. 调和级数 $\sum 1/n$: $1/n\to 0$, 但级数发散 (例 1.2). 故「$x_n\to 0$」仅为必要条件, 非充分条件.

### 定理 2.5 (非负项级数 $\Leftrightarrow$ 部分和有界)

**假设**: $(x_n)$ 为非负实数列 ($x_n\ge 0$).

**结论**: $\sum x_n$ 收敛 $\Leftrightarrow$ 部分和序列 $(s_n)$ 有界.

**证明**: $x_n\ge 0$ $\Rightarrow$ $(s_n)$ 递增 (单调). 由 MCT: 递增列收敛 $\Leftrightarrow$ 有界. 故级数收敛 $\Leftrightarrow$ $(s_n)$ 有界.

### 例 2.6 ($p$-调和级数, $p=2$)

$x_n=1/n^p$. 先取 $p=2$:
$$
\begin{aligned}
s_1&=1,\\
s_2&=1+\frac{1}{2^2}<1+\frac12,\\
s_4&<1+\frac{1}{2^2}+\frac{1}{2^2}+\frac{1}{2^2}=1+\frac12+\frac14
\end{aligned}
$$
(更标准的分组: $s_{2^k}<1+\frac12+\cdots+\frac{1}{2^{k-1}}<2$). 故 $(s_{2^k})$ 有界; 又 $(s_n)$ 递增, 故全体 $(s_n)$ 有界. 由 Thm 2.5, $\sum 1/n^2$ 收敛.

#### Exercise 2.7

**题目**: 对 $p\ge 2$, 证 $p$-调和级数 $\sum 1/n^p$ 收敛.

**讲解**: 对 $n\ge 1$, $0\le 1/n^p\le 1/n^2$ (因 $p\ge 2$). 由例 2.6 与下方比较检验 (Thm 2.8(1)), $\sum 1/n^p$ 收敛. (亦可用与 $p=2$ 相同的分组估界.)

课件原题只要求 $p\ge 2$. 下面是完整的 $p$-级数, 分组方式和例 1.2 相同. 同一估计也是后面 Cauchy 凝聚用在 $1/n^p$ 上的结果.

#### $p$-级数 ($p$-series)

**假设**: $p\in\mathbb{R}$, $a_n=1/n^p$.

**结论**: $\sum_{n=1}^{\infty} 1/n^p$ 收敛当且仅当 $p>1$.

调和级数是 $p=1$ 的特例, 发散 (例 1.2). $p>1$ 才收敛, 包括 $1<p<2$, 不限于课件里的 $p\ge 2$.

**证明**:

**$p>1$**. 部分和递增. 把和分成 $n=2^k,\ldots,2^{k+1}-1$ 这一段, 共 $2^k$ 项, 每一项 $\le 1/(2^k)^p$. 于是

$$
\sum_{n=2^k}^{2^{k+1}-1}\frac{1}{n^p}\le 2^k\cdot 2^{-kp}=2^{k(1-p)}.
$$

$k=0$ 时这一段只有 $n=1$, 上界 $2^{0}=1$ 仍然成立. $p>1$ 时公比 $r=2^{1-p}\in(0,1)$. 故

$$
s_{2^{N+1}-1}=\sum_{k=0}^{N}\sum_{n=2^k}^{2^{k+1}-1}\frac{1}{n^p}
\le\sum_{k=0}^{N} r^k
<\frac{1}{1-r}.
$$

$(s_{2^m-1})$ 有界. $(s_n)$ 递增, 所以全体部分和有界. 由 Thm 2.5, 级数收敛.

**$0<p\le 1$**. $n^p\le n$, 故 $1/n^p\ge 1/n$. 部分和不小于调和级数的部分和. 例 1.2 说后者无界, 所以 $\sum 1/n^p$ 发散.

**$p\le 0$**. $1/n^p\ge 1\not\to 0$. 由 Thm 2.1, 级数发散.

#### Cauchy 凝聚 (Cauchy condensation test)

课件没有这条. 它是 Tut4 第 6 题, 用来把正项递减级数收成一条更稀的级数.

**假设**: $a_n\ge 0$, 且 $(a_n)$ 递减.

**结论**: $\sum_{n=1}^{\infty} a_n$ 收敛当且仅当 $\sum_{n=0}^{\infty} 2^n a_{2^n}$ 收敛.

右边叫凝聚级数: 只留下下标 $1,2,4,8,\ldots$ 的项, 再乘上这一段的长度 $2^n$.

**证明**: 记 $s_m=\sum_{k=1}^{m} a_k$, $t_N=\sum_{n=0}^{N} 2^n a_{2^n}$. 两项都非负, 由 Thm 2.5, 各自收敛当且仅当部分和有界.

**原级数收敛 $\Rightarrow$ 凝聚级数收敛**. 设 $\sum a_n$ 的和为 $s$, 则 $s_m\le s$.

$n\ge 1$ 时, 从 $k=2^{n-1}+1$ 到 $k=2^n$ 共 $2^{n-1}$ 项, 且 $k\le 2^n$. 递减给出 $a_k\ge a_{2^n}$, 所以

$$
\sum_{k=2^{n-1}+1}^{2^n} a_k\ge 2^{n-1}a_{2^n}=\frac12\cdot 2^n a_{2^n}.
$$

对 $n=1,\ldots,N$ 求和,

$$
\sum_{n=1}^{N} 2^n a_{2^n}\le 2\sum_{k=2}^{2^N} a_k\le 2s.
$$

再加上 $2^0 a_1=a_1\le s$, 得 $t_N\le 3s$. $(t_N)$ 有界, 凝聚级数收敛.

**凝聚级数收敛 $\Rightarrow$ 原级数收敛**. 设凝聚级数的和为 $t$, 则 $t_N\le t$.

同一段里每个 $a_k\le a_{2^{n-1}}$, 共 $2^{n-1}$ 项, 所以

$$
\sum_{k=2^{n-1}+1}^{2^n} a_k\le 2^{n-1}a_{2^{n-1}}.
$$

于是

$$
s_{2^N}=a_1+\sum_{n=1}^{N}\sum_{k=2^{n-1}+1}^{2^n} a_k
\le a_1+\sum_{n=1}^{N} 2^{n-1}a_{2^{n-1}}.
$$

后一和令 $m=n-1$, 就是 $t_{N-1}\le t$. 故 $s_{2^N}\le a_1+t$. 对任意 $M$, 取 $N$ 使 $2^N\ge M$. 部分和递增, $s_M\le s_{2^N}\le a_1+t$. $(s_M)$ 有界, 原级数收敛.

**用在 $p$-级数上**. $p>0$ 时 $a_n=1/n^p$ 递减且非负. $2^n a_{2^n}=(2^{1-p})^n$. 几何级数在公比 $2^{1-p}<1$ 时收敛, 即 $p>1$. 这和上一小节的分组是同一件事.

### 定理 2.8 (比较检验, Comparison Test)

**假设**: $(x_n),(y_n)$ 满足 $0\le x_n\le y_n$ 对一切 $n$.

**结论**:

1. 若 $\sum y_n$ 收敛, 则 $\sum x_n$ 收敛;
2. 若 $\sum x_n$ 发散, 则 $\sum y_n$ 发散.

**证明**: (1) $\sum y_n$ 收敛 $\Rightarrow$ 其部分和有界 (Thm 2.5, 因 $y_n\ge 0$). 又 $0\le\sum_{k=1}^n x_k\le\sum_{k=1}^n y_k$, 故 $\sum x_n$ 的部分和有界, 再由 Thm 2.5 收敛. (2) 是 (1) 的逆否.

#### Exercise 2.9

**题目**:

1. $x_1=1$, $n\ge 2$ 时 $x_n=1/(n(n-1))$. 用 $1/(n(n-1))=1/(n-1)-1/n$ 证明部分和有上界.
2. 结合 Thm 2.8 推出 $\sum 1/n^2$ 收敛.

**讲解**:

(1) 对 $n\ge 2$,
$$
\sum_{k=2}^n x_k=\sum_{k=2}^n\Bigl(\frac{1}{k-1}-\frac{1}{k}\Bigr)=1-\frac{1}{n}<1.
$$
故 $s_n=x_1+\sum_{k=2}^n x_k=1+(1-1/n)<2$. 部分和有上界, 由 Thm 2.5, $\sum x_n$ 收敛 (望远镜级数, telescoping).

(2) 对 $n\ge 2$, $0\le 1/n^2\le 1/(n(n-1))=x_n$ (因 $n^2\ge n(n-1)$). $\sum_{n=2}^\infty x_n$ 收敛 $\Rightarrow$ 由比较检验 $\sum_{n=2}^\infty 1/n^2$ 收敛, 加上有限项后 $\sum_{n=1}^\infty 1/n^2$ 收敛.

### 例 2.10

$\sum 1/(n^2+2n)$ 收敛: $0<1/(n^2+2n)<1/n^2$, 且 $\sum 1/n^2$ 收敛, 用 Thm 2.8.

### 定理 2.11 (极限比较检验, Limit Comparison Test)

**假设**: $(x_n),(y_n)$ 严格正; $r:=\lim_{n\to\infty}(x_n/y_n)$ 存在.

**结论**:

(a) 若 $r\neq 0$, 则 $\sum x_n$ 收敛 $\Leftrightarrow$ $\sum y_n$ 收敛;

(b) 若 $r=0$ 且 $\sum y_n$ 收敛, 则 $\sum x_n$ 收敛.

**证明**:

**(a)** 取 $\varepsilon=r/2>0$ (因 $r>0$; 若 $r=\infty$ 课件假设极限存在为有限). 存在 $N$ 使 $n>N$ 时
$$
\Bigl|\frac{x_n}{y_n}-r\Bigr|<\frac{r}{2}\implies \frac{r}{2}y_n<x_n<\frac{3r}{2}y_n.
$$
(课件写 $1/(2r)$ 一侧等价改写.) 由比较检验: $\sum y_n$ 收敛 $\Rightarrow$ $\sum (3r/2)y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛; $\sum x_n$ 收敛 $\Rightarrow$ $\sum (r/2)y_n$ 收敛 $\Rightarrow$ $\sum y_n$ 收敛.

**(b)** $r=0$: 取 $\varepsilon=1$, 存在 $N$ 使 $n>N$ 时 $0<x_n/y_n<1$, 即 $x_n\le y_n$. 由 Thm 2.8 得结论.

### 例 2.12

$\sum 1/(n^3-n^2+1)$ 收敛: 与 $1/n^3$ 比,
$$
\lim\frac{1/(n^3-n^2+1)}{1/n^3}=\lim\frac{n^3}{n^3-n^2+1}=1\neq 0,
$$
且 $\sum 1/n^3$ 收敛 ($p=3\ge 2$), 用 Thm 2.11(a).

---

## 3. 绝对收敛与条件收敛 (Absolute / Conditional Convergence)

### 定义 3.1 (绝对收敛)

**定义**: 称 $\sum x_k$ **绝对收敛 (absolutely convergent)**, 若 $\sum |x_k|$ 收敛. (定义, 无需证明.)

### 例 3.2

$\sum (-1)^k/k^2$ 绝对收敛, 因 $\sum 1/k^2$ 收敛.

### 定理 3.3 (绝对收敛 $\Rightarrow$ 收敛)

**假设**: $\sum |x_k|$ 收敛.

**结论**: $\sum x_k$ 收敛.

**证明**: 对一切 $n$,
$$
0\le x_n+|x_n|\le 2|x_n|.
$$
$\sum 2|x_k|$ 收敛 $\Rightarrow$ 由比较检验 $\sum(x_k+|x_k|)$ 收敛. 又
$$
x_k=(x_k+|x_k|)-|x_k|,
$$
两收敛级数之差收敛, 故 $\sum x_k$ 收敛.

### 例 3.4

$\sum (-1)^k/k^2$ 绝对收敛, 故亦收敛.

#### Exercise 3.5

**题目**: 判断收敛性: (a) $\sum (-1)^k/(k^2+1)$; (b) $\sum (-1)^k\sin(k)/k^2$.

**讲解**:

(a) $|(-1)^k/(k^2+1)|\le 1/k^2$, $\sum 1/k^2$ 收敛 $\Rightarrow$ 绝对收敛 $\Rightarrow$ 收敛.

(b) $|\sin(k)/k^2|\le 1/k^2$, 同理绝对收敛 (从而收敛). ($\sin k$ 不趋于 0 不影响被 $1/k^2$ 压住.)

### 定义 3.6 (重排, rearrangement)

**定义**: $\sum y_n$ 称为 $\sum x_n$ 的 **重排**, 若存在双射 $f:\mathbb{N}\to\mathbb{N}$ 使 $y_n=x_{f(n)}$. (定义, 无需证明.)

### 定理 3.7 (重排定理, Rearrangement Theorem)

**假设**: $\sum x_n$ 绝对收敛, 且 $\sum x_n=L$; $\sum y_n$ 为其任一重排.

**结论**: $\sum y_n$ 亦收敛到 $L$.

**证明思路**: 令 $t_n=\sum_{k=1}^n y_k$, $s_m=\sum_{k=1}^m x_k$. 设 $f$ 为重排双射. 给定 $m$, 取 $N$ 充分大使 $\{1,\ldots,m\}\subset\{f(1),\ldots,f(N)\}$. 则对 $n\ge N$, $t_n$ 包含 $x_1,\ldots,x_m$, 故
$$
|t_n-L|\le|t_n-s_m|+|s_m-L|\le\sum_{k=m+1}^\infty |x_k|+|s_m-L|.
$$
先令 $n\to\infty$ (或对固定 $m$ 取 $n\ge N$), 再令 $m\to\infty$: 绝对收敛 $\Rightarrow$ 尾部 $\sum_{k>m}|x_k|\to 0$, 且 $s_m\to L$, 故 $t_n\to L$.

#### Exercise 3.8

**题目**: $\sum x_n$ 绝对收敛, $\sum y_n$ 为其重排. 用 Thm 3.7 推出 $\sum y_n$ 也绝对收敛.

**讲解**: $\sum |x_n|$ 收敛 (绝对收敛定义). $(|y_n|)$ 是 $(|x_n|)$ 的重排 (同一双射). 由 Thm 3.7 应用于非负项级数 $\sum |x_n|$, 得 $\sum |y_n|$ 收敛到同一和. 故 $\sum y_n$ 绝对收敛.

### 定义 3.9 (条件收敛)

**定义**: 称 $\sum x_n$ **条件收敛 (conditionally convergent)**, 若 $\sum x_n$ 收敛但**非**绝对收敛. (定义, 无需证明.)

### 例 3.10 (交错调和级数)

$\sum_{n=1}^\infty (-1)^{n+1}/n$ 条件收敛: $\sum 1/n$ 发散, 而交错级数收敛见 Thm 3.13.

### 例 3.11

$\sum (-1)^n/n^2$ 绝对收敛, 故**不是**条件收敛.

#### Exercise 3.12

**题目**: 说明收敛 / 绝对收敛 / 条件收敛的关系.

**讲解**:

- 绝对收敛 $\Rightarrow$ 收敛 (Thm 3.3);
- 条件收敛 $\Rightarrow$ 收敛, 但 $\sum |x_n|$ 发散;
- 绝对收敛与条件收敛互斥; 二者合起来覆盖「收敛但可能/不可能重排保和」的情形;
- 发散 $\Rightarrow$ 既非绝对亦非条件收敛.

### 定理 3.13 (交错级数判别, Alternating Series Test / Leibniz test)

**假设**: $(x_n)$ 为严格正的递减列, 且 $\lim x_n=0$.

**结论**: 交错级数 $\sum (-1)^{n+1}x_n$ 收敛.

**证明**:

令 $s_n=\sum_{k=1}^n (-1)^{k+1}x_k$.

**Step 1** ($(s_{2k})$ 递增):
$$
s_{2k}=(x_1-x_2)+(x_3-x_4)+\cdots+(x_{2k-1}-x_{2k}).
$$
递减 $\Rightarrow$ 每项 $x_{2j-1}-x_{2j}\ge 0$, 故 $s_{2k}$ 递增.

**Step 2** (有上界):
$$
s_{2k}=x_1-(x_2-x_3)-\cdots-(x_{2k-2}-x_{2k-1})-x_{2k}<x_1.
$$

**Step 3**: 由 MCT, $s_{2k}\to L$ 某极限. 又 $s_{2k+1}=s_{2k}+x_{2k+1}$, 且 $x_n\to 0$, 故 $s_{2k+1}\to L$. 奇偶子列同极限 $\Rightarrow$ $s_n\to L$.

#### Exercise 3.14

**题目**: 判断绝对/条件收敛: (a) $\sum (-1)^{n+1}/\sqrt{n+1}$; (b) $\sum (-1)^{n+1}/(n^2+1)$.

**讲解**:

(a) $|a_n|=1/\sqrt{n+1}$ 递减 $\to 0$, 由 AST 收敛. 但 $\sum 1/\sqrt{n+1}$ 与调和 $p=1/2\le 1$ 同类发散 (比较: $1/\sqrt{n+1}\ge 1/\sqrt{2n}$ 对大 $n$), 故为**条件收敛**.

(b) $|a_n|\le 1/n^2$, 绝对收敛 (从而非条件收敛).

#### Exercise 3.15 (条件收敛时重排可改变和)

**题目**:

(a) 证 $0<\sum_{n=1}^\infty (-1)^{n+1}/n<1$.

(b) 考虑重排 $(1-1/2)-1/4+(1/3-1/6)-1/8+(1/5-1/10)+\cdots$, 证其和**不等于**原交错调和级数之和.

**讲解**:

(a) 令 $x_n=1/n>0$, 则 $(x_n)$ 严格递减且 $x_n\to 0$, 故由 AST (定理 3.13) 知交错调和级数收敛, 记 $L=\sum_{n=1}^\infty (-1)^{n+1}/n$, 部分和 $s_n=\sum_{k=1}^n (-1)^{k+1}/k$.

由 AST 证明: $(s_{2k})$ 递增且 $s_{2k}<x_1=1$, 故 $s_{2k}\uparrow L$; 又 $s_{2k+1}=s_{2k}+x_{2k+1}$, 且可验证 $(s_{2k+1})$ 递减并趋于同一极限 $L$.

- **下界**: $s_2=1-1/2=1/2>0$. 因 $(s_{2k})$ 递增, 有 $L=\lim s_{2k}\ge s_2=1/2>0$.
- **上界**: $s_3=1-1/2+1/3=5/6<1$. 因 $(s_{2k+1})$ 递减, 有 $L=\lim s_{2k+1}\le s_3=5/6<1$.

因此 $0<L<1$, 即 $0<\sum_{n=1}^\infty (-1)^{n+1}/n<1$.

(注: 仅由 $s_{2k}<1$ 只能得 $L\le 1$; 严格 $<1$ 需用奇项递减, 例如 $L\le s_3=5/6$.)

(b) 该重排模式大致为: 取一个正项, 再减两个负项量级 (或课件给出的分组). 分组后每组形如
$$
\Bigl(\frac{1}{2k-1}-\frac{1}{4k-2}\Bigr)-\frac{1}{4k}=\frac{1}{2(2k-1)}-\frac{1}{4k}=\frac{1}{4k(2k-1)}>0,
$$
部分和趋于某个 $L'\neq L$ (可证 $L'=L/2$). 要点: **条件收敛级数重排可改变和** (Riemann 重排定理的特例); 对比绝对收敛时 Thm 3.7.

---

## 4. 根值与比值检验 (Root and Ratio Tests)

### 定理 3.16 (Root Test)

**假设**: $r=\lim_{n\to\infty}\sqrt[n]{|x_n|}$ 存在.

**结论**:

(a) $r<1$ $\Rightarrow$ $\sum x_n$ 绝对收敛;

(b) $r>1$ $\Rightarrow$ $\sum x_n$ 发散;

(c) $r=1$ 时检验无效.

**证明**:

**(a)** 取 $r_0\in(r,1)$, $\varepsilon=r_0-r$. 存在 $K$ 使 $n>K$ 时 $\sqrt[n]{|x_n|}<r_0$, 即 $|x_n|<r_0^n$. $\sum r_0^n$ 为几何级数 ($0<r_0<1$) 收敛, 比较得 $\sum |x_n|$ 收敛.

**(b)** 存在 $K$ 使 $n>K$ 时 $\sqrt[n]{|x_n|}>1$, 即 $|x_n|>1$, 故 $x_n\not\to 0$, 由 n-th test 发散.

### 定理 3.17 (Ratio Test)

**假设**: $x_n\neq 0$, $r=\lim |x_{n+1}|/|x_n|$ 存在.

**结论**: $r<1$ $\Rightarrow$ 绝对收敛; $r>1$ $\Rightarrow$ 发散; $r=1$ 无效.

**证明思路**: 与 Root Test 类似. 若 $r<1$, 取 $r_0\in(r,1)$, 大 $n$ 时 $|x_{n+1}|\le r_0|x_n|$, 从而 $|x_n|\le C r_0^n$, 与几何级数比较. 若 $r>1$, 则大 $n$ 时 $|x_{n+1}|>|x_n|$, 故 $x_n\not\to 0$. 细节见 Bartle–Sherbert p.272.

### 例 3.18

$x_n=1/(-3)^n$: $\sqrt[n]{|x_n|}=1/3<1$ (Root); $|x_{n+1}|/|x_n|=1/3$ (Ratio). 两种检验均得绝对收敛.

#### Exercise 3.19

**题目**: 用 Root/Ratio 判断: (1) $\sum (-1)^n/(2^n n)$; (2) $\sum (1+1/n)^{n^2}$.

**讲解**:

(1) Ratio:
$$
\Bigl|\frac{x_{n+1}}{x_n}\Bigr|=\frac{2^n n}{2^{n+1}(n+1)}=\frac{n}{2(n+1)}\to\frac12<1,
$$
故绝对收敛. (Root 亦可, 但含 $n^{1/n}\to 1$.)

(2) Root:
$$
\sqrt[n]{\Bigl(1+\frac{1}{n}\Bigr)^{n^2}}=\Bigl(1+\frac{1}{n}\Bigr)^n\to e>1,
$$
故 $r=e>1$, 级数发散. (项甚至 $\to\infty$, 不趋于 0.)

---

## 本节要点速览

| 工具 | 典型用途 |
|---|---|
| n-th test | 证发散 ($x_n\not\to 0$) |
| 非负 + 部分和有界 | 等价于收敛 |
| Comparison / Limit comparison | 与已知 $p$-级数, 几何级数比较 |
| Absolute $\Rightarrow$ 收敛 | 处理变号项 |
| Rearrangement | 仅绝对收敛保和 |
| AST | 交错 + 递减 $\to 0$ |
| Root / Ratio | $r<1$ 绝对收敛; $r>1$ 发散 |

---

## 与前后材料衔接

- **Assignment 3**: 嵌套区间 / Heine–Borel 型有限覆盖, 与「级数」并列同属 Ch2 后段技巧; 有理 Cauchy 反例呼应 Part 2 完备性.
- **下一主题**: 连续函数 (syllabus: Continuity, 约 Week of 5/10).
