# Summary01 — Test 1 Key Points (Ch1 + Ch2)

- **源**: `exam-review/Summary01 test1 key points.pdf` (Fall 2026 官方考点, 两页)
- **用途**: 按官方 13+13 条展开. 公理卷面会给, 这里写要推出的结论和证明骨架.
- **编号**: Ch1 用讲义原号; Ch2 写成 `P1` / `P2` / `P3`, 因为各 Part 编号重启.

官方第 13 条只点了通项、比较、极限比较. 下面第 13 节按 Part 3 slides 补全其余判别法: 交错级数、根值、比值.

---

## Chapter 1: Real Numbers

### 1. 有序域的例子与反例

域 (field, Def 1.1): (A1)–(A4) 加法交换、结合、零元、负元; (M1)–(M4) 乘法交换、结合、单位元 $1\neq 0$、非零元有逆; (D) 分配律.

有序域 (ordered field, Def 1.6): 域上再有 $\le$, 满足

- (O1) $a\le b$ 或 $b\le a$
- (O2) $a\le b$ 且 $b\le a$ $\Rightarrow$ $a=b$
- (O3) $a\le b\le c$ $\Rightarrow$ $a\le c$
- (O4) $a\le b$ $\Rightarrow$ $a+c\le b+c$
- (O5) $a\le b$ 且 $c\ge 0$ $\Rightarrow$ $ac\le bc$

$a<b$ 指 $a\le b$ 且 $a\neq b$.

**例子**: $\mathbb{Q}$, $\mathbb{R}$ 是有序域.

**反例**: $\mathbb{C}$, 以及 $\mathbb{Q}(i)=\{a+bi:a,b\in\mathbb{Q}\}$. 它们是域, 但不能成为有序域: 非零元的平方必须为正 (见下条), 但 $i^2=-1<0$.

### 2. 从公理推出的性质

公理会印在卷上. 常推的是:

- $0\cdot a=0$; $-(-a)=a$; $(-a)b=-(ab)$; $(-a)(-b)=ab$ (Prop 1.5)
- $a\neq 0$ $\Rightarrow$ $a^2>0$. 从而 $1=1^2>0$, $-1<0$
- $a\le b$ 且 $c\le 0$ 时不等式反向: $ac\ge bc$ (先化成乘 $-c\ge 0$)
- $a<b+\varepsilon$ 对一切 $\varepsilon>0$ $\Rightarrow$ $a\le b$ (Tut1 Q1: 若 $a>b$, 取 $\varepsilon=a-b$)

平方为正的证法: $a\ge 0$ 时用 (O5) 得 $a^2\ge 0$; $a\le 0$ 时 $(-a)^2=a^2\ge 0$. $a\neq 0$ 则 $a^2\neq 0$, 所以 $a^2>0$.

### 3. $\sup$ / $\inf$ 以及二者的关系

$S$ 非空.

- 上界 $M$: $\forall x\in S,\ x\le M$. 下界对偶.
- $\sup S$: 最小上界. $\inf S$: 最大下界. (Def 3.1)
- $\max S$ 存在 $\Leftrightarrow$ $\sup S\in S$, 此时二者相等. $\min$ 与 $\inf$ 同样.
- $\inf S=-\sup(-S)$, $\sup S=-\inf(-S)$.
- $\inf S\le\sup S$. 若 $\inf S=\sup S$, 则 $S$ 是单点集 (Tut1 Q3).

**上确界判别** (Thm 3.3): $u$ 已是上界时, $u=\sup S$ $\Leftrightarrow$ 对每个 $\varepsilon>0$ 存在 $x\in S$ 使 $x>u-\varepsilon$.

下确界: $v$ 已是下界, 且对每个 $\varepsilon>0$ 存在 $x\in S$ 使 $x<v+\varepsilon$.

### 4. 求 $\sup/\inf$; 加法和乘法

先证是上/下界, 再用 Thm 3.3 说明不能再紧. 确界可以不在集合里.

**平移**: $\sup(A+c)=\sup A+c$, $\inf(A+c)=\inf A+c$.

