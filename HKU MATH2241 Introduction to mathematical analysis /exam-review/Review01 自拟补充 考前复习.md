# MATH2241 背诵 — cheatsheet 已勾选 `[x]`

> 只含 `cheatsheet.md` 中 `[x]` 条目. 按 slides / 讲义出现顺序排列 (非 cheatsheet 类型分节).

## Chapter 1

+ **Ch1 Def 1.1 — Field** / **域**:
    + **假设**: 集合 $F$ 上有二元运算加法 $+:F\times F\to F$ 与乘法 $\cdot:F\times F\to F$
    + **定义**: 以下性质全部成立:
        + **(A1) 加法交换律** (commutativity for addition): $a+b=b+a$ ($\forall a,b\in F$)
        + **(A2) 加法结合律** (associativity for addition): $(a+b)+c=a+(b+c)$
        + **(A3) 零元存在** (existence of a zero element): $\exists0\in F$ 使 $0+a=a+0=a$ ($\forall a\in F$)
        + **(A4) 加法逆存在** (existence of negatives): $\forall a\in F$, $\exists(-a)\in F$ 使 $a+(-a)=(-a)+a=0$
        + **(M1) 乘法交换律** (commutativity for multiplication): $a\cdot b=b\cdot a$
        + **(M2) 乘法结合律** (associativity for multiplication): $a\cdot(b\cdot c)=(a\cdot b)\cdot c$
        + **(M3) 单位元存在** (existence of an identity element): $\exists1\in F$, $1\neq 0$, 使 $1\cdot a=a\cdot 1=a$
        + **(M4) 乘法逆存在** (existence of multiplicative inverses): $\forall a\in F$, $a\neq 0$, $\exists1/a\in F$ 使 $a\cdot(1/a)=(1/a)\cdot a=1$
        + **(D) 分配律** (distributive property): $a\cdot(b+c)=a\cdot b+a\cdot c$ ($\forall a,b,c\in F$)
    + **记号**: $a-b:=a+(-b)$; $a/b:=a\cdot(1/b)$ ($b\neq 0$); 亦可写 $a^{-1}$ 表示 $1/a$
    + **注**: $0$, $1$, $-a$, $1/a$ ($a\neq 0$) 唯一 (Ex 1.2)

+ **Ch1 Def 1.6 — Ordered field** / **有序域**:
    + **假设**: $F$ 为域, 且带关系 $\le$
    + **定义**: $\le$ 满足:
        + **(O1) 全序 / 可比较** : $\forall a,b\in F$, $a\le b$ 或 $b\le a$
        + **(O2) 反对称** : 若 $a\le b$ 且 $b\le a$, 则 $a=b$
        + **(O3) 传递** : 若 $a\le b$ 且 $b\le c$, 则 $a\le c$
        + **(O4) 与加法相容** : 若 $a\le b$, 则 $a+c\le b+c$ ($\forall c$)
        + **(O5) 与非负乘法相容** : 若 $a\le b$ 且 $c\ge 0$, 则 $ac\le bc$
    + **严格序**: $a<b$ 当且仅当 $a\le b$ 且 $a\neq b$
    + **例子**: $\mathbb{Q},\mathbb{R}$ 可序; $\mathbb{C}$ (或含 $i$ 的域) **不能**成为有序域 ($a\neq 0\Rightarrow a^2>0$ 与 $i^2=-1$ 矛盾)

+ **Ch1 Def 3.8–3.9 — Completeness axiom / Complete ordered field** / **完备性公理/完备有序域**:
    + **假设**: $F$ 为有序域
    + **定义 (完备)**: 每个非空且有上界的子集 $S\subseteq F$ 在 $F$ 中都有 $\sup S$
    + **约定**: $\mathbb{R}$ 定义为完备有序域 (存在且在同构意义下唯一, 含 $\mathbb{N},\mathbb{Z},\mathbb{Q}$)
    + **对比**: $\mathbb{Q}$ **不完备**; 例 $S=x\in\mathbb{Q}: x^2<2$ 在 $\mathbb{Q}$ 中无上确界

+ **(自拟) — Archimedean property (术语汇总)** / **阿基米德性质**:
    + **假设**: 在 $\mathbb{R}$ 中
    + **结论**: $\mathbb{N}$ 无上界; $\forall x,\ \exists n,\ n>x$; $\forall\varepsilon>0,\ \exists n,\ 1/n<\varepsilon$
    + **对应**: Ch1 Thm 4.1–4.2

+ **(自拟) — Dense (术语)** / **稠密**:
    + **假设**: $A,B\subseteq\mathbb{R}$
    + **定义 ($A$ 在 $B$ 中稠密)**: 对任意 $a,b\in B$ 且 $a<b$, 存在 $r\in A$ 使 $a<r<b$
    + **典型**: $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密 (Ch1 Cor 4.6)

+ **Ch1 Cor 4.6 — Density of $\mathbb{Q}$** / **有理数稠密**:
    + **假设**: $a,b\in\mathbb{R}$ 且 $a<b$
    + **结论**: 存在 $r\in\mathbb{Q}$ 使 $a<r<b$
    + **要点**: 由 Archimedes 取 $n$ 使 $1/n<b-a$, 再取整数 $m$ 使 $a<m/n<b$
    + **注**: 无理数在 $\mathbb{R}$ 中亦稠密 (常作练习/推论)

