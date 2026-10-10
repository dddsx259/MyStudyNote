# MATH3603 Quiz1 考前复习 (Ch1 + §2.1–2.5)

> 来源: `Lec/Lec01 probability theory lecture notes.pdf` (Bao).
> **范围**: Chapter 1 全部 (笔记 p.6–20) + Chapter 2 **§2.1–2.5** (笔记 p.21–34, 至 coupon collector).
> **不含**: §2.6 起 (随机变量独立 / 协方差 / 卷积), §2.7 MGF, §2.8 WLLN/CLT, 以及 Ch3–Ch5. 指数无记忆性在 Ch5, 不在本范围.
> 闭卷, 无 cheat sheet. 卷面可能给出部分分布定义; 下面把定义, 编号命题, 以及「用范围内定义当场可推」的矩都写全.
> 证明只保留能复现结论的步骤. 更细的讲义在 `Lec/Lec01 … Ch01 讲义.md` 与 `Lec/Lec02 … Ch02 讲义.md`.

---

# 0. 一张图: 范围内要会什么

| 块 | 必须能默写或当场推出 |
|---|---|
| 公理与推论 | 三条公理; $P(\emptyset)=0$; 有限可加; 补集; 单调; 两事件容斥; 一般容斥的形状 |
| 条件概率 | 定义; $Q(\cdot)=P(\cdot\mid B)$ 仍是概率; 乘法法则; 划分; 全概率; Bayes |
| 独立 | 乘积定义; 等价于条件概率不变; 互斥 $\neq$ 独立; 两两 vs 相互; 乘积空间; 无放回不独立 |
| RV / CDF / PMF / PDF | 定义; CDF 五条性质; 区间概率; 离散与连续的差别 |
| 离散族 | Bernoulli, Bin, Geom, NegBin, Poisson 的支撑与 PMF; 二项怎么数出来; 泊松极限的假设 |
| 连续族 | Unif / 逆变换 / Exp / Gamma / Normal 的密度 (及笔记给出的 CDF); 正态归一化与仿射 |
| 期望 | 定义; LOTUS; 矩与方差; $\mathrm{Var}=E[X^2]-(EX)^2$; $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$ |
| 随机向量 | 联合 CDF/PMF/PDF; 边缘; 边缘定不了联合; 矩形概率; 联合 LOTUS; **线性性不需独立**; coupon |

---

# 1. Chapter 1 概率基础

## 1.1 样本空间, 事件, 公理

**实验 (experiment / trial)**: 结果事先未知. **结果 (outcome)**: 一个可能结果. **样本空间 (sample space)** $S$ 或 $\Omega$: 全部结果的集合 (Def. 1.1.1).

| 实验 | $S$ |
|---|---|
| 一枚硬币 | $\{H,T\}$ |
| 两枚硬币 (有序) | $\{(H,H),(H,T),(T,H),(T,T)\}$ |
| 灯泡寿命 | $[0,\infty)$ |

**事件 (event)** (Def. 1.1.5): 本笔记中即 $S$ 的子集. 发生 $\Leftrightarrow$ $\omega\in E$.

- **简单/基本事件 (elementary / simple event)**: 单点集, 如骰子 $\{4\}$.
- **复合事件 (compound event)**: 多点集, 如偶数 $\{2,4,6\}$, 或两硬币「第一枚正面」$\{HH,HT\}$.

**集合运算**:

| 记号 | 含义 |
|---|---|
| $E\cup F$ | 至少一个发生 |
| $E\cap F$ | 同时发生 |
| $E^c=S\setminus E$ | $E$ 不发生 |
| $E\cap F=\emptyset$ | 互斥 (mutually exclusive / disjoint) |

**概率 (probability)** (Def. 1.1.8): $P:\mathcal{F}\to[0,1]$ 满足

1. **$0\le P(A)\le 1$**
2. **$P(S)=1$**
3. **可数可加 (countable additivity)**: $A_i$ 两两互斥时 **$P(\bigcup_{i=1}^\infty A_i)=\sum_{i=1}^\infty P(A_i)$**

**概率空间 (probability space)** (Def. 1.1.9): $(S,\mathcal{F},P)$. 概率作用在事件上: 写 $P(\{2\})$, 不写 $P(2)$.

### 命题 1.1.10 (公理推论)

**假设**: $P$ 满足上述公理.

**结论**:

1. **$P(\emptyset)=0$**
2. **有限可加**: **$P(\bigcup_{i=1}^n A_i)=\sum_{i=1}^n P(A_i)$**
3. **$P(A^c)=1-P(A)$**
4. **单调**: **$A\subseteq B\Rightarrow P(A)\le P(B)$**

**证明**:

1. 令 $A_i=\emptyset$. 并仍是 $\emptyset$, 可数可加给出 $P(\emptyset)=\sum_{i=1}^\infty P(\emptyset)$. 唯一可能是 $P(\emptyset)=0$ (否则右端为 $\infty$, 与 $P\le 1$ 矛盾).
2. 把第 $n+1,n+2,\ldots$ 个补成 $\emptyset$, 再用 (1) 与可数可加.
3. $A$ 与 $A^c$ 互斥且并为 $S$, 故 $P(A)+P(A^c)=1$.
4. $B=A\cup(B\setminus A)$ 且两块互斥, $B\setminus A=B\cap A^c$, 故 $P(B)=P(A)+P(B\setminus A)\ge P(A)$.

### 定理 1.1.11 (两事件容斥)

$$\boldsymbol{P(A\cup B)=P(A)+P(B)-P(A\cap B).}$$

**证明** (笔记的三块分解): 三块互斥,

$$A\cup B=(A\setminus B)\cup(A\cap B)\cup(B\setminus A),$$

