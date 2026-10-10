# Chapter 2: 序列 (Sequences) Part 2

- **来源**: `Lec/Lec06 chapter2 sequences part2.pdf` (7 页)
- **课程**: MATH2241, Fall 2026, K.Y. Chan
- **前置**: Part 1 ($\varepsilon$-$N$ 收敛, 有界性, 极限代数, MCT, 常用极限)
- **本章目标 (本 PDF)**: 子列 (subsequence), 单调子列定理, Bolzano-Weierstrass 定理, Cauchy 序列与完备性
- **说明**: 凡非定义公式/定理均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

---

## 本节在课程中的位置

Part 1 建立了序列极限与 MCT. Part 2 用 **子列** 分析发散/收敛, 证明 **Bolzano-Weierstrass (BW)** 定理, 并引入 **Cauchy 序列 (Cauchy sequence)** 作为「不必先知道极限」的收敛判据, 从而刻画 $\mathbb{R}$ 的完备性.

---

## 1. 子列 (Subsequences)

### 定义 1.1 (子列)

**假设**: $(x_n)$ 为 $\mathbb{R}$ 中序列.

**定义**: 若 $n_1<n_2<n_3<\cdots$ 为严格递增的自然数列, 则
$$
(x_{n_1},x_{n_2},x_{n_3},\ldots)
$$
称为 $(x_n)$ 的 **子列 (subsequence)**. 记指标集 $K=\{n_1,n_2,\ldots\}\subset\mathbb{N}$. (定义, 无需证明.)

**例 1.2**:
1. $x_n=n^2$. 取 $n_k=3k$ 得子列 $(9,36,81,144,\ldots)$, 即取指标为 $3$ 的倍数的项.
2. $x_n=(-1)^n$. 子列 $(x_{2n})=(1,1,1,\ldots)$ 为常值列.

**例 1.3**:
设
$$
x_n=
\begin{cases}
\dfrac{1}{n^2+1}, & n \text{ 为奇数}, \\[6pt]
-\dfrac{1}{n+1}, & n \text{ 为偶数}.
\end{cases}
$$
- $(x_{2k})$ 与 $(x_{2k-1})$ 为两条子列.
- $(x_{2k})\to 0$, $(x_{2k-1})\to 0$ (分别用 $\varepsilon$-$N$ 或直接观察).
- **不能** 由此断定 $(x_n)$ 收敛: 两条子列同极限只是必要条件; 还需原列整体趋于同一极限 (见 Thm 1.6 逆命题不成立).

### Exercise 1.4

**题目**: 设 $(x_n)$ 有界. 证明 $(x_n)$ 的任意子列也有界.

**讲解**:

因 $(x_n)$ 有界, 存在 $M>0$ 使 $|x_n|\le M$ 对所有 $n\in\mathbb{N}$. 设 $(x_{n_k})$ 为任意子列 ($n_1<n_2<\cdots$). 则对每个 $k$, $n_k\in\mathbb{N}$, 故 $|x_{n_k}|\le M$. 子列有界.

---

### Exercise 1.5

**题目**: 设 $(y_n)$ 为 $(x_n)$ 的子列, $(z_n)$ 为 $(y_n)$ 的子列. 用子列定义证明 $(z_n)$ 也是 $(x_n)$ 的子列.

**讲解**:

