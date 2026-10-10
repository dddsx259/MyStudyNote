# 题集 — Ch02 Random Variables & Limit Theorems

> 对齐: `Lec/Lec02 probability theory lecture notes Ch02 讲义.md`.
> 含: (1) 练习题 (2) 课件证明.

## 课件证明

### P1. CDF 性质 (Prop. 2.1.7)

- **陈述**: **假设** $F(x)=P(X\le x)$; **结论** $F$ 非降, 右连续, $\lim_{x\to-\infty}F=0$, $\lim_{x\to\infty}F=1$, 且 $P(X=x)=F(x)-F(x-)$.
- **证明**: 非降由事件包含; 右连续/极限用概率连续性 ($A_n\downarrow A\Rightarrow P(A_n)\to P(A)$, 对补集得递增情形); 跳跃 $P(X\le x)-P(X<x)$.
- **来源**: `Lec/Lec02 probability theory lecture notes Ch02 讲义.md` §2.1

### P2. 区间概率 via CDF

- **陈述**: **结论** $P(a<X\le b)=F(b)-F(a)$, $P(a\le X\le b)=F(b)-F(a-)$.
- **证明**: 事件差分解 $\{X\le b\}\setminus\{X\le a\}$ 或 $\{X\le b\}\setminus\{X<a\}$.
- **来源**: 同上 §2.1

### P3. PMF 归一化与 CDF 表示

- **陈述**: **假设** 离散 $X$; **结论** $\sum_x p_X(x)=1$, $F(b)=\sum_{x\le b}p_X(x)$.
- **证明**: 值点互斥且覆盖值域, 可数可加; $\{X\le b\}$ 为互斥并 $\bigcup_{x\le b}\{X=x\}$.
- **来源**: 同上 §2.1

### P4. 泊松逼近二项 (Prop. 2.2.7)

- **陈述**: **假设** $X_n\sim\mathrm{Bin}(n,p_n)$, $np_n\to\lambda$; **结论** $P(X_n=k)\to e^{-\lambda}\lambda^k/k!$.
- **证明**: 展开 $\binom{n}{k}p_n^k(1-p_n)^{n-k}$, 因子 $(np_n)^k\to\lambda^k$, $(1-p_n)^n\to e^{-\lambda}$, $\prod_{j<k}(1-j/n)\to1$.
- **来源**: 同上 §2.2

### P5. PDF 与区间概率

- **陈述**: **假设** $F(x)=\int_{-\infty}^x f(u)\,du$; **结论** $P(a<X\le b)=\int_a^b f(x)\,dx$.
- **证明**: $F(b)-F(a)=\int_{-\infty}^b f-\int_{-\infty}^a f$ (微积分基本定理).
- **来源**: 同上 §2.3

### P6. 逆变换采样 (Inverse transform sampling)

- **陈述**: **假设** $U\sim\mathrm{Unif}[0,1]$, $F$ 连续严格增, $X=F^{-1}(U)$; **结论** $X$ 的 CDF 为 $F$.
- **证明**: $P(X\le x)=P(U\le F(x))=F(x)$.
- **来源**: 同上 §2.3

### P7. 指数无记忆性 (Memorylessness)

- **陈述**: **假设** $X\sim\mathrm{Exp}(\lambda)$; **结论** $P(X>s+t\mid X>s)=P(X>t)$.
- **证明**: 比值为 $e^{-\lambda(s+t)}/e^{-\lambda s}=e^{-\lambda t}$.
- **来源**: 同上 §2.3

### P8. 方差恒等式与仿射

- **陈述**: **结论** $\mathrm{Var}(X)=E[X^2]-(EX)^2$, $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$.
- **证明**: 展开 $E[(X-\mu)^2]$; 仿射时 $(aX+b-a\mu-b)^2=a^2(X-\mu)^2$.
- **来源**: 同上 §2.4

### P8b. 指示变量和的方差用二阶矩 (自拟) (variance of an indicator sum via the second moment)