**数乘** $cA=\{ca:a\in A\}$:

- $c>0$: $\sup(cA)=c\sup A$, $\inf(cA)=c\inf A$
- $c<0$: $\sup(cA)=c\inf A$, $\inf(cA)=c\sup A$ (Practice 第 3 题. $c<0$ 时不是 $c\sup A$)

**集合相加** $A+B=\{a+b\}$ (Tut1 Q5(a), 为真):

$$
\sup(A+B)=\sup A+\sup B,\qquad \inf(A+B)=\inf A+\inf B.
$$

证 $\sup$: 每个 $a+b\le\sup A+\sup B$. 若右边更大, 差为 $r>0$, 取 $a',b'$ 使两边各亏不到 $r/2$, 则 $a'+b'$ 超过 $\sup(A+B)$.

**集合相乘** $AB=\{ab\}$ (Tut1 Q5(b), 一般为假):

反例 $A=\{1,2\}$, $B=\{-2,-1\}$, $AB=\{-4,-2,-1\}$, $\sup(AB)=-1$, 而 $(\sup A)(\sup B)=-2$.

两边都在 $[0,\infty)$ 时才有 $\sup(AB)=(\sup A)(\sup B)$. 有负数时, $\sup(AB)$ 是 $(\inf A)(\inf B)$, $(\inf A)(\sup B)$, $(\sup A)(\inf B)$, $(\sup A)(\sup B)$ 四者中的最大者.

子集: $A\subseteq B$ 且都有界 $\Rightarrow$ $\inf B\le\inf A\le\sup A\le\sup B$ (Tut1 Q4).

### 5. 完备性, 以及用它证明方程有解

**完备性公理** (Def 3.8): 有序域里, 每个非空且有上界的子集都有上确界.

标准用法 (Thm 4.9, $\sqrt{2}$): 令 $S=\{y\ge 0:y^2<2\}$. $S$ 非空有上界, 令 $x=\sup S$. 排除 $x^2<2$ (还能再抬一点仍在 $S$ 里) 和 $x^2>2$ (还能把上界压低). 故 $x^2=2$.

递推或不等式里「解存在」也是同一套路: 造一个非空有上界的集合, 取 $\sup$, 再排除太小和太大.

### 6. 实数在本课里怎么定义

$\mathbb{R}$ 是完备有序域: 有序域, 并且满足完备性. 在同构意义下唯一, 并且含有 $\mathbb{N}\subset\mathbb{Z}\subset\mathbb{Q}$.

作业里的另一种构造是戴德金分割, 不在这份清单的必背范围里. 卷面问「定义」时, 答完备有序域即可.

### 7. 为何 $\mathbb{Q}$ 不完备

$S=\{q\in\mathbb{Q}:q\ge 0,\ q^2<2\}$ 在 $\mathbb{Q}$ 里非空、有上界 (例如 $2$), 但在 $\mathbb{Q}$ 里没有上确界.

理由: 若 $u\in\mathbb{Q}$ 是上确界, Thm 4.8 说没有有理数平方等于 $2$. $u^2<2$ 时能找到更大的有理数仍在 $S$ 里; $u^2>2$ 时能找到更小的有理上界. 两种都矛盾.

完备性是 $\mathbb{R}$ 有、$\mathbb{Q}$ 没有的那条公理. 同样的集合在 $\mathbb{R}$ 里的上确界就是 $\sqrt{2}$.

### 8. $\mathbb{N}$ 的良序

**良序** (well-ordering): $\mathbb{N}$ 的每个非空子集都有最小元. 本课当已知性质用.

它和阿基米德性质一起用. 阿基米德 (Thm 4.1–4.2, 由完备性推出): $\mathbb{N}$ 无上界; 对任意实数 $x$ 存在 $n$ 使 $n>x$; 对任意 $\varepsilon>0$ 存在 $n$ 使 $1/n<\varepsilon$.

证 $\mathbb{N}$ 无上界: 若有上界, $u=\sup\mathbb{N}$, 则有 $n>u-1$, 于是 $n+1>u$.

