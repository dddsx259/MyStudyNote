# Chapter 3: 条件分布 (conditional distributions), 条件期望 (conditional expectation) 与变换 (transformations)

- **来源**: `Lec/01-probability-theory-lecture-notes.pdf` Chapter 3 (p.44–56)
- **课程**: MATH3603, Zhigang Bao
- **前置**: Ch.2 联合分布 (joint distribution), 期望 (expectation), 独立性 (independence)
- **本章目标**: 条件分布/条件期望 (离散与连续), 全期望定律 (law of total expectation), 二元正态 (bivariate normal) 条件律, 最佳奖品问题 (best choice / secretary problem) 停时, 随机变量变换与雅可比行列式 (Jacobian)
- **说明**: 凡非定义公式均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

---

## 3.1 离散条件分布

给定 $p_X(x)>0$:
$$p_{Y|X}(y|x)=\frac{p_{X,Y}(x,y)}{p_X(x)},\qquad F_{Y|X}(y|x)=P(Y\le y|X=x).$$

(定义, 无需证明.)

对固定 $x$, 条件律是普通分布. 若 $X\perp\!\!\!\perp Y$, 则 $p_{Y|X}(y|x)=p_Y(y)$.

**证明**: $X\perp\!\!\!\perp Y$ $\Rightarrow$ $p_{X,Y}(x,y)=p_X(x)p_Y(y)$, 故
$$p_{Y|X}(y|x)=\frac{p_X(x)p_Y(y)}{p_X(x)}=p_Y(y).$$

### 泊松条件恒等式 (Poisson conditioning identity) (例 3.1.3)

$X\sim\mathrm{Poisson}(\lambda_1)$, $Y\sim\mathrm{Poisson}(\lambda_2)$ 独立 $\Rightarrow$
$$X\mid(X+Y=n)\sim\mathrm{Bin}\Bigl(n,\frac{\lambda_1}{\lambda_1+\lambda_2}\Bigr).$$

**证明**: 独立泊松 $\Rightarrow$ $X+Y\sim\mathrm{Poisson}(\lambda_1+\lambda_2)$. 对 $0\le k\le n$,
\begin{align*}
P(X=k\mid X+Y=n)
&=\frac{P(X=k,Y=n-k)}{P(X+Y=n)}
=\frac{e^{-\lambda_1}\lambda_1^k/k!\cdot e^{-\lambda_2}\lambda_2^{n-k}/(n-k)!}{e^{-(\lambda_1+\lambda_2)}(\lambda_1+\lambda_2)^n/n!}\\
&=\binom{n}{k}\Bigl(\frac{\lambda_1}{\lambda_1+\lambda_2}\Bigr)^k\Bigl(\frac{\lambda_2}{\lambda_1+\lambda_2}\Bigr)^{n-k}.
\end{align*}

**补充直觉**: 独立泊松叠加后, "每个事件来自源 1" 的比例恰为 $\lambda_1/(\lambda_1+\lambda_2)$ (与 Ch.5 叠加一致).

---

## 3.2 条件期望与全期望

### 定义

离散: $E[Y|X=x]=\sum_y y\,p_{Y|X}(y|x)$. 令 $m(x)=E[Y|X=x]$, 则
$$E[Y|X]:=m(X)$$
是 $X$ 的函数 (只含 $X$ 可读信息).

(定义, 无需证明.)

恒等式: $E[X|X]=X$; 若 $X\perp\!\!\!\perp Y$ 则 $E[X|Y]=EX$.

