# 题集 — Ch01 Foundations of Probability

> 对齐: `Lec/Lec01 probability theory lecture notes Ch01 讲义.md`.
> 含: (1) 练习题 (HW1 / Tut1–2 / 讲义例题) (2) 课件证明.

## 课件证明

### P1. 命题 1.1.10 (Probability axioms consequences)

- **陈述**: **假设** $(S,\mathcal{F},P)$ 为概率空间; **结论** $P(\emptyset)=0$, $P(A^c)=1-P(A)$, 且 $A\subseteq B\Rightarrow P(A)\le P(B)$.
- **证明**: (1) 取互斥列 $A_i=\emptyset$, 可数可加得 $P(\emptyset)=\sum_{i\ge1}P(\emptyset)$, 故 $P(\emptyset)=0$. (2) $A\cup A^c=S$ 互斥, $P(A)+P(A^c)=1$. (3) $B=A\cup(B\setminus A)$ 互斥, $P(B)=P(A)+P(B\setminus A)\ge P(A)$.
- **来源**: `Lec/Lec01 probability theory lecture notes Ch01 讲义.md` §1.2

### P2. 有限可加性 (Finite additivity)

- **陈述**: **假设** $A_1,\ldots,A_n$ 两两互斥; **结论** $P(\bigcup_{i=1}^n A_i)=\sum_{i=1}^n P(A_i)$.
- **证明**: 令 $A_{n+1}=A_{n+2}=\cdots=\emptyset$, 可数可加性与 $P(\emptyset)=0$ 即得.
- **来源**: 同上 §1.2

### P3. 两事件容斥 (Inclusion–exclusion, two events)

- **陈述**: **结论** $P(A\cup B)=P(A)+P(B)-P(A\cap B)$.
- **证明**: $A\cup B=A\cup(B\setminus A)$ 与 $B=(A\cap B)\cup(B\setminus A)$ 均为互斥分解, 相减消去 $P(B\setminus A)$.
- **来源**: 同上 §1.2

### P4. 乘法法则 (Multiplication rule)

- **陈述**: **结论** $P(A\cap B)=P(A|B)P(B)=P(B|A)P(A)$ (在相应条件概率有定义时; 若 $P(B)=0$ 则交集概率为 0, 等式仍成立).
- **证明**: $P(B)>0$ 时由 $P(A|B)=P(A\cap B)/P(B)$ 两边乘 $P(B)$; 对称处理 $P(A)>0$; 零概率情形用单调性.
- **来源**: 同上 §1.3

### P5. 全概率公式 (Law of total probability)

- **陈述**: **假设** $F_1,\ldots,F_n$ 为分区 ($\bigcup F_j=S$, 互斥, $P(F_j)>0$); **结论** $P(E)=\sum_j P(F_j)P(E|F_j)$.
- **证明**: $E=\bigcup_j(E\cap F_j)$ 互斥并, 有限可加得 $P(E)=\sum_j P(E\cap F_j)=\sum_j P(F_j)P(E|F_j)$.
- **来源**: 同上 §1.3

### P6. 贝叶斯定理 (Bayes' theorem)

- **陈述**: **假设** 同上分区; **结论** $P(F_i|E)=\dfrac{P(F_i)P(E|F_i)}{\sum_j P(F_j)P(E|F_j)}$.
- **证明**: $P(F_i|E)=P(F_i\cap E)/P(E)$, 分子用乘法法则, 分母用全概率.
- **来源**: 同上 §1.3

### P7. 条件概率仍为概率测度

- **陈述**: **假设** $P(B)>0$, $Q(A):=P(A|B)$; **结论** $Q$ 满足概率公理.
- **证明**: 非负显然; $Q(S)=P(B|B)=1$; 若 $A_i$ 互斥, 则 $(\bigcup A_i)\cap B=\bigcup(A_i\cap B)$ 互斥, $Q(\bigcup A_i)=\sum Q(A_i)$.
- **来源**: 同上 §1.3 补充

### P8. 独立的等价刻画 (Independence equivalence)

- **陈述**: **假设** $P(B)>0$; **结论** $A\perp\!\!\!\perp B\iff P(A|B)=P(A)\iff P(A\cap B)=P(A)P(B)$.
- **证明**: $P(A|B)=P(A)\Leftrightarrow P(A\cap B)/P(B)=P(A)\Leftrightarrow P(A\cap B)=P(A)P(B)$.
- **来源**: 同上 §1.4

