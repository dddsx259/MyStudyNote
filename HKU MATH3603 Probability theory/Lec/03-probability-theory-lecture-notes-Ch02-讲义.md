# Chapter 2: 随机变量 (random variables), 分布 (distributions) 与极限定理 (limit theorems)

- **来源**: `Lec/01-probability-theory-lecture-notes.pdf` Chapter 2 (p.21–43)
- **课程**: MATH3603, Zhigang Bao
- **前置**: Ch.1 概率公理 (probability axioms), 条件概率 (conditional probability), 独立性 (independence)
- **本章目标**: 掌握 随机变量 (RV) / 累积分布函数 (CDF, cumulative distribution function) / 概率质量函数 (PMF, probability mass function) / 概率密度函数 (PDF, probability density function), 常用分布族, 期望 (expectation) 与方差 (variance), 联合分布 (joint distribution) 与独立性, 矩母函数 (MGF, moment generating function), 以及 马尔可夫不等式 (Markov's inequality) / 切比雪夫不等式 (Chebyshev's inequality) / 弱大数定律 (WLLN, weak law of large numbers) / 中心极限定理 (CLT, central limit theorem)

---

## 2.1 随机变量与分布函数

### 核心概念

- **随机变量** $X:S\to\mathbb{R}$: 给每个结果赋数值. (课件定义; 测度论还需可测性 (measurability), 本课略.) **定义, 无需证明**.
- **事件记号**: $\{X\in B\}=\{\omega:X(\omega)\in B\}$, 故 $P(X=x)=P(\{\omega:X(\omega)=x\})$. **记号约定, 无需证明**.
- **离散 (discrete) vs 连续 (continuous)**:
  - 离散: 取值有限或可数; 单点概率可正.
  - 连续: 通常 $P(X=x)=0$; 有信息的是区间概率 $P(a<X\le b)$ 等.

### 累积分布函数 (CDF)

$$F_X(x):=P(X\le x).$$

**定义, 无需证明**.

**性质** (Prop. 2.1.7): 非降; $\lim_{x\to-\infty}F=0$, $\lim_{x\to\infty}F=1$; 右连续 (right-continuous); 左极限 $F(x-)=P(X<x)$; 跳跃 $P(X=x)=F(x)-F(x-)$.

**证明**:

1. **非降**: $x<y$ $\Rightarrow$ $\{X\le x\}\subseteq\{X\le y\}$ $\Rightarrow$ $F(x)\le F(y)$ (Ch.1 单调性).
2. **极限**: $\{X\le -n\}\downarrow\emptyset$, $\{X\le n\}\uparrow S$. 由概率的连续性 (continuity of probability; 见下) 得 $F(-n)\to 0$, $F(n)\to 1$.
3. **右连续**: 令 $x_n\downarrow x$. 则 $\{X\le x_n\}\downarrow\{X\le x\}$, 故 $F(x_n)\to F(x)$.
4. **左极限**: $x_n\uparrow x$ 时 $\{X\le x_n\}\uparrow\{X<x\}$, 故 $F(x-)=P(X<x)$.
5. **跳跃**: $P(X=x)=P(X\le x)-P(X<x)=F(x)-F(x-)$.

**概率连续性** (用于上): 若 $A_n\uparrow A$ 则 $P(A_n)\to P(A)$; 若 $A_n\downarrow A$ 则 $P(A_n)\to P(A)$.

**证明思路**: 递增时令 $B_1=A_1$, $B_k=A_k\setminus A_{k-1}$ ($k\ge 2$), 互斥且并 $=A$, 可数可加得 $P(A)=\sum P(B_k)=\lim P(A_n)$. 递减时对补集用递增情形.

区间概率:
$$P(a<X\le b)=F(b)-F(a),\qquad P(a\le X\le b)=F(b)-F(a-).$$

**证明**:
$$\{a<X\le b\}=\{X\le b\}\setminus\{X\le a\}\Rightarrow P=F(b)-F(a).$$
$$\{a\le X\le b\}=\{X\le b\}\setminus\{X<a\}\Rightarrow P=F(b)-P(X<a)=F(b)-F(a-).$$

### 概率质量函数 (PMF)