且 $A=(A\setminus B)\cup(A\cap B)$, $B=(B\setminus A)\cup(A\cap B)$. 把 $P(A)+P(B)$ 相加时 $A\cap B$ 算了两次, 减一次. 若 $A\cap B=\emptyset$, 退回有限可加.

### 定理 1.1.12 (一般容斥)

$$\boldsymbol{P\Bigl(\bigcup_{i=1}^n A_i\Bigr)=\sum_i P(A_i)-\sum_{i<j}P(A_i\cap A_j)+\sum_{i<j<k}P(A_i\cap A_j\cap A_k)-\cdots+(-1)^{n+1}P(A_1\cap\cdots\cap A_n).}$$

**证明思路**: 对 $n$ 归纳. $n=2$ 即 Thm 1.1.11. 令 $B=\bigcup_{i=1}^{n-1}A_i$, 则

$$P(B\cup A_n)=P(B)+P(A_n)-P(B\cap A_n),\qquad B\cap A_n=\bigcup_{i=1}^{n-1}(A_i\cap A_n).$$

对 $P(B)$ 与 $P(B\cap A_n)$ 用归纳假设, 交叉项符号整理后即交替和.

**概率的连续性** (CDF 证明会用, 笔记未单独编号): **$A_n\uparrow A\Rightarrow P(A_n)\to P(A)$**; **$A_n\downarrow A\Rightarrow P(A_n)\to P(A)$**.

**证明思路**: 递增时令 $B_1=A_1$, $B_k=A_k\setminus A_{k-1}$ ($k\ge 2$). $B_k$ 互斥且并为 $A$, 可数可加得 $P(A)=\sum P(B_k)=\lim P(A_n)$. 递减时对补集用递增情形.

---

## 1.2 条件概率

已知 $B$ 发生, 样本空间缩成 $B$; 在 $B$ 里 $A$ 发生的部分是 $A\cap B$.

**定义 1.2.1**: $P(B)>0$ 时

$$\boldsymbol{P(A\mid B)=\frac{P(A\cap B)}{P(B)}.}$$

### 命题 1.2.2

**假设**: $P(B)>0$. **结论**: **$Q_B(A):=P(A\mid B)$ 本身是概率**.

**证明**: $0\le P(A\cap B)\le P(B)$ 故 $0\le Q_B(A)\le 1$. $Q_B(S)=P(B)/P(B)=1$. 若 $A_i$ 互斥, 则 $A_i\cap B$ 也互斥, 且 $(\bigcup A_i)\cap B=\bigcup(A_i\cap B)$, 可数可加后除以 $P(B)$ 即得 $Q_B$ 可数可加.

### 乘法法则 (multiplication rule)

**$P(B)>0$ 时 $P(A\cap B)=P(A\mid B)P(B)$**. **$P(A)>0$ 时 $P(A\cap B)=P(B\mid A)P(A)$**.

**三事件链式** (笔记未编号, 反复用两事件乘法): 若中间条件概率有定义,

$$\boldsymbol{P(A\cap B\cap C)=P(A)\,P(B\mid A)\,P(C\mid A\cap B).}$$

### 定义 1.2.3 (划分 partition)

**$F_1,\ldots,F_n$ 两两互斥且 $\bigcup_{i=1}^n F_i=S$**.

### 定理 1.2.4 (全概率公式 law of total probability)

**假设**: $\{F_j\}$ 是 $S$ 的划分, 且每个 $P(F_j)>0$.

**结论**: 对任意事件 $E$,

$$\boldsymbol{P(E)=\sum_{j=1}^n P(F_j)\,P(E\mid F_j).}$$

**证明**: $E=\bigcup_j(E\cap F_j)$ 且这些交互斥, 故 $P(E)=\sum P(E\cap F_j)$, 再对每项用乘法法则.

### 定理 1.2.5 (贝叶斯定理 Bayes' theorem)

**假设**: $\{F_j\}$ 为划分, $P(F_j)>0$, 且 $P(E)>0$.

**结论**:

$$\boldsymbol{P(F_i\mid E)=\frac{P(F_i)\,P(E\mid F_i)}{\sum_{j=1}^n P(F_j)\,P(E\mid F_j)}.}$$

**证明**: $P(F_i\mid E)=P(F_i\cap E)/P(E)=P(F_i)P(E\mid F_i)/P(E)$, 分母用全概率.

用语: $P(F_j)$ 是先验 (prior), $P(E\mid F_j)$ 是似然 (likelihood), $P(F_i\mid E)$ 是后验 (posterior). Bayes 解决的是「已知先验和似然, 求反过来的条件概率」.

### 例 1.2.6 (两孩)

有序等可能 $S=\{(B,B),(B,G),(G,B),(G,G)\}$. $E=\{(B,B)\}$, $F=$ 至少一男孩. $E\subseteq F$, 故

$$\boldsymbol{P(E\mid F)=\frac{1/4}{3/4}=\frac13.}$$

必须用**有序**样本空间. 若把 $\{BG,GB\}$ 合成一个结果, 会得到错误的 $1/2$.

### 例 1.2.7 (两瓮)

瓮 1: 2 白 7 黑. 瓮 2: 5 白 6 黑. 公平硬币: $H$ 从瓮 1 抽, $T$ 从瓮 2 抽. 求抽到白球时硬币为 $H$ 的概率.

$$P(W\mid H)=\frac29,\qquad P(W\mid T)=\frac{5}{11},\qquad P(H)=P(T)=\frac12.$$

$$P(H\mid W)=\frac{\frac12\cdot\frac29}{\frac12\cdot\frac29+\frac12\cdot\frac{5}{11}}=\frac{2/9}{2/9+5/11}=\frac{2/9}{67/99}=\frac{22}{67}.$$

四个结果 $(H,W),(H,B),(T,W),(T,B)$ **不等可能**:

