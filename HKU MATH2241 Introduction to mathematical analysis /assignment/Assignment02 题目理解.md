# Assignment 2 题目理解: 连分数收敛子列与聚点

- **来源**: `assignment/Assignment02.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis, Fall 2026
- **Due**: 2026-09-28 (Mon) 22:00; Moodle 提交
- **参考**: [BS] Bartle & Sherbert, *Introduction to Real Analysis*, 4th ed. (题 (1)(b) 提示 BS 3.4 Ex 6; Sep 17 讲义连分数 / 黄金比)
- **格式**: 写姓名 / UID / Faculty; 文末 **AI-use disclosure**

---

## 总目标

1. 对正整数列 $(a_n)$ 定义的 **有限连分数 / 渐近分数 (convergents)** $(x_n)$, 证明 **偶数项子列** 与 **奇数项子列** 各自收敛; 特例 $a_n\equiv 1$ 时判断全序列是否收敛并求极限.
2. 建立 **聚点 (cluster point / limit point)** 的等价刻画, 并证明有界非空集 $A$ 的全体聚点集 $M$ 存在 **最大值**.

---

## 第 1 题 — 连分数型序列

**定义** (题面): $(a_n)$ 为正整数列,
$$
x_1=a_1,\quad
x_2=a_1+\frac{1}{a_2},\quad
x_3=a_1+\frac{1}{a_2+\dfrac{1}{a_3}},\quad \ldots
$$
即 $x_n=[a_1;a_2,\ldots,a_n]$ (第 $n$ 个渐近分数).

### (a)

**要求**: 证明子列 $(x_{2n})$ 与 $(x_{2n-1})$ 均收敛.

**理解要点**:

- 标准结论: 奇数项渐近分数 **严格递增且有上界**; 偶数项 **严格递减且有下界** (正整数部分商保证分母 $q_n>0$).
- 核心工具: 渐近分数递推 $p_n,q_n$ 及恒等式
  $$
  p_n q_{n-1}-p_{n-1}q_n=(-1)^{n-1},
  $$
  从而 $x_n-x_{n-1}$ 符号随 $n$ 奇偶交替, 且 $x_{2n-1}<x_{2n}$.
- 有界性: 一切 $x_n\in[a_1,\,a_1+1/a_2]$ 量级内 (更粗: $a_1\le x_n\le a_1+1$ 当 $a_2\ge 1$).
- 结论用 **单调有界定理 (MCT)**.

### (b)

**要求**: 设 $a_n=1\ (\forall n)$, 判断 $(x_n)$ 是否收敛; 若收敛求 $\lim_{n\to\infty}x_n$.

**理解要点**:

- 此时 $x_n=F_{n+1}/F_n$ ($F_n$ 为 Fibonacci, 通常 $F_1=F_2=1$).
- 奇子列递增、偶子列递减, 且 **两者极限同为** $\varphi=(1+\sqrt5)/2$ (黄金比).
- 全序列 **收敛** 当且仅当两子列极限相等; 此处相等, 故 $\lim x_n=\varphi$.
- 可引用 BS 3.4 Ex 6 或 Sep 17 讲义.

---

## 第 2 题 — 聚点

**定义** (题面): $x\in\mathbb{R}$ 是 $A\subset\mathbb{R}$ 的 **聚点**, 若 $\exists$ 取值于 $A$ 的序列 $(s_n)$ 使 $s_n\to x$. ( $x$ 不必属于 $A$.)

### (a)

**要求**: 证明
$$
x\text{ 是 }A\text{ 的聚点}
\quad\Longleftrightarrow\quad
\exists\ (x_n)\subset A,\ |x_n-x|<\frac{1}{n}\ (\forall n).
$$

**理解要点**:

- ($\Rightarrow$): 由 $s_k\to x$ **对角线 / 子列** 构造, 对每个 $n$ 取足够大的 $k_n$ 使 $|s_{k_n}-x|<1/n$.
- ($\Leftarrow$): $|x_n-x|<1/n\Rightarrow x_n\to x$, 直接得聚点.

### (b)

**要求**: $A\subset\mathbb{R}$ 非空有界; $M=$ $A$ 的全体聚点. 证明 $\max M$ 存在.

**理解要点**:

- 聚点集 $M=\overline{A}\setminus\{\text{孤立点}\}$ 的闭包意义下 $M\subseteq\overline{A}$; 有界 $\Rightarrow$ $M$ 有界.
- $M$ **闭**: 聚点列的极限仍为聚点 (用 (a) 的 $1/n$ 刻画或标准对角线).
- $M\neq\emptyset$: 有界非空 $A$ 用 **Bolzano-Weierstrass** 得 $A$ 中收敛子列, 其极限为聚点.
- 闭有界 $\subset\mathbb{R}$ $\Rightarrow$ 紧 $\Rightarrow$ $\sup M\in M$ $\Rightarrow$ $\max M$ 存在.

---

## 提交提醒

- 两题均必交; 证明须完整严谨 (本题无 optional).
- AI disclosure: 用了什么工具, 帮了哪些部分, 并声明最终论证可自行讲解.
