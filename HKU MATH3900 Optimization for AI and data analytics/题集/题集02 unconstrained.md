# 题集 — Lec02 Unconstrained

> 对齐: `Lec/Lec02 unconstrained slides 讲义.md`.
> 含: (1) 课件证明 (2) 练习题 (Tut1–3, HW1–2, 课件例).

## 课件证明

### P1. 一阶必要条件 (FONC, first-order necessary condition)

- **陈述**: $f$ 在 $x^\star$ 可微且 $x^\star$ 为局部极小点 $\Rightarrow$ $\nabla f(x^\star)=0$.
- **证明**: 反证. 设 $g:=\nabla f(x^\star)\neq 0$, 取 $p=-g$. 一阶 Taylor: $f(x^\star+tp)=f(x^\star)+t g^Tp+o(t)=f(x^\star)-t\lVert g\rVert^2+o(t)$. 对充分小 $t>0$, $-t\lVert g\rVert^2+o(t)<0$, 故 $f(x^\star+tp)<f(x^\star)$, 与局部极小矛盾. 故 $g=0$.
- **来源**: Lec02 §2 / 讲义

### P2. 二阶必要条件 (SONC, second-order necessary condition)

- **陈述**: $f$ 在 $x^\star$ 附近 $C^2$, $x^\star$ 为局部极小 $\Rightarrow$ $\nabla f(x^\star)=0$ 且 $\nabla^2 f(x^\star)\succeq 0$.
- **证明**: FONC 得 $\nabla f(x^\star)=0$. 若存在 $v\neq 0$ 使 $v^T\nabla^2 f(x^\star)v<0$, 二阶 Taylor:
  $$f(x^\star+tv)=f(x^\star)+\frac{t^2}{2}v^T\nabla^2 f(x^\star)v+o(t^2).$$
  对充分小 $t\neq 0$, 右边 $<f(x^\star)$, 矛盾. 故 $\nabla^2 f(x^\star)\succeq 0$.
- **来源**: Lec02 §2 / 讲义

### P3. 二阶充分条件 (SOSC, second-order sufficient condition)

- **陈述**: $f$ 在 $x^\star$ 附近 $C^2$, $\nabla f(x^\star)=0$, $\nabla^2 f(x^\star)\succ 0$ $\Rightarrow$ $x^\star$ 为严格局部极小.
- **证明**: $\nabla^2 f(x^\star)\succ 0$ 且连续 $\Rightarrow$ 存在 $\mu>0$ 与邻域 $U$ 使 $x\in U$ 时 $\nabla^2 f(x)\succeq\frac{\mu}{2}I$. 对 $h$ 小, 积分余项 Taylor:
  $$f(x^\star+h)=f(x^\star)+\int_0^1(1-t)h^T\nabla^2 f(x^\star+th)h\,dt\ge f(x^\star)+\frac{\mu}{4}\lVert h\rVert^2.$$
  故 $h\neq 0$ 时 $f(x^\star+h)>f(x^\star)$.
- **来源**: Lec02 §2 / 讲义

### P4. 最速下降方向 (steepest descent direction)

- **陈述**: 在 $\lVert p\rVert=1$ 约束下, $\nabla f(x)^Tp$ 的最小值为 $-\lVert\nabla f(x)\rVert$, 在 $p=-\nabla f(x)/\lVert\nabla f(x)\rVert$ 达到 (即 $-\nabla f$ 为最速下降方向).
- **证明**: Cauchy–Schwarz: $|\nabla f^Tp|\le\lVert\nabla f\rVert\lVert p\rVert=\lVert\nabla f\rVert$, 故 $\nabla f^Tp\ge-\lVert\nabla f\rVert$. 取 $p=-\nabla f/\lVert\nabla f\rVert$ 得 $\nabla f^Tp=-\lVert\nabla f\rVert$, 等号成立.
- **来源**: Lec02 §3 / 讲义

### P5. 一维 GD 步长反例 (1D gradient descent counterexample)

- **陈述**: $f(x)=\frac{1}{2}x^2$, GD $x_{k+1}=x_k-\alpha\nabla f(x_k)=(1-\alpha)x_k$. $\alpha\in(0,2)$ 收敛; $\alpha=2$ 振荡; $\alpha>2$ 发散.
- **证明**: $\nabla f(x)=x$, 故 $x_k=(1-\alpha)^k x_0$. $|1-\alpha|<1$ $\Leftrightarrow$ $\alpha\in(0,2)$ 时 $x_k\to 0$; $\alpha=2$ 时 $x_k=(-1)^k x_0$; $\alpha>2$ 时 $|1-\alpha|>1$, $|x_k|\to\infty$.
- **来源**: Lec02 §3 / 讲义

### P6. 下降引理 (descent lemma)

- **陈述**: $f$ 为 $L$-光滑 ($\nabla f$ 为 $L$-Lipschitz) $\Rightarrow$ 对任意 $u,v$,
  $$f(v)\le f(u)+\nabla f(u)^T(v-u)+\frac{L}{2}\lVert v-u\rVert^2.$$