稠密性的证明里, 「大于 $na$ 的整数中取最小的」就是良序.

### 9. $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密

**推论 4.6**: $a<b$ $\Rightarrow$ 存在 $r\in\mathbb{Q}$ 使 $a<r<b$.

取 $n$ 使 $1/n<b-a$. 再用良序取整数 $m$, 使 $m-1\le na<m$. 则 $a<m/n<b$.

无理数也稠密: $a<b$ 时先在 $(a/\sqrt{2},\,b/\sqrt{2})$ 里取有理 $r\neq 0$, 则 $r\sqrt{2}$ 是这个区间里的无理数. 清单原文只点了有理数.

### 10. 嵌套区间性质

**Thm 5.5**: $I_n=[a_n,b_n]$ 闭区间, 且 $I_{n+1}\subseteq I_n$ (即 $a_n\le a_{n+1}\le b_{n+1}\le b_n$). 则

$$
\bigcap_n I_n\neq\emptyset.
$$

证: $(a_n)$ 递增, 且每个 $b_1$ 都是上界. $c=\sup\{a_n\}$. 对每个 $n$, $a_n\le c$. 又每个 $b_n$ 都是 $\{a_m\}$ 的上界, 所以 $c\le b_n$. 于是 $c\in I_n$ 对一切 $n$.

长度 $b_n-a_n\to 0$ 时, 交恰有一个点.

例子:

| 交 | 例子 | 为何不违反定理 |
|---|---|---|
| 空 | $I_n=(0,1/n)$ | 开区间, 定理要求闭 |
| 单点 | $I_n=[0,1/n]$, 交为 $\{0\}$ | 闭且嵌套 |
| 不止一点 | $I_n=[0,1]$ 恒定, 交为 $[0,1]$ | 闭且嵌套; 长度不趋于 $0$ |

### 11. $\mathbb{Q}$ 可数

可数 (Def 5.6): 有限, 或与 $\mathbb{N}$ 有双射.

步骤:

1. 正有理写成既约 $m/n$, 得到单射 $\mathbb{Q}^+\hookrightarrow\mathbb{N}\times\mathbb{N}$.
2. $\mathbb{N}\times\mathbb{N}$ 可数: 对角线, 或 $(m,n)\mapsto 2^{m-1}(2n-1)$ (Thm 5.10).
3. $\mathbb{Z}$ 可数: $0,1,-1,2,-2,\ldots$ (Thm 5.9).
4. $\mathbb{Q}=\{0\}\cup\mathbb{Q}^+\cup\mathbb{Q}^-$ 是三个可数集的并 (Thm 5.11).

可数集的子集可数; 可数个可数集的并仍可数. 稠密和可数不矛盾: 一个是序, 一个是基数.

### 12. $\mathbb{R}$ 与无理数不可数

**Thm 5.8**: $[0,1]$ 不可数, 从而 $\mathbb{R}$ 不可数.

对角线: 设 $[0,1]=\{x_n\}$, $x_n=0.a_{n1}a_{n2}\ldots$. 令 $y=0.b_1b_2\ldots$, 其中 $a_{kk}\neq 4$ 时 $b_k=4$, 否则 $b_k=5$. 则 $y\in[0,1]$, 且 $y$ 和每个 $x_n$ 在第 $n$ 位不同. 用 $4,5$ 是为了避开 $0.1999\ldots=0.2000\ldots$.

**Thm 5.12**: 无理数不可数. 若 $\mathbb{R}\setminus\mathbb{Q}$ 可数, 它和可数集 $\mathbb{Q}$ 的并就是可数的 $\mathbb{R}$, 矛盾.

### 13. 证明某数无理, 例如 $\sqrt{2}$

**Thm 4.8**: 没有 $x\in\mathbb{Q}$ 使 $x^2=2$.

既约 $p/q$, $p^2=2q^2$. 则 $p$ 偶, 写成 $p=2k$, 得 $q$ 也偶, 与既约矛盾.

存在性是另一件事: Thm 4.9 在 $\mathbb{R}$ 里造出 $x^2=2$, 再由 Thm 4.8 知道它无理.