### P9. 互斥与独立 (Disjoint vs independent)

- **陈述**: **假设** $A,B$ 互斥且 $P(A),P(B)>0$; **结论** $A,B$ 不独立.
- **证明**: $P(A\cap B)=0\neq P(A)P(B)$.
- **来源**: 同上 §1.4

### P10. 无放回两次成功概率

- **陈述**: **假设** 总体 $N$ 个, 成功 $K$ 个, 无放回抽两次; **结论** $P(\text{两次成功})=\dfrac{K}{N}\cdot\dfrac{K-1}{N-1}\neq (K/N)^2$ (一般有放回时).
- **证明**: 乘法法则, $P(A_2|A_1)=(K-1)/(N-1)$.
- **来源**: 同上 §1.4

### P11. 独立对补集封闭 (自拟) (independence is preserved under complements)

- **陈述**: **假设** $A,B$ 独立; **结论** $A^c$ 与 $B$ 独立, $A^c$ 与 $B^c$ 独立. 若 $A,B,C$ 相互独立, 则 $A^c,B^c,C^c$ 相互独立.
- **证明**: $P(A^c\cap B)=P(B)-P(A)P(B)=P(A^c)P(B)$. $P(A^c\cap B^c)=1-P(A)-P(B)+P(A)P(B)=P(A^c)P(B^c)$. 三元补用容斥展开 $1-P(A\cup B\cup C)$, 每项换成乘积后等于 $(1-P(A))(1-P(B))(1-P(C))$.
- **来源**: `Lec/Lec01 probability theory lecture notes Ch01 讲义.md` §1.4

## 练习题

### 1. 容斥原理 (归纳)

- **题目**: 用归纳证明
  $$P\Bigl(\bigcup_{i=1}^n E_i\Bigr)=\sum_i P(E_i)-\sum_{i<j}P(E_i\cap E_j)+\cdots+(-1)^{n+1}P(E_1\cap\cdots\cap E_n).$$
- **思路**: $n=1,2$ 基例; 令 $A=\bigcup_{i=1}^k E_i$, $B=E_{k+1}$, 展开 $P(A\cup B)$ 并对 $A\cap B$ 再用归纳假设合并符号.
- **来源**: HW1 Q1 / `assignment/Homework01 解答.md`

### 2. 条件概率链式法则

- **题目**: 证明
  $$P(E_1\cap\cdots\cap E_n)=P(E_1)P(E_2|E_1)\cdots P(E_n|E_1\cap\cdots\cap E_{n-1}).$$
- **思路**: 对 $n$ 归纳; $n=2$ 用定义; 步 $F=E_1\cap\cdots\cap E_k$, $P(F\cap E_{k+1})=P(F)P(E_{k+1}|F)$.
- **来源**: HW1 Q2 / `assignment/Homework01 解答.md`

### 3. Boole 不等式 (有限)

- **题目**: 证明 $P\bigl(\bigcup_{i=1}^n E_i\bigr)\le\sum_{i=1}^n P(E_i)$.
- **思路**: 互斥化 $F_1=E_1$, $F_i=E_i\cap\bigcap_{j<i}E_j^c$; 并集概率等于 $\sum P(F_i)\le\sum P(E_i)$.
- **来源**: HW1 Q3 / `assignment/Homework01 解答.md`

### 4. 两厂尺子次品

- **题目**: I 产量为 II 的 2 倍; I 次品率 20%, II 5%. (i) 随机一根合格概率; (ii) 已知次品, 来自 I 的概率.
- **思路**: $P(I)=2/3$; 全概率得 $P(D)=0.15$; (ii) Bayes $P(I|D)=8/9$.
- **来源**: HW1 Q4 / `assignment/Homework01 解答.md`

### 5. 三事件独立的推论

- **题目**: $A,B,C$ 相互独立. 证 (i) $A\perp B^c$; (ii) $A\perp B\cap C$; (iii) $A\perp B\cup C$.
- **思路**: (i) $P(A\cap B^c)=P(A)-P(A)P(B)$; (ii) 用 $P(A\cap B\cap C)$; (iii) 对 $A\cap(B\cup C)$ 容斥.
- **来源**: HW1 Q5 / `assignment/Homework01 解答.md`

