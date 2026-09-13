# Unconstrained Optimization: 无约束优化

- **来源**: `Lec/02-unconstrained-slides.pdf` (42 页)
- **课程**: MATH3900, Prof. Lexiao Lai, 2026–27 S1
- **说明**: 同主题另有 `Lec/handout/02-unconstrained-handout.pdf`; 本讲义按 42 页 slides 整理. Boyd 等 optional textbook **不**在此展开. 凡非定义公式均附 **证明** / **证明思路**.

---

## 本节在课程中的位置

承接导论中的逻辑回归 (logistic regression) 等无闭式解目标, 系统回答迭代法三问: **朝哪走 / 走多远 / 何时停**. 后续约束 / 非光滑 / 随机优化会复用此处的光滑与凸性语言.

---

## 1. 问题设定

$$
\min_{x\in\mathbb{R}^d} f(x),\quad f\text{ 可微}.
$$

(定义问题, 无需证明.)

例 (逻辑回归):
$$
f(x)=\frac1n\sum_{i=1}^n\log\bigl(1+e^{-y_i a_i^T x}\bigr).
$$

一般无闭式解 → 需迭代逼近.

---

## 2. 最优性条件 (optimality conditions)

### 驻点 (stationary point)

$\nabla f(x^\star)=0$ 时称 $x^\star$ 为驻点. (定义, 无需证明.)

**一阶必要条件 (first-order necessary condition)**: 若 $f$ 在 $x^\star$ 可微且 $x^\star$ 为局部极小点 (local minimizer), 则 $\nabla f(x^\star)=0$.

**证明思路**: 反证. 若 $g:=\nabla f(x^\star)\neq 0$, 取方向 $p=-g$, 则一阶展开
$$
f(x^\star+tp)=f(x^\star)+t g^Tp+o(t)=f(x^\star)-t\|g\|^2+o(t).
$$
对充分小 $t>0$ 有 $f(x^\star+tp)<f(x^\star)$, 与局部极小矛盾.

驻点**不必**是极小: $x^2$, $-x^2$, $x^3$ 在 $0$ 处导数皆为 $0$, 分别是局部极小 / 局部极大 / 拐点. 需看曲率 (curvature) → 海森矩阵 (Hessian).

### 正半定 (positive semidefinite) / 正定 (positive definite)

对称矩阵 $Q=Q^T$:

| 记号 | 含义 |
|---|---|
| $Q\succeq 0$ (PSD) | $\forall z$, $z^TQz\ge 0$ |
| $Q\succ 0$ (PD) | $\forall z\neq 0$, $z^TQz>0$ |
| $P\preceq Q$ | $Q-P\succeq 0$ |

(定义, 无需证明.)

对称矩阵正交对角化: $Q=U\Lambda U^T$, $U$ 正交, $\Lambda=\mathrm{diag}(\lambda_i)$.  
则 $\lambda_{\min}(Q)I\preceq Q\preceq\lambda_{\max}(Q)I$; $Q\succeq 0$ $\Leftrightarrow$ 全体特征值 $\ge 0$; $Q\succ 0$ $\Leftrightarrow$ 全体 $>0$.

**证明思路** (特征值刻画): 令 $z=Uy$, 则
$$
z^TQz=y^T\Lambda y=\sum_i\lambda_i y_i^2.
$$
故 $z^TQz\ge 0$ $\forall z$ $\Leftrightarrow$ 全体 $\lambda_i\ge 0$. 又
$$
\lambda_{\min}\|z\|^2=\lambda_{\min}\|y\|^2\le\sum\lambda_i y_i^2\le\lambda_{\max}\|y\|^2=\lambda_{\max}\|z\|^2,
$$
即 $\lambda_{\min}I\preceq Q\preceq\lambda_{\max}I$.

### 二阶最优性条件 (second-order optimality conditions)

设 $f$ 在 $x^\star$ 附近 $C^2$:

- **必要**: 局部极小 $\Rightarrow$ $\nabla f(x^\star)=0$ 且 $\nabla^2 f(x^\star)\succeq 0$
- **充分**: $\nabla f(x^\star)=0$ 且 $\nabla^2 f(x^\star)\succ 0$ $\Rightarrow$ 局部极小

**证明思路 (必要)**: 一阶已得 $\nabla f=0$. 若存在 $v$ 使 $v^T\nabla^2 f(x^\star)v<0$, 沿 $x^\star+tv$ 的二阶展开
$$
f(x^\star+tv)=f(x^\star)+\tfrac{t^2}{2}v^T\nabla^2 f(x^\star)v+o(t^2)
$$
对小 $t$ 小于 $f(x^\star)$, 矛盾. 故 Hessian 必 PSD.