**证明**:
1. $E[X|X=x]=\sum_x' x'\,P(X=x'|X=x)=x$, 故 $E[X|X]=X$.
2. $X\perp\!\!\!\perp Y$ $\Rightarrow$ $p_{X|Y}(x|y)=p_X(x)$, 从而 $E[X|Y=y]=\sum x\,p_X(x)=EX$, 故 $E[X|Y]=EX$.

### 均方最优预测 (mean-square optimal prediction) (Prop. 3.2.4)

在平方可积函数 $h(X)$ 中, $E[Y|X]$ 最小化 $E[(Y-h(X))^2]$:
$$E[(Y-h(X))^2]=E[(Y-m(X))^2]+E[(m(X)-h(X))^2].$$

**证明**: 展开交叉项
$$E[(Y-m(X))(m(X)-h(X))]=E\bigl[E[(Y-m(X))(m(X)-h(X))\mid X]\bigr].$$
给定 $X$, $m(X)-h(X)$ 为常数, 且 $E[Y-m(X)|X]=0$, 故交叉项为 $0$. 于是
$$E[(Y-h)^2]=E[(Y-m)^2]+E[(m-h)^2]\ge E[(Y-m)^2],$$
等号当且仅当 $h(X)=m(X)$ a.s.

**补充**: 无额外信息时最优常值预测是 $EY$; 有 $X$ 时升级为条件期望.

### 全期望定律 (Thm. 3.2.6)

$$EY=E\bigl[E[Y|X]\bigr]=\sum_x E[Y|X=x]\,p_X(x).$$

**证明** (离散):
\begin{align*}
E\bigl[E[Y|X]\bigr]
&=\sum_x m(x)\,p_X(x)
=\sum_x\sum_y y\,p_{Y|X}(y|x)\,p_X(x)
=\sum_x\sum_y y\,p_{X,Y}(x,y)
=\sum_y y\,p_Y(y)=EY.
\end{align*}

### 典型应用

1. **矿工问题 (miner problem)**: 三隧道, 期望重启结构 $\Rightarrow$ $ET=15$.

**证明思路**: 设 $T$ 为逃出时间. 以 $1/3$ 概率立刻选对隧道 ($T=3$ 或按题设时长), 另两隧道分别带回延迟 $2$, $5$ (或题设) 并重新开始. 用全期望写
$$ET=\frac13\cdot(\text{成功时长})+\frac13\cdot(\text{延迟}_1+ET)+\frac13\cdot(\text{延迟}_2+ET),$$
解线性方程得 $ET=15$ (具体延迟以讲义例题数值为准).

2. **随机和 (random sum)**: $N$ 与独立同分布 (i.i.d.) $X_i$ 独立, $EN<\infty$, $E|X_1|<\infty$ $\Rightarrow$
   $$E\Bigl(\sum_{i=1}^N X_i\Bigr)=(EN)(EX_1).$$

**证明**: 条件于 $N=n$, $\sum_{i=1}^n X_i$ 的期望为 $n\,EX_1$ (独立性). 由全期望
$$E\Bigl[\sum_{i=1}^N X_i\Bigr]=E\Bigl[E\Bigl[\sum_{i=1}^N X_i\Bigm|N\Bigr]\Bigr]=E[N\cdot EX_1]=(EN)(EX_1).$$
($N=0$ 时空和取 $0$.)

---

## 3.3 连续情形

### 密度比公式 (density ratio formula)

$P(X=x)=0$, 不能直接用事件比. 对短区间取极限得
$$f_{Y|X}(y|x)=\frac{f_{X,Y}(x,y)}{f_X(x)}\quad(f_X(x)>0),$$
$$E[Y|X=x]=\int y\,f_{Y|X}(y|x)\,dy.$$

(定义 / 正则条件期望的密度刻画, 无需另证; 下面给出启发推导.)

**证明思路** (启发): 对小 $h>0$,
$$P(Y\in dy\mid X\in[x,x+h])\approx\frac{f_{X,Y}(x,y)\,h\,dy}{f_X(x)\,h}\to\frac{f_{X,Y}(x,y)}{f_X(x)}\,dy.$$

全期望: $EY=\int E[Y|X=x]f_X(x)\,dx$. 也可写
$$P(A)=\int P(A|Y=y)f_Y(y)\,dy.$$

**证明** (全期望, 连续):
$$E\bigl[E[Y|X]\bigr]=\int m(x)f_X(x)\,dx=\int\!\!\int y\,f_{Y|X}(y|x)f_X(x)\,dy\,dx=\int\!\!\int y\,f_{X,Y}(x,y)\,dy\,dx=EY.$$
事件形式: 取 $Y$ 的示性函数 $1_A$ (或对 $Y$ 的密度 marginalize).

### 二元正态

联合密度含相关参数 (correlation) $\rho\in(-1,1)$. 边缘分布 (marginal) 各为正态; $\rho=0\Leftrightarrow$ 独立 (在二元正态族内).

**条件律** (Prop. 3.3.4):
$$X\mid(Y=y)\sim N\Bigl(\mu_X+\rho\frac{\sigma_X}{\sigma_Y}(y-\mu_Y),\;\sigma_X^2(1-\rho^2)\Bigr),$$
$$E[X|Y]=\mu_X+\rho\frac{\sigma_X}{\sigma_Y}(Y-\mu_Y).$$

**证明思路**: 标准化后设 $(\tilde X,\tilde Y)$ 为标准二元正态, 密度
$$f(x,y)=\frac{1}{2\pi\sqrt{1-\rho^2}}\exp\Bigl(-\frac{x^2-2\rho xy+y^2}{2(1-\rho^2)}\Bigr).$$
写出 $f_{X|Y}(x|y)=f(x,y)/f_Y(y)$, 对 $x$ 配方得正态核, 均值为 $\rho y$, 方差为 $1-\rho^2$. 再仿射还原到 $(\mu_X,\mu_Y,\sigma_X,\sigma_Y)$.

$\rho\to\pm 1$ 时条件方差 $\to 0$, 近乎线性确定性关系.

---

## 3.4 最佳奖品问题 (最优停时 (optimal stopping))

$n$ 个不同奖品随机顺序呈现; 拒后不可召回. 策略: 先拒前 $k$ 个, 之后接受第一个优于前 $k$ 的.

$$P_k(B)=\frac{k}{n}\sum_{j=k}^{n-1}\frac{1}{j}\approx\frac{k}{n}\log\frac{n}{k}.$$

大 $n$ 最优: $k\approx n/e$, 成功概率 $\approx 1/e$.

**证明思路**: 令 $I$ 为最佳奖品位置, $I\sim\mathrm{Unif}\{1,\ldots,n\}$. 成功当且仅当: $I>k$, 且位置 $I$ 是 $(k+1,\ldots,I)$ 中相对前 $k$ (从而相对全体前 $I-1$) 的第一个候选. 等价地, 前 $I$ 个中次优者落在前 $k$ 个位置. 故
$$P(B\mid I=j)=\begin{cases}0,& j\le k,\\ k/(j-1),& j>k.\end{cases}$$
全概率:
$$P_k(B)=\sum_{j=k+1}^n\frac1n\cdot\frac{k}{j-1}=\frac{k}{n}\sum_{j=k}^{n-1}\frac1j.$$
大 $n$ 令 $x=k/n$, 和 $\approx\log(1/x)$, 故 $P\approx -x\log x$, 在 $x=1/e$ 取最大 $1/e$.

**补充**: 经典秘书问题 (secretary problem) / 最佳选择问题 (best choice problem); 用条件于最优位置 $I$ 的全概率公式 (law of total probability).

---

## 3.5 变换与分布

### 原像法 (preimage method)

$Y=g(X)$ $\Rightarrow$ $F_Y(y)=P\bigl(X\in g^{-1}((-\infty,y])\bigr)$. 不必一一映射.

(定义式 / CDF 定义, 无需证明.)

例: $X\sim N(0,1)$, $Y=X^2$ $\Rightarrow$ 卡方分布 (chi-squared) $\chi^2_1$ 密度 $f_Y(y)=\frac{1}{\sqrt{2\pi y}}e^{-y/2}$ ($y>0$).

**证明**: 对 $y>0$,
$$F_Y(y)=P(X^2\le y)=P(-\sqrt{y}\le X\le\sqrt{y})=\Phi(\sqrt{y})-\Phi(-\sqrt{y}).$$
求导:
$$f_Y(y)=\phi(\sqrt{y})\cdot\frac{1}{2\sqrt{y}}+\phi(-\sqrt{y})\cdot\frac{1}{2\sqrt{y}}=\frac{1}{\sqrt{2\pi y}}e^{-y/2}.$$

### 严格单调变换 (strictly monotone transformation)

$$f_Y(y)=f_X\bigl(g^{-1}(y)\bigr)\Bigl|\frac{d}{dy}g^{-1}(y)\Bigr|.$$

**证明**: 设 $g$ 严格增, $x=g^{-1}(y)$, 则 $F_Y(y)=F_X(g^{-1}(y))$, 链式求导得
$$f_Y(y)=f_X(g^{-1}(y))\frac{d}{dy}g^{-1}(y).$$
严格减时 $F_Y(y)=1-F_X(g^{-1}(y))+P(X=g^{-1}(y))$, 导数带负号, 取绝对值统一.

### 二维变换与雅可比行列式

$(U,V)=T(X,Y)$ 一一, 逆 $(X,Y)=(a,b)(U,V)$:
$$f_{U,V}(u,v)=f_{X,Y}(a,b)\Bigl|\det\frac{\partial(a,b)}{\partial(u,v)}\Bigr|.$$

**证明思路**: 对可积检验函数 $\varphi$,
$$E[\varphi(U,V)]=\iint\varphi(T(x,y))f_{X,Y}(x,y)\,dx\,dy.$$
换元 $(u,v)=T(x,y)$, $dx\,dy=|\det J_{(a,b)}|\,du\,dv$, 即得密度公式. (与多变量微积分换元公式一致.)

例: $Y_1=X_1+X_2$, $Y_2=X_1-X_2$ $\Rightarrow$ 因子 $1/2$. 两独立标准正态时 $Y_1\perp\!\!\!\perp Y_2$, 各 $\sim N(0,2)$.

**证明**: 逆变换 $X_1=(Y_1+Y_2)/2$, $X_2=(Y_1-Y_2)/2$, 雅可比矩阵行列式为 $-1/2$, 绝对值 $1/2$. 若 $X_1,X_2$ i.i.d. $N(0,1)$,
$$f_{Y_1,Y_2}(y_1,y_2)=\frac{1}{2\pi}e^{-(y_1^2+y_2^2)/4}\cdot\frac12=\frac{1}{\sqrt{4\pi}}e^{-y_1^2/4}\cdot\frac{1}{\sqrt{4\pi}}e^{-y_2^2/4},$$
故独立且各 $N(0,2)$.

### 前推测度视角 (pushforward)

$\mu_X(B)=P(X\in B)=P\circ X^{-1}(B)$; $F_X(x)=\mu_X((-\infty,x])$. 分布 = 原概率经 $X$ 前推.

(定义, 无需证明.)

---

## 例题要点

| 题型 | 关键 |
|---|---|
| 泊松\|和 | 条件二项, $E[X|X+Y]=\frac{\lambda_1}{\lambda_1+\lambda_2}(X+Y)$ |
| 骰子奇偶信息 | $E[Y|X]=3+X$ (均方预测) |
| 矿工 | 条件期望方程解 $ET$ |
| $\chi^2_1$ | 原像法 + 求导 |
| 和差变换 | 雅可比 $=|-2|$ (正变换行列式; 逆为 $1/2$) |

**补充** ($E[X|X+Y]$): 由二项条件律, $E[X|X+Y=n]=np$, $p=\lambda_1/(\lambda_1+\lambda_2)$, 故 $E[X|X+Y]=p(X+Y)$.

---

## 易错点

- 连续条件律用密度比, 勿写 $P(Y\le y,X=x)/P(X=x)$.
- $E[Y|X]$ 是随机变量; $E[Y|X=x]$ 是数.
- 全期望是 $E[E[Y|X]]$, 不是对条件期望再"条件一次"搞混对象.
- 单调变换漏绝对值; 非一一须用原像分段.
- 二元正态外, $\mathrm{Cov}=0$ 仍可能不独立.

---

## 与前后章关系

- **承 Ch.2**: 联合 概率质量函数/概率密度函数 (PMF/PDF), 无意识统计员定律 (LOTUS), 独立性, 矩母函数 (MGF) 工具.
- **启 Ch.4**: 条件期望 / 全期望反复用于马尔可夫链 (Markov chain) 转移, 吸收概率 (absorption probability), 分支过程 (branching process) 均值.
- **启 Ch.5**: 泊松条件二项, 指数竞赛 (exponential race), 条件到达时间 = 均匀次序统计量 (uniform order statistics), 皆是本章技术的连续时间版.
