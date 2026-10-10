# 题集 — Chapter 1 Real Numbers

> 对齐: `Lec/Lec02 chapter1 real numbers 讲义.md`.
> 含: (1) 练习题 (A1 / Tut1 / Bartle / 讲义练习) (2) 课件证明.

## 课件证明

### P1. 正数平方比较 (Exercise 1.7(g))

- **陈述**: **假设** $0<a,b$; **结论** $a<b\iff a^2<b^2$.
- **证明**:
  1. ($\Rightarrow$) 由 $a<b$ 得 $b-a>0$; 又 $a,b>0$ 故 $a+b>0$. 于是 $b^2-a^2=(b-a)(b+a)>0$, 即 $a^2<b^2$.
  2. ($\Leftarrow$) 反证: 若 $a\ge b>0$, 则由 (1) 的反向 (或同理) 得 $a^2\ge b^2$, 与 $a^2<b^2$ 矛盾. 故必有 $a<b$.
- **来源**: `Lec/Lec02 chapter1 real numbers 讲义.md` §2

### P2. 定理 3.3 (上确界判别法, Supremum characterization)

- **陈述**: **假设** $S\subseteq\mathbb{R}$ 非空有上界, $u$ 为上界; **结论** $u=\sup S\iff \forall\varepsilon>0\ \exists x\in S$ 使 $u-x<\varepsilon$.
- **证明**:
  1. ($\Rightarrow$) 设 $u=\sup S$. 对任意 $\varepsilon>0$, $u-\varepsilon$ 不是上界, 故存在 $x\in S$ 使 $x>u-\varepsilon$, 即 $u-x<\varepsilon$.
  2. ($\Leftarrow$) 设对每个 $\varepsilon>0$ 都存在上述 $x$. 若另有上界 $v<u$, 取 $\varepsilon=u-v>0$, 则存在 $x\in S$ 使 $x>v$, 与 $v$ 为上界矛盾. 故 $u=\sup S$.
- **来源**: 同上 §4

### P3. 推论 4.6 ($\mathbb{Q}$ 稠密性, Density of rationals)

- **陈述**: **假设** $a<b\in\mathbb{R}$; **结论** 存在有理数 $r$ 使 $a<r<b$.
- **证明**:
  1. 由 Archimedes, 取 $n\in\mathbb{N}$ 使 $n(b-a)>1$, 即 $1/n<b-a$.
  2. 再取整数 $m$ 使 $m-1\le na<m$ (Archimedes / 整数存在性).
  3. 则 $a<m/n$ 且 $m/n\le a+1/n<a+(b-a)=b$. 取 $r=m/n\in\mathbb{Q}$ 即可.
- **来源**: 同上 §5

### P4. 定理 4.8 ($\sqrt2$ 非有理)

- **陈述**: **结论** 无有理数 $x$ 满足 $x^2=2$.
- **证明**:
  1. 反证: 设 $x=p/q$, 其中 $p,q\in\mathbb{Z}$, $q>0$, $\gcd(p,q)=1$, 且 $p^2=2q^2$.
  2. 则 $p^2$ 为偶数, 故 $p$ 为偶数. 写 $p=2r$, 代入得 $4r^2=2q^2$, 即 $q^2=2r^2$, 故 $q$ 亦偶.
  3. 这与 $\gcd(p,q)=1$ 矛盾. 故无这样的有理数.
- **来源**: 同上 §5

### P5. 定理 4.9 ($\sqrt2$ 存在且无理)

- **陈述**: **结论** $x=\sup\{y\ge0:y^2<2\}$ 满足 $x^2=2$ 且 $x\notin\mathbb{Q}$.
- **证明**:
  1. 令 $S=\{y\ge0:y^2<2\}$. $S$ 非空有上界, 由完备性取 $x=\sup S$.
  2. 若 $x^2<2$: 可取充分小 $h>0$ 使 $(x+h)^2<2$, 则 $x+h\in S$, 与 $x=\sup S$ 矛盾.
  3. 若 $x^2>2$: 可取充分小 $h>0$ 使 $(x-h)^2>2$, 则 $x-h$ 也是 $S$ 的上界且 $<x$, 矛盾.
  4. 故 $x^2=2$. 由 P4 知 $x\notin\mathbb{Q}$.
