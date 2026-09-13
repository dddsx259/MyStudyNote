# MATH2241 Cheatsheet

> 词条/公式/定理速查; 对话中学到的内容会增量追加.
> 约定: **定义 / 定理 / 引理 / 命题 / 推论** (及带保证的公式) 一律写清 **假设** 与 **结论** (或 **定义**); 证明见对应讲义, 本表不放完整证明.

---

## 名词 (定义)

+ **Field** / **域**:
    + **假设**: 集合 $F$ 上有二元运算 $+$ 与 $\cdot$
    + **定义**: 满足 (A1)–(A4) 加法公理, (M1)–(M4) 乘法公理, 及 (D) 分配律; 即能加减乘除 (除数非零)
    + **注**: 单位元 $0,1$, 逆元 $-a$, $a^{-1}$ ($a\neq 0$) 唯一

+ **Ordered field** / **有序域**:
    + **假设**: $F$ 为域, 且带关系 $\le$
    + **定义**: $\le$ 为全序 (total order), 且满足 (O1)–(O5) (与加法/正乘法相容); $a<b$ 当 $a\le b$ 且 $a\neq b$
    + **例子**: $\mathbb{Q},\mathbb{R}$ 可序; $\mathbb{C}$ (或含 $i$ 的域) **不能**成为有序域 ($a\neq 0\Rightarrow a^2>0$ 与 $i^2=-1$ 矛盾)

+ **Upper bound / Lower bound** / **上界/下界**:
    + **假设**: $S\subseteq F$, $F$ 有序域; $M,m\in F$
    + **定义 (上界)**: $\forall x\in S,\ x\le M$
    + **定义 (下界)**: $\forall x\in S,\ m\le x$
    + **注**: 有上界 $\not\Rightarrow$ 有最大值

+ **Maximum / Minimum** / **最大值/最小值**:
    + **假设**: $S\subseteq F$, $F$ 有序域
    + **定义 (max)**: 存在 $s_0\in S$ 使 $\forall x\in S,\ x\le s_0$ (须在集内)
    + **定义 (min)**: 对偶, $s_0\in S$ 且 $\forall x\in S,\ s_0\le x$
    + **例**: $\{x\in\mathbb{Q}: 0\le x<8\}$ 有上界但无 max

+ **Supremum / Infimum** / **上确界/下确界**:
    + **假设**: $S\subseteq F$ 非空, $F$ 有序域
    + **定义 ($\sup S$)**: 上界集合中的**最小上界** (least upper bound)
    + **定义 ($\inf S$)**: 下界集合中的**最大下界** (greatest lower bound)
    + **注**: $\sup/\inf$ **可以不在** $S$ 内; 若 $\sup S\in S$ 则 $\sup S=\max S$

+ **Bounded set** / **有界集**:
    + **假设**: $S\subseteq F$, $F$ 有序域
    + **定义**: 既有上界又有下界 (即 $\exists m,M$ 使 $m\le x\le M$ 对一切 $x\in S$)

+ **Completeness axiom / Complete ordered field** / **完备性公理/完备有序域**:
    + **假设**: $F$ 为有序域
    + **定义 (完备)**: 每个非空且有上界的子集 $S\subseteq F$ 在 $F$ 中都有 $\sup S$
    + **约定**: $\mathbb{R}$ 定义为完备有序域 (存在且在同构意义下唯一, 含 $\mathbb{N},\mathbb{Z},\mathbb{Q}$)
    + **对比**: $\mathbb{Q}$ **不完备**; 例 $S=\{x\in\mathbb{Q}: x^2<2\}$ 在 $\mathbb{Q}$ 中无上确界

+ **Archimedean property** / **阿基米德性质**:
    + **假设**: 在 $\mathbb{R}$ (完备有序域) 中
    + **定义/结论**: $\mathbb{N}$ 在 $\mathbb{R}$ 中无上界; 等价地, $\forall x\in\mathbb{R},\ \exists n\in\mathbb{N},\ n>x$; 亦有 $\forall\varepsilon>0,\ \exists n,\ 1/n<\varepsilon$

+ **Dense** / **稠密**:
    + **假设**: $A,B\subseteq\mathbb{R}$ (或更一般有序集)
    + **定义 ($A$ 在 $B$ 中稠密, 课程常用)**: 对任意 $a,b\in B$ 且 $a<b$, 存在 $r\in A$ 使 $a<r<b$
    + **典型**: $\mathbb{Q}$ 在 $\mathbb{R}$ 中稠密 (见 Cor. 4.6); 无理数在 $\mathbb{R}$ 中亦稠密

+ **Irrational number** / **无理数**:
    + **假设**: $x\in\mathbb{R}$
    + **定义**: $x\notin\mathbb{Q}$
    + **典型**: $\sqrt{2}=\sup\{y\in\mathbb{R}: y^2<2\}$ (见 Thm 4.8–4.9)