- **陈述**: **假设** $I_j\in\{0,1\}$, $S=\sum_j I_j$; **结论** $E[S^2]=\sum_j E[I_j]+\sum_{j\neq k}E[I_j I_k]$. 若 $E[I_j I_k]=E[I_j]E[I_k]$ ($j\neq k$), 则 $\mathrm{Var}(S)=\sum_j p_j(1-p_j)$, $p_j=E[I_j]$.
- **证明**: $I_j^2=I_j$, 展开 $E[S^2]$. 乘积期望可拆时, $\sum_{j\neq k}p_j p_k=(\sum p_j)^2-\sum p_j^2$, 与 $(ES)^2$ 相消后剩下 $\sum p_j(1-p_j)$.
- **来源**: `Lec/Lec02 probability theory lecture notes Ch02 讲义.md` §2.5

### P9. 独立 $\Rightarrow$ $E[g(X)h(Y)]$ 分解

- **陈述**: **假设** $X\perp\!\!\!\perp Y$; **结论** $E[g(X)h(Y)]=E[g(X)]E[h(Y)]$.
- **证明**: 离散: $\sum_{x,y}g(x)h(y)p_X(x)p_Y(y)$ 分离为两乘积; 连续用 Fubini 同理.
- **来源**: 同上 §2.6

### P10. 协方差恒等式

- **陈述**: **结论** $\mathrm{Cov}(X,Y)=E[XY]-EX\,EY$.
- **证明**: 展开 $E[(X-\mu)(Y-\nu)]$, 交叉项 $E[XY]-\mu EY-\nu EX+\mu\nu$.
- **来源**: 同上 §2.6

### P11. 方差和公式

- **陈述**: **结论** $\mathrm{Var}(\sum_i X_i)=\sum_i\mathrm{Var}(X_i)+2\sum_{i<j}\mathrm{Cov}(X_i,X_j)$.
- **证明**: 展开 $E[(\sum_i(X_i-\mu_i))^2]$, 对角为方差, 非对角为协方差.
- **来源**: 同上 §2.6

### P12. 离散卷积 (Convolution, discrete)

- **陈述**: **假设** $X\perp\!\!\!\perp Y$ 离散; **结论** $p_{X+Y}(z)=\sum_x p_X(x)p_Y(z-x)$.
- **证明**: $P(X+Y=z)=\sum_x P(X=x,Y=z-x)=\sum_x p_X(x)p_Y(z-x)$.
- **来源**: 同上 §2.6

### P13. 独立和的 MGF

- **陈述**: **假设** $X\perp\!\!\!\perp Y$, MGF 存在; **结论** $M_{X+Y}(t)=M_X(t)M_Y(t)$.
- **证明**: $E[e^{t(X+Y)}]=E[e^{tX}]E[e^{tY}]$.
- **来源**: 同上 §2.7

### P14. 泊松/正态独立和 (MGF)

- **陈述**: **假设** 独立 $X\sim\mathrm{Poisson}(\lambda)$, $Y\sim\mathrm{Poisson}(\mu)$; **结论** $X+Y\sim\mathrm{Poisson}(\lambda+\mu)$. (正态: MGF 相乘仍为正态 MGF.)
- **证明**: $M_{X+Y}(t)=\exp\{(\lambda+\mu)(e^t-1)\}$, 由 MGF 识别 (本课工具).
- **来源**: 同上 §2.7

### P15. 马尔可夫不等式 (Markov's inequality)

- **陈述**: **假设** $X\ge0$, $a>0$; **结论** $P(X\ge a)\le EX/a$.
- **证明**: $X\ge a\cdot 1_{\{X\ge a\}}$, 取期望.
- **来源**: 同上 §2.8

### P16. 切比雪夫不等式 (Chebyshev's inequality)

- **陈述**: **假设** $EX=\mu$; **结论** $P(|X-\mu|\ge a)\le\mathrm{Var}(X)/a^2$.
- **证明**: 对 $Y=(X-\mu)^2\ge0$ 用马尔可夫, 阈值 $a^2$.
- **来源**: 同上 §2.8

