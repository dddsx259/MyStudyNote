# MATH3900 Cheatsheet

> 词条/公式/theorem 速查; 对话中学到的内容会增量追加.

---

## 名词

+ **Decision variable** / **决策变量** $x$:
    + $x\in\mathbb{R}^d$, 优化问题的自变量
+ **Feasible region** / **可行域** $C$:
    + $C\subseteq\mathbb{R}^d$; $x\in C$ 可行
+ **Global / Local minimizer** / **全局/局部最小点**:
    + Global: 全 $C$ 上最小; Local: 某邻域内最小
+ **Optimal value** / **最优值** $f^*$:
    + $f^*=\inf_{x\in C} f(x)$
+ **Compact set** / **紧集** (in $\mathbb{R}^d$, Heine–Borel):
    + 闭且有界 (closed and bounded)
    + 有界: $\exists M$, $\|x\|\le M\ \forall x\in C$
    + 闭: 含全部极限点
+ **Gradient / Hessian** / **梯度/ Hessian**:
    + $\nabla f$, $\nabla^2 f$; 一阶/二阶 Taylor 的核心
+ **Stationary point** / **驻点**:
    + $\nabla f(x^\star)=0$; 局部极小的一阶必要, 非充分
+ **PSD / PD** / **正半定/正定**:
    + $Q\succeq 0$: $z^TQz\ge 0$; $Q\succ 0$: $z\neq 0$ 时 $>0$
+ **L-smooth** / **$L$-光滑**:
    + $\|\nabla f(u)-\nabla f(v)\|\le L\|u-v\|$
+ **Strong convexity** / **强凸**:
    + $\mu$-强凸: 切平面 $+$ $\frac\mu2\|v-u\|^2$ 下界; $\kappa=L/\mu$
+ **Descent / steepest descent** / **下降/最速下降方向**:
    + $\nabla f^Tp<0$; 最速为 $-\nabla f$
+ **Armijo / backtracking** / **Armijo/回溯线搜索**:
    + 充分下降条件; 试探步长按 $\eta$ 缩小

## 公式

+ **Optimization problem** / **优化问题**:
    + $\min_{x\in C} f(x)$; $\max f = \min(-f)$
+ **Linear regression (MSE)** / **线性回归**:
    + $\min_x \frac{1}{2n}\sum_i (a_i^T x-y_i)^2 = \min_x \frac{1}{2n}\|Ax-y\|^2$
+ **Logistic regression** / **逻辑回归**:
    + $\min_x \frac{1}{n}\sum_i \log(1+e^{-y_i a_i^T x})$
+ **Hard-margin SVM**:
    + $\min_x \frac{1}{2}\|x\|^2$ s.t. $y_i a_i^T x\ge 1$
+ **Lasso**:
    + $\min_x \frac{1}{2n}\|Ax-y\|^2 + \lambda\|x\|_1$
+ **Chain rule** / **链式法则**:
    + $\nabla F(x)=J_h(x)^T \nabla g(h(x))$
+ **Linear regression gradient**:
    + $\nabla F(x)=\frac{1}{n}A^T(Ax-y)$
+ **First-order Taylor**:
    + $f(x+s)=f(x)+\nabla f(x)^T s+o(\|s\|)$
+ **Gradient descent**:
    + $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$; 常取 $\alpha=1/L$
+ **Descent lemma**:
    + $f(v)\le f(u)+\nabla f(u)^T(v-u)+\frac L2\|v-u\|^2$
+ **Newton step**:
    + $\nabla^2 f(x_k)p_k=-\nabla f(x_k)$ (解线性系)

## 定理

+ **Weierstrass theorem**:
    + $C$ 非空紧, $f$ 连续 $\Rightarrow$ 存在 global minimizer on $C$
+ **FOC / SOC (unconstrained)**:
    + 局部极小 $\Rightarrow$ $\nabla f=0$; $C^2$ 时再加 $\nabla^2 f\succeq 0$. 充分: $\nabla f=0$ 且 $\nabla^2 f\succ 0$
+ **Convex differentiable**:
    + 全局极小 $\Leftrightarrow$ $\nabla f=0$; 海森检验 $\nabla^2 f\succeq 0$
+ **GD rates ($α=1/L$)**:
    + 光滑有下界: $\min\|\nabla f\|^2=O(1/k)$; 凸: 间隙 $O(1/k)$; 强凸: $(1-μ/L)^k$
+ **Newton local**:
    + $\nabla f(x^\star)=0$, $\nabla^2 f(x^\star)\succ 0$, 海森 Lipschitz $\Rightarrow$ 二次收敛
+ **Newton + backtracking (strong convex + smooth)**:
    + 从任意 $x_0$ 全局收敛到唯一极小; 靠近后可恢复满步二次率

## 问答沉淀

+ **紧集为何对 Weierstrass 重要**:
    + 保证连续 $f$ 在非空 $C$ 上必取到 global minimizer; 缺闭或缺有界都可能失败
+ **几百页 optional textbook (如 Boyd)**:
    + 仅作参考存放, 不自动生成全文讲义; 需要时按章点名

