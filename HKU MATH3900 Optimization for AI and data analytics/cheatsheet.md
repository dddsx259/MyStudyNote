# MATH3900 Cheatsheet

> 词条/公式/定理速查; 对话中学到的内容会增量追加.
> 约定: **定义 / 定理 / 推论 / 命题** 一律写清 **假设** 与 **结论**; 证明见对应讲义.

---

## 名词 (定义)

+ **Optimization problem** / **优化问题**:
    + **形式**: $\min_{x\in C} f(x)$ (最大化: $\max f=\min(-f)$)
    + **决策变量 (decision variable)** $x$: $x\in\mathbb{R}^d$
    + **目标函数 (objective)** $f$: $f:\mathbb{R}^d\to\mathbb{R}$
    + **可行域 (feasible set)** $C$: $C\subseteq\mathbb{R}^d$; $x\in C$ 可行
    + **无约束**: $C=\mathbb{R}^d$

+ **Global / local minimizer** / **全局/局部极小点**:
    + **全局**: $f(x^\star)\le f(x)$ 对一切 $x\in C$
    + **局部**: 存在邻域 $N$, 使 $f(x^\star)\le f(x)$ 对一切 $x\in C\cap N$
    + **$\arg\min$**: 全体全局极小点的集合
    + **最优值** $f^\star:=\inf_{x\in C}f(x)$ (未必被某可行点达到)

+ **Compact set** / **紧集** ($\mathbb{R}^d$, Heine–Borel):
    + **定义**: 闭且有界 (closed and bounded)
    + **有界**: $\exists M$, $\|x\|\le M\ \forall x\in C$
    + **闭**: 含全部极限点

+ **Directional derivative / gradient / Hessian** / **方向导数/梯度/海森**:
    + **方向导数**: $f'(x;v)=\lim_{t\downarrow 0}\bigl(f(x+tv)-f(x)\bigr)/t$
    + **可微时**: $f'(x;v)=\nabla f(x)^Tv$
    + **海森**: $\nabla^2 f(x)$ (二阶偏导矩阵; $C^2$ 时对称)

+ **Stationary point** / **驻点**:
    + **假设**: $f$ 在 $x^\star$ 可微
    + **定义**: $\nabla f(x^\star)=0$
    + **注**: 局部极小 $\Rightarrow$ 驻点; 驻点不必是极小

+ **PSD / PD / Loewner order** / **正半定/正定/Löwner 序**:
    + **假设**: $Q=Q^T$
    + **$Q\succeq 0$ (PSD)**: $\forall z$, $z^TQz\ge 0$ ($\Leftrightarrow$ 全体特征值 $\ge 0$)
    + **$Q\succ 0$ (PD)**: $\forall z\neq 0$, $z^TQz>0$ ($\Leftrightarrow$ 全体特征值 $>0$)
    + **$P\preceq Q$**: $Q-P\succeq 0$
    + **事实**: $\lambda_{\min}(Q)I\preceq Q\preceq\lambda_{\max}(Q)I$

+ **Descent / steepest descent direction** / **下降/最速下降方向**:
    + **下降方向**: $\nabla f(x_k)^Tp_k<0$ (充分小步长下 $f$ 下降)
    + **最速下降** (单位球上): $p=-\nabla f/\|\nabla f\|$; 常用方向取 $-\nabla f$

+ **L-Lipschitz / L-smooth** / **$L$-利普希茨/$L$-光滑**:
    + **映射 $G$ 为 $L$-Lipschitz**: $\|G(u)-G(v)\|\le L\|u-v\|$
    + **$f$ 为 $L$-光滑**: $\nabla f$ 为 $L$-Lipschitz

+ **Convex set / convex function** / **凸集/凸函数**:
    + **凸集**: $u,v\in C$, $\theta\in[0,1]$ $\Rightarrow$ $\theta u+(1-\theta)v\in C$
    + **凸函数**: $f(\theta u+(1-\theta)v)\le\theta f(u)+(1-\theta)f(v)$
    + **保持凸性**: 非负线性组合; 仿射复合 $x\mapsto g(Mx+q)$; 逐点最大

