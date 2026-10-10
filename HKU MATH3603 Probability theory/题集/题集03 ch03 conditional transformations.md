# 题集 — Ch03 Conditional & Transformations

> 对齐: `Lec/Lec03 probability theory lecture notes Ch03 讲义.md`.
> 含: (1) 练习题 (2) 课件证明.

## 课件证明

### P1. 独立 $\Rightarrow$ 条件 PMF 为边缘

- **陈述**: **假设** $X\perp\!\!\!\perp Y$; **结论** $p_{Y|X}(y|x)=p_Y(y)$.
- **证明**: $p_{Y|X}(y|x)=p_{X,Y}(x,y)/p_X(x)=p_X(x)p_Y(y)/p_X(x)$.
- **来源**: `Lec/Lec03 probability theory lecture notes Ch03 讲义.md` §3.1

### P2. 泊松条件二项 (Poisson conditioning identity)

- **陈述**: **假设** $X\sim\mathrm{Poisson}(\lambda_1)$, $Y\sim\mathrm{Poisson}(\lambda_2)$ 独立; **结论** $X\mid(X+Y=n)\sim\mathrm{Bin}(n,\lambda_1/(\lambda_1+\lambda_2))$.
- **证明**: $X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$; 对 $0\le k\le n$ 用 $P(X=k,Y=n-k)/P(X+Y=n)$ 约分得二项系数与 $p^k(1-p)^{n-k}$.
- **来源**: 同上 §3.1

### P3. 条件期望基本恒等式

- **陈述**: **结论** $E[X|X]=X$; 若 $X\perp\!\!\!\perp Y$ 则 $E[X|Y]=EX$.
- **证明**: $E[X|X=x]=\sum x'P(X=x'|X=x)=x$; 独立时 $p_{X|Y}(x|y)=p_X(x)$.
- **来源**: 同上 §3.2

### P4. 均方最优预测 (Prop. 3.2.4)

- **陈述**: **假设** $m(X)=E[Y|X]$; **结论** 对任意平方可积 $h(X)$, $E[(Y-h(X))^2]=E[(Y-m(X))^2]+E[(m(X)-h(X))^2]$.
- **证明**: 展开 $E[(Y-m)(m-h)]$, 对 $X$ 取条件期望, $E[Y-m|X]=0$ 使交叉项为 0.
- **来源**: 同上 §3.2

### P5. 全期望定律 (Law of total expectation)

- **陈述**: **结论** $EY=E[E[Y|X]]=\sum_x E[Y|X=x]p_X(x)$.
- **证明**: 交换求和: $\sum_x\sum_y y\,p_{Y|X}(y|x)p_X(x)=\sum_y y\,p_Y(y)$.
- **来源**: 同上 §3.2

### P6. 随机和期望

- **陈述**: **假设** $N$ 与 i.i.d. $X_i$ 独立, 一阶矩有限; **结论** $E[\sum_{i=1}^N X_i]=(EN)(EX_1)$.
- **证明**: 全期望, 条件于 $N=n$ 得 $n EX_1$; $N=0$ 时空和为 0.
- **来源**: 同上 §3.2

### P7. 连续全期望

- **陈述**: **结论** $E[E[Y|X]]=\iint y\,f_{X,Y}(x,y)\,dy\,dx=EY$.
- **证明**: $\int m(x)f_X(x)\,dx=\iint y\,f_{Y|X}(y|x)f_X(x)\,dy\,dx$.
- **来源**: 同上 §3.3

### P8. $Y=X^2$, $X\sim N(0,1)$

- **陈述**: **结论** $Y\sim\chi^2_1$, $f_Y(y)=\dfrac{1}{\sqrt{2\pi y}}e^{-y/2}$ ($y>0$).
- **证明**: $F_Y(y)=\Phi(\sqrt y)-\Phi(-\sqrt y)$, 求导用 $\phi(\sqrt y)/\sqrt y$.
- **来源**: 同上 §3.5

