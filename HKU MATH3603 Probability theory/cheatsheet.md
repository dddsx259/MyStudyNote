# MATH3603 Cheatsheet

> 词条/公式/定理速查; 对话中学到的内容会增量追加.
> 约定: **定义 / 定理 / 引理 / 命题 / 推论** 与带保证的公式一律写清 **假设** 与 **结论** (定义可用 **定义** 代替结论); 证明见对应讲义.

---

## 名词

+ **Elementary / compound event** / **简单事件 / 复合事件**:
    + **假设**: 样本空间 $S$ 已给定
    + **定义**: 简单事件 = 单点集; 复合事件 = 多点集 (课堂 in-class notes 1)

+ **Sample space** / **样本空间** $S$:
    + **假设**: 一次随机实验已指定
    + **定义**: 该实验所有可能结果的集合; 亦可记 $\Omega$

+ **Event** / **事件**:
    + **假设**: 样本空间 $S$ 与可测族 $\mathcal{F}$ (有限情形常取幂集)
    + **定义**: $E\in\mathcal{F}$ (即 $S$ 的子集); 事件发生 $\Leftrightarrow \omega\in E$

+ **Probability as set function** / **概率作为集合函数**:
    + **假设**: 概率空间 $(S,\mathcal{F},P)$
    + **定义**: $P:\mathcal{F}\to[0,1]$ 满足概率公理 (见公式节); 作用对象是事件而非单个数字记号

+ **Mutually exclusive** / **互斥**:
    + **假设**: 事件 $E,F\subseteq S$
    + **定义**: $E\cap F=\emptyset$ (可推广到两两互斥族)

+ **Conditional probability** / **条件概率**:
    + **假设**: $P(B)>0$
    + **定义**: $P(A|B)=P(A\cap B)/P(B)$
    + **注**: 固定 $B$ 后 $Q(\cdot)=P(\cdot|B)$ 仍是概率测度

+ **Partition** / **划分**:
    + **假设**: 事件族 $\{F_j\}$
    + **定义**: 两两互斥且 $\bigcup_j F_j=S$ (全概率公式中常再要求 $P(F_j)>0$)

+ **Independent** / **独立** (两事件):
    + **假设**: 事件 $A,B$
    + **定义**: $P(A\cap B)=P(A)P(B)$
    + **注**: 当 $P(B)>0$ 时等价于 $P(A|B)=P(A)$; 互斥且 $P(A),P(B)>0$ $\Rightarrow$ 不独立

+ **Pairwise vs Mutual independence** / **两两独立 vs 相互独立**:
    + **假设**: 事件 $A_1,\ldots,A_n$
    + **两两独立**: 任意 $i\neq j$, $P(A_i\cap A_j)=P(A_i)P(A_j)$
    + **相互独立**: 任意 $J\subseteq\{1,\ldots,n\}$, $|J|\ge 2$, $P(\bigcap_{j\in J}A_j)=\prod_{j\in J}P(A_j)$
    + **注**: 相互独立 $\Rightarrow$ 两两独立; 反之不真 (需检查所有 $|J|\ge 2$ 的交集)

+ **Random variable** / **随机变量** $X$:
    + **假设**: 概率空间 $(S,\mathcal{F},P)$
    + **定义**: 可测映射 $X:S\to\mathbb{R}$; $\{X\in B\}=\{\omega:X(\omega)\in B\}$

+ **CDF** / **累积分布函数** $F_X$:
    + **假设**: 实值随机变量 $X$
    + **定义**: $F_X(x)=P(X\le x)$
    + **性质**: 非降, 右连续, $\lim_{x\to-\infty}F=0$, $\lim_{x\to\infty}F=1$; $P(X=x)=F(x)-F(x-)$

+ **PMF / PDF** / **概率质量函数 / 概率密度函数**:
    + **离散 PMF**: $p_X(x)=P(X=x)$, $\sum_x p_X(x)=1$
    + **连续 PDF**: 存在非负可积 $f_X$ 使 $F_X(x)=\int_{-\infty}^x f_X$; 密度本身不是概率; $P(a<X\le b)=\int_a^b f$

+ **LOTUS** / **无意识统计员定律**:
    + **假设**: $X$ 有已知分布, $g$ 使 $E|g(X)|<\infty$ (或非负)
    + **公式**: 离散 $E[g(X)]=\sum_x g(x)p_X(x)$; 连续 $E[g(X)]=\int g(x)f_X(x)\,dx$ (无需先求 $g(X)$ 的分布)

