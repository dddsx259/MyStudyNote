# Assignment 3 — 解答 ([0,1] 有限开覆盖与有理 Cauchy)

- **来源**: `assignment/Assignment03.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis, Fall 2026
- **说明**: 按题、按小问分开的完整解答. 交稿前自行核对.

---

## 1. $[0,1]$ 的有限子覆盖

设 $(x_n)_{n\ge 1}$ 为 $[0,1]$ 中的序列, 且对每个 $n\in\mathbb{N}$ 有 $\varepsilon_n>0$, 使得
$$
[0,1]\subset\bigcup_{n=1}^\infty (x_n-\varepsilon_n,x_n+\varepsilon_n).
$$
记 $U_n:=(x_n-\varepsilon_n,x_n+\varepsilon_n)$. 目标: 存在有限指标使 $[0,1]\subset\bigcup_{i=1}^k U_{n_i}$.

### (a) 反证假设

假设结论不成立: **不存在**有限族 $\{U_{n_1},\ldots,U_{n_k}\}$ 覆盖 $[0,1]$. 换言之, 对任意有限指标集 $F\subset\mathbb{N}$,
$$
[0,1]\not\subset\bigcup_{n\in F} U_n.
$$

### (a)(i) 嵌套闭区间构造

我们归纳构造闭区间 $I_j=[a_j,b_j]\subseteq[0,1]$ 满足:

1. $I_{j+1}\subseteq I_j$ (嵌套);
2. $|I_j|=b_j-a_j=2^{1-j}$;
3. $I_j$ 不能被有限多个 $U_n$ 覆盖.

**$j=1$**: 取 $I_1=[0,1]$. 则 $|I_1|=1=2^{0}$. 由反证假设, $I_1$ 无有限子覆盖.

**归纳步**: 设已得 $I_j=[a_j,b_j]$ 满足上述三条. 令中点
$$
m_j:=\frac{a_j+b_j}{2}.
$$
考虑左半区间 $L=[a_j,m_j]$ 与右半区间 $R=[m_j,b_j]$. 断言: $L$ 与 $R$ 中至少有一个不能被有限多个 $U_n$ 覆盖.

否则, 存在有限指标集 $F_L,F_R$ 使
$$
L\subset\bigcup_{n\in F_L} U_n,\qquad R\subset\bigcup_{n\in F_R} U_n.
$$
于是
$$
I_j=L\cup R\subset\bigcup_{n\in F_L\cup F_R} U_n,
$$
与 $I_j$ 无有限子覆盖矛盾.

选取无有限子覆盖的那一半为 $I_{j+1}$ (若两者皆无, 任取其一). 则 $|I_{j+1}|=|I_j|/2=2^{-j}=2^{1-(j+1)}$, 且 $I_{j+1}\subseteq I_j$.

由归纳, 得到满足要求的嵌套列 $(I_j)$.

### (a)(ii) $(y_j)$ 收敛

对每个 $j\in\mathbb{N}$, 任取 $y_j\in I_j$ (例如取 $y_j=a_j$).

**断言**: $(y_j)$ 为 Cauchy 列.

设 $\varepsilon>0$. 取 $N\in\mathbb{N}$ 使 $|I_N|<\varepsilon$, 即 $2^{1-N}<\varepsilon$. 若 $j,k\ge N$, 则由嵌套性 $y_j\in I_j\subseteq I_N$, $y_k\in I_k\subseteq I_N$, 故
$$
|y_j-y_k|\le |I_N|=2^{1-N}<\varepsilon.
$$
因此 $(y_j)$ 为 Cauchy. 由 $\mathbb{R}$ 完备性 (Cauchy $\Leftrightarrow$ 收敛), 存在 $c\in\mathbb{R}$ 使 $y_j\to c$.

又每个 $y_j\in[0,1]$, 闭区间 $[0,1]$ 对极限封闭, 故 $c\in[0,1]$. (亦可用 Nested Interval Property: $\bigcap_j I_j=\{c\}$, 且 $y_j\to c$.)

### (a)(iii) 某一 $I_N$ 落入单个开区间

因 $c\in[0,1]\subset\bigcup_n U_n$, 存在 $m\in\mathbb{N}$ 使 $c\in U_m=(x_m-\varepsilon_m,x_m+\varepsilon_m)$. 该开区间含 $c$, 故存在 $\delta>0$ 使
$$
(c-\delta,c+\delta)\subset U_m.
$$
因 $y_j\to c$ 且 $|I_j|\to 0$, 取 $N$ 充分大使得
$$
|I_N|<\delta\qquad\text{且}\qquad |y_N-c|<\delta-|I_N|
$$
(或更简单: 取 $N$ 使 $|I_N|<\delta$ 且 $c\in I_N$; 后者因 $c\in\bigcap I_j$). 则对任意 $y\in I_N$,
$$
|y-c|\le |I_N|<\delta,
$$
故 $I_N\subset(c-\delta,c+\delta)\subset U_m$. 即
$$
I_N\subset(x_m-\varepsilon_m,x_m+\varepsilon_m).
$$

### (b) 矛盾与结论

由 (a)(iii), $I_N$ 被**单个**开区间 $U_m$ 覆盖, 从而被有限多个 $U_n$ 覆盖. 这与 (a)(i) 中「$I_N$ 无有限子覆盖」矛盾.

因此反证假设不成立. 故存在有限指标 $n_1,\ldots,n_k$ 使
$$
[0,1]\subset\bigcup_{i=1}^k (x_{n_i}-\varepsilon_{n_i},x_{n_i}+\varepsilon_{n_i}).
$$

---

## 2. 有理 Cauchy 列未必收敛到有理数

**命题 (待判)**: 每个有理数 Cauchy 序列都收敛到一个有理数.

**判定**: 命题**假**.

**反例**: 令 $(q_n)_{n\ge 1}\subset\mathbb{Q}$ 为 $\sqrt{2}$ 的十进截断:
$$
q_1=1,\quad q_2=1.4,\quad q_3=1.41,\quad q_4=1.414,\quad \ldots
$$
更精确地, 取
$$
q_n=\frac{\lfloor 10^n\sqrt{2}\rfloor}{10^n}\in\mathbb{Q}.
$$
则 $0\le\sqrt{2}-q_n<10^{-n}$, 故 $q_n\to\sqrt{2}$ 在 $\mathbb{R}$ 中. 特别地 $(q_n)$ 为 Cauchy (收敛列必为 Cauchy).

若命题真, 则应存在 $q\in\mathbb{Q}$ 使 $q_n\to q$. 由极限唯一性得 $q=\sqrt{2}$. 但 $\sqrt{2}\notin\mathbb{Q}$ (标准既约分数论证: 若 $\sqrt{2}=p/q$ 既约则 $p,q$ 皆偶, 矛盾). 矛盾.

故存在有理 Cauchy 列不收敛到任何有理数 (其在 $\mathbb{R}$ 中的极限无理).

**结论**: 命题不成立; $\mathbb{Q}$ 对 Cauchy 序列不完备.

**注**: 亦可取牛顿迭代 $q_1=1$, $q_{n+1}=(q_n+2/q_n)/2$; 则 $q_n\in\mathbb{Q}$, 单调有界且 $q_n\to\sqrt{2}$.
