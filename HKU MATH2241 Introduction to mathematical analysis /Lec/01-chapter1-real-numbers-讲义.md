# Chapter 1: 实数 (Real Numbers)

- **来源**: `Lec/02-chapter1-real-numbers.pdf`
- **课程**: MATH2241, Fall 2026, K.Y. Chan
- **前置**: 集合/逻辑基础
- **本章目标**: 域 (field) 与序 (order), 上下界/上确界/下确界 (sup/inf), 完备性 (completeness), 有理数稠密 (density of $\mathbb{Q}$), 无理数 (irrational numbers), $\mathbb{R}$ 不可数 (uncountability)
- **说明**: 凡非定义公式/定理均附 **证明** / **证明思路**; 纯定义标「定义, 无需证明」.

## 本章在课程中的位置

实分析 (real analysis) 从**公理化重建**实数、极限、微分、积分; 本章是整个课程的基石: 没有完备性就无法严格讨论极限与连续.

---

## 1. 域与代数性质

### 定义 1.1 (域)

集合 $F$ 上有加法 $+$ 与乘法 $\cdot$, 满足 (A1)–(A4), (M1)–(M4), (D) 分配律 (distributive law). (定义, 无需证明.)

**直觉**: 像 $\mathbb{Q}$ 一样能加减乘除 (除数非零).

### 命题 1.5 (常用推论)

- $0a=0$, $-(-a)=a$, $(-a)(-b)=ab$ 等

**证明思路** ($0a=0$): 由加法单位元与分配律,
$$
0a+0a=(0+0)a=0a.
$$
两边加 $-(0a)$ 得 $0a=0$.

**证明思路** ($-(-a)=a$): $-(-a)$ 是 $(-a)$ 的加法逆. 又 $a+(-a)=0$, 故 $a$ 也是 $(-a)$ 的加法逆. 由逆元唯一性得 $-(-a)=a$.

**证明思路** ($(-a)(-b)=ab$): 先证 $(-a)b=-(ab)$: 因
$$
(-a)b+ab=(-a+a)b=0b=0,
$$
故 $(-a)b$ 是 $ab$ 的加法逆. 同理 $a(-b)=-(ab)$. 于是
$$
(-a)(-b)=-\bigl(a(-b)\bigr)=-\bigl(-(ab)\bigr)=ab.
$$

### 练习 1.2

0, 1, $-a$, $1/a$ 的唯一性 — 考试常考「用公理证」.

**证明思路** (加法单位元唯一): 若 $0'$ 也满足 $\forall x,\ x+0'=x$, 则 $0=0+0'=0'$, 故唯一. 乘法单位元同理: $1=1\cdot 1'=1'$.