+ **Covariance / Uncorrelated** / **协方差 / 不相关**:
    + **假设**: $EX^2,EY^2<\infty$
    + **定义**: $\mathrm{Cov}(X,Y)=E[XY]-EX\,EY$; 不相关指 $\mathrm{Cov}=0$
    + **注**: 独立 $\Rightarrow$ 不相关; 不相关 $\not\Rightarrow$ 独立 (二元正态族内二者等价)

+ **MGF** / **矩母函数** $M_X(t)=E[e^{tX}]$:
    + **假设**: $t$ 在使期望有限的定义域内
    + **定义**: $M_X(t)=E[e^{tX}]$
    + **性质**: 独立和 $M_{X+Y}=M_XM_Y$; 可交换求导时 $M^{(k)}(0)=E[X^k]$; 含 0 开区间上相同 $\Rightarrow$ 同分布 (见定理节)

+ **Convergence in probability / distribution** / **依概率收敛 / 依分布收敛**:
    + **依概率** $Z_n\xrightarrow{P}Z$: 对一切 $\varepsilon>0$, $P(|Z_n-Z|>\varepsilon)\to 0$
    + **依分布** $Z_n\xrightarrow{d}Z$: $F_{Z_n}(x)\to F_Z(x)$ 在 $F_Z$ 的连续点

+ **Conditional PMF/PDF** / **条件 PMF/PDF**:
    + **离散假设**: $p_X(x)>0$; **定义**: $p_{Y|X}(y|x)=p_{X,Y}(x,y)/p_X(x)$
    + **连续假设**: $f_X(x)>0$; **定义**: $f_{Y|X}(y|x)=f_{X,Y}(x,y)/f_X(x)$

+ **Conditional expectation** / **条件期望** $E[Y|X]=m(X)$:
    + **假设**: $E|Y|<\infty$; $m(x)=E[Y|X=x]$ (离散求和 / 连续积分)
    + **定义**: $E[Y|X]:=m(X)$ ($X$-可测)
    + **性质**: $E[X|X]=X$; $X\perp Y\Rightarrow E[X|Y]=EX$; 全期望 $EY=E[E[Y|X]]$

+ **Markov chain** / **Markov 链** (离散时间):
    + **假设**: 状态空间可数, 时齐转移核 $P=(p_{ij})$
    + **定义**: 马尔可夫性 — 已知现在, 过去对下一步无关; $p_{ij}=P(X_{n+1}=j\mid X_n=i)$

+ **Communicating class / Irreducible** / **互通类 / 不可约**:
    + **定义**: $i\to j$ 指存在 $n\ge 0$ 使 $p_{ij}^{(n)}>0$; $i\leftrightarrow j$ 为互通
    + **互通类**: 互通关系划分出的等价类
    + **不可约**: 整个状态空间是单一互通类

+ **Recurrent / Transient** / **常返 / 暂态**:
    + **定义**: $f_{ii}=P_i(\text{某时刻返回 }i)$; 常返 $f_{ii}=1$, 暂态 $f_{ii}<1$
    + **等价**: $\sum_n p_{ii}^{(n)}=\infty$ $\Leftrightarrow$ 常返 (暂态则级数有限)

+ **Positive / Null recurrent / Period** / **正通常返 / 零常返 / 周期**:
    + **假设**: 状态 $i$ 常返; $T_i^+=\inf\{n\ge 1:X_n=i\}$
    + **正通常返**: $m_i=E_i T_i^+<\infty$; **零常返**: $m_i=\infty$
    + **周期**: $d(i)=\gcd\{n\ge 1:p_{ii}^{(n)}>0\}$; $d=1$ 为非周期; 周期是类性质

+ **Stationary / Limiting distribution** / **平稳分布 / 极限分布**:
    + **平稳**: $\pi=\pi P$, $\pi_j\ge 0$, $\sum\pi_j=1$; 若 $X_0\sim\pi$ 则一切 $X_n\sim\pi$
    + **极限**: $\lim_n p_{ij}^{(n)}=\pi_j$ (常与起点无关); 存在极限 $\Rightarrow$ 极限必平稳, 反之未必