- **证明**: 令 $x(t)=u+t(v-u)$, $g(t)=f(x(t))$. FTC:
  $$f(v)-f(u)=\int_0^1\nabla f(x(t))^T(v-u)\,dt=\nabla f(u)^T(v-u)+\int_0^1\bigl(\nabla f(x(t))-\nabla f(u)\bigr)^T(v-u)\,dt.$$
  由 $\lVert\nabla f(x(t))-\nabla f(u)\rVert\le L\lVert x(t)-u\rVert=Lt\lVert v-u\rVert$ 与 Cauchy–Schwarz,
  $$\Bigl|\int_0^1\cdots dt\Bigr|\le\int_0^1 Lt\lVert v-u\rVert^2\,dt=\frac{L}{2}\lVert v-u\rVert^2.$$
  代入即得. (对称下界: 交换 $u\leftrightarrow v$.)
- **来源**: Lec02 §4 / 讲义

### P7. GD 单步下降推论 ($\alpha=1/L$)

- **陈述**: $f$ 为 $L$-光滑, $x_{k+1}=x_k-\alpha\nabla f(x_k)$, $0<\alpha<2/L$ 且 $g_k=\nabla f(x_k)\neq 0$ 时严格下降; $\alpha=1/L$ 时
  $$f(x_{k+1})\le f(x_k)-\frac{1}{2L}\lVert g_k\rVert^2.$$
- **证明**: 在 P6 中取 $u=x_k$, $v=x_k-\alpha g_k$:
  $$f(x_{k+1})\le f(x_k)-\alpha\lVert g_k\rVert^2+\frac{L\alpha^2}{2}\lVert g_k\rVert^2=f(x_k)-\alpha\Bigl(1-\frac{L\alpha}{2}\Bigr)\lVert g_k\rVert^2.$$
  $0<\alpha<2/L$ 时括号 $>0$. $\alpha=1/L$ 时减 $\frac{1}{2L}\lVert g_k\rVert^2$.
- **来源**: Lec02 §4 / 讲义

### P8. 仅 $L$-光滑 + 有下界: 梯度范数 $O(1/k)$

- **陈述**: $f$ 为 $L$-光滑, $f^\star:=\inf f>-\infty$, $\alpha_k=1/L$. 对 $k\ge 1$,
  $$\min_{0\le j<k}\lVert\nabla f(x_j)\rVert^2\le\frac{2L\bigl(f(x_0)-f^\star\bigr)}{k}.$$
- **证明**: 由 P7, $\frac{1}{2L}\lVert\nabla f(x_j)\rVert^2\le f(x_j)-f(x_{j+1})$. 对 $j=0,\ldots,k-1$ 望远镜求和:
  $$\sum_{j=0}^{k-1}\frac{1}{2L}\lVert\nabla f(x_j)\rVert^2\le f(x_0)-f(x_k)\le f(x_0)-f^\star.$$
  左边 $\ge\frac{k}{2L}\min_{j<k}\lVert\nabla f(x_j)\rVert^2$, 整理即得.
- **来源**: Lec02 §4 / 讲义

### P9. 凸性保持 (convexity preservation)

- **陈述**: (a) $f_i$ 凸, $\gamma_i\ge 0$ $\Rightarrow$ $\sum_i\gamma_i f_i$ 凸; (b) $g$ 凸 $\Rightarrow$ $x\mapsto g(Mx+q)$ 凸; (c) $f_i$ 凸 $\Rightarrow$ $\max_i f_i$ 凸.
- **证明**: (a) 对 $\theta\in[0,1]$, $u,v$,
  $$\sum_i\gamma_i f_i(\theta u+(1-\theta)v)\le\sum_i\gamma_i\bigl(\theta f_i(u)+(1-\theta)f_i(v)\bigr)=\theta\sum_i\gamma_i f_i(u)+(1-\theta)\sum_i\gamma_i f_i(v).$$
  (b) 令 $h(x)=Mx+q$, $y=\theta u+(1-\theta)v$, 则 $h(y)=\theta h(u)+(1-\theta)h(v)$, $g(h(y))\le\theta g(h(u))+(1-\theta)g(h(v))$. (c) 对每 $i$, $f_i(\theta u+(1-\theta)v)\le\theta f_i(u)+(1-\theta)f_i(v)\le\max_j\{\theta f_j(u)+(1-\theta)f_j(v)\}=\theta\max_j f_j(u)+(1-\theta)\max_j f_j(v)$.
- **来源**: Lec02 §5 / 讲义

### P10. 凸函数一阶刻画与驻点即全局极小

- **陈述**: $f$ 可微. (i) $f$ 凸 $\Leftrightarrow$ $f(v)\ge f(u)+\nabla f(u)^T(v-u)$ 对所有 $u,v$; (ii) 若 $f$ 凸, $x^\star$ 全局极小 $\Leftrightarrow$ $\nabla f(x^\star)=0$.
- **证明**: (i) ($\Rightarrow$) 凸性: $f(u+t(v-u))\le(1-t)f(u)+tf(v)$, 移项除以 $t>0$, $t\to 0^+$ 得 $\nabla f(u)^T(v-u)\le f(v)-f(u)$. ($\Leftarrow$) 令 $u_\theta=\theta u+(1-\theta)v$. 对 $u_\theta$ 写切平面下界:
  $$f(u)\ge f(u_\theta)+\nabla f(u_\theta)^T(u-u_\theta),\quad f(v)\ge f(u_\theta)+\nabla f(u_\theta)^T(v-u_\theta).$$
  第一式乘 $\theta$, 第二式乘 $1-\theta$, 相加得 $f(\theta u+(1-\theta)v)\le\theta f(u)+(1-\theta)f(v)$. (ii) ($\Rightarrow$) 局部极小 $\Rightarrow$ FONC. ($\Leftarrow$) $\nabla f(x^\star)=0$ 代入 (i): $f(v)\ge f(x^\star)$.
