# Assignment 1 题目理解: Dedekind cuts 构造实数

- **来源**: `assignment/01-assignment-1-dedekind-cuts.pdf`
- **课程**: MATH2241, Fall 2026
- **Due**: 2026-09-14 (Mon) 22:00; Moodle 提交
- **必交**: 第 1, 2, 4 题 (第 3 题 optional)
- **格式**: 写姓名 / UID / Faculty; 文末 **AI-use disclosure**

---

## 总目标

用 **Dedekind cut (戴德金分割)** 从 $\mathbb{Q}$ 构造实数候选集 $\mathbb{R}'$, 验证加法良定义, 并用并集给出上确界 (completeness).

### Dedekind cut 定义 (题面)

$\alpha\subsetneq\mathbb{Q}$ 满足:

1. $\alpha\neq\emptyset$, $\alpha\neq\mathbb{Q}$
2. 向下封闭: $x\in\alpha$, $y<x$ $\Rightarrow$ $y\in\alpha$
3. 无最大元: $\forall x\in\alpha$, $\exists z\in\alpha$ 使 $x<z$

$\mathbb{R}'=$ 全体 Dedekind cuts.

---

## 第 1 题

**(a)** 对每个 $r\in\mathbb{Q}$, 证明 $\hat r:=\{q\in\mathbb{Q}:q<r\}$ 是 Dedekind cut.

**(b)** 给出一个 **不是** 任何 $\hat r$ 的 cut 的例子 (典型: 刻画 $\sqrt{2}$ 的负侧有理数集).

**理解要点**: (a) 检验定义三条; (b) 说明「有理生成」的 cut 装不下无理数对应的分割.

---

## 第 2 题 (必交) — 加法良定义

定义 $\alpha+\beta:=\{q\in\mathbb{Q}:\exists a\in\alpha,\ b\in\beta,\ q=a+b\}$.  
证明 $\alpha+\beta$ 仍是 Dedekind cut.

**理解要点**: 非空/非全; 向下封闭; 无最大元 — 三块分别写清.

---

## 第 3 题 (Optional) — 非负乘法

$\alpha\ge\hat 0$ 指 $\hat 0\subseteq\alpha$. 对非负 cut 定义乘积并证明仍是 cut.

---

## 第 4 题 (必交) — 完备性

$\alpha\le\beta\Leftrightarrow\alpha\subseteq\beta$.  
$S\subseteq\mathbb{R}'$ 非空有上界时, $u:=\bigcup_{\alpha\in S}\alpha$ (题面允许直接用「$u$ 是 cut」).  
证明 $u=\sup S$ (最小上界).

**理解要点**: (i) $u$ 是上界; (ii) 任何更小的候选都不是上界.

---

## 提交提醒

- 只交 1, 2, 4
- AI disclosure: 用了什么工具, 帮了哪些部分, 并声明最终论证可自行讲解
