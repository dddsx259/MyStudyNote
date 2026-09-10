# Lec01 导论 (Introduction): 课程导论与优化基础

- **来源**: `Lec/01-introduction-slides.pdf` (23 页)
- **课程**: MATH3900, Prof. Lexiao Lai, 2026–27 S1
- **说明**: 同主题另有 `Lec/01-introduction-slides-long.pdf` (扩展版) 与 `Lec/handout/01-introduction-handout.pdf`; 本讲义按 23 页 slides 整理. 凡非定义公式均附 **证明** / **证明思路**.

---

## 本节在课程中的位置

导论课建立**优化问题 (optimization problem)** 的统一语言, 并展示 AI/数据科学中的典型实例; 后续四章分别深入无约束优化 (unconstrained optimization)、约束优化 (constrained optimization)、非光滑优化 (nonsmooth optimization)、随机优化 (stochastic optimization).

---

## 1. 优化问题的一般形式

$$\min_{x\in C} f(x)$$

(问题形式定义, 无需证明.)

| 术语 | 含义 |
|---|---|
| 决策变量 (decision variable) $x$ | $x\in\mathbb{R}^d$ |
| 目标函数 (objective function) $f$ | $f:\mathbb{R}^d\to\mathbb{R}$ |
| 可行域 (feasible set) $C$ | $C\subseteq\mathbb{R}^d$; $x\in C$ 可行 |
| 无约束 (unconstrained) | $C=\mathbb{R}^d$ |
| 最大化 (maximization) | $\max f = \min(-f)$ |

**证明** (最大化改最小化): $\max_x f(x)=-\min_x(-f(x))$, 因为对任意可行 $x$, $f(x)\le M$ $\Leftrightarrow$ $-f(x)\ge -M$, 两端最优值差一个负号.

---

## 2. 最优解

- **全局极小点 (global minimizer)** $x^*$: $f(x^*)\le f(x),\ \forall x\in C$ (定义, 无需证明)
- **局部极小点 (local minimizer)**: 在 $x^*$ 某邻域内最小 (定义)
- **$\arg\min$**: 全体全局极小点的集合 (定义)
- **最优值 (optimal value)** $f^*:=\inf_{x\in C} f(x)$; 若 $x^*$ 为全局极小点则 $f(x^*)=f^*$
- **补充**: $f^*$ 不一定被某个 $x\in C$ 达到 (如下确界 (infimum) 不可达)

**证明思路** (极小点 $\Rightarrow$ $f(x^*)=f^*$): 由定义 $f(x^*)\le f(x)$ $\forall x\in C$, 故 $f(x^*)$ 是下界且是最大下界, 等于 $\inf f$.

### 紧集 (compact set)

在 $\mathbb{R}^d$ 中 (Heine–Borel): $C$ **紧** $\Leftrightarrow$ $C$ **闭且有界** (closed and bounded).

**证明思路**: Heine–Borel 定理是 $\mathbb{R}^d$ 标准结果 (开覆盖有限子覆盖 $\Leftrightarrow$ 闭有界); 本课直接使用.

- **有界 (bounded)**: 存在 $M>0$, 使 $\|x\|\le M$ 对所有 $x\in C$ (定义)
- **闭 (closed)**: 包含所有极限点 (收敛序列的极限仍在 $C$ 内) (定义)

### 魏尔斯特拉斯定理 (Weierstrass theorem)

$C\subseteq\mathbb{R}^d$ **非空紧**, $f$ 在 $C$ 上**连续** $\Rightarrow$ 存在全局极小点.

**证明思路**: 连续像 $f(C)$ 在 $\mathbb{R}$ 中紧 $\Rightarrow$ 闭且有界 $\Rightarrow$ 有最小值 $m=\min f(C)$. 取 $x^*\in C$ 使 $f(x^*)=m$ 即为全局极小点. (等价证法: 取极小化序列 $f(x_n)\to\inf f$, 紧性抽收敛子列, 连续性得极限点达到下确界.)

**直觉**: 连续函数在紧集上必取到最小值.

---

## 3. AI/数据科学中的优化实例