一般根式 (Tut1 Q8): $\sqrt[m]{n}$ 要么是整数, 要么无理. 写成既约 $p/q$ 且 $q>1$, 取 $q$ 的素因子, 它整除 $p$, 矛盾.

---

## Chapter 2: Sequences

### 1. $\varepsilon$-$N$ 定义, 并用定义求极限

$(x_n)\to x$ (Def 1.4): $\forall\varepsilon>0$, $\exists N$, 使 $n>N\Rightarrow|x_n-x|<\varepsilon$.

极限唯一 (Thm 1.6, Part 1).

做法: 先把 $|x_n-x|$ 放大成一个趋于 $0$ 的简单式子 (如 $1/n$), 再反解 $N$. $N$ 可以取 $\lceil\cdot\rceil$, 也可以先把 $n$ 限制到大于某个固定数再估计.

例: $a_n=(n-1)/(n^2-3)\to 0$. $n>3$ 时 $0<a_n<1/(n-3)$. 取 $N=\lceil 3+1/\varepsilon\rceil$.

### 2. 收敛 / 发散的例子; 运算

收敛 $\Rightarrow$ 有界 (Thm 2.2). 逆命题假: $(-1)^n$ 有界但发散.

极限代数 (Thm 3.1): 和、差、积的极限是极限的运算; 商要分母的极限非零.

非严格不等式在极限下保留 (Lem 2.4): $L\le x_n\le M$ $\Rightarrow$ $L\le\lim x_n\le M$. 严格不等号可以在极限处变成等号.

发散的常用判据: 无界; 或两条子列极限不同 (P2 Prop 1.10).

### 3. 证明收敛的方法

- **单调 + 有界**: MCT, 见第 4、5 条.
- **Cauchy**: 见第 6 条. 不知道极限时用.
- **夹逼** (Thm 3.6): $x_n\le y_n\le z_n$, 两边趋于同一 $w$, 则 $y_n\to w$.
- **已知极限**:
  - $0<r<1$ $\Rightarrow$ $r^n\to 0$; $r>1$ 时 $(r^n)$ 发散 (Thm 5.1)
  - $n^{1/n}\to 1$ (Thm 5.2). 令 $x_n=n^{1/n}-1\ge 0$, 二项式留下二次项: $n>(n(n-1)/2)x_n^2$, 得 $x_n^2<2/(n-1)$
  - $(1+1/n)^n\to e$ (Thm 5.4). 先证递增有上界, 极限就定义为 $e$
  - $\sin n/n\to 0$: $|\sin n/n|\le 1/n$, 夹逼

### 4. 从定义证明 MCT

**Thm 4.3**: 单调序列收敛 $\Leftrightarrow$ 有界.

递增且有上界时, 令 $s=\sup\{x_n:n\in\mathbb{N}\}$ (完备性). 对 $\varepsilon>0$, 有 $x_N>s-\varepsilon$. 递增给出 $n>N$ 时 $s-\varepsilon<x_n\le s$. 所以 $x_n\to s$.

**推论 4.4**: 有界递增 $\Rightarrow$ 极限 $=\sup x_n$; 有界递减 $\Rightarrow$ 极限 $=\inf x_n$.

去掉单调则假: $x_1=3$, $n\ge 2$ 时 $x_n=2-1/n$, 极限是 $2$, 上确界是 $3$.

### 5. 用 MCT 求递推极限

固定步骤:

1. 归纳证明单调 (比 $x_1$ 和 $x_2$, 再归纳).
2. 归纳证明有界.
3. MCT 给出极限 $L$ 存在.
4. 在递推式两边取极限, 解出 $L$. 用第 2 步的界丢掉不合范围的根.

例: $a_1=c\ge 0$, $a_{n+1}=3a_n^2/(a_n^2+2)$.

$$
a_n-a_{n+1}=\frac{a_n(a_n-1)(a_n-2)}{a_n^2+2}.
$$

