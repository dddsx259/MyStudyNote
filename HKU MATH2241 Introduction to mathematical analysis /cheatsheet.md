# MATH2241 Cheatsheet

> 词条/公式/定理速查; 对话中学到的内容会增量追加.
> 约定: **定义 / 定理 / 引理 / 命题 / 推论** (及带保证的公式) 一律写清 **假设** 与 **结论** (或 **定义**); 证明见对应讲义, 本表不放完整证明.
> 命名: 优先讲义/教材标题; 须附严谨英文全称; 讲义未命名而自行整理的名称须标 `(自拟)`.
> **分类**: 按原 slides 类型分节 (Definition / Proposition / Lemma / Theorem / Corollary); 条目标题标 **原文编号**.
> **编号约定**: Ch1 用 slides 原号 (如 Def 1.1); Ch2/Ch3 各 Part 编号重启, 写成 `Ch2 P1 Thm 1.6` / `Ch3 P1 Def 1.6`.
> **公理/条件列表须展开**: 如 (A1)–(A4), (M1)–(M4), (D), (O1)–(O5) 等 **禁止只写编号**; 须逐条写出英文名 + 公式陈述.
> 勾选: 每条顶层词条前的 `- [ ]` 用于标记是否已手写整理入 HandCS, 或已决定省略; `[x]` = 已处理.

---

## Definitions / 定义

### Chapter 1

- [x] **Ch1 Def 1.1 — Field** / **域**:
  - **假设**: 集合 $F$ 上有二元运算加法 $+:F\times F\to F$ 与乘法 $\cdot:F\times F\to F$
  - **定义**: 以下性质全部成立:
    - **(A1) 加法交换律** (commutativity for addition): $a+b=b+a$ ($\forall a,b\in F$)
    - **(A2) 加法结合律** (associativity for addition): $(a+b)+c=a+(b+c)$
    - **(A3) 零元存在** (existence of a zero element): $\exists0\in F$ 使 $0+a=a+0=a$ ($\forall a\in F$)
    - **(A4) 加法逆存在** (existence of negatives): $\forall a\in F$, $\exists(-a)\in F$ 使 $a+(-a)=(-a)+a=0$
    - **(M1) 乘法交换律** (commutativity for multiplication): $a\cdot b=b\cdot a$
    - **(M2) 乘法结合律** (associativity for multiplication): $a\cdot(b\cdot c)=(a\cdot b)\cdot c$
    - **(M3) 单位元存在** (existence of an identity element): $\exists1\in F$, $1\neq 0$, 使 $1\cdot a=a\cdot 1=a$
    - **(M4) 乘法逆存在** (existence of multiplicative inverses): $\forall a\in F$, $a\neq 0$, $\exists1/a\in F$ 使 $a\cdot(1/a)=(1/a)\cdot a=1$
    - **(D) 分配律** (distributive property): $a\cdot(b+c)=a\cdot b+a\cdot c$ ($\forall a,b,c\in F$)
  - **记号**: $a-b:=a+(-b)$; $a/b:=a\cdot(1/b)$ ($b\neq 0$); 亦可写 $a^{-1}$ 表示 $1/a$
  - **注**: $0$, $1$, $-a$, $1/a$ ($a\neq 0$) 唯一 (Ex 1.2)

- [x] **Ch1 Def 1.6 — Ordered field** / **有序域**:
  - **假设**: $F$ 为域, 且带关系 $\le$
  - **定义**: $\le$ 满足:
    - **(O1) 全序 / 可比较** : $\forall a,b\in F$, $a\le b$ 或 $b\le a$
    - **(O2) 反对称** : 若 $a\le b$ 且 $b\le a$, 则 $a=b$
    - **(O3) 传递** : 若 $a\le b$ 且 $b\le c$, 则 $a\le c$
    - **(O4) 与加法相容** : 若 $a\le b$, 则 $a+c\le b+c$ ($\forall c$)
    - **(O5) 与非负乘法相容** : 若 $a\le b$ 且 $c\ge 0$, 则 $ac\le bc$
  - **严格序**: $a<b$ 当且仅当 $a\le b$ 且 $a\neq b$
  - **例子**: $\mathbb{Q},\mathbb{R}$ 可序; $\mathbb{C}$ (或含 $i$ 的域) **不能**成为有序域 ($a\neq 0\Rightarrow a^2>0$ 与 $i^2=-1$ 矛盾)

- [ ] **Ch1 (§3, 讲义未单独编号) — Upper / Lower bound** / **上界/下界**:
  - **假设**: $S\subseteq F$, $F$ 有序域; $M,m\in F$
  - **定义 (上界)**: $\forall x\in S,\ x\le M$
  - **定义 (下界)**: $\forall x\in S,\ m\le x$
  - **注**: 有上界 $\not\Rightarrow$ 有最大值