$$P(H,W)=\frac19,\; P(H,B)=\frac{7}{18},\; P(T,W)=\frac{5}{22},\; P(T,B)=\frac{3}{11}.$$

### 信息不一定增大概率

- 例 1.2.8: 选择题正确答案是 $a$, 均匀猜则 $P(\mathrm{correct})=1/4$. 得知答案在 $\{b,c,d\}$ 后, $P(\{a\}\mid\{b,c,d\})=0$.
- 例 1.2.9: 两枚公平硬币, $E=$ 第一枚正面, $F=$ 第二枚反面. $P(E\mid F)=P(E)=1/2$. 这就是下一节的独立.

---

## 1.3 独立性

**定义 1.3.1**: $A,B$ 独立 (independent), 记 $A\perp\!\!\!\perp B$, 若

$$\boldsymbol{P(A\cap B)=P(A)P(B).}$$

否则相依 (dependent).

### 命题 1.3.2

**假设**: $P(B)>0$. **结论**: **独立 $\Leftrightarrow$ $P(A\mid B)=P(A)$**. 若 $P(A)>0$, **也等价于 $P(B\mid A)=P(B)$**.

**证明**: $P(A\mid B)=P(A\cap B)/P(B)$, 故等于 $P(A)$ 当且仅当交集等于乘积.

**两个误解**:

1. 独立 $\neq$ 互斥. 若互斥且 $P(A),P(B)>0$, 则 $P(A\cap B)=0\neq P(A)P(B)$, 所以**不独立**. 只有某一方概率为 0 时, 互斥与独立可以同时成立.
2. 不能凭「看起来无关系」判断. 只认乘积等式.

**定义 1.3.3 (相互独立 mutual / joint independence)**: 对每个 $|J|\ge 2$ 的子集 $J\subseteq\{1,\ldots,n\}$,

$$\boldsymbol{P\Bigl(\bigcap_{j\in J}A_j\Bigr)=\prod_{j\in J}P(A_j).}$$

只检查两两, 叫做**两两独立 (pairwise independence)**, 比相互独立弱. **相互独立 $\Rightarrow$ 两两独立; 反之不对**.

**例 1.3.4** (两两独立但不相互独立): 两枚公平骰.

- $A=$ 点数和为 7, $B=$ 第一枚是 4, $C=$ 第二枚是 3.
- 各概率 $1/6$. 任意两事件的交都是单点 $\{(4,3)\}$, 概率 $1/36=(1/6)(1/6)$.
- 但 $P(A\cap B\cap C)=1/36\neq 1/216=P(A)P(B)P(C)$.

**例 1.3.5**: 和为 6 与「第一枚是 4」**不**独立.

$|A_6|=5$, $|B|=6$, $|A_6\cap B|=1$ (只有 $(4,2)$).

$$P(A_6\cap B)=\frac{1}{36},\qquad P(A_6)P(B)=\frac{5}{36}\cdot\frac16=\frac{5}{216}.$$

**例 1.3.6**: 和为 7 与「第一枚是 4」**独立**.

$|A_7|=6$, 交为 $\{(4,3)\}$, $1/36=(1/6)(1/6)$. 和为 7 时, 第一枚取 1 到 6 各恰一对, 所以与第一枚的面独立; 和为 6 时不是.

### 乘积概率空间 (product probability space)

两个独立实验 $(S_1,P_1)$, $(S_2,P_2)$, 合并样本空间 $S=S_1\times S_2$. 矩形事件

$$\boldsymbol{P(E_1\times E_2)=P_1(E_1)P_2(E_2).}$$

**例 1.3.7**: 硬币 $\times$ 骰子. $A=\{H\}\times S_2$, $B=S_1\times\{2,4,6\}$, 则 $A\cap B=E_1\times E_2$, 故 $P(A\cap B)=P(A)P(B)$.

### 无放回不独立 (例, §1.3.6)

袋中 1 红 3 蓝, 无放回抽两次. $(R,R)$ 不可能, 支撑不是完整的 $S_1\times S_2$.

$$\boldsymbol{P(\text{第二次红}\mid\text{第一次红})=0,\qquad P(\text{第二次红})=\frac14.}$$

条件概率 $\neq$ 无条件概率, 故两次抽取不独立. 有放回才会回到乘积空间.

---

# 2. Chapter 2 §2.1–2.5

## 2.1 随机变量与分布函数

**定义 2.1.1**: 随机变量 (random variable) 是 $X:S\to\mathbb{R}$. (测度论还要可测性, 本课略, Remark 2.1.2.) $\omega$ 不确定, 所以 $X(\omega)$ 不确定.

$$\boldsymbol{\{X\in B\}=\{\omega:X(\omega)\in B\},\qquad P(X=x)=P(\{\omega:X(\omega)=x\}).}$$

**例 2.1.3**: 两枚公平硬币, $X=$ 正面数. $X(HH)=2$, $X(HT)=X(TH)=1$, $X(TT)=0$, 值域 $\{0,1,2\}$.

**例 2.1.4**: 长 1 的绳子在 $\omega\in[0,1]$ 处剪断. $X(\omega)=\omega$ (剪点), $L(\omega)=\min\{\omega,1-\omega\}$ (较短一段). 二者都是 $\omega$ 的函数; $L$ 是 $X$ 的变换.

**例 2.1.5**: 两枚公平骰, $X=$ 点数和, $Y=$ 显示 3 的个数.

$$\boldsymbol{P(X=2)=P(\{(1,1)\})=\frac{1}{36},\qquad P(Y=2)=\frac{1}{36},\qquad P(Y=0)=\Bigl(\frac56\Bigr)^2=\frac{25}{36}.}$$