- **来源**: Lec02 §5 / 讲义

### P11. 梯度单调性 (gradient monotonicity)

- **陈述**: $f$ 可微凸 $\Rightarrow$ $(\nabla f(v)-\nabla f(u))^T(v-u)\ge 0$ 对所有 $u,v$.
- **证明**: 由 P10(i) 写两次切平面下界:
  $$f(v)\ge f(u)+\nabla f(u)^T(v-u),\qquad f(u)\ge f(v)+\nabla f(v)^T(u-v).$$
  相加: $0\ge(\nabla f(u)-\nabla f(v))^T(v-u)$, 即结论.
- **来源**: Lec02 §5 / 讲义

### P12. Hessian 凸性检验 (双向)

- **陈述**: $f\in C^2$ 在开凸集 $C$ 上. $f$ 凸 $\Leftrightarrow$ $\nabla^2 f(x)\succeq 0$ 对所有 $x\in C$.
- **证明**: ($\Rightarrow$) 固定 $x$, 方向 $d$, 取 $u=x$, $v=x+td$ ($t\neq 0$ 小). P11 给出
  $$d^T\frac{\nabla f(x+td)-\nabla f(x)}{t}\ge 0.$$
  $t\to 0$ 得 $d^T\nabla^2 f(x)d\ge 0$. ($\Leftarrow$) 固定 $u,v\in C$, $g(t)=f(u+t(v-u))$, $t\in[0,1]$. 则 $g''(t)=(v-u)^T\nabla^2 f(u+t(v-u))(v-u)\ge 0$, 故 $g'$ 递增,
  $$f(v)-f(u)=g(1)-g(0)=\int_0^1 g'(t)\,dt\ge g'(0)=\nabla f(u)^T(v-u),$$
  由 P10(i) 得 $f$ 凸.
- **来源**: Lec02 §5 / Tut2 / 讲义

### P13. 逻辑回归目标凸 (logistic loss convexity)

- **陈述**: $F(x)=\frac{1}{n}\sum_i\log(1+e^{-y_i a_i^T x})$ 为凸函数.
- **证明**: 单样本 $\ell_i(x)=\log(1+e^{-z_i})$, $z_i=-y_i a_i^T x$. 令 $w_i=\sigma(y_i a_i^T x)=\frac{1}{1+e^{-y_i a_i^T x}}$. 直接求导 (或链式法则):
  $$\nabla\ell_i=-y_i w_i a_i,\qquad \nabla^2\ell_i=w_i(1-w_i)a_ia_i^T.$$
  $w_i\in(0,1)$ $\Rightarrow$ $w_i(1-w_i)>0$, 故 $\nabla^2\ell_i\succeq 0$. 平均后 $\nabla^2 F=\frac{1}{n}\sum_i\nabla^2\ell_i\succeq 0$, $F$ 凸.
- **来源**: Lec02 §5 / 讲义

### P14. 凸 + $L$-光滑 GD: 目标间隙 $O(1/k)$

- **陈述**: $f$ 凸, $L$-光滑, $x^\star$ 为全局极小, $\alpha=1/L$, GD 迭代 $x_k$. 则
  $$f(x_k)-f(x^\star)\le\frac{L\lVert x_0-x^\star\rVert^2}{2k}.$$
- **证明**: 记 $g_k=\nabla f(x_k)$, $x_{k+1}=x_k-\frac{1}{L}g_k$.
  **Step 1 (距离恒等式)**:
  $$\lVert x_{k+1}-x^\star\rVert^2=\lVert x_k-x^\star\rVert^2-\frac{2}{L}g_k^T(x_k-x^\star)+\frac{1}{L^2}\lVert g_k\rVert^2.$$
  **Step 2 (凸性)** $f(x_k)-f(x^\star)\le g_k^T(x_k-x^\star)$, 故
  $$-\frac{2}{L}g_k^T(x_k-x^\star)\le-\frac{2}{L}\bigl(f(x_k)-f(x^\star)\bigr).$$
  **Step 3 (下降引理, P7)** $f(x_{k+1})\le f(x_k)-\frac{1}{2L}\lVert g_k\rVert^2$, 即 $\frac{1}{L^2}\lVert g_k\rVert^2\le\frac{2}{L}\bigl(f(x_k)-f(x_{k+1})\bigr)$.
  **Step 4 (合并)** 代入 Step 1:
  $$\lVert x_{k+1}-x^\star\rVert^2\le\lVert x_k-x^\star\rVert^2-\frac{2}{L}\bigl(f(x_k)-f(x^\star)\bigr)+\frac{2}{L}\bigl(f(x_k)-f(x_{k+1})\bigr),$$
  整理得
  $$f(x_{k+1})-f(x^\star)\le\frac{L}{2}\bigl(\lVert x_k-x^\star\rVert^2-\lVert x_{k+1}-x^\star\rVert^2\bigr).$$
  **Step 5 (望远镜)** 对 $j=0,\ldots,k-1$ 求和, 中间 $\lVert x_j-x^\star\rVert^2$ 抵消:
  $$\sum_{j=0}^{k-1}\bigl(f(x_{j+1})-f(x^\star)\bigr)\le\frac{L}{2}\lVert x_0-x^\star\rVert^2.$$
  左边 $\ge k\bigl(f(x_k)-f(x^\star)\bigr)$ (因 $f(x_j)-f(x^\star)$ 沿 GD 非增), 故 $f(x_k)-f(x^\star)\le\frac{L\lVert x_0-x^\star\rVert^2}{2k}$.