离散时 $p_X(x)=P(X=x)$, $\sum_x p_X(x)=1$, $F(b)=\sum_{x\le b}p_X(x)$.

**定义** $p_X(x)=P(X=x)$. **定义, 无需证明**.

**证明** ($\sum p=1$ 与 CDF 表示): 支撑点 $\{x_i\}$ 互斥且并覆盖 $S$ (在 $X$ 的值域意义下), 可数可加得 $\sum_i p_X(x_i)=1$. 又 $\{X\le b\}=\bigcup_{x_i\le b}\{X=x_i\}$, 故 $F(b)=\sum_{x\le b}p_X(x)$.

---

## 2.2 重要离散分布

| 分布 | 含义 | PMF |
|---|---|---|
| 伯努利分布 (Bernoulli distribution) $\mathrm{Bernoulli}(p)$ | 单次成败; 指示 $1_A\sim\mathrm{Bernoulli}(P(A))$ | $P(X=1)=p$ |
| 二项分布 (binomial distribution) $\mathrm{Bin}(n,p)$ | $n$ 次独立伯努利成功数 | $\binom{n}{k}p^k(1-p)^{n-k}$ |
| 几何分布 (geometric distribution) $\mathrm{Geom}(p)$ | 首次成功所需试验次数 ($k=1,2,\ldots$) | $(1-p)^{k-1}p$ |
| 负二项分布 (negative binomial) $\mathrm{NegBin}(r,p)$ | 第 $r$ 次成功所需试验次数 | $\binom{k-1}{r-1}p^r(1-p)^{k-r}$ |
| 泊松分布 (Poisson distribution) $\mathrm{Poisson}(\lambda)$ | 稀有事件计数模型 | $e^{-\lambda}\lambda^k/k!$ |

上表各 PMF 为**分布定义**. **定义, 无需证明** (需验证其非负且和为 1).

**归一化验证**:

- 伯努利: $p+(1-p)=1$.
- 二项: 二项式定理 $\sum_k\binom{n}{k}p^k(1-p)^{n-k}=(p+(1-p))^n=1$.
- 几何: $\sum_{k=1}^\infty(1-p)^{k-1}p=p/(1-(1-p))=1$ ($0<p\le 1$).
- 负二项: 可视为第 $r$ 次成功恰在第 $k$ 次 $\Leftrightarrow$ 前 $k-1$ 次恰有 $r-1$ 次成功, 再乘末次成功; 求和用负二项式级数或「等待拆成 $r$ 段几何」的概率解释得 1.
- 泊松: $e^{-\lambda}\sum_{k\ge 0}\lambda^k/k!=e^{-\lambda}e^\lambda=1$.

**二项 PMF 推导**: $n$ 次独立 $\mathrm{Bernoulli}(p)$, $X=\sum_{i=1}^n X_i$. 恰 $k$ 次成功的具体序列概率为 $p^k(1-p)^{n-k}$, 共有 $\binom{n}{k}$ 个, 相加即得.

**几何 / 负二项推导**: 几何: 前 $k-1$ 次失败再成功, 概率 $(1-p)^{k-1}p$. 负二项: 前 $k-1$ 次中恰 $r-1$ 次成功 (二项系数), 第 $k$ 次成功.

**泊松逼近二项** (Prop. 2.2.7): $X_n\sim\mathrm{Bin}(n,p_n)$, $np_n\to\lambda$ $\Rightarrow$ $P(X_n=k)\to e^{-\lambda}\lambda^k/k!$.

**证明**:
$$
\begin{aligned}
P(X_n=k)
&=\binom{n}{k}p_n^k(1-p_n)^{n-k}
=\frac{n(n-1)\cdots(n-k+1)}{k!}\,p_n^k\,(1-p_n)^{n-k}\\
&=\frac{1}{k!}\Bigl(\prod_{j=0}^{k-1}\bigl(1-\tfrac{j}{n}\bigr)\Bigr)(np_n)^k\,(1-p_n)^{n}\,(1-p_n)^{-k}.
\end{aligned}
$$
因 $np_n\to\lambda$, 有 $p_n\to 0$, 故 $(1-p_n)^{-k}\to 1$, 且 $\prod(1-j/n)\to 1$. 又
$$(1-p_n)^n=\exp\bigl(n\log(1-p_n)\bigr),\qquad n\log(1-p_n)=n\bigl(-p_n+O(p_n^2)\bigr)\to-\lambda,$$
故 $(1-p_n)^n\to e^{-\lambda}$. 合起来得 $P(X_n=k)\to e^{-\lambda}\lambda^k/k!$.