+ **Strong convexity / condition number** / **强凸/条件数**:
    + **$\mu$-强凸** ($\mu>0$): $f(v)\ge f(u)+\nabla f(u)^T(v-u)+\frac\mu2\|v-u\|^2$
    + **条件数**: 若同时 $L$-光滑, $\kappa:=L/\mu\ge 1$

+ **Hessian $\rho$-Lipschitz** / **海森 $\rho$-利普希茨**:
    + $\|\nabla^2 f(u)-\nabla^2 f(v)\|\le\rho\|u-v\|$ (矩阵 2-范数)

+ **Line search / Armijo / backtracking** / **线搜索/Armijo/回溯**:
    + **线搜索**: 选定方向 $p_k$ 后取 $x_{k+1}=x_k+\alpha_k p_k$ (精确或非精确)
    + **Armijo**: 固定 $c_A\in(0,1)$, 要求 $f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha\nabla f(x_k)^Tp_k$
    + **回溯**: 从 $\bar\alpha$ 起不满足则 $\alpha\leftarrow\eta\alpha$ ($\eta\in(0,1)$)

---

## 公式 / 算法

+ **典型模型**:
    + 线性回归: $\min_x\frac1{2n}\|Ax-y\|^2$
    + 逻辑回归: $\min_x\frac1n\sum_i\log(1+e^{-y_ia_i^Tx})$
    + 硬间隔 SVM: $\min_x\frac12\|x\|^2$ s.t. $y_ia_i^Tx\ge 1$
    + Lasso: $\min_x\frac1{2n}\|Ax-y\|^2+\lambda\|x\|_1$

+ **Chain rule** / **链式法则**:
    + **假设**: $F=g\circ h$, $h:\mathbb{R}^d\to\mathbb{R}^m$ 可微, $g$ 可微
    + **结论**: $\nabla F(x)=J_h(x)^T\nabla g(h(x))$

+ **Linear regression gradient**:
    + **假设**: $F(x)=\frac1{2n}\|Ax-y\|^2$
    + **结论**: $\nabla F(x)=\frac1n A^T(Ax-y)$; 满秩时正规方程 $x^\star=(A^TA)^{-1}A^Ty$

+ **FTC along a segment** / **沿线段的 FTC**:
    + **假设**: $f$ 可微
    + **结论**: $f(v)-f(u)=\int_0^1\nabla f\bigl(u+t(v-u)\bigr)^T(v-u)\,dt$

+ **Taylor**:
    + 一阶 (可微): $f(x+s)=f(x)+\nabla f(x)^Ts+o(\|s\|)$
    + 二阶 ($C^2$): $f(x+s)=f(x)+\nabla f(x)^Ts+\frac12 s^T\nabla^2 f(x)s+o(\|s\|^2)$

+ **Quadratic form gradient** / **二次型梯度**:
    + **一般 $A$**: $\nabla_x(x^TAx)=(A+A^T)x$
    + **$A$ 对称**: $\nabla_x(x^TAx)=2Ax$; 故 $\nabla(\tfrac12 x^THx)=Hx$

+ **Gradient descent (GD)**:
    + $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$; 常取 $\alpha=1/L$; 停机如 $\|\nabla f\|\le\varepsilon$

+ **Newton step**:
    + 二阶模型 $m_k^{(2)}(p)=f(x_k)+\nabla f^Tp+\frac12 p^TH_kp$, $H_k=\nabla^2 f(x_k)$
    + 令 $\nabla_p m=0$: $H_kp_k=-\nabla f(x_k)$; 满步 $x_{k+1}=x_k+p_k$

+ **Exact line search (quadratic + GD direction)**:
    + **假设**: $f(x)=\tfrac12 x^TQx$ ($Q\succ 0$) 或一般正定二次型; $g=\nabla f(x)$, $p=-g$
    + **结论**: $\alpha^\star=g^Tg/(g^TQg)$