### P17. 弱大数定律 (WLLN)

- **陈述**: **假设** i.i.d., $EX=\mu$, $\mathrm{Var}(X)=\sigma^2<\infty$; **结论** $\bar X_n\xrightarrow{P}\mu$.
- **证明**: $\mathrm{Var}(\bar X_n)=\sigma^2/n$, 切比雪夫得 $P(|\bar X_n-\mu|\ge\varepsilon)\le\sigma^2/(n\varepsilon^2)\to0$.
- **来源**: 同上 §2.8

### P18. 中心极限定理 (CLT, MGF 版)

- **陈述**: **假设** i.i.d., 均值 $\mu$, 方差 $\sigma^2\in(0,\infty)$, MGF 在 0 邻域存在; **结论** $\dfrac{1}{\sigma\sqrt{n}}\sum_{i=1}^n(X_i-\mu)\xrightarrow{d}N(0,1)$.
- **证明**: 标准化 $Y_i=(X_i-\mu)/\sigma$, $M_{S_n/\sqrt{n}}(t)=[M_Y(t/\sqrt{n})]^n$. Taylor: $M_Y(u)=1+u^2/2+o(u^2)$, 故 $[1+t^2/(2n)+o(n^{-1})]^n\to e^{t^2/2}$, 即标准正态 MGF.
- **来源**: 同上 §2.8

### P19. MGF 唯一决定分布 (工具性)

- **陈述**: MGF 在含 0 的开区间上相同 $\Rightarrow$ 同分布.
- **证明**: 超出本课已授范围; 讲义仅陈述 (特征函数 / Lévy 唯一性). 本课作识别分布工具.
- **来源**: 同上 §2.7

## 练习题

### 1. 两枚硬币头数 CDF

- **题目**: 两枚公平硬币, 正面数 $X$ 的 CDF (右连续).
- **思路**: $P(X=k)$ 为 $1/4,1/2,1/4$; 阶梯函数跳跃为点质量.
- **来源**: Lec Ch02 例题要点

### 2. 优惠券 — 种类数期望

- **题目**: $N$ 种卡, i.i.d. 均匀抽. $n$ 次后不同种类数期望.
- **思路**: 指示 $I_j$, $E[\sum I_j]=N(1-(1-1/N)^n)$.
- **来源**: Lec Ch02 coupon collector

### 3. 优惠券 — 集齐时间

- **题目**: 集齐 $N$ 种等待 $T$ 的期望.
- **思路**: $T_j\sim\mathrm{Geom}((N-j+1)/N)$; $ET=N\sum_{j=1}^N 1/j$.
- **来源**: Lec Ch02 coupon collector

### 4. 两 Unif[0,1] 之和

- **题目**: $X,Y$ i.i.d. $\mathrm{Unif}[0,1]$, 求 $X+Y$ 的 PDF.
- **思路**: 卷积; 三角密度 $z$ 与 $2-z$ 在 $[0,2]$.
- **来源**: Lec Ch02 例题要点

### 5. MGF 与泊松/正态可加

- **题目**: 用 MGF 说明独立泊松参数可加, 独立正态和仍正态.
- **思路**: $M_{X+Y}=M_X M_Y$; 识别指数型.
- **来源**: Lec Ch02 例题要点

### 6. 正反面差 PMF (HW2 Q1)

- **题目**: $X=\#$heads $-\#$tails, $n$ 次抛; $n=3$ 公平币 PMF.
- **思路**: $X=2H-n$; $H\sim\mathrm{Bin}(n,1/2)$.
- **来源**: HW2 Q1 / `assignment/Homework02 解答.md`

### 7. 二次密度归一化 (HW2 Q2)

- **题目**: $f=c(4x-2x^2)$ on $(0,2)$; 求 $c$, $P(1/2<X<3/2)$, $EX$, $\mathrm{Var}$.
- **思路**: 积分归一; $E(X^2)-(EX)^2$.
- **来源**: HW2 Q2