连续情形单点通常概率为 0: $X\sim\mathrm{Unif}[0,1]$ 时 $P(X=x)=0$. 有信息的是区间 $P(a<X\le b)$, $P(X\le b)$ 等.

### 定义 2.1.6 (CDF)

$$\boldsymbol{F_X(x)=P(X\le x).}$$

左半直线的概率决定区间概率: $a<b$ 时

$$\boldsymbol{P(a<X\le b)=F_X(b)-F_X(a).}$$

### 命题 2.1.7 (CDF 性质)

**假设**: $F_X$ 是某个随机变量的 CDF.

**结论**:

1. **非降**
2. **$\lim_{x\to-\infty}F_X(x)=0$, $\lim_{x\to\infty}F_X(x)=1$**
3. **右连续**: **$F_X(x)=\lim_{h\downarrow 0}F_X(x+h)$**
4. **左极限**: **$F_X(x-):=\lim_{h\downarrow 0}F_X(x-h)=P(X<x)$**
5. **跳跃即点质量**: **$P(X=x)=F_X(x)-F_X(x-)$**

**证明**:

1. $a\le b\Rightarrow\{X\le a\}\subseteq\{X\le b\}$, 用 Ch1 单调性.
2.–4. $\{X\le -n\}\downarrow\emptyset$, $\{X\le n\}\uparrow S$; $x_n\downarrow x$ 时 $\{X\le x_n\}\downarrow\{X\le x\}$; $x_n\uparrow x$ 时 $\{X\le x_n\}\uparrow\{X<x\}$. 用概率连续性.
5. $\{X\le x\}=\{X<x\}\cup\{X=x\}$ 不交, 相减.

**推论**: **$P(a\le X\le b)=F_X(b)-F_X(a-)$**. 闭区间要把左端点的跳跃加回来, 所以减的是左极限, 不是 $F(a)$.

**例 2.1.8**: 两硬币正面数, $P(X=0)=1/4$, $P(X=1)=1/2$, $P(X=2)=1/4$.

$$
F_X(x)=\begin{cases}
0 & x<0\\
1/4 & 0\le x<1\\
3/4 & 1\le x<2\\
1 & x\ge 2
\end{cases}
$$

阶梯取值: **$x<0$ 时 $F=0$**; **$0\le x<1$ 时 $F=1/4$**; **$1\le x<2$ 时 $F=3/4$**; **$x\ge 2$ 时 $F=1$**.

右连续阶梯; 跳跃高度就是 $P(X=k)$. 例如 $P(X=1)=3/4-1/4=1/2$.

### 定义 2.1.9 (离散 RV 与 PMF)

取值有限或可数, 则称离散. **概率质量函数 (PMF)** $p_X(x)=P(X=x)$.

$$\boldsymbol{p_X(x_i)\ge 0,\qquad \sum_i p_X(x_i)=1,\qquad F_X(b)=\sum_{x_i\le b}p_X(x_i),}$$

反过来 **$p_X(x)=F_X(x)-F_X(x-)$**.

---

## 2.2 重要离散分布

### 定义 2.2.1 Bernoulli$(p)$

一次成败, **$P(X=1)=p$, $P(X=0)=1-p$**.

### 定义 2.2.2 指示变量 (indicator)

$$
1_A(\omega)=\begin{cases}1 & \omega\in A\\ 0 & \omega\notin A\end{cases},\qquad \boldsymbol{1_A\sim\mathrm{Bernoulli}(P(A)).}
$$

后面 coupon 与线性性全靠它.

### 定义 2.2.3 $\mathrm{Bin}(n,p)$

$n$ 次独立 Bernoulli$(p)$, $X=$ 成功次数, $k=0,1,\ldots,n$,

$$\boldsymbol{P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}.}$$

**为何如此**: 指定哪 $k$ 次成功有 $\binom{n}{k}$ 种, 每种具体 0-1 序列概率都是 $p^k(1-p)^{n-k}$.

**归一**: 二项式定理 **$\sum_k\binom{n}{k}p^k(1-p)^{n-k}=1$**.

### 定义 2.2.4 $\mathrm{Geom}(p)$ (从 1 起)

$X=$ 首次成功所需试验次数, $k=1,2,\ldots$,

$$\boldsymbol{P(X=k)=(1-p)^{k-1}p.}$$

前 $k-1$ 次失败, 第 $k$ 次成功. **归一**: **$\sum_{k\ge 1}(1-p)^{k-1}p=1$** ($0<p\le 1$).

### 定义 2.2.5 $\mathrm{NegBin}(r,p)$

$X=$ 第 $r$ 次成功所需试验次数, $k=r,r+1,\ldots$,

$$\boldsymbol{P(X=k)=\binom{k-1}{r-1}p^r(1-p)^{k-r}.}$$

**为何如此**: 前 $k-1$ 次里恰有 $r-1$ 次成功, 第 $k$ 次必须是成功.

### 定义 2.2.6 $\mathrm{Poisson}(\lambda)$, $\lambda>0$

$$\boldsymbol{P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,2,\ldots.}$$

**归一**: **$e^{-\lambda}\sum_{k\ge 0}\lambda^k/k!=1$**. 用来做固定时间/区域内稀有事件计数 (错字, 事故).

### 命题 2.2.7 (泊松极限)

**假设**: $X_n\sim\mathrm{Bin}(n,p_n)$, $np_n\to\lambda\in(0,\infty)$.

**结论**: 每个固定 $k\ge 0$,

$$\boldsymbol{P(X_n=k)\to e^{-\lambda}\frac{\lambda^k}{k!}.}$$

即 **$X_n$ 依分布收敛到 $\mathrm{Poisson}(\lambda)$**. (「依分布」的正式定义在 §2.8, 本命题只要求逐点 PMF 极限.)

**证明** (笔记先证 $p_n=\lambda/n$; 一般情形同样):

