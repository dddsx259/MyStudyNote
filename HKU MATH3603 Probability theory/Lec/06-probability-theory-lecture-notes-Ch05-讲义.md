# Chapter 5: 泊松过程 (Poisson Processes)

- **来源**: `Lec/01-probability-theory-lecture-notes.pdf` Chapter 5 (p.86–104)
- **课程**: MATH3603, Zhigang Bao
- **前置**: Ch.2 指数/伽马/泊松分布 (Exp/Gamma/Poisson), Ch.3 条件分布 (conditional distribution) 与随机和 (random sum), Ch.4 稀疏 (thinning)/概率生成函数 (PGF) 直觉
- **本章目标**: 齐次泊松过程 (homogeneous Poisson process) 两种定义, 到达/间隔时间 (arrival/interarrival times), 稀疏与叠加 (superposition), 指数竞赛 (exponential race), 条件到达 = 均匀次序统计量 (uniform order statistics), 非齐次强度 (inhomogeneous intensity)
- **说明**: 凡非定义公式均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

---

## 5.1 指数分布 (exponential distribution) 与无记忆性 (memorylessness)

$X\sim\mathrm{Exp}(\lambda)$: $f=\lambda e^{-\lambda x}1_{[0,\infty)}$, $P(X>x)=e^{-\lambda x}$, $EX=1/\lambda$, $\mathrm{Var}=1/\lambda^2$, $M(u)=\lambda/(\lambda-u)$ ($u<\lambda$).

(密度为定义; 以下为直接计算.)

**证明**:
$$P(X>x)=\int_x^\infty\lambda e^{-\lambda t}\,dt=e^{-\lambda x}.$$
$$EX=\int_0^\infty e^{-\lambda x}\,dx=1/\lambda,\quad EX^2=2/\lambda^2\Rightarrow\mathrm{Var}=1/\lambda^2.$$
$$M(u)=E[e^{uX}]=\int_0^\infty\lambda e^{-(\lambda-u)x}\,dx=\lambda/(\lambda-u).$$

**无记忆**: $P(X>s+t\mid X>t)=P(X>s)$.

**证明**:
$$P(X>s+t\mid X>t)=\frac{P(X>s+t)}{P(X>t)}=\frac{e^{-\lambda(s+t)}}{e^{-\lambda t}}=e^{-\lambda s}=P(X>s).$$

等价短时刻画: $P(t<X\le t+h\mid X>t)=\lambda h+o(h)$.

**证明**: $P(X\le t+h\mid X>t)=1-e^{-\lambda h}=\lambda h+o(h)$.

**补充**: 瞬时风险率 (hazard rate) 恒为 $\lambda$; 连续时间"几何等待"的对应物.

---

## 5.2 计数过程 (counting process) 与泊松过程

**计数过程** $N(t)$: 非负整值, 非降, $N(t)-N(s)$ = $(s,t]$ 内事件数.

(定义, 无需证明.)

- **独立增量 (independent increments)**: 不交区间计数独立.
- **平稳增量 (stationary increments)**: $N(t)-N(s)$ 的分布只依赖 $t-s$.

(定义, 无需证明.)

### 定义 A (增量分布)

1. $N(0)=0$;
2. 独立增量;
3. $N(s+t)-N(s)\sim\mathrm{Poisson}(\lambda t)$.

(定义, 无需证明.)

于是 $N(t)\sim\mathrm{Poisson}(\lambda t)$, $EN(t)=\mathrm{Var}(N(t))=\lambda t$.

**证明**: 取 $s=0$ 得 $N(t)\sim\mathrm{Poisson}(\lambda t)$; 泊松均值方差皆为参数 $\lambda t$.

### 定义 B (无穷小)

$N(0)=0$; 平稳独立增量; $P(N(h)=1)=\lambda h+o(h)$; $P(N(h)\ge 2)=o(h)$.

(定义, 无需证明.)

**Thm. 5.2.6**: 两定义等价 (矩母函数 (MGF) / 微分方程论证).

**证明思路** (B$\Rightarrow$A): 令 $p_k(t)=P(N(t)=k)$. 由独立平稳增量与无穷小,
$$p_0(t+h)=p_0(t)(1-\lambda h)+o(h)\Rightarrow p_0'(t)=-\lambda p_0(t),\quad p_0(0)=1\Rightarrow p_0(t)=e^{-\lambda t}.$$
对 $k\ge 1$:
$$p_k(t+h)=p_k(t)(1-\lambda h)+p_{k-1}(t)\lambda h+o(h),$$
得 $p_k'=-\lambda p_k+\lambda p_{k-1}$. 归纳得 $p_k(t)=e^{-\lambda t}(\lambda t)^k/k!$. 或对 MGF $M(t,u)=E[e^{uN(t)}]$ 得 $\partial_t M=\lambda(e^u-1)M$.

