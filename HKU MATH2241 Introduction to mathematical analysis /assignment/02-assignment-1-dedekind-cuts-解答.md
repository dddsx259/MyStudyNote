# Assignment 1 解答提示: Dedekind cuts

- **来源**: `assignment/01-assignment-1-dedekind-cuts.pdf`
- **说明**: 提示与证明提纲, 非完整誊写稿; 请自行写成可交版本

---

## Q1(a) $\hat r=\{q:q<r\}$ 是 cut

1. 非空: 取 $r-1$. 非全: $r\notin\hat r$.
2. 向下封闭: 若 $q<r$ 且 $y<q$ 则 $y<r$.
3. 无最大: 对 $q\in\hat r$, 取 $z=(q+r)/2$, 则 $q<z<r$.

## Q1(b) 非有理 cut 的例子

令
$$\alpha=\{q\in\mathbb{Q}:q\le 0\}\cup\{q\in\mathbb{Q}:q>0,\ q^2<2\}.$$
验证三条后说明: 若 $\alpha=\hat r$ 则 $r^2=2$, 但无理平方不为 2 (标准数论引理). 其他等价写法亦可.

## Q2 加法是 cut

设 $\gamma=\alpha+\beta$.

1. **非空**: 取 $a\in\alpha$, $b\in\beta$. **非全**: 因 $\alpha,\beta\neq\mathbb{Q}$, 存在有理上界 $A\notin\alpha$, $B\notin\beta$; 则 $A+B\notin\gamma$ (若 $A+B=a+b$ 则 $a\ge A$ 或利用向下封闭推出矛盾 — 按课堂/教材写法细化).
2. **向下封闭**: $q=a+b\in\gamma$, $y<q$ $\Rightarrow$ $y=a+(b-(q-y))$, 把差值并入一侧并保持在 cut 内.
3. **无最大**: 对 $q=a+b$, 因 $\alpha$ 无最大, 取 $a'>a$ 仍在 $\alpha$, 则 $a'+b>q$ 在 $\gamma$.

(细节按你 notes 中「有理数运算封闭」写全.)

## Q3 (optional) 非负乘法

定义中含「$q<0$ 或存在正 $a\in\alpha$, 正 $b\in\beta$ 使 $q<ab$」.  
证明时分别处理负部与正部; 无最大元用「可把正因子略放大」.

## Q4 $u=\bigcup_{\alpha\in S}\alpha=\sup S$

1. **上界**: 每个 $\alpha\in S$ 有 $\alpha\subseteq u$, 故 $\alpha\le u$.
2. **最小性**: 若 $v$ 也是上界, 则对所有 $\alpha\in S$ 有 $\alpha\subseteq v$, 故 $u\subseteq v$, 即 $u\le v$.

题面已允许不证 $u$ 本身是 cut.

---

## 写作建议

- 每条公理/定义条件单独成段, 标 (i)(ii)(iii)
- Q1(b) 务必证明「不可能等于某个 $\hat r$」, 不只写出集合
- 交前检查 AI disclosure