- [ ] **Ch1 (§3, 讲义未单独编号) — Maximum / Minimum** / **最大值/最小值**:
  - **假设**: $S\subseteq F$, $F$ 有序域
  - **定义 (max)**: 存在 $s_0\in S$ 使 $\forall x\in S,\ x\le s_0$ (须在集内)
  - **定义 (min)**: 对偶, $s_0\in S$ 且 $\forall x\in S,\ s_0\le x$
  - **例**: $x\in\mathbb{Q}: 0\le x<8$ 有上界但无 max

- [ ] **Ch1 Def 3.1 — Supremum / Infimum** / **上确界/下确界**:
  - **假设**: $S\subseteq F$ 非空, $F$ 有序域
  - **定义 ($\sup S$)**: 上界集合中的**最小上界** (least upper bound)
  - **定义 ($\inf S$)**: 下界集合中的**最大下界** (greatest lower bound)
  - **注**: $\sup/\inf$ **可以不在** $S$ 内; 若 $\sup S\in S$ 则 $\sup S=\max S$

- [x] **Ch1 Def 3.8–3.9 — Completeness axiom / Complete ordered field** / **完备性公理/完备有序域**:
  - **假设**: $F$ 为有序域
  - **定义 (完备)**: 每个非空且有上界的子集 $S\subseteq F$ 在 $F$ 中都有 $\sup S$
  - **约定**: $\mathbb{R}$ 定义为完备有序域 (存在且在同构意义下唯一, 含 $\mathbb{N},\mathbb{Z},\mathbb{Q}$)
  - **对比**: $\mathbb{Q}$ **不完备**; 例 $S=x\in\mathbb{Q}: x^2<2$ 在 $\mathbb{Q}$ 中无上确界

- [x] **Ch1 Def 5.6 — Countable / Uncountable** / **可数/不可数**:
  - **假设**: 集合 $A$
  - **定义 (可数)**: $A$ 有限, 或存在双射 $A\leftrightarrow\mathbb{N}$
  - **定义 (不可数)**: 非可数
  - **注**: 可数个可数集之并仍可数; 可数集的子集可数

- [ ] **Ch1 (§5.2) — Interval notation** / **区间记号**:
  - **定义**: $(a,b)=x: a<x<b$; $[a,b]=x: a\le x\le b$; 半开 $(a,b],[a,b)$; 无界 $(-\infty,a]$, $[a,\infty)$, $\mathbb{R}=(-\infty,\infty)$

- [ ] **(自拟 / Assignment 1) — Dedekind cut** / **戴德金分割**:
  - **假设**: $\alpha\subsetneq\mathbb{Q}$
  - **定义**: (1) $\alpha\neq\emptyset$, $\alpha\neq\mathbb{Q}$; (2) 向下封闭: $x\in\alpha$, $y<x$ $\Rightarrow$ $y\in\alpha$; (3) 无最大元: $\forall x\in\alpha,\ \exists z\in\alpha,\ x<z$
  - **约定**: $\mathbb{R}'=$ 全体 Dedekind cuts; 有理嵌入 $\hat r=q\in\mathbb{Q}: q<r$



### Chapter 2 Part 1 (Sequences)

- [ ] **Ch2 P1 Def 1.1 — Sequence** / **序列**:
  - **定义**: 函数 $x:\mathbb{N}\to\mathbb{R}$, 记 $(x_n)$

- [ ] **Ch2 P1 Def 1.4 — Convergence / Limit ($\varepsilon$-$N$)** / **收敛/极限**:
  - **假设**: 序列 $(x_n)$, $x\in\mathbb{R}$
  - **定义 (收敛于 $x$)**: $\forall\varepsilon>0$, $\exists N$ 使 $n>N\Rightarrow|x_n-x|<\varepsilon$

- [ ] **Ch2 P1 Def 2.1 — Bounded sequence** / **有界序列**:
  - **假设**: 序列 $(x_n)$
  - **定义**: 存在 $M$ 使 $|x_n|\le M$ 对一切 $n$

- [ ] **Ch2 P1 Def 4.1 — Monotone sequence** / **单调序列**:
  - **假设**: 序列 $(x_n)$
  - **定义**: 递增 ($x_n\le x_{n+1}$) 或递减 ($x_n\ge x_{n+1}$); 严格单调同理用 $<$ / $>$



### Chapter 2 Part 2 (Subsequences / Cauchy)

- [ ] **Ch2 P2 Def 1.1 — Subsequence** / **子列**:
  - **定义**: 严格递增指标 $n_k$ 时 $(x_{n_k})$ 为 $(x_n)$ 的子列

- [x] **Ch2 P2 Def 3.1 — Cauchy sequence** / **Cauchy 序列**:
  - **定义**: $\forall\varepsilon>0$, $\exists N$ 使 $n,m>N\Rightarrow|x_n-x_m|<\varepsilon$



### Chapter 2 Part 3 (Series)

- [ ] **Ch2 P3 Def 1.1 — Series / Partial sums** / **级数/部分和**:
  - **定义**: $s_k=\sum_{n=1}^k x_n$; $\sum x_n$ 收敛 $\Leftrightarrow$ $\lim s_k$ 存在