- **来源**: 同上 §5

### P6. 定理 5.8 ($[0,1]$ 不可数)

- **陈述**: **结论** $[0,1]$ 不可数.
- **证明**:
  1. 反证: 设 $[0,1]=\{x_n\}_{n=1}^\infty$, 写小数 $x_n=0.a_{n1}a_{n2}\ldots$ (约定避开无限 $9$).
  2. 构造 $y=0.b_1b_2\ldots\in[0,1]$, 使每个 $b_k\neq a_{kk}$ (例如 $a_{kk}\neq 4$ 则取 $b_k=4$, 否则取 $5$).
  3. 则对一切 $n$, $y$ 与 $x_n$ 在第 $n$ 位不同, 故 $y\neq x_n$. 矛盾. 因此 $[0,1]$ 不可数.
- **来源**: 同上 §6

### P7. 定理 5.5 (嵌套区间性质, Nested Interval Property)

- **陈述**: **假设** 闭区间 $[a_n,b_n]$ 嵌套; **结论** $\bigcap_{n=1}^\infty[a_n,b_n]\ne\emptyset$.
- **证明**:
  1. 令 $A=\{a_n:n\in\mathbb{N}\}$. 嵌套蕴含每个 $b_m$ 是 $A$ 的上界, 故 $A$ 有上界. 取 $c=\sup A$.
  2. 对任意固定 $n$: 由上确界定义 $a_n\le c$; 又对一切 $m$, $a_m\le b_n$ (嵌套), 故 $c\le b_n$.
  3. 于是 $c\in[a_n,b_n]$ 对一切 $n$, 即交非空.
- **来源**: 同上 §6

### P8. 命题 1.5 域推论 ($0a=0$ 等)

- **陈述**: 在域 $F$ 中, $0a=0$, $-(-a)=a$, $(-a)(-b)=ab$.
- **证明**:
  1. $0a=(0+0)a=0a+0a$. 两边加 $-(0a)$ 得 $0a=0$.
  2. 由加法逆唯一性, $-(-a)=a$.
  3. $(-a)(-b)+(-a)b=(-a)((-b)+b)=(-a)\cdot 0=0$, 故 $(-a)(-b)$ 是 $(-a)b$ 的加法逆, 而 $(-a)b=-(ab)$, 其逆为 $ab$. 故 $(-a)(-b)=ab$.
- **来源**: 同上 §1

### P9. $\mathbb{Q}(i)$ 不可有序

- **陈述**: **结论** $\mathbb{Q}(i)$ (故 $\mathbb{C}$) 不能成为有序域.
- **证明**:
  1. 在任何有序域中, 若 $a\neq 0$ 则 $a^2>0$ (由有序公理).
  2. 取 $a=i$: $i\neq 0$ 却 $i^2=-1$. 若 $-1>0$ 则与 $1>0$ 及加法相容矛盾.
  3. 故 $\mathbb{Q}(i)$ (及 $\mathbb{C}$) 不能成为有序域.
- **来源**: 同上 §2

### P10. $\mathbb{Q}$ 不完备

- **陈述**: **假设** $S=\{x\in\mathbb{Q}:x^2<2\}$; **结论** $S$ 在 $\mathbb{Q}$ 中无上确界.
- **证明**:
  1. 反证: 设有理数 $u=\sup_{\mathbb{Q}} S$.
  2. 由 P4 不能有 $u^2=2$.
  3. 若 $u^2<2$: 可取充分小正有理 $h$ 使 $(u+h)^2<2$, 则 $u+h\in S$ 且 $>u$, 矛盾.
  4. 若 $u^2>2$: 可取充分小正有理 $h$ 使 $(u-h)^2>2$, 则 $u-h$ 仍是 $S$ 的有理上界且 $<u$, 矛盾.
  5. 故 $S$ 在 $\mathbb{Q}$ 中无上确界.
- **来源**: 同上 §4

## 练习题

