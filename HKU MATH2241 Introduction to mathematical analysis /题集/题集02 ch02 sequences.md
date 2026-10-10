# 题集 — Chapter 2 Sequences

> 对齐: `Lec/Lec05 chapter2 sequences part1 讲义.md`, `Lec/Lec06 chapter2 sequences part2 讲义.md`, `Lec/Lec07 chapter2 sequences part3 讲义.md`.
> 含: (1) 练习题 (A2 / A3 / 讲义) (2) 课件证明.

## 课件证明

### P1. 定理 1.6 (极限唯一性, Uniqueness of limit)

- **陈述**: **假设** $(x_n)$ 收敛; **结论** 极限唯一.
- **证明**:
  1. 设 $x_n\to x'$ 且 $x_n\to x''$. 若 $x'\neq x''$, 取 $\varepsilon=|x'-x''|/2>0$.
  2. 存在 $N$ 使 $n>N$ 时 $|x_n-x'|<\varepsilon$ 且 $|x_n-x''|<\varepsilon$.
  3. 三角不等式: $|x'-x''|\le|x'-x_n|+|x_n-x''|<2\varepsilon=|x'-x''|$, 矛盾. 故极限唯一.
- **来源**: `Lec/Lec05 chapter2 sequences part1 讲义.md` §1

### P2. 定理 2.2 (收敛 $\Rightarrow$ 有界)

- **陈述**: **假设** $(x_n)\to x$; **结论** $(x_n)$ 有界.
- **证明**:
  1. 取 $\varepsilon=1$, 存在 $N$ 使 $n>N$ 时 $|x_n-x|<1$, 即 $x-1<x_n<x+1$.
  2. 令 $M=\max\{|x_1|,\ldots,|x_N|,|x|+1\}$. 则对一切 $n$, $|x_n|\le M$.
- **来源**: 同上 §2

### P3. 定理 3.6 (夹逼, Squeeze theorem)

- **陈述**: **假设** $x_n\le y_n\le z_n$, $\lim x_n=\lim z_n=w$; **结论** $\lim y_n=w$.
- **证明**:
  1. 固定 $\varepsilon>0$. 存在 $N$ 使 $n>N$ 时 $|x_n-w|<\varepsilon$ 且 $|z_n-w|<\varepsilon$.
  2. 于是 $w-\varepsilon<x_n\le y_n\le z_n<w+\varepsilon$, 故 $|y_n-w|<\varepsilon$.
- **来源**: 同上 §3

### P4. 定理 4.3 (单调收敛定理, MCT)

- **陈述**: **假设** $(x_n)$ 单调; **结论** $(x_n)$ 收敛 $\iff$ 有界.
- **证明**:
  1. (递增有界 $\Rightarrow$ 收敛) 令 $s=\sup\{x_n\}$. 对 $\varepsilon>0$, 存在 $N$ 使 $x_N>s-\varepsilon$. 因递增, $n>N$ 时 $s-\varepsilon<x_n\le s$, 故 $|x_n-s|<\varepsilon$.
  2. (递减有界) 对偶论证, 极限为 $\inf\{x_n\}$.
  3. (收敛 $\Rightarrow$ 有界) 由 Thm 2.2.
- **来源**: 同上 §4

### P5. 定理 5.1 (几何序列 $r^n$)

- **陈述**: **结论** $0<r<1\Rightarrow r^n\to0$; $r>1\Rightarrow r^n$ 发散.
- **证明**:
  1. 若 $0<r<1$: $(r^n)$ 递减且下有界 $0$, 由 MCT 收敛到某 $L\ge 0$. 则 $L=\lim r^{n+1}=rL$, 故 $L(1-r)=0\Rightarrow L=0$.
  2. 若 $r>1$: 若 $r^n\to L$, 则同样 $L=rL\Rightarrow L=0$. 但 $r^n\ge r>1$, 不可能趋于 $0$. 故发散.
- **来源**: 同上 §5

### P6. 定理 5.2 ($n^{1/n}\to1$)

