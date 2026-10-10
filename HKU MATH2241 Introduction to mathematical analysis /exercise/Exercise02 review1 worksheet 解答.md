# Exercise02 Review1 Worksheet — 解答

- **来源**: `exercise/Exercise02 review1 worksheet.pdf`
- **课程**: MATH2241; STA Review Session 1 (2026-10-05)
- **说明**: 完整解答稿, 交稿前自行核对. 定理编号对齐 Ch2 Part 3 讲义 (Root/Ratio = Thm 3.16/3.17).

---

## 1.

**题意**: $A\subset\mathbb{R}$ 非空, $\alpha$ 为 $A$ 的上界, 且对每个 $n\in\mathbb{N}$ 存在 $a_n\in A$ 使 $\alpha-1/n<a_n$. 证 $\alpha=\sup A$.

**目标**: 证 $\alpha$ 是最小上界.

$\alpha$ 已是上界, 故只需证: 任何 $\beta<\alpha$ 都不是上界.

设 $\beta<\alpha$. 由 Archimedes, 存在 $n\in\mathbb{N}$ 使
$$
\frac1n<\alpha-\beta\qquad\text{即}\qquad \alpha-\frac1n>\beta.
$$
由题设, 存在 $a_n\in A$ 使 $a_n>\alpha-1/n>\beta$. 故 $\beta$ 不是 $A$ 的上界.

因此 $\alpha$ 是 $A$ 的最小上界, 即 $\alpha=\sup A$.

**结论**: $\alpha=\sup A$.

---

## 2.

### (a)

**题意**: $\{a_n\}$ 收敛, $\{b_n\}$ 无界, $\{a_nb_n\}$ 收敛. 给例或证不可能.

**例子** (可能): 取 $a_n=0$, $b_n=n$. 则 $a_n\to 0$, $\{b_n\}$ 无界, $a_nb_n=0\to 0$.

(另一例: $a_n=1/n$, $b_n=n$, 则 $a_nb_n=1\to 1$.)

**结论**: 可能. 上例即可.

### (b)

**题意**: $\{a_n\}$ 无界, $\{b_n\}$ 收敛, $\{a_n-b_n\}$ 有界. 给例或证不可能.

**证明不可能**. 收敛序列有界, 故存在 $M_1$ 使 $|b_n|\le M_1$ 对一切 $n$. 若 $|a_n-b_n|\le M_2$ 对一切 $n$, 则
$$
|a_n|=|(a_n-b_n)+b_n|\le |a_n-b_n|+|b_n|\le M_2+M_1,
$$
故 $\{a_n\}$ 有界, 矛盾.

**结论**: 不可能.

### (c)

**题意**: $\{a_n\}$ 收敛, $\{b_n\}$ 发散, $\{a_n+b_n\}$ 收敛. 给例或证不可能.

**证明不可能**. 若 $a_n\to A$ 且 $a_n+b_n\to C$, 则
$$
b_n=(a_n+b_n)-a_n\to C-A,
$$
与 $\{b_n\}$ 发散矛盾. (代数极限定理.)

**结论**: 不可能.

### (d)

**题意**: $\{a_n\},\{b_n\}$ 都发散, 但 $\{a_n+b_n\}$, $\{a_nb_n\}$, $\{a_n/b_n\}$ 都收敛. 给例或证不可能.

**例子** (可能): 取
$$
a_n=(-1)^n,\qquad b_n=(-1)^{n+1}.
$$
二者均不收敛 (两项子列极限分别为 $\pm 1$). 且 $b_n\neq 0$. 同时
$$
a_n+b_n=0\to 0,\qquad a_nb_n=-1\to -1,\qquad \frac{a_n}{b_n}=-1\to -1.
$$

**结论**: 可能. 上例即可.

---

## 3.

设 $a>1$, $x_1=a$, $x_{n+1}=\dfrac12\bigl(x_n+a/x_n\bigr)$.