+ **Fundamental matrix** / **基本矩阵** $G_T=(I-Q)^{-1}$:
    + **假设**: $T$ 为暂态态集合, $Q=(p_{ij})_{i,j\in T}$, 暂态类上级数收敛
    + **定义 / 公式**: $g_{ij}=E_i\sum_{n=0}^\infty 1_{\{X_n=j\}}$, $G_T=(g_{ij})=\sum_{n\ge 0}Q^n=(I-Q)^{-1}$
    + **注**: 到达概率 $f_{ij}=(g_{ij}-\delta_{ij})/g_{jj}$

+ **PGF** / **概率生成函数** $G_X(s)=E[s^X]$:
    + **假设**: 非负整值随机变量 $X$, $|s|\le 1$ (或使级数收敛)
    + **定义**: $G_X(s)=\sum_k p_X(k)s^k$
    + **性质**: $EX=G'(1-)$; 独立和 PGF 相乘; 复合和 $G_{S_N}=G_N\circ G_Y$

+ **Poisson process** / **Poisson 过程** (齐次):
    + **假设**: 计数过程 $N(t)$, 速率 $\lambda>0$
    + **定义 A**: $N(0)=0$; 独立增量; $N(s+t)-N(s)\sim\mathrm{Poisson}(\lambda t)$
    + **定义 B**: $N(0)=0$; 平稳独立增量; $P(N(h)=1)=\lambda h+o(h)$, $P(N(h)\ge 2)=o(h)$
    + **注**: 两定义等价 (Thm. 5.2.6)

+ **Memoryless / Thinning / Superposition** / **无记忆 / 稀疏 / 叠加**:
    + **无记忆** (Exp): $P(X>s+t\mid X>s)=P(X>t)$
    + **稀疏**: 每事件独立以概率 $p$ 标记保留, 得速率 $\lambda p$ 的泊松过程
    + **叠加**: 独立泊松过程叠加, 速率相加

+ **Order statistics** / **次序统计量**:
    + **假设**: i.i.d. 连续样本 $Y_1,\ldots,Y_n$, 密度 $f$
    + **定义**: $Y_{(1)}\le\cdots\le Y_{(n)}$; 有序区域联合密度 $=n!\prod_i f(y_i)$
    + **泊松联系**: 给定 $N(t)=n$, 到达时刻 $\stackrel{d}{=}$ $n$ 个 $\mathrm{Unif}[0,t]$ 的次序统计

+ **Nonhomogeneous intensity** / **非齐次强度** $\lambda(t)$, $m(t)=\int_0^t\lambda$:
    + **假设**: $\lambda(t)\ge 0$ 可积; NHPP 独立增量与无穷小条件
    + **定义**: 均值函数 $m(t)=\int_0^t\lambda(s)\,ds$; 增量 $N(t)-N(s)\sim\mathrm{Poisson}(m(t)-m(s))$

---

## 公式

+ **Probability axioms** / **概率公理** (Def. 1.1.8–1.1.9):
    + **假设**: $P:\mathcal{F}\to[0,1]$ 为概率
    + **公式**: $0\le P(A)\le 1$; $P(S)=1$; 互斥可数族 $A_i$ 时 $P(\bigcup A_i)=\sum P(A_i)$

+ **Complement** / **补集**:
    + **假设**: 概率公理成立
    + **公式**: $P(A^c)=1-P(A)$

+ **Inclusion–exclusion (2 events)** / **两事件容斥**:
    + **假设**: 事件 $A,B$
    + **公式**: $P(A\cup B)=P(A)+P(B)-P(A\cap B)$

+ **Multiplication rule** / **乘法法则**:
    + **假设**: 相应条件概率有定义 (如 $P(B)>0$)
    + **公式**: $P(A\cap B)=P(A|B)P(B)=P(B|A)P(A)$
    + **链式**: $P(A\cap B\cap C)=P(A)P(B|A)P(C|A\cap B)$

+ **Law of total probability** / **全概率公式**:
    + **假设**: $\{F_j\}$ 为划分且 $P(F_j)>0$
    + **公式**: $P(E)=\sum_j P(F_j)P(E|F_j)$

+ **Bayes' theorem** / **贝叶斯定理**:
    + **假设**: $\{F_j\}$ 为划分, $P(F_j)>0$, $P(E)>0$
    + **公式**: $P(F_i|E)=\dfrac{P(F_i)P(E|F_i)}{\sum_j P(F_j)P(E|F_j)}$

+ **Product space** / **乘积概率空间**:
    + **假设**: 独立实验 $(S_1,P_1)$, $(S_2,P_2)$
    + **公式**: $P(E_1\times E_2)=P_1(E_1)P_2(E_2)$