- **陈述**: **结论** $\lim_{n\to\infty} n^{1/n}=1$.
- **证明**:
  1. 令 $x_n=n^{1/n}-1\ge 0$ ($n\ge 1$). 目标证 $x_n\to 0$.
  2. 二项式: $(1+x_n)^n=n\ge \binom{n}{2}x_n^2=\frac{n(n-1)}{2}x_n^2$ (对 $n\ge 2$).
  3. 故 $x_n^2\le\frac{2}{n-1}\to 0$, 从而 $x_n\to 0$, 即 $n^{1/n}\to 1$.
- **来源**: 同上 §5

### P7. 定理 1.6 Part2 (子列同极限)

- **陈述**: **假设** $x_n\to x$; **结论** 任意子列 $(x_{n_k})\to x$.
- **证明**:
  1. 固定 $\varepsilon>0$, 取 $N$ 使 $n>N$ 时 $|x_n-x|<\varepsilon$.
  2. 因 $n_k\ge k$, 当 $k>N$ 时 $n_k>N$, 故 $|x_{n_k}-x|<\varepsilon$.
- **来源**: `Lec/Lec06 chapter2 sequences part2 讲义.md` §1

### P8. 命题 1.10 (两子列不同极限 $\Rightarrow$ 发散)

- **陈述**: **假设** 两子列极限 $L_1\neq L_2$; **结论** $(x_n)$ 发散.
- **证明**:
  1. 反证: 设 $x_n\to x$.
  2. 由 P7, 两子列皆应趋于 $x$, 故 $L_1=L_2=x$, 矛盾.
- **来源**: 同上 §1

### P9. 定理 2.1 (单调子列定理)

- **陈述**: **结论** 任意实数列有单调子列.
- **证明**:
  1. 称 $n$ 为峰, 若对一切 $m>n$ 有 $x_n\ge x_m$.
  2. 若有无穷多峰 $n_1<n_2<\cdots$, 则 $(x_{n_k})$ 递减.
  3. 若只有有限多峰, 取过最后一峰后的指标 $m_1$; 再归纳取 $m_{k+1}>m_k$ 使 $x_{m_{k+1}}>x_{m_k}$ (因 $m_k$ 非峰), 得严格递增子列.
- **来源**: 同上 §2

### P10. 定理 2.4 (Bolzano–Weierstrass)

- **陈述**: **假设** $(x_n)$ 有界; **结论** 存在收敛子列.
- **证明**:
  1. 由 Thm 2.1, 存在单调子列 $(x_{n_k})$.
  2. 该子列仍有界, 由 MCT 收敛.
- **来源**: 同上 §2

### P11. 定理 3.4 (收敛 $\Rightarrow$ Cauchy)

- **陈述**: **假设** $x_n\to x$; **结论** $(x_n)$ 为 Cauchy 列.
- **证明**:
  1. 固定 $\varepsilon>0$, 取 $N$ 使 $n>N$ 时 $|x_n-x|<\varepsilon/2$.
  2. 若 $n,m>N$, 则 $|x_n-x_m|\le|x_n-x|+|x-x_m|<\varepsilon$.
- **来源**: 同上 §3

### P12. 引理 3.5 (Cauchy $\Rightarrow$ 有界)

- **陈述**: **假设** $(x_n)$ Cauchy; **结论** $(x_n)$ 有界.
- **证明**:
  1. 取 $\varepsilon=1$, 存在 $N$ 使 $n,m>N$ 时 $|x_n-x_m|<1$. 特取 $m=N+1$: $n>N$ 时 $|x_n-x_{N+1}|<1$.
  2. 令 $M=\max\{|x_1|,\ldots,|x_N|,|x_{N+1}|+1\}$. 则对一切 $n$, $|x_n|\le M$.
- **来源**: 同上 §3

### P13. 定理 3.6 (Cauchy $\Rightarrow$ 收敛, 完备性)

- **陈述**: **假设** $(x_n)$ Cauchy in $\mathbb{R}$; **结论** $(x_n)$ 收敛.
- **证明**:
  1. 由 Lem 3.5, $(x_n)$ 有界; 由 BW 存在收敛子列 $x_{n_k}\to x^*$.
  2. 固定 $\varepsilon>0$. 取 $N$ 使 $n,m>N$ 时 $|x_n-x_m|<\varepsilon/2$, 且取 $k$ 使 $n_k>N$ 且 $|x_{n_k}-x^*|<\varepsilon/2$.
  3. 对 $n>N$: $|x_n-x^*|\le|x_n-x_{n_k}|+|x_{n_k}-x^*|<\varepsilon$. 故 $x_n\to x^*$.