### (a)

**目标**: 归纳证 $x_n>\sqrt a$ 对一切 $n\in\mathbb{N}$.

**基步**: $a>1$ $\Rightarrow$ $a^2>a$ $\Rightarrow$ $a>\sqrt a$ (正根). 故 $x_1=a>\sqrt a$.

**归纳步**: 设 $x_n>\sqrt a$ (从而 $x_n>0$). 则
$$
x_{n+1}-\sqrt a=\frac12\Bigl(x_n+\frac a{x_n}\Bigr)-\sqrt a=\frac{(x_n-\sqrt a)^2}{2x_n}.
$$
分子 $>0$ (归纳假设给出严格不等式), 分母 $>0$, 故 $x_{n+1}>\sqrt a$.

由归纳, 对一切 $n$ 有 $x_n>\sqrt a$.

**结论**: $x_n>\sqrt a$ ($\forall n$).

### (b)

**目标**: 证递减, 从而收敛, 并求极限.

由 (a), $x_n^2>a$, 且 $x_n>0$, 故
$$
x_n-x_{n+1}=x_n-\frac12\Bigl(x_n+\frac a{x_n}\Bigr)=\frac{x_n^2-a}{2x_n}>0.
$$
因此 $x_{n+1}<x_n$, 即 $\{x_n\}$ 递减. 又由 (a) 有下界 $\sqrt a$, 单调收敛定理给出 $x_n\to L$ 对某 $L\ge\sqrt a$.

递推两边取极限 (极限运算): $L=\dfrac12\bigl(L+a/L\bigr)$. 因 $L\ge\sqrt a>0$, 可乘 $2L$ 得 $2L^2=L^2+a$, 即 $L^2=a$, 故 $L=\sqrt a$ (负根舍去).

**结论**: $\{x_n\}$ 递减且有下界, 故收敛; $\lim x_n=\sqrt a$.

---

## 4.

设 $x_1=a>0$, $x_{n+1}=x_n+1/x_n$. 判断敛散.

**单调**: $x_n>0$ 对一切 $n$ (归纳显然), 故 $x_{n+1}-x_n=1/x_n>0$, 序列严格递增.

**无 (有限) 上界**: 平方,
$$
x_{n+1}^2=x_n^2+2+\frac1{x_n^2}\ge x_n^2+2.
$$
迭代得
$$
x_n^2\ge x_1^2+2(n-1)=a^2+2(n-1)\to+\infty.
$$
故 $x_n\to+\infty$, 作为实数列发散.

(若假设收敛到有限 $L$, 则 $L=L+1/L$ $\Rightarrow$ $1/L=0$, 不可能.)

**结论**: 发散 (实际上 $x_n\to+\infty$).

---

## 5.

设 $0<\alpha<1$, 且 $|a_{n+2}-a_{n+1}|\le\alpha|a_{n+1}-a_n|$ 对一切 $n\in\mathbb{N}$. 证 $\{a_n\}$ 为 Cauchy (从而收敛).

**目标**: 把 $|a_{n+k}-a_n|$ 用几何级数控制.

对 $m\ge 1$ 归纳得
$$
|a_{m+1}-a_m|\le\alpha^{m-1}|a_2-a_1|.
$$
($m=1$ 显然; 递推用题设.) 于是对 $k\ge 1$,
$$
\begin{align*}
|a_{n+k}-a_n|
&\le\sum_{j=0}^{k-1}|a_{n+j+1}-a_{n+j}|
\le |a_2-a_1|\sum_{j=0}^{k-1}\alpha^{n+j-1}\\
&= |a_2-a_1|\,\alpha^{n-1}\sum_{j=0}^{k-1}\alpha^j
\le |a_2-a_1|\,\frac{\alpha^{n-1}}{1-\alpha}.
\end{align*}
$$
因 $\alpha^{n-1}\to 0$, 对任意 $\varepsilon>0$ 存在 $N$ 使 $n\ge N$ 时右边 $<\varepsilon$. 从而当 $m,n\ge N$ 时 $|a_m-a_n|<\varepsilon$. 故 $\{a_n\}$ 是 Cauchy. $\mathbb{R}$ 完备 $\Rightarrow$ 收敛.

