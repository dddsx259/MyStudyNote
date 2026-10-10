# Tutorial 4 — 总结

- **来源**: `tut/Tut04.pdf` (2026-09-29); 官方解答 `tut/Tut04 sol.pdf`
- **课程**: MATH3603 Probability Theory
- **说明**: 已对照官方 sol; 乘积反例官方用 $[0,\sqrt{2}]$ 上密度 $f(x)=x$, 讲义用 Exp/正态同样说明「乘积一般不是密度」.

---

## 1. 密度的凸组合与乘积

**题**: $f,g$ 为密度, $0\le\lambda\le 1$. $\lambda f+(1-\lambda)g$ 是否密度? $fg$ 是否密度?

**解答**:

- **凸组合**: $\lambda f+(1-\lambda)g\ge 0$, 且
  $$
  \int\bigl(\lambda f+(1-\lambda)g\bigr)=\lambda\cdot 1+(1-\lambda)\cdot 1=1.
  $$
  故是密度 (混合分布, mixture).

- **乘积 $fg$**: 一般**不是**. 例如 $f=g=\mathbf{1}_{[0,1]}$ (Unif$[0,1]$ 密度), 则 $fg=\mathbf{1}_{[0,1]}$, 仍碰巧是密度; 但取 $f=g$ 为 $\mathrm{Exp}(1)$ 密度 $e^{-x}\mathbf{1}_{x>0}$, 则
  $$
  \int_0^\infty f(x)g(x)\,dx=\int_0^\infty e^{-2x}\,dx=\tfrac12\neq 1.
  $$
  也可取两个标准正态密度: 乘积正比于 $e^{-x^2}$, 积分不是 $1$. 故乘积一般需再归一化才成密度.

---

## 2. 常见分布的期望与方差

记标准结果 (推导见讲义 / 母函数; 几何取 $P(X=k)=(1-p)^{k-1}p$, $k=1,2,\ldots$).

| 分布 | $E(X)$ | $\mathrm{Var}(X)$ |
|---|---|---|
| (a) $\mathrm{Geom}(p)$ | $1/p$ | $(1-p)/p^2$ |
| (b) $\mathrm{NB}(r,p)$ (至 $r$ 次成功) | $r/p$ | $r(1-p)/p^2$ |
| (c) $\mathrm{Poisson}(\lambda)$ | $\lambda$ | $\lambda$ |
| (d) $\mathrm{Unif}[a,b]$ | $(a+b)/2$ | $(b-a)^2/12$ |
| (e) $\mathrm{Exp}(\lambda)$ | $1/\lambda$ | $1/\lambda^2$ |
| (f) $\mathrm{Gamma}(\alpha,\lambda)$ (rate $\lambda$) | $\alpha/\lambda$ | $\alpha/\lambda^2$ |

**要点推导提示**:

- Geom: $E=\sum k(1-p)^{k-1}p$, 或用 $E=1+(1-p)E$.
- NB: $r$ 个独立 Geom 之和.
- Poisson: $E=\sum k e^{-\lambda}\lambda^k/k!=\lambda$; 方差用 $E[X(X-1)]=\lambda^2$.
- Unif: 直接积分 $x,x^2$ 于 $[a,b]$.
- Exp: $\int_0^\infty x\lambda e^{-\lambda x}=\lambda^{-1}$; 或 Gamma$(1,\lambda)$.
- Gamma: 用密度 $\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}$, 或矩母函数.

(若讲义 Geom 从 $0$ 起计失败次数, 则 $E=(1-p)/p$, $\mathrm{Var}=(1-p)/p^2$; 与上表差 $1$ 的平移.)

---

## 3. 逆变换采样 (Inverse transform sampling)

**题**: $F$ 为 $X$ 的 CDF, $F^{-1}(u)=\inf\{x:F(x)\ge u\}$, $U\sim\mathrm{Unif}[0,1]$. 证 $F^{-1}(U)\stackrel{d}{=}X$.

**证明**: 对任意 $x\in\mathbb{R}$,
$$
P\bigl(F^{-1}(U)\le x\bigr)=P\bigl(\inf\{t:F(t)\ge U\}\le x\bigr).
$$
由广义逆性质: $F^{-1}(u)\le x\iff u\le F(x)$ (对任意 CDF 成立). 故
$$
P\bigl(F^{-1}(U)\le x\bigr)=P\bigl(U\le F(x)\bigr)=F(x)=P(X\le x).
$$
因此 $F^{-1}(U)$ 与 $X$ 同分布.

**注**: $F$ 连续严格增时 $F^{-1}$ 为通常反函数, 证明化为 $P(F^{-1}(U)\le x)=P(U\le F(x))$.

---

## 易错点

1. 混合密度要非负且积分为 1; 乘积通常要重新归一化.
2. Geom / NB 的「从 0 还是从 1」约定影响期望公式.
3. 广义逆 $F^{-1}$ 对跳跃型 CDF 仍成立; 不要只写连续情形.