+ **Ch1 Thm 5.5 — Nested Interval Property** / **嵌套区间性质**:
    + **假设**: $I_n$ 为闭区间, $I_n=[a_n,b_n]$, 且嵌套: $I_{n+1}\subseteq I_n$ 对一切 $n$
    + **结论**: $\bigcap_{n=1}^\infty I_n\neq\emptyset$; 事实上 $c=\sup a_n$ 属于交
    + **注**: 开区间嵌套未必非空交; 长度 $\to 0$ 时交为单点 (后续常用)

+ **Ch1 Def 5.6 — Countable / Uncountable** / **可数/不可数**:
    + **假设**: 集合 $A$
    + **定义 (可数)**: $A$ 有限, 或存在双射 $A\leftrightarrow\mathbb{N}$
    + **定义 (不可数)**: 非可数
    + **注**: 可数个可数集之并仍可数; 可数集的子集可数

+ **(自拟) — Cantor diagonal (idea)** / **康托对角线 (要点)**:
    + **假设**: 试图枚举 $[0,1]=x_n*{n=1}^\infty$, $x_n=0.a*{n1}a_{n2}\ldots$
    + **构造**: 取 $b_k\neq a_{kk}$ (如 $a_{kk}\neq 4$ 则 $b_k=4$, 否则 $b_k=5$), 得 $y=0.b_1b_2\ldots\in[0,1]$ 且 $y\neq x_n$ 对一切 $n$
    + **用途**: 支撑 Ch1 Thm 5.8

+ **(自拟) — Countability of $\mathbb{Q}$: map into $\mathbb{N}$** / **$\mathbb{Q}$ 可数: 构造映射**:
    + **目标**: 证 $\mathbb{Q}$ 可数 — 常构造**单射** $\mathbb{Q}\hookrightarrow\mathbb{N}$ (或给出与 $\mathbb{N}$ 的双射 / 枚举)
    + **Step 1 (正有理)**: 每个 $r\in\mathbb{Q}^+$ 写成既约分数 $r=m/n$ ($m,n\in\mathbb{N}$, $\gcd(m,n)=1$). 得单射
      $$
      \mathbb{Q}^+\hookrightarrow\mathbb{N}\times\mathbb{N},\qquad \frac{m}{n}\mapsto(m,n).
      $$
    + **Step 2 ($\mathbb{N}\times\mathbb{N}$ 可数)**: 构造双射 (或单射) $\mathbb{N}\times\mathbb{N}\to\mathbb{N}$, 例如 Cantor pairing
      $$
      (m,n)\mapsto 2^{m-1}(2n-1)
      $$
      (奇数因子唯一分解 $\Rightarrow$ 双射). 或用对角线枚举: 按 $m+n=2,3,4,\ldots$ 扫格子.
    + **Step 3 (全体有理)**: $\mathbb{Q}=\{0\}\cup\mathbb{Q}^+\cup\mathbb{Q}^-$ 是三个可数集之并, 故可数. 负有理用 $-m/n\mapsto$ 另一份 $\mathbb{N}\times\mathbb{N}$ (或整体嵌入 $\mathbb{Z}\times\mathbb{N}$).
    + **考试写法**: 「既约 $\Rightarrow$ 单射进 $\mathbb{N}\times\mathbb{N}$」+「$\mathbb{N}\times\mathbb{N}\sim\mathbb{N}$」+「可数并」; 不必把每个有理的编号公式全写开.
    + **对比**: 这是**可数**构造; 下一则对角线是**不可数**反证, 不要混.

## Chapter 2 Part 1 (Sequences)

+ **Ch2 P1 Thm 3.6 — Squeeze theorem** / **夹逼定理**:
    + **假设**: $x_n\le y_n\le z_n$; $\lim x_n=\lim z_n=w$
    + **结论**: $\lim y_n=w$

+ **Ch2 P1 Thm 4.3 — Monotone Convergence Theorem (MCT)** / **单调收敛定理**:
    + **假设**: $(x_n)$ 单调
    + **结论**: 收敛 $\Leftrightarrow$ 有界; 有界递增时极限 $=\sup x_n$

## Chapter 2 Part 2 (Subsequences / Cauchy)

+ **Ch2 P2 Thm 2.1 — Monotone Subsequence Theorem** / **单调子列定理**:
    + **假设**: $(x_n)$ 为实序列
    + **结论**: 存在单调子列 (peak 论证)

+ **Ch2 P2 Thm 2.4 — Bolzano–Weierstrass Theorem** / **Bolzano–Weierstrass 定理**:
    + **假设**: $(x_n)$ 有界
    + **结论**: 存在收敛子列

+ **Ch2 P2 Def 3.1 — Cauchy sequence** / **Cauchy 序列**:
    + **定义**: $\forall\varepsilon>0$, $\exists N$ 使 $n,m>N\Rightarrow|x_n-x_m|<\varepsilon$