- [x] **Ch2 P3 Def 3.1 — Absolute convergence** / **绝对收敛**:
  - **定义**: $\sum |x_k|$ 收敛

- [x] **Ch2 P3 Def 3.6 — Rearrangement** / **重排**:
  - **定义**: 序列 $(y_n)$ 是 $(x_n)$ 的重排, 若存在双射 $\sigma:\mathbb{N}\to\mathbb{N}$ 使 $y_n=x_{\sigma(n)}$

- [x] **Ch2 P3 Def 3.9 — Conditional convergence** / **条件收敛**:
  - **定义**: $\sum x_n$ 收敛但非绝对收敛

### Chapter 3 Part 1 (Limits of functions)

- [ ] **Ch3 P1 Def 1.1 — Cluster point** / **聚点**:
  - **假设**: $A\subseteq\mathbb{R}$, $c\in\mathbb{R}$
  - **定义**: 对每个 $\delta>0$, 存在 $x\in A$ 使 $0<|x-c|<\delta$

- [ ] **Ch3 P1 Def 1.6 — Limit of a function** / **函数极限**:
  - **假设**: $c$ 是 $A$ 的聚点, $f:A\to\mathbb{R}$
  - **定义**: $\lim_{x\to c}f=L$ 指: $\forall\varepsilon>0$, $\exists\delta>0$, 使 $x\in A$ 且 $0<|x-c|<\delta$ $\Rightarrow$ $|f(x)-L|<\varepsilon$

- [ ] **Ch3 P1 Def 5.1 — One-sided limits** / **单侧极限**:
  - **假设**: 右/左极限分别要求 $c$ 是 $A\cap(c,\infty)$ / $A\cap(-\infty,c)$ 的聚点
  - **定义**: 半邻域上的 $\varepsilon$-$\delta$ 极限; 双边极限存在 $\Leftrightarrow$ 左右极限存在且相等

### Chapter 3 Part 2 (Continuity)

- [ ] **Ch3 P2 Def 1.1 — Continuity at a point** / **在一点连续**:
  - **假设**: $f:A\to\mathbb{R}$, $c\in A$
  - **定义**: $\forall\varepsilon>0$, $\exists\delta>0$, 使 $x\in A$ 且 $|x-c|<\delta$ $\Rightarrow$ $|f(x)-f(c)|<\varepsilon$
  - **注**: $c$ 为聚点时 $\Leftrightarrow$ $\lim_{x\to c}f=f(c)$; 孤立点自动连续

- [ ] **Ch3 P2 Def 6.1 — Uniform continuity** / **一致连续**:
  - **假设**: $f:A\to\mathbb{R}$
  - **定义**: $\forall\varepsilon>0$, $\exists\delta>0$, 使凡 $x,y\in A$ 且 $|x-y|<\delta$ 都有 $|f(x)-f(y)|<\varepsilon$ ($\delta$ 不依赖点)

- [ ] **Ch3 P2 Def 6.12 — Lipschitz function** / **Lipschitz 函数**:
  - **假设**: $f:A\to\mathbb{R}$, $L\ge0$
  - **定义**: $|f(x)-f(y)|\le L|x-y|$ ($\forall x,y\in A$)
  - **注**: Lipschitz $\Rightarrow$ 一致连续

---



## Propositions / 命题

- [ ] **Ch1 Prop 1.5 — Field corollaries** / **域的常用推论**:
  - **假设**: $F$ 为域, $a,b,z,u\in F$
  - **结论**:
    - (a) 若 $z+a=a$, 则 $z=0$
    - (b) 若 $b\neq 0$ 且 $ub=b$, 则 $u=1$
    - (c) $0\cdot a=0$
    - (d) $-(-a)=a$
    - (e) $(-a)b=-(ab)$ (讲义亦写 $(-a)(b)=-ab$)
    - (f) $(-a)(-b)=ab$
  - **要点**: 证明只用 (A)/(M)/(D) 与逆元唯一性; 考试常考「用公理推」

- [ ] **Ch2 P2 Prop 1.10 — Divergence by two subsequences** / **两子列不同极限 ⇒ 发散**:
  - **假设**: $(x_n)$ 有两子列收敛到不同极限
  - **结论**: $(x_n)$ 发散

---



## Lemmas / 引理

- [ ] **Ch2 P1 Lem 2.4 / Cor 2.5 — Limit preserves closed inequalities** / **极限保持非严格不等式**:
  - **假设**: $(x_n)$ 收敛且 $L\le x_n\le M$ $\forall n$
  - **结论 (Lem 2.4)**: $L\le\lim x_n\le M$
  - **结论 (Cor 2.5)**: 若 $x_n\in[a,b]$ 且收敛, 则 $\lim x_n\in[a,b]$
  - **注**: 不能随意改成严格 $<$ (极限可落在端点)

- [x] **Ch2 P2 Lem 3.5 — Cauchy $\Rightarrow$ bounded** / **Cauchy ⇒ 有界**:
  - **假设**: $(x_n)$ 为 Cauchy 序列
  - **结论**: $(x_n)$ 有界

