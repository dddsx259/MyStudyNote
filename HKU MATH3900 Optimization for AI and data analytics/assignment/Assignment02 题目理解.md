# Assignment 2 — 题目理解

- **来源**: `assignment/Assignment02.pdf` (3 页; 原名 `assignment_2.pdf`)
- **课程**: MATH3900, Lexiao Lai
- **Due**: 2026-10-20 23:59 (Gradescope; 迟交不收)
- **分值**: 100 pts; **必须**附 AI-use declaration (缺则扣 50)
- **对齐**: Unconstrained — Newton, Armijo / 回溯, 下降法全局收敛, inexact Newton

---

## 总览

| 题 | 主题 | 分 |
|---|---|---|
| 1 | T/F (Newton 仿射, 精确线搜索 FOC, Armijo 尺度, Armijo-GD, Newton 一步到极小⇒二次) | 20 |
| 2 | $f(t)=\sqrt{1+t^2}$: Newton 公式 / Armijo 两步 / 满 Newton 吸引域与超线性阶 | 20 |
| 3 | $f=x_1^2+x_1x_2+x_2^2+\frac14(x_1+x_2)^4$: 满 Newton; $(u,v)$ 坐标; Newton 仿射不变 | 20 |
| 4 | 角条件 + 范数下界方向 + 回溯: 步长下界 / 充分下降 / 强凸线性率; 精确线搜索继承 | 20 |
| 5 | Inexact Newton: 残差例子; 角条件; 全局收敛; 局部二次 | 20 |

---

## 分题要点

### 1. T/F (各 4)

| | 直觉 |
|---|---|
| (a) $af+b$ ($a>0$) 不改 Newton 方向 | 真: $H,g$ 同乘 $a$ |
| (b) 精确线搜索 $\alpha^\star>0$ $\Rightarrow$ $\nabla f(x+\alpha^\star p)^Tp=0$ | 真: $\phi'(\alpha^\star)=0$ |
| (c) $p\mapsto sp$ 时同一套 Armijo 回溯得同一下一点 | 假: 候选步长集不随 $s$ 缩放 |
| (d) 仅「某 $\alpha_k>0$ 过 Armijo」的 GD $\Rightarrow\|\nabla f\|\to0$ | 假: 步长可人为过小; 需回溯下界 |
| (e) $f''>0$, 满 Newton 处处一步到 $t^\star$ $\Rightarrow$ 二次 | 真: 推出 $f'''=0$ |

### 2. Soft-abs / hyperbola

- $f'=\dfrac{t}{\sqrt{1+t^2}}$, $f''=(1+t^2)^{-3/2}$; 极小 $t^\star=0$
- 满 Newton: $t_+=-t^3$
- (b) 从 $t_0=2$ 做 Newton+Armijo ($\bar\alpha=1,\eta=1/2,c_A=1/4$), 逐试记录
- (c) $|t_0|<1$ 收敛; $|t_0|>1$ 发散; $0<|t_0|<1$ 时阶 $q=3$, 极限比 $=1$

### 3. 四次扰动二次型

- 在 $x^{(0)}=(1,0)$ 算 $\nabla,\nabla^2$, 满 Newton 一步
- $u=x_1+x_2$, $v=x_1-x_2$: 写 $F(u,v)$, 对 $F$ 做一步 Newton 再映回 $x$
- 一般: $F(z)=f(Az+b)$ 时满 Newton 与 $x=Az+b$ 仿射共变 ($x_+=Az_++b$)

### 4. 广义下降方向 + 回溯

方向满足
$$
-\nabla f^Tp_k\ge a\|\nabla f\|\|p_k\|,\qquad \|p_k\|\ge b\|\nabla f\|.
$$
- (a)(b) 用 $L$-光滑 + Armijo 回溯标准论证给 $\delta,C$
- (c) 强凸间隙界 $\Rightarrow$ 几何率 $q=1-\mu C$ (或等价改写)
- (d) 精确线搜索 $\alpha_k$ 不差于任意可行 Armijo 步, 故同 $C,q$

### 5. Inexact Newton

- 残差 $r_k=\nabla^2f(x_k)p_k+\nabla f(x_k)$
- (a) 小例子: 解方程, 查 $\|r\|?\|\nabla f\|$, 是否下降方向
- (b)–(d) $\|r_k\|\le\theta\|\nabla f\|$, $\theta<\mu/L$: 推出角条件; 套 Q4 全局收敛; 再加 Lipschitz Hessian + 满步 + $\|r\|=O(\|g\|^2)$ 得局部二次

---

## 提交检查

- [ ] Gradescope 单一 PDF
- [ ] AI declaration (Level 0–3 格式完整)
- [ ] 引用课堂定理可不再证, 但反例须验证
- [ ] Q2(b) 每个 trial 写出步长 / 目标值 / Armijo 界