**证明思路 (充分)**: $\nabla^2 f(x^\star)\succ 0$ $\Rightarrow$ 在 $x^\star$ 附近 $\nabla^2 f\succeq \mu I$ ($\mu>0$). 由 Taylor (带积分余项) 对小 $\|h\|$,
$$
f(x^\star+h)\ge f(x^\star)+\tfrac\mu4\|h\|^2>f(x^\star)\quad(h\neq 0),
$$
故为严格局部极小.

---

## 3. 下降方向与梯度下降 (gradient descent)

### 最速下降

一阶展开: $f(x_k+tp)=f(x_k)+t\nabla f(x_k)^Tp+o(t)$.  
若 $\nabla f(x_k)^Tp<0$, 则 $p$ 为**下降方向 (descent direction)**. (由 $o(t)/t\to 0$ 直接得到.)

由柯西–施瓦茨不等式 (Cauchy–Schwarz): 单位球上 $\nabla f^Tp$ 的最小值为 $-\|\nabla f\|$, 在
$$
p_k=-\frac{\nabla f(x_k)}{\|\nabla f(x_k)\|}
$$
达到 → $-\nabla f(x_k)$ 为**最速下降方向 (steepest descent direction)**.

**证明**: 对 $\|p\|=1$, $|\nabla f^Tp|\le\|\nabla f\|\|p\|=\|\nabla f\|$, 故 $\nabla f^Tp\ge-\|\nabla f\|$, 等号当且仅当 $p$ 与 $-\nabla f$ 同向.

### 算法

$$
x_{k+1}=x_k-\alpha_k\nabla f(x_k),\quad
\text{若 }\|\nabla f(x_k)\|\le\varepsilon\text{ 则停}.
$$

(算法定义, 无需证明.)

方向由梯度定, **步长 (step size)** $\alpha_k$ 定走多远.  
反例: $f(x)=\tfrac12 x^2$ 时 $x_{k+1}=(1-\alpha)x_k$; $\alpha\in(0,2)$ 收敛, $\alpha=2$ 振荡, $\alpha>2$ 发散.

**证明**: $f'(x)=x$, 故 $x_{k+1}=x_k-\alpha x_k=(1-\alpha)x_k$. 于是 $x_k=(1-\alpha)^k x_0$.  
$|1-\alpha|<1$ $\Leftrightarrow$ $\alpha\in(0,2)$ 时 $x_k\to 0$; $\alpha=2$ 时 $x_k=(-1)^k x_0$; $\alpha>2$ 时 $|1-\alpha|>1$ 发散.

---

## 4. $L$-光滑 (L-smooth) 与下降引理 (descent lemma)

映射 $G$ **$L$-利普希茨 (L-Lipschitz)**: $\|G(u)-G(v)\|\le L\|u-v\|$.  
$f$ **$L$-光滑**: $\nabla f$ 为 $L$-Lipschitz. (定义, 无需证明.)

**下降引理**: 若 $f$ 为 $L$-光滑, 则
$$
f(v)\le f(u)+\nabla f(u)^T(v-u)+\frac L2\|v-u\|^2.
$$

**证明** (FTC 沿线段 + 梯度 Lipschitz):

