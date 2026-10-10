# Assignment 1 — 解答

- **来源**: `assignment/Assignment01.pdf`
- **课程**: MATH3900, Lexiao Lai
- **说明**: 按题、按小问分开的完整解答; 交稿前自行核对表述与计算. 范数默认可欧氏范数.

---

## 1. True / False

### (a)

**题意**: 是否每个有下界的 $C^1$ 函数 $f:\mathbb{R}\to\mathbb{R}$ 都有全局极小点.

**解答**: **False**. 反例取 $f(x)=e^{x}$. 则 $f'(x)=e^{x}$ 连续, 故 $f\in C^1(\mathbb{R})$. 又 $f(x)>0$ 对一切 $x$, 故有下界 (例如 $0$). 但 $\inf_x f(x)=0$ 不可达: 若存在 $x^\star$ 使 $f(x^\star)=0$, 则 $e^{x^\star}=0$, 不可能. 故无全局极小点.

**结论**: False; 反例 $e^{x}$.

---

### (b)

**题意**: 若可微 $f:\mathbb{R}^d\to\mathbb{R}$ 在两点 $u\neq v$ 满足 $\nabla f(u)=\nabla f(v)$, 则 $f$ 不可能强凸.

**解答**: **True**. 设 $f$ 为 $\mu$-强凸 ($\mu>0$). 则可微强凸给出梯度强单调:
$$
\bigl(\nabla f(u)-\nabla f(v)\bigr)^T(u-v)\ge\mu\|u-v\|^2.
$$
代入 $\nabla f(u)=\nabla f(v)$ 得左边 $=0$, 右边 $=\mu\|u-v\|^2>0$ (因 $u\neq v$), 矛盾. 故 $f$ 不可能强凸.

**结论**: True.

---

### (c)

**题意**: $C^2$ 凸函数若有唯一全局极小, 是否必对某 $\mu>0$ 强凸.

**解答**: **False**. 反例取 $f(t)=t^4$. 则 $f''(t)=12t^2\ge 0$, 故 $f$ 凸且 $C^2$. 又 $f(t)\ge 0=f(0)$, 且仅当 $t=0$ 时等号, 故 $0$ 为唯一全局极小.

若 $f$ 对某 $\mu>0$ $\mu$-强凸, 则 $f(t)-\frac\mu2 t^2$ 凸, 从而其二阶导 $\ge 0$:
$$
f''(t)-\mu=12t^2-\mu\ge 0\quad\forall t,
$$
在 $t=0$ 得 $-\mu\ge 0$, 与 $\mu>0$ 矛盾. 故非强凸.

**结论**: False; 反例 $t^4$.

---

### (d)

**题意**: 凸函数若有两个不同全局极小 $u,v$, 则连线上每点也是全局极小.

**解答**: **True**. 设 $f(u)=f(v)=f^\star:=\inf f$. 对任意 $\theta\in[0,1]$, 令 $w=\theta u+(1-\theta)v$. 由凸性
$$
f(w)\le\theta f(u)+(1-\theta)f(v)=f^\star.
$$
又 $f^\star$ 为下界, 故 $f(w)\ge f^\star$. 于是 $f(w)=f^\star$, 即 $w$ 亦为全局极小.

**结论**: True.

---

### (e)

**题意**: $C^1$ 且 $\nabla f(x)\neq 0$ 是否必有 $f\bigl(x-\nabla f(x)\bigr)<f(x)$ (满步长 $1$).

