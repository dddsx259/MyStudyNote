# Chapter 2: 序列 (Sequences) Part 1

- **来源**: `Lec/Lec05 chapter2 sequences part1.pdf` (11 页; 原名 `Chapter2 (Part1)(2026).pdf`)
- **课程**: MATH2241, Fall 2026, K.Y. Chan
- **前置**: Chapter 1 实数 / 完备性 / 确界
- **本章目标 (本 PDF)**: 序列与收敛 ($\varepsilon$-$N$), 有界性, 极限代数与夹逼, 单调收敛定理 (MCT), 常用极限 ($r^n$, $n^{1/n}$, $e$)
- **说明**: 凡非定义公式/定理均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

---

## 本节在课程中的位置

有了完备实数后, 用 **序列极限** 精确化「无限逼近」. Part 1 建立 $\varepsilon$-$N$ 语言与 MCT; 后续 Part 将继续子列 / Cauchy 等.

---

## 1. 序列与收敛

### 定义 1.1 (序列)

**定义**: $\mathbb{R}$ 中的序列是函数 $x:\mathbb{N}\to\mathbb{R}$; 记 $x(n)=x_n$, 或写作 $(x_n)$ / $(x_1,x_2,\ldots)$. (定义, 无需证明.)

**例**: 常值; 几何 $x_n=r^n$; $(-1)^n$; Fibonacci: $f_1=f_2=1$, $f_{n+1}=f_n+f_{n-1}$.

### Exercise 1.3

**题目**:
(1) 设 $(x_n)$ 为 $\mathbb{R}$ 中序列. 说明: 存在 $r\in\mathbb{R}$ 使得对所有 $n\in\mathbb{N}$ 有 $x_n\neq r$.
(2) 描述一条 $(x_n)\subset\mathbb{Q}$, 使得对每个 $r\in\mathbb{Q}$, 存在 **唯一** $m\in\mathbb{N}$ 满足 $x_m=r$.

**讲解**:

**(1) 证法 A (可数性 / 对角线思想)**

反证: 若每个 $r\in\mathbb{R}$ 都等于某个 $x_n$, 则
$$
\mathbb{R}\subseteq \{x_n:n\in\mathbb{N}\},
$$
右端至多可数, 与 $\mathbb{R}$ 不可数矛盾. 故必存在 $r\in\mathbb{R}$ 不在 $\{x_n\}$ 中, 即 $x_n\neq r$ 对所有 $n$ 成立.

**(1) 证法 B (嵌套闭区间, 与 BW 构造同型)**

在 $[0,1]$ 上归纳构造闭区间套 $[a_k,b_k]$:
- 设已得 $[a_{n-1},b_{n-1}]$, 长度 $\ell_{n-1}>0$, 且 $x_1,\ldots,x_{n-1}$ 皆不在其中 ( $n=1$ 时取 $[a_0,b_0]=[0,1]$ ).
- 将 $[a_{n-1},b_{n-1}]$ 二等分. 若 $x_n$ 落在左半, 取右半为 $[a_n,b_n]$; 若落在右半, 取左半; 若 $x_n$ 恰为端点, 仍可取 **不含** $x_n$ 的那一半 (闭区间, 端点可归属一侧).

则 $|b_n-a_n|=\ell_{n-1}/2\to 0$, 且对每个 $k$, $x_k\notin[a_k,b_k]$. 由 **嵌套区间定理**, $\bigcap_{k=1}^\infty[a_k,b_k]=\{r\}$. 若 $r=x_m$, 则 $r\in[a_m,b_m]$, 与 $x_m\notin[a_m,b_m]$ 矛盾. 故 $r\neq x_n$ 对所有 $n$.

**(2)** 因 $\mathbb{Q}$ 可数, 可写 $\mathbb{Q}=\{q_1,q_2,q_3,\ldots\}$ (例如按 Stern–Brocot 或任意固定枚举). 令 $x_n=q_n$. 对任意 $r\in\mathbb{Q}$, 存在唯一 $k$ 使 $r=q_k$, 故唯一 $m=k$ 满足 $x_m=r$.

