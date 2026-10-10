# Review03 — Test 1 (Fall 2025) 解答

- **题面**: `docs/archives/previous/test&quiz/Test01 2025.pdf` 第 11–12 页 (第 12 页是有序域公理 (O1)–(O5))
- **官方解答**: 无
- **范围**: 六题都在本次 Test 1 (Ch1 + Ch2)
- **说明**: 自写完整解答. 先做再对照.

---

## (1) Cauchy 序列的定义

**定义**: 序列 $(x_n)$ 是 Cauchy 序列, 若

$$
\forall\varepsilon>0,\ \exists N\in\mathbb{N},\ \text{使 } n,m>N\Rightarrow |x_n-x_m|<\varepsilon.
$$

(Ch2 P2 Def 3.1.)

---

## (2) $\sup A=10/3$, $\inf A=8/3$

**结论**: $\sup A=\dfrac{10}{3}$, $\inf A=\dfrac{8}{3}$. 两者都不在 $A$ 中.

记

$$
A=\left\{3\pm\frac{n}{3n+1}:n\in\mathbb{N}\right\}.
$$

先看分数项. 对 $n\ge 1$,

$$
\frac13-\frac{n}{3n+1}=\frac{1}{3(3n+1)}>0,
$$

故

$$
0<\frac{n}{3n+1}<\frac13.
$$

于是每个元素都落在开区间里:

$$
\frac83=3-\frac13<3-\frac{n}{3n+1}<3+\frac{n}{3n+1}<3+\frac13=\frac{10}{3}.
$$

因此 $10/3$ 是 $A$ 的上界, $8/3$ 是 $A$ 的下界.

**上确界**. 设 $v<10/3$, 令 $\delta=10/3-v>0$. 由阿基米德性质, 存在 $n\in\mathbb{N}$ 使 $3n+1>1/(3\delta)$, 即

$$
\frac{1}{3(3n+1)}<\delta.
$$

对应的正号元素

$$
x_n=3+\frac{n}{3n+1}=\frac{10}{3}-\frac{1}{3(3n+1)}>\frac{10}{3}-\delta=v.
$$

$x_n\in A$ 且 $x_n>v$, 故 $v$ 不是上界. $10/3$ 是最小上界.

**下确界**. 设 $\ell>8/3$, 令 $\delta=\ell-8/3>0$. 同样取 $n$ 使 $1/(3(3n+1))<\delta$. 负号元素

$$
y_n=3-\frac{n}{3n+1}=\frac83+\frac{1}{3(3n+1)}<\frac83+\delta=\ell.
$$

$y_n\in A$ 且 $y_n<\ell$, 故 $\ell$ 不是下界. $8/3$ 是最大下界.

上面的差 $1/(3(3n+1))$ 对一切有限的 $n$ 都是正的, 所以 $10/3\notin A$, $8/3\notin A$.

---

## (3) $\lim n!/n^n=0$

**结论**: 极限存在, 且等于 $0$.

对 $n\ge 1$,

$$
0<\frac{n!}{n^n}=\frac{1}{n}\cdot\frac{2}{n}\cdots\frac{n}{n}\le\frac{1}{n},
$$

因为每个因子 $k/n$ 都在 $(0,1]$ 里, 而第一个因子就是 $1/n$. 又 $1/n\to 0$. 由夹逼,

$$
\lim_{n\to\infty}\frac{n!}{n^n}=0.
$$

---

## (4) 绝对收敛 $\Rightarrow$ 收敛

**结论**: 若 $\sum |x_n|$ 收敛, 则 $\sum x_n$ 收敛. (Ch2 P3 Thm 3.3.)

**证明**: 对每个 $n$,

$$
0\le x_n+|x_n|\le 2|x_n|.
$$

$\sum 2|x_n|$ 收敛. 通项 $x_n+|x_n|$ 非负, 由比较检验 (题目允许直接用), $\sum(x_n+|x_n|)$ 收敛. 又

$$
x_n=(x_n+|x_n|)-|x_n|,
$$

两个收敛级数的差仍收敛, 故 $\sum x_n$ 收敛.

---

## (5) $\mathbb{Q}(i)$ 不是有序域

**结论**: 给定的加法和乘法使 $\mathbb{Q}(i)$ 成为域 (题目已给, 不必验证), 但它**不能**成为有序域.

先用 (O1)–(O5) 说明有序域里非零元的平方为正. 设 $a\in F$.

- 若 $a\ge 0$, 由 (O5) (乘数 $a\ge 0$) 得 $0\cdot a\le a\cdot a$, 即 $0\le a^2$.
- 若 $a\le 0$, 由 (O4) 加 $-a$ 得 $0\le -a$. 上一种情形给出 $0\le(-a)^2=a^2$.

所以一切平方 $\ge 0$. 若 $a\neq 0$, 则 $a^2\neq 0$ (域里没有零因子). 于是 $a^2>0$. 特别地 $1=1^2>0$, 再由 (O4) 加 $-1$ 得 $-1<0$.

现在取 $i=0+1\cdot i$. 按题目给的乘法,

$$
i\cdot i=(0\cdot 0-1\cdot 1)+(0\cdot 1+1\cdot 0)i=-1.
$$

$i\neq 0$, 故若序存在则应有 $i^2>0$, 即 $-1>0$. 这与 $-1<0$ 矛盾.

因此 $\mathbb{Q}(i)$ 不是有序域.

---

## (6) 真: 有界发散序列有两条极限不同的收敛子列

**结论**: 命题为真.

**证明**: $(x_n)$ 有界. 由 Bolzano–Weierstrass 定理 (Ch2 P2 Thm 2.4), 存在收敛子列 $x_{n_k}\to L$.

$(x_n)$ 发散, 所以它不收敛到 $L$. 于是存在 $\varepsilon>0$, 使得有无穷多个下标满足 $|x_n-L|\ge\varepsilon$. 把这些下标排成严格递增的 $m_j$, 得到子列 $y_j=x_{m_j}$, 且

$$
|y_j-L|\ge\varepsilon\quad(j\in\mathbb{N}).
$$

$(y_j)$ 仍有界. 再由 Bolzano–Weierstrass, 它有收敛子列 $y_{j_i}\to M$. 对不等式取极限,

$$
|M-L|\ge\varepsilon>0,
$$

故 $M\neq L$.

$y_{j_i}=x_{m_{j_i}}$ 也是 $(x_n)$ 的子列. 于是 $(x_{n_k})$ 与 $(x_{m_{j_i}})$ 都收敛, 极限分别是 $L$ 和 $M$, 且 $L\neq M$.