$$
P(X_n=k)=\binom{n}{k}\Bigl(\frac{\lambda}{n}\Bigr)^k\Bigl(1-\frac{\lambda}{n}\Bigr)^{n-k}
=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot\Bigl(1-\frac{\lambda}{n}\Bigr)^n\cdot\Bigl(1-\frac{\lambda}{n}\Bigr)^{-k}.
$$

第一段 $\to 1$, 最后一段 $\to 1$, $(1-\lambda/n)^n\to e^{-\lambda}$.

---

## 2.3 连续随机变量

### 定义 2.3.1 (连续 RV 与 PDF)

存在非负可积 $f_X$ 使

$$\boldsymbol{F_X(x)=\int_{-\infty}^x f_X(u)\,du.}$$

$f_X$ 叫概率密度 (PDF). **密度不是概率**. 概率是积分:

$$\boldsymbol{P(a<X\le b)=\int_a^b f_X.}$$

$f_X$ 在 $x$ 连续时, $P(x<X\le x+\Delta x)\approx f_X(x)\Delta x$.

### 命题 2.3.2 (密度的基本性质)

1. **$f_X\ge 0$ 且 $\int_{-\infty}^\infty f_X=1$**
2. **每个固定 $x$, $P(X=x)=0$**
3. **$P(a\le X\le b)=\int_a^b f_X$** (单点无质量, 开闭端点一样)
4. **足够规则的 $B\subseteq\mathbb{R}$: $P(X\in B)=\int_B f_X$**

**$F_X$ 在 $x$ 可微时 $F_X'(x)=f_X(x)$**.

### 定义 2.3.3 $\mathrm{Unif}[a,b]$, $a<b$

$$
f_X(x)=\frac{1}{b-a}\mathbf{1}_{[a,b]}(x),\qquad
F_X(x)=\begin{cases}
0 & x<a\\
(x-a)/(b-a) & a\le x\le b\\
1 & x>b
\end{cases}.
$$

**密度**: **$f=1/(b-a)$** 在 $[a,b]$ 上. **CDF**: **$F(x)=(x-a)/(b-a)$** 在 $[a,b]$ 上.

### 命题 2.3.4 (逆变换采样, 连续严格增情形)

**假设**: $U\sim\mathrm{Unif}[0,1]$, $F$ 是连续且严格增的 CDF.

**结论**: **$X=F^{-1}(U)$ 的 CDF 就是 $F$**.

**证明**:

$$\boldsymbol{P(X\le x)=P(F^{-1}(U)\le x)=P(U\le F(x))=F(x),}$$

因为 $0\le t\le 1$ 时 $P(U\le t)=t$.

### 定义 2.3.5 $\mathrm{Exp}(\lambda)$, $\lambda>0$ (速率 rate)

**密度**: **$f_X(x)=\lambda e^{-\lambda x}$** ($x\ge 0$). **CDF**: **$F_X(x)=1-e^{-\lambda x}$** ($x\ge 0$), $x<0$ 时 $F=0$.

它是泊松过程里**第一次事件的等待时间**, 对应离散里的几何「等到第一次成功」. **生存函数 $P(X>x)=e^{-\lambda x}$** ($x\ge 0$) 由 $1-F$ 直接得到. **无记忆性不在本范围** (Ch5).

### 定义 2.3.6 $\mathrm{Gamma}(\alpha,\lambda)$, $\alpha>0$, $\lambda>0$

$$\boldsymbol{f_X(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x},\quad x>0,\qquad \Gamma(\alpha)=\int_0^\infty e^{-u}u^{\alpha-1}\,du.}$$

$\alpha$ 为正整数时, 这是泊松过程里**第 $\alpha$ 次事件的等待时间** (离散对照: 负二项). **$\mathrm{Exp}(\lambda)=\mathrm{Gamma}(1,\lambda)$**.

### 定义 2.3.7 $N(\mu,\sigma^2)$, $\sigma^2>0$

$$\boldsymbol{f_X(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\Bigl(-\frac{(x-\mu)^2}{2\sigma^2}\Bigr).}$$

标准正态 $Z\sim N(0,1)$: $\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}$, $\Phi(x)=\int_{-\infty}^x\varphi$. 一般正态是平移缩放:

$$\boldsymbol{f_X(x)=\frac1\sigma\,\varphi\Bigl(\frac{x-\mu}{\sigma}\Bigr).}$$

### 命题 2.3.8 (高斯密度归一)

**结论**: **$\int_{-\infty}^\infty\varphi(x)\,dx=1$**.

**证明**: 令 $I=\int_{-\infty}^\infty e^{-x^2/2}\,dx$. 则

$$I^2=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)/2}\,dx\,dy=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}\,r\,dr\,d\theta=2\pi,$$

故 $I=\sqrt{2\pi}$.

### 命题 2.3.9 (正态的仿射变换)

**假设**: $X\sim N(\mu,\sigma^2)$, $Y=aX+b$, $a\neq 0$.

**结论**: **$Y\sim N(a\mu+b,a^2\sigma^2)$**. 特别地 **$\mu+\sigma Z\sim N(\mu,\sigma^2)$** ($Z\sim N(0,1)$).

**证明** ($a>0$): $F_Y(y)=F_X((y-b)/a)$. 求导

$$f_Y(y)=\frac1a f_X\Bigl(\frac{y-b}{a}\Bigr),$$

这就是所述正态密度. $a<0$ 时不等式反向, 密度变换里用 $|a|$.

---

## 2.4 期望, 矩, 方差

重复试验的样本平均 $\bar X_N=N^{-1}\sum_{i=1}^N X_i$. 离散值 $x$ 的频率大约是 $N p_X(x)$ 时, $\bar X_N\approx\sum x\,p_X(x)$. 这是期望的动机.