### 8. max / min 的 CDF (HW2 Q3)

- **题目**: i.i.d. 共同 $F$, 求 $F_{\max}$, $F_{\min}$.
- **思路**: $F^n$; $1-(1-F)^n$.
- **来源**: HW2 Q3

### 9. 不同生日个数 (HW2 Q4)

- **题目**: 100 人 / 365 天, $X=$ 不同生日数; $EX$, $\mathrm{Var}(X)$.
- **思路**: $X=\sum I_j$; $p=1-(364/365)^{100}$; 协方差用 $P(I_j=I_k=1)$.
- **来源**: HW2 Q4

### 10. 单位圆盘均匀 (HW2 Q5)

- **题目**: 求 $C$ 与边缘 $f_X$.
- **思路**: $C=1/\pi$; $f_X(x)=2\sqrt{1-x^2}/\pi$ ($|x|\le 1$).
- **来源**: HW2 Q5

### 11. 四发 vs 两发飞机 (Tut3 Q1)

- **题目**: 何时四发优于两发.
- **思路**: Binomial 尾概率; 化简得 $p\ge 2/3$.
- **来源**: Tut3 / `tut/Tut03 总结.md`

### 12. 负二项 PMF (Tut3 Q2)

- **题目**: 推导 $P(X=n)=\binom{n-1}{r-1}p^r(1-p)^{n-r}$.
- **思路**: 前 $n-1$ 次恰 $r-1$ 正面 + 第 $n$ 次正面.
- **来源**: Tut3 Q2

### 13. Coupon 等待 $P(X>n)$ (Tut3 Q3)

- **题目**: $m$ 类结果, 容斥写 $P(X>n)$, $P(X=n)$.
- **思路**: $A_i$ 未出现 $i$; HW1 容斥.
- **来源**: Tut3 Q3

### 14. Geom / Exp 无记忆 (Tut3 Q4)

- **题目**: 证 memoryless.
- **思路**: 条件概率比; Exp 用生存函数 $e^{-\lambda x}$.
- **来源**: Tut3 Q4

### 15. 密度混合与乘积 (Tut4 Q1)

- **题目**: $\lambda f+(1-\lambda)g$ 是否密度? $fg$?
- **思路**: 混合是; 乘积一般否 (需归一化).
- **来源**: Tut4 / `tut/Tut04 总结.md`

### 16. 常见分布矩 (Tut4 Q2)

- **题目**: Geom / NB / Poisson / Unif / Exp / Gamma 的 $E$, $\mathrm{Var}$.
- **思路**: 见 Tut4 总结表; 注意 Geom 支撑约定.
- **来源**: Tut4 Q2

### 17. 逆变换采样一般情形 (Tut4 Q3)

- **题目**: $F^{-1}(U)\stackrel{d}{=}X$, $F^{-1}(u)=\inf\{x:F(x)\ge u\}$.
- **思路**: $F^{-1}(u)\le x\iff u\le F(x)$.
- **来源**: Tut4 Q3


### 18. Tut5 Q1 — 联合质量 / $U=X+Y$ / $V=X-Y$

- **题目**: $f(x,y)=C/[(x+y-1)(x+y)(x+y+1)]$; 求 $C$, $U$, $V$ 的 PMF.
- **思路**: 按 $u=x+y$ 切片 + 部分分式; $C=2$, $P(U=u)=2/(u(u+1))$.
- **来源**: `tut/Tut05`

### 19. Tut5 Q2–Q4 — max/min; $XY$ 与 $Z^2$; 正态和差独立

- **题目**: i.i.d. 的 max/min 密度; Unif 下 $P(XY<Z^2)=5/9$; $N(\mu,\sigma^2)$ 的 $X\pm Y$ 独立 (MGF).
- **思路**: CDF 求导; $f_{XY}=-\log w$; 联合 MGF 因子化 / 联合正态+协方差 0.
- **来源**: Tut5
