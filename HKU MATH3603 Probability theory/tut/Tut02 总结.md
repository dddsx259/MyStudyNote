# Tutorial 2 — 总结

- **来源**: `tut/Tut02.pdf`; 官方解答 `tut/Tut02 sol.pdf`
- **课程**: MATH3603 Probability Theory

> 下文整理 sol 中四题解法; 符号与条件概率定义对齐 Ch.1–2.

---

## 1. Bill 与 George 打靶

Bill 命中概率 $P(B)=0.6$, George 独立, $P(G)=0.3$.

记 $S_1$ = 恰有一枪命中, $S_2$ = 两枪都命中.

### (a) 已知恰有一枪命中, 是 George 的概率

$$P(G\mid S_1)=\frac{P(G\cap B^c)}{P(G\cap B^c)+P(B\cap G^c)}=\frac{0.3\times 0.4}{0.3\times 0.4+0.6\times 0.7}=\boxed{\frac{2}{9}}.$$

### (b) 已知靶被命中, 是 George 的概率

靶被命中 $\Leftrightarrow$ 至少一人命中 $= S_1\cup S_2$. 独立下 $P(\text{都未中})=0.4\times 0.7=0.28$.

$$P(G\mid S_1\cup S_2)=\frac{P(G)}{P(\text{靶被命中})}=\frac{0.3}{1-0.28}=\boxed{\frac{5}{12}}.$$

---

## 2. 三囚犯 / Monty Hall 变体

$A/B/C$ = 囚犯 A/B/C 被处决; $J_B/J_C$ = 狱卒私下告知 B/C 将被释放.

规则: 若 B (或 C) 将被处决, 狱卒只能答 C (或 B); 若 A 将被处决, 狱卒可随机答 B 或 C.

狱卒称: 若 A 知道哪位同伴获释, 自己被处决概率会从 $1/3$ 升到 $1/2$. **狱卒错了.**

以 $J_B$ 为例:

$$P(A\mid J_B)=\frac{P(A\cap J_B)}{P(A\cap J_B)+P(C\cap J_B)}=\frac{\frac13\cdot\frac12}{\frac13\cdot\frac12+\frac13}=\boxed{\frac13}=P(A).$$

($A$ 被处决时狱卒答 B 概率 $1/2$; $C$ 被处决时必答 B.) 同理 $P(A\mid J_C)=1/3$.

**要点**: 条件化于狱卒回答不改变 A 的边际概率; 与 Monty Hall 中换门后概率上升不同, 因此处狱卒在 A 将被处决时**随机**透露信息, 非刻意排除 A.

---

## 3. 樱桃与鸽子

20 颗樱桃, 15 颗已去核 (5 颗带核). 鸽子随机吃 5 颗整樱桃, 余下 15 颗中随机取 1 颗.

### (a) 取到的樱桃带核的概率

**法 1 (全概率).** 令 $A_i$ = 鸽子吃了 $i$ 颗带核樱桃 ($i=0,\ldots,5$), $B$ = 取到的樱桃带核.

$$P(B\mid A_i)=\frac{5-i}{15}, \quad P(A_i)=\frac{\binom{5}{i}\binom{15}{5-i}}{\binom{20}{5}}.$$

对 $i$ 求和得 $P(B)=\boxed{\frac14}$.

**法 2 (对称).** 将 20 颗排成一列, 第 6 个位置为所取樱桃: 带核概率 $5/20=1/4$.

### (b) 已知取到的樱桃带核, 鸽子至少吃过 1 颗带核

令 $A$ = 鸽子至少吃过 1 颗带核.

$$P(A^c\mid B)=\frac{P(A^c\cap B)}{P(B)}, \quad P(A^c\cap B)=\frac{\binom{15}{5}\binom{5}{1}}{\binom{20}{5}\binom{15}{1}}.$$

故

$$P(A\mid B)=1-P(A^c\mid B)=\boxed{1-\frac{15}{19}\cdot\frac{14}{18}\cdot\frac{13}{17}\cdot\frac{12}{16}\cdot\frac{11}{15}}.$$

(分子: 鸽子 5 颗全从无核 15 颗中选, 且条件樱桃为 5 颗带核之一.)

---

## 4. 飞机座位 (错座链)

$n$ 个座位, 乘客 $1,\ldots,n$ 依次登机. 第 1 人坐错座; 之后每人若自己的座位空则坐自己的, 否则随机选一空座. **求: 已知第 1 人坐错, 最后一人 ($n$) 找到空座的概率.**

### 经典对照

- 无条件 (第 1 人随机): 最后一人有空座概率 = **$1/2$** (经典结果).
- **本题条件于 "第 1 人坐错"**, 答案不同.

### 解法概要 (sol)

若第 1 人错坐 $i_1$ 号位, 则 $2,\ldots,i_1-1$ 都能坐对; $i_1$ 再随机选座, 形成链 $1\to i_1\to i_2\to\cdots\to i_k\to 1$ (闭链, $i_k\ne n$). 最后一人有空 $\Leftrightarrow$ 闭链长度 $k\in\{1,\ldots,n-2\}$.

$$P(B)=\frac{n-1}{n} \quad (B=\text{第 1 人坐错}).$$

$$P(A\cap B)=\sum_{k=1}^{n-2} P(k)=\frac{n-2}{2n},$$

其中用 $\prod_{t=1}^n(1+X_t)=1+\sum_{k\ge 1}\sum_{i_1<\cdots<i_k}X_{i_1}\cdots X_{i_k}$ 化简求和.

$$\boxed{P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{n-2}{2(n-1)}}.$$

**检验**: $n=2$ 时 $P(A\mid B)=0$ (第 1 人占 2 号位, 最后一人必无座); $n\to\infty$ 时 $\to 1/2$.

---

## 易错点

1. $P(G\mid\text{命中})$ 与 $P(G\mid\text{恰一命中})$ 分母不同.
2. 囚犯题: 狱卒**随机**透露 vs Monty **刻意**开门, 结论不同.
3. 樱桃 (b): 用 $1-P(\text{鸽子零颗带核}\mid B)$, 勿忘条件 $B$ 缩小样本.
4. 座位题: 条件于 "第 1 人错" 时答案 $(n-2)/(2(n-1))$, 非无条件 $1/2$.