### 定义 2.4.1 (期望 expectation)

离散 (和有定义时): **$EX=\sum_x x\,p_X(x)$**.

连续 (积分有定义时): **$EX=\int_{-\infty}^\infty x f_X(x)\,dx$**.

**例 2.4.2**: **$X\sim\mathrm{Bernoulli}(p)\Rightarrow EX=p$**.

**例 2.4.3**: **$X\sim\mathrm{Bin}(n,p)\Rightarrow EX=np$**.

**推导**: $k\binom{n}{k}=n\binom{n-1}{k-1}$, 故

$$EX=\sum_{k=0}^n k\binom{n}{k}p^k(1-p)^{n-k}=np\sum_{k=1}^n\binom{n-1}{k-1}p^{k-1}(1-p)^{n-k}=np.$$

(用 §2.5 的线性性也可以: $X=\sum_{i=1}^n 1_{\{\text{第 }i\text{ 次成功}\}}$, 每项期望 $p$, 不需要先证明方差可加.)

**例 2.4.4**: **$X\sim N(\mu,\sigma^2)\Rightarrow EX=\mu$**. 令 $y=x-\mu$, 被积的 $y$ 部分是奇函数, 积分为 0.

### 命题 2.4.5 (LOTUS, law of the unconscious statistician)

**假设**: $g:\mathbb{R}\to\mathbb{R}$, 下面的和或积分有定义.

**结论**: 不必先求 $g(X)$ 的分布,

$$\boldsymbol{E[g(X)]=\sum_x g(x)p_X(x)\quad\text{(离散)},\qquad E[g(X)]=\int g(x)f_X(x)\,dx\quad\text{(连续)}.}$$

**证明** (离散): $Y=g(X)$,

$$EY=\sum_y y\,P(Y=y)=\sum_y y\sum_{x:g(x)=y}p_X(x)=\sum_x g(x)p_X(x).$$

### 定义 2.4.6–2.4.7

- **第 $k$ 阶矩**: **$E[X^k]$**. **第 $k$ 阶中心矩**: **$E[(X-EX)^k]$**.
- **方差**: **$\mathrm{Var}(X)=E[(X-EX)^2]$**. **标准差**: **$\mathrm{SD}(X)=\sqrt{\mathrm{Var}(X)}$**.
- 方差度量 $X$ 在均值附近的离散程度.

### 命题 2.4.8 (方差计算式)

**假设**: $E[X^2]<\infty$.

**结论**: **$\mathrm{Var}(X)=E[X^2]-(EX)^2$**.

**证明**: 记 $\mu=EX$,

$$E[(X-\mu)^2]=E[X^2-2\mu X+\mu^2]=E[X^2]-2\mu^2+\mu^2=E[X^2]-\mu^2.$$

### 命题 2.4.9 (仿射变换下的方差)

**结论**: **$\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$**. 平移 $b$ 不改变方差; 缩放带 $a^2$, 不是 $|a|$.

**证明**: $aX+b$ 的均值是 $a\mu+b$, 偏差是 $a(X-\mu)$, 平方后提出 $a^2$.

**例 2.4.10**: **$X\sim N(\mu,\sigma^2)\Rightarrow\mathrm{Var}(X)=\sigma^2$**.

令 $y=x-\mu$, $t=y/\sigma$, 则 $\mathrm{Var}(X)=\sigma^2\int t^2\varphi(t)\,dt$. 该积分等于 1 (分部积分, 或认作标准正态二阶矩).

**矩可以不存在**: 标准柯西密度 **$f(x)=1/(\pi(1+x^2))$** 满足

$$E[X^2]=\int_{-\infty}^\infty\frac{x^2}{\pi(1+x^2)}\,dx=\infty.$$

所以不是每个随机变量都有有限均值或方差. 写 $EX$ 或 $\mathrm{Var}(X)$ 之前要确认矩存在.

### 范围内可当场推出、笔记未单独编号的矩

方法都是 Def 2.4.1 + Prop 2.4.8, 或几何级数 / 指示变量. Quiz 若给 PMF/PDF 让算均值, 用这些步骤, 不要背一个没有假设的表.

**几何** (从 1 起; 例 2.5.10 直接用了 **$EX=1/p$**). 令 $q=1-p$.

条件分解: 第一次成功则 $X=1$ (概率 $p$); 否则 $X=1+X'$, $X'\stackrel{d}{=}X$. 故

$$\boldsymbol{EX=p\cdot 1+(1-p)(1+EX)\Rightarrow EX=\frac1p.}$$

级数法: $\sum_{k\ge 1}k q^{k-1}=1/(1-q)^2$, 所以 $EX=p/(1-q)^2=1/p$.

二阶: 同样用 $E[X(X-1)]=\sum k(k-1)q^{k-1}p=2q/p^2$, 故 $E[X^2]=E[X(X-1)]+EX=2q/p^2+1/p$, 

$$\boldsymbol{\mathrm{Var}(X)=\frac{1-p}{p^2}.}$$

**负二项**: 拆成 $r$ 段「再等一次成功」的等待, 每段是 $\mathrm{Geom}(p)$, 和为 $X$. 线性性 (Prop 2.5.8, **不需要**各段独立) 给出 **$EX=r/p$**.

**泊松**:

$$\boldsymbol{EX=\sum_{k\ge 1}k\,e^{-\lambda}\frac{\lambda^k}{k!}=\lambda\sum_{k\ge 1}e^{-\lambda}\frac{\lambda^{k-1}}{(k-1)!}=\lambda.}$$

$$\boldsymbol{E[X(X-1)]=\lambda^2,\qquad E[X^2]=\lambda^2+\lambda,\qquad \mathrm{Var}(X)=\lambda.}$$

**均匀** $\mathrm{Unif}[a,b]$:

