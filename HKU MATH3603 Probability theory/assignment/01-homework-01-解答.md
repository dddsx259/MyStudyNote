# Homework 1 — 解答提示

- **来源**: `assignment/01-homework-01.pdf`
- **课程**: MATH3603 (提示向, 非完整交稿替代)

## Q1 容斥 (归纳)

**证明思路**: $n=1$ 显然. 假设对 $n=k$ 成立. 对 $n=k+1$, 令 $A=\bigcup_{i=1}^k E_i$, $B=E_{k+1}$. 用二元容斥
$P(A\cup B)=P(A)+P(B)-P(A\cap B)$, 再把 $P(A)$ 与 $P(A\cap B)=P(\bigcup_i (E_i\cap E_{k+1}))$ 用归纳假设展开并合并同类项.

## Q2 链式法则

**证明思路**: 由条件概率定义反复改写:
$P(E_1\cap E_2)=P(E_1)P(E_2|E_1)$, 再对 $E_1\cap E_2\cap E_3$ 同理, 归纳即可.

## Q3 Boole

**证明思路**: 取 $F_1=E_1$, $F_i=E_i\cap\bigcap_{j<i} E_j^c$. 则 $F_i$ 互斥且 $\bigcup F_i=\bigcup E_i$, 故
$P(\bigcup E_i)=\sum P(F_i)\le\sum P(E_i)$ (因 $F_i\subseteq E_i$).

## Q4 次品 Bayes

设 $I,II$ 为来自两厂; 产量比 $P(I):P(II)=2:1$ ⇒ $P(I)=\tfrac23$, $P(II)=\tfrac13$.
$P(D|I)=0.2$, $P(D|II)=0.05$.

(i) 合格: $P(D^c)=1-P(D)$, $P(D)=P(D|I)P(I)+P(D|II)P(II)$.

(ii) $P(I|D)=\dfrac{P(D|I)P(I)}{P(D)}$.

## Q5 独立性推论

用 $P(A\cap B)=P(A)P(B)$ 等定义直接算:

(i) $P(A\cap B^c)=P(A)-P(A\cap B)=P(A)(1-P(B))=P(A)P(B^c)$.

(ii) $P(A\cap B\cap C)=P(A)P(B)P(C)=P(A)P(B\cap C)$ (因 $B,C$ 亦独立于三维独立假设).

(iii) $P(A\cap(B\cup C))=P((A\cap B)\cup(A\cap C))$ 展开并用独立消项, 得 $P(A)P(B\cup C)$.