+ **Countable / Uncountable** / **可数/不可数**:
    + **假设**: 集合 $A$
    + **定义 (可数)**: $A$ 有限, 或存在双射 $A\leftrightarrow\mathbb{N}$ (可与 $\mathbb{N}$ 一一对应)
    + **定义 (不可数)**: 非可数
    + **注**: 可数个可数集之并仍可数; 可数集的子集可数

+ **Bijection / Injection / Surjection** / **双射/单射/满射**:
    + **假设**: 映射 $f:A\to B$
    + **定义 (单射)**: $f(x)=f(y)\Rightarrow x=y$
    + **定义 (满射)**: $\forall b\in B,\ \exists a\in A,\ f(a)=b$
    + **定义 (双射)**: 既单又满 (等价于存在逆映射)

+ **Nested intervals** / **嵌套区间**:
    + **假设**: 闭区间列 $I_n=[a_n,b_n]$
    + **定义 (嵌套)**: $\forall n,\ I_{n+1}\subseteq I_n$ (即 $a_n\le a_{n+1}\le b_{n+1}\le b_n$)

+ **Interval notation** / **区间记号**:
    + **定义**: $(a,b)=\{x: a<x<b\}$; $[a,b]=\{x: a\le x\le b\}$; 半开 $(a,b],[a,b)$; 无界 $(-\infty,a]$, $[a,\infty)$, $\mathbb{R}=(-\infty,\infty)$

+ **Well-ordering of N** / **自然数良序**:
    + **假设**: $A\subseteq\mathbb{N}$ 非空
    + **结论**: $A$ 有最小元 (least element)

+ **Dedekind cut** / **戴德金分割** (Assignment 1):
    + **假设**: $\alpha\subsetneq\mathbb{Q}$
    + **定义**: (1) $\alpha\neq\emptyset$, $\alpha\neq\mathbb{Q}$; (2) 向下封闭: $x\in\alpha$, $y<x$ $\Rightarrow$ $y\in\alpha$; (3) 无最大元: $\forall x\in\alpha,\ \exists z\in\alpha,\ x<z$
    + **约定**: $\mathbb{R}'=$ 全体 Dedekind cuts; 有理嵌入 $\hat r=\{q\in\mathbb{Q}: q<r\}$

---

## 公式 / 判别法

+ **Supremum criterion (Thm 3.3 形式)** / **上确界判别**:
    + **假设**: $S\subseteq\mathbb{R}$ 非空, $u\in\mathbb{R}$ 为 $S$ 的上界
    + **保证**: $u=\sup S$ $\iff$ $\forall\epsilon>0,\ \exists x\in S$ 使 $u-x<\epsilon$ (即 $x>u-\epsilon$)
    + **对偶 (inf)**: $v=\inf S$ $\iff$ $v$ 为下界且 $\forall\epsilon>0,\ \exists x\in S,\ x-v<\epsilon$

+ **Relation max/min vs sup/inf** / **最值与确界关系**:
    + **假设**: $S\subseteq\mathbb{R}$ 非空
    + **保证**: 若 $\max S$ 存在则 $\max S=\sup S$; 若 $\min S$ 存在则 $\min S=\inf S$
    + **注**: 反之仅当确界落在 $S$ 内

+ **Positive squares in ordered field** / **有序域中平方为正**:
    + **假设**: $F$ 有序域, $a\in F$, $a\neq 0$
    + **结论**: $a^2>0$; 特别地 $1>0$, 且 $1+1\neq 0$

+ **Square monotonicity for positives** / **正数平方单调** (Ex. 1.7(g)):
    + **假设**: $a,b>0$
    + **结论**: $a<b \iff a^2<b^2$

+ **Cantor diagonal (idea)** / **康托对角线 (要点)**:
    + **假设**: 试图枚举 $[0,1]=\{x_n\}_{n=1}^\infty$, $x_n=0.a_{n1}a_{n2}\ldots$
    + **构造**: 取 $b_k\neq a_{kk}$ (如 $a_{kk}\neq 4$ 则 $b_k=4$, 否则 $b_k=5$), 得 $y=0.b_1b_2\ldots\in[0,1]$ 且 $y\neq x_n$ 对一切 $n$

---

## 定理

+ **Proposition 1.5 (field corollaries)** / **域的常用推论**:
    + **假设**: $F$ 为域, $a,b\in F$
    + **结论**: $0\cdot a=0$; $-(-a)=a$; $(-a)(-b)=ab$; 以及 $(-a)b=a(-b)=-(ab)$ 等

+ **Theorem 3.3 (Supremum criterion)** / **上确界判别法**:
    + **假设**: $S\subseteq\mathbb{R}$ 非空; $u\in\mathbb{R}$ 是 $S$ 的一个上界
    + **结论**: $u=\sup S$ 当且仅当对任意 $\epsilon>0$, 存在 $x\in S$ 满足 $x>u-\epsilon$

