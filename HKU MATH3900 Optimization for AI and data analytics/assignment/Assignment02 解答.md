# Assignment 2 — 解答

- **来源**: `assignment/Assignment02.pdf`
- **课程**: MATH3900, Lexiao Lai
- **说明**: 按题、按小问分开的完整解答; 交稿前自行核对表述与计算. 范数默认可欧氏范数及其诱导算子范数.

---

## 1. True / False

### (a)

**题意**: $f\in C^2$, $\nabla^2f(x)$ 可逆. 用 $af+b$ ($a>0$, $b\in\mathbb{R}$) 替换 $f$ 后, 在 $x$ 的 Newton 方向是否不变.

**解答**: **True**. 令 $g=\nabla f(x)$, $H=\nabla^2f(x)$. 原 Newton 方向 $p$ 满足 $Hp=-g$.

对 $\tilde f=af+b$: $\nabla\tilde f(x)=ag$, $\nabla^2\tilde f(x)=aH$. 新 Newton 方程为
$$
(aH)\tilde p=-(ag)\iff H\tilde p=-g
$$
(因 $a>0$). 由 $H$ 可逆得 $\tilde p=p$.

**结论**: True.

---

### (b)

**题意**: $f\in C^1$. 若 $\alpha^\star>0$ 在 $\alpha\ge 0$ 上极小化 $f(x+\alpha p)$, 是否必有 $\nabla f(x+\alpha^\star p)^Tp=0$.

**解答**: **True**. 令 $\phi(\alpha)=f(x+\alpha p)$ ($\alpha\ge 0$). 则 $\phi'(\alpha)=\nabla f(x+\alpha p)^Tp$. 因 $\alpha^\star>0$ 是 $[0,\infty)$ 上的极小点, 它是相对开集 $(0,\infty)$ 的内点, 故一阶必要条件给出 $\phi'(\alpha^\star)=0$, 即 $\nabla f(x+\alpha^\star p)^Tp=0$.

**结论**: True.

---

### (c)

**题意**: 固定 $f,x$ 与下降方向 $p$, 以及固定回溯参数 $\bar\alpha>0$, $c_A,\eta\in(0,1)$. 把 $p$ 换成 $sp$ ($s>0$) 后, Armijo 回溯是否产生同一下一点.

**解答**: **False**. 回溯对方向 $p$ 与 $sp$ 都从同一 $\bar\alpha$ 起试 $\bar\alpha,\bar\alpha\eta,\bar\alpha\eta^2,\ldots$. 接受步长后下一点分别为 $x+\alpha_p p$ 与 $x+\alpha_{sp}(sp)$. 二者相同当且仅当 $\alpha_{sp}=\alpha_p/s$. 但候选步长集不随 $s$ 缩放, 一般不成立.

**反例**: 取 $f(t)=\frac12 t^2$, $x=1$, $p=-1$ (即负梯度). 则 $\nabla f(1)=1$, $\nabla f^Tp=-1$. Armijo 为
$$
\frac12(1-\alpha)^2\le \frac12 - c_A\alpha.
$$
取 $\bar\alpha=1$, $\eta=\frac12$, $c_A=\frac14$. $\alpha=1$: 左边 $0$, 右边 $\frac12-\frac14=\frac14$, 成立, 故接受 $x_+=0$.

对方向 $sp=2p=-2$: Armijo 为 $\frac12(1-2\alpha)^2\le\frac12-c_A\alpha\cdot(-2)\cdot?$ 仔细: $\nabla f^T(sp)=1\cdot(-2)=-2$, 试 $\alpha=1$:
$$
f(1-2)=\frac12\cdot 4=2,\qquad f(1)+c_A\cdot 1\cdot(-2)=\frac12-\frac12=0.
$$
$2\le 0$ 不成立. $\alpha=\frac12$: $f(1-1)=0$, 右边 $\frac12+c_A\cdot\frac12\cdot(-2)=\frac12-\frac14=\frac14$, $0\le\frac14$ 成立, 接受 $x_+=0$. 本例碰巧同点.

再取 $s=\frac12$, 方向 $p'=-\frac12$. 试 $\alpha=1$: 点 $1-\frac12=\frac12$, $f=\frac18$; 右边 $\frac12+c_A\cdot 1\cdot\bigl(1\cdot(-\frac12)\bigr)=\frac12-\frac18=\frac38$. $\frac18\le\frac38$ 成立, 接受 $x_+=\frac12\neq 0$.