+ **Common discrete laws** / **常用离散分布**:
    + **Bernoulli$(p)$**: $P(X=1)=p$, $P(X=0)=1-p$
    + **Bin$(n,p)$**: $\binom{n}{k}p^k(1-p)^{n-k}$
    + **Geom$(p)$** (首次成功时刻): $(1-p)^{k-1}p$, $k=1,2,\ldots$
    + **Poisson$(\lambda)$**: $e^{-\lambda}\lambda^k/k!$

+ **Common continuous laws** / **常用连续分布**:
    + **Unif$[a,b]$**: $f=1/(b-a)$ on $[a,b]$
    + **Exp$(\lambda)$**: $f(x)=\lambda e^{-\lambda x}$ ($x>0$), 无记忆
    + **$N(\mu,\sigma^2)$**: $\dfrac{1}{\sqrt{2\pi}\sigma}\exp\bigl(-(x-\mu)^2/(2\sigma^2)\bigr)$

+ **Variance / Cov** / **方差 / 协方差展开**:
    + **假设**: 相应二阶矩有限
    + **公式**: $\mathrm{Var}(X)=E[X^2]-(EX)^2$; $\mathrm{Var}(\sum_i X_i)=\sum_i\mathrm{Var}(X_i)+2\sum_{i<j}\mathrm{Cov}(X_i,X_j)$
    + **独立时**: 协方差交叉项为 0, 方差可加

+ **Markov / Chebyshev** / **马尔可夫 / 切比雪夫不等式**:
    + **Markov 假设**: $X\ge 0$, $a>0$; **保证**: $P(X\ge a)\le EX/a$
    + **Chebyshev 假设**: $E|X|<\infty$, $\mathrm{Var}(X)<\infty$, $a>0$; **保证**: $P(|X-\mu|\ge a)\le\mathrm{Var}(X)/a^2$ ($\mu=EX$)

+ **WLLN / CLT** / **弱大数定律 / 中心极限定理**:
    + **WLLN 假设**: $X_i$ i.i.d., $EX_i=\mu$, $\mathrm{Var}(X_i)=\sigma^2<\infty$; **结论**: $\bar X_n\xrightarrow{P}\mu$
    + **CLT 假设**: $X_i$ i.i.d., $EX_i=\mu$, $\mathrm{Var}(X_i)=\sigma^2\in(0,\infty)$; **结论**: $\dfrac{1}{\sigma\sqrt{n}}\sum_{i=1}^n(X_i-\mu)\xrightarrow{d}N(0,1)$

+ **Law of total expectation / Random sum** / **全期望 / 随机和**:
    + **全期望假设**: $E|Y|<\infty$; **公式**: $EY=E[E[Y|X]]$
    + **随机和假设**: $N$ 与 i.i.d. $X_i$ 独立, $EN<\infty$, $E|X_1|<\infty$; **公式**: $E\sum_{i=1}^N X_i=(EN)(EX_1)$

+ **Poisson|sum binomial** / **泊松和条件二项**:
    + **假设**: $X\sim\mathrm{Poisson}(\lambda_1)$, $Y\sim\mathrm{Poisson}(\lambda_2)$ 独立
    + **公式**: $X\mid(X+Y=n)\sim\mathrm{Bin}\bigl(n,\lambda_1/(\lambda_1+\lambda_2)\bigr)$

+ **Bivariate normal conditional** / **二元正态条件律**:
    + **假设**: $(X,Y)$ 二元正态, 参数 $(\mu_X,\mu_Y,\sigma_X,\sigma_Y,\rho)$, $|\rho|<1$
    + **公式**: $E[X|Y]=\mu_X+\rho(\sigma_X/\sigma_Y)(Y-\mu_Y)$; 条件方差 $\sigma_X^2(1-\rho^2)$
    + **注**: 族内 $\rho=0\Leftrightarrow$ 独立

+ **Monotone transform / Jacobian** / **单调变换 / 雅可比**:
    + **一维假设**: $Y=g(X)$ 严格单调可微, $X$ 有密度 $f_X$
    + **公式**: $f_Y(y)=f_X(g^{-1}(y))\bigl|(g^{-1})'(y)\bigr|$
    + **二维假设**: $(U,V)=T(X,Y)$ 光滑可逆
    + **公式**: $f_{U,V}(u,v)=f_{X,Y}(T^{-1}(u,v))\bigl|\det DT^{-1}(u,v)\bigr|$