---

## 定理 / 推论 / 命题

### Lec01: 存在性与基础

+ **Weierstrass theorem** / **魏尔斯特拉斯定理**:
    + **假设**: $C\subseteq\mathbb{R}^d$ 非空紧; $f$ 在 $C$ 上连续
    + **结论**: 存在全局极小点 $x^\star\in C$

### Lec02: 最优性条件

+ **FOC (first-order necessary)** / **一阶必要条件**:
    + **假设**: $f$ 在 $x^\star$ 可微; $x^\star$ 为局部极小点
    + **结论**: $\nabla f(x^\star)=0$

+ **SOC necessary** / **二阶必要条件**:
    + **假设**: $f$ 在 $x^\star$ 附近 $C^2$; $x^\star$ 为局部极小
    + **结论**: $\nabla f(x^\star)=0$ 且 $\nabla^2 f(x^\star)\succeq 0$

+ **SOC sufficient** / **二阶充分条件**:
    + **假设**: $f$ 在 $x^\star$ 附近 $C^2$; $\nabla f(x^\star)=0$ 且 $\nabla^2 f(x^\star)\succ 0$
    + **结论**: $x^\star$ 为严格局部极小

+ **Steepest descent on unit sphere** / **单位球上最速下降**:
    + **假设**: $\nabla f(x_k)\neq 0$; 在 $\|p\|=1$ 上极小化 $\nabla f^Tp$
    + **结论**: 最小值 $-\|\nabla f\|$, 在 $p=-\nabla f/\|\nabla f\|$ 达到

+ **1D GD step-size (toy)** / **一维 GD 步长反例**:
    + **假设**: $f(x)=\tfrac12 x^2$; $x_{k+1}=x_k-\alpha f'(x_k)$
    + **结论**: $\alpha\in(0,2)$ 收敛; $\alpha=2$ 振荡; $\alpha>2$ 发散

### 光滑与 GD 速率

+ **Descent lemma** / **下降引理**:
    + **假设**: $f$ 为 $L$-光滑
    + **结论**: $f(v)\le f(u)+\nabla f(u)^T(v-u)+\frac L2\|v-u\|^2$
    + **对称下界**: $f(v)\ge f(u)+\nabla f(u)^T(v-u)-\frac L2\|v-u\|^2$

+ **Corollary (GD decrease)** / **推论 (GD 下降)**:
    + **假设**: $f$ 为 $L$-光滑; $x_{k+1}=x_k-\alpha\nabla f(x_k)$; $0<\alpha<2/L$
    + **结论**: $f(x_{k+1})\le f(x_k)-\alpha\bigl(1-\frac{L\alpha}{2}\bigr)\|\nabla f(x_k)\|^2$; 特别 $\alpha=1/L$ 时下降至少 $\frac1{2L}\|\nabla f\|^2$

+ **GD rate: smooth + bounded below** / **仅光滑有下界**:
    + **假设**: $f$ 为 $L$-光滑; $f^\star:=\inf f>-\infty$; $\alpha_k=1/L$
    + **结论**: $\min_{0\le j<k}\|\nabla f(x_j)\|^2\le\frac{2L(f(x_0)-f^\star)}{k}=O(1/k)$
    + **注**: 非凸时不保证 $x_k$ 是极小 (可能鞍点)

### 凸性刻画与凸 GD

+ **First-order characterization of convexity** / **凸性一阶刻画**:
    + **假设**: $f$ 可微; 定义域为开凸集
    + **结论**: $f$ 凸 $\Leftrightarrow$ $f(v)\ge f(u)+\nabla f(u)^T(v-u)$ $\forall u,v$
    + **附**: 凸 $\Rightarrow$ $(\nabla f(v)-\nabla f(u))^T(v-u)\ge 0$ (梯度单调)

+ **Corollary (convex stationary = global min)** / **推论**:
    + **假设**: $f$ 可微凸
    + **结论**: $x^\star$ 全局极小 $\Leftrightarrow$ $\nabla f(x^\star)=0$

