# Tutorial 3 — 总结

- **来源**: `tut/Tut03.pdf`; 官方解答 `tut/Tut03 sol.pdf`
- **课程**: MATH3900 Optimization for AI and data analytics

> 下文整理 sol; 主题: 条件数 / Newton / Armijo / 逻辑回归一步比较 / 一维 Newton 局部二次收敛 / 精确线搜索 vs Armijo.

---

## 1. True / False

| | 判定 | 要点 |
|---|---|---|
| (a) $f(x)=\frac12 x^T Qx$, $Q\succ 0$; 乘正数 $s$ 后条件数不变 | **T** | $\kappa(sf)=sL/(s\mu)=L/\mu$ |
| (b) $H$ 可逆 $\Rightarrow$ Newton 方向必使二次模型取极小 | **F** | 反例 $f(t)=-t^2/2$ 于 $t=1$: $H=-1$ 可逆, 模型无下界 (鞍/极大) |
| (c) $H\succ 0$, $\nabla f\neq 0$ $\Rightarrow$ Newton 方向为下降方向 | **T** | $g^Tp=-p^THp<0$ |
| (d) 可微凸 + Armijo 步 $\alpha$ $\Rightarrow$ $\alpha/2$ 亦 Armijo | **T** | 中点凸性: $f(x+\frac\alpha2 p)\le\frac12 f(x)+\frac12 f(x+\alpha p)$ |

---

## 2. 逻辑回归六样本

数据: $(1,0)$ 标签 $+1,+1,-1$; $(0,3)$ 标签 $+1,+1,-1$.
$$
F(x)=\frac16\sum_{i=1}^6\log(1+e^{-y_i a_i^Tx}).
$$

### (a)

用 $\log(1+e^{-t})=\log(1+e^t)-t$:
$$
F(x)=\tfrac12\log(1+e^{x_1})+\tfrac12\log(1+e^{3x_2})-\tfrac13 x_1-x_2.
$$
$$
\nabla F=\begin{pmatrix}\frac12\sigma(x_1)-\frac13\\ \frac32\sigma(3x_2)-1\end{pmatrix},\quad
\nabla^2 F=\begin{pmatrix}\frac12 w(x_1)&0\\ 0&\frac92 w(3x_2)\end{pmatrix}.
$$

### (b)

$w\le 1/4$ $\Rightarrow$ $\lVert\nabla^2 F\rVert_2\le 9/8$. 于 $0$: $\nabla^2 F(0)=\mathrm{diag}(1/8,9/8)$, 方向 $e_2$ 得锐界 **$L=9/8$**.

### (c)

$x^{(0)}=0$, $g_0=(-1/12,-1/4)^T$.

- GD ($1/L=8/9$): $x^{(1)}_{GD}=(2/27,2/9)^T$.
- Newton: $p=(2/3,2/9)^T$, $x^{(1)}_N=(2/3,2/9)^T$.

$x^\star=(\log 2,\frac13\log 2)^T\approx(0.693,0.231)$. Newton 更近; **非**一步到达 (非二次目标, Hessian 随点变).

---

## 3. 一维 Newton: $f(t)=t^3/3-t$ ($t>0$)

### (a)

$f'=t^2-1$, $f''=2t$; $t^\star=1$. 于 $t=2$: $m(p)=\frac23+3p+2p^2$.

### (b)

$$
t^{(k+1)}=\frac12\Bigl(t^{(k)}+\frac{1}{t^{(k)}}\Bigr).
$$
$t^{(0)}=2$ $\Rightarrow$ $t^{(1)}=5/4$, $t^{(2)}=41/40$.

### (c)

在 $D=[1/2,3/2]$: $|f''(u)-f''(v)|=2|u-v|$ (2-Lipschitz), $f''\ge 1$. 误差 $e_{k+1}=e_k^2/(2t^{(k)})$. $|e_k|\le 1/2$ $\Rightarrow$ $|e_{k+1}|\le|e_k|^2\le 1/4$, 得**局部二次收敛**.

---

## 4. 二次型线搜索与 Armijo

$f(x)=\frac12(x_1^2+3x_2^2)$, $x=(3,1)^T$, $p=-g$.

### (a)

$g=(3,3)^T$, $g^Tp=-18$, $\phi(\alpha)=6-18\alpha+18\alpha^2$. 精确步 $\alpha^\star=1/2$, 新点 $(3/2,-1/2)$, $f=3/2$.

### (b)

$c_A=1/4$: Armijo $\Leftrightarrow$ $0<\alpha\le 3/4$.

### (c)

- $\alpha=1/4$: $\phi=21/8\le 39/8$ (Armijo 成立), 但非精确步.
- $\alpha=5/6$: $\phi=7/2<6$ (下降), 但 $7/2>9/4$ (**不**满足 Armijo).

区分: 精确线搜索 / 满足 Armijo / 仅下降.

---

## 易错点

1. Newton 需 $H\succ 0$ 才保证二次模型有极小且方向下降.
2. Armijo 半步论证依赖**凸性**.
3. 逻辑回归全局 $L$ 由 Hessian 谱半径上确界决定, 须证锐性.
4. 全 Newton 步对非二次目标一般不能一步到最优.
