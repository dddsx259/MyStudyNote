# MATH3603 往年试卷考点分析

> 材料 (都在 `docs/archives/previous/test&quiz/`, 与本学期卷分开):
>
> | 文件 | 是什么 |
> |---|---|
> | `Test01.pdf` | 一套 Test 1, **无官方解答**; 详解在 `test&quiz/Quiz01 往年Test01 解答.md` |
> | `Test01 with solution.pdf` | **另一套** Test 1, 带官方解答 (不是上面那份的 sol) |
> | `Test02.heic` | 往年 Test 2 扫描, 无文字解答 |
> | `Test02 with solution.pdf` | 一套 Test 2, 带官方解答 (Markov + 随机和) |
>
> 往年压缩包已解压后删除. HW1–HW5 题面在 `docs/archives/previous/assignment/Homework0k.pdf`.
>
> **本次 Quiz 1** (2026-10-07, Ch1 + §2.1–2.5, 闭卷无 cheat sheet). 下表「本次」列按这个范围标. 超出的题留着, 不要今晚赶.

---

## 1. 今晚怎么刷

按这个顺序, 做完就停:

1. **`Test01.pdf` 整卷** (三题都在或紧贴本次范围). 对 `test&quiz/Quiz01 备考 往年Test01.md`.
2. **`Test01 with solution.pdf` 只做 Q1**. 密度归一 + CDF, 纯 §2.3. 做完对官方 sol.
3. 有余力再做该卷 **Q6(a)(b)**: 泊松 + 全概率. **(c) 方差**用到条件二阶矩, 讲义在 Ch3, 本次可不写.
4. **不要做**: 该卷 Q2 (CLT, §2.8), Q3 (奇偶递推), Q4–Q5 (条件期望, Ch3), 以及 **整份 Test 2** (Ch4 Markov, 随机和).

---

## 2. 三份卷对照

| 卷 | 题 | 考点 | 章节 | 本次 Quiz1 |
|---|---|---|---|---|
| Test01.pdf | Q1 | 相互独立 ⇒ 补事件仍相互独立 | Ch1 §1.3 | **必做** |
| Test01.pdf | Q2 | 均匀断棍: $\|2U-1\|$ 的分布, 两段乘积, 方差 | §2.1–2.4 CDF / LOTUS | **必做** |
| Test01.pdf | Q3 | 指示变量 + 线性性算期望和方差 (骰子得分) | §2.2 指示, §2.4–2.5 线性性 | **必做** |
| Test01 with solution | Q1 | $c(1-x^2)$ 定 $c$, 再写 CDF | §2.3 PDF / CDF | **必做** |
| Test01 with solution | Q2 | 10 个 Unif 之和用 CLT 估尾概率 | §2.8 | 不考 |
| Test01 with solution | Q3 | 有放回抽球, 白球次数为偶数的递推与极限 | Ch1 全概率 + 递推 | 不优先 |
| Test01 with solution | Q4 | $Y\sim\mathrm{Unif}(0,1)$, $X\mid Y=y\sim\mathrm{Unif}(0,y)$, 求 $EX,\mathrm{Var}(X)$ | Ch3 条件期望 | 不考 |
| Test01 with solution | Q5 | 位置的条件均值 0, 条件方差 $\beta x^2$, 求 $E X_n,\mathrm{Var}(X_n)$ | Ch3 | 不考 |
| Test01 with solution | Q6 | 雨天/晴天泊松混合: 均值, $P(X=0)$, 方差 | §2.2 泊松 + 全概率; 方差偏 Ch3 | (a)(b) 可练 |
| Test02 with solution | Q1 | 加权图上的 Markov 链: 转移阵, 平稳, 先达, 暂态占用, Metropolis 型 $\alpha_{ij}$ | Ch4 | 不考 |
| Test02 with solution | Q2 | $N\sim\mathrm{Poisson}(4)$, $Y_i$ i.i.d. 几何, $S=\sum_{i=1}^N Y_i$ 的均值方差与 $P(S=k)$ | Ch3 随机和 / 后期 | 不考 |

`Test01.pdf` 和 `Test01 with solution.pdf` **不是同一张卷**. 前者三题都短, 更像现在这门课的 50 分钟卷; 后者六题, 后半已经是条件期望和 CLT.