---

### 定义 1.4 (收敛 / 极限)

**假设**: $(x_n)$ 为实序列, $x\in\mathbb{R}$.

**定义**: $(x_n)$ **收敛于** $x$ (写作 $\lim x_n=x$ 或 $\lim_{n\to\infty}x_n=x$) 当且仅当: 对每个 $\varepsilon>0$, 存在 $N=N(\varepsilon)$ 使一切 $n>N$ 满足 $|x_n-x|<\varepsilon$.

- 极限存在则称 **收敛 (convergent)**; 否则 **发散 (divergent)**.

### Exercise 1.5

**题目**: 画实数轴, 标出定义 1.4 中落在区间 $(x-\varepsilon,x+\varepsilon)$ 内的那些 $x_n$.

**讲解**:

固定极限 $x$ 与 $\varepsilon>0$. 开区间 $(x-\varepsilon,x+\varepsilon)$ 是 $x$ 的 **$\varepsilon$-邻域**. 定义 1.4 说: 存在 $N(\varepsilon)$, 使得 **一切** $n>N(\varepsilon)$ 对应的 $x_n$ 都落在此开区间内 (在数轴上用点标出). $n\le N(\varepsilon)$ 的 **有限多个** 前项可以落在区间外, 不影响收敛.

图示要点: 在 $x$ 两侧各标 $x-\varepsilon$, $x+\varepsilon$ (开区间, 端点空心); $N$ 之后所有 $x_n$ 点都夹在中间; 前面少数点可任意.

---

### 定理 1.6 (极限唯一性)

**假设**: $(x_n)$ 收敛.

**结论**: 极限唯一.

