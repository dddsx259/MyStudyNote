# Chapter 1: 概率基础 (Foundations of Probability)

- **来源**: `Lec/01-probability-theory-lecture-notes.pdf` Chapter 1 (p.6–25)
- **课程**: MATH3603, Zhigang Bao
- **前置**: 集合运算
- **本章目标**: 概率公理 (probability axioms), 条件概率 (conditional probability) / 贝叶斯定理 (Bayes' theorem), 独立性 (independence) (含 两两独立 (pairwise independence) vs 相互独立 (mutual independence))

---

## 1.1 样本空间 (sample space) 与事件 (event)

### 实验、结果、样本空间

- **实验/试验 (experiment/trial)**: 结果事先未知
- **结果 (outcome)**: 单个可能结果
- **样本空间** $S$ (或 $\Omega$): 所有结果的集合

| 实验 | $S$ |
|---|---|
| 掷硬币 | $\{H,T\}$ |
| 两枚硬币 (有序) | $\{HH,HT,TH,TT\}$ |
| 灯泡寿命 | $[0,\infty)$ |

### 事件

- **定义**: $S$ 的子集. **定义, 无需证明**.
- **基本/简单事件 (elementary/simple event)**: 单点集; **复合事件 (compound event)**: 多点集. **定义, 无需证明**.
- $E$ 发生 $\Leftrightarrow \omega\in E$

### 集合运算

| 符号 | 含义 |
|---|---|
| $E\cup F$ | 至少一个发生 |
| $E\cap F$ | 同时发生 |
| $E^c$ | $E$ 不发生 |
| $E\cap F=\emptyset$ | 互斥 (mutually exclusive) |

集合运算为集合论记号约定. **定义, 无需证明**.

---

## 1.2 概率公理

### 定义 1.1.8–1.1.9

概率 $P:\mathcal{F}\to[0,1]$ 满足:

1. $0\le P(A)\le 1$
2. $P(S)=1$
3. **可数可加性 (countable additivity)**: 互斥 $A_i$ 则 $P(\bigcup A_i)=\sum P(A_i)$

**概率空间 (probability space)**: $(S,\mathcal{F},P)$. **定义, 无需证明**.

**注意**: 写 $P(\{2\})$ 而非 $P(2)$ (掷骰).

### 命题 1.1.10

- $P(\emptyset)=0$
- $P(A^c)=1-P(A)$
- $A\subseteq B \Rightarrow P(A)\le P(B)$

**证明**:

1. $P(\emptyset)=0$: 取 $A_1=\emptyset$, $A_2=\emptyset,\ldots$ (两两互斥), 则 $\bigcup_{i=1}^\infty A_i=\emptyset$. 由可数可加性
   $$P(\emptyset)=\sum_{i=1}^\infty P(\emptyset).$$
   若 $P(\emptyset)=c>0$, 则右端为 $\infty$, 与 $P(\emptyset)\le 1$ 矛盾; 故 $c=0$. (有限可加性也够: $S=S\cup\emptyset\cup\emptyset\cup\cdots$ 得同样结论.)

2. $P(A^c)=1-P(A)$: $A$ 与 $A^c$ 互斥且 $A\cup A^c=S$, 故
   $$P(A)+P(A^c)=P(S)=1.$$

3. 单调性: 若 $A\subseteq B$, 则 $B=A\cup(B\setminus A)$ 且二者互斥, 故
   $$P(B)=P(A)+P(B\setminus A)\ge P(A),$$
   因为 $P(B\setminus A)\ge 0$.

### 有限可加性 (finite additivity)

互斥 $A_1,\ldots,A_n$:
$$P\Bigl(\bigcup_{i=1}^n A_i\Bigr)=\sum_{i=1}^n P(A_i).$$

**证明**: 令 $A_{n+1}=A_{n+2}=\cdots=\emptyset$. 由可数可加性与 $P(\emptyset)=0$ 即得.

### 容斥原理 (inclusion–exclusion)

两事件:
$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$

**证明**: 写
$$A\cup B=A\cup(B\setminus A),\qquad B=(A\cap B)\cup(B\setminus A),$$
且右端两对都互斥. 故
$$P(A\cup B)=P(A)+P(B\setminus A),\qquad P(B)=P(A\cap B)+P(B\setminus A).$$
消去 $P(B\setminus A)$ 得结论.

一般 $n$ 事件 (Theorem 1.1.12):
$$
\begin{aligned}
P\Bigl(\bigcup_{i=1}^n A_i\Bigr)
&=\sum_i P(A_i)-\sum_{i<j}P(A_i\cap A_j)+\sum_{i<j<k}P(A_i\cap A_j\cap A_k)\\
&\quad-\cdots+(-1)^{n+1}P(A_1\cap\cdots\cap A_n).
\end{aligned}
$$

**证明思路**: 对 $n$ 归纳. $n=2$ 已证. 假设对 $n-1$ 成立. 令 $B=\bigcup_{i=1}^{n-1}A_i$, 则
$$P(B\cup A_n)=P(B)+P(A_n)-P(B\cap A_n),$$
其中 $B\cap A_n=\bigcup_{i=1}^{n-1}(A_i\cap A_n)$. 对 $P(B)$ 与 $P(B\cap A_n)$ 分别用归纳假设, 整理交集项的符号即得交替和.

**另一思路 (指示函数)**: 对任意 $\omega$,
$$1_{\bigcup A_i}(\omega)=1-\prod_{i=1}^n\bigl(1-1_{A_i}(\omega)\bigr).$$
展开乘积后对两边取期望 (期望线性), 即得容斥.

---

## 1.3 条件概率

### 定义 1.2.1

$P(B)>0$ 时:
$$P(A|B)=\frac{P(A\cap B)}{P(B)}.$$

**定义, 无需证明**.

**直觉**: 已知 $B$ 发生, 样本空间缩为 $B$, 在 $B$ 内 $A$ 的份额.

**补充**: 固定 $B$ 后, $Q(\cdot)=P(\cdot|B)$ 仍是概率测度 (非负, $Q(S)=1$, 可数可加). **证明思路**: 由 $P$ 的公理直接验证; 例如互斥 $A_i$ 时 $P\bigl((\bigcup A_i)\cap B\bigr)=\sum P(A_i\cap B)$, 再除以 $P(B)$.

### 乘法法则 (multiplication rule)

$$P(A\cap B)=P(A|B)P(B)=P(B|A)P(A).$$

**证明**: 当 $P(B)>0$ 时, 由定义 $P(A|B)=P(A\cap B)/P(B)$ 两边乘 $P(B)$. 当 $P(A)>0$ 时同理. 若某事件概率为 0, 则对应交集概率亦为 0 (单调性), 等式仍成立 (约定或直接检验).

链式法则 (chain rule) 对三事件 (若中间条件概率有定义):
$$P(A\cap B\cap C)=P(A)P(B|A)P(C|A\cap B).$$

**证明**: 反复用两事件乘法法则:
$$P(A\cap B\cap C)=P\bigl((A\cap B)\cap C\bigr)=P(C|A\cap B)P(A\cap B)=P(C|A\cap B)P(B|A)P(A).$$

### 全概率公式 (law of total probability)

分区 $F_1,\ldots,F_n$ (互斥且并 $=S$, $P(F_j)>0$):
$$P(E)=\sum_{j=1}^n P(F_j)P(E|F_j).$$

**证明**: $E=\bigcup_{j=1}^n (E\cap F_j)$ 且右端两两互斥 (因 $F_j$ 互斥). 有限可加性给出
$$P(E)=\sum_{j=1}^n P(E\cap F_j).$$
再对每项用乘法法则 $P(E\cap F_j)=P(F_j)P(E|F_j)$.

可数分区情形同理, 用可数可加性.

### 贝叶斯定理

$$P(F_i|E)=\frac{P(F_i)P(E|F_i)}{\sum_j P(F_j)P(E|F_j)}.$$

**证明**: 由条件概率定义与乘法法则,
$$P(F_i|E)=\frac{P(F_i\cap E)}{P(E)}=\frac{P(F_i)P(E|F_i)}{P(E)}.$$
分母用全概率公式换成 $\sum_j P(F_j)P(E|F_j)$.

**用途**: 已知先验概率 (prior) $P(F_j)$ 与似然 (likelihood) $P(E|F_j)$, 求后验概率 (posterior) $P(F_i|E)$.

### 例题要点

- **两孩问题 (two-child problem)**: $P(BB\mid \text{至少一男孩})=1/3$ (有序样本空间)

**证明思路**: 有序样本空间 $\{BB,BG,GB,GG\}$ 等可能. 令 $A=\{BB\}$, $B=\{BB,BG,GB\}$. 则
$$P(A|B)=\frac{P(A\cap B)}{P(B)}=\frac{1/4}{3/4}=\frac13.$$

- **两个瓮 (urn)**: 用贝叶斯定理求 $P(H|W)$ (按具体先验与似然代入上述公式即可).

### 信息不一定增大概率

- 知道答案在 $\{b,c,d\}$ 后 $P(\text{正确})=0$
- 也可能不变: 两硬币 $P(E|F)=P(E)$ $\Rightarrow$ 独立 (见下一节等价刻画)

---

## 1.4 独立性

### 两事件独立

$$P(A\cap B)=P(A)P(B)\quad (A\perp\!\!\!\perp B).$$

**定义, 无需证明**.

等价 (当 $P(B)>0$): $P(A|B)=P(A)$.

**证明** (等价性):
$$P(A|B)=P(A)\iff \frac{P(A\cap B)}{P(B)}=P(A)\iff P(A\cap B)=P(A)P(B).$$
当 $P(A)>0$ 时同理有 $P(B|A)=P(B)$.

**易错**:

- 独立 $\ne$ 互斥 (互斥且 $P(A),P(B)>0$ $\Rightarrow$ 不独立)

**证明**: 若互斥且 $P(A),P(B)>0$, 则 $P(A\cap B)=0$, 但 $P(A)P(B)>0$, 故不相等.

- 不能凭直觉, 必须验证公式

### 多事件: 两两独立 vs 相互独立

- **两两独立**: 任意两事件独立. **定义, 无需证明**.
- **相互独立**: 任意 $J\subseteq\{1,\ldots,n\}$, $|J|\ge 2$,
  $$P\left(\bigcap_{j\in J}A_j\right)=\prod_{j\in J}P(A_j).$$
  **定义, 无需证明**.

相互独立 $\Rightarrow$ 两两独立 (取 $|J|=2$). **证明**: 定义的特殊情形.

**例 1.3.4**: 两骰子 $A,B,C$ 两两独立但 **不** 相互独立.

**证明思路**: 典型构造: 掷两枚公平骰, $A=$「第一枚偶数」, $B=$「第二枚偶数」, $C=$「两枚同奇偶」. 验证任意两事件交的概率为 $1/4=P(\cdot)P(\cdot)$, 但 $P(A\cap B\cap C)=P(A\cap B)=1/4\neq 1/8=P(A)P(B)P(C)$.

### 乘积概率空间 (product probability space)

独立实验 $(S_1,P_1), (S_2,P_2)$:
$$P(E_1\times E_2)=P_1(E_1)P_2(E_2).$$

**定义 / 构造约定, 无需证明** (在有限样本空间上可直接定义矩形事件概率为乘积, 再由可加性延拓到并). 该构造保证「第一实验结果属 $E_1$」与「第二属 $E_2$」独立:
$$P\bigl((E_1\times S_2)\cap(S_1\times E_2)\bigr)=P(E_1\times E_2)=P_1(E_1)P_2(E_2).$$

### 有放回 (with replacement) vs 无放回 (without replacement)

- 有放回: 通常可建模为乘积空间
- 无放回: 依赖, 用条件概率/组合计数

**对比公式 (有限总体)**: 总体 $N$ 个, $K$ 个成功型; 两次无放回抽到两次成功:
$$P(\text{两次成功})=\frac{K}{N}\cdot\frac{K-1}{N-1},$$
而有放回为 $(K/N)^2$. 前者一般 $\ne$ 乘积, 故不独立.

**证明**: 无放回用乘法法则 $P(A_1\cap A_2)=P(A_1)P(A_2|A_1)$; 第二次条件概率为 $(K-1)/(N-1)$.

---

## 易错点

1. 混淆 $P(A|B)$ 与 $P(B|A)$
2. 「两孩至少一男孩」样本空间必须写**有序**对
3. 两两独立推不出相互独立
4. 互斥与独立: 仅当 $P(A)=0$ 或 $P(B)=0$ 可同时成立

---

## 与后续章节

- Ch.2: 随机变量 (random variable), 将事件概率提升到分布函数 (distribution function)
- Ross 教材 Ch.1 对照阅读

## 关键公式速查

见 `cheatsheet.md` 概率基础部分.