+ **Second-order characterization (Hessian test)** / **凸性二阶刻画**:
    + **假设**: $f\in C^2$; 定义域为开凸集
    + **结论**: $f$ 凸 $\Leftrightarrow$ $\nabla^2 f(x)\succeq 0$ $\forall x$
    + **特例**: $f(x)=\tfrac12 x^TQx-b^Tx$ 凸 $\Leftrightarrow$ $Q\succeq 0$

+ **Logistic loss convexity** / **逻辑回归凸**:
    + **假设**: $F(x)=\frac1n\sum_i\log(1+e^{-y_ia_i^Tx})$
    + **结论**: $\nabla^2 F(x)\succeq 0$, 故 $F$ 凸 (单样本海森 $w(1-w)aa^T\succeq 0$)

+ **GD rate: convex + L-smooth** / **凸 + 光滑**:
    + **假设**: $f$ 凸且 $L$-光滑; 存在极小点 $x^\star$; $\alpha_k=1/L$
    + **结论**: $f(x_k)-f(x^\star)\le\frac{L\|x_0-x^\star\|^2}{2k}=O(1/k)$
    + **复杂度**: 间隙 $\le\delta$ 需 $O(1/\delta)$ 步

### 强凸

+ **Hessian sandwich for strong convex + smooth** / **海森夹逼**:
    + **假设**: $f\in C^2$
    + **结论**: $\mu$-强凸且 $L$-光滑 $\Leftrightarrow$ $\mu I\preceq\nabla^2 f(x)\preceq LI$ $\forall x$

+ **GD rate: μ-strongly convex + L-smooth** / **强凸线性收敛**:
    + **假设**: $f$ 为 $\mu$-强凸且 $L$-光滑; $\alpha_k=1/L$
    + **结论**: $f(x_k)-f^\star\le\bigl(1-\frac\mu L\bigr)^k\bigl(f(x_0)-f^\star\bigr)$
    + **复杂度**: 缩间隙因子约需 $O(\kappa\log(1/\delta))$ 步, $\kappa=L/\mu$

### 牛顿法

+ **Newton step from quadratic model** / **牛顿步**:
    + **假设**: $H_k=\nabla^2 f(x_k)$ 可逆 (常需 $H_k\succ 0$)
    + **结论**: $H_kp_k=-\nabla f(x_k)$; 若 $H_k\succ 0$ 则该临界点是二阶模型唯一全局极小

+ **Newton on PD quadratic** / **正定二次型一步到解**:
    + **假设**: $f(x)=\tfrac12 x^TQx-b^Tx$, $Q\succ 0$; 满步牛顿
    + **结论**: 从任意 $x_0$, 一步到达 $x^\star=Q^{-1}b$

+ **Local quadratic convergence of Newton** / **局部二次收敛**:
    + **假设**: $\nabla f(x^\star)=0$; $\nabla^2 f(x^\star)\succ 0$; 海森在 $x^\star$ 附近 $\rho$-Lipschitz; $x_0$ 足够靠近 $x^\star$; 满步牛顿
    + **结论**: 存在 $C$ 使 $\|x_{k+1}-x^\star\|\le C\|x_k-x^\star\|^2$
    + **注**: 保证是局部的; 远处满步可能失败

### 线搜索与全球化

+ **Backtracking finite termination** / **回溯有限终止**:
    + **假设**: $p_k$ 为下降方向 ($\nabla f^Tp_k<0$); $c_A\in(0,1)$; $\eta\in(0,1)$
    + **结论**: 存在 $\alpha_0>0$ 使一切 $\alpha\in(0,\alpha_0]$ 满足 Armijo; 几何缩小必在有限步终止