**证明**: 设 $x',x''$ 皆为极限且 $x'\neq x''$. 取 $\varepsilon=|x'-x''|/2>0$. 存在 $N',N''$ 使 $n>\max\{N',N''\}$ 时 $|x_n-x'|<\varepsilon$ 且 $|x_n-x''|<\varepsilon$. 于是
$$
|x'-x''|\le|x'-x_n|+|x_n-x''|<2\varepsilon=|x'-x''|,
$$
矛盾. 故 $x'=x''$.

**例 1.7**: $\lim 1/n=0$ (取 $N>1/\varepsilon$); $\lim 2/(n^2+2)=0$ ($\varepsilon\ge 1$ 取 $N=1$; $\varepsilon<1$ 取 $N>\sqrt{2/\varepsilon-2}$).

### Exercise 1.8

**题目**: (非收敛例) 设 $x_n=(-1)^n$. 用 $\varepsilon$-$N$ 极限定义证明 $(x_n)$ 发散.

**讲解**:

反证: 设 $\lim x_n=L\in\mathbb{R}$. 取 $\varepsilon=\tfrac{1}{2}$. 按定义, 存在 $N$ 使一切 $n>N$ 有 $|x_n-L|<\tfrac{1}{2}$.

取 $n>N$ 为 **偶数**, 则 $x_n=1$, 故 $|1-L|<\tfrac{1}{2}$.
取 $m>N$ 为 **奇数**, 则 $x_m=-1$, 故 $|-1-L|<\tfrac{1}{2}$.

两式相加并用三角不等式:
$$
2=|1-(-1)|\le|1-L|+|-1-L|<\tfrac{1}{2}+\tfrac{1}{2}=1,
$$
矛盾. 故极限不存在, $(x_n)$ 发散.

---

### Exercise 1.9

**题目**: 设 $(x_n)\subset\mathbb{R}$, $m\in\mathbb{N}$, 定义尾序列 $y_n=x_{m+n}$. 用 $\varepsilon$-$N$ 证明: $(x_n)$ 收敛 $\Leftrightarrow$ $(y_n)$ 收敛; 且若极限存在, 则 $\lim y_n=\lim x_n$.

**讲解**:

**($\Rightarrow$)** 设 $x_n\to x$. 对 $\varepsilon>0$, 存在 $N_1$ 使 $n>N_1$ 时 $|x_n-x|<\varepsilon$. 令 $N=N_1-m$ (若 $m\ge N_1$ 则取 $N=1$). 对 $n>N$, 有 $m+n>N_1$, 故
$$
|y_n-x|=|x_{m+n}-x|<\varepsilon.
$$
故 $y_n\to x$.

**($\Leftarrow$)** 设 $y_n\to y$. 对 $\varepsilon>0$, 存在 $N_2$ 使 $n>N_2$ 时 $|y_n-y|<\varepsilon$, 即 $|x_{m+n}-y|<\varepsilon$. 令 $K=N_2+m$. 则一切 $k>K$ 可写 $k=m+n$ 且 $n>N_2$, 故 $|x_k-y|<\varepsilon$. 又前 $m$ 项 $x_1,\ldots,x_m$ 有限, 不影响极限, 故 $x_n\to y$.

两方向极限值相同: 上式均为 $x$ 或 $y$, 故 $\lim x_n=\lim y_n$.


---


## 2. 收敛 $\Rightarrow$ 有界

### 定义 2.1 (有界序列)

**定义**: $(x_n)$ 有界 $\Leftrightarrow$ 集合 $\{x_n:n\in\mathbb{N}\}$ 有界 (存在 $L,M$ 使 $L<x_n<M$ $\forall n$). (定义.)

### 定理 2.2

**假设**: $(x_n)$ 在 $\mathbb{R}$ 中收敛.

**结论**: $(x_n)$ 有界.

**证明**: 设 $x=\lim x_n$, 取 $\varepsilon=1$, 得 $N$ 使 $n>N$ 时 $|x_n-x|<1$. 令 $M=\max\{x+1,x_1,\ldots,x_N\}$, 则全体 $x_n\le M$. 下界类似.

**注**: 逆命题不成立 (有界不必收敛, 如 $(-1)^n$).

### 引理 2.4 / 推论 2.5

**假设**: $(x_n)$ 收敛且 $L\le x_n\le M$ $\forall n$.

**结论**: $L\le\lim x_n\le M$. 特别地, 若 $x_n\in[a,b]$ 且收敛, 则 $\lim x_n\in[a,b]$.

**证明思路**: 若 $\lim x_n>M$, 取 $\varepsilon$ 使 $x-\varepsilon>M$, 则大 $n$ 时 $x_n>M$, 矛盾. 下界同理.

**注意**: 不能把 $\le$ 随意改成严格 $<$ (极限可落在端点).

### Exercise 2.6

**题目**:
(a) 定理 2.2 的逆命题是否成立?
(b) 引理 2.4 中的非严格不等式能否全部改为严格不等式?

**讲解**:

**(a)** **不成立**. 反例: $x_n=(-1)^n$ 有界 ($|x_n|\le 1$) 但不收敛 (Ex 1.8).

**(b)** **不能** 随意改为严格不等式. 反例: $x_n=\tfrac{1}{n+1}$, 则 $0<x_n<1$ 对所有 $n$, 但 $\lim x_n=0$, 极限落在下界上而非 $(0,1)$ 内. 推论 2.5 对闭区间 $[a,b]$ 成立正是因为允许极限取端点.


---


## 3. 极限的代数与夹逼

### 定理 3.1 (极限运算)

**假设**: $\lim x_n=x$, $\lim y_n=y$.

**结论**:
- $\lim(cx_n)=cx$; $\lim(x_n\pm y_n)=x\pm y$; $\lim(x_ny_n)=xy$; $\lim(-x_n)=-x$
- 若 $x_n\neq 0$ 且 $x\neq 0$, 则 $\lim(1/x_n)=1/x$

**证明思路**:
- 标量/加法: 对给定 $\varepsilon$ 分别取更小的 $\varepsilon/|c|$ 或 $\varepsilon/2$, 再取 $N=\max\{N_x,N_y\}$.
- 乘积: 先用 Thm 2.2 得有界 $|x_n|,|y_n|<M$; 写
  $|x_ny_n-xy|\le M|y_n-y|+M|x_n-x|$, 取足够小的容差.
- 倒数: 先证 $|x_n|$ 最终有正下界 $M>0$ (类似有界证明), 再用 $|1/x_n-1/x|=|x-x_n|/(|x_n||x|)$.

**例**: $x_n=2(1-1/n)\Rightarrow\lim=2$.

### Exercise 3.3

**题目**: 设 $k\in\mathbb{N}$ 为正整数, $(x_n)$ 收敛于 $x$. 证明 $\lim x_n^k=x^k$.

**讲解**:

**$k=1$**: 即已知条件.

**$k=2$**: 由定理 3.1(c), $\lim(x_n\cdot x_n)=x\cdot x=x^2$.

**归纳步**: 设 $\lim x_n^{k-1}=x^{k-1}$. 则
$$
x_n^k=x_n\cdot x_n^{k-1},\quad
\lim x_n^k=\lim(x_n)\cdot\lim(x_n^{k-1})=x\cdot x^{k-1}=x^k
$$
(再用 Thm 3.1(c)). 故对所有正整数 $k$ 成立.

---

### Exercise 3.4

**题目**: 设 $x_n=\dfrac{n^2+2n+3}{3n^2+4n+5}$. 求 $\lim x_n$.

**讲解**:

分子分母同除 $n^2$:
$$
x_n=\frac{1+2/n+3/n^2}{3+4/n+5/n^2}\xrightarrow[n\to\infty]{}\frac{1}{3}.
$$
(用 $\lim(1/n)=0$ 与 Thm 3.1.)

---

### Exercise 3.5

**题目**: 设 $(x_n),(y_n),(z_n)$ 在 $\mathbb{R}$ 中收敛, 且 $x_n\le y_n\le z_n$ 对所有 $n\in\mathbb{N}$. 证明 $\lim x_n\le\lim y_n\le\lim z_n$.

**讲解**:

令 $a=\lim x_n$, $b=\lim y_n$, $c=\lim z_n$. 反证 $b<a$: 取 $\varepsilon=(a-b)/2>0$. 存在 $N$ 使 $n>N$ 时 $|x_n-a|<\varepsilon$, 故 $x_n>a-\varepsilon=(a+b)/2$. 又 $y_n\ge x_n$, 故 $y_n>(a+b)/2$. 令 $n\to\infty$ 得 $b\ge(a+b)/2$, 即 $b\ge a$, 与 $b<a$ 矛盾. 故 $b\ge a$. 同理 $b\le c$. 因此 $a\le b\le c$.

---

### 定理 3.6 (夹逼 / Squeeze)

**假设**: $x_n\le y_n\le z_n$ $\forall n$; $\lim x_n=\lim z_n=w$.

**结论**: $\lim y_n=w$.

**证明**: 对 $\varepsilon>0$, 大 $n$ 时 $|x_n-w|<\varepsilon$, $|z_n-w|<\varepsilon$, 故 $-\varepsilon<x_n-w\le y_n-w\le z_n-w<\varepsilon$.

**例 3.8**: $\sqrt{n+1}-\sqrt{n}=1/(\sqrt{n+1}+\sqrt{n})\in(0,1/(2\sqrt{n}))\to 0$.

### Exercise 3.9

**题目**: 设 $(x_n)\subset\mathbb{R}$, $x\in\mathbb{R}$, $(a_n)$ 为正数列且 $\lim a_n=0$. 若对所有 $n\in\mathbb{N}$ 有 $|x_n-x|\le a_n$, 证明 $\lim x_n=x$.

**讲解**:

对 $\varepsilon>0$, 因 $a_n\to 0$, 存在 $N$ 使 $n>N$ 时 $0<a_n<\varepsilon$. 则
$$
|x_n-x|\le a_n<\varepsilon.
$$
由收敛定义, $x_n\to x$.


---


## 4. 单调收敛定理 (MCT)

### 定义 4.1 (单调)

**定义**: 递增: $x_1\le x_2\le\cdots$; 递减对偶; 单调 = 递增或递减. (定义.)

### 定理 4.3 (Monotone Convergence Theorem)

**假设**: $(x_n)$ 单调.

**结论**: $(x_n)$ 收敛 $\Leftrightarrow$ $(x_n)$ 有界.

**证明** (递增情形):
- ($\Rightarrow$) 由 Thm 2.2.
- ($\Leftarrow$) 令 $s=\sup\{x_n\}$ (完备性). 对 $\varepsilon>0$ 存在 $N$ 使 $x_N>s-\varepsilon$. 递增 $\Rightarrow$ $n>N$ 时 $s-\varepsilon<x_n\le s$, 即 $|x_n-s|<\varepsilon$. 故 $\lim x_n=s$.

### 推论 4.4

**假设 / 结论**:
- 有界递增 $\Rightarrow$ $\lim x_n=\sup\{x_n\}$
- 有界递减 $\Rightarrow$ $\lim x_n=\inf\{x_n\}$

**注**: 去掉单调则假: $x_1=3$, $x_n=2-1/n$ ($n\ge 2$) 收敛到 $2$ 但 $\sup=3$.

**例 4.5**: $1<x_1<2$, $x_{n+1}=1+\sqrt{x_n-1}$. 归纳得递增且落在 $(1,2)$; MCT $\Rightarrow$ 极限 $L$ 满足 $(L-1)^2=L-1\Rightarrow L\in\{1,2\}$; 由 $x_1>1$ 得 $L=2$.

### Exercise 4.6

**题目**: 定义 $x_1=\sqrt{3}$; 对 $n\ge 2$ 定义 $x_n>0$ 且 $x_n^2=3x_{n-1}$. 证明 $\lim x_n$ 存在并求其值.

**讲解**:

对 $n\ge 2$, $x_n=\sqrt{3x_{n-1}}$. **正性**: $x_1=\sqrt{3}>0$, 归纳得 $x_n>0$.

**有上界 3**: $x_1=\sqrt{3}<3$. 若 $x_{n-1}<3$, 则 $x_n^2=3x_{n-1}<9$, 故 $x_n<3$.

**递增**: $x_2=\sqrt{3x_1}=3^{3/4}>\sqrt{3}=x_1$. 若 $x_{n-1}\le x_{n-2}$, 则 $x_n^2=3x_{n-1}\ge 3x_{n-2}=x_{n-1}^2$, 故 $x_n\ge x_{n-1}$ (皆正).

由 **MCT**, $L=\lim x_n$ 存在. 在 $x_n^2=3x_{n-1}$ 两边取极限: $L^2=3L$, 故 $L=0$ 或 $L=3$. 又 $x_n\ge x_1=\sqrt{3}>0$, 极限 $L\ge\sqrt{3}$, 故 **$L=3$**.


---


## 5. 常用极限

### 定理 5.1 (几何序列)

**假设 / 结论**:
- $0<r<1$ $\Rightarrow$ $\lim r^n=0$
- $r>1$ $\Rightarrow$ $(r^n)$ 发散

**证明**:
- (1) $x_{n+1}=rx_n<x_n$ 且有下界 $0$, MCT $\Rightarrow$ 收敛到 $L=rL\Rightarrow L=0$.
- (2) 若收敛到 $L$ 则 $L=rL\Rightarrow L=0$, 但 $r^n>1\Rightarrow L\ge 1$, 矛盾.

### 定理 5.2

**结论**: $\lim n^{1/n}=1$.

**证明**: 令 $x_n=n^{1/n}-1$ ($n>1$). 由二项展开
$$
n=(1+x_n)^n>1+\frac{n(n-1)}{2}x_n^2\Rightarrow x_n^2<\frac{2}{n}.
$$
夹逼得 $x_n\to 0$, 故 $n^{1/n}\to 1$.

### Exercise 5.3

**题目**: 求下列极限:
(1) $\lim n^{1/n^3}$;
(2) $\lim (n!)^{1/n}$;
(3) 对 $a>0$, $\lim a^{1/n}$.

**讲解**:

**(1)** $n^{1/n^3}=(n^{1/n})^{1/n^2}$. 由 Thm 5.2, $n^{1/n}\to 1$; 又 $1/n^2\to 0$, 故
$$
n^{1/n^3}\to 1^0=1.
$$
(亦可写 $n^{1/n^3}=e^{\frac{\ln n}{n^3}}\to e^0=1$.)

**(2)** 取对数: $\ln\big((n!)^{1/n}\big)=\frac{1}{n}\sum_{k=1}^n\ln k$. 因 $\ln k$ 递增,
$$
\frac{1}{n}\int_1^n\ln t\,dt\le\frac{1}{n}\sum_{k=1}^n\ln k\le\frac{1}{n}\int_2^{n+1}\ln t\,dt.
$$
而 $\frac{1}{n}\int_1^n\ln t\,dt=\frac{n\ln n-n+1}{n}=\ln n-1+\frac{1}{n}\to\infty$. 下界同样 $\to\infty$, 故 $(n!)^{1/n}\to\infty$.

**(3)** 对 $a>0$, $a^{1/n}=e^{\ln a/n}\to e^0=1$. ($a=1$ 时为常列 $1$.)

---

### 定理 5.4 (Euler 数 $e$)

**结论**: $x_n=(1+1/n)^n$ 收敛; 记极限为 $e$.

**证明思路**: 二项展开比较相邻项得 $(x_n)$ 递增; 又各项 $\le 1/2^{k-1}$ 型估计得 $x_n<3$ 有上界; MCT 得收敛.

### Exercise 5.5

**题目**: 求极限:
(1) $\big(1+\dfrac{1}{n+1}\big)^n$;
(2) $\big(1+\dfrac{1}{n}\big)^{2n}$.

**讲解**:

**(1)** 改写:
$$
\left(1+\frac{1}{n+1}\right)^n
=\left(1+\frac{1}{n+1}\right)^{n+1}\cdot\left(1+\frac{1}{n+1}\right)^{-1}.
$$
第一项 $\to e$ (Thm 5.4 型定义), 第二项 $\to 1$, 故极限为 **$e$**.

**(2)** $\big(1+\tfrac{1}{n}\big)^{2n}=\big(\big(1+\tfrac{1}{n}\big)^n\big)^2\to e^2$.

---

### Exercise 5.6

**题目**: 用三角学求 $\displaystyle\lim_{n\to\infty} n\sin\frac{1}{n}$.

**讲解**:

令 $\theta_n=1/n\to 0^+$. 则
$$
n\sin\frac{1}{n}=\frac{\sin\theta_n}{\theta_n}.
$$
由标准极限 $\lim_{\theta\to 0}\dfrac{\sin\theta}{\theta}=1$ (单位圆: 弧长与正弦线之比), 得
$$
\lim_{n\to\infty} n\sin\frac{1}{n}=1.
$$


---


## 易错点

1. $\varepsilon$-$N$: $N$ 可依赖 $\varepsilon$; 只需 $n>N$ 成立, 前有限项无关
2. 有界 $\not\Rightarrow$ 收敛; 收敛 $\Rightarrow$ 有界
3. MCT 需要 **单调 + 有界**; 极限等于 $\sup/\inf$ 也需要单调
4. 极限运算中除法需极限 **非零** 且项最终非零
5. 夹逼两端极限须相同

## 与前后章

- 前: Ch.1 确界 / 完备性 (MCT 证明用 $\sup$)
- 后: 子列, Cauchy, 级数; Bartle/Ross 对应章节可作补充例