**结论**: $\{a_n\}$ 是 Cauchy, 因而收敛.

---

## 6.

### (a)

级数 $\displaystyle\sum\frac{n^2}{n!}$.

比值检验: $x_n=n^2/n!>0$,
$$
\frac{x_{n+1}}{x_n}=\frac{(n+1)^2}{(n+1)!}\cdot\frac{n!}{n^2}=\frac{(n+1)^2}{(n+1)n^2}=\frac{n+1}{n^2}\to 0<1.
$$
故绝对收敛, 从而收敛.

**结论**: 收敛.

### (b)

级数 $\displaystyle\sum\bigl(\sqrt{n+1}-\sqrt n\bigr)$.

有理化:
$$
\sqrt{n+1}-\sqrt n=\frac{1}{\sqrt{n+1}+\sqrt n}\ge\frac{1}{2\sqrt{n+1}}.
$$
$\sum 1/\sqrt{n}$ 为 $p=1/2$ 的 $p$-级数, 发散; 比较 (或极限比较, 通项 $\sim 1/(2\sqrt n)$) 得原级数发散.

(望远镜: 部分和 $s_N=\sqrt{N+1}-\sqrt 1\to+\infty$.)

**结论**: 发散.

### (c)

级数 $\displaystyle\sum\dfrac{n!}{n^n}$.

比值:
$$
\frac{x_{n+1}}{x_n}=\frac{(n+1)!}{(n+1)^{n+1}}\cdot\frac{n^n}{n!}=\frac{n^n}{(n+1)^n}=\Bigl(\frac{n}{n+1}\Bigr)^n=\Bigl(1-\frac1{n+1}\Bigr)^n\to\frac1e<1.
$$
故收敛.

**结论**: 收敛.

### (d)

级数 $\displaystyle\sum_{n=2}^\infty\frac{1}{\sqrt n\,\log n}$.

通项正且最终递减. Cauchy 凝缩: 令 $b_k=2^k a_{2^k}$,
$$
2^k\cdot\frac{1}{\sqrt{2^k}\,\log(2^k)}=\frac{2^{k/2}}{k\log 2}.
$$
$\sum 2^{k/2}/k$ 发散 (通项 $\to+\infty$, 或比几何 $\sum r^k$ 对任意 $r\in(1,\sqrt 2)$). 凝缩检验给出原级数发散.

(积分: $u=\log x$, $x=e^u$, $\displaystyle\int_2^\infty\frac{dx}{\sqrt x\log x}=\int_{\log 2}^\infty\frac{e^{u/2}}{u}\,du=+\infty$.)

**结论**: 发散.

---

## 7.

### (a)

**假设**: $\sum a_k$ 绝对收敛, 即 $\sum |a_k|<\infty$.

**目标**: $\sum a_k^3$ 收敛.

绝对收敛 $\Rightarrow$ $a_n\to 0$, 故存在 $N$ 使 $n\ge N$ 时 $|a_n|<1$. 此时
$$
|a_n^3|=|a_n|^3\le |a_n|.
$$
比较检验: $\sum_{n\ge N}|a_n|$ 收敛 $\Rightarrow$ $\sum_{n\ge N}|a_n^3|$ 收敛. 有限项不影响, 故 $\sum |a_n^3|<\infty$, 即 $\sum a_n^3$ 绝对收敛, 从而收敛.

**结论**: $\sum a_n^3$ 收敛 (且绝对收敛).

### (b)

对其他整数 $k$:

