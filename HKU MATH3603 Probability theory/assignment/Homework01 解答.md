# Homework 1 — 解答

- **来源**: `assignment/Homework01.pdf`
- **课程**: MATH3603 Probability Theory
- **说明**: 按题、按小问分开的完整解答; 交稿前自行核对.
- **官方解答**: `assignment/Homework01 official solution.pdf` (容斥归纳 / 链式法则 / 并事件界 / 次品尺子 Bayes / 独立性推论; **勿覆盖本学生解答**; 核对时对照即可).

---

## 1. 容斥原理 (归纳)

**题意**: 用归纳证明
$$
\begin{align*}
P\Bigl(\bigcup_{i=1}^n E_i\Bigr)
&=\sum_i P(E_i)-\sum_{i<j}P(E_i\cap E_j)+\sum_{i<j<k}P(E_i\cap E_j\cap E_k)\\
&\quad-\cdots+(-1)^{n+1}P(E_1\cap\cdots\cap E_n).
\end{align*}
$$

**解答**:

对 $n$ 归纳.

**$n=1$**: 左边 $P(E_1)$, 右边 $P(E_1)$, 成立.

**$n=2$**: 由二元容斥 (或公理推导)
$$
P(E_1\cup E_2)=P(E_1)+P(E_2)-P(E_1\cap E_2),
$$
即公式在 $n=2$ 时成立. (可证: $E_1\cup E_2=E_1\cup(E_2\setminus E_1)$ 互斥, $P(E_2\setminus E_1)=P(E_2)-P(E_1\cap E_2)$.)

**归纳步**: 假设公式对某个 $k\ge 2$ 及任意 $k$ 个事件成立. 对 $k+1$ 个事件 $E_1,\ldots,E_{k+1}$, 令
$$
A=\bigcup_{i=1}^k E_i,\qquad B=E_{k+1}.
$$
则 $\bigcup_{i=1}^{k+1}E_i=A\cup B$, 且
$$
P(A\cup B)=P(A)+P(B)-P(A\cap B).
$$
对 $A=\bigcup_{i=1}^k E_i$ 用归纳假设展开 $P(A)$. 又
$$
A\cap B=\bigcup_{i=1}^k (E_i\cap E_{k+1}),
$$
对这 $k$ 个事件 $E_i\cap E_{k+1}$ 再用归纳假设展开 $P(A\cap B)$.

把两项合并: 只含 $E_1,\ldots,E_k$ 的交集项来自 $P(A)$; 含 $E_{k+1}$ 的交集项来自 $-P(A\cap B)$, 符号相对「在 $k$ 个事件上的容斥」再乘 $-1$, 恰对应 $(-1)^{m+1}$ 在 $m$ 个下标含 $E_{k+1}$ 时的符号. 于是得到 $n=k+1$ 的容斥公式.

由归纳原理, 对一切 $n$ 成立.

**结论**: 容斥公式由归纳得证.

---

## 2. 条件概率链式法则

**题意**: 证明
$$
P(E_1\cap\cdots\cap E_n)=P(E_1)\,P(E_2|E_1)\,P(E_3|E_1\cap E_2)\cdots P(E_n|E_1\cap\cdots\cap E_{n-1}),
$$
(在出现条件概率处默认条件事件概率为正; 否则两边皆为 $0$ 的约定下仍可讨论.)

**解答**:

对 $n$ 归纳.

**$n=1$**: 两边均为 $P(E_1)$.

**$n=2$**: 由条件概率定义 (若 $P(E_1)>0$),
$$
P(E_2|E_1)=\frac{P(E_1\cap E_2)}{P(E_1)}\Rightarrow P(E_1\cap E_2)=P(E_1)P(E_2|E_1).
$$

**归纳步**: 假设对 $n=k$ 成立. 令 $F=E_1\cap\cdots\cap E_k$. 则
$$
P(E_1\cap\cdots\cap E_{k+1})=P(F\cap E_{k+1})=P(F)\,P(E_{k+1}|F)
$$
(若 $P(F)>0$). 右边第一因子用归纳假设展开为
$$
P(E_1)P(E_2|E_1)\cdots P(E_k|E_1\cap\cdots\cap E_{k-1}),
$$
第二因子即 $P(E_{k+1}|E_1\cap\cdots\cap E_k)$. 故 $n=k+1$ 成立.

**结论**: 链式法则成立.

---

## 3. Boole 不等式

**题意**: 证明 $P\bigl(\bigcup_{i=1}^n E_i\bigr)\le\sum_{i=1}^n P(E_i)$.

**解答**:

先看 $n=2$. 因 $E_1\cup E_2=E_1\cup(E_2\setminus E_1)$ 且二者互斥,
$$
P(E_1\cup E_2)=P(E_1)+P(E_2\setminus E_1)\le P(E_1)+P(E_2),
$$
其中用了 $E_2\setminus E_1\subseteq E_2\Rightarrow P(E_2\setminus E_1)\le P(E_2)$.