$$\boldsymbol{EX=\int_a^b\frac{x}{b-a}\,dx=\frac{a+b}{2}.}$$

$$\boldsymbol{E[X^2]=\frac{a^2+ab+b^2}{3},\qquad \mathrm{Var}(X)=\frac{(b-a)^2}{12}.}$$

(方差: $(a^2+ab+b^2)/3-(a+b)^2/4=(b-a)^2/12$.)

**指数** $\mathrm{Exp}(\lambda)$: 分部积分 $u=x$, $dv=\lambda e^{-\lambda x}dx$,

$$\boldsymbol{EX=\int_0^\infty e^{-\lambda x}\,dx=\frac1\lambda.}$$

再分部一次得 $E[X^2]=2/\lambda^2$, 故 $\mathrm{Var}(X)=1/\lambda^2$.

**二项方差** (若被问): $X=\sum_{i=1}^n X_i$, $X_i$ 为第 $i$ 次成败的指示. 单次 $\mathrm{Var}(X_i)=E[X_i^2]-(EX_i)^2=p-p^2=p(1-p)$. 各次独立时方差相加得 $np(1-p)$. **「独立则方差相加」的一般陈述在 §2.6, 超出范围**; 若卷面只给到 §2.5, 用 PMF 直接算 $E[X(X-1)]=n(n-1)p^2$ 更稳:

$$\boldsymbol{E[X^2]=n(n-1)p^2+np,\qquad \mathrm{Var}(X)=np(1-p).}$$

---

## 2.5 随机向量与联合分布

### 定义 2.5.1

$X=(X_1,\ldots,X_d):S\to\mathbb{R}^d$ 叫随机向量 (random vector). 各分量称为联合分布 (jointly distributed).

**例 2.5.2** (身高体重): 5 人等可能抽 1 人.

| 候选 | $H$ | $W$ |
|---|---|---|
| 1 | 180 | 69 |
| 2 | 182 | 75 |
| 3 | 175 | 65 |
| 4 | 174 | 70 |
| 5 | 170 | 68 |

$$\boldsymbol{P(H\ge 175)=\frac35,\qquad P(W\ge 70)=\frac25,\qquad P(H\ge 175,\,W\ge 70)=\frac15.}$$

联合 $\neq$ 边缘之积 ($1/5\neq 6/25$). **两个边缘概率决定不了联合概率.**

### 定义 2.5.3 (联合 CDF)

$$\boldsymbol{F_{X,Y}(x,y)=P(X\le x,\,Y\le y).}$$

**$d$ 维**: **$F(x_1,\ldots,x_d)=P(X_1\le x_1,\ldots,X_d\le x_d)$**.

**边缘 CDF**: 另一坐标趋于 $\infty$,

$$\boldsymbol{F_X(x)=\lim_{y\to\infty}F_{X,Y}(x,y),\qquad F_Y(y)=\lim_{x\to\infty}F_{X,Y}(x,y).}$$

反过来不对: **$F_X$ 与 $F_Y$ 不能决定 $F_{X,Y}$**.

### 定义 2.5.4 (联合 PMF)

取值有限或可数时 **$p_{X,Y}(x,y)=P(X=x,Y=y)$**.

**边缘**: **$p_X(x)=\sum_y p_{X,Y}(x,y)$**, **$p_Y(y)=\sum_x p_{X,Y}(x,y)$**.

$$\boldsymbol{F_{X,Y}(x,y)=\sum_{u\le x}\sum_{v\le y}p_{X,Y}(u,v).}$$

**矩形** (边界用左极限, 离散时必须留神端点):

$$\boldsymbol{P(x_1\le X\le x_2,\; y_1\le Y\le y_2)=F(x_2,y_2)-F(x_1-,y_2)-F(x_2,y_1-)+F(x_1-,y_1-).}$$

加回 $F(x_1-,y_1-)$ 是因为两个左极限各减了一次角上那块.

### 定义 2.5.5 (联合 PDF)

存在非负 $f_{X,Y}$ 使

$$\boldsymbol{F_{X,Y}(x,y)=\int_{-\infty}^x\int_{-\infty}^y f_{X,Y}(u,v)\,dv\,du.}$$

规则区域 $B\subseteq\mathbb{R}^2$:

$$\boldsymbol{P((X,Y)\in B)=\iint_B f_{X,Y}(x,y)\,dx\,dy.}$$

**边缘密度**:

$$\boldsymbol{f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dy,\qquad f_Y(y)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dx.}$$

**联合 CDF 二阶可微时 $f_{X,Y}=\partial^2 F_{X,Y}/(\partial x\,\partial y)$**.

**注 2.5.6**: **边缘连续推不出有二维密度**. $X\sim\mathrm{Unif}[0,1]$, $Y=X$. 两个边缘都连续, 但质量在直线 $y=x$ 上, 二维面积为 0, 没有普通的二维密度.

### 命题 2.5.7 (联合 LOTUS)

**联合离散**: **$E[g(X,Y)]=\sum_x\sum_y g(x,y)\,p_{X,Y}(x,y)$**.

**联合连续**: **$E[g(X,Y)]=\iint g(x,y)\,f_{X,Y}(x,y)\,dx\,dy$**.

取 $g(x,y)=x+y$ 得 **$E(X+Y)=EX+EY$**.

### 命题 2.5.8 (期望线性性)

**假设**: $X_1,\ldots,X_n$ 的期望存在, $a_i$ 为常数. **不假设独立**.

**结论**:

$$\boldsymbol{E\Bigl[\sum_{i=1}^n a_i X_i\Bigr]=\sum_{i=1}^n a_i EX_i.}$$

这是本范围内最常用的计算工具: 和的期望等于期望的和, 即使变量相依 (无放回, coupon 的指示变量都相依).

