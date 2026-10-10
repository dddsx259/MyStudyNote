# MATH3900 Test1 快速复习 (Lec01 Introduction + Lec02 Unconstrained 至 p.39)

> 对齐: `Lec/Lec01 introduction slides 讲义.md`, `Lec/Lec02 unconstrained slides 讲义.md`.
> Scope: Introduction 全部 + Unconstrained **p.1–39** (至「带回溯下降法全局收敛」含). **不含** p.40+ Newton+回溯全局.
> 形式: 紧凑速览; 定义/定理/公式不漏, 证明只留关键步骤. 详证见讲义.

---

## Lec01 Introduction

### 1. 优化一般形式

$$\min_{x\in C} f(x),\quad f:\mathbb{R}^d\to\mathbb{R},\ C\subseteq\mathbb{R}^d.$$

| 术语 | 含义 |
|---|---|
| 决策变量 $x$ | $x\in\mathbb{R}^d$ |
| 目标 $f$ | $\mathbb{R}^d\to\mathbb{R}$ |
| 可行域 $C$ | $C\subseteq\mathbb{R}^d$; 无约束时 $C=\mathbb{R}^d$ |
| 最大化 | $\max f=-\min(-f)$ (最优值差一负号) |

### 2. 最优解

- **全局极小** $x^*$: $f(x^*)\le f(x)\ \forall x\in C$.
- **局部极小**: 在某邻域内最小.
- **最优值** $f^*:=\inf_{x\in C} f(x)$; $x^*$ 达到则 $f(x^*)=f^*$.
- $f^*$ 未必被达到.

**Weierstrass**: $C$ 非空紧 + $f$ 连续 $\Rightarrow$ 全局极小存在.
- 证: $f(C)$ 紧 $\Rightarrow$ 有最小值; 或极小化序列 + 紧性抽子列.

### 3. AI 实例 (写优化问题)

| 模型 | 目标 |
|---|---|
| 线性回归 | $\min \frac{1}{2n}\|Ax-y\|^2$ |
| 逻辑回归 | $\min \frac1n\sum_i \log(1+e^{-y_i a_i^T x})$ (NLL, 非指数损失) |
| 硬间隔 SVM | $\min \frac12\|x\|^2$ s.t. $y_i a_i^T x\ge 1$ |
| Lasso | $\min \frac{1}{2n}\|Ax-y\|^2+\lambda\|x\|_1$ ($\ell_1$ 在 0 不可微) |
| 神经网络 | $\min \frac1n\sum_i L(h(a_i;x),y_i)$ (常非凸) |

逻辑回归损失来源: sigmoid $\sigma(z)=1/(1+e^{-z})$ + NLL: $-\log\sigma(ya^Tx)=\log(1+e^{-ya^Tx})$.

### 4. 线代与梯度

- $F=\frac{1}{2n}\|Ax-y\|^2$ $\Rightarrow$ $\nabla F=\frac1n A^T(Ax-y)$.
- 链式: $\nabla(g\circ h)=J_h^T\nabla g$.

### 5. 沿线 FTC + Taylor

- **线段 FTC**: $f(v)-f(u)=\int_0^1 \nabla f(u+t(v-u))^T(v-u)\,dt$.
- **一阶 Taylor**: $f(x+s)=f(x)+\nabla f(x)^T s+o(\|s\|)$.
- **二阶 Taylor**: $f(x+s)=f(x)+\nabla f^T s+\frac12 s^T\nabla^2 f(x)s+o(\|s\|^2)$.

---

## Lec02 Unconstrained (至 p.39)

### 6. 最优性条件

设 $f$ 可微, $x^*$ 局部极小.

| 阶 | 条件 |
|---|---|
| 一阶必要 | $\nabla f(x^*)=0$ |
| 二阶必要 | $\nabla f(x^*)=0$ 且 $\nabla^2 f(x^*)\succeq 0$ |
| 二阶充分 | $\nabla f(x^*)=0$ 且 $\nabla^2 f(x^*)\succ 0$ $\Rightarrow$ 严格局部极小 |

- 一阶证: 反证 $g=\nabla f(x^*)\ne 0$, 取 $p=-g$, $f(x^*+tp)=f(x^*)-t\|g\|^2+o(t)<f(x^*)$ 矛盾.
- 充分证: $H\succ 0$ $\Rightarrow$ 邻域内 $H\succeq \mu I$, Taylor 积分余项得 $f(x^*+h)\ge f(x^*)+\frac\mu4\|h\|^2$.