### 1. 有理 cut

- **题目**: 对每个 $r\in\mathbb{Q}$, 证 $\hat r=\{q\in\mathbb{Q}:q<r\}$ 是 Dedekind cut.
- **思路**: 非空/非全; 向下封闭; 无最大元 (取 $(x+r)/2$).
- **来源**: A1 Q1(a) / `assignment/Assignment01 dedekind cuts 解答.md`

### 2. 非有理 cut ($\sqrt2$)

- **题目**: 给出一个不等于任何 $\hat r$ 的 cut.
- **思路**: $\alpha=\{q:q\le0\}\cup\{q>0,q^2<2\}$; 反证 $\alpha=\hat r$ 得 $r^2=2$.
- **来源**: A1 Q1(b)

### 3. cut 加法良定义

- **题目**: $\alpha+\beta=\{a+b:a\in\alpha,b\in\beta\}$ 仍是 cut.
- **思路**: 非空; $A+B\notin\alpha+\beta$; 向下封闭; 无最大元.
- **来源**: A1 Q2 (必交)

### 4. (Optional) 非负 cut 乘法

- **题目**: $\alpha,\beta\ge\hat0$ 时题面乘积仍是 cut.
- **思路**: 负有理兜底; 上界不在积中; 无最大元.
- **来源**: A1 Q3 / `assignment/Assignment01 dedekind cuts 解答.md`

### 5. $u=\sup S$ 为并 cut

- **题目**: 非空有上界 $S\subseteq\mathbb{R}'$, $u=\bigcup_{\alpha\in S}\alpha$. 证 $u=\sup S$.
- **思路**: $\alpha\subseteq u$; 任一上界 $v$ 含各 $\alpha$ 故 $u\subseteq v$.
- **来源**: A1 Q4 (必交)

### 6. $a<b+\varepsilon$ $\forall\varepsilon>0$

- **题目**: 证 $a\le b$.
- **思路**: 反证 $a>b$, $\varepsilon=(a-b)/2$.
- **来源**: Tut1 Q1 / `tut/Tut01 总结.md`

### 7. 求 sup/inf (三集合)

- **题目**: (i) $S_1=\{x\neq0:1/x>2\}$; (ii) $S_2=\{1/k+2/m+3/n:k,m,n\in\mathbb{N}\}$; (iii) $S_3=\{3^x:x\in\mathbb{Z}\}$. 求 sup/inf, 判 max/min.
- **思路**: (i) $(0,1/2)$, sup=$1/2$ 非 max, inf=$0$ 非 min; (ii) inf=sup min=6, sup=$+\infty$; (iii) inf=$0$ 非 min, sup=$+\infty$.
- **来源**: Tut1 Q2

### 8. $\inf A=\sup A$

- **题目**: 非空有界 $A$, $\inf A=\sup A$ $\Rightarrow$ $A$ 单点.
- **思路**: 若两不同元则区间长度正.
- **来源**: Tut1 Q3

### 9. 子集确界

- **题目**: $A\subseteq B$ 非空有界 $\Rightarrow$ $\inf B\le\inf A\le\sup A\le\sup B$.
- **思路**: 上/下界定义.
- **来源**: Tut1 Q4

### 10. $A+B$, $AB$ 的 sup

- **题目**: (a) $\sup(A+B)=\sup A+\sup B$? (b) $\sup(AB)=(\sup A)(\sup B)$? 判真假.
- **思路**: (a) 通常证真; (b) 对符号/负元取反例.
- **来源**: Tut1 Q5

### 11. 序列逼近 sup

- **题目**: $w$ 上界, 且 $\forall n\ \exists a_n\in A$, $w-1/n\le a_n$. 证 $w=\sup A$.
- **思路**: 定理 3.3, $\varepsilon=1/n$.
- **来源**: Tut1 Q6

### 12. sup 有理/无理对调例子

- **题目**: 无理集 sup 为有理; 有理集 sup 为无理, 各举一例.
- **思路**: 如 $\{q\in\mathbb{Q}:q^2<2\}$ 在 $\mathbb{R}$ 中 sup=$\sqrt2$.
- **来源**: Tut1 Q7