**补充直觉**: 几何/负二项是"等成功"的等待; 泊松是"大量试验, 每次极小成功概率"的极限计数.

---

## 2.3 连续随机变量

### 概率密度函数 (PDF)

存在非负可积 $f_X$ 使 $F_X(x)=\int_{-\infty}^x f_X(u)\,du$. 密度本身不是概率; $P(a<X\le b)=\int_a^b f$. 小区间: $P(x<X\le x+\Delta x)\approx f(x)\Delta x$.

**定义** (绝对连续情形). **定义, 无需证明**.

**证明** ($P(a<X\le b)=\int_a^b f$): 由 CDF 定义与微积分基本定理 (fundamental theorem of calculus),
$$P(a<X\le b)=F(b)-F(a)=\int_{-\infty}^b f-\int_{-\infty}^a f=\int_a^b f.$$
近似式来自 $F(x+\Delta x)-F(x)\approx f(x)\Delta x$ (当 $f$ 在 $x$ 连续).

### 常用连续族

- 均匀分布 (uniform distribution) $\mathrm{Unif}[a,b]$: $f=1/(b-a)$ on $[a,b]$. **定义, 无需证明**. ($\int_a^b f=1$ 显然.)
- **逆变换采样 (inverse transform sampling)**: $U\sim\mathrm{Unif}[0,1]$, $F$ 连续严格增 $\Rightarrow$ $X=F^{-1}(U)$ 有 CDF $F$.

**证明**:
$$P(X\le x)=P\bigl(F^{-1}(U)\le x\bigr)=P\bigl(U\le F(x)\bigr)=F(x),$$
最后一步因 $U\sim\mathrm{Unif}[0,1]$ 且 $F(x)\in[0,1]$. (若 $F$ 仅非降, 用广义逆 $F^{-1}(u)=\inf\{x:F(x)\ge u\}$ 同理.)

- 指数分布 (exponential distribution) $\mathrm{Exp}(\lambda)$: $f=\lambda e^{-\lambda x}$ ($x\ge 0$); 泊松过程 (Poisson process) 首次到达等待 (Ch.5). **定义, 无需证明**.
- 伽马分布 (gamma distribution) $\mathrm{Gamma}(\alpha,\lambda)$: $f=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}$; $\alpha$ 为正整数时为第 $\alpha$ 次事件等待. **定义, 无需证明**. ($\int_0^\infty f=1$ 由 $\Gamma$ 函数定义.)
- 正态分布 (normal distribution) $N(\mu,\sigma^2)$: $f(x)=\frac{1}{\sqrt{2\pi}\sigma}\exp\bigl(-(x-\mu)^2/(2\sigma^2)\bigr)$; 标准正态 (standard normal) $\varphi,\Phi$. **定义, 无需证明**.

**正态归一化** ($\int\varphi=1$):

**证明思路**: 令 $I=\int_{-\infty}^\infty e^{-x^2/2}\,dx$. 则
$$I^2=\iint_{\mathbb{R}^2}e^{-(x^2+y^2)/2}\,dx\,dy=\int_0^{2\pi}\int_0^\infty e^{-r^2/2}r\,dr\,d\theta=2\pi,$$
故 $I=\sqrt{2\pi}$. 一般 $N(\mu,\sigma^2)$ 作替换 $z=(x-\mu)/\sigma$ 即得.

**正态仿射**: $X\sim N(\mu,\sigma^2)$ $\Rightarrow$ $aX+b\sim N(a\mu+b,a^2\sigma^2)$ ($a\neq 0$).