---



## Theorems / 定理



### Chapter 1

- [ ] **Ch1 Thm 3.3 — Supremum criterion** / **上确界判别法**:
  - **假设**: $S\subseteq\mathbb{R}$ 非空; $u\in\mathbb{R}$ 是 $S$ 的一个上界
  - **结论**: $u=\sup S$ 当且仅当对任意 $\epsilon>0$, 存在 $x\in S$ 满足 $x>u-\epsilon$
  - **对偶 (inf)**: $v=\inf S$ $\iff$ $v$ 为下界且 $\forall\epsilon>0,\ \exists x\in S,\ x-v<\epsilon$

- [ ] **Ch1 Thm 4.1–4.2 — $\mathbb{N}$ unbounded / Archimedean** / **$\mathbb{N}$ 无界与阿基米德**:
  - **假设**: 在完备有序域 $\mathbb{R}$ 中
  - **结论**: $\mathbb{N}$ 无上界; 对任意 $x\in\mathbb{R}$ 存在 $n\in\mathbb{N}$ 使 $n>x$; 对 $a<b$ 可取 $n$ 使 $1/n<b-a$
  - **注**: 讲义亦述 $\mathbb{N}$ 良序 (well-ordering): 非空 $A\subseteq\mathbb{N}$ 有最小元

- [ ] **Ch1 Thm 4.8 — No rational square equals 2** / **无有理数平方为 2**:
  - **假设**: $x\in\mathbb{Q}$
  - **结论**: $x^2\neq 2$
  - **要点**: 既约分数 $p/q$ 反证得 $p,q$ 皆偶, 矛盾

- [ ] **Ch1 Thm 4.9 — Existence of $\sqrt{2}$ via $\sup$** / **用上确界构造 $\sqrt{2}$**:
  - **假设**: 在 $\mathbb{R}$ (完备) 中; 令 $S=y\in\mathbb{R}: y\ge 0,\ y^2<2$
  - **结论**: $x:=\sup S$ 满足 $x^2=2$, 且由 Thm 4.8 得 $x\notin\mathbb{Q}$
  - **要点**: 排除 $x^2<2$ (可再抬高) 与 $x^2>2$ (可压低上界)

- [x] **Ch1 Thm 5.5 — Nested Interval Property** / **嵌套区间性质**:
  - **假设**: $I_n$ 为闭区间, $I_n=[a_n,b_n]$, 且嵌套: $I_{n+1}\subseteq I_n$ 对一切 $n$
  - **结论**: $\bigcap_{n=1}^\infty I_n\neq\emptyset$; 事实上 $c=\supa_n$ 属于交
  - **注**: 开区间嵌套未必非空交; 长度 $\to 0$ 时交为单点 (后续常用)

- [ ] **Ch1 Thm 5.8 — $\mathbb{R}$ uncountable** / **实数不可数**:
  - **结论**: $\mathbb{R}$ 不可数; 等价地 $[0,1]$ 不可数
  - **要点**: 康托对角线论证于 $[0,1]$ 的十进/二进展开

- [ ] **Ch1 Thm 5.9 — $\mathbb{Z}$ countable** / **整数可数**:
  - **结论**: $\mathbb{Z}$ 可数
  - **要点**: 枚举 $0,1,-1,2,-2,\ldots$

- [ ] **Ch1 Thm 5.10 — $\mathbb{N}\times\mathbb{N}$ countable** / **$\mathbb{N}\times\mathbb{N}$ 可数**:
  - **结论**: $\mathbb{N}\times\mathbb{N}$ 可数
  - **要点**: 对角线枚举, 或双射 $(m,n)\mapsto 2^{m-1}(2n-1)$

- [ ] **Ch1 Thm 5.11 — $\mathbb{Q}$ countable** / **有理数可数**:
  - **结论**: $\mathbb{Q}$ 可数
  - **要点**: 正有理既约 $p/q$ 注入 $\mathbb{N}\times\mathbb{N}$; $\mathbb{Q}=\mathbb{Q}^+\cup0\cup\mathbb{Q}^-$ 为可数并

- [ ] **Ch1 Thm 5.12 — Irrationals uncountable** / **无理数不可数**:
  - **结论**: $\mathbb{R}\setminus\mathbb{Q}$ 不可数
  - **要点**: 若可数则与 $\mathbb{Q}$ 可数合起来得 $\mathbb{R}$ 可数, 与 Thm 5.8 矛盾



### Chapter 2 Part 1 (Sequences)

- [ ] **Ch2 P1 Thm 1.6 — Uniqueness of limit** / **极限唯一性**:
  - **假设**: $(x_n)$ 收敛
  - **结论**: 极限唯一

- [ ] **Ch2 P1 Thm 2.2 — Convergent $\Rightarrow$ bounded** / **收敛 ⇒ 有界**:
  - **假设**: $(x_n)$ 收敛
  - **结论**: $(x_n)$ 有界 (逆命题一般假)

