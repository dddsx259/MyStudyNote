# Assignment 1 — 题目理解

- **来源**: `assignment/Assignment01.pdf` (3 页; 原名 `assignment_1.pdf`)
- **课程**: MATH3900, Lexiao Lai
- **Due**: 2026-09-28 23:59 (Gradescope; 迟交不收)
- **分值**: 100 pts; **必须**附 AI-use declaration (缺则扣 50)
- **对齐**: Intro / Unconstrained (凸, 强凸, L-smooth, GD, 最速下降)

---

## 总览

| 题 | 主题 | 分 |
|---|---|---|
| 1 | T/F (存在性, 强凸, 凸极小集, 满步 GD) | 20 |
| 2 | $f=\frac14 x_1^4-\frac12 x_1^2+\frac12 x_2^2$ 驻点分类; 另 $h=x_1^4-x_4^2$ 在原点 | 20 |
| 3 | ridge 型 $f_\lambda$ ($n=d=2$ 给定数据): 显式 / 凸性 / 极小点 | 20 |
| 4 | $f(t)=t^4/4+t^2/2$ 的 GD 步长与收缩 | 20 |
| 5 | sign 梯度 / $\ell_\infty$ 最速下降与收敛率 | 20 |

---

## 分题要点

### 1. T/F (各 4)

| | 直觉 |
|---|---|
| (a) $C^1$ 有下界 $\Rightarrow$ 有全局极小 | 假: 如 $e^x$ 有下界无极小 |
| (b) $\nabla f(u)=\nabla f(v)$ ($u\neq v$) $\Rightarrow$ 非强凸 | 真: 强凸梯度严格单调 |
| (c) $C^2$ 凸且唯一全局极小 $\Rightarrow$ 某 $\mu$-强凸 | 假: 可「扁」但仍唯一极小 |
| (d) 凸 + 两全局极小 $\Rightarrow$ 线段上皆极小 | 真: 凸性标准事实 |
| (e) $\nabla f\neq 0$ $\Rightarrow$ $f(x-\nabla f)<f(x)$ | 假: 步长 1 可能过大 (Tut1 同类) |

### 2. 驻点与全局极小

- 算 $\nabla f$, $\nabla^2 f$; 找驻点并分类 (局部极小/极大/皆非)
- 找**全局**极小与最优值
- $h=x_1^4-x_2^4$ 在 $0$: 看 Hessian / 沿坐标轴符号变化

### 3. Ridge 扩展

$$
f_\lambda(x)=\frac1{2n}\sum_i(a_i^Tx-y_i)^2+\frac\lambda2\|x\|^2,\quad n=d=2,\ a_1=(1,1),y_1=1,\ a_2=(2,2),y_2=2.
$$

- 写出显式 $f_\lambda(x_1,x_2)$, $\nabla$, $H$
- 按 $\lambda$ 判定凸 / 强凸; 强凸时给 $\mu,L,\kappa=L/\mu$
- 各 $\lambda$ 是否有全局极小, 是否唯一; $\lambda=1$ 时算最小值

### 4. 一维 GD

$f(t)=t^4/4+t^2/2$, $t_{k+1}=t_k-\alpha f'(t_k)$.

- $f',f''$; 全局极小; 是否强凸; 梯度是否全局 $L$-Lipschitz
- $t_0=1$, $\alpha=1/4$ 算 $t_1,t_2$; 刻画使 $f(t_1)<f(t_0)$ 的 $\alpha$
- $\alpha=1/4$, $|t_0|\le 1$ $\Rightarrow$ $|t_k|\le(3/4)^k|t_0|$ 并收敛到极小

### 5. Sign / $\ell_\infty$ 最速下降

- $\min_{\|p\|_\infty\le 1}\nabla f(x)^Tp$: 最优值与方向; $\nabla f\neq 0$ 时是否皆为下降方向
- 一维 $\phi(t)=t^2/2$, $t_{k+1}=t_k-\eta\mathrm{sign}(\phi'(t_k))$, $t_0=\eta/2$: 是否收敛到 0
- $L$-光滑下找 $\alpha=\alpha(\nabla f,L,d)$ 使
  $$f\bigl(x-\alpha\mathrm{sign}(\nabla f(x))\bigr)\le f(x)-\frac{\|\nabla f(x)\|_1^2}{2Ld}$$
- 再加 $\mu$-强凸: 证 $f(x_k)-f^\star\le(1-\mu/(Ld))^k(f(x_0)-f^\star)$

---

## 提交检查

- [ ] Gradescope 单一 PDF
- [ ] AI declaration (Level 0–3 格式完整)
- [ ] 引用课堂定理可不再证, 但反例须验证
