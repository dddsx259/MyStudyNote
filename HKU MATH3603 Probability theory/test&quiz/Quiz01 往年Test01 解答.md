# 往年 Test 1 解答

- **来源**: `docs/archives/previous/test&quiz/Test01.pdf` (50 min, 无官方解答)
- **范围**: 三题都在本学期 Quiz1 (Ch1 + §2.1–2.5) 内
- 题型对照仍见 `test&quiz/Quiz01 备考 往年Test01.md`

---

## 1. 补事件的独立

**题**: $A,B,C$ 相互独立. 证明:

(a) $A^c$ 与 $B$ 独立

(b) $A^c$ 与 $B^c$ 独立

(c) $A^c,B^c,C$ 相互独立

(d) $A^c,B^c,C^c$ 相互独立

相互独立是指: 每个至少含两个事件的子族, 交集概率等于各自概率的乘积. 三个事件要用到

$$
P(A\cap B)=P(A)P(B),\quad
P(A\cap C)=P(A)P(C),\quad
P(B\cap C)=P(B)P(C),
$$

$$
P(A\cap B\cap C)=P(A)P(B)P(C).
$$

### (a)

$$
P(A^c\cap B)=P(B)-P(A\cap B)=P(B)-P(A)P(B)=P(B)\bigl(1-P(A)\bigr)=P(A^c)P(B).
$$

### (b)

$$
\begin{aligned}
P(A^c\cap B^c)
&=1-P(A\cup B)\\
&=1-\bigl(P(A)+P(B)-P(A\cap B)\bigr)\\
&=1-P(A)-P(B)+P(A)P(B)\\
&=\bigl(1-P(A)\bigr)\bigl(1-P(B)\bigr)=P(A^c)P(B^c).
\end{aligned}
$$

### (c)

要查三个二元子族和唯一的三元子族.

- $A^c$ 与 $B^c$: (b).
- $A^c$ 与 $C$: 把 (a) 里的 $B$ 换成 $C$, 用 $P(A\cap C)=P(A)P(C)$.
- $B^c$ 与 $C$: 同样, $P(B^c\cap C)=P(B^c)P(C)$.

三元:

$$
\begin{aligned}
P(A^c\cap B^c\cap C)
&=P(C)-P\bigl((A\cup B)\cap C\bigr)\\
&=P(C)-P\bigl((A\cap C)\cup(B\cap C)\bigr)\\
&=P(C)-\bigl(P(A\cap C)+P(B\cap C)-P(A\cap B\cap C)\bigr)\\
&=P(C)-P(A)P(C)-P(B)P(C)+P(A)P(B)P(C)\\
&=P(C)\bigl(1-P(A)\bigr)\bigl(1-P(B)\bigr)\\
&=P(A^c)P(B^c)P(C).
\end{aligned}
$$

### (d)

二元子族就是 (b) 对每一对使用: $\{A,B\}$, $\{A,C\}$, $\{B,C\}$ 都相互独立, 所以

$$
P(A^c\cap B^c)=P(A^c)P(B^c),\quad
P(A^c\cap C^c)=P(A^c)P(C^c),\quad
P(B^c\cap C^c)=P(B^c)P(C^c).
$$

三元用容斥. $(1-a)(1-b)(1-c)=1-a-b-c+ab+ac+bc-abc$, 令 $a=P(A)$ 等,

$$
\begin{aligned}
P(A^c\cap B^c\cap C^c)
&=1-P(A\cup B\cup C)\\
&=1-\bigl(P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C)\bigr)\\
&=1-P(A)-P(B)-P(C)+P(A)P(B)+P(A)P(C)+P(B)P(C)-P(A)P(B)P(C)\\
&=P(A^c)P(B^c)P(C^c).
\end{aligned}
$$

---

## 2. 均匀断棍

**题**: 棍长 $1$, 断点 $U\sim\mathrm{Unif}[0,1]$. 两段长 $U$ 与 $1-U$.

$$
X=|U-(1-U)|=|2U-1|,\qquad Y=U(1-U).
$$

(i) $X$ 的分布. (ii) $P(Y<1/8)$. (iii) $\mathrm{Var}(X)$ 与 $\mathrm{Var}(Y)$.

### (i)

$X$ 的值在 $[0,1]$. 对 $x<0$, $F_X(x)=0$. 对 $x>1$, $F_X(x)=1$. 对 $x\in[0,1]$,

$$
\begin{aligned}
F_X(x)
&=P(|2U-1|\le x)
=P\Bigl(\frac{1-x}{2}\le U\le\frac{1+x}{2}\Bigr)
=\frac{1+x}{2}-\frac{1-x}{2}
=x.
\end{aligned}
$$