### P9. 严格单调变换密度

- **陈述**: **假设** $Y=g(X)$, $g$ 严格单调可微; **结论** $f_Y(y)=f_X(g^{-1}(y))|d g^{-1}/dy|$.
- **证明**: $g$ 增时 $F_Y(y)=F_X(g^{-1}(y))$, 链式法则; 减时取绝对值.
- **来源**: 同上 §3.5

### P10. 和差变换 Jacobian

- **陈述**: **假设** $Y_1=X_1+X_2$, $Y_2=X_1-X_2$, $X_1,X_2$ i.i.d. $N(0,1)$; **结论** $Y_1\perp\!\!\!\perp Y_2$, 各 $\sim N(0,2)$.
- **证明**: 逆变换 Jacobian $|\det|=1/2$, 代入联合密度分离为两正态密度乘积.
- **来源**: 同上 §3.5

### P11. 二元正态条件律

- **陈述**: 二元正态下 $X\mid Y=y$ 仍为正态 (线性均值, 方差 $(1-\rho^2)\sigma_X^2$).
- **证明**: 超出本课已授范围; 讲义仅陈述 / 配平方完成 (未在 Ch.3 给出完整逐步).
- **来源**: 同上 §3.3

## 练习题

### 1. 泊松条件二项 (例 3.1.3)

- **题目**: $X\sim\mathrm{Poisson}(\lambda_1)$, $Y\sim\mathrm{Poisson}(\lambda_2)$ 独立. 求 $X\mid(X+Y=n)$.
- **思路**: 和仍 Poisson; 比概率得 $\mathrm{Bin}(n,\lambda_1/(\lambda_1+\lambda_2))$.
- **来源**: Lec Ch03 §3.1

### 2. $E[X\mid X+Y]$

- **题目**: 同上, 求 $E[X\mid X+Y]$.
- **思路**: 条件二项均值 $np(X+Y)$, $p=\lambda_1/(\lambda_1+\lambda_2)$.
- **来源**: Lec Ch03 例题要点

### 3. 矿工期望时间

- **题目**: 三隧道, 选错重启 (讲义数值). 求期望逃出时间 $ET$.
- **思路**: 全期望方程 $ET=\frac13(\cdots)+\frac13(\text{延迟}_1+ET)+\cdots$, 解得 $ET=15$.
- **来源**: Lec Ch03 §3.2

### 4. 随机和期望

- **题目**: $N$ 与 i.i.d. $X_i$ 独立, 有限一阶矩. 求 $E[\sum_{i=1}^N X_i]$.
- **思路**: 全期望, 条件于 $N=n$ 得 $n EX_1$.
- **来源**: Lec Ch03 §3.2

### 5. 秘书 / 最佳奖品

- **题目**: $n$ 奖品随机序; 拒前 $k$ 个后取第一个优于前 $k$. 求 $P_k(B)$ 与大 $n$ 最优策略.
- **思路**: 条件于最佳位置 $I$; $P_k(B)=\frac{k}{n}\sum_{j=k}^{n-1}1/j$; $k\approx n/e$, $P\approx 1/e$.
- **来源**: Lec Ch03 §3.4

### 6. $Y=X^2$, $X\sim N(0,1)$

- **题目**: 求 $Y$ 的分布 ($\chi^2_1$).
- **思路**: $F_Y(y)=P(-\sqrt y\le X\le\sqrt y)$; 求导.
- **来源**: Lec Ch03 §3.5

### 7. 骰子奇偶与预测

- **题目**: (讲义设定) 用 $X$ 信息得 $E[Y|X]=3+X$ 型结论.
- **思路**: 离散条件期望 / 均方最优预测.
- **来源**: Lec Ch03 例题要点

### 8. 和差变换 Jacobian

- **题目**: 二元和差变换求联合密度 (讲义 $|J|=2$ 情形).
- **思路**: 反解 + Jacobian 绝对值倒数.
- **来源**: Lec Ch03 例题要点