| 任务 | 优化问题 |
|---|---|
| 线性回归 (linear regression) | $\min_x \frac{1}{2n}\sum_i (a_i^T x - y_i)^2$ |
| 逻辑回归 (logistic regression) 二分类 | $\min_x \frac{1}{n}\sum_i \log(1+e^{-y_i a_i^T x})$ |
| 硬间隔支持向量机 (hard-margin SVM) | $\min_x \frac{1}{2}\|x\|^2$ s.t. $y_i a_i^T x\ge 1$ |
| 套索回归 (Lasso) | $\min_x \frac{1}{2n}\sum_i (a_i^T x-y_i)^2 + \lambda\|x\|_1$ |
| 神经网络 (neural network) | $\min_x \frac{1}{n}\sum_i L(h(a_i;x), y_i)$ |

**工作流**: 收集数据 $D$ → 建模型 $\hat y(a;x)$ → 优化参数 $x$.

### 逻辑回归损失为何含 $e^{-\cdot}$: 负对数似然

讲义目标 $\frac{1}{n}\sum_i \log(1+e^{-y_i a_i^T x})$ 中的指数来自 **sigmoid (logistic function)**, 外层 $\log$ 来自 **负对数似然 (negative log-likelihood, NLL)**; 不是 AdaBoost 那种纯 **指数损失 (exponential loss)** $e^{-y a^T x}$.

1. **对数几率 (log-odds) 与 sigmoid**: 标签常取 $y_i\in\{+1,-1\}$. 用线性分数建模
   $$\log\frac{P(y=1\mid a)}{P(y=-1\mid a)}=a^T x$$
   得
   $$P(y\mid a)=\sigma(y\, a^T x)=\frac{1}{1+e^{-y a^T x}}$$

   **证明**: 令 $p=P(y=1\mid a)$, 则 $\log\frac{p}{1-p}=a^T x$ $\Rightarrow$ $\frac{p}{1-p}=e^{a^T x}$ $\Rightarrow$ $p=\frac{e^{a^T x}}{1+e^{a^T x}}=\frac{1}{1+e^{-a^T x}}=\sigma(a^T x)$.  
   对 $y=\pm 1$: $P(y\mid a)=\sigma(y a^T x)$ (因 $y=-1$ 时 $P=\sigma(-a^T x)=1-\sigma(a^T x)$).

2. **极大似然 (maximum likelihood) → NLL**: 独立样本下最小化
   $$-\log P(y_i\mid a_i)=-\log\sigma(z_i)=\log(1+e^{-z_i}),\quad z_i=y_i a_i^T x$$
   平均后即讲义目标. 标签为 $\{0,1\}$ 时等价于 **二元交叉熵 (binary cross-entropy)**.

   **证明**: $\sigma(z)=\frac{1}{1+e^{-z}}$, 故 $-\log\sigma(z)=\log(1+e^{-z})$. 独立样本似然 $\prod_i P(y_i\mid a_i)$, 取负对数并平均得 ERM 目标.

3. **对比**: 线性回归的平方损失对应高斯噪声假设; 逻辑回归对应 Bernoulli + logit 链接. $y a^T x$ 很大 (分对且间隔大) 时损失 $\to 0$; 分错则损失增大.

### 大规模与随机优化

- 现代模型: $n$ 与 $d$ 极大, 全量算 $F(x)$ 昂贵
- **小批量随机梯度下降 (mini-batch SGD)**: 每步只用数据子集 — 课程第 4 部分主题

---

## 4. 线性代数回顾 (矩阵形式)

线性回归目标可写为:
$$\min_{x\in\mathbb{R}^d} \frac{1}{2n}\|Ax-y\|^2$$
其中 $A$ 行向量为 $a_i^T$, $y=(y_1,\ldots,y_n)^T$.

**补充**: 矩阵–向量乘法按行点积; $MN=[Mw_1\ \cdots\ Mw_r]$.

---

## 5. 方向导数 (directional derivative) 与梯度 (gradient)

**方向导数**:
$$f'(x;v)=\lim_{t\downarrow 0}\frac{f(x+tv)-f(x)}{t}$$
(定义, 无需证明.)