故把 $p$ 换成 $\frac12 p$ 后下一点不同.

**结论**: False; 反例 $f(t)=\frac12 t^2$, $x=1$, $p=-1$, $s=\frac12$, $\bar\alpha=1$, $c_A=\frac14$, $\eta=\frac12$.

---

### (d)

**题意**: $f$ 有下界且 $L$-光滑. 若 GD 更新 $x_{k+1}=x_k-\alpha_k\nabla f(x_k)$ 均对同一 $c_A\in(0,1)$ 与**某个** $\alpha_k>0$ 满足 Armijo, 是否必有 $\|\nabla f(x_k)\|\to 0$.

**解答**: **False**. Armijo 对充分小的正步长在下降方向上总成立, 但若 $\alpha_k$ 选得过小, 函数下降可平方可和而梯度不必趋于 $0$.

**反例**: 取 $f(t)=\frac12 t^2$ (有下界, $L=1$-光滑), $c_A=\frac14$. 令 $t_0=1$,
$$
\alpha_k=\min\Bigl\{\frac{2(1-c_A)}{L},\ \frac{1}{(k+1)^2}\Bigr\}=\frac{1}{(k+1)^2}
$$
(对一切 $k\ge 0$ 有 $\frac{1}{(k+1)^2}\le\frac32$). 沿 $p_k=-f'(t_k)=-t_k$, Armijo 在 $\alpha\in\bigl(0,\frac{2(1-c_A)}{L}\bigr]$ 上成立, 故所选 $\alpha_k$ 合法. 迭代
$$
t_{k+1}=t_k\bigl(1-\alpha_k\bigr)=t_k\Bigl(1-\frac{1}{(k+1)^2}\Bigr).
$$
于是
$$
t_k=t_0\prod_{j=0}^{k-1}\Bigl(1-\frac{1}{(j+1)^2}\Bigr).
$$
因 $\sum\frac{1}{(j+1)^2}<\infty$, 无穷乘积 $\prod(1-\frac{1}{(j+1)^2})$ 收敛到**严格正**的极限 (对大 $j$ 有 $1-\frac{1}{(j+1)^2}>0$, 且 $\sum\log(1-\frac{1}{(j+1)^2})$ 收敛). 故 $t_k\to t_\infty\neq 0$, 从而 $|f'(t_k)|=|t_k|\not\to 0$.

**结论**: False; 反例如上 (步长无一致正下界时 Armijo 不足以迫使梯度 $\to 0$; 课堂回溯从固定 $\bar\alpha$ 起才给出步长下界).

---

### (e)

**题意**: $f\in C^2(\mathbb{R})$, $f''(t)>0$ 处处, 有全局极小 $t^\star$. 若从任意 $t_0$ 做一步满 Newton 都到 $t^\star$, 则 $f$ 是否必为二次函数.

