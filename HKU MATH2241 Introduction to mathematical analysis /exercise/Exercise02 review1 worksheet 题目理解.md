# Exercise02 Review1 Worksheet — 题目理解

- **来源**: `exercise/Exercise02 review1 worksheet.pdf` (原名 `2241_review1_worksheet_Q.pdf`)
- **课程**: MATH2241; STA Review Session 1 (2026-10-05)
- **用途**: Test 1 前复习卷 (无官方 sol; 下列为题意 + 思路)

---

## Problem 1 — 上确界刻画

**题**: $\alpha$ 为 $A$ 上界, 且 $\forall n$ 存在 $a_n\in A$ 使 $\alpha-1/n<a_n$. 证 $\alpha=\sup A$.

**思路**: $\alpha$ 已是上界. 若存在更小上界 $\beta<\alpha$, 取 $n>1/(\alpha-\beta)$ 得 $a_n>\alpha-1/n>\beta$, 矛盾. 故为最小上界.

---

## Problem 2 — 例子 / 不可能

| | 设定 | 结论要点 |
|---|---|---|
| (a) | $a_n$ 收敛, $b_n$ 无界, $a_nb_n$ 收敛 | **可能**: $a_n=0$, $b_n=n$ |
| (b) | $a_n$ 无界, $b_n$ 收敛, $a_n-b_n$ 有界 | **不可能**: $a_n=(a_n-b_n)+b_n$ 有界+收敛 $\Rightarrow$ 有界 |
| (c) | $a_n$ 收敛, $b_n$ 发散, $a_n+b_n$ 收敛 | **不可能**: $b_n=(a_n+b_n)-a_n$ 会收敛 |
| (d) | 两列发散, 但和/积/商皆收敛 | **可能**: $a_n=(-1)^n$, $b_n=(-1)^{n+1}$ (和$\to0$; 积$\to-1$; 商$\to-1$) |

---

## Problem 3 — Babylonian / Newton 开方迭代

$x_1=a>1$, $x_{n+1}=\frac12\bigl(x_n+a/x_n\bigr)$.

- (a) 归纳: $x_n>\sqrt a$ (用 AM-GM 或 $(x-\sqrt a)^2>0$).
- (b) 递减: $x_n-x_{n+1}=\frac1{2x_n}(x_n^2-a)>0$; MCT $\Rightarrow$ 收敛, 极限 $L=\sqrt a$.

---

## Problem 4 — $x_{n+1}=x_n+1/x_n$

$x_1=a>0$. **发散** (到 $+\infty$): 递增且无上界 (若收敛到有限 $L$ 则 $1/L=0$ 矛盾); 或 $x_{n+1}^2\ge x_n^2+2$ $\Rightarrow$ $x_n^2\ge a^2+2(n-1)$.

---

## Problem 5 — 几何型相邻差 $\Rightarrow$ Cauchy

$|a_{n+2}-a_{n+1}|\le\alpha|a_{n+1}-a_n|$, $0<\alpha<1$.

**思路**: $|a_{n+k}-a_n|\le |a_2-a_1|(\alpha^{n-1}+\cdots+\alpha^{n+k-2})\le |a_2-a_1|\alpha^{n-1}/(1-\alpha)$; 故 Cauchy.

---

## Problem 6 — 级数收敛性

| | 级数 | 结论 |
|---|---|---|
| (a) | $\sum n^2/n!$ | 收敛 (Ratio $\to0$, 或与指数级数比) |
| (b) | $\sum(\sqrt{n+1}-\sqrt n)$ | 发散 (通项 $\sim 1/(2\sqrt n)$, 或望远镜 $\to\infty$) |
| (c) | $\sum n!/n^n$ | 收敛 (Ratio $\to0$) |
| (d) | $\sum_{n\ge2}1/(\sqrt n\log n)$ | 发散 (积分判别 / Cauchy 凝缩 / 比谐和) |

---

## Problem 7 — 绝对收敛 $\Rightarrow$ $\sum a_n^3$ 收敛

(a) 绝对收敛 $\Rightarrow$ $a_n\to0$ $\Rightarrow$ 大 $n$ 时 $|a_n|<1$ $\Rightarrow$ $|a_n^3|\le|a_n|$; 比较得 $\sum a_n^3$ 绝对收敛 (从而收敛).

(b) 对奇数 $k$: 同理 $|a_n|^k\le|a_n|$ 最终成立. 对偶数 $k$: 同样绝对收敛. (若仅条件收敛, 立方等可能改变收敛性 — 本问在绝对假设下.)

---

## Problem 8 — Root vs Ratio

经典构造用「奇偶块」改系数, 使比值极限不存在而根极限存在:

- (a) 发散且 Root 判出发散, Ratio 无信息: 如 $a_n=2^n$ (偶) / $3^n$ (奇) 等块构造使 $\limsup\sqrt[n]{|a_n|}>1$.
- (b) 收敛且 Root 判出收敛, Ratio 无信息: 如 Tut3 Q6 型 $a_n=2^{-n}$ 或 $3\cdot2^{-n}$ 交替; $\sqrt[n]{a_n}\to1/2$, 比值极限不存在.

(具体系数以课堂/标准教材例为准; 核心是 **Root 用 limsup, Ratio 要极限存在**.)

---

## 与 Test1 关系

覆盖 Ch1 确界 + Ch2 序列/Cauchy/级数. 建议与 `Test01 practice` 及 Tut1–3 交错做.
