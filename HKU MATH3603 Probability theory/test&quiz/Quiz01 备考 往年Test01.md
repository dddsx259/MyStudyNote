# Quiz1 备考 — 往年 Test1 精读与对标

- **本学期考试**: Quiz 1, 2026-10-07 Tue 12:00–12:50 @ CYPP4
- **本学期 scope**: **Ch1 + §2.1–2.5** (至 Random Vectors & Joint Dist.); 闭卷, **无 cheat sheet**; 部分分布定义卷面可给
- **往年材料**: [`docs/archives/previous/test&quiz/Test01.pdf`](../docs/archives/previous/test&quiz/Test01.pdf) (往年 Test 1, 50 min)
- **用途**: 用往年题练手感 / 题型; **非**本学期原卷. 超出 §2.5 的技巧仍可练 (期望/方差/指示变量), 但独立性定义以本学期 Ch1 为准

> 往年完整归档见 [`docs/archives/previous/readme.md`](../docs/archives/previous/readme.md).

---

## 1. 往年 Test1 题型 vs Quiz1 scope

| 往年题 | 主题 | 对齐本学期 | Quiz1 是否应熟练 |
|---|---|---|---|
| Q1 | 事件独立 → 补事件 / 相互独立 | Ch1 独立 | **必练** |
| Q2 | 均匀断棍 → 变换分布 / P / Var | §2.1–2.4 (RV, CDF/密度, LOTUS, 矩) | **必练** |
| Q3 | 指示变量 + 线性性; 骰子得分 | §2.1–2.3 (期望方差); 组合计数 | **必练** (经典套路) |

**本学期还要单独补** (往年卷未直接考, 但 scope 到 2.5):

- 常见离散/连续分布的 PMF/PDF/期望方差 (卷面可能给定义)
- 联合分布 / 边缘 / 随机向量 (§2.5)
- 条件概率, 全概率, Bayes (Ch1)

---

## 2. 往年 Test1 — 题意与完整解答

逐步计算见 [`Quiz01 往年Test01 解答.md`](Quiz01%20往年Test01%20解答.md). 下面保留同一份答案的提纲.

### Q1. 独立事件的补 / 相互独立

**题**: $A,B,C$ 相互独立. 证:

(a) $A^c$ 与 $B$ 独立  
(b) $A^c$ 与 $B^c$ 独立  
(c) $A^c,B^c,C$ 相互独立  
(d) $A^c,B^c,C^c$ 相互独立  

**思路**: 两事件独立 $\Leftrightarrow P(E\cap F)=P(E)P(F)$. 相互独立 = 对任意子族交集概率等于概率乘积.

**(a)**  
$$
P(A^c\cap B)=P(B)-P(A\cap B)=P(B)-P(A)P(B)=P(A^c)P(B).
$$

**(b)**  
$$
\begin{aligned}
P(A^c\cap B^c)&=1-P(A\cup B)=1-\bigl(P(A)+P(B)-P(A\cap B)\bigr)\\
&=1-P(A)-P(B)+P(A)P(B)=(1-P(A))(1-P(B))=P(A^c)P(B^c).
\end{aligned}
$$

**(c)** 需验证所有 $|J|\ge 2$ 的子族. 已有 (b): $A^c\perp B^c$.  

$A^c$ 与 $C$: 同 (a), $P(A^c\cap C)=P(A^c)P(C)$.  
$B^c$ 与 $C$: 同理.  

三元交:
$$
\begin{aligned}
P(A^c\cap B^c\cap C)&=P(C)-P\bigl((A\cup B)\cap C\bigr)\\
&=P(C)-\bigl(P(A\cap C)+P(B\cap C)-P(A\cap B\cap C)\bigr)\\
&=P(C)-P(A)P(C)-P(B)P(C)+P(A)P(B)P(C)\\
&=P(A^c)P(B^c)P(C).
\end{aligned}
$$

**(d)** 在 (c) 基础上对 $C$ 取补, 或对称重复 (b)(c) 的计算:
$$
P(A^c\cap B^c\cap C^c)=1-P(A\cup B\cup C),
$$
展开容斥并用相互独立把交集拆成乘积, 得 $P(A^c)P(B^c)P(C^c)$. 亦可用: 由 (c), $A^c,B^c,C$ 相互独立 $\Rightarrow$ 对 $C$ 用 (a)(b) 型论证得与 $C^c$ 的相互独立.

**易错**: 相互独立 $\neq$ 两两独立; 证相互独立必须查**所有**二元与三元 (以及更高) 交.

---

### Q2. 断棍: $X=$ 长度差绝对值, $Y=$ 长度乘积

**设定**: 棍长 1, 断点 $U\sim\mathrm{Unif}[0,1]$. 两段长 $U$, $1-U$.  
$X=|2U-1|$, $Y=U(1-U)$.

#### (i) $X$ 的分布