(A$\Rightarrow$B): 泊松增量在 $h\to 0$ 时 $P(N(h)=1)=\lambda h e^{-\lambda h}=\lambda h+o(h)$, $P(N(h)\ge 2)=o(h)$.

---

## 5.3 间隔时间与到达时间

$S_n$ = 第 $n$ 次事件时刻, $T_n=S_n-S_{n-1}$, $S_0=0$.

(定义, 无需证明.)

**Thm. 5.3.1**: $T_1,T_2,\ldots$ 独立同分布 (i.i.d.) $\sim\mathrm{Exp}(\lambda)$.

**证明思路**: $P(T_1>t)=P(N(t)=0)=e^{-\lambda t}$. 由独立增量与无记忆 (或强马尔可夫于跳跃时刻), 重启后等待同样 $\mathrm{Exp}(\lambda)$ 且与过去独立. 归纳得全体 i.i.d.

关系: $S_n=T_1+\cdots+T_n$, $N(t)=\sum_{n=1}^\infty 1_{\{S_n\le t\}}$, $EN(t)=\lambda t=t/ET_1$.

**证明**: 前两式由定义. $EN(t)=\lambda t$ 已由泊松边际; $ET_1=1/\lambda$ $\Rightarrow$ $\lambda t=t/ET_1$ (更新报酬直觉: 单位时间事件率 = $1/$平均间隔).

**到达时间**: $S_n\sim\mathrm{Gamma}(n,\lambda)$,
$$f_{S_n}(t)=\frac{\lambda^n}{(n-1)!}t^{n-1}e^{-\lambda t},\quad P(S_n\le t)=P(N(t)\ge n).$$

**证明**: i.i.d. $\mathrm{Exp}(\lambda)$ 之和为 $\mathrm{Gamma}(n,\lambda)$ (形状–速率), 密度即上式 (归纳卷积或 MGF $(\lambda/(\lambda-u))^n$). 事件等价: $\{S_n\le t\}=\{N(t)\ge n\}$.

---

## 5.4 稀疏与叠加

**稀疏**: 每事件独立标为 I (概率 $p$) / II. 则 $N_1,N_2$ 独立, 速率 $\lambda p$ 与 $\lambda(1-p)$.

**证明思路**: 固定区间长度 $t$, $N(t)\sim\mathrm{Poisson}(\lambda t)$, 条件二项分裂 $\Rightarrow$ $N_1(t),N_2(t)$ 独立泊松 (Ch.3/Ch.4 PGF). 对有限多个不交区间, 联合增量仍独立泊松, 故过程级独立. 速率由均值 $\lambda t p$ 读出.

**叠加**: 独立速率 $\lambda_1,\lambda_2$ 的泊松过程之和为速率 $\lambda_1+\lambda_2$; 合并事件来自源 1 的概率 $\lambda_1/(\lambda_1+\lambda_2)$.

**证明**: $N=N_1+N_2$ 独立增量且 $N(t)\sim\mathrm{Poisson}((\lambda_1+\lambda_2)t)$ (独立泊松和). 给定合并点落在 $dt$, 来自源 1 的概率正比于速率:
$$P(\text{类型 1}\mid\text{恰一事件 in }dt)=\frac{\lambda_1 dt}{(\lambda_1+\lambda_2)dt}.$$
等价地, 由指数竞赛 (下节) 或 Ch.3 泊松条件二项.

与 Ch.3 泊松\|和 $\sim$ 二项同一比例.

---

## 5.5 应用

### 优惠券泊松化 (coupon Poissonization)

类型概率 $p_j$; 用速率 1 的地面过程 + 独立类型标记. 分裂后 $M_j$ 独立速率 $p_j$, 首次出现 $X_j\sim\mathrm{Exp}(p_j)$ 独立, 集齐时刻 $X=\max_j X_j$.

$EK=EX=\int_0^\infty\bigl(1-\prod_j(1-e^{-p_j t})\bigr)\,dt$ (随机和 + $ET_1=1$).

