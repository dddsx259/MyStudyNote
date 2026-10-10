# 题集 — Tutorial 1: Decode the Rhind Papyrus

> 对齐: `tut/2026-09-15 tut01/Tut01 worksheet.docx`, `Lec/Lec02 Numbers/`, `Lec/Lec06 Student Version/`.
> 含: (1) 课件证明 (2) 练习题.

---

## 课件证明

本章主体为 Rhind **算题程序** 与 Tut 练习; 对齐讲义 Lec02 记数文化, Lec06 古代程序, **无讲义级命名定理**. 下列为 worksheet 要求论证的算术事实 (与埃及加倍算法同源).

### P1. 埃及「加倍表」整数乘法正确

- **陈述**: 对被乘数 $n$ 与乘数 $m$, 列出 $n,2n,4n,\ldots$ 直至超过 $m$, 再选取行号对应 $2^k$ 且 $\sum 2^k=m$ 的那些行相加, 则和为 $nm$.
- **证明**: 每个正整数 $m$ 有唯一二进制表示 $m=\sum_{k\in S}2^k$ ($S$ 为指标集). 加倍表第 $k$ 行存 $2^k n$. 选中行之和为 $n\sum_{k\in S}2^k=nm$. 例: $m=13=1+4+8$ 时 $11\times 13=11+44+88=143$.
- **来源**: Tut1 worksheet §B Question 2; 算法背景见 `Lec/Lec06 Student Version/Lec06 Student Version 讲义.md` 古代程序

### P2. Rhind Problem 79 事物总数 (有限等比和)

- **陈述**: 7 座房, 每房 7 猫, 每猫 7 鼠, 每鼠 7 麦粒, 每粒 7 hekat, 各级计数之和为 $19607$.
- **证明**: 各级数量为 $7,7^2,\ldots,7^5$. 和 $S=7+7^2+\cdots+7^5=7\frac{7^5-1}{7-1}=7\times 2801=19607$.
- **来源**: Tut1 worksheet §F Problem 79; Answer 19607

> 讲义 Lec02 中 $\sqrt{2}$ 无理等完整证明见 [02-lecture-examples](题集02 lecture examples.md).

---

## 练习题

## A. 记数系统

### 1. 读象形数字

- **题目**: (Question 1) 根据 worksheet 右侧 **埃及象形数字图** (见 docx), 该图表示的十进制整数是多少?
- **思路**: 按符号量级 (1, 10, 100, …) 累加; 对照 Lec02 埃及笔画/踵/绳/睡莲等单位.
- **来源**: `tut/2026-09-15 tut01/Tut01 worksheet.docx` §A Q1 (图在 docx)

### 2. 写出 246709

- **题目**: 用古埃及 **十进制象形系统** 写出 $246709$.
- **思路**: 从高位到低位选各量级符号个数 (重复笔画等规则见课件); 无占位零则省略该位符号.
- **来源**: Tut1 worksheet §A (246709 小问)

---

## B. 乘法

### 3. 解释「加倍表」乘法

- **题目**: 埃及人用 1, 2, 4, 8, … 加倍被乘数, 再选行相加得到积 (例: $13=1+4+8$, 故 $11\times 13 = 11+44+88 = 143$). **为何**对整数乘法正确?
- **思路**: 见 **P1** (二进制分解).
- **来源**: Tut1 worksheet §B Question 2

---

## C. 单位分数 (Egyptian fractions)

### 4. 将 $2/7$, $2/9$ 表为不同单位分数之和

- **题目**: (Q3a) 把 $\frac{2}{7}$, $\frac{2}{9}$ 写成 **分子为 1、分母互异** 的单位分数之和 (可查 Rhind $2/n$ 表或贪心: 取不超过余量的最大单位分数).
- **思路**: 例 $\frac{2}{7}=\frac{1}{4}+\frac{1}{28}$; $\frac{2}{9}=\frac{1}{6}+\frac{1}{18}$ (答案不唯一, 需 distinct denominators).
- **来源**: Tut1 worksheet §C Q3a

### 5. 埃及如何表示 $7/9$

- **题目**: (Q3b) 古埃及如何把 $\frac{7}{9}$ 写成单位分数和? (可联系 Horus Eye 对 $1/2,1/4,\ldots$ 的表示.)
- **思路**: 常见拆法如 $\frac{2}{3}+\frac{1}{9}$ 或 $\frac{1}{2}+\frac{1}{4}+\frac{1}{36}$ 等; 对照 worksheet 与 Lec02 埃及分数文化背景.
- **来源**: Tut1 worksheet §C Q3b

---

## D–F. 纸草书经典题

### 6. Rhind Problem 31 (一元一次方程)

- **题目**: 「某量, 其 $\frac{2}{3}$, 其 $\frac{1}{2}$, 其 $\frac{1}{7}$, 再加该量本身, 总和为 33. 求该量.」用现代代数求解.
- **思路**: 设量为 $x$, $x+\frac{2}{3}x+\frac{1}{2}x+\frac{1}{7}x=33$, 通分得 $x=\frac{33}{\frac{139}{42}}=\frac{1386}{139}$ (纸草书用单位分数表答案, 约 $14\frac{4}{97}+\cdots$).
- **来源**: Tut1 worksheet §D (Problem 31)

### 7. Rhind Problem 40 (等差分配)

- **题目**: 100 块饼分给 5 人, 份额成 **等差数列**, 且 **最大三份之和的 $\frac{2}{3}$** 等于 **最小两份之和**. 求每人份数.
- **思路**: 设五份 $a,a+d,\ldots,a+4d$, $\sum=100$; 条件 $\frac{2}{3}[(a+2d)+(a+3d)+(a+4d)]=(a)+(a+d)$ 与 $5a+10d=100$ 联立 (docx 若 OCR 成 "17" 应以 $\frac{2}{3}$ 为准).
- **来源**: Tut1 worksheet §E (Problem 40)

### 8. Rhind Problem 79 / St Ives (几何级数)

- **题目**: 7 座房, 每房 7 猫, 每猫 7 鼠, 每鼠 7 麦粒, 每粒可产 7 hekat. **一共提到多少事物**? ( nursery rhyme 「去 St Ives」与纸草版本: 数的是各级总数之和, 不是只数「去 St Ives 的人」.)
- **思路**: 见 **P2**.
- **来源**: Tut1 worksheet §F (Problem 79; Answer 19607)

### 9. (拓展, 非必做) 任意正有理数的埃及分数

- **题目**: worksheet 称任意正有理数可表为 distinct unit fractions 之和; **贪心算法** 如何做? (课程注明不必证明.)
- **思路**: repeatedly 取 $\frac{1}{\lceil b/a\rceil}$ 并从 $\frac{a}{b}$ 减去, 直到为 0; 与 Greedy / Eye of Horus 算法并列提及.
- **来源**: Tut1 worksheet §C 说明文字