- **来源**: 同上 §3

### P14. 定理 3.1 (极限代数, 概要)

- **陈述**: **假设** $\lim x_n=x$, $\lim y_n=y$; **结论** 和/差/积/常数倍极限为相应代数组合; 若 $x\ne0$ 则 $1/x_n\to1/x$.
- **证明**:
  1. (和) 用 $\varepsilon/2$ 拆分 $| (x_n+y_n)-(x+y) |$.
  2. (积) 先由收敛得 $(x_n)$ 有界 $|x_n|\le M$; 再估 $|x_ny_n-xy|\le M|y_n-y|+|y||x_n-x|$.
  3. (倒数) 因 $x\neq 0$, 尾段有 $|x_n|\ge|x|/2$, 故 $\bigl|\frac{1}{x_n}-\frac{1}{x}\bigr|=\frac{|x_n-x|}{|x_n||x|}\le\frac{2}{|x|^2}|x_n-x|$.
- **来源**: `Lec/Lec05 chapter2 sequences part1 讲义.md` §3

### P15. 定理 5.4 ($e$ 存在)

- **陈述**: **结论** $x_n=(1+1/n)^n$ 收敛 (记极限为 $e$).
- **证明**:
  1. 二项式:
     $$
     x_n=\sum_{k=0}^n\binom{n}{k}n^{-k}=2+\sum_{k=2}^n\frac{1}{k!}\prod_{j=1}^{k-1}\Bigl(1-\frac{j}{n}\Bigr)
     $$
     (约定 $k=0,1$ 两项分别为 $1$ 与 $1$). 同理
     $$
     x_{n+1}=2+\sum_{k=2}^{n+1}\frac{1}{k!}\prod_{j=1}^{k-1}\Bigl(1-\frac{j}{n+1}\Bigr).
     $$
  2. (递增) 对每个固定的 $2\le k\le n$ 及 $1\le j\le k-1$, 有 $1-j/(n+1)>1-j/n$, 故 $x_{n+1}$ 中对应 $k$ 的项严格大于 $x_n$ 中的项; 又 $x_{n+1}$ 多一项 $k=n+1$ 且为正. 因此 $x_{n+1}>x_n$.
  3. (上界) $0<1-j/n\le 1$, 故
     $$
     0<\frac{1}{k!}\prod_{j=1}^{k-1}\Bigl(1-\frac{j}{n}\Bigr)\le\frac{1}{k!}\le\frac{1}{2^{k-1}}\quad(k\ge 2).
     $$
     (因 $k!=2\cdot 3\cdots k\ge 2^{k-1}$.) 于是
     $$
     x_n\le 2+\sum_{k=2}^n\frac{1}{2^{k-1}}=2+\sum_{m=1}^{n-1}\frac{1}{2^m}<2+1=3.
     $$
  4. 由 MCT, 递增且有上界 $\Rightarrow$ $(x_n)$ 收敛. 记极限为 $e$.
- **来源**: `Lec/Lec05 chapter2 sequences part1 讲义.md` §5 (讲义为思路; 上为二项展开的完整写法)

### P16. 定理 2.1 Part3 (n-th 项检验)

- **陈述**: **假设** $\sum x_n$ 收敛; **结论** $x_n\to 0$.
- **证明**:
  1. 令 $s_n=\sum_{k=1}^n x_k\to s$, 并约定 $s_0=0$.
  2. 则 $x_n=s_n-s_{n-1}\to s-s=0$.
- **来源**: `Lec/Lec07 chapter2 sequences part3 讲义.md` §2

### P17. 定理 2.5 (非负项 $\Leftrightarrow$ 部分和有界)

- **陈述**: **假设** $x_n\ge 0$; **结论** $\sum x_n$ 收敛 $\Leftrightarrow$ $(s_n)$ 有界.
- **证明**:
  1. 因 $x_n\ge 0$, $(s_n)$ 递增.
  2. 由 MCT: $(s_n)$ 收敛 $\Leftrightarrow$ $(s_n)$ 有界. 而级数收敛即 $(s_n)$ 收敛.
- **来源**: 同上 §2

### P18. 定理 2.8 (比较检验)

