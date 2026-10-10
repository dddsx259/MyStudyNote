# Tutorial 3 — 总结

- **来源**: `tut/Tut03.pdf` (2026-09-22); 官方解答 `tut/Tut03 sol.pdf`
- **课程**: MATH3603 Probability Theory

> 下文整理 sol 中四题解法; 对齐二项 / 负二项 / coupon collector / 无记忆性.

---

## 1. 四发 vs 两发飞机

引擎独立, 失效概率 $1-p$; 至少一半引擎工作则飞行成功. 求何时四发优于两发:
$$
P(X_4\ge 2)\ge P(X_2\ge 1),
$$
其中 $X_n\sim\mathrm{Bin}(n,p)$.

$$
\begin{aligned}
P(X_4\ge 2)&=6p^2(1-p)^2+4p^3(1-p)+p^4,\\
P(X_2\ge 1)&=2p(1-p)+p^2.
\end{aligned}
$$
不等式化简为 $p(1-p)^2(3p-2)\ge 0$. 在 $p\in[0,1]$ 上等价于
$$
\boxed{\tfrac23\le p\le 1}.
$$

---

## 2. 负二项 (Negative binomial)

抛硬币至第 $r$ 次正面, $X=$ 总抛次. $\{X=n\}$ = 前 $n-1$ 次恰 $r-1$ 次正面, 且第 $n$ 次正面.

$$
P(X=n)=\binom{n-1}{r-1}p^r(1-p)^{n-r},\qquad n\ge r.
$$

---

## 3. Coupon collector 型等待时

$m$ 种结果, 概率 $p_1,\ldots,p_m$. $X=$ 直到每种至少出现一次所需试验次数. $A_i=$ 前 $n$ 次未出现结果 $i$.

### (a) $m=2$

$$
P(X>n)=P(A_1\cup A_2)=P(A_1)+P(A_2)-P(A_1\cap A_2)=(1-p_1)^n+(1-p_2)^n,
$$
因 $P(A_1\cap A_2)=(1-p_1-p_2)^n=0$.

### (b) 一般 $m$

容斥 (HW1 Q1):
$$
P(X>n)=\sum_{k=1}^{m-1}(-1)^{k+1}\sum_{1\le i_1<\cdots<i_k\le m}\Bigl(1-\sum_{\ell=1}^k p_{i_\ell}\Bigr)^n.
$$

### (c)

$$
P(X=n)=P(X>n-1)-P(X>n),
$$
化简得
$$
P(X=n)=\sum_{k=1}^{m-1}(-1)^{k+1}\sum_{i_1<\cdots<i_k}\Bigl(\sum_{\ell=1}^k p_{i_\ell}\Bigr)\Bigl(1-\sum_{\ell=1}^k p_{i_\ell}\Bigr)^{n-1}.
$$

---

## 4. 无记忆性 (Memoryless)

### (a) 几何 $X\sim\mathrm{Geom}(p)$ (支撑从 $1$ 起, sol 约定)

$$
P(X=n+k\mid X>k)=\frac{P(X=n+k)}{P(X>k)}=\frac{(1-p)^{n+k-1}p}{(1-p)^k}=(1-p)^{n-1}p=P(X=n).
$$

### (b) 指数 $X\sim\mathrm{Exp}(\lambda)$

$$
P(X>n+k\mid X>k)=\frac{e^{-\lambda(n+k)}}{e^{-\lambda k}}=e^{-\lambda n}=P(X>n).
$$

---

## 易错点

1. 飞机题: 「至少 50%」对四发是 $\ge 2$, 对两发是 $\ge 1$.
2. 负二项: 组合数是 $\binom{n-1}{r-1}$, 不是 $\binom{n}{r}$.
3. Geom 支撑从 $0$ 或从 $1$ 起公式不同; 跟讲义/本题约定一致.
4. Coupon: $P(A_1\cap\cdots\cap A_m)=0$ (不可能所有类型都未出现却概率用完).