### 13. 根式无理性

- **题目**: (a) $\sqrt[m]{n}$ 整数或无理; (b) $\sqrt n+\sqrt{n+1}$ 无理; (c) $\sqrt{n+\sqrt n}$ 无理.
- **思路**: 反证平方; 既约分数.
- **来源**: Tut1 Q8

### 14. Bartle §2.1 Ex 4

- **题目**: 见 `exercise/Exercise01 extra bartle.pdf` §2.1 第 4 题 (域公理).
- **思路**: 对照 Ch1 讲义 §1.
- **来源**: Extra / `exercise/Exercise01 extra bartle 题目理解.md`

### 15. Bartle §2.1 Ex 5

- **题目**: 见 PDF §2.1 Ex 5.
- **思路**: 域公理推导.
- **来源**: Extra

### 16. Bartle §2.1 Ex 12

- **题目**: 见 PDF §2.1 Ex 12.
- **思路**: 有序域.
- **来源**: Extra

### 17. Bartle §2.1 Ex 13

- **题目**: 见 PDF §2.1 Ex 13.
- **思路**: 有序域.
- **来源**: Extra

### 18. Bartle §2.3 Ex 5, 10, 11

- **题目**: 见 PDF §2.3 (sup/inf 相关).
- **思路**: 确界判别与例子.
- **来源**: Extra

### 19. Bartle 完备性主题 Ex 2, 4, 19

- **题目**: 见 PDF 题面 (Archimedean / 稠密 / 无理).
- **思路**: 定理 4.x 系列.
- **来源**: Extra

### 20. 练习 1.2 唯一性

- **题目**: 用公理证 $0,1,-a,1/a$ 唯一.
- **思路**: 设两个单位元相等.
- **来源**: Lec Ch1 §1

### 21. 练习 1.7

- **题目**: $a^2>0$, $0<1$, $0<a\Rightarrow0<a^{-1}$, $1+1\ne0$; (g) $0<a,b\Rightarrow(a<b\iff a^2<b^2)$.
- **思路**: 三分性; $(b-a)(b+a)$.
- **来源**: Lec Ch1 §2

### 22. $\mathbb{Q}(i)$ 不可有序

- **题目**: 证 $\mathbb{Q}(i)$ (或 $\mathbb{C}$) 不能有序域.
- **思路**: $i^2=-1>0$ 矛盾.
- **来源**: Lec Ch1 Ex 1.10

### 23. $\mathbb{Q}$ 中无 max 例

- **题目**: $S=\{x\in\mathbb{Q}:0\le x<8\}$ 是否有 max?
- **思路**: 有上界无最大元.
- **来源**: Lec Ch1 §3

### 24. $\mathbb{Q}$ 不完备

- **题目**: $S=\{x\in\mathbb{Q}:x^2<2\}$ 在 $\mathbb{Q}$ 中无上确界.
- **思路**: 假设有理 sup 导致 $u^2=2$ 或逼近矛盾.
- **来源**: Lec Ch1 §4

### 25. $\sqrt2$ 存在且无理

- **题目**: 无有理 $x^2=2$; $x=\sup\{y\ge0:y^2<2\}$ 满足 $x^2=2$.
- **思路**: 既约分数; 完备性 + $h$ 构造.
- **来源**: Lec Ch1 定理 4.8–4.9

### 26. 可数性

- **题目**: $\mathbb{Z},\mathbb{N}^2,\mathbb{Q}$ 可数; $[0,1]$ 不可数; 无理不可数.
- **思路**: 对角枚举; Cantor 对角线.
- **来源**: Lec Ch1 §6

### 27. 嵌套区间

- **题目**: 闭区间套, 证交非空.
- **思路**: $c=\sup a_n\in\bigcap$.
- **来源**: Lec Ch1 定理 5.5

### 28. Exercise 1.7(g) 正数条件

- **题目**: 说明 $a<b\iff a^2<b^2$ 需 $a,b>0$.
- **思路**: 反例: $-2<-1$ 但 $4>1$.
- **来源**: Lec Ch1 易错点