**证明**: CDF 法. 设 $a>0$,
$$P(aX+b\le y)=P\bigl(X\le\tfrac{y-b}{a}\bigr)=\Phi\Bigl(\tfrac{(y-b)/a-\mu}{\sigma}\Bigr)=\Phi\Bigl(\tfrac{y-(a\mu+b)}{|a|\sigma}\Bigr),$$
即 $N(a\mu+b,a^2\sigma^2)$ 的 CDF. $a<0$ 时不等式反向, 标准差用 $|a|\sigma$, 结论相同. (亦可用 MGF: $M_{aX+b}(t)=e^{bt}M_X(at)$, 代入正态 MGF.)

**指数无记忆性 (memorylessness)**: $P(X>s+t\mid X>s)=P(X>t)$.

**证明**: $P(X>s)=e^{-\lambda s}$, 故
$$P(X>s+t\mid X>s)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda s}}=e^{-\lambda t}=P(X>t).$$

---

## 2.4 期望, 矩 (moment), 方差

### 定义

离散: $EX=\sum xp_X(x)$; 连续: $EX=\int xf_X(x)\,dx$ (存在时). **定义, 无需证明**.

**无意识统计员定律 (LOTUS, law of the unconscious statistician)**: $E[g(X)]=\sum g(x)p_X(x)$ 或 $\int g(x)f_X(x)\,dx$, 不必先求 $g(X)$ 的分布.

**证明思路** (离散): 设 $Y=g(X)$. 则
$$EY=\sum_y y\,P(Y=y)=\sum_y y\sum_{x:g(x)=y}p_X(x)=\sum_x g(x)p_X(x).$$
连续情形对简单函数逼近再取极限 (或换元 / Fubini), 本课可接受「按定义对像空间积分」.

$$\mathrm{Var}(X)=E[(X-EX)^2]=E[X^2]-(EX)^2,\qquad \mathrm{Var}(aX+b)=a^2\mathrm{Var}(X).$$

**证明** (方差展开):
$$
\begin{aligned}
E[(X-\mu)^2]
&=E[X^2-2\mu X+\mu^2]=E[X^2]-2\mu EX+\mu^2\\
&=E[X^2]-2\mu^2+\mu^2=E[X^2]-\mu^2,
\end{aligned}
$$
其中 $\mu=EX$. 仿射:
$$\mathrm{Var}(aX+b)=E[(aX+b-a\mu-b)^2]=E[a^2(X-\mu)^2]=a^2\mathrm{Var}(X).$$

**注意**: 柯西分布 (Cauchy) 等重尾分布 (heavy-tailed distribution) 可无有限均值/方差.

常用: 伯努利: $EX=p$; 二项: $EX=np$; $N(\mu,\sigma^2)$: 均值 $\mu$, 方差 $\sigma^2$.

**证明**:

- 伯努利: $EX=0\cdot(1-p)+1\cdot p=p$.
- 二项: $X=\sum_{i=1}^n X_i$, $X_i$ i.i.d. 伯努利, 由线性性 $EX=np$. (或直接 $\sum k\binom{n}{k}p^k(1-p)^{n-k}=np$.)
- 正态: 对称性 / 对密度积分; 或对 MGF 求导: $M'(0)=\mu$, $M''(0)-[M'(0)]^2=\sigma^2$ (见 2.7).

**几何期望**: $X\sim\mathrm{Geom}(p)$ (从 1 起) $\Rightarrow$ $EX=1/p$.

**证明思路**: $EX=\sum_{k=1}^\infty k(1-p)^{k-1}p$. 用 $\sum_{k\ge 1}kq^{k-1}=1/(1-q)^2$ ($|q|<1$), 得 $EX=p\cdot 1/p^2=1/p$. 或条件期望: 首次试验成功则 $X=1$, 否则 $X=1+X'$, $X'\stackrel{d}{=}X$, 得 $EX=p\cdot 1+(1-p)(1+EX)$.

---

## 2.5 随机向量 (random vector) 与联合分布

- **联合累积分布函数 (joint CDF)**: $F_{X,Y}(x,y)=P(X\le x,Y\le y)$; 边缘分布 (marginal distribution) 由另一坐标 $\to\infty$ 得到. **边缘不定联合**.
- **联合离散**: $p_{X,Y}(x,y)$; 边缘对另一变量求和.
- **联合连续**: 联合密度 (joint density) $f_{X,Y}$; $P((X,Y)\in B)=\iint_B f$; 边缘对另一变量积分.
- **补充**: 边缘连续 $\not\Rightarrow$ 有二维密度 (例: $Y=X$, 质量在对角线上).

