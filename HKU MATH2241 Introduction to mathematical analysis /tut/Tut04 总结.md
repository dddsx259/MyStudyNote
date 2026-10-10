# Tut04 — 总结

- **源**: `tut/Tut04.pdf` (题面; 官方 sol 尚未入库)
- **解答**: [`Tut04 解答.md`](Tut04%20解答.md)
- **范围**: Ch2 Part3 级数 (比较 / 极限比较 / 交错 / Cauchy 凝聚 / $p$-级数)
- **与 Test1**: 落在 Ch2 级数范围内, 可作 Test1 前练题

---

## 1. 证明或反驳

判断 $\sum_{n=1}^\infty \dfrac{1}{n^{1+1/n}}$ 是否发散.

- **提示**: $2^n>n$ ($\forall n\in\mathbb{N}$), 用来得到 $n^{1/n}<2$
- **思路**: 注意指数 $1+1/n\to 1$, 与调和级数比较; 或估计 $n^{1/n}\to 1$ 得通项 $\sim 1/n$.

## 2. Limit Comparison Test

设 $\{a_n\},\{b_n\}$ 为正项, $\lim\dfrac{a_n}{b_n}=L\ge 0$.

- **(a)** 若 $L>0$, 则 $\sum a_n$ 敛 $\Leftrightarrow$ $\sum b_n$ 敛
- **(b)** 若 $L=0$ 且 $\sum b_n$ 敛, 则 $\sum a_n$ 敛
- **(c)** 举正项例: $\lim a_n/b_n=0$, $\sum a_n$ 敛但 $\sum b_n$ 散
- **(d)** 判断 $\sum\dfrac{n^2+n-1}{27n^5-n^4+9n^3-2n+6}$ 敛散

## 3. 求和

证明 $\dfrac{1^2}{0!}+\dfrac{2^2}{1!}+\dfrac{3^2}{2!}+\dfrac{4^2}{3!}+\cdots$ 收敛并求其和.

- **提示**: $\sum_{n=0}^\infty 1/n!=e$; 可用 $n^2=(n)(n-1)+n$ 改写阶乘分母.

## 4. 与 $\sin$/$\cos$ 的组合

- **(a)** 若 $\sum a_n$ 收敛, 则 $\sum\cos a_n$ 发散
- **(b)** 若 $\sum a_n$ 绝对收敛, 则 $\sum\sin a_n$ 绝对收敛

## 5. 绝对 / 条件 / 发散

判断:

- **(a)** $\sum(-1)^{n+1}/(n+\sqrt n)$
- **(b)** $\sum(-1)^{n+1}n/(n+\sqrt n)$

## 6. Cauchy Condensation

- **(a)** $\{a_n\}$ 递减且 $a_n\ge 0$: $\sum a_n$ 敛 $\Leftrightarrow$ $\sum 2^n a_{2^n}$ 敛
- **(b)** 用凝聚判别证 $p$-级数 $\sum 1/n^p$ 敛 $\Leftrightarrow$ $p>1$