+ **Chapman–Kolmogorov** / **查普曼–柯尔莫哥洛夫**:
    + **假设**: 时齐 Markov 链, 转移阵 $P$
    + **公式**: $p_{ij}^{(m+n)}=\sum_k p_{ik}^{(m)}p_{kj}^{(n)}$; 行分布 $\mu_n=\mu_0 P^n$

+ **Gambler's ruin** / **赌徒破产**:
    + **假设**: 状态 $\{0,\ldots,N\}$, $0,N$ 吸收; 内部以 $p$ 上 $q=1-p$ 下; $u_i=P_i(\text{先达 }N)$
    + **公式**: $p\neq q$ 时 $u_i=\dfrac{1-(q/p)^i}{1-(q/p)^N}$; $p=q=1/2$ 时 $u_i=i/N$
    + **注**: $N\to\infty$ 固定 $i$: $p>1/2$ 时极限 $1-(q/p)^i$; $p\le 1/2$ 时极限 $0$

+ **Branching extinction** / **分支过程灭绝概率**:
    + **假设**: Galton–Watson, $Z_0=1$, 子代 i.i.d. PGF $G$, $p_0>0$, 非退化; $\mu=E\xi$, $\eta=\lim P(Z_n=0)$
    + **公式 / 结论**: $\eta=\min\{s\in[0,1]:s=G(s)\}$; $\mu\le 1$ (非 $\xi\equiv 1$) $\Rightarrow\eta=1$; $\mu>1\Rightarrow\eta<1$; $\xi\equiv 1\Rightarrow\eta=0$

+ **Poisson process basics** / **泊松过程基本量**:
    + **假设**: 齐次 PP 速率 $\lambda$
    + **公式**: $P(N(t)=k)=e^{-\lambda t}(\lambda t)^k/k!$; 间隔 $T_i\sim\mathrm{Exp}(\lambda)$ i.i.d.; 到达 $S_n\sim\mathrm{Gamma}(n,\lambda)$; $EN(t)=\mathrm{Var}(N(t))=\lambda t$

+ **Thinning / Superposition / Race** / **稀疏 / 叠加 / 指数竞赛**:
    + **稀疏假设**: 独立标记概率 $p$; **结论**: 子过程速率 $\lambda p$ (且与互补过程独立)
    + **叠加假设**: 独立 PP 速率 $\lambda_1,\lambda_2$; **结论**: 和过程速率 $\lambda_1+\lambda_2$
    + **竞赛假设**: 独立 $X_i\sim\mathrm{Exp}(\lambda_i)$; **结论**: $\min\sim\mathrm{Exp}(\sum\lambda_i)$, $P(X_i=\min)=\lambda_i/\sum\lambda_j$; 两时钟 $P(X_1<X_2)=\lambda_1/(\lambda_1+\lambda_2)$

+ **Conditional arrivals** / **条件到达时刻**:
    + **假设**: 齐次 PP, 条件于 $N(t)=n$
    + **公式**: $(S_1,\ldots,S_n)$ 条件密度 $n!/t^n$ on $0<s_1<\cdots<s_n<t$

+ **NHPP mean** / **非齐次泊松均值**:
    + **假设**: NHPP 强度 $\lambda(\cdot)$, $m(t)=\int_0^t\lambda$
    + **公式**: $N(t)-N(s)\sim\mathrm{Poisson}\bigl(m(t)-m(s)\bigr)$; $EN(t)=\mathrm{Var}(N(t))=m(t)$

---

## 定理

+ **Proposition 1.1.10** / **公理推论**:
    + **假设**: $P$ 满足概率公理
    + **结论**: (i) $P(\emptyset)=0$; (ii) $P(A^c)=1-P(A)$; (iii) $A\subseteq B\Rightarrow P(A)\le P(B)$ (单调性); (iv) 有限互斥族有限可加 $P(\bigcup_{i=1}^n A_i)=\sum_{i=1}^n P(A_i)$

+ **Theorem 1.1.12** / **一般容斥**:
    + **假设**: 事件 $A_1,\ldots,A_n$
    + **结论**:
      $$
      P\Bigl(\bigcup_{i=1}^n A_i\Bigr)
      =\sum_i P(A_i)-\sum_{i<j}P(A_i\cap A_j)+\cdots+(-1)^{n+1}P(A_1\cap\cdots\cap A_n).
      $$