一般 $n$: 按提示构造互斥化
$$
F_1=E_1,\qquad
F_i=E_i\cap\bigcap_{j=1}^{i-1}E_j^c\quad(i=2,\ldots,n).
$$
则:
1. $F_i\subseteq E_i$, 故 $P(F_i)\le P(E_i)$;
2. $F_i$ 两两互斥 (若 $i<k$, 则 $F_k\subseteq E_i^c$, 与 $F_i\subseteq E_i$ 不交);
3. $\bigcup_{i=1}^n F_i=\bigcup_{i=1}^n E_i$ (每个落在并中的点有最小下标 $i$ 使其属于 $E_i$, 则该点属于 $F_i$).

由有限可加性,
$$
P\Bigl(\bigcup_{i=1}^n E_i\Bigr)=P\Bigl(\bigcup_{i=1}^n F_i\Bigr)=\sum_{i=1}^n P(F_i)\le\sum_{i=1}^n P(E_i).
$$

**结论**: Boole 不等式成立.

---

## 4. 两厂次品 (Bayes)

设 $I$, $II$ 表示尺子来自工厂 I, II; $D$ 表示次品. 产量比 $2:1$, 故
$$
P(I)=\frac23,\qquad P(II)=\frac13.
$$
已知 $P(D|I)=0.2=\frac15$, $P(D|II)=0.05=\frac1{20}$.

### (i)

**题意**: 随机抽一根合格的概率.

**解答**: 先求次品概率 (全概率公式):
$$
\begin{align*}
P(D)
&=P(D|I)P(I)+P(D|II)P(II)\\
&=0.2\cdot\frac23+0.05\cdot\frac13
=\frac{0.4}{3}+\frac{0.05}{3}
=\frac{0.45}{3}
=0.15.
\end{align*}
$$
合格概率
$$
P(D^c)=1-P(D)=1-0.15=0.85.
$$

**结论**: $0.85$ (或 $\dfrac{17}{20}$).

---

### (ii)

**题意**: 已知次品, 来自工厂 I 的概率.

**解答**: Bayes 公式:
$$
P(I|D)=\frac{P(D|I)P(I)}{P(D)}=\frac{0.2\cdot\tfrac23}{0.15}=\frac{0.4/3}{0.15}=\frac{0.4}{0.45}=\frac{8}{9}.
$$

**结论**: $\dfrac{8}{9}$.

---

## 5. 独立性推论

**设定**: $A,B,C$ 相互独立, 即对任意子集其交的概率等于各概率之积. 特别地
$$
\begin{align*}
P(A\cap B)&=P(A)P(B),\\
P(A\cap C)&=P(A)P(C),\\
P(B\cap C)&=P(B)P(C),\\
P(A\cap B\cap C)&=P(A)P(B)P(C).
\end{align*}
$$

### (i)

**题意**: 证明 $A$ 与 $B^c$ 独立, 即 $P(A\cap B^c)=P(A)P(B^c)$.

**解答**:
$$
A=(A\cap B)\cup(A\cap B^c)
$$
且右边互斥, 故
$$
P(A)=P(A\cap B)+P(A\cap B^c).
$$
于是
$$
P(A\cap B^c)=P(A)-P(A\cap B)=P(A)-P(A)P(B)=P(A)\bigl(1-P(B)\bigr)=P(A)P(B^c).
$$

**结论**: $A$ 与 $B^c$ 独立.

---

### (ii)

**题意**: 证明 $A$ 与 $B\cap C$ 独立.

**解答**:
$$
P\bigl(A\cap(B\cap C)\bigr)=P(A\cap B\cap C)=P(A)P(B)P(C)=P(A)\,P(B\cap C),
$$
其中最后一步用了 $B,C$ 独立: $P(B\cap C)=P(B)P(C)$.

**结论**: $A$ 与 $B\cap C$ 独立.

---

### (iii)

**题意**: 证明 $A$ 与 $B\cup C$ 独立.

**解答**:
$$
A\cap(B\cup C)=(A\cap B)\cup(A\cap C).
$$
故
$$
\begin{align*}
P\bigl(A\cap(B\cup C)\bigr)
&=P(A\cap B)+P(A\cap C)-P(A\cap B\cap C)\\
&=P(A)P(B)+P(A)P(C)-P(A)P(B)P(C)\\
&=P(A)\bigl(P(B)+P(C)-P(B)P(C)\bigr)\\
&=P(A)\,P(B\cup C),
\end{align*}
$$
其中 $P(B\cup C)=P(B)+P(C)-P(B\cap C)=P(B)+P(C)-P(B)P(C)$.

**结论**: $A$ 与 $B\cup C$ 独立.