---

## 3. 本次范围内, 往年真的在考什么

下面只保留 Quiz1 该会的. 每条是「题怎么问 → 你要写出的式子」.

### 3.1 相互独立对补集封闭 (Test01.pdf Q1)

**考法**: 给 $A,B,C$ 相互独立, 证 $A^c$ 与 $B$ 独立, $A^c$ 与 $B^c$ 独立, 再升到三个补事件相互独立.

**要会**:

- 定义是**每一个** $|J|\ge 2$ 的子族都满足交集概率 = 概率乘积, 不是只查两两.
- 补集公式从容斥来, 不需要新定理:

$$P(A^c\cap B)=P(B)-P(A)P(B)=P(A^c)P(B),$$

$$P(A^c\cap B^c)=1-P(A)-P(B)+P(A)P(B)=P(A^c)P(B^c).$$

三元交把 $(A\cup B)\cap C$ 拆开, 再用相互独立把每一项换成乘积. 详解见备考稿 Q1.

### 3.2 自己定密度常数, 再积分出 CDF (Test01 with solution Q1)

**考法**: $f(x)=c(1-x^2)$ 在 $(-1,1)$, 外面为 0. (a) 求 $c$. (b) 求 $F$.

**做法**: 密度积分必须是 1.

$$\int_{-1}^{1}(1-x^2)\,dx=\Bigl[x-\frac{x^3}{3}\Bigr]_{-1}^{1}=\Bigl(1-\frac13\Bigr)-\Bigl(-1+\frac13\Bigr)=\frac43,$$

故 **$c=3/4$**. 再累加:

$$F(x)=\int_{-1}^{x}\frac34(1-y^2)\,dy=\frac{3x-x^3+2}{4},\qquad -1<x<1,$$

两端 $F=0$ ($x\le -1$), $F=1$ ($x\ge 1$). 官方解答与此相同.

**同类还会怎么变**: 给出分段函数让你验证它是密度, 或反求 CDF 再求 $P(a<X\le b)=F(b)-F(a)$. 连续型单点概率为 0, 开闭端点不影响.

### 3.3 均匀断棍 (Test01.pdf Q2)

**考法**: 棍长 1, 断点 $U\sim\mathrm{Unif}[0,1]$. $X=|2U-1|$ (两段长度差的绝对值), $Y=U(1-U)$ (两段乘积). 求 $X$ 的分布, $P(Y<1/8)$, $\mathrm{Var}(X),\mathrm{Var}(Y)$.

**要会**:

- 先写 $X=g(U)$ 的 CDF: $P(|2U-1|\le x)=P\bigl(\tfrac{1-x}{2}\le U\le\tfrac{1+x}{2}\bigr)$, $x\in[0,1]$, 长度是 $x$, 所以 $X\sim\mathrm{Unif}[0,1]$.
- $Y$ 没有要求先求出密度也可以: $P(Y<1/8)=P\bigl(U(1-U)<1/8\bigr)$ 解二次方程, 再用均匀的长度.
- 方差用 LOTUS: $E[h(U)]=\int_0^1 h(u)\,du$, 然后 $\mathrm{Var}=E[Z^2]-(EZ)^2$. **不必**先求 $Y$ 的密度.

这是本次最值得限时重做的一题. 完整计算在备考稿 Q2, 这里不重复.

### 3.4 指示变量 + 线性性 (Test01.pdf Q3)

**考法**: $n$ 人各掷一颗公平骰. 两种计分, 都求期望和方差, 答案用 $n$ 表示.

- 相同点数: 每一对相同结果贡献 1 分. 例 $(2,2,2,5)$ 得 $\binom{3}{2}=3$.
- 按面值: 面 $k$ 出现 $m_k$ 次则贡献 $m_k\cdot k$.

**要会**:

- 得分写成和, 对**一对人**或**一个人**放指示变量 $I$.
- $E[\sum I_j]=\sum E I_j$ **不需要独立** (Prop. 2.5.8).
- 方差要 $E[S^2]$ 或 $\mathrm{Var}(S)=\sum\mathrm{Var}+2\sum\mathrm{Cov}$. 两两是否独立决定协方差是不是 0; 骰子题里不同对会共享一个人, 协方差一般不是 0, 要按「对与对是否相交」分类. 详解在备考稿 Q3.