**PSD/PD**: $Q=Q^T$, $Q\succeq 0$ $\Leftrightarrow$ 特征值 $\ge 0$; $Q\succ 0$ $\Leftrightarrow$ 特征值 $>0$; $\lambda_{\min}I\preceq Q\preceq\lambda_{\max}I$.

### 7. 下降方向与 GD

- $\nabla f^Tp<0$ $\Rightarrow$ $p$ 下降方向.
- **最速下降**: $p=-\nabla f/\|\nabla f\|$ (Cauchy–Schwarz 等号).
- **GD**: $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$; 停 $\|\nabla f\|\le\varepsilon$.
- 反例 $f=\frac12 x^2$: $x_{k+1}=(1-\alpha)x_k$; $\alpha\in(0,2)$ 收敛, $\alpha=2$ 振荡, $\alpha>2$ 发散.

### 8. $L$-光滑与下降引理

- $f$ **$L$-光滑**: $\|\nabla f(u)-\nabla f(v)\|\le L\|u-v\|$.
- **下降引理**:
  $$f(v)\le f(u)+\nabla f(u)^T(v-u)+\frac L2\|v-u\|^2.$$
  证: 线段 FTC + CS + Lipschitz: 余项 $\le\int_0^1 Lt\|v-u\|^2 dt=\frac L2\|v-u\|^2$.

- **GD 推论** ($0<\alpha<2/L$): $f(x_{k+1})\le f(x_k)-\alpha(1-\frac{L\alpha}{2})\|g_k\|^2$; $\alpha=1/L$:
  $$f(x_{k+1})\le f(x_k)-\frac1{2L}\|g_k\|^2.$$

### 9. 仅 $L$-光滑 + 有下界: GD 收敛 $O(1/k)$

$$\min_{0\le j<k}\|\nabla f(x_j)\|^2\le \frac{2L(f(x_0)-f^*)}{k}.$$

证: 单步下降 $\frac1{2L}\|g_j\|^2\le f(x_j)-f(x_{j+1})$ $\to$ 望远镜求和 $\to$ 用 $f^*$ 下界 $\to$ 和 $\ge k\cdot\min$.

注: 只保证前 $k$ 步某次梯度小, 不保证 $x_k$ 是极小 (非凸可能鞍点).

### 10. 凸性

- **凸函数**: $f(\theta u+(1-\theta)v)\le \theta f(u)+(1-\theta)f(v)$.
- **保持凸性**: 非负线性组合; 仿射复合; 逐点 $\max$.
- **一阶刻画** (可微凸): $f(v)\ge f(u)+\nabla f(u)^T(v-u)$ (切平面全局下界).
  - $\Rightarrow$: 凸性移项除 $t$ 取 $t\to0^+$.
  - $\Leftarrow$: 对 $u_\theta$ 写两次加权相加.
- **推论**: 可微凸时 $x^*$ 全局极小 $\Leftrightarrow$ $\nabla f(x^*)=0$.
- **梯度单调**: $(\nabla f(v)-\nabla f(u))^T(v-u)\ge 0$ (两次切平面相加).
- **二阶刻画** ($C^2$): 凸 $\Leftrightarrow$ $\nabla^2 f\succeq 0$.
  - $\Rightarrow$: 梯度单调 + $t\to0$ 得 $d^T\nabla^2 f d\ge 0$.
  - $\Leftarrow$: $g(t)=f(u+t(v-u))$, $g''\ge 0$ $\Rightarrow$ $g'$ 增 $\Rightarrow$ 积分得切平面下界.
- **积分余项**: $f(v)=f(u)+\nabla f(u)^T(v-u)+\int_0^1(1-t)(v-u)^T\nabla^2 f(\cdot)(v-u)\,dt$.
- 二次型 $\frac12 x^TQx-b^Tx$ 凸 $\Leftrightarrow$ $Q\succeq 0$.
- **逻辑回归凸**: $\nabla^2 \ell_i=w_i(1-w_i)a_ia_i^T\succeq 0$ ($w_i(1-w_i)\ge 0$).

### 11. 凸 + $L$-光滑: GD $O(1/k)$

$$f(x_k)-f^*\le \frac{L\|x_0-x^*\|^2}{2k}=O(1/k).$$

证: 下降引理 + 切平面下界 $\Rightarrow$ 一步有 $f(x_{k+1})-f^*\le \frac L2(\|x_k-x^*\|^2-\|x_{k+1}-x^*\|^2)$; 望远镜 + 平均.

### 12. 强凸与条件数