- **陈述**: **假设** $0\le x_n\le y_n$; **结论** $\sum y$ 敛 $\Rightarrow$ $\sum x$ 敛; $\sum x$ 散 $\Rightarrow$ $\sum y$ 散.
- **证明**:
  1. 若 $\sum y_n$ 收敛, 则其部分和有界. 因 $0\le\sum_{k=1}^n x_k\le\sum_{k=1}^n y_k$, $(x$ 的部分和) 亦有界, 由 Thm 2.5 得 $\sum x_n$ 收敛.
  2. 第二断言是第一断言的逆否.
- **来源**: 同上 §2

### P19. 定理 2.11 (极限比较)

- **陈述**: **假设** $x_n,y_n>0$, $r=\lim x_n/y_n$; **结论** 见讲义 (a)(b).
- **证明**:
  1. 若 $r\in(0,\infty)$: 终有 $\frac{r}{2}y_n\le x_n\le 2r\,y_n$ (适当常数), 再由比较检验两者同敛散.
  2. 若 $r=0$ 且 $\sum y_n$ 收敛: 终有 $x_n\le y_n$, 故 $\sum x_n$ 收敛.
- **来源**: 同上 §2

### P20. 定理 3.3 (绝对 $\Rightarrow$ 收敛)

- **陈述**: **假设** $\sum |x_k|$ 收敛; **结论** $\sum x_k$ 收敛.
- **证明**:
  1. 注意 $0\le x_k+|x_k|\le 2|x_k|$, 故 $\sum(x_k+|x_k|)$ 收敛 (比较检验).
  2. 写 $x_k=(x_k+|x_k|)-|x_k|$, 两收敛级数之差仍收敛.
- **来源**: 同上 §3

### P21. 定理 3.7 (重排定理)

- **陈述**: **假设** 绝对收敛且和 $L$; **结论** 任意重排仍和为 $L$.
- **证明**:
  1. 绝对收敛 $\Rightarrow$ 尾部 $\sum_{k>m}|x_k|$ 可任意小.
  2. 对重排部分和 $t_n$, 取 $m$ 使原尾小, 再取 $N$ 使 $\{1,\ldots,m\}$ 的项都已出现在 $t_N$ 中.
  3. 对 $n>N$, $|t_n-L|$ 被原尾部控制, 故 $t_n\to L$.
- **来源**: 同上 §3

### P22. 定理 3.13 (交错级数判别)

- **陈述**: **假设** $x_n>0$ 递减 $\to 0$; **结论** $\sum (-1)^{n+1}x_n$ 收敛.
- **证明**:
  1. 偶部分和: $s_{2k}=(x_1-x_2)+\cdots+(x_{2k-1}-x_{2k})$ 递增 (因递减), 且 $s_{2k}\le x_1$, 故由 MCT 收敛到某 $s$.
  2. 奇部分和: $s_{2k+1}=s_{2k}+x_{2k+1}\to s+0=s$ (因 $x_n\to 0$).
  3. 故全体部分和 $\to s$.
- **来源**: 同上 §3

### P23. 定理 3.16–3.17 (Root / Ratio)

- **陈述**: **结论** $r<1$ 绝对收敛; $r>1$ 发散; $r=1$ 无效.
- **证明**:
  1. (Root, $r<1$) 取 $r_0\in(r,1)$. 终有 $\sqrt[n]{|x_n|}<r_0$, 即 $|x_n|<r_0^n$. 与几何级数比较得绝对收敛.
  2. (Root, $r>1$) 终有 $\sqrt[n]{|x_n|}>1$, 故 $|x_n|>1$, 从而 $x_n\not\to 0$, 级数发散.
  3. (Ratio) 类似: $r<1$ 时终有 $|x_{n+1}|\le r_0|x_n|$ 并与几何比较; $r>1$ 时 $|x_n|$ 最终递增故不趋于 $0$.
  4. $r=1$ 时调和级数与 $1/n^2$ 说明检验无效.
- **来源**: 同上 §4

## 练习题

### 1. 连分数子列收敛

- **题目**: $(a_n)\in\mathbb{N}$, $x_n=[a_1;\ldots,a_n]$. 证 $(x_{2n})$, $(x_{2n-1})$ 收敛.
- **思路**: $p_n,q_n$ 递推; 差 $x_n-x_{n-1}=(-1)^{n-1}/(q_n q_{n-1})$; 有界; MCT.
- **来源**: A2 Q1(a) / `assignment/Assignment02 解答.md`