$0\le c<1$ 时递减有下界 $0$, 极限 $0$; $c=1$ 时恒为 $1$; $c>1$ 时单调且夹在 $1$ 和 $\infty$ 的某一侧, 极限 $2$. 可能的极限只有 $0,1,2$, 因为取极限后 $L(L-1)(L-2)=0$.

### 6. Cauchy 序列, 以及和收敛的两端

**定义 3.1**: $\forall\varepsilon>0$, $\exists N$, 使 $n,m>N\Rightarrow|x_n-x_m|<\varepsilon$.

要所有充分大的下标两两接近, 不只是相邻项.

**Cauchy 准则**: 实序列收敛 $\Leftrightarrow$ 它是 Cauchy 序列.

- $\Rightarrow$ 是 Thm 3.4: $|x_n-x_m|\le|x_n-x|+|x_m-x|$, 各小于 $\varepsilon/2$.
- $\Leftarrow$ 是 Thm 3.6: Lem 3.5 先得有界, BW 抽出收敛子列, 再用 Cauchy 把整列拉到同一极限. 这一端用完备性. $\mathbb{Q}$ 里有 Cauchy 列不收敛 (逼近 $\sqrt{2}$ 的有理列).

2020 Test 1 第 2 题写 "Using the Cauchy criterion" 就是要求用这两端, 不是只验证定义.

### 7. 压缩列 $\Rightarrow$ Cauchy

**Exercise 3.9**: 存在 $0<C<1$ 使 $|x_{n+2}-x_{n+1}|\le C|x_{n+1}-x_n|$ 对一切 $n$.

则 $|x_{j+1}-x_j|\le C^{j-1}|x_2-x_1|$. $m>n$ 时

$$
|x_m-x_n|\le\sum_{j=n}^{m-1}|x_{j+1}-x_j|\le\frac{C^{n-1}}{1-C}|x_2-x_1|.
$$

右边随 $n\to\infty$ 趋于 $0$, 所以是 Cauchy, 从而在 $\mathbb{R}$ 里收敛.

例子: Fibonacci $f_1=f_2=1$, $x_n=f_n/f_{n+1}$ 是压缩列, 极限 $L=1/(1+L)$, 正根 $L=(\sqrt{5}-1)/2$.

### 8. 子列判敛准则

子列 (Def 1.1): 指标 $n_k$ 严格递增.

**子列准则**: $(x_n)\to L$ 当且仅当 $(x_n)$ 的**每一个**子列都有一条进一步的子列趋于 $L$.

- $\Rightarrow$: 原列趋于 $L$ 时, 任意子列也趋于 $L$ (Thm 1.6), 这条子列自己就是所要的进一步子列.
- $\Leftarrow$: 若原列不趋于 $L$, 则存在 $\varepsilon>0$, 有无穷多项满足 $|x_n-L|\ge\varepsilon$. 这些项组成一条子列, 它的任何进一步子列都不能趋于 $L$.

常用推论 (Prop 1.10): 两条子列趋于不同极限 $\Rightarrow$ 原列发散.

两条子列趋于**同一个**极限, 推不出原列收敛. 原列自己是一条子列, 所以「所有子列都趋于 $L$」确实推出原列趋于 $L$; 缺的是「所有」, 不是这一步逻辑.

有界且发散 $\Rightarrow$ 存在两条极限不同的收敛子列 (2025 第 6 题): BW 先给一条趋于 $L$ 的子列; 不收敛到 $L$ 就有无穷多项离 $L$ 至少 $\varepsilon$; 再对这子列用 BW.

### 9. 单调子列定理与 Bolzano–Weierstrass

**Thm 2.1**: 任何实序列都有单调子列.

峰: $x_m$ 是峰, 若对一切 $n\ge m$ 有 $x_m\ge x_n$.

- 无穷多个峰: 峰本身组成递减子列.
- 只有有限个峰: 从最后一峰之后开始, 每次取后面更大的一项, 得到严格递增子列.

**Thm 2.4 (BW)**: 有界序列有收敛子列.

证: Thm 2.1 取出单调子列; 子列仍有界; MCT 给出收敛. 清单要求会用单调子列定理推 BW.