令 $x(t)=u+t(v-u)$ ($t:0\to 1$, 即从 $u$ 到 $v$ 的直线), $g(t)=f(x(t))$. 一维微积分基本定理 + 链式法则:
$$
f(v)-f(u)=g(1)-g(0)=\int_0^1 g'(t)\,dt
=\int_0^1 \nabla f(x(t))^T(v-u)\,dt.
$$
(这里 $\int_0^1$ 是路径参数化, **不是**换成别的路径; 因子 $v-u=x'(t)$.)

拆成一阶项 + 梯度变化:
$$
f(v)-f(u)
=\nabla f(u)^T(v-u)
+\int_0^1\Bigl(\nabla f(x(t))-\nabla f(u)\Bigr)^T(v-u)\,dt.
$$

Cauchy–Schwarz + Lipschitz:
$$
\Bigl|\bigl(\nabla f(x(t))-\nabla f(u)\bigr)^T(v-u)\Bigr|
\le L\|x(t)-u\|\,\|v-u\|=Lt\|v-u\|^2.
$$

从而
$$
\int_0^1\cdots\,dt\le\int_0^1 Lt\|v-u\|^2\,dt=\frac L2\|v-u\|^2,
$$
即得下降引理.

(对称下界: 对上式换 $u\leftrightarrow v$ 或取余项另一侧符号, 得 $f(v)\ge f(u)+\nabla f(u)^T(v-u)-\frac L2\|v-u\|^2$.)

**推论**: $0<\alpha<2/L$ 时 GD 可保证下降; 常取 $\alpha=1/L$, 得
$$
f(x_{k+1})\le f(x_k)-\frac1{2L}\|\nabla f(x_k)\|^2.
$$

**证明**: 令 $u=x_k$, $v=x_k-\alpha\nabla f(x_k)$, $g=\nabla f(x_k)$. 下降引理:
$$
f(x_{k+1})\le f(x_k)-\alpha\|g\|^2+\frac{L\alpha^2}{2}\|g\|^2
=f(x_k)-\alpha\Bigl(1-\frac{L\alpha}{2}\Bigr)\|g\|^2.
$$
当 $0<\alpha<2/L$ 时括号为正 → 严格下降 (若 $g\neq 0$). 取 $\alpha=1/L$:
$$
f(x_{k+1})\le f(x_k)-\frac1{2L}\|g\|^2.
$$

### 仅 $L$-光滑 + 有下界时的收敛

$\alpha_k=1/L$ 时, 对任意 $k\ge 1$:
$$
\min_{0\le j<k}\|\nabla f(x_j)\|^2\le\frac{2L\bigl(f(x_0)-f^\star\bigr)}{k},\quad f^\star:=\inf f.
$$

**证明** (逐步展开):

**Step 1 (单步下降)**. 由上节推论, $\alpha=1/L$ 时对每个 $j\ge 0$,
$$
f(x_{j+1})\le f(x_j)-\frac1{2L}\|\nabla f(x_j)\|^2.
$$
移项得「函数值下降量下界」:
$$
\frac1{2L}\|\nabla f(x_j)\|^2\le f(x_j)-f(x_{j+1}).
$$

**Step 2 (求和 / 望远镜)**. 对 $j=0,1,\ldots,k-1$ 把上式相加:
$$
\begin{align*}
\sum_{j=0}^{k-1}\frac1{2L}\|\nabla f(x_j)\|^2
&\le\sum_{j=0}^{k-1}\bigl(f(x_j)-f(x_{j+1})\bigr)\\
&=f(x_0)-f(x_1)+f(x_1)-f(x_2)+\cdots+f(x_{k-1})-f(x_k)\\
&=f(x_0)-f(x_k).
\end{align*}
$$
中间项全部抵消 (望远镜求和).

**Step 3 (用下界 $f^\star$)**. 因 $f^\star:=\inf f\le f(x_k)$, 有
$$
f(x_0)-f(x_k)\le f(x_0)-f^\star.
$$
故
$$
\sum_{j=0}^{k-1}\frac1{2L}\|\nabla f(x_j)\|^2\le f(x_0)-f^\star.
$$

**Step 4 (用最小值下界求和)**. 和式中每一项 $\ge$ 其中最小的那一项, 共 $k$ 项:
$$
\sum_{j=0}^{k-1}\|\nabla f(x_j)\|^2
\ge k\cdot\min_{0\le j<k}\|\nabla f(x_j)\|^2.
$$
因此
$$
\frac1{2L}\cdot k\cdot\min_{0\le j<k}\|\nabla f(x_j)\|^2
\le\sum_{j=0}^{k-1}\frac1{2L}\|\nabla f(x_j)\|^2
\le f(x_0)-f^\star.
$$

**Step 5 (整理)**. 两边乘 $2L/k$:
$$
\min_{0\le j<k}\|\nabla f(x_j)\|^2
\le\frac{2L\bigl(f(x_0)-f^\star\bigr)}{k}.
$$
即得结论. 特别地, 右边 $=O(1/k)$, 所以前 $k$ 步里**梯度范数最小的那一次**以 $O(1/k)$ 变小.

**备注**: 该界只保证存在某次迭代梯度小, **不**保证 $x_k$ 本身是局部/全局极小 (非凸时小梯度可能是鞍点). 也不保证 $\|\nabla f(x_k)\|$ 本身单调下降.

---

## 5. 凸性 (convexity)

### 凸集 / 凸函数

- 凸集: $u,v\in C$, $\theta\in[0,1]$ $\Rightarrow$ $\theta u+(1-\theta)v\in C$
- 凸函数: $f(\theta u+(1-\theta)v)\le\theta f(u)+(1-\theta)f(v)$

(定义, 无需证明. 图在弦下方 $\Leftrightarrow$ 上境图 (epigraph) 凸.)

**保持凸性**: 非负线性组合; 仿射复合 $x\mapsto g(Mx+q)$; 逐点最大 $\max_i f_i$.

**证明思路**: 直接代入定义验证 (仿射复合: 弦的像仍是弦; 逐点最大: 每条弦上界仍被最大值压住).

### 一阶刻画

$f$ 可微凸 $\Leftrightarrow$ $f(v)\ge f(u)+\nabla f(u)^T(v-u)$ (切平面是**全局下界**).

**证明思路 ($\Rightarrow$)**: 凸性给出
$$
f(u+t(v-u))\le (1-t)f(u)+tf(v).
$$
移项除以 $t>0$, 令 $t\to 0^+$ 得 $\nabla f(u)^T(v-u)\le f(v)-f(u)$.

**证明思路 ($\Leftarrow$)**: 切平面下界对 $u_\theta=\theta u+(1-\theta)v$ 写两次, 加权相加即得凸性不等式.

**推论**: 可微凸时, $x^\star$ 全局极小 $\Leftrightarrow$ $\nabla f(x^\star)=0$.

**证明**: $(\Rightarrow)$ 局部极小的一阶必要. $(\Leftarrow)$ 切平面下界: $f(v)\ge f(x^\star)+\nabla f(x^\star)^T(v-x^\star)=f(x^\star)$.

### 二阶刻画 (海森检验)

$C^2$ 时: $f$ 在开凸集上凸 $\Leftrightarrow$ $\forall x$, $\nabla^2 f(x)\succeq 0$.

**预备 — 梯度单调**: 由一阶刻画, 凸 $\Rightarrow$
$$
\bigl(\nabla f(v)-\nabla f(u)\bigr)^T(v-u)\ge 0\quad(\forall u,v).
$$
**证明**: 写两次切平面下界并交换 $u,v$:
$$
f(v)\ge f(u)+\nabla f(u)^T(v-u),\qquad
f(u)\ge f(v)+\nabla f(v)^T(u-v).
$$
相加即得上式.

**证明 ($\Rightarrow$)**: 凸 $\Rightarrow$ $\nabla^2 f\succeq 0$.  
任取 $x$ 与方向 $d$. 对充分小 $t\neq 0$, 取 $u=x$, $v=x+td$. 由梯度单调:
$$
d^T\Bigl(\frac{\nabla f(x+td)-\nabla f(x)}{t}\Bigr)\ge 0.
$$
令 $t\to 0$. 因 $f\in C^2$, 左边 $\to d^T\nabla^2 f(x)\,d$. 故对一切 $d$ 有 $d^T\nabla^2 f(x)\,d\ge 0$, 即 $\nabla^2 f(x)\succeq 0$.

**证明 ($\Leftarrow$)**: $\nabla^2 f\succeq 0$ $\Rightarrow$ 凸.  
固定 $u,v$, 令 $g(t)=f(u+t(v-u))$, $t\in[0,1]$. 则
$$
g'(t)=\nabla f(u+t(v-u))^T(v-u),\qquad
g''(t)=(v-u)^T\nabla^2 f(u+t(v-u))(v-u).
$$
海森 PSD $\Rightarrow$ $g''(t)\ge 0$ $\Rightarrow$ $g'$ 递增, 故 $g'(t)\ge g'(0)=\nabla f(u)^T(v-u)$. 积分得
$$
f(v)-f(u)=g(1)-g(0)=\int_0^1 g'(t)\,dt\ge\nabla f(u)^T(v-u),
$$
即一阶刻画, 故 $f$ 凸.

**等价写法 (积分余项)**:
$$
f(v)=f(u)+\nabla f(u)^T(v-u)
+\int_0^1(1-t)(v-u)^T\nabla^2 f\bigl(u+t(v-u)\bigr)(v-u)\,dt.
$$
若 $\nabla^2 f\succeq 0$, 积分项 $\ge 0$, 立刻得切平面下界 $\Rightarrow$ 凸.

二次型 $f(x)=\tfrac12 x^TQx-b^Tx$ 凸 $\Leftrightarrow$ $Q\succeq 0$.

**证明**: $\nabla^2 f=Q$ 为常数, 由上等价于 $Q\succeq 0$.

### 逻辑回归目标凸

单样本 $\ell_i(x)=\log(1+e^{-y_i a_i^T x})$, $w_i=1/(1+e^{y_i a_i^T x})$:
$$
\nabla\ell_i=-y_i w_i a_i,\quad
\nabla^2\ell_i=w_i(1-w_i)a_ia_i^T\succeq 0
$$
(因 $w_i(1-w_i)\ge 0$). 平均后 $\nabla^2 F\succeq 0$ → $F$ 凸.

**证明思路**: 令 $z=-y_i a_i^T x$, $\ell=\log(1+e^z)$. 则 $\ell'=e^z/(1+e^z)$, $\ell''=e^z/(1+e^z)^2\in(0,1/4]$. 链式法则给出上述梯度/海森; $w_i(1-w_i)a_ia_i^T$ 为 PSD 秩一型.

### 凸 + $L$-光滑上的 GD

$\alpha_k=1/L$ 时:
$$
f(x_k)-f(x^\star)\le\frac{L\|x_0-x^\star\|^2}{2k}=O(k^{-1}).
$$

**证明思路**: 下降引理 + 凸性切平面下界 $\Rightarrow$ 一步有
$$
f(x_{k+1})-f(x^\star)\le\frac L2\bigl(\|x_k-x^\star\|^2-\|x_{k+1}-x^\star\|^2\bigr)
$$
(标准「距离平方望远镜」论证). 对 $0..k-1$ 求和并取平均 / 用单调性得到 $O(1/k)$.

目标间隙 $\le\delta$ 需 $O(1/\delta)$ 步. 平坦极小附近海森退化时 GD 变慢.

---

## 6. 强凸 (strong convexity) 与条件数 (condition number)

$f$ **$\mu$-强凸** ($\mu>0$):
$$
f(v)\ge f(u)+\nabla f(u)^T(v-u)+\frac\mu2\|v-u\|^2.
$$
(定义, 无需证明. 比凸性多一个二次下界.)

$C^2$ 时: $\mu$-强凸且 $L$-光滑 $\Leftrightarrow$ $\mu I\preceq\nabla^2 f(x)\preceq LI$ $\forall x$.  
**条件数** $\kappa:=L/\mu\ge 1$.

**证明思路**: 强凸 $\Leftrightarrow$ $f(x)-\frac\mu2\|x\|^2$ 凸 $\Leftrightarrow$ 海森 $\succeq\mu I$; $L$-光滑类似给出上界 $LI$ (或由下降引理的二次上界与海森联系).

### 强凸上的 GD (线性收敛)

$\alpha_k=1/L$:
$$
f(x_k)-f(x^\star)\le\Bigl(1-\frac\mu L\Bigr)^k\bigl(f(x_0)-f(x^\star)\bigr).
$$

**证明思路**: 强凸给出 $f(x)-f(x^\star)\le\frac1{2\mu}\|\nabla f(x)\|^2$ (对 $v=x^\star$ 极小化二次下界). 代入一步下降
$$
f(x_{k+1})-f^\star\le f(x_k)-f^\star-\frac1{2L}\|\nabla f\|^2
\le\Bigl(1-\frac\mu L\Bigr)\bigl(f(x_k)-f^\star\bigr).
$$
归纳即得. 缩间隙因子 $\delta$ 约需 $O(\kappa\log(1/\delta))$ 步.

对角二次型上各坐标以 $1-\alpha\lambda_i$ 收缩; $\alpha=1/L$ 时最慢方向因子为 $1-\mu/L$.

---

## 7. 牛顿法 (Newton's method)

一阶模型给出 GD 方向; 二阶模型
$$
m_k^{(2)}(p)=f(x_k)+\nabla f(x_k)^Tp+\tfrac12 p^T\nabla^2 f(x_k)p
$$
匹配曲率. 记 $H_k:=\nabla^2 f(x_k)$ (第 $k$ 步海森; 在对 $p$ 求导时视为常矩阵). 令 $\nabla_p m_k^{(2)}=0$:
$$
H_k\,p_k=-\nabla f(x_k),\quad x_{k+1}=x_k+p_k.
$$

**证明 (牛顿步公式)**: 对 $p$ 求导时 $f(x_k)$、$\nabla f(x_k)$、$H_k$ 皆为常数:
$$
\nabla_p\bigl[f(x_k)\bigr]=0,\quad
\nabla_p\bigl[\nabla f(x_k)^Tp\bigr]=\nabla f(x_k),\quad
\nabla_p\bigl[\tfrac12 p^TH_kp\bigr]=H_kp
$$
(最后一步用 $H_k$ 对称: $\nabla(\tfrac12 p^THp)=\tfrac12(H+H^T)p=Hp$). 故
$$
\nabla_p m_k^{(2)}(p)=\nabla f(x_k)+H_kp.
$$
令其为 $0$ 即得 $H_kp_k=-\nabla f(x_k)$.  

若 $H_k\succ 0$, 则 $m_k^{(2)}$ 为严格凸二次函数, 上述临界点是其**唯一全局极小**.  
(注: 模型截断在二阶, 已丢掉真函数的三阶余项 $R_3$; 求导时不会出现 $\nabla^3 f$, 因为 $H_k$ 不依赖 $p$.)

**二次目标** $f(x)=\tfrac12 x^TQx-b^Tx$ ($Q\succ 0$): 精确牛顿一步到达 $x^\star=Q^{-1}b$.

**证明**: $\nabla f(x)=Qx-b$, $\nabla^2 f(x)=Q$ (常数). 从任意 $x_0$ 取牛顿步:
$$
Qp_0=-(Qx_0-b)\quad\Rightarrow\quad p_0=-x_0+Q^{-1}b.
$$
故 $x_1=x_0+p_0=Q^{-1}b=x^\star$. (真函数本身就是二次, 模型无截断误差.)

### 局部二次收敛

矩阵 2-范数: $\|A\|=\max_{\|z\|=1}\|Az\|$; $A$ 对称时 $\|A\|=\max_i|\lambda_i(A)|$. (定义/标准事实.)  
海森 **$\rho$-Lipschitz**: $\|\nabla^2 f(u)-\nabla^2 f(v)\|\le\rho\|u-v\|$.

若 $\nabla f(x^\star)=0$, $\nabla^2 f(x^\star)\succ 0$, 海森在 $x^\star$ 附近 $\rho$-Lipschitz, 且 $x_0$ 足够靠近, 则存在常数 $C$ 使
$$
\|x_{k+1}-x^\star\|\le C\|x_k-x^\star\|^2
$$
(**二次收敛 (quadratic convergence)**).

**证明** (逐步展开):

**Step 1 (误差恒等式)**. 满步牛顿 $x_{k+1}=x_k-H_k^{-1}\nabla f(x_k)$, 故
$$
x_{k+1}-x^\star
=x_k-x^\star-H_k^{-1}\nabla f(x_k)
=H_k^{-1}\Bigl(H_k(x_k-x^\star)-\nabla f(x_k)\Bigr).
$$

**Step 2 (梯度的积分表示)**. 因 $\nabla f(x^\star)=0$, 沿线段用 FTC:
$$
\nabla f(x_k)
=\nabla f(x_k)-\nabla f(x^\star)
=\int_0^1\nabla^2 f\bigl(x^\star+t(x_k-x^\star)\bigr)(x_k-x^\star)\,dt.
$$
记 $e_k:=x_k-x^\star$, $H(t):=\nabla^2 f(x^\star+te_k)$. 则
$$
H_k e_k-\nabla f(x_k)
=\int_0^1\bigl(H_k-H(t)\bigr)e_k\,dt.
$$

**Step 3 (Lipschitz 控制)**. $\|H_k-H(t)\|=\|\nabla^2 f(x_k)-\nabla^2 f(x^\star+te_k)\|\le\rho\|e_k-te_k\|=\rho(1-t)\|e_k\|$, 故
$$
\bigl\|H_k e_k-\nabla f(x_k)\bigr\|
\le\int_0^1\rho(1-t)\|e_k\|^2\,dt=\frac\rho2\|e_k\|^2.
$$

**Step 4 (海森可逆上界)**. $\nabla^2 f(x^\star)\succ 0$ $\Rightarrow$ 在足够小邻域内 $\lambda_{\min}(H_k)\ge\mu'>0$, 从而 $\|H_k^{-1}\|\le 1/\mu'$. 于是
$$
\|x_{k+1}-x^\star\|
=\bigl\|H_k^{-1}(H_ke_k-\nabla f(x_k))\bigr\|
\le\frac1{\mu'}\cdot\frac\rho2\|e_k\|^2
=\frac{\rho}{2\mu'}\|x_k-x^\star\|^2.
$$
取 $C=\rho/(2\mu')$ 即得二次收敛.  

**备注**: 保证是**局部**的 (需先进入该邻域); 每步要算海森并解线性系. 远处满步可能失败 → 用线搜索全球化 (§8).

---

## 8. 线搜索 (line search)

选定方向 $p_k$ 后: $x_{k+1}=x_k+\alpha_k p_k$. (定义.)

| 方法 | 常用 $\alpha$ | 局限 |
|---|---|---|
| GD | $1/L$ | 需全局 $L$; 可能过保守 |
| Newton | 满步 $1$ | 模型仅局部, 可能过冲 |

### 精确线搜索 (exact line search)

$\alpha_k^{\mathrm{exact}}\in\arg\min_{\alpha\ge 0}f(x_k+\alpha p_k)$.  
二次型 + GD 方向有闭式 $\alpha=g^Tg/(g^TQg)$.

**证明**: 设 $f(x)=\tfrac12 x^TQx$ ($Q\succ 0$), 在 $x$ 处 $g=\nabla f(x)=Qx$, 取 $p=-g$. 令
$$
\phi(\alpha)=f(x-\alpha g)=\tfrac12(x-\alpha g)^TQ(x-\alpha g).
$$
展开:
$$
\phi(\alpha)=\tfrac12 x^TQx-\alpha g^TQx+\tfrac{\alpha^2}{2}g^TQg
=f(x)-\alpha\|g\|^2+\tfrac{\alpha^2}{2}g^TQg
$$
(因 $g=Qx$). 求导:
$$
\phi'(\alpha)=-\|g\|^2+\alpha\,g^TQg.
$$
令 $\phi'(\alpha)=0$ 得 $\alpha^\star=\|g\|^2/(g^TQg)=g^Tg/(g^TQg)$. 又 $\phi''=g^TQg>0$ (若 $g\neq 0$), 故为极小.

### Armijo 条件 (充分下降)

$c_A\in(0,1)$; 可接受步长满足
$$
f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha\,\nabla f(x_k)^Tp_k.
$$
(接受准则定义, 无需证明. 右边是「线性模型下降」的 $c_A$ 折.)

### 回溯线搜索 (backtracking line search)

从试探 $\bar\alpha>0$ 起, 不满足 Armijo 则 $\alpha\leftarrow\eta\alpha$ ($\eta\in(0,1)$), 直到满足为止.

**证明 (有限终止)**: 设 $p_k$ 为下降方向, 即 $\nabla f(x_k)^Tp_k<0$. 由可微性,
$$
\lim_{\alpha\to 0^+}\frac{f(x_k+\alpha p_k)-f(x_k)}{\alpha}=\nabla f(x_k)^Tp_k.
$$
因 $c_A\in(0,1)$ 且 $\nabla f^Tp_k<0$, 有 $c_A\nabla f^Tp_k>\nabla f^Tp_k$ (两边同乘负数反号). 故存在 $\alpha_0>0$, 使一切 $\alpha\in(0,\alpha_0]$ 满足
$$
\frac{f(x_k+\alpha p_k)-f(x_k)}{\alpha}\le c_A\nabla f(x_k)^Tp_k,
$$
即 Armijo. 回溯每次乘 $\eta<1$, 至多有限步后落入 $(0,\alpha_0]$, 算法终止.

### 带回溯的全局收敛

若 $f$ 有下界且 $L$-光滑, 方向满足一致条件
$$
\nabla f(x_k)^Tp_k\le-\sigma\|\nabla f(x_k)\|^2,\qquad
\|p_k\|\le\beta\|\nabla f(x_k)\|
$$
($\sigma,\beta>0$), 则存在与 $k$ 无关的步长下界
$$
\alpha:=\min\Bigl\{\bar\alpha,\;\frac{2\eta(1-c_A)\sigma}{L\beta^2}\Bigr\},
$$
使得回溯接受的 $\alpha_k\ge\alpha$, 并且
$$
\min_{0\le j<k}\|\nabla f(x_j)\|^2\le\frac{f(x_0)-f^\star}{c_A\sigma\alpha\,k},\qquad
\|\nabla f(x_k)\|\to 0.
$$

**证明** (逐步展开):

**Step 1 (充分小步长必过 Armijo)**. 由下降引理, 对任意 $\alpha>0$,
$$
f(x_k+\alpha p_k)
\le f(x_k)+\alpha\nabla f^Tp_k+\frac{L\alpha^2}{2}\|p_k\|^2.
$$
若要推出 Armijo $f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha\nabla f^Tp_k$, 只需
$$
\alpha\nabla f^Tp_k+\frac{L\alpha^2}{2}\|p_k\|^2\le c_A\alpha\nabla f^Tp_k,
$$
即 (两边减 $c_A\alpha\nabla f^Tp_k$, 注意 $\nabla f^Tp_k<0$)
$$
(1-c_A)\alpha\nabla f^Tp_k+\frac{L\alpha^2}{2}\|p_k\|^2\le 0.
$$
用方向条件: $\nabla f^Tp_k\le-\sigma\|g_k\|^2$, $\|p_k\|\le\beta\|g_k\|$ ($g_k=\nabla f(x_k)$),
$$
-(1-c_A)\alpha\sigma\|g_k\|^2+\frac{L\alpha^2}{2}\beta^2\|g_k\|^2\le 0.
$$
当 $g_k\neq 0$ 时除以 $\|g_k\|^2>0$, 得只要
$$
0<\alpha\le\frac{2(1-c_A)\sigma}{L\beta^2}
$$
则下降引理上界已蕴含 Armijo.  

**Step 2 (回溯接受步长有下界)**. 回溯从 $\bar\alpha$ 几何缩小. 一旦某候选 $\alpha$ 落入 $\bigl(0,\frac{2(1-c_A)\sigma}{L\beta^2}\bigr]$, Armijo 成立. 因每次乘 $\eta$, 最终接受的 $\alpha_k$ 满足
$$
\alpha_k\ge\min\Bigl\{\bar\alpha,\;\eta\cdot\frac{2(1-c_A)\sigma}{L\beta^2}\Bigr\}=\alpha
$$
(标准 backtracking 下界论证: 若 $\bar\alpha$ 已合格则 $\alpha_k=\bar\alpha$; 否则最后一个不合格步长 $>\frac{2(1-c_A)\sigma}{L\beta^2}$, 再乘 $\eta$ 后仍 $\ge\eta\cdot\frac{2(1-c_A)\sigma}{L\beta^2}$).

**Step 3 (每步函数下降)**. Armijo + 方向条件:
$$
f(x_k)-f(x_{k+1})
\ge -c_A\alpha_k\nabla f^Tp_k
\ge c_A\alpha_k\sigma\|g_k\|^2
\ge c_A\alpha\sigma\|g_k\|^2.
$$

**Step 4 (望远镜)**. 对 $j=0,\ldots,k-1$ 求和:
$$
\sum_{j=0}^{k-1}\|g_j\|^2
\le\frac{f(x_0)-f(x_k)}{c_A\alpha\sigma}
\le\frac{f(x_0)-f^\star}{c_A\alpha\sigma}.
$$
左边 $\ge k\min_{j<k}\|g_j\|^2$, 即得 $\min\|\nabla f\|^2=O(1/k)$. 又部分和有界 $\Rightarrow\|g_k\|^2\to 0$ 的某一子列, 再结合标准论证 (或直接由 $\sum\|g_j\|^2<\infty$) 得 $\|\nabla f(x_k)\|\to 0$.

### 牛顿 + 回溯

若 $f\in C^2$ 且 $\mu$-强凸、$L$-光滑, 则从任意 $x_0$, 牛顿方向 + 回溯有 $x_k\to x^\star$.  
若 $\bar\alpha=1$, $c_A<1/2$, 且海森局部 Lipschitz, 则最终接受满步 $\alpha_k=1$ 并恢复二次收敛.

**证明** (逐步展开):

**Step 1 (牛顿方向满足一致下降条件)**. $\mu$-强凸 + $L$-光滑 $\Rightarrow$ $\mu I\preceq H_k\preceq LI$, 故 $\|H_k^{-1}\|\le 1/\mu$. 牛顿方向 $p_k=-H_k^{-1}g_k$ 满足
$$
\nabla f^Tp_k=-g_k^TH_k^{-1}g_k\le-\frac1L\|g_k\|^2
$$
(因 $H_k^{-1}\succeq\tfrac1L I$), 以及
$$
\|p_k\|\le\|H_k^{-1}\|\,\|g_k\|\le\frac1\mu\|g_k\|.
$$
故可取 $\sigma=1/L$, $\beta=1/\mu$.

**Step 2 (全局到驻点)**. 上一段带回溯的全局收敛适用 $\Rightarrow\|\nabla f(x_k)\|\to 0$. 强凸时驻点唯一且为全局极小 $x^\star$, 且 $\|\nabla f(x)\|\ge\mu\|x-x^\star\|$ 一类不等式给出 $x_k\to x^\star$.

**Step 3 (靠近后满步可接受)**. 在 $x^\star$ 附近, 由局部二次收敛分析: 满步牛顿的函数下降与模型预测可比. 当 $c_A<1/2$ 且 $x_k$ 足够近时, 可验证 $\alpha=1$ 满足 Armijo (标准结果: 二次模型在邻域内足够准确, 真实下降至少是线性预测的一半以上). 于是回溯直接接受 $\bar\alpha=1$.

**Step 4 (恢复二次率)**. 一旦始终取满步, §7 的局部二次收敛定理适用.

---

## 9. 速记表

### 梯度下降 ($\alpha=1/L$)

| 假设 | 保证 |
|---|---|
| 有下界 + $L$-光滑 | $\min_{j<k}\|\nabla f(x_j)\|^2=O(1/k)$ |
| 再 + 凸 | $f(x_k)-f^\star=O(1/k)$ |
| 再 + $\mu$-强凸 | $(1-\mu/L)^k$ 线性收敛 |

(证明见 §4–§6.)

### 牛顿与线搜索

- 正定二次型: 满步牛顿 **1 步**到解 (§7)
- 局部: 海森 PD + Lipschitz → 二次收敛 (§7)
- Armijo 回溯: 下降方向下有限终止 (§8)
- 强凸 + 光滑: 牛顿+回溯 **全局**收敛; 靠近后常恢复满步二次率 (§8)

---

## 易错点

1. 驻点 $\neq$ 极小; 需二阶 / 凸性
2. 小 $\|\nabla f\|$ alone 不保证最优 (非凸时)
3. 步长过大则发散; $L$ 未知时用回溯比盲目 $1/L$ 更稳
4. 精确线搜索短期最优 $\neq$ 长期最优
5. 牛顿满步在远处可能失败 — 用回溯全球化
6. 病态 $\kappa\gg 1$ 时 GD 沿平坦方向极慢
7. 下降引理里的 $\int_0^1$ 是**从 $u$ 到 $v$ 的线段参数化**, 不是换路径

## 与前后章

- 前: 导论中的 logistic / 梯度与 Taylor
- 后: 约束优化 (可行方向 / KKT); 非光滑 (次梯度 / proximal); 随机 (SGD)
