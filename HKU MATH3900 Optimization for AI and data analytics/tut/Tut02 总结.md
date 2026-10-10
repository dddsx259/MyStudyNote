# Tutorial 2 — 总结

- **来源**: `tut/Tut02.pdf` (2026-09-18); 官方解答 `tut/Tut02 sol.pdf`
- **课程**: MATH3900 Optimization for AI and data analytics

> 下文为题意与要点; 完整书写见官方 sol. 证明类条目写清假设与结论.

---

## 定理: Hessian 凸性判别 (Hessian test for convexity)

**陈述.** 设 $C\subseteq\mathbb{R}^d$ 开且凸, $f:C\to\mathbb{R}$ 二阶连续可微. 则

$$f \text{ 在 } C \text{ 上凸} \quad \Longleftrightarrow \quad \nabla^2 f(x)\succeq 0 \;\; \forall x\in C.$$

### 证明思路 (来自 sol)

**($\Rightarrow$) 凸 $\Rightarrow$ Hessian 半正定**

1. 凸 + 可微 $\Rightarrow$ 一阶刻画: $f(y)\ge f(x)+\nabla f(x)^T(y-x)$.
2. 交换 $x,y$ 后相加, $f(x),f(y)$ 相消, 得梯度单调性:
   $$(\nabla f(y)-\nabla f(x))^T(y-x)\ge 0.$$
3. 固定 $x\in C$, 取 $v\in\mathbb{R}^d$. 因 $C$ 开, 对充分小 $t>0$ 有 $x+tv\in C$. 令 $y=x+tv$, 除以 $t^2>0$ 得
   $$\frac{(\nabla f(x+tv)-\nabla f(x))^T v}{t}\ge 0.$$
4. 令 $t\downarrow 0$, 用 $\nabla f$ 可微:
   $$v^T\nabla^2 f(x)v=\lim_{t\downarrow 0}\frac{(\nabla f(x+tv)-\nabla f(x))^T v}{t}\ge 0.$$
5. $v$ 任意 $\Rightarrow \nabla^2 f(x)\succeq 0$.

**($\Leftarrow$) Hessian 半正定 $\Rightarrow$ 凸**

1. 固定 $x,y\in C$, 令 $d=y-x$, 在段 $[x,y]$ 上定义 $\phi(t)=f(x+td)$, $0\le t\le 1$.
2. 链式法则: $\phi'(t)=\nabla f(x+td)^T d$, $\phi''(t)=d^T\nabla^2 f(x+td)d\ge 0$.
3. 一维 Taylor: 存在 $\tau\in(0,1)$ 使
   $$\phi(1)=\phi(0)+\phi'(0)+\tfrac12\phi''(\tau)\ge \phi(0)+\phi'(0).$$
4. 代入 $\phi(1)=f(y)$, $\phi(0)=f(x)$, $\phi'(0)=\nabla f(x)^T(y-x)$, 得一阶刻画, 故 $f$ 凸.

---

## 1. 概念判断 True / False

| | 判定 | 要点 |
|---|---|---|
| (a) 严格凸 + 可微 + $\nabla f(x^*)=0$ $\Rightarrow$ $x^*$ 唯一全局极小 | **T** | 凸性一阶刻画 $\Rightarrow$ 全局极小; 若另有全局极小 $y^*\ne x^*$, 严格凸在 $\theta x^*+(1-\theta)y^*$ 处严格更小, 矛盾 |
| (b) $f''(x^*)=0$, $f'(x^*)=0$, $f''(x^*)\ge 0$ $\Rightarrow$ 局部极小 | **F** | 反例 $f(x)=x^3$, $x^*=0$: $f'(0)=f''(0)=0$, 但 $x<0$ 时 $f(x)<0=f(0)$; $f''>0$ 才充分 |
| (c) $\mu$-强凸且 $L$-光滑, GD 步长 $1/L$ 的收缩因子 $1-\mu/L=1-1/\kappa$, $\kappa$ 越大越慢 | **T** | 强凸标准界: $f(x^{(k)})-f(x^*)\le (1-\mu/L)^k(f(x^{(0)})-f(x^*))$; $\kappa=L/\mu$ 大则因子更接近 1 |

---

## 2. 逻辑回归: 严格凸 vs 强凸

数据: $a_1=(1,0)^T$, $y_1=1$; $a_2=(1,1)^T$, $y_2=-1$.