### 2. 全 1 连分数与 $\varphi$

- **题目**: $a_n\equiv1$. $(x_n)$ 是否收敛? 极限?
- **思路**: $x_n=F_{n+1}/F_n\to(1+\sqrt5)/2$; 奇偶子列同极限.
- **来源**: A2 Q1(b)

### 3. 聚点 $\Leftrightarrow$ $1/n$ 邻域

- **题目**: $x$ 为 $A$ 聚点 $\Leftrightarrow$ $\exists(x_n)\subset A$, $|x_n-x|<1/n$.
- **思路**: 对角子列 / 直接 $1/n\to0$.
- **来源**: A2 Q2(a)

### 4. $\max M$ 存在

- **题目**: $A$ 非空有界, $M$=聚点集. 证 $\max M$ 存在.
- **思路**: $M$ 有界非空闭; $\sup M\in M$.
- **来源**: A2 Q2(b)

### 5. $\varepsilon$-$N$ 基础

- **题目**: 证 $\lim 1/n=0$, $\lim 2/(n^2+2)=0$; $(-1)^n$ 发散.
- **思路**: 取 $N>1/\varepsilon$; 振荡.
- **来源**: Lec Part1 例 1.7

### 6. 极限唯一

- **题目**: 收敛列极限唯一 (Thm 1.6).
- **思路**: 两极限差 $<2\varepsilon$ 矛盾.
- **来源**: Lec Part1 §1

### 7. 收敛 $\Rightarrow$ 有界

- **题目**: 证收敛 $\Rightarrow$ 有界; 逆不成立.
- **思路**: $\varepsilon=1$ 邻域 + 有限项; $(-1)^n$.
- **来源**: Lec Part1 §2

### 8. 极限代数与夹逼

- **题目**: 和/积/倒数极限; 夹逼; $\sqrt{n+1}-\sqrt n\to0$.
- **思路**: $\varepsilon/2$; 有界乘积; 有理化.
- **来源**: Lec Part1 §3

### 9. MCT 与反例

- **题目**: 单调有界 $\Leftrightarrow$ 收敛; 无单调反例 $x_1=3$, $x_n=2-1/n$.
- **思路**: 递增极限 $=\sup\{x_n\}$.
- **来源**: Lec Part1 §4

### 10. $x_{n+1}=1+\sqrt{x_n-1}$

- **题目**: $1<x_1<2$, 求 $\lim x_n$.
- **思路**: 单调有界; $(L-1)^2=L-1\Rightarrow L=2$.
- **来源**: Lec Part1 例 4.5

### 11. $r^n$, $n^{1/n}$, $(1+1/n)^n$

- **题目**: 证 $\lim r^n$ ($0<r<1$), $\lim n^{1/n}=1$, $(1+1/n)^n\to e$.
- **思路**: MCT; 二项估; 单调有界.
- **来源**: Lec Part1 §5

### 12. $\lim a^{1/n}=1$

- **题目**: $a>1$, 证 $\lim a^{1/n}=1$.
- **思路**: MCT; 子列 $x_{2n}^2=x_n$ 得 $x^2=x$, $x=1$.
- **来源**: Lec Part2 例 1.7

### 13. 子列逆命题与单调

- **题目**: (1.8) 子列同极限 $\not\Rightarrow$ 收敛; (1.9) 单调 + 一收敛子列 $\Rightarrow$ 全列收敛.
- **思路**: 枚举 $\mathbb{Q}\cap[0,1]$; MCT.
- **来源**: Lec Part2 §1

### 14. $\lim(-1)^n x_n$

- **题目**: $x_n\ge0$ 收敛. 何时 $(-1)^n x_n$ 收敛?
- **思路**:  iff $\lim x_n=0$.
- **来源**: Lec Part2 例 1.11

### 15. 单调子列定理

- **题目**: 证任意实列有单调子列; peak 练习 2.2, 2.3.
- **思路**: 无穷峰递减; 有限峰构造递增.
- **来源**: Lec Part2 Thm 2.1

### 16. Bolzano-Weierstrass