- [ ] **Ch2 P1 Thm 3.1 — Algebra of limits** / **极限运算**:
  - **假设**: $\lim x_n=x$, $\lim y_n=y$
  - **结论**: 和差积商 (分母极限非零) 的极限为对应运算

- [x] **Ch2 P1 Thm 3.6 — Squeeze theorem** / **夹逼定理**:
  - **假设**: $x_n\le y_n\le z_n$; $\lim x_n=\lim z_n=w$
  - **结论**: $\lim y_n=w$

- [x] **Ch2 P1 Thm 4.3 — Monotone Convergence Theorem (MCT)** / **单调收敛定理**:
  - **假设**: $(x_n)$ 单调
  - **结论**: 收敛 $\Leftrightarrow$ 有界; 有界递增时极限 $=\supx_n$

- [ ] **Ch2 P1 Thm 5.1 — Geometric sequence** / **几何序列**:
  - **假设**: $r\in\mathbb{R}$
  - **结论**: $0<r<1\Rightarrow r^n\to 0$; $r>1\Rightarrow(r^n)$ 发散 (细节以 slides 为准)

- [ ] **Ch2 P1 Thm 5.2 — $n^{1/n}\to 1$ 等** / **常用极限**:
  - **结论**: $n^{1/n}\to 1$ 等 (见讲义 Ch2 Part 1 §5)

- [ ] **Ch2 P1 Thm 5.4 — Euler number $e$** / **Euler 数 $e$**:
  - **结论**: $(1+1/n)^n\to e$ (定义/极限存在性见讲义)



### Chapter 2 Part 2 (Subsequences / BW / Cauchy)

- [ ] **Ch2 P2 Thm 1.6 — Subsequences of convergent sequences** / **收敛序列的子列同极限**:
  - **假设**: $(x_n)\to x$
  - **结论**: 任意子列亦 $\to x$

- [x] **Ch2 P2 Thm 2.1 — Monotone Subsequence Theorem** / **单调子列定理**:
  - **假设**: $(x_n)$ 为实序列
  - **结论**: 存在单调子列 (peak 论证)

- [x] **Ch2 P2 Thm 2.4 — Bolzano–Weierstrass Theorem** / **Bolzano–Weierstrass 定理**:
  - **假设**: $(x_n)$ 有界
  - **结论**: 存在收敛子列

- [x] **Ch2 P2 Thm 3.4 — Convergent $\Rightarrow$ Cauchy** / **收敛 ⇒ Cauchy**:
  - **假设**: $(x_n)$ 收敛
  - **结论**: $(x_n)$ 为 Cauchy

- [x] **Ch2 P2 Thm 3.6 — Cauchy $\Rightarrow$ convergent (completeness)** / **Cauchy ⇒ 收敛 (完备性)**:
  - **假设**: $(x_n)$ 为实 Cauchy 序列
  - **结论**: $(x_n)$ 收敛
  - **合写**: 与 Thm 3.4 合得 $\mathbb{R}$ 中收敛 $\Leftrightarrow$ Cauchy; 见下条 Cauchy 准则

- [ ] **Ch2 P2 Thm 3.4 + 3.6 — Cauchy criterion** / **Cauchy 准则**:
  - **假设**: $(x_n)$ 为实序列
  - **结论**: $(x_n)$ 收敛 $\Leftrightarrow$ $(x_n)$ 为 Cauchy 序列
  - **注**: 讲义把两端分开编号. $\Rightarrow$ 是 Thm 3.4, $\Leftarrow$ 是 Thm 3.6 (完备性). 2020 Test 1 第 2 题的 Cauchy criterion 指这个等价.



### Chapter 2 Part 3 (Series)

- [x] **Ch2 P3 Thm 2.1 — n-th series test (Term test)** / **n-th 项检验**:
  - **假设**: $\sum x_n$ 收敛
  - **结论**: $x_n\to 0$ (逆命题假: 调和级数)

- [x] **Ch2 P3 Thm 2.5 — Nonnegative series $\Leftrightarrow$ bounded partial sums** / **非负项级数 ⇔ 部分和有界**:
  - **假设**: $x_n\ge 0$
  - **结论**: $\sum x_n$ 收敛 $\Leftrightarrow$ $(s_n)$ 有界 (用 MCT)

- [x] **Ch2 P3 Thm 2.8 — Comparison Test** / **比较检验**:
  - **假设**: $0\le x_n\le y_n$
  - **结论**: $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛; $\sum x_n$ 发散 $\Rightarrow$ $\sum y_n$ 发散

- [x] **Ch2 P3 Thm 2.11 — Limit Comparison Test** / **极限比较检验**:
  - **假设**: $x_n,y_n>0$, $r=\lim(x_n/y_n)$ 存在
  - **结论**: $r\neq 0$ 时两者同敛散; $r=0$ 且 $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛

- [ ] **(自拟) — Cauchy condensation test** / **Cauchy 凝聚判别**:
  - **假设**: $a_n\ge 0$ 且 $(a_n)$ 递减
  - **结论**: $\sum_{n=1}^{\infty} a_n$ 收敛 $\Leftrightarrow$ $\sum_{n=0}^{\infty} 2^n a_{2^n}$ 收敛
  - **注**: slides 未编号; Tut4 第 6 题. $a_n=1/n^p$ ($p>0$) 时凝聚级数是公比 $2^{1-p}$ 的几何级数, 故 $p>1$ 收敛. 讲义 Lec07, $p$-级数之后

- [x] **Ch2 P3 Thm 3.3 — Absolute $\Rightarrow$ convergent** / **绝对收敛 ⇒ 收敛**:
  - **假设**: $\sum |x_k|$ 收敛
  - **结论**: $\sum x_k$ 收敛 (用 $0\le x+|x|\le 2|x|$)

- [x] **Ch2 P3 Thm 3.7 — Rearrangement Theorem** / **重排定理**:
  - **假设**: $\sum x_n$ 绝对收敛且和为 $L$; $\sum y_n$ 为其重排
  - **结论**: $\sum y_n\to L$ (条件收敛时一般不成立)

- [x] **Ch2 P3 Thm 3.13 — Alternating Series Test (Leibniz)** / **交错级数判别**:
  - **假设**: $x_n>0$ 递减且 $x_n\to 0$
  - **结论**: $\sum (-1)^{n+1}x_n$ 收敛

- [x] **Ch2 P3 Thm 3.16 — Root Test** / **根值检验**:
  - **假设**: $r=\lim\sqrt[n]{|x_n|}$ 存在
  - **结论**: $r<1$ 绝对收敛; $r>1$ 发散; $r=1$ 无效

- [x] **Ch2 P3 Thm 3.17 — Ratio Test** / **比值检验**:
  - **假设**: $x_n\neq 0$, $r=\lim|x_{n+1}|/|x_n|$ 存在
  - **结论**: $r<1$ 绝对收敛; $r>1$ 发散; $r=1$ 无效

### Chapter 3 Part 1 (Limits of functions)

- [ ] **Ch3 P1 Thm 1.5 — Sequential criterion for cluster points** / **聚点的序列刻画**:
  - **假设**: $A\subseteq\mathbb{R}$, $c\in\mathbb{R}$
  - **结论**: $c$ 是聚点 $\Leftrightarrow$ 存在 $x_n\in A\setminus\{c\}$ 使 $x_n\to c$

- [ ] **Ch3 P1 Thm 2.1 — Sequential criterion for functional limits** / **函数极限的序列准则**:
  - **假设**: $c$ 是 $A$ 的聚点, $f:A\to\mathbb{R}$
  - **结论**: $\lim_{x\to c}f=L$ $\Leftrightarrow$ 凡 $x_n\in A\setminus\{c\}$, $x_n\to c$ 都有 $f(x_n)\to L$

- [ ] **Ch3 P1 Thm 2.2 — Uniqueness of functional limits** / **函数极限唯一性**:
  - **假设**: $\lim_{x\to c}f=L$ 且 $=M$
  - **结论**: $L=M$

- [ ] **Ch3 P1 Thm 2.3 — Divergence criterion** / **发散准则**:
  - **假设**: 两序列在 $A\setminus\{c\}$ 中都 $\to c$, 但 $f$ 沿它们极限不同 (或不存在)
  - **结论**: $\lim_{x\to c}f$ 不存在

- [ ] **Ch3 P1 Thm 3.1 — Boundedness near a limit** / **有极限则局部有界**:
  - **假设**: $\lim_{x\to c}f$ 存在
  - **结论**: $f$ 在 $c$ 的某空心邻域上有界

- [ ] **Ch3 P1 Thm 4.6 — Squeeze theorem (functions)** / **函数夹逼定理**:
  - **假设**: 靠近 $c$ 有 $f\le g\le h$ 且 $\lim f=\lim h=L$
  - **结论**: $\lim g=L$

### Chapter 3 Part 2 (Continuity)

- [ ] **Ch3 P2 Thm 2.1 — Algebra of continuous functions** / **连续函数的代数运算**:
  - **假设**: $f,g$ 在 $c$ 连续
  - **结论**: $f\pm g$, $fg$ 在 $c$ 连续; $g(c)\ne0$ 时 $f/g$ 在 $c$ 连续

- [ ] **Ch3 P2 Thm 2.3 — Composition of continuous functions** / **连续函数的复合**:
  - **假设**: $f(A)\subset B$; $f$ 在 $c$ 连续, $g$ 在 $f(c)$ 连续
  - **结论**: $g\circ f$ 在 $c$ 连续

- [ ] **Ch3 P2 Thm 4.3 — Boundedness on a closed bounded interval** / **闭有界区间上连续则有界**:
  - **假设**: $I=[a,b]$, $f:I\to\mathbb{R}$ 连续
  - **结论**: $f$ 在 $I$ 上有界

