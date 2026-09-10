# MATH3603 Cheatsheet

> 词条/公式/定理速查; 对话中学到的内容会增量追加.

---

## 名词

+ **Elementary / compound event** / **简单事件 / 复合事件**:
    + 简单 = 单点集; 复合 = 多点集 (课堂 in-class notes 1)
+ **Sample space** / **样本空间** $S$:
    + 实验所有可能结果的集合; 亦可记 $\Omega$
+ **Event** / **事件**:
    + $S$ 的子集; 发生 $\Leftrightarrow \omega\in E$
+ **Probability as set function** / **概率作为集合函数**:
    + $\mathbb{P}$ 作用在事件上; 公理见 Ch.1 讲义
+ **Mutually exclusive** / **互斥**:
    + $E\cap F=\emptyset$
+ **Conditional probability** / **条件概率**:
    + $P(A|B)=P(A\cap B)/P(B)$, 需 $P(B)>0$
+ **Partition** / **划分**:
    + 互斥且并 $=S$ 的事件组
+ **Independent** / **独立**:
    + $P(A\cap B)=P(A)P(B)$; 互斥 (正概率) 则不独立
+ **Pairwise vs Mutual independence** / **两两独立 vs 相互独立**:
    + 两两独立弱于相互独立; 需检查所有 $|J|\ge 2$ 的交集
+ **Random variable** / **随机变量** $X$:
    + $X:S\to\mathbb{R}$; $\{X\in B\}=\{\omega:X(\omega)\in B\}$
+ **CDF** $F_X(x)=P(X\le x)$:
    + 非降, 右连续; $P(X=x)=F(x)-F(x-)$
+ **PMF / PDF**:
    + 离散 $p_X(x)=P(X=x)$; 连续 $F=\int f$, 密度本身非概率
+ **LOTUS**:
    + $E[g(X)]$ 直接对 $X$ 的分布积分/求和
+ **Covariance / Uncorrelated**:
    + $\mathrm{Cov}(X,Y)=E[XY]-EX\,EY$; 不相关 $\not\Rightarrow$ 独立
+ **MGF** $M_X(t)=E[e^{tX}]$:
    + 独立和乘积; 唯一性; $M^{(k)}(0)=E[X^k]$
+ **Convergence in probability / distribution**:
    + $Z_n\xrightarrow{P}Z$; $Z_n\xrightarrow{d}Z$ (CDF 在连续点收敛)
+ **Conditional PMF/PDF**:
    + $p_{Y|X}=p_{X,Y}/p_X$; $f_{Y|X}=f_{X,Y}/f_X$
+ **Conditional expectation** $E[Y|X]=m(X)$:
    + 均方最优 $X$-可测预测; $EY=E[E[Y|X]]$
+ **Markov chain** / **Markov 链**:
    + 已知现在, 过去对下一步无关; $p_{ij}$ 一步转移
+ **Communicating class / Irreducible**:
    + $i\leftrightarrow j$ 划分互通类; 不可约 = 单类
+ **Recurrent / Transient**:
    + $f_{ii}=1$ / $<1$; $\sum_n p_{ii}^{(n)}=\infty$ $\Leftrightarrow$ 常返
+ **Positive / Null recurrent**:
    + $E_i T_i^+<\infty$ / $=\infty$; 周期 $d(i)=\gcd$ 返回步
+ **Stationary / Limiting distribution**:
    + $\pi=\pi P$; 极限 $p_{ij}^{(n)}\to\pi_j$ (遍历时)
+ **Fundamental matrix** $G_T=(I-Q)^{-1}$:
    + 暂态期望占用时间
+ **PGF** $G_X(s)=E[s^X]$:
    + 独立和乘积; 复合和 $G_N\circ G_Y$
+ **Poisson process** / **Poisson 过程**:
    + 独立增量 + $N(t)-N(s)\sim\mathrm{Poisson}(\lambda(t-s))$ (齐次)
+ **Memoryless / Thinning / Superposition**:
    + Exp 无记忆; 独立标记分裂; 独立过程叠加速率相加
+ **Order statistics** / **次序统计量**:
    + $N(t)=n$ 时到达 $\stackrel{d}{=}$ $n$ 个 $\mathrm{Unif}[0,t]$ 的次序统计
+ **Nonhomogeneous intensity** $\lambda(t)$, $m(t)=\int_0^t\lambda$:
    + 增量 $\sim\mathrm{Poisson}(m(t)-m(s))$

## 公式

+ **Probability axioms** / **概率公理**:
    + $P(S)=1$; 可数可加
+ **Complement** / **补集**:
    + $P(A^c)=1-P(A)$
+ **Inclusion–exclusion (2 events)** / **两事件容斥**:
    + $P(A\cup B)=P(A)+P(B)-P(A\cap B)$
+ **Multiplication rule** / **乘法法则**:
    + $P(A\cap B)=P(A|B)P(B)$
+ **Law of total probability** / **全概率公式**:
    + $P(E)=\sum_j P(F_j)P(E|F_j)$
+ **Bayes' theorem** / **贝叶斯定理**:
    + $P(F_i|E)=\dfrac{P(F_i)P(E|F_i)}{\sum_j P(F_j)P(E|F_j)}$