找单调子列时, 先看峰是有限还是无穷, 或者直接按奇偶、周期把单调的那一截写出来. 例如 $x_n=2n+(-1)^n 2n$: 偶数项 $4k$ 严格递增.

### 10. 级数的定义和收敛例子

$s_k=\sum_{n=1}^k x_n$. $\sum x_n$ 收敛指 $(s_k)$ 收敛 (Def 1.1).

几何级数: $0<r<1$ 时 $\sum_{k=1}^\infty r^k=r/(1-r)$; $r\ge 1$ 发散 (Ex 1.1).

调和级数 $\sum 1/n$ 发散 (Ex 1.2): 分组后 $s_{2^k}$ 大于 $1+k/2$ 这一类下界.

$p\ge 2$ 时 $\sum 1/n^p$ 收敛 (Ex 2.6), 和 $1/n^2$ 比较即可. 一般的 $p>1$ 要用 Cauchy 凝聚, 官方清单没有单独点凝聚.

非负项 (Thm 2.5): $\sum x_n$ 收敛 $\Leftrightarrow$ 部分和有界. 这就是把 MCT 用在 $(s_k)$ 上.

### 11. 绝对收敛与条件收敛

绝对收敛 (Def 3.1): $\sum|x_n|$ 收敛.

条件收敛 (Def 3.9): $\sum x_n$ 收敛, 但 $\sum|x_n|$ 发散.

**Thm 3.3**: 绝对收敛 $\Rightarrow$ 收敛.

$$
0\le x_n+|x_n|\le 2|x_n|.
$$

比较得到 $\sum(x_n+|x_n|)$ 收敛, 再减去 $\sum|x_n|$.

关系: 绝对收敛 $\Rightarrow$ 收敛, 而且不是条件收敛. 条件收敛 $\Rightarrow$ 收敛, 但不是绝对收敛. 收敛推不出绝对收敛.

例子: $\sum(-1)^{n+1}/n$ 条件收敛; $\sum(-1)^n/n^2$ 绝对收敛.

### 12. 重排

重排 (Def 3.6): 存在双射 $f$ 使 $y_n=x_{f(n)}$. 换顺序, 不丢项也不重复.

**重排定理 Thm 3.7**: 绝对收敛且和为 $L$ 时, 任意重排仍收敛到 $L$.

证的骨架: 重排的部分和 eventualy 含有原级数的前 $m$ 项, 差被尾部 $\sum_{k>m}|x_k|$ 控制. 绝对收敛使这个尾部趋于 $0$.

同一双射也重排了 $|x_n|$, 所以绝对收敛级数的重排仍绝对收敛 (Ex 3.8).

条件收敛时定理的假设不在, 重排可以改变和. 交错调和级数就是标准例子: 收敛, 但不绝对收敛, 换顺序后和可以不同.

### 13. Slides 里的敛散判别

**n-th term test (Thm 2.1)**: $\sum x_n$ 收敛 $\Rightarrow$ $x_n\to 0$.

**Comparison test (Thm 2.8)**: $0\le x_n\le y_n$.

- $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛
- $\sum x_n$ 发散 $\Rightarrow$ $\sum y_n$ 发散

**Limit comparison test (Thm 2.11)**: $x_n,y_n>0$, $r=\lim x_n/y_n$ 存在.

- $r>0$: 两者同敛散
- $r=0$ 且 $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛
- $r=0$ 时反向不成立

**Alternating series test (Thm 3.13, Leibniz test)**: $x_n>0$, $(x_n)$ 递减, $x_n\to 0$ $\Rightarrow$ $\sum (-1)^{n+1}x_n$ 收敛.

**Root test (Thm 3.16)**: $r=\lim |x_n|^{1/n}$ 存在.

- $r<1$: 绝对收敛
- $r>1$: 发散
- $r=1$: 无效

**Ratio test (Thm 3.17)**: $x_n\neq 0$, $r=\lim |x_{n+1}/x_n|$ 存在.

- $r<1$: 绝对收敛
- $r>1$: 发散
- $r=1$: 无效