+ **Global convergence with backtracking** / **带回溯的全局收敛**:
    + **假设**: $f$ 有下界且 $L$-光滑; 方向一致满足 $\nabla f^Tp_k\le-\sigma\|\nabla f\|^2$ 且 $\|p_k\|\le\beta\|\nabla f\|$ ($\sigma,\beta>0$); Armijo 回溯参数 $c_A,\eta,\bar\alpha$
    + **结论**: 接受步长有与 $k$ 无关的下界 $\alpha=\min\bigl\{\bar\alpha,\,2\eta(1-c_A)\sigma/(L\beta^2)\bigr\}$; 且
      $$\min_{0\le j<k}\|\nabla f(x_j)\|^2\le\frac{f(x_0)-f^\star}{c_A\sigma\alpha\,k},\qquad \|\nabla f(x_k)\|\to 0$$

+ **Newton + backtracking (global then local)** / **牛顿+回溯**:
    + **假设**: $f\in C^2$, $\mu$-强凸且 $L$-光滑; 牛顿方向 + 回溯
    + **结论**: 从任意 $x_0$ 有 $x_k\to x^\star$ (唯一全局极小)
    + **加强假设**: $\bar\alpha=1$, $c_A<1/2$, 海森局部 Lipschitz
    + **加强结论**: 最终接受满步 $\alpha_k=1$ 并恢复局部二次收敛

---

## 速率速记 (GD, $\alpha=1/L$)

| 假设 | 结论 |
|---|---|
| 有下界 + $L$-光滑 | $\min_{j<k}\|\nabla f(x_j)\|^2=O(1/k)$ |
| 再 + 凸 | $f(x_k)-f^\star=O(1/k)$ |
| 再 + $\mu$-强凸 | $(1-\mu/L)^k$ 线性收敛 |

| 方法 | 典型保证 |
|---|---|
| 正定二次型满步牛顿 | 1 步到解 |
| 海森 PD + Lipschitz, 靠近 | 二次收敛 |
| Armijo 回溯 | 下降方向下有限终止 |
| 强凸光滑 + 牛顿回溯 | 全局收敛; 靠近后常恢复满步二次率 |

---

## 易错点

1. 驻点 $\neq$ 极小; 需二阶 / 凸性
2. 小 $\|\nabla f\|$ alone 不保证最优 (非凸时)
3. 魏尔斯特拉斯需紧 + 连续
4. 精确线搜索是选 $\alpha$ 的方法, 方向可为 GD / 牛顿等; 闭式 $g^Tg/(g^TQg)$ 是「二次型 + $p=-g$」特例
5. 牛顿满步在远处可能失败 — 用回溯全球化
6. 病态 $\kappa\gg 1$ 时 GD 沿平坦方向极慢
7. Lasso 的 $\ell_1$ 在 $0$ 不可微; 逻辑回归损失是 NLL $\log(1+e^{-ya^Tx})$, 非指数损失

---

## 问答沉淀

+ **紧集为何对 Weierstrass 重要**:
    + 保证连续 $f$ 在非空 $C$ 上必取到 global minimizer; 缺闭或缺有界都可能失败
+ **几百页 optional textbook (如 Boyd)**:
    + 仅作参考存放, 不自动生成全文讲义; 需要时按章点名
+ **$x^TAx$ 对 $x$ 的梯度**:
    + 一般 $(A+A^T)x$; $A$ 对称时 $2Ax$
+ **精确线搜索 vs 牛顿方向**:
    + 线搜索选步长; 方向另定. 讲义闭式对应 GD 方向; 牛顿方向在正定二次型上精确线搜索常得 $\alpha=1$
+ **Armijo 的 $c_A$**:
    + 固定超参 $\in(0,1)$; 要求真实下降至少为线性预测的 $c_A$ 倍; 实务常取很小 (如 $10^{-4}$)
+ **Tutorial1 易错 (min 不保凸; 步长过大可升值)**:
    + **假设**: 讨论凸性保持运算, 或对 $L$-光滑 $f$ 做固定步长 GD
    + **结论**: 若干凸函数取 $\min$ **一般不**保持凸; GD 步长过大 (如 $\alpha\ge 2/L$) 时目标值可能上升甚至发散, 不可默认「沿负梯度必降」

