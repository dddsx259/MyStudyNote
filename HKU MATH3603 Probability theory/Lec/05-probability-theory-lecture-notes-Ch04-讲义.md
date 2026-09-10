# Chapter 4: 离散时间马尔可夫链 (Discrete-Time Markov Chains)

- **来源**: `Lec/01-probability-theory-lecture-notes.pdf` Chapter 4 (p.57–85)
- **课程**: MATH3603, Zhigang Bao
- **前置**: Ch.2–3 条件概率 (conditional probability)/期望 (expectation), 生成函数预备
- **本章目标**: 离散时间马尔可夫链: 转移矩阵 (transition matrix), 互通类 (communicating class), 常返/暂态 (recurrent/transient), 平稳与极限分布 (stationary/limiting distribution), 赌徒破产 (gambler's ruin), 基本矩阵 (fundamental matrix), 高尔顿–沃森过程 (Galton–Watson) 与概率生成函数 (PGF, probability generating function)
- **说明**: 凡非定义公式均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

---

## 4.1 随机过程 (stochastic process) 与马尔可夫性 (Markov property)

**随机过程**: $\{X_t:t\in T\}$, $X_t:\Omega\to S$. 本章: 离散时间 $T=\mathbb{N}_0$, 离散状态 $S$ 有限或可数.

(定义, 无需证明.)

**马尔可夫链 (Markov chain)**: 已知现在, 过去对下一步无关:
$$P(X_{n+1}=j\mid X_n=i,X_{n-1},\ldots,X_0)=P(X_{n+1}=j\mid X_n=i).$$

(定义, 无需证明.)

**时齐 (time-homogeneous)**: $p_{ij}:=P(X_{n+1}=j\mid X_n=i)$ 与 $n$ 无关. 本章默认时齐.

(定义, 无需证明.)

**例**: 一般随机游走 (random walk) $p_{ij}=q(j-i)$; 分支过程 (branching process) (0 吸收); 埃伦费斯特链 (Ehrenfest chain) $p_{k,k+1}=(r-k)/r$, $p_{k,k-1}=k/r$.

**补充直觉**: 马尔可夫 = "无记忆于路径", 状态已概括预测下一步所需信息.

---

## 4.2 转移矩阵与多步转移

行随机 (row-stochastic): $p_{ij}\ge 0$, $\sum_j p_{ij}=1$. 有限 $S$ 时 $P=(p_{ij})$ 为转移矩阵.

(定义, 无需证明.)

**$n$ 步**: $p_{ij}^{(n)}=P(X_{m+n}=j\mid X_m=i)$, $p_{ij}^{(0)}=1_{\{i=j\}}$.

(定义, 无需证明.)

**查普曼–柯尔莫哥洛夫方程 (Chapman–Kolmogorov)**:
$$p_{ij}^{(m+n)}=\sum_k p_{ik}^{(m)}p_{kj}^{(n)}\quad\Leftrightarrow\quad P^{m+n}=P^m P^n.$$

**证明**: 由全概率与马尔可夫性 (时齐),
\begin{align*}
p_{ij}^{(m+n)}
&=P(X_{m+n}=j\mid X_0=i)
=\sum_k P(X_m=k\mid X_0=i)\,P(X_{m+n}=j\mid X_m=k)\\
&=\sum_k p_{ik}^{(m)}p_{kj}^{(n)}.
\end{align*}
矩阵形式即 $P^{m+n}=P^m P^n$.

分布演化: 行向量 $\mu_n$, $\mu_{n+1}=\mu_n P$, $\mu_n=\mu_0 P^n$.

**证明**: $(\mu_{n+1})_j=\sum_i P(X_n=i)p_{ij}=(\mu_n P)_j$. 迭代得 $\mu_n=\mu_0 P^n$.

边界例: $Z$ 上最近邻游走; $\{0,\ldots,N\}$ 吸收边界 (赌徒破产).

---

## 4.3 互通类与不可约 (irreducible)

- $i\to j$: 存在 $n\ge 0$ 使 $p_{ij}^{(n)}>0$.
- $i\leftrightarrow j$: 双向可达. **等价关系**, 划分互通类.
- **不可约**: 整个状态空间是一个互通类.

(定义, 无需证明. $\leftrightarrow$ 的自反/对称显然; 传递性: $i\to j\to k$ 则存在路径拼接, 故 $i\to k$.)

---

## 4.4 常返与暂态

$T_j^+=\inf\{n\ge 1:X_n=j\}$, $f_{ij}=P_i(T_j^+<\infty)$.

- **常返**: $f_{ii}=1$; **暂态**: $f_{ii}<1$.

(定义, 无需证明.)

访问次数 $N_j=\sum_{n=0}^\infty 1_{\{X_n=j\}}$. 暂态自 $j$ 出发: $E_j N_j=1/(1-f_{jj})<\infty$.

**证明**: 自 $j$ 出发, 每次离开后再返回的概率为 $f_{jj}$; 访问次数服从几何分布 (含首次在 $0$ 的停留): $P_j(N_j=k)=f_{jj}^{k-1}(1-f_{jj})$ ($k\ge 1$). 故
$$E_j N_j=\frac{1}{1-f_{jj}}.$$
暂态 $f_{jj}<1$ $\Rightarrow$ 有限.

**判据**: $i$ 常返 $\Leftrightarrow$ $\sum_n p_{ii}^{(n)}=\infty$.

**证明思路**: 由单调收敛 / Fubini,
$$E_i N_i=\sum_{n=0}^\infty p_{ii}^{(n)}.$$
又 $E_i N_i=1/(1-f_{ii})$ (上式对常返形式化为 $\infty$). 故 $f_{ii}=1$ $\Leftrightarrow$ $E_i N_i=\infty$ $\Leftrightarrow$ $\sum_n p_{ii}^{(n)}=\infty$.

**类性质**: 互通 $\Rightarrow$ 同为常返或同为暂态. 常返类不可"单向逃出".

**证明思路**: 设 $i\leftrightarrow j$, $i$ 常返. 存在 $r,s$ 使 $p_{ij}^{(r)}>0$, $p_{ji}^{(s)}>0$. 则
$$\sum_n p_{jj}^{(n)}\ge\sum_n p_{ji}^{(s)}p_{ii}^{(n)}p_{ij}^{(r)}=p_{ji}^{(s)}p_{ij}^{(r)}\sum_n p_{ii}^{(n)}=\infty,$$
故 $j$ 常返. 若常返类可逃到类外, 返回概率 $<1$, 矛盾.

---

## 4.5 随机游走常返性

$Z$ 上最近邻, $p$ 右 $q=1-p$ 左:
$$p_{00}^{(2n)}=\binom{2n}{n}p^n q^n\sim\frac{[4pq]^n}{\sqrt{\pi n}}.$$

**证明思路**: 回到 $0$ 须偶数步且恰 $n$ 右 $n$ 左, 故二项式. Stirling $n!\sim\sqrt{2\pi n}(n/e)^n$ 得渐近.

- $p=1/2$: 常返; $p\neq 1/2$: 暂态.

**证明**: $4pq=4p(1-p)\le 1$, 等号当且仅当 $p=1/2$. 故 $p=1/2$ 时 $p_{00}^{(2n)}\sim 1/\sqrt{\pi n}$, $\sum_n p_{00}^{(2n)}=\infty$ (与 $p$-级数同类); $p\neq 1/2$ 时 $4pq<1$, 几何衰减, $\sum<\infty$ $\Rightarrow$ 暂态.

- 简单对称游走 (simple symmetric random walk): $d=1,2$ 常返; $d\ge 3$ 暂态.

**证明思路**: $d$ 维回到原点概率 $\sim c_d\,n^{-d/2}$; $\sum n^{-d/2}$ 在 $d=1,2$ 发散, $d\ge 3$ 收敛 (Polya 定理).

- **有限不可约链**: 全部常返 (且正通常返 (positive recurrent)).

**证明思路**: 有限态空间上若存在暂态, 则逃出暂态类后几乎必然不再返回, 与不可约 (唯一类) 矛盾. 有限常返 $\Rightarrow$ 平均返回时间有限 $\Rightarrow$ 正通常返.

---

## 4.6 平稳分布与极限分布

**平稳分布** $\pi$: $\pi=\pi P$, $\pi_j\ge 0$, $\sum\pi_j=1$. 若 $X_0\sim\pi$ 则一切 $X_n\sim\pi$.

(定义; 后半由 $\mu_n=\mu_0 P^n$ 直接得.)

**极限分布**: $\lim_n p_{ij}^{(n)}=\pi_j$ (与起点无关). 存在极限 $\Rightarrow$ 极限必平稳; 反之未必 ($P$ 可有平稳但不收敛).

**证明** (极限 $\Rightarrow$ 平稳): 设 $\lim_n p_{ij}^{(n)}=\pi_j$. 则
$$\pi_j=\lim_n p_{ij}^{(n+1)}=\lim_n\sum_k p_{ik}^{(n)}p_{kj}=\sum_k\pi_k p_{kj},$$
(有限态可交换极限与和; 可数态需额外控制.) 且 $\sum_j\pi_j=1$.

### 收敛的两大障碍

1. **可约 (reducible)**: 极限可依赖起始闭类.
2. **周期 (periodicity)**: 例 $P=\begin{pmatrix}0&1\\1&0\end{pmatrix}$ 振荡; $\pi=(1/2,1/2)$ 仍平稳.

**周期** $d(i)=\gcd\{n\ge 1:p_{ii}^{(n)}>0\}$; $d=1$ 为非周期 (aperiodic). 周期是类性质.

(定义, 无需证明. 类性质: 互通态有相同 gcd.)

**正通常返 / 零常返 (null recurrent)**: 常返且 $m_i=E_i T_i^+<\infty$ / $=\infty$. 正通常返是类性质; 有限常返态必正通常返.

(定义, 无需证明.)

**遍历 (ergodic)**: 不可约 + 正通常返 + 非周期.

(定义, 无需证明.)

**收敛定理** (Thm. 4.6.7): 遍历 $\Rightarrow$ 唯一平稳 $\pi_j>0$, $p_{ij}^{(n)}\to\pi_j$, 且 $\pi_j=1/m_j$.

**证明思路**:
1. 正通常返不可约 $\Rightarrow$ 存在唯一概率平稳 $\pi$, 且 $\pi_j=1/m_j>0$ (再生论 / 平均返回时间倒数).
2. 非周期 $\Rightarrow$ 返回时间的支撑生成 $\mathbb{Z}_+$, 由耦合或更新理论得 $p_{ij}^{(n)}\to\pi_j$.
3. 唯一性: 任意平稳必等于极限分布.

**遍历平均 (ergodic average)**: $\frac1N\sum_{n=1}^N r(X_n)\to\sum_j r(j)\pi_j$ a.s. (有界 $r$).

**证明思路**: 不可约正通常返时, 按返回时间分块 (循环引理 / 强大数律于 i.i.d. 循环奖赏), 得时间平均 $\to$ 平稳平均. 非周期非必需于此结论.

两状态手机模型: $\pi_0=\beta/(\beta+1-\alpha)$, $\pi_1=(1-\alpha)/(\beta+1-\alpha)$.

**证明**: $P=\begin{pmatrix}\alpha&1-\alpha\\\beta&1-\beta\end{pmatrix}$, 解 $\pi=\pi P$ 与 $\pi_0+\pi_1=1$:
$$\pi_0=\pi_0\alpha+\pi_1\beta,\quad\Rightarrow\quad\pi_0(1-\alpha)=\pi_1\beta.$$
代入归一化即得上式.

---

## 4.7 赌徒破产

状态 $\{0,\ldots,N\}$, 内部 $p$ 上 $q$ 下, $0,N$ 吸收 (absorbing). $1,\ldots,N-1$ 暂态; 几乎必然吸收.

$u_i=P_i(\text{先达 }N\text{ 再达 }0)$:
$$u_i=\begin{cases}
\dfrac{1-(q/p)^i}{1-(q/p)^N}, & p\neq q,\\[0.6em]
i/N, & p=q=1/2.
\end{cases}$$

**证明**: 首步分析: $u_0=0$, $u_N=1$, 且对 $1\le i\le N-1$,
$$u_i=p\,u_{i+1}+q\,u_{i-1}.$$
整理得 $p(u_{i+1}-u_i)=q(u_i-u_{i-1})$. 令 $\delta_i=u_i-u_{i-1}$, 则 $\delta_{i+1}=(q/p)\delta_i$.
- $p\neq q$: $\delta_i=\delta_1(q/p)^{i-1}$, $u_i=\delta_1\sum_{k=0}^{i-1}(q/p)^k=\delta_1\frac{1-(q/p)^i}{1-q/p}$. 由 $u_N=1$ 定 $\delta_1$.
- $p=q$: $\delta_i$ 常数, $u_i=i/N$.

几乎必然吸收: 暂态有限, 或用 $u_i+(1-u_i)=1$ 为达 $\{0,N\}$ 的概率.

$N\to\infty$, 固定 $i$: $p>1/2$ 时极限 $1-(q/p)^i$; $p\le 1/2$ 时极限 $0$ (公平/不利必破产).

**证明**: $p>1/2$ $\Rightarrow$ $q/p<1$, $N\to\infty$ 分母 $\to 1$, 极限 $1-(q/p)^i$. $p\le 1/2$ $\Rightarrow$ $q/p\ge 1$, 分子分母同阶 $\to 0$ (或公平时 $i/N\to 0$).

---

## 4.8 暂态占用时间 (transient occupation time)

$T$ = 全部暂态态, $Q=(p_{ij})_{i,j\in T}$.

$g_{ij}=E_i\sum_{n=0}^\infty 1_{\{X_n=j\}}$, $G_T=(g_{ij})$.

**基本矩阵**: $G_T=(I-Q)^{-1}=\sum_{n=0}^\infty Q^n$.

**证明思路**: $(Q^n)_{ij}=P_i(X_n=j,\,n$ 步内仍在 $T)$. 于是
$$g_{ij}=\sum_{n=0}^\infty (Q^n)_{ij}.$$
暂态类上谱半径 $<1$ (或有限暂态), 故 Neumann 级数 $\sum Q^n=(I-Q)^{-1}$.

到达概率 (hitting probability): $f_{ij}=(g_{ij}-\delta_{ij})/g_{jj}$.

**证明思路**: $g_{jj}=E_j N_j=1/(1-f_{jj})$; 自 $i$ 出发首次击中 $j$ 后, 此后占用与自 $j$ 出发同分布. 更精细地: $g_{ij}=f_{ij}g_{jj}+\delta_{ij}$ (是否从 $i=j$ 计初始), 整理得 $f_{ij}=(g_{ij}-\delta_{ij})/g_{jj}$.

---

## 4.9–4.11 高尔顿–沃森过程与概率生成函数 (PGF)

$Z_0=1$, $Z_n=\sum_{i=1}^{Z_{n-1}}\xi_{n,i}$, 子代独立同分布 (i.i.d.), $p_0>0$, 非退化. 0 吸收常返; $i\ge 1$ 暂态.

$\mu=E\xi$, $\sigma^2=\mathrm{Var}(\xi)$: $EZ_n=\mu^n$;
$$\mathrm{Var}(Z_n)=\begin{cases}
\sigma^2\mu^{n-1}\dfrac{1-\mu^n}{1-\mu}, & \mu\neq 1,\\
n\sigma^2, & \mu=1.
\end{cases}$$

**证明**: 条件于 $Z_{n-1}$, $E[Z_n\mid Z_{n-1}]=Z_{n-1}\mu$, 故 $EZ_n=\mu\,EZ_{n-1}=\mu^n$.
方差: 条件方差公式
$$\mathrm{Var}(Z_n)=E[\mathrm{Var}(Z_n\mid Z_{n-1})]+\mathrm{Var}(E[Z_n\mid Z_{n-1}])=E[Z_{n-1}\sigma^2]+\mathrm{Var}(Z_{n-1}\mu)$$
$$=\sigma^2\mu^{n-1}+\mu^2\mathrm{Var}(Z_{n-1}).$$
递推求解即得两种情形.

### 概率生成函数

$G_X(s)=E[s^X]=\sum p_X(k)s^k$. $EX=G'(1-)$; 阶乘矩 (factorial moment) 由高阶导; 独立和 PGF 相乘.

(定义 $G_X$; 以下为性质.)

**证明**: $G'(s)=\sum k p_k s^{k-1}$, 故 $G'(1-)=EX$ (若 $EX<\infty$). 独立 $X\perp Y$ $\Rightarrow$ $E[s^{X+Y}]=E[s^X]E[s^Y]$.

**复合和 (compound sum)**: $S_N=\sum_{i=1}^N Y_i$ $\Rightarrow$ $G_{S_N}(s)=G_N(G_Y(s))$. 泊松稀疏 (Poisson thinning) $\Rightarrow\mathrm{Poisson}(\lambda p)$.

**证明**: $E[s^{S_N}\mid N]=G_Y(s)^N$, 故 $G_{S_N}(s)=E[G_Y(s)^N]=G_N(G_Y(s))$.
泊松稀疏: $N\sim\mathrm{Poisson}(\lambda)$, 每点保留概率 $p$ 独立 $\Leftrightarrow$ $G_N(1-p+ps)=e^{\lambda p(s-1)}$, 即 $\mathrm{Poisson}(\lambda p)$.

### 灭绝概率 (extinction probability)

子代 PGF $G$, $G_n=G^{\circ n}$, $\eta_n=G_n(0)\uparrow\eta$. **$\eta$ = $[0,1]$ 上 $s=G(s)$ 的最小解**.

| 情形 | $\eta$ |
|---|---|
| $\mu<1$ | $1$ |
| $\mu>1$ | $<1$ |
| $\mu=1$, $\sigma^2>0$ | $1$ |
| $\mu=1$, $\sigma^2=0$ ($\xi\equiv 1$) | $0$ |

**证明思路**: $\eta_n=P(Z_n=0)$ 递增有界, 极限 $\eta$ 满足 $\eta=G(\eta)$. 任意不动点 $\zeta$ 有 $\eta_n\le\zeta$ (归纳), 故 $\eta$ 最小.
- $\mu=G'(1)<1$: $G(s)>s$ 在 $[0,1)$ (凸性), 唯一不动点为 $1$.
- $\mu>1$: 另有唯一 $\eta\in[0,1)$; $G(0)=p_0>0$ 保证 $\eta\ge p_0$.
- $\mu=1$, 非退化: $G(s)>s$ on $[0,1)$ $\Rightarrow$ 唯一不动点 $1$.
- $\xi\equiv 1$: $G(s)=s$, $\eta_n=0$.

---

## 4.12 返回时间生成函数与零常返

一维最近邻游走: $P_0(s)=\sum p_{00}^{(n)}s^n=1/\sqrt{1-4pqs^2}$, $F_0(s)=1-\sqrt{1-4pqs^2}$.

**证明思路**: 用首达分解 $P_0(s)=1/(1-F_0(s))$ (标准生成函数恒等式). 组合计数或反射原理给出闭式; 或由 $p_{00}^{(2n)}=\binom{2n}{n}p^n q^n$ 的常生成函数 $\sum\binom{2n}{n}(pqs^2)^n=1/\sqrt{1-4pqs^2}$.

$P(T_0^+<\infty)=F_0(1-)=1-|p-q|$. 对称时必返回, 但 $E_0 T_0^+=\infty$ $\Rightarrow$ **零常返**.

**证明**: $F_0(1-)=\lim_{s\uparrow 1}F_0(s)=1-|p-q|$. $p=q=1/2$ 时 $F_0(1-)=1$, 但 $F_0'(1-)=\infty$ (或由 $p_{00}^{(2n)}\sim n^{-1/2}$ 知平均返回时间发散) $\Rightarrow$ 零常返.

---

## 例题要点

1. 手机两状态: 算 $P^n$, 解 $\pi=\pi P$, 对照数值收敛.
2. 赌徒破产: 首步分析 (first-step analysis) 差分方程 + 边界.
3. 基本矩阵: $G_T=(I-Q)^{-1}$ 读期望占用.
4. 分支过程: 画 $y=G(s)$ 与 $y=s$ 交点判 $\eta$.

---

## 易错点

- $p_{ij}^{(n)}$ 上标是步数, 不是标量幂.
- 不可约不足以保证 $P^n$ 收敛 (还需非周期 + 正通常返).
- 常返 $\neq$ 正通常返 (对称 1D 游走).
- 平稳存在 $\neq$ 极限存在 (周期链).
- 分支过程: 临界 (critical) $\mu=1$ (非退化) 仍几乎必然灭绝.
- PGF 在 $s=1$ 取左极限求矩时注意矩是否有限.

---

## 与前后章关系

- **承 Ch.1–3**: 条件概率即一步转移; 全期望/条件期望解吸收概率与均值; 独立和与复合和用 PGF.
- **承 Ch.2**: 泊松 / 伯努利稀疏与矩母函数 (MGF) 平行于 PGF.
- **启 Ch.5**: 连续时间计数过程; 泊松过程 (Poisson process) 增量独立类似"无记忆跳跃", 但时间连续. 分支与稀疏在泊松化 (Poissonization) 中再现.