以上为**定义 / 记号**. **定义, 无需证明**.

**边缘公式验证** (离散): $p_X(x)=P(X=x)=\sum_y P(X=x,Y=y)=\sum_y p_{X,Y}(x,y)$. 连续同理用 Fubini:
$$P(X\le x)=\int_{-\infty}^x\int_{-\infty}^\infty f_{X,Y}(u,v)\,dv\,du.$$

**联合 LOTUS** + **期望线性性 (linearity of expectation)** (无需独立): $E\sum a_i X_i=\sum a_i EX_i$.

**证明思路**: 对非负或绝对可积情形, 离散时
$$E\Bigl[\sum_i a_i X_i\Bigr]=\sum_{\omega}\Bigl(\sum_i a_i X_i(\omega)\Bigr)P(\{\omega\})=\sum_i a_i\sum_{\omega}X_i(\omega)P(\{\omega\})=\sum_i a_i EX_i$$
(有限和可交换; 一般用 Tonelli/Fubini). 连续类似. **关键**: 不需要独立性.

### 优惠券收集问题 (coupon collector) (例)

$N$ 种卡, 均匀独立抽取.

- $n$ 次后不同种类期望: $N\bigl(1-(1-1/N)^n\bigr)$ (指示变量 (indicator variable) + 线性).
- 集齐时间 $T$: $ET=N\sum_{j=1}^N 1/j$ (分段几何等待).

**证明**:

1. 令 $I_j=1_{\{\text{种类 }j\text{ 在 }n\text{ 次中出现}\}}$. 则 $E I_j=1-(1-1/N)^n$, 不同种类数 $K=\sum_{j=1}^N I_j$, 故 $EK=N(1-(1-1/N)^n)$.
2. 令 $T_j$ 为已有 $j-1$ 种后再等到新种类的等待 ($j=1,\ldots,N$). 则 $T_j\sim\mathrm{Geom}((N-j+1)/N)$ (从 1 起), $ET_j=N/(N-j+1)$. $T=\sum_{j=1}^N T_j$, 线性性得
   $$ET=\sum_{j=1}^N\frac{N}{N-j+1}=N\sum_{m=1}^N\frac{1}{m}.$$

---

## 2.6 独立性, 协方差 (covariance), 和的分布

### 独立性

$X\perp\!\!\!\perp Y$ $\Leftrightarrow$ $P(X\in A,Y\in B)=P(X\in A)P(Y\in B)$ $\Leftrightarrow$ $F_{X,Y}=F_XF_Y$ $\Leftrightarrow$ PMF/PDF 乘积分解.

**定义** (事件形式 / 联合 CDF 形式). **定义, 无需证明**.

**证明思路** (等价性摘要):

- 事件形式 $\Rightarrow$ $F_{X,Y}=F_XF_Y$: 取 $A=(-\infty,x]$, $B=(-\infty,y]$.
- $F$ 分解 $\Rightarrow$ 离散 PMF 分解: 用跳跃 $p(x,y)=F(x,y)-F(x-,y)-F(x,y-)+F(x-,y-)$ 得乘积.
- 连续: 在密度存在时对 CDF 求混合偏导得 $f_{X,Y}=f_Xf_Y$.
- 反之由乘积积分/求和还原矩形概率, 再延拓.

独立 $\Rightarrow$ $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$, 特别 $E[XY]=EX\,EY$.

**证明** (离散): 
$$E[g(X)h(Y)]=\sum_{x,y}g(x)h(y)p_X(x)p_Y(y)=\Bigl(\sum_x g(x)p_X(x)\Bigr)\Bigl(\sum_y h(y)p_Y(y)\Bigr).$$
连续用 $\iint g(x)h(y)f_X(x)f_Y(y)\,dx\,dy$ 同理 (Fubini).

### 协方差

$$\mathrm{Cov}(X,Y)=E[(X-EX)(Y-EY)]=E[XY]-EX\,EY.$$

**定义** 前者; 后者为恒等式.

