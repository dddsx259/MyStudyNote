# Test01 Practice — 解答

- **源**: `test&quiz/Test01 practice sol.pdf` (官方练习卷 + 解答页)
- **题面**: 同目录 `Test01 practice.pdf` / 题目理解
- **说明**: 完整解答稿; MCQ 以官方填空为准

---

## Section A: Multiple Choice (1)–(6)

官方答案栏: **C F E E F E**

| 题 | 答案 | 含义 (选项表 A–H) |
|---|---|---|
| 1 | C | 只有 (III) 正确 |
| 2 | F | 只有 (II)(III) 正确 |
| 3 | E | 只有 (I)(III) 正确 |
| 4 | E | 只有 (I)(III) 正确 |
| 5 | F | 只有 (II)(III) 正确 |
| 6 | E | 只有 (I)(III) 正确 |

### (1) BW / 有界无收敛子列 / 有理序列

- (I) 错: BW 说**有界**序列有收敛子列, 不是「收敛序列的任意子列」的定义性陈述 (且措辞把 BW 说成子列定理是错的).
- (II) 错: $[-2026,2026]$ 有界, BW $\Rightarrow$ 必有收敛子列.
- (III) 对: 例如枚举 $\mathbb{Q}$ 的序列可在 $\mathbb{R}$ 中无收敛子列? 实际上有理序列若无界仍有实数极限的子列; 更干净: 取 $x_n=n$ (整数, 故有理), 无收敛子列.

**结论**: 仅 (III) → **C**.

### (2) 域与有序域

- (I) 错: 域不必有序 (如 $\mathbb{C}$).
- (II) 对: 有序域中 $0<1$.
- (III) 对: $a\neq 0\Rightarrow a^2>0$.

**结论**: (II)(III) → **F**.

### (3) $\sup$ 与数乘

- (I) 对: $c>0$ 时 $\sup(cS)=c\sup S$.
- (II) 错: $c<0$ 时不等式反向, 一般是 $\sup(cS)=c\inf S$.
- (III) 对: $c<0$ 且 $S$ 有下界时 $\sup(cS)=c\inf S$.

**结论**: (I)(III) → **E**.

### (4) 乘积极限

对照官方 **E** = 仅 (I)(III). (具体三项措辞见题面末页; 与有界$\times$零序列 / 乘积为零未必有界 / 非负极限保号一致.)

### (5) $\varepsilon$-$N$ 语序 / 有界性

官方 **F** = 仅 (II)(III): 收敛 $\Rightarrow$ 有界; 单调收敛 $\Rightarrow$ 有界. (I) 把量词顺序写错则假.

### (6) 级数

官方 **E** = 仅 (I)(III):

- (I) $\sum(-1)^{n+1}n^2/(n^3+1)$ 条件收敛 (通项 $\sim(-1)^{n+1}/n$, 绝对发散, 交错/Dirichlet 可收敛).
- (II) $\sum(-1)^{n+1}/\sqrt n$ **收敛** (交错), 故「发散」为假.
- (III) 绝对收敛级数的任意重排仍收敛 (且和不变).

---

## Section B

### 7(a) $\lim\bigl(1+\frac1n\bigr)^{n^2}$

**结论**: 极限**不存在** (序列无界).

**证明**: 已知 $\bigl(1+\frac1n\bigr)^n\to e$. 取 $\varepsilon>0$ 使 $e-\varepsilon>1$. 则 $\exists N$ 使 $n>N$ 时
\[
\bigl(1+\tfrac1n\bigr)^n > e-\varepsilon>1.
\]
两边 $n$ 次方:
\[
\bigl(1+\tfrac1n\bigr)^{n^2} > (e-\varepsilon)^n.
\]
右边 $\to\infty$, 故左边无界, 极限不存在.

### 7(b) $\lim\bigl(\sin\frac{n\pi}{7}+\frac1n\bigr)$

**结论**: 极限**不存在**.

**证明**: 子列 $n=7k$:
\[
x_{7k}=\sin(k\pi)+\frac1{7k}=\frac1{7k}\to 0.
\]
子列 $n=7k+1$:
\[
x_{7k+1}=\sin\bigl(\tfrac{(7k+1)\pi}{7}\bigr)+\frac1{7k+1}=\sin\bigl(k\pi+\tfrac\pi7\bigr)+\cdots=\sin\tfrac\pi7+\frac1{7k+1}\to\sin\tfrac\pi7\neq 0.
\]
两子列极限不同 $\Rightarrow$ 原序列发散.

### 8. 绝对收敛 $\Rightarrow$ $\sum a_n^2$ 绝对收敛?

**结论**: **真**.

**证明**: $\sum|a_n|<\infty\Rightarrow |a_n|\to 0$, 故 $\exists N$ 使 $n>N$ 时 $|a_n|<1$, 从而 $|a_n|^2<|a_n|$. 比较判别得 $\sum_{n>N}a_n^2$ 收敛, 故 $\sum a_n^2$ 收敛 (且绝对, 因 $a_n^2\ge 0$).