+ **Poisson limit of Binomial** / **二项的泊松极限** (Prop. 2.2.7):
    + **假设**: $X_n\sim\mathrm{Bin}(n,p_n)$, $np_n\to\lambda\in(0,\infty)$
    + **结论**: 对每个固定 $k$, $P(X_n=k)\to e^{-\lambda}\lambda^k/k!$ (即 $X_n\xrightarrow{d}\mathrm{Poisson}(\lambda)$)

+ **MGF uniqueness** / **矩母函数唯一性** (Thm. 2.7.3):
    + **假设**: $M_X,M_Y$ 在含 0 的某开区间上相等 (且有限)
    + **结论**: $X$ 与 $Y$ 同分布

+ **WLLN** / **弱大数定律** (Thm. 2.8.4):
    + **假设**: $X_1,X_2,\ldots$ i.i.d., $EX_i=\mu$, $\mathrm{Var}(X_i)=\sigma^2<\infty$
    + **结论**: $\bar X_n=n^{-1}\sum_{i=1}^n X_i\xrightarrow{P}\mu$

+ **CLT** / **中心极限定理** (Thm. 2.8.7):
    + **假设**: $X_i$ i.i.d., $EX_i=\mu$, $\mathrm{Var}(X_i)=\sigma^2\in(0,\infty)$
    + **结论**: $\dfrac{1}{\sigma\sqrt{n}}\sum_{i=1}^n(X_i-\mu)\xrightarrow{d}N(0,1)$
    + **注**: 课件证明常另设 MGF 在 0 邻域存在; 经典 CLT 本质只需有限方差

+ **Mean-square prediction** / **均方最优预测** (Prop. 3.2.4):
    + **假设**: $E Y^2<\infty$, $h$ 为平方可积的 $X$-可测函数, $m(X)=E[Y|X]$
    + **结论**: $E[(Y-h(X))^2]=E[(Y-m(X))^2]+E[(m(X)-h(X))^2]$, 故 $E[Y|X]$ 最小化均方误差

+ **Law of total expectation** / **全期望定律** (Thm. 3.2.6):
    + **假设**: $E|Y|<\infty$
    + **结论**: $EY=E[E[Y|X]]$

+ **Ergodic MC limit** / **遍历链极限定理** (Thm. 4.6.7):
    + **假设**: 时齐 Markov 链不可约, 正通常返, 非周期 (即遍历)
    + **结论**: 存在唯一平稳分布 $\pi_j>0$, $p_{ij}^{(n)}\to\pi_j$ (与 $i$ 无关), 且 $\pi_j=1/m_j$ ($m_j=E_j T_j^+$)

+ **Finite irreducible MC** / **有限不可约链**:
    + **假设**: 状态空间有限且链不可约
    + **结论**: 全部状态正通常返 (因而存在唯一平稳分布; 再加非周期则遍历)

+ **RW recurrence** / **随机游走常返性**:
    + **1D 最近邻假设**: $\mathbb{Z}$ 上 $p$ 右 $q=1-p$ 左
    + **结论**: 仅 $p=1/2$ 常返 (且为零常返); $p\neq 1/2$ 暂态
    + **简单对称假设**: $d$ 维格点对称游走
    + **结论**: $d=1,2$ 常返; $d\ge 3$ 暂态 (Pólya)

+ **Poisson process equivalence** / **泊松过程两定义等价** (Thm. 5.2.6):
    + **假设**: 计数过程满足定义 A (泊松增量) 或定义 B (无穷小) 之一的全部条件
    + **结论**: 两定义等价 (互相推出)

+ **Interarrival i.i.d. Exp** / **间隔时间为 i.i.d. 指数** (Thm. 5.3.1):
    + **假设**: 齐次 Poisson 过程速率 $\lambda$
    + **结论**: 间隔 $T_1,T_2,\ldots$ i.i.d. $\sim\mathrm{Exp}(\lambda)$

+ **Conditional arrivals = uniform order stats** / **条件到达 = 均匀次序统计** (Thm. 5.6.4):
    + **假设**: 齐次 PP, 条件于 $N(t)=n$
    + **结论**: $(S_1,\ldots,S_n)\stackrel{d}{=}(Y_{(1)},\ldots,Y_{(n)})$, 其中 $Y_i$ i.i.d. $\mathrm{Unif}[0,t]$; 条件密度 $n!/t^n$ on 有序单纯形

---

## 问答沉淀

_(待补充)_