- [ ] **Ch3 P2 Thm 5.4 — Extreme Value Theorem** / **最大最小值定理**:
  - **假设**: $I=[a,b]$, $f:I\to\mathbb{R}$ 连续
  - **结论**: $f$ 在 $I$ 上达到最大值与最小值

- [ ] **Ch3 P2 Thm 5.7 — Bolzano's intermediate value theorem** / **Bolzano 介值定理**:
  - **假设**: $I$ 为区间, $f:I\to\mathbb{R}$ 连续
  - **结论**: $f(I)$ 为区间 (特别地闭区间上异号则有根)

- [ ] **Ch3 P2 Thm 6.8 — Continuous on compact interval ⇒ uniformly continuous** / **闭有界区间上连续 ⇒ 一致连续**:
  - **假设**: $I=[a,b]$, $f:I\to\mathbb{R}$ 连续
  - **结论**: $f$ 在 $I$ 上一致连续

- [ ] **Ch3 P2 Thm 6.16 — Lipschitz ⇒ uniformly continuous** / **Lipschitz ⇒ 一致连续**:
  - **假设**: $f$ 为 Lipschitz
  - **结论**: $f$ 一致连续

---



## Corollaries / 推论

- [x] **Ch1 Cor 4.6 — Density of $\mathbb{Q}$** / **有理数稠密**:
  - **假设**: $a,b\in\mathbb{R}$ 且 $a<b$
  - **结论**: 存在 $r\in\mathbb{Q}$ 使 $a<r<b$
  - **要点**: 由 Archimedes 取 $n$ 使 $1/n<b-a$, 再取整数 $m$ 使 $a<m/n<b$
  - **注**: 无理数在 $\mathbb{R}$ 中亦稠密 (常作练习/推论)

- [ ] **Ch2 P1 Cor 2.5 — (见上 Lem 2.4 / Cor 2.5)** / **推论 2.5**:
  - **注**: 与 Lem 2.4 合写于同一条; 见上方 Lemmas 节

- [ ] **Ch2 P1 Cor 4.4 — Limit equals $\sup$/$\inf$ under MCT** / **MCT 下极限等于确界**:
  - **假设**: $(x_n)$ 有界单调
  - **结论**: 有界递增 $\Rightarrow$ $\lim x_n=\sup x_n$; 有界递减 $\Rightarrow$ $\lim x_n=\inf x_n$
  - **注**: 去掉单调则假 (讲义例: $x_1=3$, $x_n=2-1/n$ ($n\ge 2$) $\to 2$ 但 $\sup=3$)

---



## 例题级结果 / Examples (slides 编号, 常当事实用)

- [ ] **Ch2 P3 Ex 1.1 — Geometric series** / **几何级数**:
  - **假设**: $r>0$
  - **结论**: $0<r<1$ 时 $\sum_{k=1}^\infty r^k=r/(1-r)$; $r\ge 1$ 时发散

- [ ] **Ch2 P3 Ex 1.2 — Harmonic series diverges** / **调和级数发散**:
  - **结论**: $\sum 1/n$ 发散 (分组 $s_{2^k-1}>1+(k-1)/2$)

- [ ] **Ch2 P3 Ex 2.6 — $p$-harmonic ($p=2$)** / **$p$-调和级数 ($p=2$)**:
  - **假设**: $p=2$ (Exercise 2.7 把比较推广到 $p\ge 2$)
  - **结论**: $\sum 1/n^2$ 收敛 (分组后部分和有界)
  - **注**: 一般 $p$ 见下方 $p$-级数

- [ ] **(自拟) — $p$-series** / **$p$-级数**:
  - **假设**: $p\in\mathbb{R}$
  - **结论**: $\sum 1/n^p$ 收敛 $\Leftrightarrow$ $p>1$; $p\le 1$ 发散
  - **注**: 调和级数是 $p=1$. 课件 Ex 2.6 / Ex 2.7 只证 $p\ge 2$; $1<p<2$ 用分组或 Cauchy 凝聚, 公比 $2^{1-p}<1$. 讲义 Lec07 例 2.6 后

---



## (自拟) 补充整理

> 讲义未单独标号, 或作业/练习中整理的条目.

- [ ] **(自拟) — Relation max/min vs $\sup$/$\inf$** / **最值与确界关系**:
  - **假设**: $S\subseteq\mathbb{R}$ 非空
  - **保证**: 若 $\max S$ 存在则 $\max S=\sup S$; 若 $\min S$ 存在则 $\min S=\inf S$
  - **注**: 反之仅当确界落在 $S$ 内

- [ ] **(自拟) — Positive squares in ordered field** / **有序域中平方为正**:
  - **假设**: $F$ 有序域, $a\in F$, $a\neq 0$
  - **结论**: $a^2>0$; 特别地 $1>0$, 且 $1+1\neq 0$
  - **来源**: Ch1 Ex 1.7 要点

- [ ] **Ch1 Ex 1.7(g) — Square monotonicity for positives** / **正数平方单调**:
  - **假设**: $a,b>0$
  - **结论**: $a<b \iff a^2<b^2$