+ **Ch2 P2 Thm 3.4 — Convergent $\Rightarrow$ Cauchy** / **收敛 ⇒ Cauchy**:
    + **假设**: $(x_n)$ 收敛
    + **结论**: $(x_n)$ 为 Cauchy

+ **Ch2 P2 Lem 3.5 — Cauchy $\Rightarrow$ bounded** / **Cauchy ⇒ 有界**:
    + **假设**: $(x_n)$ 为 Cauchy 序列
    + **结论**: $(x_n)$ 有界

+ **Ch2 P2 Thm 3.6 — Cauchy $\Rightarrow$ convergent (completeness)** / **Cauchy ⇒ 收敛 (完备性)**:
    + **假设**: $(x_n)$ 为实 Cauchy 序列
    + **结论**: $(x_n)$ 收敛
    + **合写**: 与 Thm 3.4 合得 $\mathbb{R}$ 中收敛 $\Leftrightarrow$ Cauchy

+ **(自拟) — Contractive $\Rightarrow$ Cauchy** / **压缩序列 ⇒ Cauchy**:
    + **假设**: $|x_{n+2}-x_{n+1}|\le C|x_{n+1}-x_n|$, $0<C<1$
    + **结论**: $(x_n)$ 为 Cauchy (故在 $\mathbb{R}$ 中收敛)
    + **来源**: Ch2 Part 2 练习/例题脉络

## Chapter 2 Part 3 (Series)

+ **Ch2 P3 Thm 2.1 — n-th series test (Term test)** / **n-th 项检验**:
    + **假设**: $\sum x_n$ 收敛
    + **结论**: $x_n\to 0$ (逆命题假: 调和级数)

+ **Ch2 P3 Thm 2.5 — Nonnegative series $\Leftrightarrow$ bounded partial sums** / **非负项级数 ⇔ 部分和有界**:
    + **假设**: $x_n\ge 0$
    + **结论**: $\sum x_n$ 收敛 $\Leftrightarrow$ $(s_n)$ 有界 (用 MCT)

+ **Ch2 P3 Thm 2.8 — Comparison Test** / **比较检验**:
    + **假设**: $0\le x_n\le y_n$
    + **结论**: $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛; $\sum x_n$ 发散 $\Rightarrow$ $\sum y_n$ 发散

+ **Ch2 P3 Thm 2.11 — Limit Comparison Test** / **极限比较检验**:
    + **假设**: $x_n,y_n>0$, $r=\lim(x_n/y_n)$ 存在
    + **结论**: $r\neq 0$ 时两者同敛散; $r=0$ 且 $\sum y_n$ 收敛 $\Rightarrow$ $\sum x_n$ 收敛

+ **Ch2 P3 Def 3.1 — Absolute convergence** / **绝对收敛**:
    + **定义**: $\sum |x_k|$ 收敛

+ **Ch2 P3 Thm 3.3 — Absolute $\Rightarrow$ convergent** / **绝对收敛 ⇒ 收敛**:
    + **假设**: $\sum |x_k|$ 收敛
    + **结论**: $\sum x_k$ 收敛 (用 $0\le x+|x|\le 2|x|$)

+ **Ch2 P3 Def 3.6 — Rearrangement** / **重排**:
    + **定义**: 序列 $(y_n)$ 是 $(x_n)$ 的重排, 若存在双射 $\sigma:\mathbb{N}\to\mathbb{N}$ 使 $y_n=x_{\sigma(n)}$

+ **Ch2 P3 Thm 3.7 — Rearrangement Theorem** / **重排定理**:
    + **假设**: $\sum x_n$ 绝对收敛且和为 $L$; $\sum y_n$ 为其重排
    + **结论**: $\sum y_n\to L$ (条件收敛时一般不成立)

+ **Ch2 P3 Def 3.9 — Conditional convergence** / **条件收敛**:
    + **定义**: $\sum x_n$ 收敛但非绝对收敛

+ **Ch2 P3 Thm 3.13 — Alternating Series Test (Leibniz)** / **交错级数判别**:
    + **假设**: $(x_n)$ 严格正且递减, 且 $\lim x_n=0$
    + **结论**: $\sum (-1)^{n+1}x_n$ 收敛
    + **证明要点**: 偶部分和 $s_{2k}=(x_1-x_2)+\cdots+(x_{2k-1}-x_{2k})$ 递增, 且 $s_{2k}<x_1$, 由 MCT 收敛到某 $L$; $s_{2k+1}=s_{2k}+x_{2k+1}\to L$. 有限项不影响敛散, 故「从某项起递减」即可用

+ **Ch2 P3 Thm 3.16 — Root Test** / **根值检验**:
    + **假设**: $r=\lim\sqrt[n]{|x_n|}$ 存在
    + **结论**: $r<1$ 绝对收敛; $r>1$ 发散; $r=1$ 无效

+ **Ch2 P3 Thm 3.17 — Ratio Test** / **比值检验**:
    + **假设**: $x_n\neq 0$, $r=\lim|x_{n+1}|/|x_n|$ 存在
    + **结论**: $r<1$ 绝对收敛; $r>1$ 发散; $r=1$ 无效