本学期 Tut / coupon collector 用的是同一招: 先写指示, 再线性性. 集齐时间 $ET=NH_N$ 也是这个套路.

### 3.5 泊松混合里, 本次够得着的部分 (Test01 with solution Q6)

雨天 (概率 0.6) 事故数 $\sim\mathrm{Poisson}(9)$, 晴天 (概率 0.4) $\sim\mathrm{Poisson}(3)$. $X$ 为明天事故数.

**(a) 均值, 本次可写.** 全概率 (或全期望, 这里只是两路加权):

$$EX=9\cdot 0.6+3\cdot 0.4=6.6.$$

**(b) $P(X=0)$, 本次可写.** 泊松 PMF $P(X=0\mid\lambda)=e^{-\lambda}$, 再全概率:

$$P(X=0)=0.6e^{-9}+0.4e^{-3}.$$

**(c) 方差, 本次不必.** 官方用 $E[X^2\mid Y]=\lambda^2+\lambda$ (因为泊松方差 = 均值), 得 $E[X^2]=58.8$, $\mathrm{Var}(X)=58.8-6.6^2=15.24$. 这一步的工具是条件二阶矩, 笔记在 Ch3. 若卷子只给到 §2.5, 不要硬套「独立则方差相加」: 混合以后 $X$ 不是单个泊松.

---

## 4. 往年出现、但这次明确不考

知道名字即可, 避免把复习时间花掉.

| 工具 | 出现在 | 本课位置 |
|---|---|---|
| 中心极限定理, 标准化和 $\approx\Phi$ | Test01 with solution Q2 | §2.8 |
| 条件密度 $f_{X\mid Y}$, $E[X]=E[E[X\mid Y]]$ | Q4, Q5, Q6(c) | Ch3 |
| 奇偶递推 $P_{n+1}=\alpha+(1-2\alpha)P_n$ 并解开几何级数 | Q3 | 不在 Ch1–§2.5 的例题里 |
| 转移阵 $P_{ij}=w_{ij}/\sum_k w_{ik}$ | Test02 Q1(a) | Ch4 |
| $\pi P=\pi$ 平稳分布 | Q1(b); 官方一组解 $(1/6,\,1/4,\,5/18,\,11/36)$ | Ch4 |
| 把目标态改成吸收, 用 $(I-P_T)^{-1}$ 算到达概率 / 占用期望 | Q1(c)(d); 官方 $f_{12}\approx 0.559$, $E[N]=1.8$ | Ch4 基本矩阵 |
| 随机和 $E[S]=E[N]E[Y]$, $\mathrm{Var}(S)$ 公式 | Test02 Q2; 官方 $E[S]=8$, $\mathrm{Var}(S)=24$, $P(S=0)=e^{-4}$ | Ch3 |

Test02 Q2 里几何「均值 2」若是从 1 起的 $\mathrm{Geom}(p)$, 则 $1/p=2$, $p=1/2$, $P(Y=1)=1/2$. 官方 $P(S=1)=e^{-4}\cdot 4\cdot 1/2$ 与此一致. 这是 Quiz1 之后的题.

---

## 5. 和本学期卷的差距

往年 **没有**直接出, 但 Bao 把本次范围划到 §2.5, 所以仍要会, 不能只刷上面三题:

- 条件概率, Bayes, 划分上的全概率 (两瓮, 两孩 $1/3$).
- 两两独立 $\neq$ 相互独立 (例 1.3.4 骰子).
- 离散族 PMF: Bernoulli, Bin, Geom (从 1 起), NegBin, Poisson, 以及 $np_n\to\lambda$ 的泊松极限 **假设**.
- 连续族: Unif CDF, 逆变换 $X=F^{-1}(U)$, Exp / Gamma / Normal 的密度. 正态仿射 $aX+b$.
- 联合 CDF / PMF / PDF, **边缘定不了联合**, 矩形概率要加减左极限.
- Coupon: $n$ 次后不同种类期望 $N(1-(1-1/N)^n)$, 集齐时间 $NH_N$.

这些在 `exam-review/Review01 Quiz1 Ch1-2.5 考前复习.md`. 往年卷负责练「独立 + CDF + 指示变量」这三块手感, 不覆盖上面整张清单.