**证明思路**: 稀疏得独立 $M_j\sim\mathrm{PP}(p_j)$, 故 $X_j=\inf\{t:M_j(t)\ge 1\}\sim\mathrm{Exp}(p_j)$ 独立. $X=\max_j X_j$ 的尾概率
$$P(X>t)=1-\prod_j(1-e^{-p_j t}),$$
非负 r.v. 期望 $EX=\int_0^\infty P(X>t)\,dt$. 地面过程速率 1 时总到达数 $K$ 满足 $EK=EX$ (瓦尔德 / $EN(X)=EX\cdot 1$).

"恰出现一次"可用第二次到达 $\mathrm{Gamma}(2,p_i)$ 积分表示.

### 指数竞赛

独立 $X_i\sim\mathrm{Exp}(\lambda_i)$:
$$\min_i X_i\sim\mathrm{Exp}\Bigl(\sum_i\lambda_i\Bigr),\qquad P(X_i=\min)=\frac{\lambda_i}{\sum_j\lambda_j}.$$
两时钟: $P(X_1<X_2)=\lambda_1/(\lambda_1+\lambda_2)$.

**证明**: $P(\min>t)=\prod_i P(X_i>t)=e^{-(\sum\lambda_i)t}$. 对两时钟,
$$P(X_1<X_2)=\int_0^\infty\lambda_1 e^{-\lambda_1 x}P(X_2>x)\,dx=\int_0^\infty\lambda_1 e^{-(\lambda_1+\lambda_2)x}\,dx=\frac{\lambda_1}{\lambda_1+\lambda_2}.$$
一般 $i$: 由 $\min_{j\neq i}$ 与 $X_i$ 竞赛, 或对称性.

### 谁先到达目标

独立泊松 $N_1,N_2$; $p=\lambda_1/(\lambda_1+\lambda_2)$. $S_n^{(1)}<S_m^{(2)}$ $\Leftrightarrow$ 前 $n+m-1$ 次合并事件中至少 $n$ 次为类型 1 (二项尾和).

**证明思路**: 合并过程为速率 $\lambda_1+\lambda_2$ 的泊松; 各点独立以概率 $p$ 属类型 1. $\{S_n^{(1)}<S_m^{(2)}\}$ 当且仅当在类型 2 达到 $m$ 次之前类型 1 已达 $n$ 次, 即前 $n+m-1$ 次中类型 1 至少 $n$ 次. 计数 $\sim\mathrm{Bin}(n+m-1,p)$.

---

## 5.6 条件到达时间与次序统计量 (order statistics)

$N(t)=1$ $\Rightarrow$ $S_1\sim\mathrm{Unif}[0,t]$.

**证明**: 对 $0<s<t$,
$$P(S_1\le s\mid N(t)=1)=\frac{P(N(s)=1,N(t)-N(s)=0)}{P(N(t)=1)}=\frac{(\lambda s e^{-\lambda s})e^{-\lambda(t-s)}}{\lambda t e^{-\lambda t}}=\frac{s}{t}.$$

**次序统计量**: i.i.d. 密度 $f$ 的 $Y_{(1)}\le\cdots\le Y_{(n)}$ 联合密度 $=n!\prod f(y_i)$ (有序区域).

**证明**: $n$ 个 i.i.d. 无序样本联合密度 $\prod f(y_i)$; 映射到有序区域有 $n!$ 个排列原像 (连续分布几乎必然无结), 故乘 $n!$.

**Thm. 5.6.4**: 给定 $N(t)=n$,
$$(S_1,\ldots,S_n)\;\stackrel{d}{=}\;(Y_{(1)},\ldots,Y_{(n)}),\quad Y_i\;\mathrm{iid}\;\mathrm{Unif}[0,t],$$
条件密度 $n!/t^n$ on $0<s_1<\cdots<s_n<t$.

**证明思路**: 用间隔表示或直接算联合:
$$P(S_1\in ds_1,\ldots,S_n\in ds_n,N(t)=n)=e^{-\lambda s_1}\lambda\,ds_1\cdots\lambda\,ds_n\,e^{-\lambda(t-s_n)},$$
除以 $P(N(t)=n)=e^{-\lambda t}(\lambda t)^n/n!$, 得条件密度 $n!/t^n$ on 有序单纯形. 此恰为 $n$ 个 $\mathrm{Unif}[0,t]$ 次序统计的联合密度.

给定 $S_n=t$, 前 $n-1$ 个到达 $\stackrel{d}{=}$ $n-1$ 个 $\mathrm{Unif}[0,t]$ 的次序统计.

