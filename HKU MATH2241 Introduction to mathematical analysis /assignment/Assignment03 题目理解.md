# Assignment 3 题目理解: [0,1] 有限开覆盖与有理 Cauchy 列

- **来源**: `assignment/Assignment03.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis, Fall 2026
- **Due**: 2026-10-05 (Mon) 22:00; Moodle 提交
- **参考**: Nested Interval Property (Thm 5.5 / Ch1); Cauchy 完备性 (Ch2 Part2); 有理数不完备
- **格式**: 封面写姓名 / UID / Faculty; **内页 (Page 3 起) 勿写身份信息** (匿名评分); AI-use disclosure 按课程要求

---

## 总目标

1. 证明: 若 $[0,1]$ 被一列开区间 $(x_n-\varepsilon_n,x_n+\varepsilon_n)$ 覆盖 ($x_n\in[0,1]$, $\varepsilon_n>0$), 则存在**有限**子覆盖. 用反证 + 嵌套闭区间 + 极限点落入某一区间.
2. 判断: 每个有理 Cauchy 列是否必收敛到有理数 (证或反例).

---

## 第 1 题 — $[0,1]$ 的有限开覆盖 (Heine–Borel 型特例)

**设定**: $(x_n)$ 为 $[0,1]$ 中序列; 对每个 $n\in\mathbb{N}$, $\varepsilon_n>0$. 假设
$$
[0,1]\subset\bigcup_{n\in\mathbb{N}}(x_n-\varepsilon_n,x_n+\varepsilon_n).
$$
**目标**: 存在有限指标 $n_1,\ldots,n_k$ 使
$$
[0,1]\subset\bigcup_{i=1}^k (x_{n_i}-\varepsilon_{n_i},x_{n_i}+\varepsilon_{n_i}).
$$

### (a) 反证假设

**要求**: 假设**不存在**有限子覆盖, 即任意有限个开区间都不能覆盖 $[0,1]$.

### (a)(i) 嵌套闭区间构造

**要求**: 构造嵌套闭有界区间
$$
I_1\supset I_2\supset I_3\supset\cdots,
$$
使得每个 $I_j$ **都不能**被有限多个 $(x_n-\varepsilon_n,x_n+\varepsilon_n)$ 覆盖, 且
$$
|I_j|=\frac{1}{2^{j-1}}\qquad(\forall j\in\mathbb{N}).
$$

**理解要点**:

- 标准二分法: $I_1=[0,1]$ (长度 1). 若 $I_j=[a_j,b_j]$ 无有限子覆盖, 取中点 $m=(a_j+b_j)/2$, 则 $[a_j,m]$ 与 $[m,b_j]$ 中**至少有一个**无有限子覆盖 (否则两者各取有限覆盖再并起来得 $I_j$ 的有限覆盖, 矛盾). 选该半区间为 $I_{j+1}$, 长度减半.
- 这正是 Nested Interval Property 证明中的构造, 加上「无有限子覆盖」的遗传性.

### (a)(ii) 选取 $(y_j)$ 并证收敛

**要求**: 对每个 $j$, 取 $y_j\in I_j$; 证明 $(y_j)$ 收敛.

**理解要点**:

- 嵌套 + $|I_j|\to 0$ $\Rightarrow$ 交为单点 $c$; 或证 $(y_j)$ 为 Cauchy: $j,k\ge N$ 时 $y_j,y_k\in I_N$, 故 $|y_j-y_k|\le|I_N|\to 0$.
- 由 $\mathbb{R}$ 完备性 (Cauchy $\Rightarrow$ 收敛) 得 $y_j\to c$; 且 $c\in\bigcap I_j\subseteq[0,1]$.

### (a)(iii) 某一 $I_N$ 落入单个开区间

**要求**: 证明存在 $m,N\in\mathbb{N}$ 使
$$
I_N\subset(x_m-\varepsilon_m,x_m+\varepsilon_m).
$$

**理解要点**:

- $c\in[0,1]$ 被某个 $(x_m-\varepsilon_m,x_m+\varepsilon_m)$ 覆盖, 故存在 $\delta>0$ 使 $(c-\delta,c+\delta)$ 落在该开区间内.
- 取 $N$ 使 $|I_N|<\delta$ 且 $y_N$ (或任意 $I_N$ 中点) 靠近 $c$, 则整段 $I_N\subset(c-\delta,c+\delta)$.

### (b) 导出矛盾

**要求**: 用 (a) 得矛盾, 从而原命题成立 (存在有限子覆盖).

**理解要点**:

- $I_N$ 被**单个**开区间覆盖, 更被有限个覆盖, 与 $I_N$ 「无有限子覆盖」矛盾.
- 故反证假设假, $[0,1]$ 有有限子覆盖.

---

## 第 2 题 — 有理 Cauchy 列

**要求**: 证明或反驳: 每个有理数 Cauchy 序列都收敛到一个有理数.

**理解要点**:

- 在 $\mathbb{R}$ 中 Cauchy $\Leftrightarrow$ 收敛, 但极限可在 $\mathbb{R}\setminus\mathbb{Q}$.
- **反例方向**: 构造 $(q_n)\subset\mathbb{Q}$ 为 Cauchy, 且 $q_n\to\sqrt{2}$ (或任何无理数). 例如 $q_n$ 取 $\sqrt{2}$ 的十进截断, 或 $q_{n+1}=(q_n+2/q_n)/2$ 从有理初值迭代.
- 结论: 命题**假**; $\mathbb{Q}$ 对 Cauchy 列不完备.

---

## 提交提醒

- Q1 四小步 + Q2 均必交; 证明须完整.
- 内页勿写姓名/UID; 封面单独填身份.
- AI disclosure: 工具与用途, 并声明可自行讲解论证.
