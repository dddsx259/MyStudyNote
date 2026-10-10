# Assignment 1 — 解答 (Dedekind cuts)

- **来源**: `assignment/Assignment01 dedekind cuts.pdf`
- **课程**: MATH2241 Introduction to Mathematical Analysis
- **说明**: 按题、按小问分开的完整解答; 必交 1, 2, 4; 第 3 题 optional 亦写出. 交稿前自行核对.

**约定**: Dedekind cut $\alpha\subsetneq\mathbb{Q}$ 满足 (i) $\alpha\neq\emptyset$, $\alpha\neq\mathbb{Q}$; (ii) 向下封闭: $x\in\alpha$, $y<x\Rightarrow y\in\alpha$; (iii) 无最大元: $\forall x\in\alpha$, $\exists z\in\alpha$ 使 $x<z$. $\mathbb{R}'=$ 全体 cuts. 题面中 $\hat r$ / $\mathrm{br}$ 均记为
$$
\hat r=\{q\in\mathbb{Q}:q<r\}.
$$

---

## 1. 有理 cut 与非有理 cut

### (a)

**题意**: 证明对每个 $r\in\mathbb{Q}$, $\hat r$ 是 Dedekind cut.

**解答**:

**(i) 非空且非全.** 取 $q=r-1\in\mathbb{Q}$, 则 $q<r$, 故 $q\in\hat r$, 非空. 又 $r\notin\hat r$ (因不满足 $r<r$), 故 $\hat r\neq\mathbb{Q}$.

**(ii) 向下封闭.** 设 $x\in\hat r$ 且 $y<x$. 则 $y<x<r$, 故 $y<r$, 从而 $y\in\hat r$.

**(iii) 无最大元.** 设 $x\in\hat r$, 即 $x<r$. 令
$$
z=\frac{x+r}{2}\in\mathbb{Q}.
$$
则 $x<z<r$, 故 $z\in\hat r$ 且 $z>x$.

**结论**: $\hat r$ 是 Dedekind cut.

---

### (b)

**题意**: 给出一个不等于任何 $\hat r$ 的 Dedekind cut.

**解答**: 定义
$$
\alpha=\bigl\{q\in\mathbb{Q}:q\le 0\bigr\}\cup\bigl\{q\in\mathbb{Q}:q>0,\ q^2<2\bigr\}.
$$

**验证 $\alpha$ 是 cut.**

**(i)** $0\in\alpha$, 故非空. 取正有理 $M$ 使 $M^2>2$ (如 $M=2$), 则 $M\notin\alpha$, 故 $\alpha\neq\mathbb{Q}$.

**(ii)** 设 $x\in\alpha$, $y<x$. 若 $x\le 0$, 则 $y<x\le 0$, 故 $y\in\alpha$. 若 $x>0$ 且 $x^2<2$: 若 $y\le 0$ 则 $y\in\alpha$; 若 $y>0$ 则 $0<y<x\Rightarrow y^2<x^2<2$, 故 $y\in\alpha$.

**(iii)** 设 $x\in\alpha$. 若 $x\le 0$, 取 $z=\min\{x/2+1/2,\ 1\}$ 中介于 $x$ 与正且平方小于 $2$ 的有理 (例如取 $z=1/2$: 若 $x<1/2$ 则已大于 $x$ 且 $(1/2)^2<2$; 若 $x\ge 1/2$ 但仍 $\le 0$ 不可能). 更干净: 取 $z=x/2$ 当 $x<0$; 当 $x=0$ 取 $z=1/2$. 若 $x>0$, $x^2<2$, 则存在有理 $z$ 使 $x<z$ 且 $z^2<2$ (标准: 取足够小的正有理 $h$ 使 $(x+h)^2=x^2+2xh+h^2<2$). 故无最大元.

**证明 $\alpha\neq\hat r$ 对一切 $r\in\mathbb{Q}$.** 反证: 设 $\alpha=\hat r$. 则 $r$ 应为 $\alpha$ 的「分割点」. 若 $r\le 0$, 则所有正且平方小于 $2$ 的有理 (如 $1$) 属于 $\alpha=\hat r$, 故 $1<r\le 0$, 矛盾. 若 $r>0$, 则:
- 一切 $q\in\alpha$ 满足 $q<r$, 特别对满足 $q^2<2$ 的正有理有 $q<r$, 取上确界得 $\sqrt{2}\le r$, 即 $r^2\ge 2$;
- 又若 $r^2>2$, 则存在有理 $s$ 使 $0<s<r$ 且 $s^2>2$ (稠密/逼近), 于是 $s\in\hat r=\alpha$, 但 $s>0$ 且 $s^2>2$ 与 $\alpha$ 的定义矛盾; 故必 $r^2=2$.

但无有理数平方等于 $2$ (标准引理: 若 $r=m/n$ 既约则 $m,n$ 皆偶). 矛盾. 故 $\alpha$ 不是任何 $\hat r$.

**结论**: 上例 $\alpha$ (对应 $\sqrt{2}$ 的 cut) 即可.

---

## 2. 加法良定义

**题意**: $\alpha+\beta=\{q\in\mathbb{Q}:\exists a\in\alpha,\ b\in\beta,\ q=a+b\}$, 证明仍是 Dedekind cut.

**解答**: 固定 $\alpha,\beta\in\mathbb{R}'$.

**(i) 非空.** 取 $a\in\alpha$, $b\in\beta$ (二者非空), 则 $a+b\in\alpha+\beta$.