**证明**:
$$
\begin{aligned}
E[(X-\mu)(Y-\nu)]
&=E[XY-\mu Y-\nu X+\mu\nu]=E[XY]-\mu EY-\nu EX+\mu\nu\\
&=E[XY]-\mu\nu.
\end{aligned}
$$

$$\mathrm{Var}\Bigl(\sum_i X_i\Bigr)=\sum_i\mathrm{Var}(X_i)+2\sum_{i<j}\mathrm{Cov}(X_i,X_j).$$

**证明**:
$$
\begin{aligned}
\mathrm{Var}\Bigl(\sum_i X_i\Bigr)
&=E\Bigl[\Bigl(\sum_i(X_i-\mu_i)\Bigr)^2\Bigr]
=\sum_i\sum_j E[(X_i-\mu_i)(X_j-\mu_j)]\\
&=\sum_i\mathrm{Var}(X_i)+2\sum_{i<j}\mathrm{Cov}(X_i,X_j).
\end{aligned}
$$

独立 $\Rightarrow$ 协方差为 0 $\Rightarrow$ 方差可加. **不相关 (uncorrelated) $\not\Rightarrow$ 独立** (例: $Y=1_{\{X=0\}}$).

**证明**: 独立 $\Rightarrow$ $E[XY]=EX\,EY$ $\Rightarrow$ $\mathrm{Cov}=0$. 代入方差公式得可加. 反例思路: 取对称 $X$ 使 $EX=0$, $Y=X^2$ 或示性 $1_{\{X=0\}}$ 适当中心化后 $\mathrm{Cov}=0$ 但函数相关, 故不独立.

### 卷积 (convolution)

独立时: $p_{X+Y}(z)=\sum_x p_X(x)p_Y(z-x)$; $f_{X+Y}=f_X*f_Y$.

**证明** (离散):
$$P(X+Y=z)=\sum_x P(X=x,Y=z-x)=\sum_x p_X(x)p_Y(z-x).$$
连续: 先求 CDF $P(X+Y\le z)=\iint_{x+y\le z}f_X(x)f_Y(y)\,dx\,dy$, 换元后对 $z$ 求导得 $f_{X+Y}(z)=\int f_X(x)f_Y(z-x)\,dx$.

独立正态之和仍正态, 均值/方差相加 (Thm. 2.6.8).

**证明思路**: 用卷积直接算两个正态密度的卷积 (配平方) ; 或用 MGF: 独立时 $M_{X+Y}=M_XM_Y$, 正态 MGF 相乘仍为正态 MGF, 由唯一性得分布. 均值方差由线性与独立方差可加得到.

---

## 2.7 矩母函数 (MGF)

$$M_X(t)=E[e^{tX}]\quad\text{(定义域内)}.$$

**定义, 无需证明**.

- 独立和: $M_{X+Y}=M_XM_Y$.

**证明**: 独立 $\Rightarrow$ $E[e^{t(X+Y)}]=E[e^{tX}e^{tY}]=E[e^{tX}]E[e^{tY}]$.

- **唯一性 (uniqueness)**: 在含 0 的开区间上 MGF 相同 $\Rightarrow$ 同分布.

**证明思路**: 标准结果 — MGF 在 0 邻域存在则决定所有矩, 且在一定条件下决定分布 (可与特征函数 (characteristic function) $\varphi(t)=E[e^{itX}]$ 联系: MGF 在虚轴上即特征函数; 特征函数唯一决定分布 (Lévy 连续性定理的唯一性部分)). 本课作工具使用.

- 导数: $M_X^{(k)}(0)=E[X^k]$ (可交换时).

**证明思路**: $M_X(t)=E[e^{tX}]$. 在积分/求和号下对 $t$ 求导 (控制收敛或一致可积保证交换): $\partial_t^k e^{tX}=X^k e^{tX}$, 再令 $t=0$ 得 $E[X^k]$.