+ **Product space** / **乘积概率空间**:
    + $P(E_1\times E_2)=P_1(E_1)P_2(E_2)$ (独立实验)
+ **Common discrete laws**:
    + $\mathrm{Bin}$: $\binom{n}{k}p^k(1-p)^{n-k}$; $\mathrm{Geom}$: $(1-p)^{k-1}p$; $\mathrm{Poisson}$: $e^{-\lambda}\lambda^k/k!$
+ **Common continuous laws**:
    + $\mathrm{Exp}(\lambda)$: $\lambda e^{-\lambda x}$; $N(\mu,\sigma^2)$: $\frac{1}{\sqrt{2\pi}\sigma}e^{-(x-\mu)^2/(2\sigma^2)}$
+ **Variance / Cov**:
    + $\mathrm{Var}(X)=E[X^2]-(EX)^2$; $\mathrm{Var}(\sum X_i)=\sum\mathrm{Var}+2\sum_{i<j}\mathrm{Cov}$
+ **Markov / Chebyshev**:
    + $P(X\ge a)\le EX/a$ ($X\ge 0$); $P(|X-\mu|\ge a)\le\mathrm{Var}(X)/a^2$
+ **WLLN / CLT**:
    + $\bar X_n\xrightarrow{P}\mu$; $\sum(X_i-\mu)/(\sigma\sqrt{n})\xrightarrow{d}N(0,1)$
+ **Law of total expectation / Random sum**:
    + $EY=E[E[Y|X]]$; $E\sum_{i=1}^N X_i=(EN)(EX_1)$
+ **Poisson|sum binomial**:
    + $X\mid(X+Y=n)\sim\mathrm{Bin}(n,\lambda_1/(\lambda_1+\lambda_2))$
+ **Bivariate normal conditional**:
    + $E[X|Y]=\mu_X+\rho(\sigma_X/\sigma_Y)(Y-\mu_Y)$; 条件方差 $\sigma_X^2(1-\rho^2)$
+ **Monotone transform / Jacobian**:
    + $f_Y(y)=f_X(g^{-1}(y))| (g^{-1})'|$; $f_{U,V}=f_{X,Y}|\det DT^{-1}|$
+ **Chapman–Kolmogorov**:
    + $p_{ij}^{(m+n)}=\sum_k p_{ik}^{(m)}p_{kj}^{(n)}$; $\mu_n=\mu_0 P^n$
+ **Gambler's ruin**:
    + $u_i=\dfrac{1-(q/p)^i}{1-(q/p)^N}$ ($p\neq q$); $i/N$ ($p=1/2$)
+ **Branching extinction**:
    + $\eta=\min\{s\in[0,1]:s=G(s)\}$; $\mu\le 1$ (非退化) $\Rightarrow\eta=1$; $\mu>1\Rightarrow\eta<1$
+ **Poisson process basics**:
    + $P(N(t)=k)=e^{-\lambda t}(\lambda t)^k/k!$; $T_i\sim\mathrm{Exp}(\lambda)$ i.i.d.; $S_n\sim\mathrm{Gamma}(n,\lambda)$
+ **Thinning / Superposition / Race**:
    + 速率 $\lambda p$; 叠加 $\lambda_1+\lambda_2$; $P(X_1<X_2)=\lambda_1/(\lambda_1+\lambda_2)$
+ **Conditional arrivals**:
    + 给定 $N(t)=n$: 密度 $n!/t^n$ on $0<s_1<\cdots<s_n<t$
+ **NHPP mean**:
    + $N(t)-N(s)\sim\mathrm{Poisson}\bigl(\int_s^t\lambda(u)\,du\bigr)$

## 定理

+ **Proposition 1.1.10**:
    + $P(\emptyset)=0$, 单调性, 有限可加
+ **Theorem 1.1.12**:
    + 一般容斥公式
+ **Poisson limit of Binomial** (Prop. 2.2.7):
    + $np_n\to\lambda$ $\Rightarrow$ $\mathrm{Bin}(n,p_n)\xrightarrow{d}\mathrm{Poisson}(\lambda)$
+ **MGF uniqueness** (Thm. 2.7.3):
    + 含 0 开区间上 MGF 相同 $\Rightarrow$ 同分布
+ **WLLN / CLT** (Thm. 2.8.4 / 2.8.7):
    + 见公式节
+ **Mean-square prediction** (Prop. 3.2.4):
    + $E[Y|X]$ 最小化 $E[(Y-h(X))^2]$
+ **Ergodic MC limit** (Thm. 4.6.7):
    + 不可约正通常返非周期 $\Rightarrow$ $p_{ij}^{(n)}\to\pi_j=1/m_j$
+ **Finite irreducible MC**:
    + 全部正通常返
+ **RW recurrence**:
    + 1D: 仅 $p=1/2$ 常返 (且零常返); $d=1,2$ 对称常返, $d\ge 3$ 暂态
+ **Poisson process equivalence** (Thm. 5.2.6):
    + 增量定义 $\Leftrightarrow$ 无穷小定义
+ **Conditional arrivals = uniform order stats** (Thm. 5.6.4)

## 问答沉淀

_(待补充)_