- **来源**: Lec02 §5 / 讲义

### P15. 强凸海森 sandwich (strong convexity and Hessian)

- **陈述**: $f\in C^2$. $f$ 为 $\mu$-强凸 $\Leftrightarrow$ $\nabla^2 f(x)\succeq\mu I$ 对所有 $x$; $f$ 为 $L$-光滑 $\Leftrightarrow$ $\nabla^2 f(x)\preceq LI$. 故 $\mu$-强凸且 $L$-光滑时 $\mu I\preceq\nabla^2 f(x)\preceq LI$, 条件数 $\kappa=L/\mu$.
- **证明**: $f$ $\mu$-强凸 $\Leftrightarrow$ $g(x):=f(x)-\frac{\mu}{2}\lVert x\rVert^2$ 凸. $g\in C^2$ 时 $\nabla^2 g=\nabla^2 f-\mu I$, 由 P12, $g$ 凸 $\Leftrightarrow$ $\nabla^2 f\succeq\mu I$. 同理 $L$-光滑与 $\nabla^2 f\preceq LI$ 由下降引理二次上界或 $\lVert\nabla f(u)-\nabla f(v)\rVert\le L\lVert u-v\rVert$ 对线性函数取 $u,v$ 沿特征方向得 (讲义 §6 思路).
- **来源**: Lec02 §6 / 讲义

### P16. 强凸最优性间隙界 (optimality gap bound)

- **陈述**: $f$ 为 $\mu$-强凸且可微, $x^\star$ 为全局极小. 则
  $$f(x)-f(x^\star)\le\frac{1}{2\mu}\lVert\nabla f(x)\rVert^2.$$
- **证明**: 强凸: $f(x^\star)\ge f(x)+\nabla f(x)^T(x^\star-x)+\frac{\mu}{2}\lVert x^\star-x\rVert^2$. 移项,
  $$f(x)-f(x^\star)\le-\nabla f(x)^T(x^\star-x)-\frac{\mu}{2}\lVert x^\star-x\rVert^2.$$
  右端关于 $x^\star-x$ 的二次函数在 $x^\star-x=-\frac{1}{\mu}\nabla f(x)$ 处取最大 (配平方), 最大值为 $\frac{1}{2\mu}\lVert\nabla f(x)\rVert^2$.
- **来源**: Lec02 §6 / 讲义

### P17. 强凸 + $L$-光滑 GD 线性收敛

- **陈述**: $f$ 为 $\mu$-强凸, $L$-光滑, $\alpha=1/L$. 则
  $$f(x_k)-f(x^\star)\le\Bigl(1-\frac{\mu}{L}\Bigr)^k\bigl(f(x_0)-f(x^\star)\bigr).$$
- **证明**: P7: $f(x_{k+1})-f^\star\le f(x_k)-f^\star-\frac{1}{2L}\lVert\nabla f(x_k)\rVert^2$. P16: $\frac{1}{2L}\lVert\nabla f(x_k)\rVert^2\ge\frac{\mu}{L}(f(x_k)-f^\star)$. 故
  $$f(x_{k+1})-f^\star\le\Bigl(1-\frac{\mu}{L}\Bigr)(f(x_k)-f^\star).$$
  归纳即得.
- **来源**: Lec02 §6 / 讲义

### P18. 牛顿步 (Newton step)

- **陈述**: 二次模型 $m_k(p)=f(x_k)+\nabla f(x_k)^Tp+\frac{1}{2}p^T H_k p$, $H_k=\nabla^2 f(x_k)\succ 0$. 其唯一极小点满足 $H_k p_k=-\nabla f(x_k)$, 牛顿迭代 $x_{k+1}=x_k+p_k$.
- **证明**: $\nabla_p m_k(p)=\nabla f(x_k)+H_k p$ ($H_k$ 对称). 令其为 $0$ 得 $p_k=-H_k^{-1}\nabla f(x_k)$. $H_k\succ 0$ 时 $m_k$ 严格凸, 临界点为全局唯一极小.
- **来源**: Lec02 §7 / 讲义

### P19. 正定二次型: 牛顿一步到解

- **陈述**: $f(x)=\frac{1}{2}x^TQx-b^Tx$, $Q\succ 0$. 从任意 $x_0$ 满步牛顿得 $x_1=Q^{-1}b=x^\star$.
- **证明**: $\nabla f(x)=Qx-b$, $H=Q$. 牛顿步 $Q p_0=-(Qx_0-b)$ $\Rightarrow$ $p_0=-x_0+Q^{-1}b$. 故 $x_1=x_0+p_0=Q^{-1}b$.
- **来源**: Lec02 §7 / 讲义

