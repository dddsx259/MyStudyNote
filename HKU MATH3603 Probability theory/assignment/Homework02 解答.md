# Homework 2 — 解答

- **来源**: `assignment/Homework02.pdf`
- **提交稿**: `assignment/Homework02-Dai Yuxuan-3036292116.pdf`
- **课程**: MATH3603 Probability Theory
- **Due**: 2026-10-08
- **说明**: 按题、按小问分开的完整解答. 交稿前自行核对.

---

## 1. 正反面次数差

抛硬币 $n$ 次. 令 $H=$ 正面次数, $T=n-H=$ 反面次数, $X=H-T=2H-n$.

### (i) 可能取值

$H\in\{0,1,\ldots,n\}$, 故
$$
X\in\{2h-n:h=0,1,\ldots,n\}=\{-n,-n+2,\ldots,n-2,n\}.
$$
即与 $n$ 同奇偶、介于 $-n$ 与 $n$ 之间的全体整数.

**结论**: 可能值为 $-n,-n+2,\ldots,n$.

### (ii) $n=3$ 公平币的 PMF

公平币: $H\sim\mathrm{Bin}(3,1/2)$, $P(H=k)=\binom{3}{k}/8$.

| $H$ | $X=2H-3$ | $P(X=\cdot)$ |
|---|---|---|
| 0 | $-3$ | $1/8$ |
| 1 | $-1$ | $3/8$ |
| 2 | $1$ | $3/8$ |
| 3 | $3$ | $1/8$ |

即
$$
p_X(-3)=\frac18,\quad p_X(-1)=\frac38,\quad p_X(1)=\frac38,\quad p_X(3)=\frac18,
$$
其余为 $0$.

---

## 2. 密度 $f(x)=c(4x-2x^2)$ on $(0,2)$

### (a) 求 $c$

$$
\int_0^2 c(4x-2x^2)\,dx=c\Bigl[2x^2-\frac{2}{3}x^3\Bigr]_0^2=c\Bigl(8-\frac{16}{3}\Bigr)=c\cdot\frac{8}{3}=1.
$$
故 $c=\dfrac{3}{8}$.

### (b) $P(1/2<X<3/2)$

$$
\begin{aligned}
P\Bigl(\tfrac12<X<\tfrac32\Bigr)
&=\int_{1/2}^{3/2}\frac38(4x-2x^2)\,dx
=\frac38\Bigl[2x^2-\frac{2}{3}x^3\Bigr]_{1/2}^{3/2}\\
&=\frac38\Biggl(\Bigl(2\cdot\frac94-\frac{2}{3}\cdot\frac{27}{8}\Bigr)-\Bigl(2\cdot\frac14-\frac{2}{3}\cdot\frac18\Bigr)\Biggr)\\
&=\frac38\Biggl(\Bigl(\frac92-\frac94\Bigr)-\Bigl(\frac12-\frac{1}{12}\Bigr)\Biggr)
=\frac38\Biggl(\frac94-\frac{5}{12}\Biggr)
=\frac38\cdot\frac{22}{12}
=\frac38\cdot\frac{11}{6}
=\boxed{\frac{11}{16}}.
\end{aligned}
$$

### (c) $E(X)$ 与 $\mathrm{Var}(X)$

$$
E(X)=\int_0^2 x\cdot\frac38(4x-2x^2)\,dx=\frac38\int_0^2(4x^2-2x^3)\,dx
=\frac38\Bigl[\frac43 x^3-\frac12 x^4\Bigr]_0^2
=\frac38\Bigl(\frac{32}{3}-8\Bigr)=\frac38\cdot\frac{8}{3}=1.
$$

$$
E(X^2)=\int_0^2 x^2\cdot\frac38(4x-2x^2)\,dx=\frac38\int_0^2(4x^3-2x^4)\,dx
=\frac38\Bigl[x^4-\frac{2}{5}x^5\Bigr]_0^2
=\frac38\Bigl(16-\frac{64}{5}\Bigr)=\frac38\cdot\frac{16}{5}=\frac{6}{5}.
$$

$$
\mathrm{Var}(X)=E(X^2)-(EX)^2=\frac65-1=\boxed{\frac15}.
$$

**结论**: $c=3/8$; $P=11/16$; $EX=1$, $\mathrm{Var}(X)=1/5$.

