# Chapter 3 Limits and Continuity (Part 2): 讲义

- **来源**: `Lec/Lec09 chapter3 limits of functions part2.pdf` (14 页; Chan; Fall 2025 版式, 本学期沿用)
- **课程**: MATH2241 Introduction to Mathematical Analysis
- **前承**: `Lec08 chapter3 … part1` (聚点 / 函数极限 / 序列准则等)
- **目标**: 连续; 运算与复合; 闭区间上有界与最大最小值; Bolzano IVT; 一致连续与 Lipschitz

---

## 1. Continuous functions (连续函数)

### 1.1 Definition 1.1

设 $A\subset\mathbb{R}$, $f:A\to\mathbb{R}$, $c\in A$.

1. **$f$ 在 $c$ 连续**: $\forall\varepsilon>0$, $\exists\delta>0$, 使得凡 $x\in A$ 且 $|x-c|<\delta$, 有 $|f(x)-f(c)|<\varepsilon$.
2. 若不连续则称在 $c$ **间断**.
3. 在子集 $B\subset A$ 上连续: 在 $B$ 每一点连续.

**Remark 1.2**: 若 $c$ 是 $A$ 的聚点, 则连续 $\Leftrightarrow$ $\lim_{x\to c}f(x)$ 存在且等于 $f(c)$. 若 $c$ 是**孤立点**, 则自动连续.

#### Exercise 1.3 (孤立点)

题意: $c\in A$ 孤立 $\Rightarrow$ $f$ 在 $c$ 连续.

**思路**: 取 $\delta$ 使 $(c-\delta,c+\delta)\cap A=\{c\}$. 则 $|x-c|<\delta$ 且 $x\in A$ 只剩 $x=c$, $|f(x)-f(c)|=0<\varepsilon$.

#### Exercise 1.4–1.6 (等价刻画 / 间断)

- 连续 $\Leftrightarrow$ (序列准则) 凡 $A$ 中 $x_n\to c$ 有 $f(x_n)\to f(c)$.
- 间断 $\Leftrightarrow$ 存在序列 $x_n\to c$ 使 $f(x_n)\not\to f(c)$ (或极限不存在 / 不等于 $f(c)$).

### 1.2–1.3 例子与延拓

多项式, 有理函数 (分母非零处), 根式等可用极限运算法则证明连续. 延拓: 若 $c$ 为聚点且极限存在, 可定义 $f(c)$ 使连续 (课件 Exercise 1.11 一类填洞).

---

## 2. Construction of continuous functions

### Theorem 2.1 (代数运算)

若 $f,g$ 在 $c$ 连续, 则 $f\pm g$, $fg$, 及 $g(c)\ne0$ 时 $f/g$ 在 $c$ 连续. (由极限四则 + 连续定义.)

#### Exercise 2.2

由乘积连续推常数倍连续: 取常值函数 $g\equiv b$.

### Theorem 2.3 (复合)

$f:A\to\mathbb{R}$, $g:B\to\mathbb{R}$, $f(A)\subset B$. 若 $f$ 在 $c$ 连续且 $g$ 在 $f(c)$ 连续, 则 $g\circ f$ 在 $c$ 连续.

#### Exercise 2.4

用 $\varepsilon$-$\delta$: 先对 $g$ 在 $f(c)$ 取 $\delta_1$, 再对 $f$ 在 $c$ 取 $\delta$ 使 $|f(x)-f(c)|<\delta_1$.

---

## 3. Examples

幂函数 $x^{m/n}$ (适当定义域), $\max\{f,g\}$ / $\min\{f,g\}$ (可用 $\frac{f+g\pm|f-g|}{2}$) 等. 注意: **间断与连续复合不必连续** (Exercise 3.5).

---

## 4. Boundedness on an interval

### Theorem 4.3 (闭有界区间上连续 $\Rightarrow$ 有界)

$I=[a,b]$, $f:I\to\mathbb{R}$ 连续 $\Rightarrow$ $f$ 有界.

**证明思路**: 若无界, 造 $|f(x_n)|\ge n$; Bolzano–Weierstrass 取子列 $x_{n_k}\to c\in I$; 连续性 $\Rightarrow f(x_{n_k})\to f(c)$, 与无界矛盾.

反例说明假设必要: $(a,\infty)$, $(a,b]$, 非闭区间上可造无界连续函数; 闭但函数不连续也可无界.

---

## 5. Maximum–minimum / IVT / 保区间

### Theorem 5.4 (Extreme Value Theorem)

$I=[a,b]$, $f$ 连续 $\Rightarrow$ 达到最大值与最小值.

**思路**: 有界 $\Rightarrow$ $M=\sup f(I)$ 有限; 取 $f(x_n)\to M$, 再 BW 得极限点, 连续推出达到 $M$. 最小值同理.

### Theorem 5.6–5.7 (Bolzano intermediate value theorem)

$f$ 在区间上连续, 则像集是区间 (介值). 特别地 $[a,b]$ 上 $f(a),f(b)$ 异号 $\Rightarrow$ 存在根.

**应用**: 奇次多项式有实根; 二分法直觉 (Exercise 5.10).

### Corollary 5.11

连续函数把区间映成区间.

---

## 6. Uniform continuity (一致连续)

### 6.1 定义

$f:A\to\mathbb{R}$ **一致连续**: $\forall\varepsilon>0$, $\exists\delta>0$, 使得凡 $x,y\in A$ 且 $|x-y|<\delta$, 有 $|f(x)-f(y)|<\varepsilon$.

与点态连续的差别: $\delta$ **不依赖点**, 只依赖 $\varepsilon$.

一致连续 $\Rightarrow$ 连续 (Exercise 6.2); 反之在一般定义域上不成立 (如 $(0,1)$ 上 $1/x$).

### Theorem 6.8

闭有界区间上连续 $\Rightarrow$ 一致连续.

### Lipschitz

存在 $L$ 使 $|f(x)-f(y)|\le L|x-y|$ $\Rightarrow$ 一致连续 (取 $\delta=\varepsilon/L$).

### Cauchy / Extension

一致连续把 Cauchy 序列映成 Cauchy 序列; 开区间上连续且可一致连续延拓到端点等 (Theorem 6.18–6.20) — 细节对照 PDF 例题.

---

## 7. 与 todo / 考试

- Part1 (Lec08) 偏极限; **Part2 本讲** 偏连续与一致连续, 常进 Test2 / Final 范围 (以教师公布为准).
- Exercises 1.3–6.23 建议挑证: 孤立点, 序列准则, EVT, EVT 应用, 非一致连续判据.

---

## 8. 参考

- 同目录 Part1 讲义; Bartle 相应连续章节 (可选)