**证明思路** (加法逆唯一): 若 $b,b'$ 都满足 $a+b=a+b'=0$, 则
$$
b=b+0=b+(a+b')=(b+a)+b'=0+b'=b'.
$$
乘法逆唯一同理 (用乘法结合律与单位元).

---

## 2. 有序域 (ordered field)

### 定义 1.6

存在全序 (total order) $\le$ 满足 (O1)–(O5); $a<b$ 当 $a\le b$ 且 $a\ne b$. (定义, 无需证明.)

**典型例子**: $\mathbb{Q}$ 有序; $\mathbb{Q}[\sqrt{-1}]$ **不能**有序 (Exercise 1.10: $a^2>0$ 对 $a\ne 0$ 与 $i^2=-1$ 矛盾).

**证明思路** (复数域不可序): 在有序域中可证 $a\ne 0\Rightarrow a^2>0$ (见练习 1.7). 若 $\mathbb{C}$ (或 $\mathbb{Q}(i)$) 有序, 则 $i\ne 0\Rightarrow i^2>0$, 即 $-1>0$. 但 $1^2>0$ 又给出 $1>0$, 两边加 $-1$ 得 $0>-1$, 与 $-1>0$ 矛盾. 故不能成为有序域.

### 练习 1.7 要点

- $a\ne 0 \Rightarrow 0<a$ 或 $0<-a$
- $a^2>0$, $0<1$, $0<a \Rightarrow 0<a^{-1}$
- $1+1\ne 0$

**证明思路** (三分性): 全序下对 $0,a$ 必有 $0\le a$ 或 $a\le 0$; 若 $a\ne 0$ 则严格不等式, 即 $0<a$ 或 $a<0$ (后者等价于 $0<-a$).

**证明思路** ($a^2>0$): 若 $a>0$, 由序与乘法正性得 $a\cdot a>0$. 若 $a<0$, 则 $-a>0$, 故 $(-a)^2>0$, 而 $(-a)^2=a^2$.

**证明思路** ($0<1$): $1\ne 0$, 故 $1^2>0$, 即 $1>0$.

**证明思路** ($0<a\Rightarrow 0<a^{-1}$): 若 $a^{-1}\le 0$, 则与 $a>0$ 相乘得 $1=a\cdot a^{-1}\le 0$, 与 $1>0$ 矛盾.

**证明思路** ($1+1\ne 0$): 若 $1+1=0$, 则 $1=-1$. 但 $1>0$ 与 $-1<0$ 矛盾 (或: $1+1=1^2+1^2>0$).

**补充** (Exercise 1.7(g)): $0<a,b$ 时 $a<b\iff a^2<b^2$.

**证明**: $(\Rightarrow)$ $a<b$ 且 $a,b>0$ $\Rightarrow$ $0<b-a$, 且 $a+b>0$, 故
$$
b^2-a^2=(b-a)(b+a)>0.
$$
$(\Leftarrow)$ 若 $a\ge b>0$, 则由上得 $a^2\ge b^2$, 与 $a^2<b^2$ 矛盾.

---

## 3. 上下界, 最大/最小值

| 概念 | 定义 |
|---|---|
| 上界 (upper bound) $M$ | $\forall x\in S,\ x\le M$ |
| 下界 (lower bound) $m$ | $\forall x\in S,\ m\le x$ |
| 最大值 (maximum) | $s_0\in S$ 且 $\forall x\in S,\ x\le s_0$ |
| 最小值 (minimum) | 对偶 |

(以上为定义, 无需证明.)

**关键**: 有上界 $\not\Rightarrow$ 有最大值. 例: $\{x\in\mathbb{Q}: 0\le x<8\}$ 无 max.

**证明思路**: 该集有上界 (如 $8$). 若存在最大值 $m$, 则 $m\in S$ 故 $m<8$, 取有理数 $r$ 使 $m<r<8$ (稠密性或直接取 $r=(m+8)/2$), 则 $r\in S$ 且 $r>m$, 矛盾.

---

## 4. 上确界 (supremum) 与下确界 (infimum)

### 定义 3.1

- $\sup S$: 上界集合中的**最小上界 (least upper bound)**
- $\inf S$: 下界集合中的**最大下界 (greatest lower bound)**

(定义, 无需证明.)

**与 max/min 区别**: 上确界/下确界 **可以不在** $S$ 内.

### 定理 3.3 (上确界判别法)

上界 $u$ 是 $\sup S$ 当且仅当: $\forall \epsilon>0,\ \exists x\in S$ 使 $u-x<\epsilon$ (即 $x>u-\epsilon$).

**直觉**: 上确界被 $S$ 中的点「从下方逼近」.

**证明** ($\Rightarrow$): 设 $u=\sup S$. 对 $\epsilon>0$, $u-\epsilon$ 不是上界 (否则比 $u$ 更小), 故存在 $x\in S$ 使 $x>u-\epsilon$, 即 $u-x<\epsilon$.

**证明** ($\Leftarrow$): 设 $u$ 为上界且满足逼近条件. 若存在更小上界 $v<u$, 取 $\epsilon=u-v>0$, 则存在 $x\in S$ 使 $x>u-\epsilon=v$, 与 $v$ 为上界矛盾. 故 $u$ 是最小上界.

### 完备性公理 (completeness axiom) (Definition 3.8–3.9)

- **完备有序域 (complete ordered field)**: 每个非空有上界子集都有上确界
- **$\mathbb{R}$** 定义为完备有序域 (存在且唯一, 含 $\mathbb{N},\mathbb{Z},\mathbb{Q}$)
- **$\mathbb{Q}$ 不完备**: 例 $S=\{x\in\mathbb{Q}: x^2<2\}$ 在 $\mathbb{Q}$ 中无上确界

(前两条为公理/定义约定, 无需证明.)

**证明思路** ($\mathbb{Q}$ 不完备): 假设 $u=\sup_{\mathbb{Q}} S\in\mathbb{Q}$. 不能有 $u^2=2$ (定理 4.8). 若 $u^2<2$, 可构造有理 $h>0$ 使 $(u+h)^2<2$ (取充分小正有理 $h$), 则 $u+h\in S$ 且 $>u$, 矛盾. 若 $u^2>2$, 可构造有理 $h>0$ 使 $(u-h)^2>2$ 且 $u-h$ 仍为上界, 与最小上界矛盾. 故 $S$ 在 $\mathbb{Q}$ 中无上确界.

(更具体的 $h$ 选取见定理 4.9 的同类构造.)

---

## 5. $\mathbb{Q}$ 的稠密性 (density)

### 定理 4.1, 4.2

- $\mathbb{N}$ 良序 (well-ordered); $\mathbb{N}$ 在 $\mathbb{R}$ 中无上界
- **推论 4.6 (Corollary 4.6)**: 任意 $a<b$ 存在有理数 $r$ 使 $a<r<b$

**证明思路** ($\mathbb{N}$ 无上界 / Archimedes): 若 $\mathbb{N}$ 有上界, 由完备性令 $u=\sup\mathbb{N}$. 则存在 $n\in\mathbb{N}$ 使 $n>u-1$, 从而 $n+1>u$, 与 $u$ 为上界矛盾. 故对任意 $x\in\mathbb{R}$ 存在 $n\in\mathbb{N}$ 使 $n>x$ (Archimedes 性质 (Archimedean property)).

**证明思路** (良序): $\mathbb{N}$ 的每个非空子集有最小元 — 作为 $\mathbb{N}$ 的归纳/良序公理 (或由 Peano 公理推出); 本课程通常作为已知性质使用.

**证明** (推论 4.6, 稠密性): 由 Archimedes, 存在 $n\in\mathbb{N}$ 使 $n(b-a)>1$, 即 $1/n<b-a$. 再取整数 $m$ 使 $m>na$ 且 $m$ 尽量小 (或: 存在 $m\in\mathbb{Z}$ 使 $m-1\le na<m$). 则
$$
a<\frac{m}{n}\le a+\frac{1}{n}<b,
$$
故 $r=m/n$ 满足 $a<r<b$. (细节: 由 Archimedes 取 $m$ 使 $m>na$; 再取最小这样的正整数/用良序保证存在临界 $m$, 得 $m-1\le na$, 从而 $m/n\le a+1/n<b$.)

### 无理数

- **定理 4.8**: 无有理数 $x$ 使 $x^2=2$
- **定理 4.9**: 存在 $x\in\mathbb{R}$, $x^2=2$, 且 $x=\sup\{y\in\mathbb{R}: y^2<2\}$ (无理)

**证明** (定理 4.8): 反证. 设 $x=p/q$, $p,q\in\mathbb{Z}$, $q>0$, $\gcd(p,q)=1$, 且 $p^2=2q^2$. 则 $p^2$ 偶 $\Rightarrow$ $p$ 偶, 写 $p=2k$, 得 $4k^2=2q^2\Rightarrow q^2=2k^2$, 故 $q$ 偶. 与 $\gcd(p,q)=1$ 矛盾.

**证明思路** (定理 4.9): 令 $S=\{y\in\mathbb{R}: y\ge 0,\ y^2<2\}$. $S$ 非空有上界 (如 $2$), 由完备性令 $x=\sup S$. 断言 $x^2=2$.

- 若 $x^2<2$, 取 $h=\min\bigl\{1,\ (2-x^2)/(2x+1)\bigr\}>0$, 则
  $$
  (x+h)^2=x^2+2xh+h^2\le x^2+2xh+h\le x^2+(2x+1)h\le 2,
  $$
  且可调整使严格 $<2$, 得 $x+h\in S$, 矛盾.
- 若 $x^2>2$, 取 $h=\min\bigl\{x,\ (x^2-2)/(2x)\bigr\}>0$, 则对所有 $y\ge x-h$ 有 $y^2>2$, 故 $x-h$ 为上界且 $<x$, 矛盾.

因此 $x^2=2$. 由定理 4.8, $x\notin\mathbb{Q}$.

---

## 6. 可数 (countable) 与不可数 (uncountable)

### 定义 5.6

- **可数**: 有限或与 $\mathbb{N}$ 双射 (bijection)
- **不可数**: 否则

(定义, 无需证明.)

### 主要结果

| 定理 | 内容 |
|---|---|
| 5.8 | $\mathbb{R}$ 不可数 (康托对角线论证 (Cantor diagonal argument) 于 $[0,1]$) |
| 5.9–5.11 | $\mathbb{Z}$, $\mathbb{N}\times\mathbb{N}$, $\mathbb{Q}$ 可数 |
| 5.12 | 无理数不可数 |

**证明思路** (5.9, $\mathbb{Z}$ 可数): 枚举 $0,1,-1,2,-2,\ldots$, 即双射 $f:\mathbb{N}\to\mathbb{Z}$,
$$
f(n)=\begin{cases} n/2 & n\text{ 偶},\\ -(n+1)/2 & n\text{ 奇}.\end{cases}
$$

**证明思路** (5.10, $\mathbb{N}\times\mathbb{N}$ 可数): 按对角线枚举 $(1,1),\ (1,2),(2,1),\ (1,3),(2,2),(3,1),\ldots$, 或显式双射 $(m,n)\mapsto 2^{m-1}(2n-1)$ (奇数部分唯一分解).

**证明思路** (5.11, $\mathbb{Q}$ 可数): 正有理数可写成既约 $p/q$, 注入 $\mathbb{N}\times\mathbb{N}$, 故可数; $\mathbb{Q}=\mathbb{Q}^+\cup\{0\}\cup\mathbb{Q}^-$ 为可数个可数集之并, 仍可数.

**证明** (5.8, $\mathbb{R}$ 不可数): 证 $[0,1]$ 不可数即可. 反证: 设 $[0,1]=\{x_1,x_2,\ldots\}$, 写十进 (或二进) 展开 $x_n=0.a_{n1}a_{n2}a_{n3}\ldots$. 定义 $b_k=4$ 若 $a_{kk}\ne 4$, 否则 $b_k=5$. 则 $y=0.b_1b_2\ldots\in[0,1]$, 但对每个 $n$ 有 $b_n\ne a_{nn}$, 故 $y\ne x_n$, 矛盾. (避免 $0.1999\ldots=0.2000\ldots$ 歧义时可用二进并排除尾部全 $1$ 的表示.)

**证明思路** (5.12, 无理数不可数): $\mathbb{R}=\mathbb{Q}\cup(\mathbb{R}\setminus\mathbb{Q})$. 若无理数可数, 则 $\mathbb{R}$ 为两个可数集之并, 可数, 与 5.8 矛盾.

### 定理 5.5 (嵌套区间性质 (Nested Interval Property))

闭区间 $[a_n,b_n]$ 嵌套 (即 $[a_{n+1},b_{n+1}]\subset[a_n,b_n]$) $\Rightarrow$ $\bigcap_n I_n\ne\emptyset$ (用 $\sup\{a_n\}$).

**证明**: 由嵌套, $\{a_n\}$ 有上界 (任一 $b_1$ 即可), 令 $c=\sup\{a_n\}$. 对每个 $n$, 有 $a_n\le c$ (上确界定义). 又对任意 $m$, $a_m\le b_n$ (因 $a_m\le a_{\max(m,n)}\le b_{\max(m,n)}\le b_n$), 故 $c\le b_n$. 因此 $c\in[a_n,b_n]$ 对一切 $n$, 即 $c\in\bigcap I_n$.

---

## 区间记号 (§5.2)

$(a,b), [a,b], (-\infty,a], [a,\infty)$ 等 — 后文序列/连续会反复使用. (记号约定, 无需证明.)

---

## 易错点

1. **最大值与上确界**: $\sup S\in S$ 时才等于最大值
2. **$\mathbb{Q}$ 中上确界可能不存在**: 完备性是 $\mathbb{R}$ 特有
3. **Exercise 1.7 (g)**: $0<a,b$ 时 $a<b \iff a^2<b^2$ (需正数条件; 证明见 §2)
4. **可数性证明**: $\mathbb{Q}$ 用既约分数注入 $\mathbb{N}\times\mathbb{N}$ (或经 $\mathbb{Z}\times\mathbb{N}$)

---

## 与后续章节

- Ch.2 序列极限将用到上确界/下确界与嵌套区间
- 完备性保证柯西列 (Cauchy sequence) 收敛 (后续)

## 参考书

Bartle & Sherbert; Ross — 见 syllabus