- [ ] **(自拟) — $\mathbb{Q}$ incomplete (standard example)** / **有理数不完备 (标准例)**:
  - **假设**: 在有序域 $\mathbb{Q}$ 中; $S=x\in\mathbb{Q}: x^2<2$
  - **结论**: $S$ 非空有上界, 但在 $\mathbb{Q}$ 中不存在 $\sup S$

- [x] **(自拟) — Cantor diagonal (idea)** / **康托对角线 (要点)**:
  - **假设**: 试图枚举 $[0,1]=x_n*{n=1}^\infty$, $x_n=0.a*{n1}a_{n2}\ldots$
  - **构造**: 取 $b_k\neq a_{kk}$ (如 $a_{kk}\neq 4$ 则 $b_k=4$, 否则 $b_k=5$), 得 $y=0.b_1b_2\ldots\in[0,1]$ 且 $y\neq x_n$ 对一切 $n$
  - **用途**: 支撑 Ch1 Thm 5.8

- [x] **(自拟) — Contractive $\Rightarrow$ Cauchy** / **压缩序列 ⇒ Cauchy**:
  - **假设**: $|x_{n+2}-x_{n+1}|\le C|x_{n+1}-x_n|$, $0<C<1$
  - **结论**: $(x_n)$ 为 Cauchy (故在 $\mathbb{R}$ 中收敛)
  - **来源**: Ch2 Part 2 练习/例题脉络

- [ ] **(自拟) — Bijection / Injection / Surjection** / **双射/单射/满射**:
  - **假设**: 映射 $f:A\to B$
  - **定义 (单射)**: $f(x)=f(y)\Rightarrow x=y$
  - **定义 (满射)**: $\forall b\in B,\ \exists a\in A,\ f(a)=b$
  - **定义 (双射)**: 既单又满 (等价于存在逆映射)
  - **用途**: 可数性定义的前置语言

- [ ] **(自拟) — Nested intervals (术语)** / **嵌套区间 (术语)**:
  - **假设**: 闭区间列 $I_n=[a_n,b_n]$
  - **定义 (嵌套)**: $\forall n,\ I_{n+1}\subseteq I_n$ (即 $a_n\le a_{n+1}\le b_{n+1}\le b_n$)
  - **用途**: Ch1 Thm 5.5 的假设语言

- [x] **(自拟) — Archimedean property (术语汇总)** / **阿基米德性质**:
  - **假设**: 在 $\mathbb{R}$ 中
  - **结论**: $\mathbb{N}$ 无上界; $\forall x,\ \exists n,\ n>x$; $\forall\varepsilon>0,\ \exists n,\ 1/n<\varepsilon$
  - **对应**: Ch1 Thm 4.1–4.2

- [x] **(自拟) — Dense (术语)** / **稠密**:
  - **假设**: $A,B\subseteq\mathbb{R}$
  - **定义 ($A$ 在 $B$ 中稠密)**: 对任意 $a,b\in B$ 且 $a<b$, 存在 $r\in A$ 使 $a<r<b$
  - **典型**: $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密 (Ch1 Cor 4.6)

- [ ] **(自拟) — Irrational number** / **无理数**:
  - **假设**: $x\in\mathbb{R}$
  - **定义**: $x\notin\mathbb{Q}$
  - **典型**: $\sqrt{2}=\sup y\in\mathbb{R}: y^2<2$ (Ch1 Thm 4.8–4.9)

- [ ] **(自拟) — Bounded set** / **有界集**:
  - **假设**: $S\subseteq F$, $F$ 有序域
  - **定义**: 既有上界又有下界

---



## 易错对照

- [ ] **max vs $\sup$**:
  - **假设**: 讨论 $S$ 的「最大」与「上确界」
  - **结论**: $\sup$ 总谈最小上界; 仅当该点 $\in S$ 时才是 $\max$

- [ ] **completeness is about $\mathbb{R}$**:
  - **假设**: 在 $\mathbb{Q}$ 内找确界
  - **结论**: 可能不存在; 完备性是 $\mathbb{R}$ 相对 $\mathbb{Q}$ 的关键公理

- [ ] **countable proofs**:
  - **假设**: 证 $\mathbb{Q}$ 可数
  - **结论**: 用既约分数注入 (勿宣称「$\mathbb{Q}$ 与 $\mathbb{N}$ 一样稀」与稠密矛盾 — 稠密是序/拓扑语言, 可数是基数语言)

- [ ] **Ch2: convergent $\Rightarrow$ bounded 之逆**:
  - **结论**: 有界不必收敛 (例 $(-1)^n$); 需 MCT / BW / Cauchy 等额外条件

- [ ] **Ch2: term test 之逆**:
  - **结论**: $x_n\to 0$ 不必级数收敛 (调和级数)

- [ ] **Ch2: absolute vs conditional**:
  - **结论**: 绝对 $\Rightarrow$ 收敛; 条件收敛时重排一般改变和 (对照 Ch2 P3 Thm 3.7)

---



## 问答沉淀

*(待补充)*