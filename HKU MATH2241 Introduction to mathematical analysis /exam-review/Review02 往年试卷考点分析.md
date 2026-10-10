# MATH2241 往年试卷考点分析

> 材料都在 `docs/archives/previous/`, 与本学期 `test&quiz/Test01 practice.pdf` 分开.
> **这次 Test 1** (2026-10-08 Thu 15:00–15:50, MBG07): **Chapter 1 和 Chapter 2**, Chapter 3 不考. 无计算器. 没有公告允许 cheat sheet.
> 2025 秋的 study guide (`test&quiz/Study guide Test01 2025.pdf`) 把 Test 1 写到 Chapter 2 Part 3 的比较判别 / 极限比较判别. 与这次范围一致.

---

## 1. 考前怎么刷

按这个顺序, 做完就停:

1. **2025 Test 1 整卷** (`docs/archives/previous/test&quiz/Test01 2025.pdf` 第 11 页). 六题都在 Ch1–Ch2. 没有官方解答. 自写: `exam-review/Review03 Test01 2025 解答.md`.
2. **Sample Test 1** (`docs/archives/previous/test&quiz/Sample Test01.pdf`, 有官方解答). 跳过第 3(c) 题 (liminf). 自写: `exam-review/Review04 Sample Test01 解答.md`.
3. **2020-10-09 Test 1** (有官方解答). 跳过第 4 题 (limsup / liminf). 自写: `exam-review/Review05 Test01 2020-10-09 解答.md`.
4. 有余力再做 **Midterm 的 (1)(2)(3)**. 第 (4) 题不要做.

下面这些留到 Test 1 之后: 所有 Test 2、Sample Test 2、2025 Test 2、Midterm (4)、Tut6–Tut8、Chapter 3–4.

---

## 2. 2025 Test 1 (最接近这次)

题在 PDF 第 11 页. 第 12 页只给有序域公理 (O1)–(O5), 给第 5 题用. 没有官方解答. 自写: `exam-review/Review03 Test01 2025 解答.md`.

| 题 | 在考什么 | 这次 |
|---|---|---|
| (1) 4 分 | 用 $\varepsilon$-$N$ **定义** Cauchy 序列 | 做 |
| (2) 5 分 | 一个由 $n$ 写成的集合, 求 $\sup$ 和 $\inf$ 并简述. 分数在 PDF 里排成两行, 以第 11 页为准 | 做. 确界: 先证上/下界, 再说明不能再紧 |
| (3) 5 分 | $\lim n!/n^n$ 是否存在, 并说明 | 做. 序列极限, 可夹逼或写成连乘 |
| (4) 6 分 | 绝对收敛 $\Rightarrow$ 收敛. 比较判别可直接用 | 做. Ch2 Part 3 |
| (5) 4 分 | $\mathbb{Q}(i)=\{a+bi:a,b\in\mathbb{Q}\}$ 按给定加法和乘法是域 (不用验证). 问它是不是有序域, 公理在下一页 | 做. 有序域里平方非负, $i^2=-1$ |
| (6) 6 分 | 有界序列若发散, 是否必有两条极限不同的收敛子列. 证明或举反例 | 做. 单调子列 / Bolzano–Weierstrass |

---

## 3. 有解答、且大部分在范围内

### Sample Test 1

| 题 | 内容 | 这次 |
|---|---|---|
| 1 | $\varepsilon$-$N$ 求 $\lim (n-1)/(n^2-3)$ | 做 |
| 2 | 对每个 $x\in X$ 都有 $y\in Y$ 使 $x\le y$: (a) $\sup X\le\sup Y$; (b) $\inf$ 是否同样 | 做. (b) 要反例 |
| 3 | $c_k=\inf\{b_1,\ldots,b_k\}$: 为何是实数; $(b_n)$ 有界则 $(c_k)$ 收敛; (c) 极限是否等于 $\liminf b_n$ | (a)(b) 做. **(c) 跳过**: 讲义没有 liminf |
| 4 | $a_{n+1}=a_n+b_n$, $b_{n+1}=a_n b_n$, 三个陈述等价 | 做. $(a_n)$ 递增, 三条互推 |
| 5 | 三个判断题: 确界附近必有点; 子列极限相加; 值域在 $\mathbb{R}$ 稠密则序列发散 | 做. (a) 的严格不等式 $a<\sup S$ 要注意最大元 |