**非全.** 因 $\alpha\neq\mathbb{Q}$, 存在 $A\in\mathbb{Q}\setminus\alpha$; 因向下封闭, 一切 $x\ge A$ 都不在 $\alpha$ (否则 $A\le x$ 且 $A\in\alpha$ 推出 $A\in\alpha$). 同理存在 $B\notin\beta$. 断言 $A+B\notin\alpha+\beta$. 若不然, $A+B=a+b$ 对某 $a\in\alpha$, $b\in\beta$. 则 $a-A=B-b$. 若 $a\ge A$, 由向下封闭及 $A\notin\alpha$ 的上界性质: 实际上 $a\in\alpha\Rightarrow a<A$ (否则 $a\ge A\Rightarrow A\in\alpha$). 同理 $b<B$. 于是 $a+b<A+B$, 与 $a+b=A+B$ 矛盾. 故 $A+B\notin\alpha+\beta$, $\alpha+\beta\neq\mathbb{Q}$.

**(ii) 向下封闭.** 设 $q\in\alpha+\beta$, $y<q$. 写 $q=a+b$, $a\in\alpha$, $b\in\beta$. 令 $\delta=q-y>0$. 则
$$
y=a+(b-\delta).
$$
需把 $b-\delta$ 放进 $\beta$ 或调整. 因 $\beta$ 无最大元, 存在 $b'\in\beta$ 使 $b'>b$; 更直接的标准写法: 因 $\alpha$ 向下封闭不直接给出 $a-\delta$. 采用: 取
$$
y=(a-\delta)+b.
$$
若 $a-\delta\in\alpha$ 则完成. 因 $a\in\alpha$ 无最大, 存在 $a_1\in\alpha$ 使 $a_1>a$; 但我们需要更小. 实际上 $a-\delta<a$, 由向下封闭 $a-\delta\in\alpha$. 是的: $a-\delta<a$ 且 $a\in\alpha\Rightarrow a-\delta\in\alpha$. 故 $y=(a-\delta)+b\in\alpha+\beta$.

**(iii) 无最大元.** 设 $q=a+b\in\alpha+\beta$. 因 $\alpha$ 无最大, 存在 $a'\in\alpha$ 使 $a'>a$. 则 $a'+b>a+b=q$ 且 $a'+b\in\alpha+\beta$.

**结论**: $\alpha+\beta$ 是 Dedekind cut, 加法良定义.

---

## 3. (Optional) 非负乘法

**题意**: $\alpha,\beta\ge\hat 0$ (即 $\hat 0\subseteq\alpha,\hat 0\subseteq\beta$) 时,
$$
\alpha\beta=\{q\in\mathbb{Q}:q<0\}\cup\{q:\exists a\in\alpha,\ a>0,\ \exists b\in\beta,\ b>0,\ q<ab\}
$$
是 Dedekind cut. (题面定义等价写法.)

**解答**:

**(i) 非空.** 一切负有理属于 $\alpha\beta$; 或取正 $a\in\alpha$, $b\in\beta$ (因 $\hat 0\subseteq\alpha$ 且无最大, $\alpha$ 含正元), 则 $ab/2<\ ab$ 给出正元属于 $\alpha\beta$.

**非全.** 因 $\alpha\neq\mathbb{Q}$, 存在正有理上界型元素: 取 $A\notin\alpha$ 且 $A>0$ (若所有正有理都在 $\alpha$ 则与非全+向下封闭矛盾于存在正的不在 $\alpha$ 的有理). 同理正 $B\notin\beta$. 则任何 $q\ge AB$ 不能写成小于某 $ab$ ($a\in\alpha,a>0,b\in\beta,b>0$), 因为 $a<A$, $b<B\Rightarrow ab<AB$. 故 $AB\notin\alpha\beta$.

**(ii) 向下封闭.** 若 $q\in\alpha\beta$ 且 $y<q$: 若 $y<0$ 则 $y\in\alpha\beta$. 若 $y\ge 0$, 则 $q$ 必来自某 $q<ab$, 从而 $y<ab$, 故 $y\in\alpha\beta$.

**(iii) 无最大元.** 设 $q\in\alpha\beta$. 若 $q<0$, 取 $z=q/2$ (仍负) 或 $0$ 的负侧中间值 $z$ 使 $q<z<0$, 则 $z\in\alpha\beta$. 若 $q$ 由 $q<ab$ 给出 ($a,b>0$), 因 $\alpha$ 无最大可取 $a'\in\alpha$, $a'>a>0$, 则 $q<ab<a'b$, 取有理 $z$ 使 $q<z<a'b$, 即得 $z\in\alpha\beta$ 且 $z>q$.

**结论**: 非负 cut 的乘积仍是 cut.

---

## 4. 完备性: $u=\bigcup_{\alpha\in S}\alpha=\sup S$

**题意**: $S\subseteq\mathbb{R}'$ 非空有上界; $u=\bigcup_{\alpha\in S}\alpha$ (可用 $u$ 是 cut 这一事实); 序 $\alpha\le\beta\Leftrightarrow\alpha\subseteq\beta$. 证明 $u=\sup S$.

**解答**:

**(1) $u$ 是上界.** 对任意 $\alpha\in S$, 由并集定义 $\alpha\subseteq u$, 即 $\alpha\le u$.

**(2) $u$ 是最小上界.** 设 $v\in\mathbb{R}'$ 也是 $S$ 的上界, 即对一切 $\alpha\in S$ 有 $\alpha\subseteq v$. 则
$$
u=\bigcup_{\alpha\in S}\alpha\subseteq v,
$$
即 $u\le v$.

因此 $u$ 是 $S$ 的最小上界: $u=\sup S$.

**结论**: $u=\sup S$.