若可微: $\nabla f(x)=(\partial f/\partial x_1,\ldots,\partial f/\partial x_d)^T$, $f'(x;v)=\nabla f(x)^T v$.

**证明思路**: 可微意味着 $f(x+tv)=f(x)+t\nabla f(x)^T v+o(t)$; 除以 $t$ 取极限即得方向导数公式.

### 链式法则 (chain rule)

$F(x)=g(h(x))$, $h:\mathbb{R}^d\to\mathbb{R}^m$:
$$\nabla F(x)=J_h(x)^T \nabla g(h(x))$$
$J_h$ 为雅可比矩阵 (Jacobian), 行向量为 $\nabla h_j(x)^T$.

**证明思路**: 一阶展开 $h(x+s)=h(x)+J_h(x)s+o(\|s\|)$, 再对 $g$ 展开并复合; 整理一次项系数得 $J_h^T\nabla g$.

**线性回归梯度** ($F=\frac{1}{2n}\|Ax-y\|^2$):
$$\nabla F(x)=\frac{1}{n}A^T(Ax-y)$$

**证明**: $F=\frac{1}{2n}(Ax-y)^T(Ax-y)$. 对 $x$ 的微分: $\mathrm{d}F=\frac{1}{n}(Ax-y)^T A\,\mathrm{d}x$, 故 $\nabla F=\frac{1}{n}A^T(Ax-y)$. (或写成 $F=\frac{1}{2n}\sum_i (a_i^T x-y_i)^2$, 逐项求导再合成.)

---

## 6. 沿直线的微积分基本定理与泰勒展开 (Taylor expansion)

对 $\phi(t)=f(u+t(v-u))$:
$$f(v)-f(u)=\int_0^1 \nabla f(u+t(v-u))^T(v-u)\,dt$$

**证明**: 令 $x(t)=u+t(v-u)$ (从 $u$ 到 $v$ 的直线参数化), $\phi(t)=f(x(t))$. 一维微积分基本定理 + 链式法则: $\phi(1)-\phi(0)=\int_0^1\phi'(t)\,dt$, 而 $\phi'(t)=\nabla f(x(t))^T(v-u)$.

**一阶泰勒展开** (可微):
$$f(x+s)=f(x)+\nabla f(x)^T s + o(\|s\|)$$

**证明思路**: 可微的定义即为此式 (或等价: 沿任意方向的差商极限为 $\nabla f^T s$).

**二阶泰勒展开** ($C^2$ 近邻):
$$f(x+s)=f(x)+\nabla f(x)^T s+\frac{1}{2}s^T\nabla^2 f(x)s+o(\|s\|^2)$$

**证明思路**: 对 $\phi(t)=f(x+ts)$ 用一维带 Peano 余项的二阶 Taylor: $\phi(1)=\phi(0)+\phi'(0)+\frac12\phi''(0)+o(1)$; 计算 $\phi',\phi''$ 即得. $\nabla^2 f$ 为海森矩阵 (Hessian).

---

## 易错点

1. 局部极小点 $\ne$ 全局极小点
2. 魏尔斯特拉斯定理需**紧 + 连续**; 缺一可能无最小值
3. 套索的 $\ell_1$ 在 $x_j=0$ 处不可微 — 属非光滑优化
4. Logistic 回归**无**闭式解 (与线性回归对比)
5. 逻辑回归损失是 $\log(1+e^{-ya^T x})$ (NLL), 勿与指数损失 $e^{-ya^T x}$ 混淆

---

## 与后续章节

1. 无约束优化算法 (梯度下降 (gradient descent) 等)
2. 约束优化 / KKT 条件 (KKT conditions) (支持向量机 (SVM))
3. 非光滑 (近端算子 (proximal), 次梯度 (subgradient))
4. 随机优化 (SGD, 小批量)

## 推荐教材

Boyd & Vandenberghe; Nocedal & Wright; Beck (见 `课程信息.md` / `Lec/textbook/`)

---

## 附录: 本节涉及 ML 模型基础知识速查

> 符号与讲义一致: 样本特征 $a_i\in\mathbb{R}^d$, 标签 $y_i$, 参数 $x\in\mathbb{R}^d$ (有的书写作 $w$). 你已学过 d2l 时可当回忆卡; 本课重点是把它们写成优化问题.