- **$\mu$-强凸**: $f(v)\ge f(u)+\nabla f(u)^T(v-u)+\frac\mu2\|v-u\|^2$.
- $C^2$: $\mu$-强凸 + $L$-光滑 $\Leftrightarrow$ $\mu I\preceq \nabla^2 f\preceq LI$.
- **条件数** $\kappa:=L/\mu\ge 1$.
- **强凸 + GD** ($\alpha=1/L$): $f(x_k)-f^*\le (1-\mu/L)^k(f(x_0)-f^*)$ (线性收敛).
  - 证: 强凸给 $f(x)-f^*\le \frac1{2\mu}\|\nabla f\|^2$; 代入一步下降得因子 $1-\mu/L$.

### 13. 牛顿法

- 二阶模型 $m_k^{(2)}(p)=f(x_k)+\nabla f^T p+\frac12 p^T H_k p$, $H_k=\nabla^2 f(x_k)$.
- 令 $\nabla_p m=0$: $H_k p_k=-\nabla f(x_k)$, $x_{k+1}=x_k+p_k$.
- **二次目标** $f=\frac12 x^TQx-b^Tx$ ($Q\succ 0$): 一步到 $x^*=Q^{-1}b$.
- **局部二次收敛**: $\nabla f(x^*)=0$, $H(x^*)\succ 0$, 海森 $\rho$-Lipschitz, $x_0$ 足够近 $\Rightarrow$
  $$\|x_{k+1}-x^*\|\le C\|x_k-x^*\|^2,\quad C=\rho/(2\mu').$$
  证: 误差恒等式 + 梯度 FTC + 海森 Lipschitz + $H_k^{-1}$ 有界.
- 注: 局部; 每步算海森解线性系; 远处满步可能失败 → 线搜索全球化.

### 14. 线搜索

- **精确**: $\alpha=\arg\min_{\alpha\ge0} f(x_k+\alpha p_k)$; 二次型 + GD 方向 $\alpha=g^Tg/(g^TQg)$.
- **Armijo** ($c_A\in(0,1)$): $f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha\nabla f^T p_k$.
- **回溯**: 从 $\bar\alpha$ 起, 不满足 Armijo 则 $\alpha\leftarrow\eta\alpha$ ($\eta\in(0,1)$).
  - 有限终止: 可微 $\Rightarrow$ 充分小 $\alpha$ 必过 Armijo.
- **带回溯全局收敛** (Test1 scope 上限):
  - 假设: $f$ 有下界 + $L$-光滑; 方向一致条件 $\nabla f^T p_k\le -\sigma\|g_k\|^2$, $\|p_k\|\le\beta\|g_k\|$.
  - 步长下界: $\alpha_k\ge \min\{\bar\alpha,\frac{2\eta(1-c_A)\sigma}{L\beta^2}\}$.
  - 结论: $\min_{j<k}\|g_j\|^2\le \frac{f(x_0)-f^*}{c_A\sigma\alpha\cdot k}$, 且 $\|\nabla f(x_k)\|\to 0$.
  - 证: 下降引理给充分小步长必过 Armijo $\to$ 回溯接受下界 $\to$ Armijo+方向条件给每步下降 $\to$ 望远镜.

---

## 速记总表

| 假设 | GD $\alpha=1/L$ 保证 |
|---|---|
| 有下界 + $L$-光滑 | $\min_{j<k}\|\nabla f\|^2=O(1/k)$ |
| + 凸 | $f(x_k)-f^*=O(1/k)$ |
| + $\mu$-强凸 | $(1-\mu/L)^k$ 线性 |

| 方法 | 关键 |
|---|---|
| GD | $-\nabla f$ 最速; $\alpha<2/L$ 下降; $1/L$ 常用 |
| 牛顿 | 解 $Hp=-g$; 二次 1 步; 局部二次收敛 |
| Armijo 回溯 | 下降方向有限终止; 充分小步长必过 |

---

## 易错点

1. 驻点 $\ne$ 极小; 需二阶/凸性.
2. 小 $\|\nabla f\|$ alone 不保证最优 (非凸).
3. 步长过大发散; $L$ 未知用回溯.
4. 下降引理 $\int_0^1$ 是线段参数化, 不是换路径.
5. 牛顿满步远处可能失败; 用回溯全球化.
6. 病态 $\kappa\gg1$ 时 GD 沿平坦方向极慢.
7. 逻辑回归损失是 $\log(1+e^{-ya^Tx})$ (NLL), 非指数损失.
8. Weierstrass 需紧+连续, 缺一不可.
9. Lasso $\ell_1$ 在 $x_j=0$ 不可微 → 非光滑.
10. 强凸 $\Leftrightarrow$ $f-\frac\mu2\|x\|^2$ 凸.