- **题目**: 有界列有收敛子列.
- **思路**: 单调子列 + MCT; 或嵌套区间.
- **来源**: Lec Part2 Thm 2.4

### 17. 多极限点例 2.5

- **题目**: 构造有界列, 不同子列不同极限.
- **思路**: $1,1/2,1,2/3,\ldots$ 型分块.
- **来源**: Lec Part2

### 18. Cauchy 例 3.3

- **题目**: $(1/n)$ Cauchy; $(n+(-1)^n/n)$ 非 Cauchy.
- **思路**: $N>2/\varepsilon$; $n=N+1,m=N+5$, $\varepsilon=1$.
- **来源**: Lec Part2

### 19. Cauchy $\Leftrightarrow$ 收敛

- **题目**: 在 $\mathbb{R}$ 证 Cauchy 列收敛 (Thm 3.6).
- **思路**: Cauchy $\Rightarrow$ 有界 $\Rightarrow$ BW 子列 $\Rightarrow$ 全列同极限.
- **来源**: Lec Part2 §3

### 20. 交错阶乘和

- **题目**: $y_n=\sum_{k=1}^n(-1)^{k+1}/k!$, 证 Cauchy.
- **思路**: 尾部 $\le1/2^{n-1}$.
- **来源**: Lec Part2 例 3.7

### 21. 压缩列与 Fibonacci 比

- **题目**: 压缩列 $\Rightarrow$ Cauchy; $f_n/f_{n+1}\to(\sqrt5-1)/2$.
- **思路**: 几何级数估; $x_{n+1}=1/(1+x_n)$.
- **来源**: Lec Part2 Ex 3.9–3.10 (与 A2 Q1(b) 相关)

### 22. $[0,1]$ 有限开覆盖 (A3 Q1)

- **题目**: $[0,1]\subset\bigcup(x_n-\varepsilon_n,x_n+\varepsilon_n)$ $\Rightarrow$ 存在有限子覆盖.
- **思路**: 反证 + 二分嵌套 $I_j$ + Cauchy $(y_j)\to c$ + $I_N\subset$ 某开区间.
- **来源**: A3 Q1 / `assignment/Assignment03 解答.md`

### 23. 有理 Cauchy 不必收敛到有理 (A3 Q2)

- **题目**: 证或驳: 有理 Cauchy 列极限必有理.
- **思路**: 反例 $q_n=\lfloor 10^n\sqrt{2}\rfloor/10^n\to\sqrt{2}\notin\mathbb{Q}$.
- **来源**: A3 Q2

### 24. 几何级数与调和发散

- **题目**: $\sum r^k$ ($0<r<1$) 求和; 证 $\sum 1/n$ 发散.
- **思路**: 有限几何和; 分组 $s_{2^k-1}$.
- **来源**: Lec Part3 §1

### 25. n-th test 与逆命题

- **题目**: 收敛 $\Rightarrow x_n\to 0$; 逆不成立例.
- **思路**: $s_n-s_{n-1}$; 调和级数.
- **来源**: Lec Part3 Ex 2.3–2.4

### 26. 比较 / 极限比较

- **题目**: $\sum 1/(n^2+2n)$; $\sum 1/(n^3-n^2+1)$; Ex 2.9 望远镜.
- **思路**: 与 $1/n^2$, $1/n^3$ 比较; $1/(n(n-1))$ 裂项.
- **来源**: Lec Part3 §2

### 27. 绝对 / 条件 / AST

- **题目**: Ex 3.5, 3.14; 交错调和条件收敛; Ex 3.15 重排改和.
- **思路**: 绝对用比较; AST; 奇偶部分和.
- **来源**: Lec Part3 §3

### 28. Root / Ratio

- **题目**: $\sum (-1)^n/(2^n n)$; $\sum(1+1/n)^{n^2}$.
- **思路**: Ratio $\to 1/2$; Root $\to e>1$ 发散.
- **来源**: Lec Part3 Ex 3.19

### 29. Tut2 P1 — 求极限 (裂项 / 夹逼 / 多项和)

- **题目**: (a) $\sum_{k=1}^n 1/(k(k+1))\to1$; (b) $\sqrt[n]{1-1/n}\to1$; (c) $\sum_{k=0}^n 1/(n+k)^2\to0$; (d) $\sum_{k=1}^n 1/\sqrt{n^2+k}\to1$.
- **思路**: 望远镜; 夹逼; 项数×上下界. **(d) 官方 sol 误写极限 0, 正确为 1**.
- **来源**: `tut/Tut02` (+ sol)