| 分布 | MGF |
|---|---|
| $\mathrm{Bernoulli}(p)$ | $1-p+pe^t$ |
| $\mathrm{Bin}(n,p)$ | $(1-p+pe^t)^n$ |
| $\mathrm{Poisson}(\lambda)$ | $\exp\{\lambda(e^t-1)\}$ |
| $\mathrm{Exp}(\lambda)$ | $\lambda/(\lambda-t)$ ($t<\lambda$) |
| $N(\mu,\sigma^2)$ | $\exp\{\mu t+\frac12\sigma^2 t^2\}$ |

**证明** (逐行):

- 伯努利: $E[e^{tX}]=(1-p)+p e^t$.
- 二项: $X=\sum_{i=1}^n X_i$ 独立伯努利 $\Rightarrow$ $M_X=(1-p+pe^t)^n$.
- 泊松: $\sum_{k\ge 0}e^{tk}e^{-\lambda}\lambda^k/k!=e^{-\lambda}\sum(\lambda e^t)^k/k!=\exp\{\lambda(e^t-1)\}$.
- 指数: $\int_0^\infty e^{tx}\lambda e^{-\lambda x}\,dx=\lambda/(\lambda-t)$ ($t<\lambda$).
- 正态: 对 $N(0,1)$, $E[e^{tZ}]=\frac{1}{\sqrt{2\pi}}\int e^{tz-z^2/2}\,dz=e^{t^2/2}$ (配平方). 一般 $X=\mu+\sigma Z$, $M_X(t)=e^{\mu t}M_Z(\sigma t)=\exp\{\mu t+\frac12\sigma^2 t^2\}$.

应用: 泊松独立和 $\sim\mathrm{Poisson}(\lambda+\mu)$; 独立正态和再证.

**证明**: $M_{X+Y}(t)=\exp\{\lambda(e^t-1)\}\exp\{\mu(e^t-1)\}=\exp\{(\lambda+\mu)(e^t-1)\}$, 由唯一性即 $\mathrm{Poisson}(\lambda+\mu)$. 正态同理乘 MGF.