解答: `Sample Test01 solution.pdf`. 自写详解: `exam-review/Review04 Sample Test01 解答.md`.

### 2020-10-09 Test 1

| 题 | 内容 | 这次 |
|---|---|---|
| 1 | $S=\{2ab/(a^2+b^2):a,b\in\mathbb{N}\}$, 证 $\sup S=1$, $\inf S=0$ | 做 |
| 2 | $(a_n)$ 收敛且 $|a_n-b_n|<1/n$, 用 **Cauchy 准则** 证 $(b_n)$ 收敛 | 做. 题目指定方法 |
| 3 | $a_1=c\ge 0$, $a_{n+1}=3a_n^2/(a_n^2+2)$, 按 $c$ 讨论极限或发散 | 做. 先看单调与有界 |
| 4 | 另一递推, 证 $\limsup$ 与 $\liminf$ 存在且有限 | **跳过**. 讲义没写这两个词 |
| 5 | 三个判断: 三条子列都收敛是否全列收敛; $c_n=b_n-b_{n^2}\to 0$; $Y=\{1/x\}$ 的下确界是否 $1/\sup X$ | 做 |

解答: `Test01 2020-10-09 solution.pdf`. 自写详解: `exam-review/Review05 Test01 2020-10-09 解答.md`.

### Midterm (只做前三题)

| 题 | 内容 | 这次 |
|---|---|---|
| (1) | $(a_n)\to L$, $x_n>0$ 且 $x_n^2-a_n x_n-1=0$, 证 $(x_n)$ 收敛 | 做 |
| (2) | 每个序列都有单调子列 | 做. 这是单调子列定理的证明 |
| (3) | $\sum k!/k^k$ 收敛还是发散 | 做. 级数 |
| (4) | $\lim_{x\to 0}f(x)=L$ 推出 $\lim_{x\to 0}f(x^2)=L$ | **不做**. 函数极限, Chapter 3 |

解答: `Midterm solution.pdf`.

---

## 4. 只有解答稿的更早 Test 1

题干写在解答里, 没有单独题纸.

| 文件 | 能看出来的题 | 这次 |
|---|---|---|
| `Test01 solution 18-19 first.pdf` | 默写完备性公理; 嵌套区间定理 | 可用来对书上的定理陈述, 不是整卷模拟 |
| `Test01 solution 17-18 second.pdf` | $A=\{m/(m+n)\}$ 的上确界 | 和 2020 第 1 题、2025 第 2 题是同一类 |

---

## 5. 这次不要做

| 材料 | 原因 |
|---|---|
| `Test02 2025.pdf`, `Study guide Test02 2025.pdf` | 函数极限的定义、中值定理、连续函数零点、Thomae 型函数的连续点与是否为某函数的导数 |
| `Sample Test02.pdf` 及解答 | 聚点、函数极限、连续 |
| `Test02 2020-11-13.pdf` 及解答 | 级数判别里夹了后面的内容, 且整卷是 Test 2; 分数报告 `Test02 report.pdf` 只是得分分布 |
| `Test02 2022-11-25.pdf`, `Test02 2023-04-17.pdf` | 可微、连续、不动点、一致连续 |
| `Test02 solution 18-19 first.pdf` | 连续的序列刻画 (当时书上的 Theorem 4.26) |
| `Test02 solution 17-18 second.pdf` | 级数的 Cauchy 准则等, 当书的定理默写; 不是这次卷型 |
| `Lec/Chapter3*.pdf`, `Chapter4.pdf` | 极限与连续、微分 |
| `tut/Tut06` 起 | Tut6 是函数极限定义的等价说法; Tut7 后半和 Tut8 是一致连续 |

Tut1–Tut5 的解答在 `tut/`, 课题是确界、序列、$\sqrt[n]{n}$、级数部分和. 本学期 Tut1–Tut3 已经做过的话, 这些只作对照, 不必再整份重做.