**解答**: **True**. 满 Newton 更新为
$$
t-\frac{f'(t)}{f''(t)}=t^\star\qquad\forall t\in\mathbb{R},
$$
即 $f'(t)=f''(t)\,(t-t^\star)$. 两边对 $t$ 求导 ($f\in C^2$ 且 $f''>0$, 实际上由等式知 $f'$ 可微且 $f'''$ 存在于古典意义下若再设 $C^3$; 或对等式两边在分布/差商意义下): 若假定 $f\in C^3$ (由 $f''>0$ 连续且等式可推出所需光滑; 作业情境下可对等式微分),
$$
f''(t)=f'''(t)(t-t^\star)+f''(t)\implies f'''(t)(t-t^\star)=0\quad\forall t.
$$
故对一切 $t\neq t^\star$ 有 $f'''(t)=0$, 由连续性 $f'''\equiv 0$, 从而 $f$ 为二次多项式. 又 $f''>0$ 故为首正二次.

(不显式用 $C^3$: 由 $f'(t)=f''(t)(t-t^\star)$ 与 $f''>0$, 令 $u=f''>0$, 则 $f'(t)=u(t)(t-t^\star)$. 再微分一次在差商意义下同样得 $u$ 为常数.)

**结论**: True.

---

## 2. $f(t)=\sqrt{1+t^2}$

### (a)

**题意**: 求 $f',f''$, 全局极小, 以及满 Newton 更新公式.

**解答**:
$$
f'(t)=\frac{t}{\sqrt{1+t^2}},\qquad
f''(t)=\frac{1}{(1+t^2)^{3/2}}.
$$
因 $f'(t)=0\iff t=0$, 且 $f''(0)=1>0$ (或 $f(t)\ge f(0)=1$), 故全局极小为 $t^\star=0$.

Newton 方向 $p=-f'/f''=-t(1+t^2)$, 满步更新
$$
t_+=t+p=t-t(1+t^2)=-t^3.
$$

**结论**: $f',f''$ 如上; $t^\star=0$; $t_{k+1}=-t_k^3$.

---

### (b)

**题意**: $t_0=2$, Newton 方向 + Armijo 回溯 $\bar\alpha=1$, $\eta=\frac12$, $c_A=\frac14$. 逐试记录并给出 $t_1,t_2$.

**解答**: Armijo: $f(t+\alpha p)\le f(t)+c_A\alpha f'(t)p$, 其中 $p=-f'(t)/f''(t)$.

**迭代 0** ($t_0=2$): $f(2)=\sqrt5$, $f'(2)=\frac{2}{\sqrt5}$, $f''(2)=5^{-3/2}$, $p=-10$. 线性预测项 $f'p=-\frac{2}{\sqrt5}\cdot 10=-4\sqrt5$.

| 试探 $\alpha$ | $t+\alpha p$ | $f(\cdot)$ | Armijo 右端 $f+c_A\alpha f'p$ | 是否接受 |
|---|---|---|---|---|
| $1$ | $-8$ | $\sqrt{65}\approx 8.062$ | $\sqrt5+c_A(-4\sqrt5)=0$ | 否 |
| $1/2$ | $-3$ | $\sqrt{10}\approx 3.162$ | $\sqrt5+\frac14\cdot\frac12\cdot(-4\sqrt5)=\sqrt5-\frac12\sqrt5=\frac12\sqrt5\approx 1.118$ | 否 |
| $1/4$ | $-0.5$ | $\sqrt{5/4}=\sqrt5/2\approx 1.118$ | $\sqrt5+\frac14\cdot\frac14\cdot(-4\sqrt5)=\sqrt5-\frac14\sqrt5=\frac34\sqrt5\approx 1.677$ | 是 |

故 $t_1=-\frac12$.

**迭代 1** ($t_1=-\frac12$): $f(t_1)=\sqrt{5}/2$, $f'(t_1)=-\frac{1/2}{\sqrt{5}/2}=-\frac{1}{\sqrt5}$, $f''(t_1)=(5/4)^{-3/2}=\frac{8}{5\sqrt5}$,
$$
p=-\frac{f'}{f''}=\frac{1/\sqrt5}{8/(5\sqrt5)}=\frac58=0.625.
$$
满 Newton 点: $-\frac12+\frac58=\frac18$. 试 $\alpha=1$:
$$
f(t_1+p)=f\Bigl(\frac18\Bigr)=\sqrt{1+\frac{1}{64}}=\sqrt{\frac{65}{64}}\approx 1.0078,
$$
右端 $f(t_1)+c_A\cdot 1\cdot f'p$. 计算 $f'p=\bigl(-\frac{1}{\sqrt5}\bigr)\cdot\frac58=-\frac{1}{\sqrt5}\cdot\frac58$, 而 $f(t_1)=\sqrt5/2$,
$$
\text{RHS}=\frac{\sqrt5}{2}+\frac14\Bigl(-\frac{5}{8\sqrt5}\Bigr)=\frac{\sqrt5}{2}-\frac{5}{32\sqrt5}=\frac{16\cdot 5-5}{32\sqrt5}=\frac{75}{32\sqrt5}\approx 1.048.
$$
$1.0078\le 1.048$, 接受. 故 $t_2=\frac18$.

**结论**: $t_1=-\frac12$, $t_2=\frac18$; 试探表见上.

---

### (c)

**题意**: 满 Newton $t_{k+1}=-t_k^3$ 的收敛行为; 对 $0<|t_0|<1$ 求阶 $q>1$ 与极限比.

**解答**: $|t_{k+1}|=|t_k|^3$.

- 若 $|t_0|<1$, 则 $|t_k|=|t_0|^{3^k}\to 0$, 故 $t_k\to t^\star=0$.
- 若 $|t_0|=1$, 则 $t_k=(-1)^{3^k}t_0$ 在 $\{\pm 1\}$ 上 (实际上 $t_{k+1}=-t_k$, 在 $\pm 1$ 间振荡), 不收敛到 $0$.
- 若 $|t_0|>1$, 则 $|t_k|\to\infty$.

对 $0<|t_0|<1$: 取 $q=3$,
$$
\frac{|t_{k+1}|}{|t_k|^3}=1\qquad\forall k,
$$
故极限为 $1$ (有限且严格正).

**结论**: 仅当 $|t_0|<1$ 收敛到 $0$; $|t_0|=1$ 振荡; $|t_0|>1$ 发散; $q=3$, 极限比 $=1$.

---

## 3. 四次扰动与 Newton 仿射不变性

令 $u=x_1+x_2$. 直接计算:
$$
\nabla f(x)=\begin{pmatrix}2x_1+x_2+u^3\\ x_1+2x_2+u^3\end{pmatrix},\qquad
\nabla^2f(x)=\begin{pmatrix}2+3u^2&1+3u^2\\ 1+3u^2&2+3u^2\end{pmatrix}.
$$

### (a)

**题意**: 在 $x^{(0)}=(1,0)^T$ 算梯度, Hessian, 满 Newton 一步.

**解答**: $u=1$, $\nabla f(x^{(0)})=(3,2)^T$,
$$
\nabla^2f(x^{(0)})=\begin{pmatrix}5&4\\4&5\end{pmatrix}.
$$
解 $\nabla^2f\,p=-\nabla f$:
$$
\begin{pmatrix}5&4\\4&5\end{pmatrix}p=\begin{pmatrix}-3\\-2\end{pmatrix}.
$$
第一式 $\times 5$ 减第二式 $\times 4$:
$$
(25-16)p_1=-15+8\implies 9p_1=-7\implies p_1=-\frac79.
$$
代入第二式: $4(-\frac79)+5p_2=-2\implies 5p_2=\frac{10}{9}\implies p_2=\frac{2}{9}$.
验证: $5(-\frac79)+4(\frac29)=-3$, $4(-\frac79)+5(\frac29)=-2$.

故
$$
x^{(1)}=x^{(0)}+p=\Bigl(1-\frac79,\ \frac29\Bigr)=\Bigl(\frac29,\frac29\Bigr).
$$

**结论**: $\nabla f=(3,2)^T$, $H=\begin{pmatrix}5&4\\4&5\end{pmatrix}$, $x^{(1)}=\bigl(\frac29,\frac29\bigr)^T$.

---

### (b)

**题意**: $u=x_1+x_2$, $v=x_1-x_2$, $F(u,v)=f\bigl(\frac{u+v}{2},\frac{u-v}{2}\bigr)$. 写 $F$, 对 $F$ 做满 Newton 再映回 $x$.

**解答**: $x_1=\frac{u+v}{2}$, $x_2=\frac{u-v}{2}$. 则
$$
x_1^2+x_2^2+x_1x_2=\frac{(u+v)^2+(u-v)^2+(u^2-v^2)}{4}=\frac{3u^2+v^2}{4},
$$
故
$$
F(u,v)=\frac34 u^2+\frac14 v^2+\frac14 u^4.
$$
对应 $x^{(0)}=(1,0)$: $u=1$, $v=1$.
$$
\nabla F=\begin{pmatrix}\frac32 u+u^3\\ \frac12 v\end{pmatrix},\qquad
\nabla^2F=\begin{pmatrix}\frac32+3u^2&0\\ 0&\frac12\end{pmatrix}.
$$
在 $(1,1)$: $\nabla F=(2.5,\ 0.5)^T$, $\nabla^2F=\mathrm{diag}(4.5,\ 0.5)$. Newton:
$$
p_u=-\frac{2.5}{4.5}=-\frac59,\quad p_v=-\frac{0.5}{0.5}=-1,
$$
$$
(u_+,v_+)=\Bigl(1-\frac59,\ 0\Bigr)=\Bigl(\frac49,\ 0\Bigr).
$$
映回
$$
x_+=\Bigl(\frac{u_++v_+}{2},\frac{u_+-v_+}{2}\Bigr)=\Bigl(\frac29,\frac29\Bigr),
$$
与 (a) 相同.

**结论**: $F=\frac34 u^2+\frac14 v^2+\frac14 u^4$; Newton 后 $(u,v)=(\frac49,0)$, 对应 $x=(\frac29,\frac29)$.

---

### (c)

**题意**: $F(z)=f(Az+b)$, $A$ 可逆, 在对应点 $x=Az+b$ 且 $\nabla^2f(x)$ 可逆时, 证满 Newton 满足 $x_+=Az_++b$.

**解答**: 链式法则:
$$
\nabla F(z)=A^T\nabla f(x),\qquad \nabla^2F(z)=A^T\nabla^2f(x)\,A.
$$
$F$ 的 Newton 步 $p_z$ 满足 $\nabla^2F(z)p_z=-\nabla F(z)$, 即
$$
A^T\nabla^2f(x)\,A\,p_z=-A^T\nabla f(x).
$$
因 $A^T$ 可逆, 等价于 $\nabla^2f(x)\,(Ap_z)=-\nabla f(x)$. 故 $p_x:=Ap_z$ 恰为 $f$ 在 $x$ 的 Newton 方向. 于是
$$
z_+=z+p_z,\qquad x_+=x+p_x=Az+b+Ap_z=A(z+p_z)+b=Az_++b.
$$

**结论**: 已证 $x_+=Az_++b$.

---

## 4. 角条件方向 + 回溯

设非驻点处 $p_k$ 满足
$$
-\nabla f(x_k)^Tp_k\ge a\|\nabla f(x_k)\|\,\|p_k\|,\qquad \|p_k\|\ge b\|\nabla f(x_k)\|,
$$
并用课堂 **Descent method with backtracking** ($\varepsilon=0$; 参数 $\bar\alpha,c_A,\eta$). 驻点后保持不动.

记 $g_k=\nabla f(x_k)$. 由 $L$-光滑下降引理, 对任意 $\alpha>0$,
$$
f(x_k+\alpha p_k)\le f(x_k)+\alpha g_k^Tp_k+\frac{L}{2}\alpha^2\|p_k\|^2.
$$
要推出 Armijo $f(x_k+\alpha p_k)\le f(x_k)+c_A\alpha g_k^Tp_k$, 只需
$$
\alpha g_k^Tp_k+\frac{L}{2}\alpha^2\|p_k\|^2\le c_A\alpha g_k^Tp_k,
$$
即 (因 $g_k^Tp_k<0$)
$$
\frac{L}{2}\alpha\|p_k\|^2\le (c_A-1)g_k^Tp_k=(1-c_A)(-g_k^Tp_k).
$$
用角条件 $-g_k^Tp_k\ge a\|g_k\|\|p_k\|$:
$$
\alpha\le\frac{2(1-c_A)(-g_k^Tp_k)}{L\|p_k\|^2}\le\frac{2(1-c_A)a\|g_k\|}{L\|p_k\|}.
$$
更紧地写出**充分**条件: 若
$$
0<\alpha\le\frac{2(1-c_A)a\|g_k\|}{L\|p_k\|},
$$
则 Armijo 成立. 再由 $\|p_k\|\ge b\|g_k\|$ 得 $\|g_k\|/\|p_k\|\le 1/b$, 但下界步长要用 $\|p_k\|$ 的上控? 实际上标准写法: 由 $-g^Tp\ge a\|g\|\|p\|$,
$$
\frac{-g^Tp}{\|p\|^2}\ge a\frac{\|g\|}{\|p\|}\ge a\cdot ? 
$$
我们有 $\|p\|\ge b\|g\|$ 给出 $\|g\|/\|p\|\le 1/b$, 这是上界不是下界. 对角条件充分下降需要 $\|g\|/\|p\|$ 的**下界**. 由角条件与 Cauchy:
$$
a\|g\|\|p\|\le -g^Tp\le \|g\|\|p\|\implies a\le 1,
$$
且 $\|p\|$ 可以很大. 若只有 $\|p\|\ge b\|g\|$ 而无上界, $\alpha$ 的充分条件 $\frac{2(1-c_A)a\|g\|}{L\|p\|}$ 可能很小.

回溯仍从 $\bar\alpha$ 起. 接受的 $\alpha_k$ 满足: 要么 $\alpha_k=\bar\alpha$, 要么前一试探 $\alpha_k/\eta$ 失败. 失败意味着
$$
\frac{\alpha_k}{\eta}>\frac{2(1-c_A)(-g_k^Tp_k)}{L\|p_k\|^2},
$$
从而
$$
\alpha_k>\eta\cdot\frac{2(1-c_A)(-g_k^Tp_k)}{L\|p_k\|^2}\ge\eta\cdot\frac{2(1-c_A)a\|g_k\|}{L\|p_k\|}.
$$
因此
$$
\alpha_k\ge\min\Bigl\{\bar\alpha,\ \eta\cdot\frac{2(1-c_A)a\|g_k\|}{L\|p_k\|}\Bigr\}.
$$

### (a)

**题意**: 找 $\delta>0$ (只依赖 $a,b,L,\bar\alpha,c_A,\eta$) 使 $\|x_{k+1}-x_k\|\ge\delta\|g_k\|$.

**解答**: $\|x_{k+1}-x_k\|=\alpha_k\|p_k\|$. 需要处理 $\|p_k\|$ 可能很大导致中间项变小的问题. 用
$$
\alpha_k\|p_k\|\ge\min\Bigl\{\bar\alpha\|p_k\|,\ \eta\cdot\frac{2(1-c_A)a\|g_k\|}{L}\Bigr\}.
$$
第一支: $\bar\alpha\|p_k\|\ge\bar\alpha b\|g_k\|$. 第二支已是 $\|g_k\|$ 的倍数. 故
$$
\|x_{k+1}-x_k\|\ge\min\Bigl\{\bar\alpha b,\ \eta\cdot\frac{2(1-c_A)a}{L}\Bigr\}\|g_k\|.
$$
取
$$
\delta:=\min\Bigl\{\bar\alpha b,\ \frac{2\eta(1-c_A)a}{L}\Bigr\}>0.
$$

**结论**: $\delta=\min\bigl\{\bar\alpha b,\ \frac{2\eta(1-c_A)a}{L}\bigr\}$.

---

### (b)

**题意**: 找 $C>0$ 使 $f(x_{k+1})\le f(x_k)-C\|g_k\|^2$.

**解答**: Armijo 与角条件:
$$
f(x_{k+1})\le f(x_k)+c_A\alpha_k g_k^Tp_k=f(x_k)-c_A\alpha_k(-g_k^Tp_k)\le f(x_k)-c_A\alpha_k a\|g_k\|\|p_k\|.
$$
而 $\alpha_k\|p_k\|\ge\delta\|g_k\|$ (由 (a)), 故
$$
f(x_{k+1})\le f(x_k)-c_A a\delta\|g_k\|^2.
$$
取 $C:=c_A a\delta>0$.

**结论**: $C=c_A a\delta$, $\delta$ 同 (a).

---

### (c)

**题意**: 另设 $f$ 为 $\mu$-强凸 ($0<\mu\le L$), $x^\star$ 为极小. 找 $q\in(0,1)$ 使 $f(x_k)-f(x^\star)\le q^k\bigl(f(x_0)-f(x^\star)\bigr)$, 并推 $x_k\to x^\star$.

**解答**: 强凸给出 $\|g_k\|^2\ge 2\mu\bigl(f(x_k)-f(x^\star)\bigr)$ (标准间隙界: $f(x)-f^\star\le\frac{1}{2\mu}\|g(x)\|^2$ 的逆形式来自 $\mu$-强凸 + 可微; 等价常用 $\|g\|^2\ge 2\mu(f-f^\star)$). 由 (b),
$$
f(x_{k+1})-f^\star\le f(x_k)-f^\star-C\|g_k\|^2\le f(x_k)-f^\star-2\mu C\bigl(f(x_k)-f^\star\bigr)
=(1-2\mu C)\bigl(f(x_k)-f^\star\bigr).
$$
需 $2\mu C<1$. 若否, 可把 $C$ 换成 $\min\{C,\frac{1}{4\mu}\}$ 仍作充分下降常数 (更小的正下降常数仍成立). 更干净: 由 $\mu\le L$ 与 $\delta\le\frac{2\eta(1-c_A)a}{L}$,
$$
2\mu C=2\mu c_A a\delta\le 2L\cdot c_A a\cdot\frac{2\eta(1-c_A)a}{L}=4\eta c_A(1-c_A)a^2\le 4\cdot 1\cdot\frac14\cdot 1=\eta\le 1? 
$$
$c_A(1-c_A)\le\frac14$, $a\le 1$, $\eta<1$, 故 $2\mu C\le\eta<1$. 于是可取
$$
q:=1-2\mu C\in(0,1).
$$
归纳得几何衰减. 又强凸 $\Rightarrow$ $f(x_k)\to f^\star\Rightarrow x_k\to x^\star$.

**结论**: $q=1-2\mu C$ ( $C$ 同 (b) ); $x_k\to x^\star$.

---

### (d)

**题意**: 改为精确线搜索 $\alpha_k\in\arg\min_{\alpha\ge 0}f(x_k+\alpha p_k)$ (假设可达). 证 (b)(c) 的结论对同一 $C,q$ 仍成立.

**解答**: 精确线搜索给出的 $\alpha_k$ 满足 $f(x_k+\alpha_k p_k)\le f(x_k+\alpha p_k)$ 对一切 $\alpha\ge 0$. 特别地, 对回溯算法会接受的那个可行 Armijo 步长 $\alpha_k^{\mathrm{BT}}$ (存在性由课堂保证),
$$
f(x_{k+1})=f(x_k+\alpha_k p_k)\le f(x_k+\alpha_k^{\mathrm{BT}}p_k)\le f(x_k)-C\|g_k\|^2,
$$
其中第二步用 (b) 对回溯步的论证. 故同一 $C$ 的充分下降成立; (c) 的 $q$ 论证原样复制.

**结论**: 已证.

---

## 5. Inexact Newton

残差 $r_k=\nabla^2f(x_k)p_k+\nabla f(x_k)$, 即 $\nabla^2f\,p_k=-\nabla f+r_k$.

### (a)

**题意**: $f(x)=\frac12 x_1^2+2x_2^2$, $x=(1,\frac14)^T$, $r=(\frac54,\frac14)^T$. 解 $\nabla^2f(x)p=-\nabla f(x)+r$; 检查 $\|r\|?\|\nabla f\|$; $p$ 是否下降方向.

**解答**: $\nabla f(x)=(x_1,\ 4x_2)=(1,1)^T$, $\nabla^2f=\mathrm{diag}(1,4)$. 方程
$$
\begin{pmatrix}1&0\\0&4\end{pmatrix}p=-(1,1)^T+(\tfrac54,\tfrac14)^T=(\tfrac14,-\tfrac34)^T.
$$
故 $p_1=\frac14$, $4p_2=-\frac34\Rightarrow p_2=-\frac{3}{16}$. 即 $p=\bigl(\frac14,-\frac{3}{16}\bigr)^T$.

$$
\|r\|=\sqrt{\bigl(\tfrac54\bigr)^2+\bigl(\tfrac14\bigr)^2}=\sqrt{\frac{25+1}{16}}=\frac{\sqrt{26}}{4},\qquad
\|\nabla f\|=\sqrt{2}.
$$
$\frac{\sqrt{26}}{4}\approx 1.275 < \sqrt{2}\approx 1.414$, 故 $\|r\|<\|\nabla f\|$.

下降性: $g^Tp=1\cdot\frac14+1\cdot\bigl(-\frac{3}{16}\bigr)=\frac{4-3}{16}=\frac{1}{16}>0$, 故 **不是** 下降方向 ($g^Tp\not< 0$).

**结论**: $p=(\frac14,-\frac{3}{16})^T$; $\|r\|<\|\nabla f\|$; $p$ **不是**下降方向.

---

### (b)

**题意**: $\mu$-强凸 + $L$-光滑, $\|r_k\|\le\theta\|g_k\|$, $0\le\theta<\mu/L$. 找 $a\in(0,1]$, $b>0$ 使 (1) 成立.

**解答**: $Hp=-g+r$. 强凸 $\Rightarrow$ $H\succeq\mu I$, 故
$$
-g^Tp=g^TH^{-1}g-g^TH^{-1}r\ge\mu\|H^{-1/2}g\|^2-\|H^{-1}g\|\,\|r\|.
$$
更直接:
$$
-g^Tp=g^T H^{-1}(g-r)\ge \lambda_{\min}(H^{-1})\|g\|^2-\|H^{-1}\|\,\|g\|\|r\|
\ge\frac1L\|g\|^2-\frac1\mu\|g\|\|r\|
$$
(因 $H\preceq LI\Rightarrow H^{-1}\succeq\frac1L I$, $H^{-1}\preceq\frac1\mu I$). 用 $\|r\|\le\theta\|g\|$:
$$
-g^Tp\ge\Bigl(\frac1L-\frac\theta\mu\Bigr)\|g\|^2.
$$
又 $\|p\|=\|H^{-1}(g-r)\|\le\frac1\mu(\|g\|+\|r\|)\le\frac{1+\theta}{\mu}\|g\|$, 以及
$$
\|p\|\ge\frac1L\|g-r\|\ge\frac1L(\|g\|-\|r\|)\ge\frac{1-\theta}{L}\|g\|.
$$
(当 $\theta<1$; 由 $\theta<\mu/L\le 1$ 自动成立.)

角条件: $-g^Tp\ge a\|g\|\|p\|$ 需要
$$
\Bigl(\frac1L-\frac\theta\mu\Bigr)\|g\|^2\ge a\|g\|\cdot\frac{1+\theta}{\mu}\|g\|,
$$
即取
$$
a:=\frac{\mu}{1+\theta}\Bigl(\frac1L-\frac\theta\mu\Bigr)=\frac{\mu/L-\theta}{1+\theta}\in(0,1].
$$
范数下界取
$$
b:=\frac{1-\theta}{L}>0.
$$

**结论**: $a=\dfrac{\mu/L-\theta}{1+\theta}$, $b=\dfrac{1-\theta}{L}$.

---

### (c)

**题意**: 用 Q4 证 inexact Newton 迭代全局收敛到唯一极小, 并给 $f(x_k)-f^\star$ 的几何界.

**解答**: (b) 已验证方向满足 Q4 的 (1). 由 Q4(c), 对同一套回溯参数,
$$
f(x_k)-f(x^\star)\le q^k\bigl(f(x_0)-f(x^\star)\bigr),\qquad q=1-2\mu C,
$$
其中 $C=c_A a\delta$, $\delta=\min\{\bar\alpha b,\frac{2\eta(1-c_A)a}{L}\}$, $a,b$ 如 (b). 强凸 $\Rightarrow$ 唯一极小且 $x_k\to x^\star$.

**结论**: 几何界如上; $x_k\to x^\star$.

---

### (d)

**题意**: 另设 (i) $\nabla^2f$ 在 $x^\star$ 附近 Lipschitz; (ii) 最终 $\alpha_k=1$; (iii) $\|r_k\|\le D\|g_k\|^2$. 证大 $k$ 有 $\|x_{k+1}-x^\star\|\le K\|x_k-x^\star\|^2$.

**解答**: 标准 inexact Newton 局部分析. 记 $H_k=\nabla^2f(x_k)$, $H_\star=\nabla^2f(x^\star)$, $e_k=x_k-x^\star$. 满步时
$$
x_{k+1}-x^\star=x_k-x^\star-H_k^{-1}g_k+H_k^{-1}r_k.
$$
由积分余项 / Lipschitz Hessian: 存在常数 $L_H$ 使
$$
\bigl\|g_k-H_\star e_k\bigr\|\le\frac{L_H}{2}\|e_k\|^2,\qquad
\bigl\|H_k-H_\star\bigr\|\le L_H\|e_k\|
$$
(在 $x^\star$ 邻域). 又 $g_k=H_k(x_k-x_{k+1}^{\mathrm{N}})$ 等标准分解给出
$$
e_{k+1}=H_k^{-1}\bigl((H_k-H_\star)e_k-(g_k-H_\star e_k)\bigr)+H_k^{-1}r_k.
$$
强凸 $\Rightarrow$ $\|H_k^{-1}\|\le 1/\mu$ (邻域内). 故
$$
\|e_{k+1}\|\le\frac1\mu\Bigl(L_H\|e_k\|^2+\frac{L_H}{2}\|e_k\|^2\Bigr)+\frac1\mu\|r_k\|
\le\frac{3L_H}{2\mu}\|e_k\|^2+\frac{D}{\mu}\|g_k\|^2.
$$
由 $L$-光滑 $\|g_k\|\le L\|e_k\|$, 得 $\|g_k\|^2\le L^2\|e_k\|^2$, 从而
$$
\|e_{k+1}\|\le\Bigl(\frac{3L_H}{2\mu}+\frac{DL^2}{\mu}\Bigr)\|e_k\|^2.
$$
取 $K:=\frac{3L_H}{2\mu}+\frac{DL^2}{\mu}$. 由 (c) 有 $x_k\to x^\star$, 故对充分大 $k$ 落入该邻域且 (ii)(iii) 适用.

**结论**: 已证; 例如 $K=\dfrac{3L_H}{2\mu}+\dfrac{DL^2}{\mu}$.

---

## 提交提醒

- Gradescope 单一 PDF; 文末附 AI-use declaration (缺则扣 50).
- 可用课堂定理 (如下降引理, 强凸间隙界, 回溯终止) 并点名, 不必重证.