### 例 2.5.9 (抽 $n$ 次后的不同种类数)

$N$ 种卡, 每次均匀独立. $I_i=1_{\{\text{种类 }i\text{ 出现在前 }n\text{ 次}\}}$, $X=\sum_{i=1}^N I_i$.

$$\boldsymbol{EI_i=1-\Bigl(1-\frac1N\Bigr)^n,\qquad EX=N\Bigl(1-\Bigl(1-\frac1N\Bigr)^n\Bigr).}$$

$I_i$ 彼此不独立, 但线性性不需要独立.

### 例 2.5.10 (集齐时间)

已有 $i$ 种时, 下一次抽到新种类的概率 $p_i=(N-i)/N$. 额外等待

$$\boldsymbol{Y_i\sim\mathrm{Geom}\Bigl(\frac{N-i}{N}\Bigr),\qquad EY_i=\frac{N}{N-i},\qquad T=\sum_{i=0}^{N-1}Y_i.}$$

$$\boldsymbol{ET=\sum_{i=0}^{N-1}\frac{N}{N-i}=N\sum_{j=1}^N\frac1j=N H_N.}$$

$H_N$ 是第 $N$ 个调和数. 各段 $Y_i$ 的分布不同, 仍然只用线性性.

---

# 3. 分布卡片 (只含范围内对象)

| 分布 | 支撑 | PMF / PDF | 笔记给出的 CDF 或均值 |
|---|---|---|---|
| Bernoulli$(p)$ | $\{0,1\}$ | $P(X=1)=p$ | $EX=p$ (例 2.4.2) |
| Bin$(n,p)$ | $0,\ldots,n$ | $\binom{n}{k}p^k(1-p)^{n-k}$ | $EX=np$ (例 2.4.3) |
| Geom$(p)$ | $1,2,\ldots$ | $(1-p)^{k-1}p$ | 例 2.5.10 用 $EX=1/p$ |
| NegBin$(r,p)$ | $r,r+1,\ldots$ | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ | 拆成 $r$ 段几何后 $EX=r/p$ |
| Poisson$(\lambda)$ | $0,1,\ldots$ | $e^{-\lambda}\lambda^k/k!$ | 由 PMF 可推 $EX=\mathrm{Var}=\lambda$ |
| Unif$[a,b]$ | $[a,b]$ | $1/(b-a)$ | CDF $(x-a)/(b-a)$; $EX=(a+b)/2$ |
| Exp$(\lambda)$ | $[0,\infty)$ | $\lambda e^{-\lambda x}$ | $F=1-e^{-\lambda x}$; $EX=1/\lambda$ |
| Gamma$(\alpha,\lambda)$ | $(0,\infty)$ | $\lambda^\alpha x^{\alpha-1}e^{-\lambda x}/\Gamma(\alpha)$ | 整数 $\alpha$: 第 $\alpha$ 次事件等待 |
| $N(\mu,\sigma^2)$ | $\mathbb{R}$ | $\sigma^{-1}\varphi((x-\mu)/\sigma)$ | $EX=\mu$, $\mathrm{Var}=\sigma^2$ (例 2.4.4, 2.4.10) |

---

# 4. 范围内易错

1. **$P(A\mid B)$ 与 $P(B\mid A)$ 分子相同, 分母不同**. 瓮的例子就是在求后者.
2. **两孩问题必须有序**; 四个结果等可能, 条件后剩三个.
3. **互斥且概率都正 $\Rightarrow$ 不独立**. 独立看乘积, 不看「像不像无关」.
4. **和为 7 与第一枚的面独立; 和为 6 则不独立**. 要算, 不要猜.
5. **两两独立检查的是每对; 相互独立还要三重及更多交集**. 例 1.3.4 的三重概率是 $1/36$ 不是 $1/216$.
6. **无放回: 条件概率会变, 不是乘积空间**.
7. **CDF 右连续**. **$P(X=x)$ 是跳跃 $F(x)-F(x-)$**, 不是 $F(x)$ 本身.
8. **$P(a<X\le b)=F(b)-F(a)$**; **闭区间 $P(a\le X\le b)=F(b)-F(a-)$**. 连续型二者相同, 因为单点概率为 0.
9. **PDF 的函数值可以大于 1** (例如 $\mathrm{Unif}[0,0.1]$ 的密度是 10). 积分才是概率.
10. **边缘定不了联合**. 身高体重: $3/5$ 与 $2/5$ 的乘积不是 $1/5$.
11. **$Y=X$ 且 $X$ 连续: 边缘有密度, 联合没有二维密度**.
12. **线性性不需要独立**. 方差可加才需要 (那是 §2.6, 别提前用, 除非你改用 $E[X^2]-(EX)^2$ 直接算).
13. **$\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$**, 常数项消失, 系数是平方.
14. **柯西: 密度积分可以是 1, 同时 $E[X^2]=\infty$**.
15. **泊松极限要 $np_n\to\lambda$**, 不是单独 $n\to\infty$ 或单独 $p\to 0$.

---

# 5. 明确不在 Quiz1

做到 §2.5 的 coupon collector 为止. 下面这些在同一章后半或后章, **不要**当成这次必背:

- §2.6: $X\perp\!\!\!\perp Y$ 的定义, $F_{X,Y}=F_XF_Y$, 密度/质量乘积, 协方差, 不相关, 独立正态之和, 卷积
- §2.7: MGF, 独立和的 MGF 相乘, MGF 唯一性
- §2.8: Markov, Chebyshev, 依概率收敛, WLLN, 依分布收敛, CLT
- Ch3: 条件分布, 条件期望, 全期望, 变换与 Jacobian
- Ch5: 指数无记忆, 泊松过程

事件的独立 (Ch1) 已经在范围内; 随机变量的独立 (§2.6) 不在.