**解答**: **False**. 反例取一元 $f(t)=t^4$, 在 $x=1$: $f'(1)=4\neq 0$,
$$
f\bigl(1-f'(1)\bigr)=f(1-4)=f(-3)=81,\qquad f(1)=1.
$$
故 $f(x-\nabla f(x))=81>1=f(x)$. (下降方向只保证**充分小**步长下降, 不保证步长 $1$.)

**结论**: False; 反例 $t^4$ 在 $t=1$.

---

## 2. 驻点分类

设
$$
f(x_1,x_2)=\frac14 x_1^4-\frac12 x_1^2+\frac12 x_2^2.
$$

### (a)

**题意**: 求 $\nabla f$, $\nabla^2 f$ 及全部驻点.

**解答**: 逐分量求导:
$$
\partial_1 f=x_1^3-x_1,\qquad \partial_2 f=x_2.
$$
故
$$
\nabla f(x)=\begin{pmatrix}x_1^3-x_1\\ x_2\end{pmatrix}.
$$
再求导:
$$
\nabla^2 f(x)=\begin{pmatrix}3x_1^2-1&0\\ 0&1\end{pmatrix}.
$$
令 $\nabla f=0$: $x_2=0$ 且 $x_1^3-x_1=x_1(x_1^2-1)=0$, 故 $x_1\in\{0,1,-1\}$. 驻点为
$$
(0,0),\quad (1,0),\quad (-1,0).
$$

**结论**: $\nabla f=(x_1^3-x_1,\,x_2)^T$, $\nabla^2 f=\mathrm{diag}(3x_1^2-1,\,1)$; 驻点 $(0,0),(\pm 1,0)$.

---

### (b)

**题意**: 分类各驻点; 求全部全局极小与最小值.

**解答**:

在 $(\pm 1,0)$: $\nabla^2 f=\mathrm{diag}(2,1)\succ 0$, 且梯度为 $0$, 由二阶充分条件得**严格局部极小**. 函数值
$$
f(\pm 1,0)=\frac14-\frac12=-\frac14.
$$

在 $(0,0)$: $\nabla^2 f=\mathrm{diag}(-1,1)$. 二次型对 $e_1=(1,0)$ 为 $-1<0$, 对 $e_2=(0,1)$ 为 $1>0$, 故海森**不定**, 既非局部极小也非局部极大 (鞍点). 更直接: 对充分小 $t\neq 0$,
$$
f(t,0)=\frac14 t^4-\frac12 t^2=t^2\Bigl(\frac14 t^2-\frac12\Bigr)<0=f(0,0)\quad(|t|<\sqrt 2),
$$
$$
f(0,t)=\frac12 t^2>0=f(0,0).
$$

全局: 配方
$$
f(x)=\frac14\bigl(x_1^2-1\bigr)^2-\frac14+\frac12 x_2^2\ge -\frac14,
$$
等号当且仅当 $x_1^2=1$ 且 $x_2=0$, 即 $x=(\pm 1,0)$. 故全局极小点恰为这两点, 最小值为 $-\frac14$.

**结论**: $(\pm 1,0)$ 严格局部 (且全局) 极小; $(0,0)$ 非局部极值; 最小值 $-\frac14$.

---

### (c)

**题意**: $h(x_1,x_2)=x_1^4-x_2^4$ 在原点的梯度, 海森, 是否局部极值.

**解答**:
$$
\nabla h(x)=\begin{pmatrix}4x_1^3\\ -4x_2^3\end{pmatrix},\qquad
\nabla^2 h(x)=\begin{pmatrix}12x_1^2&0\\ 0&-12x_2^2\end{pmatrix}.
$$
在原点: $\nabla h(0)=0$, $\nabla^2 h(0)=0$. 海森检验失效.

对任意 $\delta>0$, 取 $0<t<\delta$:
$$
h\bigl(t(1,0)\bigr)=t^4>0=h(0),\qquad
h\bigl(t(0,1)\bigr)=-t^4<0=h(0).
$$
故任意邻域内既有更大值也有更小值, 原点既非局部极小也非局部极大.

**结论**: $\nabla h(0)=0$, $\nabla^2 h(0)=0$; 原点非局部极值.

---

## 3. Ridge 型目标

$n=d=2$, $a_1=(1,1)^T$, $y_1=1$, $a_2=(2,2)^T$, $y_2=2$,
$$
f_\lambda(x)=\frac1{4}\sum_{i=1}^2(a_i^Tx-y_i)^2+\frac\lambda2\|x\|^2.
$$

### (a)

**题意**: 写出 $f_\lambda$ 关于 $x_1,x_2$ 的显式, 以及梯度与海森.

**解答**: $a_1^Tx=x_1+x_2$, $a_2^Tx=2x_1+2x_2$, 故
$$
a_1^Tx-y_1=x_1+x_2-1,\qquad
a_2^Tx-y_2=2(x_1+x_2-1).
$$
$$
\sum_{i=1}^2(a_i^Tx-y_i)^2=(1+4)(x_1+x_2-1)^2=5(x_1+x_2-1)^2.
$$
因此
$$
f_\lambda(x)=\frac54(x_1+x_2-1)^2+\frac\lambda2(x_1^2+x_2^2).
$$
记 $s=x_1+x_2-1$. 则
$$
\nabla f_\lambda(x)=\frac52 s\begin{pmatrix}1\\1\end{pmatrix}+\lambda\begin{pmatrix}x_1\\x_2\end{pmatrix}
=\begin{pmatrix}\tfrac52(x_1+x_2-1)+\lambda x_1\\ \tfrac52(x_1+x_2-1)+\lambda x_2\end{pmatrix},
$$
$$
\nabla^2 f_\lambda(x)=\frac52\begin{pmatrix}1&1\\1&1\end{pmatrix}+\lambda I
=\begin{pmatrix}\lambda+\tfrac52&\tfrac52\\ \tfrac52&\lambda+\tfrac52\end{pmatrix}.
$$

**结论**: 上式.

---

### (b)

**题意**: 对哪些 $\lambda$ 凸 / 强凸; 强凸时给 $\mu,L,\kappa$.

**解答**: 矩阵 $\begin{pmatrix}1&1\\1&1\end{pmatrix}$ 特征值 $0,2$ (特征向量 $(1,-1)$, $(1,1)$). 故
$$
\nabla^2 f_\lambda=\frac52\begin{pmatrix}1&1\\1&1\end{pmatrix}+\lambda I
$$
的特征值为 $\lambda$ 与 $\lambda+5$.

- **凸** $\Leftrightarrow$ $\nabla^2 f_\lambda\succeq 0$ $\Leftrightarrow$ $\lambda\ge 0$.
- **强凸** $\Leftrightarrow$ $\nabla^2 f_\lambda\succeq\mu I$ 对某 $\mu>0$ $\Leftrightarrow$ $\lambda>0$. 此时可取
  $$
  \mu=\lambda,\qquad L=\lambda+5,\qquad \kappa=\frac L\mu=1+\frac5\lambda.
  $$
  (因 $\mu I\preceq\nabla^2 f_\lambda\preceq LI$ 当 $\mu=\lambda_{\min}$, $L=\lambda_{\max}$.)

**结论**: $\lambda\ge 0$ 凸; $\lambda>0$ 强凸, $\mu=\lambda$, $L=\lambda+5$, $\kappa=1+5/\lambda$.

---

### (c)

**题意**: 各 $\lambda$ 是否有全局极小, 是否唯一; $\lambda=1$ 时最小值.

**解答**:

**情形 $\lambda>0$**. $f_\lambda$ 强凸 $\Rightarrow$ 存在唯一全局极小, 由 $\nabla f_\lambda(x)=0$ 刻画. 由
$$
\frac52(x_1+x_2-1)+\lambda x_1=0,\qquad
\frac52(x_1+x_2-1)+\lambda x_2=0
$$
两式相减得 $\lambda(x_1-x_2)=0\Rightarrow x_1=x_2$. 代回:
$$
\frac52(2x_1-1)+\lambda x_1=0\Rightarrow x_1=\frac{5/2}{5+\lambda}=\frac{5}{2(5+\lambda)},\quad x_2=x_1.
$$

**情形 $\lambda=0$**. $f_0(x)=\frac54(x_1+x_2-1)^2\ge 0$, 最小值 $0$, 当且仅当 $x_1+x_2=1$. 故全局极小点为整条直线 $\{x:x_1+x_2=1\}$, **不唯一**.

**情形 $\lambda<0$**. 沿方向 $v=(1,-1)^T$ (对应特征值 $\lambda<0$),
$$
v^T\nabla^2 f_\lambda\, v=\lambda\|v\|^2<0,
$$
故 $f_\lambda$ 在该方向无下界: 取 $x=tv$, $t\to\infty$ 时 $f_\lambda(x)\to-\infty$. **无全局极小**.

**$\lambda=1$**: 唯一极小点
$$
x^\star=\Bigl(\frac{5}{2\cdot 6},\,\frac{5}{12}\Bigr)^T=\Bigl(\frac{5}{12},\,\frac{5}{12}\Bigr)^T.
$$
$$
s=\frac{5}{12}+\frac{5}{12}-1=-\frac16,
$$
$$
f_1(x^\star)=\frac54\cdot\frac1{36}+\frac12\Bigl(2\cdot\frac{25}{144}\Bigr)=\frac{5}{144}+\frac{25}{144}=\frac{30}{144}=\frac{5}{24}.
$$

**结论**: $\lambda>0$ 唯一极小 $x_1=x_2=5/(2(5+\lambda))$; $\lambda=0$ 极小集为 $x_1+x_2=1$; $\lambda<0$ 无极小; $\lambda=1$ 时最小值为 $5/24$.

---

## 4. 一维梯度下降

$f(t)=\dfrac{t^4}{4}+\dfrac{t^2}{2}$, $t_{k+1}=t_k-\alpha f'(t_k)$.

### (a)

**题意**: $f',f''$; 全局极小; 是否强凸; 梯度是否全局 $L$-Lipschitz.

**解答**:
$$
f'(t)=t^3+t=t(t^2+1),\qquad f''(t)=3t^2+1.
$$
$f'(t)=0\Leftrightarrow t=0$ (因 $t^2+1>0$). 又 $f''(t)\ge 1>0$, 故 $0$ 为严格局部极小; 且 $f(t)\ge 0=f(0)$, 故 **唯一全局极小** 为 $t=0$.

由 $f''(t)\ge 1$, 知 $f$ 在 $\mathbb{R}$ 上 **$1$-强凸** (可取 $\mu=1$).

梯度全局 Lipschitz? 若存在 $L$ 使 $|f'(u)-f'(v)|\le L|u-v|$ $\forall u,v$, 则
$$
\biggl|\frac{f'(u)-f'(v)}{u-v}\biggr|=|u^2+uv+v^2+1|
$$
在 $|u|,|v|\to\infty$ 时可任意大, 矛盾. 故 **不存在** 有限的全局 $L$.

**结论**: $f'=t^3+t$, $f''=3t^2+1$; 唯一全局极小 $0$; $\mu=1$ 强凸; 梯度非全局 Lipschitz.

---

### (b)

**题意**: $t_0=1$, $\alpha=1/4$ 算 $t_1,t_2$; 求使 $f(t_1)<f(t_0)$ 的全部 $\alpha>0$.

**解答**: $f'(1)=2$. $\alpha=1/4$ 时
$$
t_1=1-\frac14\cdot 2=\frac12,
$$
$$
t_2=\frac12-\frac14\Bigl(\Bigl(\frac12\Bigr)^3+\frac12\Bigr)=\frac12-\frac14\cdot\frac58=\frac12-\frac5{32}=\frac{11}{32}.
$$

一般 $\alpha>0$: $t_1=1-2\alpha$. 需 $f(1-2\alpha)<f(1)=\frac34$. 令 $s=1-2\alpha$, 即
$$
\frac{s^4}{4}+\frac{s^2}{2}<\frac34\Leftrightarrow s^4+2s^2-3<0\Leftrightarrow (s^2-1)(s^2+3)<0.
$$
因 $s^2+3>0$, 得 $s^2<1$, 即 $|1-2\alpha|<1$. 结合 $\alpha>0$:
$$
-1<1-2\alpha<1\Rightarrow 0<\alpha<1.
$$
(当 $\alpha=1$ 时 $t_1=-1$, $f(-1)=f(1)$, 不严格小于.)

**结论**: $t_1=\frac12$, $t_2=\frac{11}{32}$; 严格下降当且仅当 $0<\alpha<1$.

---

### (c)

**题意**: $\alpha=1/4$, $|t_0|\le 1$ 时证 $|t_k|\le\bigl(\frac34\bigr)^k|t_0|$, 并推出收敛到极小点.

**解答**:
$$
t_{k+1}=t_k-\frac14(t_k^3+t_k)=t_k\Bigl(1-\frac14-\frac14 t_k^2\Bigr)=t_k\Bigl(\frac34-\frac14 t_k^2\Bigr).
$$
故
$$
|t_{k+1}|=|t_k|\cdot\Bigl|\frac34-\frac14 t_k^2\Bigr|.
$$
若 $|t_k|\le 1$, 则 $\frac14 t_k^2\in[0,\frac14]$, 从而 $\frac34-\frac14 t_k^2\in\bigl[\frac12,\frac34\bigr]\subset(0,1]$, 于是
$$
|t_{k+1}|\le\frac34|t_k|\le|t_k|\le 1.
$$
由归纳: $|t_0|\le 1\Rightarrow$ 全体 $|t_k|\le 1$, 且
$$
|t_{k+1}|\le\frac34|t_k|\Rightarrow |t_k|\le\Bigl(\frac34\Bigr)^k|t_0|.
$$
右边 $\to 0$, 故 $t_k\to 0$, 即收敛到唯一全局极小点.

**结论**: $|t_k|\le(3/4)^k|t_0|\to 0$.

---

## 5. Sign 梯度下降

记 $g=\nabla f(x)$, $\mathrm{sign}$ 分量作用; $\|v\|_1=\sum_i|v_i|$, $\|v\|_\infty=\max_i|v_i|$.

### (a)

**题意**: 解 $\min_{\|p\|_\infty\le 1} g^Tp$; 最优值与最优方向; $\nabla f(x)\neq 0$ 时是否皆为下降方向.

**解答**:
$$
g^Tp=\sum_{i=1}^d g_i p_i,\qquad |p_i|\le 1.
$$
各项独立: 要使 $g_ip_i$ 最小, 取 $p_i=-\mathrm{sign}(g_i)$ (若 $g_i=0$ 则 $p_i\in[-1,1]$ 任意). 最小值为
$$
\sum_i g_i\bigl(-\mathrm{sign}(g_i)\bigr)=-\sum_i|g_i|=-\|g\|_1.
$$
最优方向集: $p_i=-\mathrm{sign}(g_i)$ 对所有 $g_i\neq 0$; 对 $g_i=0$ 可任意取 $[-1,1]$.

若 $g\neq 0$, 则对任一最优 $p$,
$$
g^Tp=-\|g\|_1<0,
$$
故 $p$ 为下降方向.

**结论**: 最小值 $-\|\nabla f(x)\|_1$; 最优 $p=-\mathrm{sign}(\nabla f(x))$ (零分量任意); $g\neq 0$ 时均为下降方向.

---

### (b)

**题意**: $\phi(t)=t^2/2$, $t_{k+1}=t_k-\eta\mathrm{sign}(\phi'(t_k))$, $t_0=\eta/2$; 是否收敛到极小.

**解答**: $\phi'(t)=t$, 唯一极小在 $0$. $t_0=\eta/2>0$ (设 $\eta>0$), 则 $\mathrm{sign}(\phi'(t_0))=1$,
$$
t_1=\frac\eta2-\eta=-\frac\eta2.
$$
$\mathrm{sign}(\phi'(t_1))=-1$,
$$
t_2=-\frac\eta2-\eta(-1)=\frac\eta2=t_0.
$$
序列在 $\{\eta/2,\,-\eta/2\}$ 上周期振荡, **不**趋于 $0$.

**结论**: $t_1=-\eta/2$, $t_2=\eta/2$; 不收敛到极小点.

---

### (c)

**题意**: $L$-光滑时找 $\alpha=\alpha(g,L,d)\ge 0$ 使
$$
f\bigl(x-\alpha\mathrm{sign}(g)\bigr)\le f(x)-\frac{\|g\|_1^2}{2Ld},
$$
并写出算法.

**解答**: 记 $s=\mathrm{sign}(g)$. 由下降引理,
$$
f(x-\alpha s)\le f(x)-\alpha g^Ts+\frac{L\alpha^2}{2}\|s\|^2.
$$
$g^Ts=\|g\|_1$, 且 $\|s\|^2=\sum_i\mathrm{sign}(g_i)^2\le d$ (零分量贡献 $0$). 故
$$
f(x-\alpha s)\le f(x)-\alpha\|g\|_1+\frac{L d}{2}\alpha^2.
$$
取
$$
\alpha=\frac{\|g\|_1}{L d}
$$
(若 $g=0$ 则取 $\alpha=0$). 代入右边第二、三项:
$$
-\frac{\|g\|_1^2}{Ld}+\frac{Ld}{2}\cdot\frac{\|g\|_1^2}{L^2 d^2}=-\frac{\|g\|_1^2}{Ld}+\frac{\|g\|_1^2}{2Ld}=-\frac{\|g\|_1^2}{2Ld}.
$$
即得所求界.

**算法**: 任取 $x_0$; 对 $k=0,1,2,\ldots$
$$
g_k=\nabla f(x_k),\quad
\alpha_k=\frac{\|g_k\|_1}{L d},\quad
x_{k+1}=x_k-\alpha_k\,\mathrm{sign}(g_k).
$$

**结论**: $\alpha=\|\nabla f(x)\|_1/(Ld)$; 算法如上.

---

### (d)

**题意**: 再设 $\mu$-强凸 ($0<\mu\le L$), 证
$$
f(x_k)-f^\star\le\Bigl(1-\frac{\mu}{Ld}\Bigr)^k\bigl(f(x_0)-f^\star\bigr).
$$

**解答**: 由 (c), 每步
$$
f(x_{k+1})\le f(x_k)-\frac{\|g_k\|_1^2}{2Ld}.
$$
$\mu$-强凸且可微时有
$$
f(x_k)-f^\star\le\frac1{2\mu}\|g_k\|_2^2.
$$
又 $\|g_k\|_2\le\|g_k\|_1$, 故 $\|g_k\|_1^2\ge\|g_k\|_2^2\ge 2\mu\bigl(f(x_k)-f^\star\bigr)$. 代入下降:
$$
f(x_{k+1})-f^\star\le f(x_k)-f^\star-\frac{2\mu\bigl(f(x_k)-f^\star\bigr)}{2Ld}
=\Bigl(1-\frac{\mu}{Ld}\Bigr)\bigl(f(x_k)-f^\star\bigr).
$$
归纳即得结论.

**结论**: 线性收敛, 因子 $1-\mu/(Ld)$.