### 共用设定

| 概念 | 要点 |
|---|---|
| 监督学习 (supervised learning) | 数据 $\{(a_i,y_i)\}_{i=1}^n$; 学映射 $a\mapsto\hat y$ |
| 经验风险最小化 (empirical risk minimization, ERM) | $\min_x \frac{1}{n}\sum_i L(\hat y(a_i;x), y_i)$ (+ 可选正则) |
| 假设类 (hypothesis class) | 线性: $\hat y=a^T x$ (可加偏置: 特征扩一维常 1) |
| 训练 / 测试 | 在训练集上优化 $x$; 泛化看未见数据 |

---

### A. 线性回归 (linear regression)

- **任务**: 回归, $y_i\in\mathbb{R}$
- **模型**: $\hat y_i = a_i^T x$
- **损失**: 均方误差 (mean squared error, MSE)
  $$\min_x \frac{1}{2n}\sum_i (a_i^T x-y_i)^2 = \min_x \frac{1}{2n}\|Ax-y\|^2$$
- **概率故事**: $y_i = a_i^T x + \varepsilon_i$, $\varepsilon_i\sim\mathcal{N}(0,\sigma^2)$ 时, 极大似然 $\Leftrightarrow$ MSE

  **证明思路**: 似然 $\propto\exp(-\frac{1}{2\sigma^2}\sum_i(y_i-a_i^T x)^2)$, 最大化等价于最小化 $\sum_i(y_i-a_i^T x)^2$.
- **闭式解 (closed-form)**: 若 $A^T A$ 可逆, 正规方程 (normal equation)
  $$x^* = (A^T A)^{-1} A^T y$$
  (讲义里的 $\frac{1}{2n}$ 不改变极小点; 实践中常用 QR / 伪逆, 病态时加正则)

  **证明**: $F(x)=\frac{1}{2n}\|Ax-y\|^2$, $\nabla F=\frac{1}{n}A^T(Ax-y)=0$ $\Leftrightarrow$ $A^T Ax=A^T y$. $A^TA$ 可逆时唯一解如上. 系数 $\frac{1}{2n}$ 不影响令梯度为零的解.
- **梯度**: $\nabla F(x)=\frac{1}{n}A^T(Ax-y)$ (证明见 §5)
- **本课位置**: 无约束光滑优化的标准例子; 有闭式解, 可对照「无闭式」的 logistic

---

### B. 逻辑回归 (logistic regression)

- **任务**: 二分类; 讲义常用 $y_i\in\{+1,-1\}$ (另常见 $\{0,1\}$)
- **模型**: 先算线性分数 $a_i^T x$, 再经 sigmoid 得概率
  $$P(y=1\mid a)=\sigma(a^T x)=\frac{1}{1+e^{-a^T x}}$$
- **损失**: 负对数似然 / 二元交叉熵 (见上文专节)
  $$\min_x \frac{1}{n}\sum_i \log(1+e^{-y_i a_i^T x})$$
- **决策**: 常取 $\mathrm{sign}(a^T x)$ 或阈值阈值 $0.5$
- **性质**: 目标对 $x$ **凸 (convex)** 且光滑; **无**一般闭式解 → 需梯度下降等
- **单样本梯度直觉**: 令 $z_i=y_i a_i^T x$, 则 $\partial_{x}\log(1+e^{-z_i}) = -\sigma(-z_i)\, y_i a_i$; 分错或没把握时更新更大

  **证明**: $\frac{\mathrm{d}}{\mathrm{d}z}\log(1+e^{-z})=\frac{-e^{-z}}{1+e^{-z}}=-\sigma(-z)$. 链式法则乘 $\nabla_x z_i=y_i a_i$.
- **本课位置**: 无约束光滑优化; 与线性回归对照「似然假设不同 → 损失不同」

---

### C. 硬间隔支持向量机 (hard-margin SVM)