对 $x\in[0,1]$,
$$
P(X\le x)=P(|2U-1|\le x)=P\Bigl(\frac{1-x}{2}\le U\le\frac{1+x}{2}\Bigr)=x.
$$
故 $X\sim\mathrm{Unif}[0,1]$ (CDF $F_X(x)=x$ on $[0,1]$).

#### (ii) $P(Y<1/8)$

$Y=U-U^2$. $Y<1/8$ $\Leftrightarrow$ $8U^2-8U+1>0$.  

根: $\dfrac{2\pm\sqrt{2}}{4}$. 开口向上 $\Rightarrow$ 在区间外成立:
$$
P(Y<1/8)=\frac{2-\sqrt{2}}{4}+1-\frac{2+\sqrt{2}}{4}=1-\frac{\sqrt{2}}{2}.
$$

#### (iii) $\mathrm{Var}(X)$, $\mathrm{Var}(Y)$

$X\sim\mathrm{Unif}[0,1]$: $EX=\tfrac12$, $EX^2=\tfrac13$, $\mathrm{Var}(X)=\tfrac{1}{12}$.

$Y=U-U^2$:  
$EY=\tfrac12-\tfrac13=\tfrac16$,  
$EY^2=E[U^2(1-U)^2]=E[U^2-2U^3+U^4]=\tfrac13-\tfrac12+\tfrac15=\tfrac{1}{30}$,  
$\mathrm{Var}(Y)=\tfrac{1}{30}-\bigl(\tfrac16\bigr)^2=\tfrac{1}{180}$.

**易错**: 求 $X$ 分布时别忘绝对值如何拆区间; $Y$ 用 LOTUS / 直接对 $U$ 的矩, 不必先求 $Y$ 的密度.

---

### Q3. $n$ 人掷公平骰子

#### (i) Same-value scoring (相同点数的无序对各得 1 分)

令 $I_{ij}=\mathbf{1}_{\{X_i=X_j\}}$ ($1\le i<j\le n$), 总分 $S=\sum_{i<j}I_{ij}$.  
$P(I_{ij}=1)=\dfrac16$.

$$
ES=\binom{n}{2}\cdot\frac16=\frac{n(n-1)}{12}.
$$

方差: $\mathrm{Var}(I_{ij})=\dfrac16\cdot\dfrac56=\dfrac{5}{36}$.  

对任意两对不同指示变量, 可验证 $\mathrm{Cov}=0$ (共享一顶点: $P(I_{ij}=I_{ik}=1)=\dfrac1{36}=(1/6)^2$; 不交两对亦积化为 $(1/6)^2$). 故不相关加总:
$$
\mathrm{Var}(S)=\binom{n}{2}\cdot\frac{5}{36}=\frac{5n(n-1)}{72}.
$$

#### (ii) Multiplicity scoring ($\sum_k m_k\cdot k$)

观察: $\sum_{k=1}^6 m_k\cdot k=\sum_{i=1}^n X_i$ (每人点数之和).  
令 $T=\sum_{i=1}^n X_i$, $X_i$ i.i.d. 均匀于 $\{1,\ldots,6\}$.

$EX_i=\dfrac{7}{2}$, $E[X_i^2]=\dfrac{91}{6}$, $\mathrm{Var}(X_i)=\dfrac{91}{6}-\dfrac{49}{4}=\dfrac{35}{12}$.

$$
ET=\frac{7n}{2},\qquad \mathrm{Var}(T)=\frac{35n}{12}.
$$

**易错**: (i) 用指示变量按「对」计数, 别按「组大小选组合」直接开平方导致协方差算错; (ii) 先化简成 $\sum X_i$ 再算, 别对每个 $k$ 硬算 $m_k$ 的联合.

---

## 3. 建议刷题顺序 (Quiz1 前)

1. **今天**: 闭卷限时 50 min 手写往年 Test1 (三题), 再对上面解答  
2. **Ch1**: 本学期 `题集/题集01 ch01 foundations.md` + HW1 错题 + 往年 `docs/archives/previous/tut/Tut01 solution.pdf`–`Tut02`  
3. **§2.1–2.5**: `题集/题集02 ch02 random variables distributions.md` (停在 2.5) + HW2 (若已覆盖) + 往年 Tut03–04  
4. **手写小抄自用** (考场不可带): 独立定义检查清单; Unif/Exp/Bin/Poisson 矩; LOTUS; $\mathrm{Var}(aX+b)=a^2\mathrm{Var}(X)$; 指示变量 $E=\mathrm{Var}$ 公式  

---

## 4. 归档路径速查

| 文件 | 路径 |
|---|---|
| 往年 Test1 | `docs/archives/previous/test&quiz/Test01.pdf` |
| 往年 Test2 (照片) | `docs/archives/previous/test&quiz/Test02.heic` |
| 往年 HW sol | `docs/archives/previous/assignment/Homework0k solution.pdf` |
| 往年 Tut sol | `docs/archives/previous/tut/Tut0k solution.pdf` |