**证明思路**: 与上类似, 条件于 $S_n=t$ (等价于第 $n$ 次恰在 $t$) 时, 前 $n-1$ 个点在 $[0,t]$ 上均匀无序 (可视为 $n$ 个均匀点中最大为 $t$ 的剩余, 或直接写密度比).

**补充**: 条件于计数, 泊松到达"像均匀撒点再排序".

---

## 5.7 非齐次泊松过程 (inhomogeneous Poisson process)

强度 $\lambda(t)\ge 0$: $N(0)=0$; 独立增量; $P(N(t+h)-N(t)=1)=\lambda(t)h+o(h)$; 多重 $o(h)$.

(定义, 无需证明.)

**均值函数 (mean function)** $m(t)=\int_0^t\lambda(s)\,ds$:
$$N(t)-N(s)\sim\mathrm{Poisson}\bigl(m(t)-m(s)\bigr),\quad EN(t)=\mathrm{Var}(N(t))=m(t).$$

**证明思路**: 与齐次类似, 对 $p_0(t)=P(N(t)=0)$ 得 $p_0'(t)=-\lambda(t)p_0(t)$, 故 $p_0(t)=e^{-m(t)}$. 一般 $k$ 用同样微分方程或时间变换: 令 $\tau=m(t)$, 则 $N(m^{-1}(\tau))$ 为速率 1 的齐次泊松 (在 $m$ 严格增时). 因而增量为 $\mathrm{Poisson}(m(t)-m(s))$.

- 齐次速率 $\Lambda$ 在 $t$ 处以 $p(t)$ 保留 $\Rightarrow$ 强度 $\Lambda p(t)$.

**证明思路**: 无穷小: $P(\text{保留事件 in }dt)=\Lambda\,dt\cdot p(t)+o(dt)$.

- 独立非齐次叠加: 强度相加; 时刻 $t$ 来自 $N$ 的概率 $\lambda(t)/(\lambda(t)+\mu(t))$.

**证明思路**: 无穷小叠加; 条件于 $dt$ 内恰一事件, 类型概率正比于瞬时强度.

- 多类型时间相关分类: 独立非齐次, $\lambda_i(s)=\Lambda p_i(s)$, $E N_i(t)=\Lambda\int_0^t p_i$.

**证明**: 由稀疏/独立标记 + 均值函数 $m_i(t)=\int_0^t\Lambda p_i(s)\,ds$.

例: 热狗摊分段线性强度, 区间积分得泊松均值.

---

## 例题要点

| 主题 | 要点 |
|---|---|
| 两定义互通 | 小 $h$ 泊松展开 $\Leftrightarrow$ 无穷小假设 |
| 移民分类 | 4 周 $\times$ 10 $\times$ 1/12 $\Rightarrow\mathrm{Poisson}(10/3)$ |
| 竞赛 / 目标 | 比率 $\lambda_i/\sum\lambda_j$; 合并伯努利 (Bernoulli) 计数 |
| 条件均匀 | $N(t)=n$ 后到达 = 均匀次序统计 |
| 非齐次均值 | 对 $\lambda$ 积分, 勿误用 $\lambda(t)\cdot(t-s)$ 除非常值 |

---

## 易错点

- $N(t)\sim\mathrm{Poisson}(\lambda t)$ 是边际; 完整过程还需独立增量结构.
- 间隔独立 Exp $\Leftrightarrow$ 齐次泊松; 非齐次间隔一般不 i.i.d. Exp.
- 稀疏独立性是过程级的, 不只是固定 $t$ 的边际.
- 条件到达时间是有序向量; 无序集合对应无序均匀样本.
- 非齐次: $E[N(t)-N(s)]=\int_s^t\lambda$, 不是 $\lambda(t)(t-s)$.

---

## 与前后章关系

- **承 Ch.2**: 指数, 伽马 (gamma), 泊松, MGF; 优惠券收集 (coupon collector) 期望的连续时间版.
- **承 Ch.3**: 条件分布, 随机和 $ES_N=(EN)(EX)$, 密度比思想用于条件到达.
- **承 Ch.4**: 稀疏/叠加与泊松\|和 $\sim$ 二项; PGF 复合和 $\leftrightarrow$ 泊松稀疏.
- **总览**: Ch.1–2 基础分布与极限; Ch.3 条件化与变换; Ch.4 离散时间依赖; Ch.5 连续时间计数的典范模型.
