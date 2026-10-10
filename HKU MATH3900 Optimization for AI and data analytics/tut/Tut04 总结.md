# Tutorial 4 — 总结

- **来源**: `tut/Tut04.pdf`; 官方解答 `tut/Tut04 sol.pdf`
- **课程**: MATH3900 Optimization for AI and data analytics

> 下文整理 sol; 主题: Newton + Armijo 回溯的全局/二次收敛; T/F; 二次型 Armijo 试步计算.

> **与 Test1 scope**: Test1 止于「descent + backtracking 全局收敛」, **不含** p.40+ Newton-with-backtracking. 本 Tut Q1 属 Test1 **之后**; 备考 Test1 时优先 Tut1–3 / HW1. Q2–Q3 的 Armijo 计算仍可作线搜索复习.

---

## 1. Newton + Armijo backtracking

设定: $f$ 二阶连续可微, $\mu$-强凸, $L$-光滑; $0<\mu\le L$. Hessian 界 $\mu I\preceq H_k\preceq LI$. 可用课堂全局收敛定理: 有下界 + $L$-光滑 + 方向满足
$$
g_k^Tp_k\le-\sigma\|g_k\|^2,\quad \|p_k\|\le\beta\|g_k\|
$$
($\sigma,\beta>0$ 固定) $\Rightarrow$ $\|g_k\|\to0$.

### (a) 方向界

$H_k^{-1}$ 特征值在 $[1/L,1/\mu]$. $p_k=-H_k^{-1}g_k$ 得
$$
g_k^Tp_k=-g_k^TH_k^{-1}g_k\le-\frac1L\|g_k\|^2,\qquad \|p_k\|\le\frac1\mu\|g_k\|.
$$
故 $\sigma=1/L$, $\beta=1/\mu$.

### (b) 到最优点距离

强凸双向不等式相加: $\mu\|e\|^2\le g^Te\le\|g\|\|e\|$ ($e=x-x^\star$) $\Rightarrow$ $\|x-x^\star\|\le\|\nabla f(x)\|/\mu$.

### (c) 全局收敛

强凸 $\Rightarrow$ $f$ 强制且唯一极小. (a)+(定理) $\Rightarrow$ $\|g_k\|\to0$; 再 (b) $\Rightarrow$ $x_k\to x^\star$.

### (d) 最终满步 $\alpha_k=1$

额外: $\bar\alpha=1$, $c_A<1/2$, Hessian $\rho$-Lipschitz. 用
$$
f(x+p)\le f(x)+g^Tp+\tfrac12 p^THp+\tfrac\rho6\|p\|^3
$$
与 $g^Tp=-p^THp$: 满步通过 Armijo 当 $\frac\rho6\|p\|\le\mu(\tfrac12-c_A)$. 因 $x_k\to x^\star$ 且 $\|p_k\|\to0$, 最终整段 $x_k+tp_k$ 落在邻域内且该不等式成立 $\Rightarrow$ 接受 $\alpha=1$.

### (e) 二次收敛

满步后
$$
\|x_{k+1}-x^\star\|\le\frac\rho{2\mu}\|x_k-x^\star\|^2.
$$
(用 FTC: $g=\int_0^1 H(x^\star+te)e\,dt$, 再 $\|H(x)^{-1}\|\le1/\mu$ + Lipschitz.)

---

## 2. True / False

| | 判定 | 要点 |
|---|---|---|
| (a) 固定 $c_A$ 时 backtracking 总返回满足 Armijo 的**最大**正步长 | **F** | 只沿 $\bar\alpha,\eta\bar\alpha,\ldots$ 取**第一个**通过者; 反例 $f=t^2/2$, $t=1$, $p=-1$, $c_A=1/4$: 返回 1, 但 $3/2$ 也满足 |
| (b) 有下界 + $f'$ Lipschitz $\Rightarrow$ 每个驻点是全局极小 | **F** | $f=1-\cos t$: $f'(\pi)=0$ 但 $f(\pi)=2>f(0)$; 定理只给 $\|g_k\|\to0$, 不保证驻点=全局极小 (Q1 靠强凸) |

---

## 3. 二次型 Armijo 试步

$f(x)=x_1^2+3x_2^2$, $x=(1,1)^T$, $p=-\nabla f(x)$; $\bar\alpha=1$, $\eta=1/2$.

### (a)

$g=(2,6)^T$, $p=(-2,-6)^T$, $g^Tp=-40$, $\phi(\alpha)=4-40\alpha+112\alpha^2$.

### (b) $c_A=1/4$

Armijo 界 $4-10\alpha$. 试步: $\alpha=1$ 拒; $1/2$ 拒; $1/4$ 接受. 新点 $(1/2,-1/2)$, $f=1$.

### (c)

精确可接受区间: $0<\alpha\le\dfrac{5(1-c_A)}{14}$.

$c_A=3/4$ 时上端点 $5/56$; 首次接受 $\alpha=1/16$, 新点 $(7/8,5/8)$. 例: $\alpha=1/8$ 使 $f$ 下降但不满足 Armijo.

---

## 易错点

1. Newton 方向界来自 $H^{-1}$ 的谱, 不是 $H$ 本身.
2. 满步 Armijo 需要 $c_A<1/2$ 与 $\|p\|$ 充分小 (Hessian Lipschitz).
3. Backtracking $\ne$ 线搜索最大值; 只是几何试步序列.
4. 「梯度 $\to0$」$\ne$「每个驻点全局最优」(缺凸/强凸).