+ **Theorem 4.1–4.2 (N unbounded / Archimedean)** / **$\mathbb{N}$ 无界与阿基米德**:
    + **假设**: 在完备有序域 $\mathbb{R}$ 中
    + **结论**: $\mathbb{N}$ 无上界; 对任意 $x\in\mathbb{R}$ 存在 $n\in\mathbb{N}$ 使 $n>x$; 对 $a<b$ 可取 $n$ 使 $1/n<b-a$

+ **Corollary 4.6 (Density of Q)** / **有理数稠密**:
    + **假设**: $a,b\in\mathbb{R}$ 且 $a<b$
    + **结论**: 存在 $r\in\mathbb{Q}$ 使 $a<r<b$
    + **要点**: 由 Archimedes 取 $n$ 使 $1/n<b-a$, 再取整数 $m$ 使 $a<m/n<b$

+ **Theorem 4.8 ($\sqrt{2}$ irrational — no rational square)** / **无有理数平方为 2**:
    + **假设**: $x\in\mathbb{Q}$
    + **结论**: $x^2\neq 2$ (即不存在有理数其平方等于 2)
    + **要点**: 既约分数 $p/q$ 反证得 $p,q$ 皆偶, 矛盾

+ **Theorem 4.9 (existence of $\sqrt{2}$ via sup)** / **用上确界构造 $\sqrt{2}$**:
    + **假设**: 在 $\mathbb{R}$ (完备) 中; 令 $S=\{y\in\mathbb{R}: y\ge 0,\ y^2<2\}$
    + **结论**: $x:=\sup S$ 满足 $x^2=2$, 且由 Thm 4.8 得 $x\notin\mathbb{Q}$
    + **要点**: 排除 $x^2<2$ (可再抬高) 与 $x^2>2$ (可压低上界)

+ **Theorem 5.5 (Nested Interval Property)** / **嵌套区间性质**:
    + **假设**: $\{I_n\}$ 为闭区间, $I_n=[a_n,b_n]$, 且嵌套: $I_{n+1}\subseteq I_n$ 对一切 $n$
    + **结论**: $\bigcap_{n=1}^\infty I_n\neq\emptyset$; 事实上 $c=\sup\{a_n\}$ 属于交
    + **注**: 开区间嵌套未必非空交; 长度 $\to 0$ 时交为单点 (后续常用)

+ **Theorem 5.8 (R uncountable)** / **实数不可数**:
    + **假设**: 无 (在标准 $\mathbb{R}$ 设定下)
    + **结论**: $\mathbb{R}$ 不可数; 等价地 $[0,1]$ 不可数
    + **要点**: 康托对角线论证于 $[0,1]$ 的十进/二进展开

+ **Theorem 5.9 (Z countable)** / **整数可数**:
    + **假设**: 无
    + **结论**: $\mathbb{Z}$ 可数
    + **要点**: 枚举 $0,1,-1,2,-2,\ldots$

+ **Theorem 5.10 ($\mathbb{N}\times\mathbb{N}$ countable)** / **$\mathbb{N}\times\mathbb{N}$ 可数**:
    + **假设**: 无
    + **结论**: $\mathbb{N}\times\mathbb{N}$ 可数
    + **要点**: 对角线枚举, 或双射 $(m,n)\mapsto 2^{m-1}(2n-1)$

+ **Theorem 5.11 (Q countable)** / **有理数可数**:
    + **假设**: 无
    + **结论**: $\mathbb{Q}$ 可数
    + **要点**: 正有理既约 $p/q$ 注入 $\mathbb{N}\times\mathbb{N}$; $\mathbb{Q}=\mathbb{Q}^+\cup\{0\}\cup\mathbb{Q}^-$ 为可数并

+ **Theorem 5.12 (irrationals uncountable)** / **无理数不可数**:
    + **假设**: 无
    + **结论**: $\mathbb{R}\setminus\mathbb{Q}$ 不可数
    + **要点**: 若可数则与 $\mathbb{Q}$ 可数合起来得 $\mathbb{R}$ 可数, 与 5.8 矛盾

+ **Q incomplete (standard example)** / **有理数不完备 (标准例)**:
    + **假设**: 在有序域 $\mathbb{Q}$ 中; $S=\{x\in\mathbb{Q}: x^2<2\}$
    + **结论**: $S$ 非空有上界, 但在 $\mathbb{Q}$ 中不存在 $\sup S$

---

## 易错对照

+ **max vs sup**:
    + **假设**: 讨论 $S$ 的「最大」与「上确界」
    + **结论**: $\sup$ 总谈最小上界; 仅当该点 $\in S$ 时才是 $\max$

+ **completeness is about R**:
    + **假设**: 在 $\mathbb{Q}$ 内找确界
    + **结论**: 可能不存在; 完备性是 $\mathbb{R}$ 相对 $\mathbb{Q}$ 的关键公理

+ **countable proofs**:
    + **假设**: 证 $\mathbb{Q}$ 可数
    + **结论**: 用既约分数注入 (勿宣称「$\mathbb{Q}$ 与 $\mathbb{N}$ 一样稀」与稠密矛盾 — 稠密是序/拓扑语言, 可数是基数语言)

---

## 问答沉淀

_(待补充)_