---

## 3. $\max$ 与 $\min$ 的分布函数

设 $X_1,\ldots,X_n$ i.i.d., 共同 CDF $F$. 令 $M=\max\{X_1,\ldots,X_n\}$, $m=\min\{X_1,\ldots,X_n\}$.

$$
F_M(x)=P(M\le x)=P(X_1\le x,\ldots,X_n\le x)=F(x)^n.
$$

$$
F_m(x)=P(m\le x)=1-P(m>x)=1-P(X_1>x,\ldots,X_n>x)=1-\bigl(1-F(x)\bigr)^n.
$$

**结论**: $F_{\max}(x)=F(x)^n$, $F_{\min}(x)=1-(1-F(x))^n$.

---

## 4. 不同生日个数

一年 $365$ 天, $100$ 人独立均匀生日. 令 $X=$ 出现过的不同生日天数.

对 $j=1,\ldots,365$, 令
$$
I_j=\mathbf{1}\{\text{至少一人生日在第 }j\text{ 天}\}.
$$
则 $X=\sum_{j=1}^{365} I_j$.

$$
P(I_j=1)=1-\Bigl(\frac{364}{365}\Bigr)^{100},\qquad E(I_j)=p:=1-\Bigl(\frac{364}{365}\Bigr)^{100}.
$$

$$
EX=\sum_{j=1}^{365} E(I_j)=365\,p=365\Biggl(1-\Bigl(\frac{364}{365}\Bigr)^{100}\Biggr).
$$

对 $j\neq k$,
$$
\begin{aligned}
P(I_j=I_k=1)
&=1-P(I_j=0)-P(I_k=0)+P(I_j=I_k=0)\\
&=1-2\Bigl(\frac{364}{365}\Bigr)^{100}+\Bigl(\frac{363}{365}\Bigr)^{100}.
\end{aligned}
$$
故
$$
E(I_j I_k)=1-2\Bigl(\frac{364}{365}\Bigr)^{100}+\Bigl(\frac{363}{365}\Bigr)^{100},
$$
$$
\mathrm{Cov}(I_j,I_k)=E(I_j I_k)-p^2.
$$
又 $\mathrm{Var}(I_j)=p(1-p)$. 因此
$$
\begin{aligned}
\mathrm{Var}(X)
&=\sum_{j=1}^{365}\mathrm{Var}(I_j)+2\sum_{1\le j<k\le 365}\mathrm{Cov}(I_j,I_k)\\
&=365\,p(1-p)+365\cdot 364\cdot\bigl(E(I_1 I_2)-p^2\bigr).
\end{aligned}
$$

**结论**:
$$
EX=365\Bigl(1-\bigl(\tfrac{364}{365}\bigr)^{100}\Bigr),
$$
$$
\mathrm{Var}(X)=365p(1-p)+365\cdot 364\Bigl(1-2\bigl(\tfrac{364}{365}\bigr)^{100}+\bigl(\tfrac{363}{365}\bigr)^{100}-p^2\Bigr),
$$
其中 $p=1-(364/365)^{100}$.

---

## 5. 单位圆盘上的均匀分布

### (i) 常数 $C$

需 $\iint_{x^2+y^2\le 1} C\,dx\,dy=1$.

**换元 (极坐标)**: $x=r\cos\theta$, $y=r\sin\theta$, $dx\,dy=r\,dr\,d\theta$, 区域 $0\le r\le 1$, $0\le\theta\le 2\pi$.
$$
\int_0^{2\pi}\int_0^1 C\,r\,dr\,d\theta
=C\int_0^{2\pi}d\theta\int_0^1 r\,dr
=C\cdot 2\pi\cdot\frac12
=C\pi=1
\Rightarrow C=\frac{1}{\pi}.
$$

(等价看法: 单位圆盘面积为 $\pi$, 均匀密度常数为 $1/\pi$.)

### (ii) $X$ 的边缘密度

对 $|x|>1$, $f_X(x)=0$. 对 $|x|\le 1$,
$$
f_X(x)=\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\frac{1}{\pi}\,dy=\frac{2\sqrt{1-x^2}}{\pi}.
$$

**结论**: $C=1/\pi$; $f_X(x)=\dfrac{2\sqrt{1-x^2}}{\pi}$ ($|x|\le 1$), 否则 $0$.