- 若 $k\in\mathbb{N}$, $k\ge 1$: 同样 $a_n\to 0$ $\Rightarrow$ 最终 $|a_n|<1$, 从而 $|a_n|^k\le |a_n|$. 故绝对收敛推出 $\sum a_n^k$ **绝对收敛**.
- 若 $k=0$: 对 $a_n\neq 0$ 有 $a_n^0=1$, $\sum 1$ 发散 (原级数绝对收敛时最终 $a_n\neq 0$ 可不成立, 但若无穷多项非零则仍发散).
- 若 $k\le -1$: $a_n\to 0$ $\Rightarrow$ $a_n^k$ 无界 (在 $a_n\neq 0$ 处), $\sum a_n^k$ 一般发散.

**没有绝对收敛时不必成立**. 例如 $a_n=(-1)^n n^{-1/3}$: AST $\Rightarrow$ $\sum a_n$ 条件收敛; 但 $k=2$ 时 $\sum a_n^2=\sum n^{-2/3}$ 发散. (奇数 $k\ge 3$ 时同一例由 AST 仍可能收敛, 因 $a_n^k$ 保持交错且绝对值递减趋于 $0$.)

**结论**: 绝对收敛时, 一切正整数次幂级数仍绝对收敛; 负整数次一般不行; 仅条件收敛时偶数次幂可发散.

---

## 8.

课程 Root/Ratio (Thm 3.16/3.17) 要求 **极限存在**: $r=\lim\sqrt[n]{|a_n|}$ 或 $r=\lim|a_{n+1}|/|a_n|$. 「Ratio 无信息」指该极限 **不存在** (因而 Ratio 不能用), 而 Root 的极限存在且 $\neq 1$.

(若采用 limsup 版 Root, 也可改用块 $2^n$/$3^n$; 下面构造使普通极限存在, 直接套课件定理.)

### (a)

**目标**: Root 判出发散, Ratio 极限不存在.

取
$$
a_n=\begin{cases}
2^n,& n\text{ 偶},\\
3\cdot 2^n,& n\text{ 奇}.
\end{cases}
$$
则 $a_n>0$, 且
$$
\sqrt[n]{a_n}=\begin{cases}
2,& n\text{ 偶},\\
2\cdot 3^{1/n},& n\text{ 奇}.
\end{cases}
$$
因 $3^{1/n}\to 1$, 故 $\sqrt[n]{a_n}\to 2>1$. Root Test $\Rightarrow$ $\sum a_n$ 发散.

比值:
$$
\frac{a_{n+1}}{a_n}=\begin{cases}
6,& n\text{ 偶}\quad (a_{n+1}=3\cdot 2^{n+1},\ a_n=2^n),\\
2/3,& n\text{ 奇}\quad (a_{n+1}=2^{n+1},\ a_n=3\cdot 2^n).
\end{cases}
$$
两子列极限不同, $\lim a_{n+1}/a_n$ 不存在, Ratio Test 无信息.

**结论**: 上列发散, Root 给出 $r=2>1$, Ratio 极限不存在.

### (b)

**目标**: Root 判出收敛, Ratio 极限不存在. (与 Tut3 Q6 同型.)

取
$$
a_n=\begin{cases}
3\cdot 2^{-n},& n\text{ 奇},\\
2^{-n},& n\text{ 偶}.
\end{cases}
$$
则
$$
\sqrt[n]{a_n}=\begin{cases}
2^{-1}\cdot 3^{1/n},& n\text{ 奇},\\
2^{-1},& n\text{ 偶},
\end{cases}
$$
故 $\sqrt[n]{a_n}\to 1/2<1$. Root Test $\Rightarrow$ 绝对收敛.

比值:
$$
\frac{a_{n+1}}{a_n}=\begin{cases}
1/6,& n\text{ 奇},\\
3/2,& n\text{ 偶}.
\end{cases}
$$
极限不存在, Ratio 无信息.

**结论**: 上列收敛, Root 给出 $r=1/2<1$, Ratio 极限不存在.