**由 MGF 得泊松均值方差**: $M'(t)=M(t)\cdot\lambda e^t$, $M'(0)=\lambda$; 再求 $M''(0)=\lambda+\lambda^2$, 故 $\mathrm{Var}=M''(0)-[M'(0)]^2=\lambda$.

---

## 2.8 极限定理

### 不等式

- **马尔可夫不等式**: $X\ge 0$, $a>0$ $\Rightarrow$ $P(X\ge a)\le EX/a$.

**证明**: $X=X\cdot 1_{\{X\ge a\}}+X\cdot 1_{\{X<a\}}\ge a\cdot 1_{\{X\ge a\}}$. 取期望:
$$EX\ge a\,P(X\ge a).$$

- **切比雪夫不等式**: $P(|X-\mu|\ge a)\le\mathrm{Var}(X)/a^2$.

**证明**: 令 $Y=(X-\mu)^2\ge 0$, 对 $Y$ 用马尔可夫 (阈值 $a^2$):
$$P(|X-\mu|\ge a)=P(Y\ge a^2)\le E[Y]/a^2=\mathrm{Var}(X)/a^2.$$

### 依概率收敛 (convergence in probability) / 弱大数定律 (WLLN)

$Z_n\xrightarrow{P}Z$: 对一切 $\varepsilon>0$, $P(|Z_n-Z|>\varepsilon)\to 0$.

**定义, 无需证明**.

**弱大数定律**: 独立同分布 (i.i.d., independent and identically distributed), $E=\mu$, $\mathrm{Var}=\sigma^2<\infty$ $\Rightarrow$ $\bar X_n\xrightarrow{P}\mu$.

**证明**: $\bar X_n=n^{-1}\sum_{i=1}^n X_i$. 由线性性 $E\bar X_n=\mu$; 由独立方差可加
$$\mathrm{Var}(\bar X_n)=\frac{1}{n^2}\sum_{i=1}^n\mathrm{Var}(X_i)=\frac{\sigma^2}{n}.$$
切比雪夫:
$$P\bigl(|\bar X_n-\mu|\ge\varepsilon\bigr)\le\frac{\sigma^2}{n\varepsilon^2}\to 0.$$

**补充**: 若全取同一 $X$, 平均不降方差; WLLN 需要独立性 (或足够弱相关).

### 中心极限定理 (CLT)

依分布收敛 (convergence in distribution): $F_{Z_n}(x)\to F_Z(x)$ 在 $F_Z$ 连续点.

**定义, 无需证明**.

**中心极限定理**: i.i.d., 均值 $\mu$, 方差 $\sigma^2\in(0,\infty)$ $\Rightarrow$
$$\frac{1}{\sigma\sqrt{n}}\sum_{i=1}^n(X_i-\mu)\xrightarrow{d}N(0,1).$$

**证明思路** (课件: 局部 MGF + 泰勒展开; 假设 MGF 在 0 邻域存在):

1. **标准化**: 令 $Y_i=(X_i-\mu)/\sigma$, 则 $EY_i=0$, $\mathrm{Var}(Y_i)=1$. 目标证 $S_n/\sqrt{n}\xrightarrow{d}N(0,1)$, 其中 $S_n=\sum_{i=1}^n Y_i$.
2. **MGF**: 独立同分布 $\Rightarrow$ $M_{S_n/\sqrt{n}}(t)=\bigl[M_Y(t/\sqrt{n})\bigr]^n$.
3. **泰勒**: $M_Y(0)=1$, $M_Y'(0)=0$, $M_Y''(0)=1$, 故
   $$M_Y(u)=1+\frac{u^2}{2}+o(u^2)\quad(u\to 0).$$
   取 $u=t/\sqrt{n}$:
   $$M_Y(t/\sqrt{n})=1+\frac{t^2}{2n}+o(n^{-1}).$$
4. **取极限**:
   $$\bigl[M_Y(t/\sqrt{n})\bigr]^n=\exp\Bigl(n\log\bigl(1+\tfrac{t^2}{2n}+o(n^{-1})\bigr)\Bigr)\to\exp(t^2/2),$$
   因 $n\log(1+t^2/(2n)+o(n^{-1}))\to t^2/2$.
5. **唯一性**: 极限 MGF 即 $N(0,1)$ 的 MGF, 故 $S_n/\sqrt{n}\xrightarrow{d}N(0,1)$.

**注**: 经典 CLT 本身不要求 MGF 存在; 一般证明用特征函数作同样展开 $\varphi_Y(t/\sqrt{n})^n\to e^{-t^2/2}$, 再引用 Lévy 连续性定理 (Lévy's continuity theorem). 有限方差是本质条件; Lindeberg 条件可推广到非同分布三角阵列.

---

## 例题要点

1. 两枚硬币头数 CDF: 右连续阶梯, 跳跃 = 点质量.
2. 优惠券收集: 指示 / 分段几何 + 线性期望.
3. 两独立 $\mathrm{Unif}[0,1]$ 之和: 三角密度 (卷积).

**证明思路** (三角密度): $f_X=f_Y=1_{[0,1]}$.
$$f_{X+Y}(z)=\int_{\mathbb{R}}1_{[0,1]}(x)1_{[0,1]}(z-x)\,dx.$$
$z\in[0,1]$ 时积分长度为 $z$; $z\in[1,2]$ 时为 $2-z$; 否则 0. 即三角 (Irwin–Hall $n=2$).

4. MGF 推泊松均值方差, 独立泊松/正态可加性.

---

## 易错点

- 连续分布写 $P(X=x)=0$ 不代表"无信息"; 应用区间/密度.
- 几何定义从 1 起 (试验次数), 勿与从 0 起的"失败次数"混用.
- 密度可 $>1$; 积分为概率.
- 线性期望始终成立; 方差可加需要独立 (或零相关).
- 不相关 $\neq$ 独立.
- MGF 可能只在 $t=0$ 邻域或半线存在 (指数, 柯西).

---

## 与前后章关系

- **承 Ch.1**: 事件概率升级为随机变量上的分布; 独立性扩展到随机变量.
- **启 Ch.3**: 联合分布 $\to$ 条件分布 (conditional distribution) / 条件期望 (conditional expectation) / 变换 (transformation).
- **启 Ch.5**: 指数 / 伽马 / 泊松在泊松过程中系统化; 随机和与优惠券的泊松化 (Poissonization).
- **启 Ch.4**: 独立和, 指示, 期望线性贯穿马尔可夫链 (Markov chain) 计算.