### P20. 牛顿法局部二次收敛 (local quadratic convergence)

- **陈述**: $\nabla f(x^\star)=0$, $\nabla^2 f(x^\star)\succ 0$, $\nabla^2 f$ 在 $x^\star$ 附近 $\rho$-Lipschitz, $x_0$ 足够靠近 $x^\star$. 则存在 $C>0$ 使 $\lVert x_{k+1}-x^\star\rVert\le C\lVert x_k-x^\star\rVert^2$.
- **证明**: 满步牛顿 $x_{k+1}=x_k-H_k^{-1}\nabla f(x_k)$, $e_k:=x_k-x^\star$,
  $$e_{k+1}=H_k^{-1}\Bigl(H_k e_k-\nabla f(x_k)\Bigr).$$
  因 $\nabla f(x^\star)=0$, FTC:
  $$\nabla f(x_k)=\int_0^1\nabla^2 f(x^\star+te_k)e_k\,dt.$$
  故 $H_k e_k-\nabla f(x_k)=\int_0^1(H_k-\nabla^2 f(x^\star+te_k))e_k\,dt$. Lipschitz: $\lVert H_k-\nabla^2 f(x^\star+te_k)\rVert\le\rho(1-t)\lVert e_k\rVert$, 积分得 $\lVert H_k e_k-\nabla f(x_k)\rVert\le\frac{\rho}{2}\lVert e_k\rVert^2$. 邻域内 $\lambda_{\min}(H_k)\ge\mu'>0$, $\lVert H_k^{-1}\rVert\le 1/\mu'$, 故 $\lVert e_{k+1}\rVert\le\frac{\rho}{2\mu'}\lVert e_k\rVert^2$.
- **来源**: Lec02 §7 / 讲义

### P21. Armijo 回溯有限终止 (backtracking finite termination)

- **陈述**: $p_k$ 为下降方向 ($\nabla f(x_k)^Tp_k<0$), $c_A,\eta\in(0,1)$, 从 $\bar\alpha>0$ 起若 Armijo 不满足则 $\alpha\leftarrow\eta\alpha$. 则有限步内必接受某 $\alpha>0$.
- **证明**: 可微 $\Rightarrow$
  $$\lim_{\alpha\to 0^+}\frac{f(x_k+\alpha p_k)-f(x_k)}{\alpha}=\nabla f(x_k)^Tp_k.$$
  因 $c_A\in(0,1)$ 且 $\nabla f^Tp_k<0$, 存在 $\alpha_0>0$ 使一切 $\alpha\in(0,\alpha_0]$ 满足 Armijo
  $$f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha\nabla f(x_k)^Tp_k.$$
  回溯每次 $\alpha\leftarrow\eta\alpha$, 几何衰减, 有限步后 $\alpha\le\alpha_0$, 终止.
- **来源**: Lec02 §8 / 讲义

### P22. 带回溯的全局收敛 (主要步骤)

- **陈述**: $f$ 有下界, $L$-光滑, 方向满足 $\nabla f^Tp_k\le-\sigma\lVert\nabla f(x_k)\rVert^2$, $\lVert p_k\rVert\le\beta\lVert\nabla f(x_k)\rVert$ ($\sigma,\beta>0$). 则存在与 $k$ 无关的 $\alpha_{\min}>0$ 使回溯接受的 $\alpha_k\ge\alpha_{\min}$, 且 $\min_{j<k}\lVert\nabla f(x_j)\rVert^2=O(1/k)$, $\lVert\nabla f(x_k)\rVert\to 0$.
- **证明**: **Step 1**: 下降引理给出, 若 $0<\alpha\le\frac{2(1-c_A)\sigma}{L\beta^2}$, 则 Armijo 自动成立. **Step 2**: 回溯从 $\bar\alpha$ 缩小, 接受步长 $\alpha_k\ge\min\{\bar\alpha,\eta\cdot\frac{2(1-c_A)\sigma}{L\beta^2}\}=:\alpha_{\min}$. **Step 3**: Armijo + 方向条件 $\Rightarrow$ $f(x_k)-f(x_{k+1})\ge c_A\alpha_{\min}\sigma\lVert g_k\rVert^2$. **Step 4**: 对 $j=0,\ldots,k-1$ 望远镜求和, 用 $f\ge f^\star$ 得 $\sum_{j<k}\lVert g_j\rVert^2\le\frac{f(x_0)-f^\star}{c_A\alpha_{\min}\sigma}$, 故 $\min_{j<k}\lVert g_j\rVert^2=O(1/k)$ 且 $\lVert g_k\rVert\to 0$ (沿子列或级数收敛).
- **来源**: Lec02 §8 / 讲义

### P23. 牛顿 + 回溯 (Newton with backtracking, 概要)

- **陈述**: $f\in C^2$, $\mu$-强凸, $L$-光滑. 牛顿方向 + Armijo 回溯 $\Rightarrow$ $x_k\to x^\star$ (全局). 若 $\bar\alpha=1$, $c_A<1/2$, 海森局部 Lipschitz 且 $x_k$ 足够靠近 $x^\star$, 则最终接受满步 $\alpha_k=1$ 并恢复 P20 的二次收敛.
- **证明**: **Step 1**: $\mu I\preceq H_k\preceq LI$ $\Rightarrow$ $p_k=-H_k^{-1}g_k$ 满足 $\nabla f^Tp_k=-g_k^TH_k^{-1}g_k\le-\frac{1}{L}\lVert g_k\rVert^2$, $\lVert p_k\rVert\le\frac{1}{\mu}\lVert g_k\rVert$, 故 P22 适用. **Step 2**: 强凸 $\Rightarrow$ 唯一驻点 $x^\star$ 为全局极小, $\lVert g_k\rVert\to 0$ 推出 $x_k\to x^\star$. **Step 3**: 在 $x^\star$ 邻域, 满步牛顿的实际下降与二次模型一致; 标准结果表明 $c_A<1/2$ 时 $\alpha=1$ 满足 Armijo. **Step 4**: 满步后 P20 适用.
- **来源**: Lec02 §8 / 讲义

## 练习题

### 1. 凸性保持: 非负组合 / 仿射复合 / 逐点最大

- **题目**: (a) $f_i$ 凸, $\gamma_i\ge 0$ $\Rightarrow$ $\sum\gamma_i f_i$ 凸 (权重不必归一); (b) $g$ 凸 $\Rightarrow$ $g(Mx+q)$ 凸; (c) $f_i$ 凸 $\Rightarrow$ $\max_i f_i$ 凸. 用定义证明.
- **思路**: 直接代入凸不等式; (c) 用 $\max\le$ 各分量上界再取 max.
- **来源**: Tut1 Q0 / `tut/Tut01 总结.md`

### 2. Tut1 T/F (凸 / PD / 极小 / 下降)

- **题目**: 判断: (a) $h(t)=g(1-2t)$ 凸若 $g$ 凸; (b) $\min\{f_1,f_2\}$ 保凸; (c) 元全正对称 $\Rightarrow$ PD; (d) 严格局部极小 $\Rightarrow f''(t^*)>0$; (e) $p=-3\nabla f$ 为下降方向; (f) GD 步长 $1/L$ 在 $L$-光滑下严格下降 (不需凸).
- **思路**: (a)T 仿射复合; (b)F 反例 $t$ 与 $-t$; (c)F 算 $z^TQz$; (d)F $t^6$; (e)T $\nabla f^Tp=-3\lVert\nabla f\rVert^2$; (f)T 下降引理减 $\frac1{2L}\lVert\nabla f\rVert^2$.
- **来源**: Tut1 Q1 / `tut/Tut01 总结.md`

### 3. 线性回归 MSE 梯度与下降方向

- **题目**: $n=3$, $F=\frac16\lVert Ax-y\rVert^2$. 求 $\nabla F$; 在 $x^{(0)}=0$ 判断给定 $v_1,v_2$ 是否下降/最速.
- **思路**: $\nabla F=\frac13 A^T(Ax-y)$; 下降 $\Leftrightarrow \nabla F^Tv<0$; 单位球最速为 $-\nabla F/\lVert\nabla F\rVert$.
- **来源**: Tut1 Q2 / `tut/Tut01 总结.md`

### 4. 驻点分类: $f=x_1^2-2x_1x_2+\frac23 x_2^3$

- **题目**: 求驻点并用 Hessian 分类; 是否有全局极小.
- **思路**: $\nabla f=0$ 得 $(0,0)$ 鞍, $(1,1)$ 局部极小 ($H\succ 0$); $f(0,-t)\to-\infty$ 无全局极小.
- **来源**: Tut1 Q3 / `tut/Tut01 总结.md`

### 5. $L$-光滑常数与过大步长

- **题目**: $f=\frac12(4x_1^2+x_2^2)$, $x^{(0)}=(1,2)^T$. 最小 $L$; $\alpha=1/4$ 与 $\alpha=3/4$ 的下一步与目标值变化.
- **思路**: $L=\lambda_{\max}(H)=4$; $\alpha=1/L$ 下降引理保证降; $\alpha>2/L$ 可升值 (过冲).
- **来源**: Tut1 Q4 / `tut/Tut01 总结.md`

### 6. Hessian 凸性判别证明

- **题目**: $C$ 开凸, $f\in C^2$. 证 $f$ 凸 $\Leftrightarrow$ $\nabla^2 f(x)\succeq 0$ $\forall x$.
- **思路**: $\Rightarrow$ 凸$\Rightarrow$梯度单调$\Rightarrow$差商$\ge 0$$\Rightarrow$方向极限 $v^THv\ge 0$; $\Leftarrow$ 线段上 $\phi''\ge 0$ 得一阶刻画.
- **来源**: Tut2 定理 / `tut/Tut02 总结.md`

### 7. Tut2 T/F (严格凸 / SOC / 条件数)

- **题目**: (a) 严格凸+可微+$\nabla f(x^*)=0$$\Rightarrow$唯一全局极小; (b) $f'=f''=0$ 且 $f''\ge 0$$\Rightarrow$局部极小; (c) 强凸光滑 GD 因子 $1-\mu/L$, $\kappa$ 大则慢.
- **思路**: (a)T; (b)F 反例 $x^3$; (c)T.
- **来源**: Tut2 Q1 / `tut/Tut02 总结.md`

### 8. 逻辑回归: 严格凸但非强凸

- **题目**: 给定 $a_1,a_2,y_1,y_2$ 与 $\nabla^2\ell=\frac12\sum w_i aa^T$. (a) 证 $\nabla^2\ell\succ 0$ 故严格凸; (b) 沿 $x_t=t(1,-2)^T$ 说明非强凸且 $\inf\ell=0$ 不可达.
- **思路**: (a) $w_i>0$ 时二次型零仅当 $z=0$; (b) $e_2^THe_2\to 0$ 否定 $\mu I$; $\ell(x_t)\to 0$ 但处处 $>0$.
- **来源**: Tut2 Q2 / `tut/Tut02 总结.md`

### 9. 条件数与坐标 GD: $f_\kappa=\frac12(x_1^2+\kappa x_2^2)$

- **题目**: (a) 求 $\mu,L,\kappa$; (b) $\alpha=1/L$ 写出坐标更新; (c) 解释大 $\kappa$ 为何慢.
- **思路**: $\mu=1,L=\kappa$; $x_2$ 一步清零, $x_1$ 乘 $(1-1/\kappa)$; 瓶颈在平坦方向.
- **来源**: Tut2 Q3 / `tut/Tut02 总结.md`

### 10. HW1 T/F (强凸 / 凸极小集 / 满步)

- **题目**: (b) $\nabla f(u)=\nabla f(v)$ ($u\neq v$)$\Rightarrow$非强凸; (c) $C^2$ 凸且唯一全局极小$\Rightarrow$某 $\mu$-强凸; (d) 凸+两全局极小$\Rightarrow$线段上皆极小; (e) $\nabla f\neq 0$$\Rightarrow f(x-\nabla f)<f(x)$.
- **思路**: (b)T 梯度严格单调; (c)F 可扁但仍唯一; (d)T; (e)F 步长 1 可能过大.
- **来源**: HW1 Q1 / `assignment/Assignment01 题目理解.md`

### 11. 驻点与全局极小: $f=\frac14 x_1^4-\frac12 x_1^2+\frac12 x_2^2$

- **题目**: 求 $\nabla f,\nabla^2 f$; 分类驻点; 找全局极小与最优值; 另讨论 $h=x_1^4-x_2^4$ 在原点.
- **思路**: 解 $\nabla f=0$; Hessian 特征值分类; 比较函数值; $h$ 沿轴变号$\Rightarrow$鞍.
- **来源**: HW1 Q2 / `assignment/Assignment01 解答.md`

### 12. Ridge $f_\lambda$: 显式 / 凸性 / 极小

- **题目**: $n=d=2$, $a_1=(1,1),y_1=1$, $a_2=(2,2),y_2=2$. 写 $f_\lambda$, $\nabla$, $H$; 按 $\lambda$ 判凸/强凸与 $\mu,L,\kappa$; 讨论极小存在唯一性; $\lambda=1$ 求最小值.
- **思路**: 写成二次型; $H=\frac1n\sum a_ia_i^T+\lambda I$; 特征值决定 $\mu,L$.
- **来源**: HW1 Q3 / `assignment/Assignment01 解答.md`

### 13. 一维 GD: $f(t)=t^4/4+t^2/2$

- **题目**: 求 $f',f''$, 全局极小; 是否强凸 / 梯度全局 $L$-Lipschitz; $t_0=1,\alpha=1/4$ 算两步; 刻画 $f(t_1)<f(t_0)$ 的 $\alpha$; 证 $|t_0|\le 1,\alpha=1/4$$\Rightarrow |t_k|\le(3/4)^k|t_0|$.
- **思路**: $f'(t)=t^3+t$; 极小在 $0$; $f''$ 无界$\Rightarrow$非全局 $L$-光滑; 收缩用 $|1-\alpha f''(c)|$ 或直接估计.
- **来源**: HW1 Q4 / `assignment/Assignment01 解答.md`

### 14. $\ell_\infty$ 最速下降与线性率

- **题目**: (i) $\min_{\lVert p\rVert_\infty\le 1}\nabla f^Tp$ 的最优值与方向; (ii) 一维 $\phi(t)=t^2/2$ 的 sign 迭代是否到 0; (iii) $L$-光滑下降不等式含 $\lVert\nabla f\rVert_1$; (iv) 再加 $\mu$-强凸得线性率 $(1-\mu/(Ld))^k$.
- **思路**: 最优 $p=-\mathrm{sign}(\nabla f)$, 值 $-\lVert\nabla f\rVert_1$; 下降引理+$\lVert p\rVert_2\le\sqrt{d}\lVert p\rVert_\infty$; 强凸间隙界收尾.
- **来源**: HW1 Q5 / `assignment/Assignment01 解答.md`

### 15. Tut3 T/F (条件数 / Newton / Armijo)

- **题目**: (a) 正定二次型乘正数条件数不变; (b) $H$ 可逆 $\Rightarrow$ Newton 极小化二次模型; (c) $H\succ 0$ $\Rightarrow$ Newton 下降; (d) 凸 + Armijo $\alpha$ $\Rightarrow$ $\alpha/2$ Armijo.
- **思路**: (a)T; (b)F 凹二次; (c)T $g^Tp=-p^THp$; (d)T 中点凸性.
- **来源**: Tut3 Q1 / `tut/Tut03 总结.md`

### 16. 逻辑回归 GD vs Newton 一步 (Tut3 Q2)

- **题目**: 六样本 $F$; 求 $\nabla,\nabla^2$; 最小全局 $L$; 从 $0$ 比较 GD($1/L$) 与满 Newton.
- **思路**: $L=9/8$; Newton 更近 $x^\star$ 但非一步到达.
- **来源**: Tut3 Q2

### 17. 一维 Newton 局部二次收敛 (Tut3 Q3)

- **题目**: $f=t^3/3-t$; 更新公式; $D$ 上证 $|e_{k+1}|\le|e_k|^2$.
- **思路**: $t\leftarrow\frac12(t+1/t)$; $e_{k+1}=e_k^2/(2t)$.
- **来源**: Tut3 Q3

### 18. 精确线搜索 vs Armijo (Tut3 Q4)

- **题目**: $f=\frac12(x_1^2+3x_2^2)$, $p=-g$; 精确步; Armijo 区间; $\alpha=1/4,5/6$ 对照.
- **思路**: $\alpha^\star=1/2$; Armijo $0<\alpha\le 3/4$; $5/6$ 下降但不 Armijo.
- **来源**: Tut3 Q4

### 19. HW2 T/F (Newton 仿射 / 精确线搜索 / Armijo 尺度 / GD-Armijo / 一步牛顿⇒二次)

- **题目**: (a) $af+b$ 不改 Newton 方向; (b) $\alpha^\star>0$ 精确线搜索 $\Rightarrow g^Tp=0$; (c) $p\mapsto sp$ 同一套回溯是否同点; (d) 仅「某 $\alpha_k>0$ Armijo」的 GD $\Rightarrow\|g\|\to0$; (e) $f''>0$ 且满 Newton 处处一步到极小 $\Rightarrow$ 二次.
- **思路**: (a)T; (b)T; (c)F 候选步长不缩放; (d)F 步长可过小; (e)T 推出 $f'''=0$.
- **来源**: HW2 Q1 / `assignment/Assignment02 解答.md`

### 20. Soft-abs Newton + Armijo (HW2 Q2)

- **题目**: $f=\sqrt{1+t^2}$; 导数/极小/更新 $t_+=-t^3$; 从 $2$ 做 Newton+Armijo 两步; 满 Newton 吸引域与 $q=3$.
- **思路**: 试 $\alpha=1,1/2$ 失败, $1/4$ 得 $t_1=-1/2$; 再满步 $t_2=1/8$; $|t_0|<1$ 收敛.
- **来源**: HW2 Q2

### 21. 四次扰动二次型 Newton 与仿射不变 (HW2 Q3)

- **题目**: 在 $(1,0)$ 满 Newton; $(u,v)$ 坐标下对 $F$ 一步; 证 $F(z)=f(Az+b)$ 时 $x_+=Az_++b$.
- **思路**: $x^{(1)}=(2/9,2/9)$; $F=\frac34 u^2+\frac14 v^2+\frac14 u^4$; 链式法则消 $A^T$.
- **来源**: HW2 Q3

### 22. 角条件方向 + 回溯充分下降 (HW2 Q4)

- **题目**: $-g^Tp\ge a\|g\|\|p\|$, $\|p\|\ge b\|g\|$; 证 $\|x_{k+1}-x_k\|\ge\delta\|g\|$ 与 $f$ 充分下降; 强凸几何率; 精确线搜索继承同一 $C$.
- **思路**: 回溯步长下界 $\min\{\bar\alpha,\eta\cdot 2(1-c_A)a\|g\|/(L\|p\|)\}$; $\delta=\min\{\bar\alpha b,2\eta(1-c_A)a/L\}$.
- **来源**: HW2 Q4

### 23. Inexact Newton (HW2 Q5)

- **题目**: 残差例子是否下降; $\|r\|\le\theta\|g\|$ ($\theta<\mu/L$) 推出角条件; 套 Q4 全局收敛; Lipschitz Hessian + 满步 + $\|r\|=O(\|g\|^2)$ 局部二次.
- **思路**: $a=(\mu/L-\theta)/(1+\theta)$, $b=(1-\theta)/L$; 局部用积分余项.
- **来源**: HW2 Q5


### 24. Tut4 Q1 — Newton + Armijo 全局/二次收敛 (**Test1 scope 外**)

- **题目**: 强凸+$L$-光滑下方向界 $\sigma=1/L,\beta=1/\mu$; $\|x-x^\star\|\le\|g\|/\mu$; 最终满步与二次率 $\rho/(2\mu)$.
- **思路**: 课堂全局定理 + Hessian Lipschitz 余项.
- **来源**: `tut/Tut04` (+ sol)

### 25. Tut4 Q2–Q3 — Armijo T/F 与二次型试步

- **题目**: backtracking 非最大可接受步; 驻点≠全局极小; $\phi(\alpha)=4-40\alpha+112\alpha^2$ 试步计算.
- **思路**: 几何试步序列; $1-\cos t$; 可接受区间 $0<\alpha\le 5(1-c_A)/14$.
- **来源**: Tut4