$$\ell(x)=\frac12\sum_{i=1}^2 \log\bigl(1+e^{-y_i a_i^T x}\bigr), \quad m_i(x)=y_i a_i^T x, \quad w_i(x)=\frac{e^{m_i(x)}}{(1+e^{m_i(x)})^2}.$$

已知 $\nabla^2\ell(x)=\frac12\sum_i w_i(x)a_i a_i^T$.

### (a) Hessian 正定 $\Rightarrow$ 严格凸

- 有限 $x$ 时 $w_i(x)>0$.
- 对 $z=(z_1,z_2)^T$:
  $$z^T\nabla^2\ell(x)z=\frac12\bigl[w_1(x)z_1^2+w_2(x)(z_1+z_2)^2\bigr]\ge 0.$$
- 若 $=0$, 由 $w_1,w_2>0$ 得 $z_1=0$ 且 $z_1+z_2=0$, 故 $z=0$. 所以 $\nabla^2\ell(x)\succ 0$.
- 段上 $g(\theta)=\ell(u+\theta(v-u))$ 满足 $g''(\theta)=(v-u)^T\nabla^2\ell(\cdot)(v-u)>0$ ($v\ne u$), 故 $\ell$ 严格凸.

### (b) 沿 $x_t=t(1,-2)^T$: 非强凸, $\inf\ell=0$ 不可达

- 该方向上 $m_1(x_t)=m_2(x_t)=t$, 故 $w_1(x_t)=w_2(x_t)=\dfrac{e^t}{(1+e^t)^2}\to 0$ ($t\to\infty$).
- $e_2=(0,1)^T$: $e_2^T\nabla^2\ell(x_t)e_2=\frac12 w_2(x_t)\to 0$. 若 $\ell$ 为 $\mu$-强凸, 则 $\nabla^2\ell(x)\succeq\mu I$ 处处成立, 矛盾. 故**非强凸**.
- $\ell(x_t)=\log(1+e^{-t})\to 0$; 有限 $x$ 上每项 $\log(1+e^{-m_i})>0$, 故 $\ell(x)>0$, $\inf\ell=0$ 但 $\arg\min\ell=\varnothing$.
- **不矛盾严格凸**: 严格凸只保证极小点**若存在则唯一**, 不保证无界域上存在极小点.

---

## 3. 条件数与梯度下降

$$f_\kappa(x)=\frac12(x_1^2+\kappa x_2^2), \quad \kappa\ge 1.$$

### (a)  sharp 常数

$$\nabla f_\kappa=(x_1,\kappa x_2)^T, \quad \nabla^2 f_\kappa=\begin{pmatrix}1&0\\0&\kappa\end{pmatrix}.$$

Hessian 特征值 $1,\kappa$ $\Rightarrow$ **$\mu=1$**, **$L=\kappa$**, **条件数 $\kappa=L/\mu$**.

### (b) GD, 步长 $\alpha=1/L=1/\kappa$

坐标解耦:

- $x_1$: $x_1^{(k+1)}=(1-\frac1\kappa)x_1^{(k)}$.
- $x_2$: $x_2^{(k+1)}=x_2^{(k)}-\frac1\kappa\cdot\kappa x_2^{(k)}=0$ (**一步清零**).

故 $k\ge 1$ 时

$$x^{(k)}=\begin{pmatrix}(1-\frac1\kappa)^k x_1^{(0)} \\ 0\end{pmatrix}.$$

### (c) 大 $\kappa$ 为何慢

- 步长 $1/\kappa$ 针对高曲率方向 $x_2$ ($L=\kappa$) 恰好一步消掉.
- 同一 $\alpha$ 对平坦方向 $x_1$ ($\mu=1$) 过小, 每步收缩 $(1-1/\kappa)=1-\mu/L$, $\kappa$ 大时接近 1.
- 瓶颈在 $x_1$, 与理论速率因子 $1-1/\kappa$ 一致.

---

## 易错点

1. Hessian 半正定 $\Rightarrow$ 凸; 正定 $\Rightarrow$ 严格凸 (需段上 $g''>0$ 论证).
2. 严格凸 $\ne$ 强凸; 无界域上可有 $\inf=0$ 但不可达.
3. SOC $f''(x^*)\ge 0$ 非局部极小必要条件; $f''>0$ 才充分.
4. 条件数大: 高曲率坐标快, 低曲率坐标慢, 整体由 $\mu$ 决定.