- **任务**: 二分类, 要求训练数据 **线性可分 (linearly separable)**
- **几何**: 要一张间隔最大的分离超平面; 对 $y_i\in\{+1,-1\}$, 约束 $y_i a_i^T x \ge 1$ 把「功能间隔」规范化为 1, 最大化几何间隔 $\Leftrightarrow$ 最小化 $\|x\|$
  $$\min_x \tfrac12\|x\|^2 \quad\mathrm{s.t.}\quad y_i a_i^T x\ge 1\ \forall i$$

  **证明思路**: 超平面 $a^T x=0$ (过原点版本; 有偏置时可扩维) 的几何间隔与 $\|x\|$ 成反比. 将功能间隔缩放到 $\ge 1$ 后, 最大化间隔等价于最小化 $\|x\|$ (或 $\tfrac12\|x\|^2$, 单调变换不改 argmin).
- **支持向量 (support vector)**: 落在间隔边界上的样本 (最优时通常只有它们「起作用」)
- **与 logistic 对比**: logistic 输出概率、无硬约束; SVM (硬间隔) 是 **约束优化**, 可分失败则问题不可行
- **软间隔 (soft-margin) SVM** (本导论未写进公式): 允许少量违例, 加松弛变量与惩罚 — 不可分数据时用; 课程后面约束优化会更形式化
- **本课位置**: 约束优化 / 后面 KKT 的动机例子

---

### D. 套索回归 (Lasso) 与 $\ell_1$ 正则

- **任务**: 仍是线性回归, 但希望 **稀疏 (sparse)** 解 (许多 $x_j=0$ → 特征选择)
- **目标**:
  $$\min_x \frac{1}{2n}\sum_i (a_i^T x-y_i)^2 + \lambda\|x\|_1,\quad \|x\|_1=\sum_j|x_j|$$
- **$\lambda\ge 0$**: 正则强度; 越大越稀疏
- **对比岭回归 (ridge, $\ell_2$)**: ridge 用 $\lambda\|x\|_2^2$, 缩小系数但通常不精确置零; Lasso 的 $\ell_1$ 球有角, 更易得到精确 0
- **优化要点**: $\|x\|_1$ 在 $x_j=0$ **不可微** → 非光滑优化 (次梯度 / 近端梯度 (proximal gradient) 等)
- **本课位置**: 非光滑优化章节的经典例子

---

### E. 神经网络 (neural network) 在优化语言里长什么样

- **模型**: 参数全体仍记作 $x$; 预测 $h(a;x)$ 是多层仿射 + 激活函数 (activation) 的复合 (MLP, CNN, …)
- **目标** (讲义抽象形式):
  $$\min_x \frac{1}{n}\sum_i L\bigl(h(a_i;x), y_i\bigr)$$
  $L$ 随任务选: 回归常用 MSE; 分类常用交叉熵
- **与前面模型关系**: 线性回归 / logistic 可看成「一层、无隐藏层」的特例; 深网假设类大得多, 目标通常 **非凸**
- **训练**: 反向传播算梯度; $n$ 大时用 **小批量 SGD** (每步用随机子集估计 $\nabla F$) — 课程第 4 部分
- **本课位置**: 说明「AI 模型 = 选 $h$ 与 $L$ 后的优化问题」, 细节不在导论展开

---

### F. 五者对照 (速记)

| 模型 | 输出 | 典型损失 / 形式 | 约束? | 光滑? | 闭式解? |
|---|---|---|---|---|---|
| 线性回归 | 实数 | MSE | 无 | 是 | 有 (满秩时) |
| 逻辑回归 | 概率 / 类别 | $\log(1+e^{-ya^T x})$ | 无 | 是 | 无 |
| 硬间隔 SVM | 类别 | $\min\tfrac12\|x\|^2$ | 有 ($ya^T x\ge 1$) | 目标光滑 | 无 (二次规划) |
| Lasso | 实数 | MSE + $\lambda\|x\|_1$ | 无 | **否** ($\ell_1$) | 无 |
| 神经网络 | 任意 | $\frac1n\sum L(h(a_i;x),y_i)$ | 通常无 | 视 $L$/激活 | 无 (且常非凸) |

**一条线串起来**: 先把预测写成 $\hat y(a;x)$, 再选损失 (与概率假设一致), 需要时加约束或正则, 最后问: 凸吗? 光滑吗? 能不能闭式解? 该用哪种优化算法?