### 6. 集合分配律

- **题目**: 证明 $E\cap(F\cup G)=(E\cap F)\cup(E\cap G)$.
- **思路**: 元素 $\in$ 两边双向包含.
- **来源**: Tut1 Q1 / `tut/Tut01 总结.md`

### 7. 互斥事件下的重复试验

- **题目**: $E,F$ 互斥. (a) 重复直到 $E$ 或 $F$ 的样本空间; (b) 无限重复时 $E$ 先于 $F$ 的概率.
- **思路**: (a) 列出终止路径; (b) 几何级数, $P(E)/(P(E)+P(F))$.
- **来源**: Tut1 Q2 / `tut/Tut01 总结.md`

### 8. 可数 Boole 不等式

- **题目**: 证明 $P\bigl(\bigcup_{i=1}^\infty E_i\bigr)\le\sum_{i=1}^\infty P(E_i)$.
- **思路**: 同有限情形构造 $F_i$, 用可数可加.
- **来源**: Tut1 Q3 / `tut/Tut01 总结.md`

### 9. 帽子错排

- **题目**: $n$ 人随机取帽. (a) $n=2$; (b) 一般 $n$ 无人拿回自己帽子的概率.
- **思路**: 错排 $D_n/n!=\sum_{k=0}^n(-1)^k/k!$; $n=2$ 枚举.
- **来源**: Tut1 Q4 / `tut/Tut01 总结.md` (详 `tut/Tut01 sol.pdf`)

### 10. Bill 与 George 打靶

- **题目**: $P(B)=0.6$, $P(G)=0.3$, 独立. (a) 已知恰一枪命中, 是 George 的概率; (b) 已知靶被命中, 是 George 的概率.
- **思路**: (a) $2/9$; (b) $P(G)/(1-0.28)=5/12$. 分母与「恰一命中」不同.
- **来源**: Tut2 Q1 / `tut/Tut02 总结.md`

### 11. 三囚犯 / Monty 变体

- **题目**: 狱卒称 A 若知同伴获释则 $P(A$ 被处决$)$ 从 $1/3$ 升到 $1/2$. 判断并算 $P(A|J_B)$.
- **思路**: $P(A|J_B)=1/3$; A 将被处决时狱卒随机答, 非 Monty 刻意排除.
- **来源**: Tut2 Q2 / `tut/Tut02 总结.md`

### 12. 樱桃与鸽子

- **题目**: 20 颗, 5 带核; 鸽子吃 5 颗, 余 15 中随机 1 颗. (a) 带核概率; (b) 已知带核, 鸽子至少吃过 1 颗带核.
- **思路**: (a) $1/4$ (全概率或对称位); (b) $1-P(\text{五颗全无核}\mid B)$.
- **来源**: Tut2 Q3 / `tut/Tut02 总结.md`

### 13. 飞机错座 (条件于第一人错)

- **题目**: 第 1 人坐错, 之后规则同上. 求已知第 1 人错时最后一人 ($n$) 仍有空座概率.
- **思路**: 闭链; $P(A|B)=(n-2)/(2(n-1))$, 非无条件 $1/2$.
- **来源**: Tut2 Q4 / `tut/Tut02 总结.md`

### 14. 两孩问题

- **题目**: 有序两孩, 已知至少一男孩, 求两男孩概率.
- **思路**: 条件样本 $\{BB,BG,GB\}$, 答案 $1/3$.
- **来源**: Lec Ch01 例题 / `Lec/Lec01 probability theory lecture notes Ch01 讲义.md`

### 15. 两两独立但不相互独立

- **题目**: 构造 $A,B,C$ 两两独立但不相互独立 (例 1.3.4).
- **思路**: 两骰子; $A,B$ 各枚偶, $C$ 同奇偶; $P(ABC)=1/4\neq 1/8$.
- **来源**: Lec Ch01 / `Lec/Lec01 probability theory lecture notes Ch01 讲义.md`

### 16. 有放回 vs 无放回

- **题目**: 总体 $N$, 成功 $K$. 连续两次成功: 有放回 vs 无放回概率.
- **思路**: $(K/N)^2$ vs $(K/N)((K-1)/(N-1))$; 一般不相等.
- **来源**: Lec Ch01 / `Lec/Lec01 probability theory lecture notes Ch01 讲义.md`