这是 $\mathrm{Unif}[0,1]$ 的 CDF, 所以 $X\sim\mathrm{Unif}[0,1]$. 密度在 $(0,1)$ 上为 $1$.

### (ii)

$Y<1/8$ 即 $U(1-U)<1/8$, 也就是 $8U^2-8U+1>0$. 根为

$$
\frac{8\pm\sqrt{64-32}}{16}=\frac{2\pm\sqrt{2}}{4}.
$$

二次项系数为正, 不等式在两根之外成立. $U$ 在 $[0,1]$ 上均匀, 所以

$$
P(Y<1/8)
=\frac{2-\sqrt{2}}{4}+\Bigl(1-\frac{2+\sqrt{2}}{4}\Bigr)
=1-\frac{\sqrt{2}}{2}.
$$

### (iii)

$X\sim\mathrm{Unif}[0,1]$: $EX=1/2$, $E[X^2]=\int_0^1 x^2\,dx=1/3$,

$$
\mathrm{Var}(X)=\frac13-\Bigl(\frac12\Bigr)^2=\frac{1}{12}.
$$

$Y$ 不必先求密度. $U\sim\mathrm{Unif}[0,1]$ 时 $E[U^k]=1/(k+1)$,

$$
EY=E[U]-E[U^2]=\frac12-\frac13=\frac16,
$$

$$
E[Y^2]=E\bigl[U^2(1-2U+U^2)\bigr]=E[U^2]-2E[U^3]+E[U^4]
=\frac13-\frac12+\frac15=\frac{1}{30},
$$

$$
\mathrm{Var}(Y)=\frac{1}{30}-\Bigl(\frac16\Bigr)^2=\frac{1}{180}.
$$

---

## 3. $n$ 人掷公平骰

每人独立, 点数在 $\{1,\ldots,6\}$ 上均匀.

### (i) 相同点数: 每一对相同结果得 $1$ 分

对 $1\le i<j\le n$ 设 $I_{ij}=\mathbf{1}_{\{X_i=X_j\}}$, 总分 $S=\sum_{i<j}I_{ij}$.

$$
P(I_{ij}=1)=6\cdot\frac16\cdot\frac16=\frac16,\qquad ES=\binom{n}{2}\cdot\frac16=\frac{n(n-1)}{12}.
$$

方差用二阶矩, 不用 §2.6 的协方差公式. $I_{ij}^2=I_{ij}$, 故 $E[I_{ij}^2]=1/6$. 对两个不同的对 $\{i,j\}\neq\{k,\ell\}$,

$$
E[I_{ij}I_{kl}]=P(X_i=X_j,\,X_k=X_\ell).
$$

- 两对不交 (四个人): 概率 $(1/6)\cdot(1/6)=1/36$.
- 两对共用一个人 (三个人, 例如 $I_{12}I_{13}$): 三人点数相同, $6\cdot(1/6)^3=1/36$.

两种情形都是 $1/36=(1/6)^2$. 记 $m=\binom{n}{2}$, 则

$$
E[S^2]=\sum_{i<j}E[I_{ij}^2]+\sum_{\{i,j\}\neq\{k,\ell\}}E[I_{ij}I_{kl}]
=\frac{m}{6}+\frac{m(m-1)}{36}.
$$

$$
\begin{aligned}
\mathrm{Var}(S)
&=E[S^2]-(ES)^2
=\frac{m}{6}+\frac{m(m-1)}{36}-\frac{m^2}{36}
=\frac{m}{6}-\frac{m}{36}
=\frac{5m}{36}
=\frac{5n(n-1)}{72}.
\end{aligned}
$$

### (ii) 按面值: 面 $k$ 出现 $m_k$ 次则贡献 $m_k\cdot k$

每个显示 $k$ 的人贡献 $k$ 一次, 所以总分就是各人点数之和:

$$
T=\sum_{k=1}^6 m_k\cdot k=\sum_{i=1}^n X_i.
$$

$X_i$ 独立同分布,

$$
EX_i=\frac{1+2+3+4+5+6}{6}=\frac72,
$$

$$
E[X_i^2]=\frac{1+4+9+16+25+36}{6}=\frac{91}{6},
$$

$$
\mathrm{Var}(X_i)=\frac{91}{6}-\Bigl(\frac72\Bigr)^2=\frac{91}{6}-\frac{49}{4}=\frac{35}{12}.
$$

独立, 方差相加:

$$
ET=\frac{7n}{2},\qquad \mathrm{Var}(T)=\frac{35n}{12}.
$$
