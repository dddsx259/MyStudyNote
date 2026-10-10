# Tutorial 5 — 总结

- **来源**: `tut/Tut05.pdf` (2026-10-06; 原名 `MATH3603_Tutorial_5 (1).pdf`; **尚无官方 sol**)
- **课程**: MATH3603 Probability Theory
- **对齐**: Ch2 联合分布 / 变换 / 独立性 (多在 §2.5–2.6; Quiz1 若只到 2.5, 可优先做 Q1)

> 下列解答据讲义可推; 官方 sol 到后可对照修订.

---

## 1. 联合质量函数与 $U=X+Y$, $V=X-Y$

$$
f(x,y)=\frac{C}{(x+y-1)(x+y)(x+y+1)},\quad x,y=1,2,3,\ldots
$$

**求 $C$, 以及 $U$, $V$ 的质量函数.**

**思路**:

1. **归一化**: 令 $u=x+y$ ($u=2,3,\ldots$). 对固定 $u$, 有 $(u-1)$ 对 $(x,y)$ (因 $x=1,\ldots,u-1$, $y=u-x$). 且
   $$
   \frac{1}{(u-1)u(u+1)}=\frac12\Bigl(\frac{1}{(u-1)u}-\frac{1}{u(u+1)}\Bigr)
   $$
   (部分分式). 于是
   $$
   \sum_{x,y\ge1}f(x,y)=C\sum_{u=2}^\infty(u-1)\cdot\frac{1}{(u-1)u(u+1)}=C\sum_{u=2}^\infty\frac{1}{u(u+1)}=C\sum_{u=2}^\infty\Bigl(\frac1u-\frac1{u+1}\Bigr)=C\cdot\frac12.
   $$
   故 $C\cdot\tfrac12=1\Rightarrow C=2$.

2. **$U=X+Y$**: $P(U=u)=\sum_{x+y=u}f(x,y)=2\cdot(u-1)\cdot\frac{1}{(u-1)u(u+1)}=\frac{2}{u(u+1)}$ ($u\ge2$).

3. **$V=X-Y$**: 对固定整数 $v$, 在 $x,y\ge1$ 上求和. 令 $u=x+y$, 则 $x=(u+v)/2$, $y=(u-v)/2$ 须为正整数, 故 $u\equiv v\pmod 2$, $u>|v|$, $u\ge2$. 于是
   $$
   P(V=v)=\sum_{\substack{u>|v|\\u\equiv v\ (2)}} \frac{2}{(u-1)u(u+1)}.
   $$
   (可再对偶/奇 $v$ 分别化简; 交稿前用部分分式或直接验证归一.)

---

## 2. i.i.d. 的 $\max$ / $\min$

$X,Y$ i.i.d., 共同 CDF $F$, 密度 $f$.

- $V=\max\{X,Y\}$: $P(V\le v)=F(v)^2$, 密度 $f_V(v)=2F(v)f(v)$.
- $U=\min\{X,Y\}$: $P(U\le u)=1-(1-F(u))^2$, 密度 $f_U(u)=2(1-F(u))f(u)$.

**证明**: 直接写 CDF; 密度对 $v$ 求导 (乘积法则).

---

## 3. $XY$ 与 $Z^2$; $P(XY<Z^2)=5/9$

$X,Y,Z\stackrel{\mathrm{iid}}{\sim}\mathrm{Unif}[0,1]$.

**联合密度** (在值域上): 先求 $W=XY$ 的密度. 对 $w\in(0,1)$,
$$
f_W(w)=\int_0^1\mathbf{1}_{0<w/x<1}\frac{1}{x}\,dx=\int_w^1\frac{1}{x}\,dx=-\log w.
$$
$T=Z^2$: $P(T\le t)=\sqrt t$ ($t\in[0,1]$), 密度 $f_T(t)=\frac12 t^{-1/2}$.

因 $(X,Y)\perp Z$, 有 $W\perp T$, 故联合密度
$$
f_{W,T}(w,t)=(-\log w)\cdot\frac12 t^{-1/2},\quad 0<w<1,\ 0<t<1.
$$

**概率**:
$$
P(W<T)=\int_0^1\int_0^t(-\log w)\cdot\tfrac12 t^{-1/2}\,dw\,dt.
$$
内层 $\int_0^t(-\log w)\,dw=[ -w\log w+w]_0^t=t-t\log t$ (用 $\lim_{w\to0}w\log w=0$). 故
$$
P=\int_0^1\tfrac12 t^{-1/2}(t-t\log t)\,dt=\int_0^1\tfrac12\bigl(t^{1/2}-t^{1/2}\log t\bigr)\,dt.
$$
用 $\int_0^1 t^a\,dt=\frac1{a+1}$ 与 $\int_0^1 t^a\log t\,dt=-\frac1{(a+1)^2}$ ($a=1/2$):
$$
\int_0^1 t^{1/2}\,dt=\tfrac23,\qquad \int_0^1 t^{1/2}\log t\,dt=-\tfrac4{9}.
$$
故
$$
P=\tfrac12\cdot\tfrac23-\tfrac12\Bigl(-\tfrac49\Bigr)=\tfrac13+\tfrac29=\tfrac59.
$$

---

## 4. 正态: $X+Y$ 与 $X-Y$ 独立

$X,Y$ i.i.d. $N(\mu,\sigma^2)$. Hint: 联合 MGF.

**证明思路**: 令 $U=X+Y$, $V=X-Y$. 联合 MGF
$$
M_{U,V}(s,t)=E\exp(sU+tV)=E\exp\bigl((s+t)X+(s-t)Y\bigr).
$$
由独立,
$$
=M_X(s+t)M_Y(s-t)=\exp\bigl(\mu(s+t)+\tfrac12\sigma^2(s+t)^2\bigr)\exp\bigl(\mu(s-t)+\tfrac12\sigma^2(s-t)^2\bigr).
$$
展开指数中二次型: $\sigma^2\bigl(s^2+t^2\bigr)+\cdots$, 可写成 $M_U(s)M_V(t)$ 之积 (均值上 $E U=2\mu$, $E V=0$; 方差 $2\sigma^2$ 各一). 故联合 MGF 因子化 $\Rightarrow$ $U\perp V$.

(也可用二维正态: 协方差 $\mathrm{Cov}(U,V)=\mathrm{Var}X-\mathrm{Var}Y=0$, 联合正态 + 不相关 $\Rightarrow$ 独立.)

---

## 易错点

1. 对 $f(x,y)$ 按 $u=x+y$ 切片时记得乘上格子点数 $(u-1)$.
2. $\max$/$\min$ 的 CDF 先写再求导, 勿直接「两密度相乘」.
3. $XY$ 密度是 $-\log w$, 不是均匀.
4. 正态和差独立依赖 **同方差** (或更一般联合正态 + 协方差 0); 非正态时不相关不必独立.
