# Test01 Practice — 题目理解

- **来源**: `test&quiz/Test01 practice.pdf` (原名 `Practice Problems 1.pdf`)
- **课程**: MATH2241 Fall 2026; **TEST 1 (PRACTICE)**
- **说明**: 无官方 sol; 下列为题意复述 + 参考判定/思路 (交稿前自行核对). MCQ 选项 A–H 见原卷.

---

## Section A — Multiple Choice (参考答案)

约定: A=仅(I), B=仅(II), C=仅(III), D=(I)(II), E=(I)(III), F=(II)(III), G=全对, H=都不.

### (1) Bolzano–Weierstrass 相关

- (I) **错**: 那是「收敛 $\Rightarrow$ 子列收敛」, 不是 BW 陈述.
- (II) **错**: $[-2026,2026]$ 有界, BW $\Rightarrow$ 必有收敛子列.
- (III) **对**: 如 $x_n=n$ (有理), 无收敛子列.

**参考**: **C**

### (2) 有序域

- (I) **错**: 如 $\mathbb{C}$ 是域但非有序域.
- (II) **对**: 有序域中 $0<1$.
- (III) **对**: $a\neq0\Rightarrow a^2>0$.

**参考**: **F**

### (3) $\sup(cS)$

- (I) **对** ($c>0$).
- (II) **错** ($c<0$ 时不等式反向, 一般 $\sup(cS)=c\inf S$).
- (III) **对** ($c<0$: $\sup(cS)=c\inf S$).

**参考**: **E**

### (4) 乘积极限 / 保序

- (I) **对**: 有界 $\times$ 零序列 $\to0$.
- (II) **错**: 反例 $y_n=0$, $x_n=n$, 乘积为 0 但 $(x_n)$ 无界.
- (III) **对**: 极限保非负.

**参考**: **E**

### (5) 收敛定义量化词

- (I) **错**: 「$\exists N\ \forall\varepsilon$」把量词顺序写反; 正确是 $\forall\varepsilon\ \exists N$.
- (II) **对**.
- (III) **对** (收敛 $\Rightarrow$ 有界, 单调与否无关).

**参考**: **F**

### (6) 级数

- (I) **对**: $\sim(-1)^{n+1}/n$ 型, AST 收敛, 绝对如谐和发散 $\Rightarrow$ 条件收敛.
- (II) **错**: $\sum(-1)^{n+1}/\sqrt n$ 由 AST **收敛** (题干写 divergent 为假).
- (III) **对**: 绝对收敛 $\Rightarrow$ 任意重排仍收敛 (同和).

**参考**: **E**

---

## Section B — Long Answer

### (7) 极限是否存在

**(a)** $\displaystyle\lim_n\Bigl(1+\frac1n\Bigr)^{n^2}$.

- **思路**: $\bigl(1+1/n\bigr)^n\to e$, 故原式 $=\Bigl[\bigl(1+1/n\bigr)^n\Bigr]^n\sim e^n\to+\infty$. **发散到 $+\infty$** (极限在 $\mathbb{R}$ 中不存在; 若允许广义极限则 $+\infty$).

**(b)** $\displaystyle\lim_n\Bigl(\sin\frac{n\pi}{7}+\frac1n\Bigr)$.

- **思路**: $\sin(n\pi/7)$ 在单位圆上取有限多个值且不趋于单点 (角度 $\pi/7$ 与 $\pi$ 有理相关, 轨道有限周期/有限集且非单点). 加 $1/n\to0$ 后仍有至少两个不同的子列极限 $\Rightarrow$ **极限不存在**.

### (8) 绝对收敛 $\Rightarrow$ $\sum a_n^2$ 绝对收敛?

**陈述**: 若 $\sum|a_n|<\infty$, 则 $\sum|a_n|^2<\infty$.

**判定**: **真**. 因 $a_n\to0$, 大 $n$ 时 $|a_n|<1$ $\Rightarrow$ $|a_n|^2\le|a_n|$; 比较判别.

**反方向不必真**: 如 $a_n=1/n$, $\sum a_n^2$ 收敛但 $\sum|a_n|$ 发散 — 本问只证「绝对 $\Rightarrow$ 平方绝对」.

---

## 备考用法

1. 先限时闭卷做 Section A+B, 再对上面参考.
2. 与 `exercise/Exercise02 review1 worksheet` + Tut1–3 交叉查缺.
3. 量词顺序 (Q5) 与有序域公理 (卷末 O1–O5) 是高频易错点.