写 $y_n=x_{m_n}$, 其中 $m_1<m_2<\cdots$. 又 $z_n=y_{p_n}$, 其中 $p_1<p_2<\cdots$. 则
$$
z_n=y_{p_n}=x_{m_{p_n}}.
$$
需证 $m_{p_1}<m_{p_2}<\cdots$: 若 $i<j$, 则 $p_i<p_j$, 故 $m_{p_i}<m_{p_j}$ (因 $(m_k)$ 严格递增). 令 $n_k':=m_{p_k}$, 则 $z_k'=x_{n_k'}$ 满足定义 1.1, $(z_n)$ 为 $(x_n)$ 的子列.


---


### 定理 1.6 (收敛序列的子列同极限)

**假设**: $(x_n)$ 在 $\mathbb{R}$ 中收敛于 $x$.

**结论**: $(x_n)$ 的 **任意** 子列 $(x_{n_k})$ 亦收敛于 $x$.

**证明**: 设 $\varepsilon>0$. 因 $x_n\to x$, 存在 $N(\varepsilon)$ 使一切 $n>N(\varepsilon)$ 有 $|x_n-x|<\varepsilon$. 对任意 $k>N(\varepsilon)$, 由 $n_k\ge k$ 得 $n_k>N(\varepsilon)$, 故 $|x_{n_k}-x|<\varepsilon$. 由收敛定义, $(x_{n_k})\to x$.

**例 1.7 ($\lim a^{1/n}=1$, $a>1$)**:

设 $x_n=a^{1/n}$ ($a>1$). Part 1 曾用夹逼; 此处用 **MCT + 子列**.

1. **单调有界 $\Rightarrow$ 极限存在**: $a>1\Rightarrow x_n>1$; 又 $x_{n+1}=a^{1/(n+1)}<a^{1/n}=x_n$, 故 $(x_n)$ 递减且有下界 $1$, MCT $\Rightarrow$ 极限 $x=\lim x_n$ 存在且 $x\ge 1$.
2. **子列**: 考虑 $(x_{2n})$. 则 $x_{2n}^2=(a^{1/2n})^2=a^{1/n}=x_n$.
3. **Thm 1.6**: $\lim x_{2n}=x$ 且 $\lim x_{2n}^2=x^2$. 而 $x_{2n}^2=x_n\to x$, 故 $x^2=x$.
4. 解 $x^2=x$ 得 $x=0$ 或 $x=1$. 又 $x_n>1\Rightarrow x\ge 1$, 故 $x=1$.

### Exercise 1.8

**题目**: 定理 1.6 的逆命题是否成立?

**讲解**:

**不成立**: 所有子列同极限 $\not\Rightarrow$ 原列收敛.

**反例**: 将 $\mathbb{Q}\cap[0,1]$ 排成序列 $(q_n)$ (枚举有理数). 对任意 $r\in\mathbb{Q}\cap[0,1]$, 存在子列 $q_{n_k}=r$ 常值趋于 $r$; 不同 $r$ 给出不同子列极限. 但 $(q_n)$ **不收敛** (否则极限须在 $\mathbb{Q}\cap[0,1]$ 且等于所有子列极限, 不可能).

更简振荡例: 若要求「一切子列同极限」, 可取 $x_n=(-1)^{\lfloor\sqrt{n}\rfloor}$ 等构造; 课件标准反例即 **有理数枚举**: 每个子列极限都是某有理点, 但全列在 $\mathbb{Q}$ 中稠密振荡.

---

### Exercise 1.9

**题目**: 设 $(x_n)$ 单调. 若 $(x_n)$ 有一条收敛子列, 问: $(x_n)$ 是否必收敛?

**讲解**:

**是**, 单调序列若有一条收敛子列, 则全列收敛 (且极限等于该子列极限).

**证明**: 设 $(x_{n_k})\to L$.

- 若 $(x_n)$ **递增**: 对任意 $n$, 取 $k$ 使 $n_k\ge n$, 则 $x_n\le x_{n_k}\le L+\varepsilon$ (大 $k$). 又 $x_n\ge x_1$, 故递增有上界 $L+\varepsilon$, 由 MCT 全列收敛于 $\sup\{x_n\}$. 子列极限为 $L$, 由 Thm 1.6 全列极限亦为 $L$.
- 若 **递减**: 对偶, 用 $\inf\{x_n\}$.

若单调 **无界** (如 $x_n=n$ 递增): 任何收敛子列极限必为 $+\infty$ 意义下不可能; 实际上无界递增无有限收敛子列, 命题前件空真. 有界单调 + 收敛子列 $\Rightarrow$ 全列收敛于 $L$.


---


### 命题 1.10 (发散判别: 两子列不同极限)

**假设**: $(x_n)$ 有两条子列分别收敛于 **不同** 的极限 $L_1\neq L_2$.

**结论**: $(x_n)$ **发散 (divergent)**.

**证明**: 反证. 若 $(x_n)\to x$, 由 Thm 1.6 两子列皆应趋于 $x$, 与 $L_1\neq L_2$ 矛盾.

**例 1.11**: 设 $x_n\ge 0$ 且 $(x_n)$ 收敛. 何时 $\lim (-1)^n x_n$ 存在?

**分析**: 若 $\lim x_n=0$, 则 $(-1)^n x_n\to 0$. 若 $\lim x_n=L>0$, 则 $(-1)^n x_n$ 在 $L$ 与 $-L$ 间振荡, 子列 $(x_{2n})\to L$, $(x_{2n-1})\to -L$, 由 Prop 1.10 发散. **结论**: 极限存在 $\Leftrightarrow$ $\lim x_n=0$.

---

## 2. Bolzano-Weierstrass 定理

### 背景

两类典型发散:
1. $(n)$: **无界 (unbounded)**
2. $((-1)^n)$: **有界** 但振荡; 却有收敛子列 $((-1)^{2n})=1$ 与 $((-1)^{2n+1})=-1$

一般现象: 有界序列未必收敛, 但 **必有收敛子列** (BW 定理).

---

### 定理 2.1 (单调子列定理, Monotone Subsequence Theorem)

**假设**: $(x_n)$ 为 $\mathbb{R}$ 中序列.

**结论**: $(x_n)$ 存在 **单调 (monotone)** 子列 (递增或递减).

**证明** (标准 peak 论证; PDF 原文 Case 1 表述有误, 以下为标准证法):

**术语**: 称 $x_m$ 为 **峰 (peak)** 若 $x_m\ge x_n$ 对一切 $n\ge m$.

**Case 1: 有无穷多个峰**

设峰指标 $m_1<m_2<\cdots$ (无穷集). 则 $x_{m_1}\ge x_{m_2}\ge x_{m_3}\ge\cdots$ (因 $m_2\ge m_1+1$ 且 $x_{m_1}$ 为峰 $\Rightarrow x_{m_1}\ge x_{m_2}$; 归纳得递减). 故 $(x_{m_k})$ 为 **递减子列**.

**Case 2: 仅有有限多个峰**

设全部峰指标为 $m_1<\cdots<m_k$. 取 $s_1=m_k+1$ (最后一峰之后的首项). $s_1$ 非峰, 故存在 $s_2>s_1$ 使 $x_{s_2}>x_{s_1}$. 归纳: 若已选 $s_1<\cdots<s_j$ 且 $s_j$ 非峰, 取 $s_{j+1}>s_j$ 使 $x_{s_{j+1}}>x_{s_j}$. 有限峰保证此过程可无限进行. 得 $x_{s_1}<x_{s_2}<x_{s_3}<\cdots$, 为 **严格递增子列**.

两情形 exhaustive, 故恒有单调子列.

### Exercise 2.2

**题目**: 描述下列序列的 **峰 (peak)** 个数 (有限或无穷):
(a) $x_n=1+(-1)^n/n$;
(b) $x_n=(-1)^n(1-1/n)$.

**讲解**:

**峰的定义**: $x_m$ 为峰 $\Leftrightarrow$ 对所有 $n\ge m$, $x_m\ge x_n$.

**(a)** $x_n=1+(-1)^n/n$: 偶数项 $x_{2k}=1+1/(2k)\searrow 1$; 奇数项 $x_{2k-1}=1-1/(2k-1)\nearrow 1$. 偶数项 $x_{2k}$ 在其后 $n\ge 2k$ 中, 奇数项更小、下一偶数项 $x_{2k+2}<x_{2k}$, 故 **每个偶数指标** $2,4,6,\ldots$ 都是峰. **无穷多个峰**.

**(b)** $x_n=(-1)^n(1-1/n)$: 偶数 $n=2k$: $x_{2k}=1-1/(2k)>0$ 且随 $k$ **严格递增** $\to 1$; 奇数 $n\ge 3$: $x_n=-(1-1/n)<0$ (且 $x_1=0$).

峰要求 $x_m\ge x_n$ 对 **一切** $n\ge m$, 不只是下一项. 对任意偶数 $m=2k$, 下一偶数 $x_{2k+2}=1-1/(2k+2)>x_{2k}$, 故偶数项都不是峰. 奇数项之后必出现更大的正偶数项, 也不是峰. 故 **无峰** (0 个; 属于 Thm 2.1 Case 2: 有限峰 → 可抽严格递增子列, 如全体偶数项).

---

### Exercise 2.3

**题目**: 求下列序列的一条单调子列:
(1) $x_n=2n+(-1)^n 2n$;
(2) $x_n=\sin(n\pi/6)$.

**讲解**:

**(1)** $n$ 偶: $x_{2k}=4k$; $n$ 奇: $x_{2k-1}=0$. 取子列 $x_{2k}=4k$, **严格递增** (且无界).

**(2)** $\sin(n\pi/6)$ 周期 12, 取值在 $\{0,\pm 1/2,\pm\sqrt{3}/2,\pm 1\}$. 例如 $n\equiv 1\pmod{12}$ 时恒为 $1/2$, 得 **常值 (从而单调)** 子列 $(1/2,1/2,\ldots)$. 亦可按 Thm 2.1 的 peak 论证保证存在单调子列.


---


### 定理 2.4 (Bolzano-Weierstrass 定理)

**假设**: $(x_n)$ 为 **有界** 实数列.

**结论**: $(x_n)$ 有 **收敛子列**.

**证明** (主证: Thm 2.1 + MCT):

1. 由 Thm 2.1, 取单调子列 $(x_{n_k})$.
2. 由 Ex 1.4, 有界列的子列仍有界, 故 $(x_{n_k})$ 有界.
3. 单调 + 有界 $\Rightarrow$ MCT $\Rightarrow$ $(x_{n_k})$ 收敛.

**证明思路** (嵌套区间法, alternate proof):

**Step 1**: $(x_n)\subset[a_1,b_1]$. 二等分 $I_1=[a_1,b_1]$ 为 $I_1'$, $I_1''$, 至少一侧含无穷多项; 选该侧为 $I_2$, 长度 $|I_2|=|I_1|/2$. 归纳得闭区间套 $I_1\supset I_2\supset\cdots$, 各 $|I_k|=|I_1|/2^{k-1}\to 0$, 且各 $I_k$ 含 $(x_n)$ 无穷多项. 由 **嵌套区间定理 (Nested Interval Theorem)**, $\bigcap_{k=1}^\infty I_k=\{x\}$.

**Step 2**: 归纳选 $n_1<n_2<\cdots$ 使 $x_{n_k}\in I_k$ (每步 $I_k$ 无穷多项, 且 $I_{k+1}\subset I_k$, 可增大指标). 则 $|x_{n_k}-x|\le |I_k|\to 0$, 故 $x_{n_k}\to x$.

**注**: BW 证明的核心仍是 **找单调子列**; 嵌套区间法是等价构造.

**例 2.5**: 序列 $1,\,1/2,\,1,\,2/3,\,1/3,\,1,\,3/4,\,2/4,\,1/4,\,1,\,4/5,\,\ldots$ (每组以 $1$ 开头, 后跟分母递增的分数块). 收敛子列极限可取得: $0$ (取各块最小分数), $1$ (取常值 $1$), 以及 $1/2,2/3,3/4,\ldots\to 1$ 等. **不同子列** 可有 **不同极限**; 有界序列的极限点集可以多个 (聚点集).

---

## 3. Cauchy 序列 (Cauchy Sequences)

### 定义 3.1 (Cauchy 序列)

**定义**: $(x_n)\subset\mathbb{R}$ 称为 **Cauchy 序列** 若: 对每个 $\varepsilon>0$, 存在 $N\in\mathbb{N}$ 使一切 $n,m>N$ 有
$$
|x_n-x_m|<\varepsilon.
$$
(定义, 无需证明.)

**直观**: 充分靠后的项彼此 **任意接近**, 不必先指定极限点. 在数轴上, $x_{N+1},x_{N+2},\ldots$ 皆落在长度 $<2\varepsilon$ 的区间内.

### Exercise 3.2

**题目**: 在实数轴上标出 $\varepsilon$ 与 $x_{N+1},x_{N+2},\ldots$, 以理解 Cauchy 定义.

**讲解**:

Cauchy 要求: 给定 $\varepsilon>0$, 存在 $N$ 使 **一切** $n,m>N$ 有 $|x_n-x_m|<\varepsilon$.

几何意义: 固定 $N$ 后, 所有尾项 $x_{N+1},x_{N+2},\ldots$ 都落在 **长度至多为 $2\varepsilon$** 的区间内 — 例如以 $x_{N+1}$ 为中心、半径 $\varepsilon$ 的开区间 $(x_{N+1}-\varepsilon,x_{N+1}+\varepsilon)$ 必包含每个 $x_m$ ($m>N$), 因 $|x_m-x_{N+1}|<\varepsilon$. 在数轴上画出 $\varepsilon$, 标 $N$ 之后各点彼此相距小于 $\varepsilon$, 整体落在一小段「簇」内, 不必先知道极限点.


---


### 例 3.3

**(1) $(1/n)$ 为 Cauchy**

**证明**: 设 $\varepsilon>0$, 取 $N>2/\varepsilon$. 对 $n,m>N$,
$$
\left|\frac{1}{n}-\frac{1}{m}\right|\le\frac{1}{n}+\frac{1}{m}<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

**(2) 反例: $(n+(-1)^n/n)$ 非 Cauchy**

**证明**: 取 $\varepsilon=1$. 对任意 $N$, 令 $n=N+1$, $m=N+5$. 则
$$
\left|\left(N+5+\frac{(-1)^{N+5}}{N+5}\right)-\left(N+1+\frac{(-1)^{N+1}}{N+1}\right)\right|
\ge 4-\frac{1}{N+5}-\frac{1}{N+1}>2>\varepsilon.
$$
故不满足 Cauchy 条件.

---

### 定理 3.4 (收敛 $\Rightarrow$ Cauchy)

**假设**: $(x_n)$ 在 $\mathbb{R}$ 中收敛.

**结论**: $(x_n)$ 为 Cauchy 序列.

**证明**: 设 $x=\lim x_n$. 对 $\varepsilon>0$, 存在 $N$ 使 $n>N$ 时 $|x_n-x|<\varepsilon/2$. 则对 $n,m>N$,
$$
|x_n-x_m|\le|x_n-x|+|x-x_m|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

---

### 引理 3.5 (Cauchy $\Rightarrow$ 有界)

**假设**: $(x_n)$ 为 Cauchy 序列.

**结论**: $(x_n)$ 有界.

**证明**: 取 $\varepsilon=1$, 得 $N$ 使 $n,m>N$ 时 $|x_n-x_m|<1$. 固定 $m=N+1$, 则 $n>N$ 时 $|x_n-x_{N+1}|<1$, 即 $x_{N+1}-1<x_n<x_{N+1}+1$. 令
$$
M=\max\{|x_1|,\ldots,|x_N|,|x_{N+1}|+1\},
$$
则 $|x_n|\le M$ $\forall n$.

---

### 定理 3.6 (Cauchy $\Rightarrow$ 收敛, 完备性)

**假设**: $(x_n)$ 为 $\mathbb{R}$ 中 Cauchy 序列.

**结论**: $(x_n)$ 收敛.

**证明**:

**Step 1**: 由 Lem 3.5, $(x_n)$ 有界. 由 Thm 2.4 (BW), 存在收敛子列 $(x_{n_k})\to x^*$.

**Step 2**: 证 $(x_n)\to x^*$. 设 $\varepsilon>0$.
- Cauchy: 存在 $N$ 使 $n,m>N$ 时 $|x_n-x_m|<\varepsilon/2$.
- 子列收敛: 存在 $K$ 使 $k>K$ 时 $|x_{n_k}-x^*|<\varepsilon/2$.
- 取 $k$ 足够大使 $n_k>\max\{N,K\}$. 则对 $n>N$,
$$
|x_n-x^*|\le|x_n-x_{n_k}|+|x_{n_k}-x^*|<\frac{\varepsilon}{2}+\frac{\varepsilon}{2}=\varepsilon.
$$

**意义**: 在 $\mathbb{R}$ 上, **Cauchy $\Leftrightarrow$ 收敛**; 这等价于 $\mathbb{R}$ 的 **完备性 (completeness)**. $\mathbb{Q}$ 中有 Cauchy 不收敛列 (如 $\mathbb{Q}$ 中对 $\sqrt{2}$ 的有理逼近).

**Cauchy 准则 (Cauchy criterion)**: 定理 3.4 与定理 3.6 合在一起的说法. 设 $(x_n)$ 是实序列, 则 $(x_n)$ 收敛当且仅当 $(x_n)$ 是 Cauchy 序列. 一端是「收敛 $\Rightarrow$ Cauchy」(定理 3.4), 另一端是「Cauchy $\Rightarrow$ 收敛」(定理 3.6, 用到完备性). 2020 Test 1 第 2 题写的 "Using the Cauchy criterion" 就是要求用这两端, 而不是只验证定义.

---

### 例 3.7 (交错阶乘级数部分和)

设
$$
y_n=\sum_{k=1}^{n}\frac{(-1)^{k+1}}{k!}=1-\frac{1}{2!}+\frac{1}{3!}-\cdots+\frac{(-1)^{n+1}}{n!}.
$$
对 $m>n\ge 1$,
$$
|y_m-y_n|=\left|\sum_{k=n+1}^{m}\frac{(-1)^{k+1}}{k!}\right|
\le\sum_{k=n+1}^{m}\frac{1}{k!}
\le\sum_{k=n+1}^{m}\frac{1}{2^{k-1}}
\le\frac{1}{2^{n-1}}.
$$
因 $1/2^{n-1}\to 0$, 对给定 $\varepsilon$ 取 $N$ 足够大可使 $m,n>N$ 时 $|y_m-y_n|<\varepsilon$. 故 $(y_n)$ Cauchy, 从而收敛.

### Exercise 3.8

**题目**: 例 3.7 中交错阶乘部分和的极限, 你是否 (不必证明) 知道其值?

**讲解**:

$$
y_n=\sum_{k=1}^{n}\frac{(-1)^{k+1}}{k!}\to\sum_{k=1}^{\infty}\frac{(-1)^{k+1}}{k!}=e^{-1}=\frac{1}{e}.
$$
因 $e^x=\sum_{k=0}^{\infty}x^k/k!$, 取 $x=-1$ 得 $e^{-1}=1-1+1/2!-1/3!+\cdots$. 例 3.7 已用 Cauchy 证收敛; 极限识别为 **$1/e$**.


---


### Exercise 3.9

**题目**: $(x_n)$ 称为 **压缩列 (contractive)** 若存在 $0<C<1$ 使 $|x_{n+2}-x_{n+1}|\le C|x_{n+1}-x_n|$ 对所有 $n\in\mathbb{N}$. 证明压缩列必为 Cauchy.

**讲解**:

对 $m>n$,
$$
|x_m-x_n|\le\sum_{j=n}^{m-1}|x_{j+1}-x_j|
\le\sum_{j=n}^{m-1}C^{j-1}|x_2-x_1|
=\frac{C^{n-1}-C^{m-1}}{1-C}|x_2-x_1|
\le\frac{C^{n-1}}{1-C}|x_2-x_1|.
$$
因 $0<C<1$, $C^{n-1}\to 0$. 对 $\varepsilon>0$, 取 $N$ 使 $n>N$ 时 $\dfrac{C^{n-1}}{1-C}|x_2-x_1|<\varepsilon$. 则一切 $n,m>N$ 有 $|x_m-x_n|<\varepsilon$. 故 Cauchy.


---


### Exercise 3.10

**题目**: Fibonacci: $f_1=f_2=1$, $f_{n+2}=f_{n+1}+f_n$. 令 $x_n=f_n/f_{n+1}$. 证明 $(x_n)$ 为压缩列, 并求 $\lim x_n$.

**讲解**:

**递推**: $x_{n+1}=\dfrac{f_{n+1}}{f_{n+2}}=\dfrac{f_{n+1}}{f_{n+1}+f_n}=\dfrac{1}{1+x_n}$.

**正性与区间**: 归纳 $f_n>0$, 故 $x_n>0$; 可证 $x_n\in(0,1)$.

**压缩性**: 函数 $g(t)=1/(1+t)$ 在 $[0,1]$ 上 Lipschitz, 可证存在 $C\in(0,1)$ 使 $|x_{n+2}-x_{n+1}|\le C|x_{n+1}-x_n|$ (例如对 $|g'(t)|=1/(1+t)^2\le 1$ 用中值定理). 故 $(x_n)$ 压缩.

**极限**: Ex 3.9 $\Rightarrow$ Cauchy $\Rightarrow$ 收敛. 设 $L=\lim x_n$, 在 $x_{n+1}=1/(1+x_n)$ 中取极限: $L=1/(1+L)$, 即 $L^2+L-1=0$, $L=\dfrac{-1\pm\sqrt{5}}{2}$. 由 $x_n>0$ 取正根
$$
L=\frac{\sqrt{5}-1}{2}=\varphi^{-1}\quad\text{(黄金比倒数)}.
$$


---


## 易错点

1. **子列指标** 必须严格递增: $n_1<n_2<\cdots$, 不能随意「跳着取」
2. Thm 1.6 **不可逆**: 所有子列同极限 $\not\Rightarrow$ 原列收敛
3. Prop 1.10: 需 **两条** 子列趋于 **不同** 极限才能判发散; 两子列同极限不够
4. Thm 2.1 的 peak 论证: Case 1 是 **无穷多峰** $\Rightarrow$ 递减子列; Case 2 是 **有限峰** $\Rightarrow$ 递增子列 (勿与 PDF 误排混淆)
5. Cauchy: 须对 **所有** 充分大的 $n,m$ 同时成立, 不是只对 $m=n+1$
6. $\mathbb{R}$ 上 Cauchy $\Leftrightarrow$ 收敛; 在 $\mathbb{Q}$ 上不成立

## 与前后章

- **前**: Part 1 收敛/MCT/有界性 (Thm 2.4 证明依赖)
- **后**: 级数 (series), 函数极限; Ross/Bartle 对应 Ch.2 后半
- **核心链条**: 有界 $\xrightarrow{\text{BW}}$ 收敛子列; Cauchy $\xrightarrow{\text{Lem 3.5}}$ 有界 $\xrightarrow{\text{BW}}$ 收敛; 完备性统一三者