### 30. Tut2 P2 — $\sqrt[n]{\sum a_i^n}\to\max a_i$

- **题目**: $a_i>0$ 时证极限为最大值.
- **思路**: $A\le\sqrt[n]{\sum a_i^n}\le A\sqrt[n]{m}$.
- **来源**: Tut2

### 31. Tut2 P3 — 零序列 × 有界; $L\neq0$ 时无结论

- **题目**: (a) $a_n\to0$ + $\{b_n\}$ 有界 $\Rightarrow a_nb_n\to0$; (b) $a_n\to L\neq0$ 时无法判定 $a_nb_n$ 收敛性.
- **思路**: $|a_nb_n|\le M|a_n|$; 常数与 $(-1)^n$ 反例.
- **来源**: Tut2

### 32. Tut2 P4 — 递推 $x_{n+1}=1/(x_n+2)$

- **题目**: $x_1=\sqrt2$; 证收敛并求极限 $\sqrt2-1$.
- **思路**: 奇偶子列 + MCT; 不动点 $L=1/(L+2)$.
- **来源**: Tut2

### 33. Tut2 P5–P6 — 比值判零; $\sum p!/n!$; $(n+1)^\alpha-n^\alpha$

- **题目**: $\frac{a_n}{a_{n+1}}\to l>1\Rightarrow a_n\to0$; $\frac{n^2}{3^n}\to0$; $\sum_{p=1}^n p!/n!\to1$; $0<\alpha<1$ 时 $(n+1)^\alpha-n^\alpha\to0$.
- **思路**: 几何衰减; 主导末项; 夹逼 $n^{\alpha-1}$.
- **来源**: Tut2


### 34. Tut3 Q1–Q2 — 子列极限集; 有界+唯一子列极限 ⇒ 收敛

- **题目**: $x_n=\cos(n\pi/2)+1/n$ 的子列极限; 有界且收敛子列皆 → $L$ ⇒ 全列 → $L$.
- **思路**: 模 4 残类; 反证 + BW.
- **来源**: `tut/Tut03 sol`

### 35. Tut3 Q3–Q6 — Cauchy vs 相邻差; 级数比较/AST/Ratio·Root

- **题目**: $\sum 1/k^2$ 型步长 ⇒ Cauchy; $\sqrt n$ 反例; 比较/通项; 条件收敛与加括号; Ratio inconclusive 但 Root 收敛.
- **思路**: 望远镜上界; AST+$p$-级数; 奇偶比值.
- **来源**: Tut3

### 36. Tut4 — 比较, 求和, 交错, 凝聚

- **题目**: (1) $\sum 1/n^{1+1/n}$ 发散; (2) 极限比较 (a–d); (3) $\sum (n+1)^2/n!=5e$; (4) $\sum a_n$ 收敛 $\Rightarrow\sum\cos a_n$ 发散, 绝对收敛 $\Rightarrow\sum\sin a_n$ 绝对收敛; (5) $1/(n+\sqrt n)$ 条件收敛, $n/(n+\sqrt n)$ 发散; (6) Cauchy 凝聚 $\Leftrightarrow$, 以及 $p$-级数 $\Leftrightarrow p>1$.
- **思路**: $2^n>n\Rightarrow n^{1/n}<2$, 再与 $1/(2n)$ 比较; 极限比较夹在两个正倍数之间; $(n+1)^2=n(n-1)+3n+1$ 拆成三个指数级数; $|\sin x|\le|x|$; 通项不趋于 $0$; 凝聚用 $2^{n-1}$ 长的递减块与部分和有界.
- **来源**: `tut/Tut04.pdf`; 完整证明见 `tut/Tut04 解答.md`

### 37. Review1 / Test01 practice — 备考卷

- **题目**: Review Session 1 P1–8; Practice Test MCQ+长题 (量词/有序域/sup(cS)/级数).
- **思路**: 见 `exercise/Exercise02 review1 worksheet 题目理解` 与 `test&quiz/Test01 practice 题目理解`.
- **来源**: 2026-10-02 入库
