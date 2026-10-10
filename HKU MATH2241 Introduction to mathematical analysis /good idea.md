### 1.  TUT03 Q3
+ Question: $x_n$ bounded, 所有的收敛子序列均收敛至 $L$, 求证 $x_n$ 收敛至 $L$.
+ good idea:
  + 反证法时, 考虑把 $\forall \varepsilon>0, \exists N, \forall n>N,\ |x_n - L| < \varepsilon$ 转换为 $\exists \varepsilon > 0, \forall N, \exists n>N,\ |x_n - L| \geq \varepsilon$

### 2.  TUT02 P1(a)
+ Question: 求 $\lim_{n\to\infty}\sum_{k=1}^n \frac{1}{k(k+1)}$.
+ good idea:
  + $\frac{1}{k(k+1)}=\frac{1}{k}-\frac{1}{k+1}$, 望远镜和 $=1-\frac{1}{n+1}\to 1$

### 3.  TUT02 P1(c)
+ Question: 求 $\lim_{n\to\infty}\sum_{k=0}^n \frac{1}{(n+k)^2}$.
+ good idea:
  + $k\ge 0$ 故每项 $\le 1/n^2$, 共 $n+1$ 项, $0\le\sum\le\frac{n+1}{n^2}\to 0$; 下界用 $0$ 即可, 不必再写 $1/(2n)^2$

### 4.  TUT02 P1(d)
+ Question: 求 $\lim_{n\to\infty}\sum_{k=1}^n \frac{1}{\sqrt{n^2+k}}$.
+ good idea:
  + $\frac{n}{\sqrt{n^2+n}}\le\sum_{k=1}^n\frac{1}{\sqrt{n^2+k}}\le\frac{n}{\sqrt{n^2+1}}$, 即 $\frac{1}{\sqrt{1+1/n}}\le\sum\le\frac{1}{\sqrt{1+1/n^2}}\to 1$; 提出 $n$ 时是 $k/n^2$ 不是 $k/n$

### 5.  TUT02 P2
+ Question: $a_1,\ldots,a_m>0$, $A=\max\{a_i\}$, 求证 $\sqrt[n]{a_1^n+\cdots+a_m^n}\to A$.
+ good idea:
  + $A=\sqrt[n]{A^n}\le\sqrt[n]{\sum a_i^n}\le\sqrt[n]{m A^n}=A\sqrt[n]{m}$, 再用 $\sqrt[n]{m}\to 1$

### 6.  Test review P6(d)
+ Question: 求证 $\log_{n+1}n\to 1$ ($n\to\infty$).
+ good idea:
  + 换底写成 $\frac{\ln n}{\ln(n+1)}$, 再用 $\ln(n+1)=\ln n+\ln(1+1/n)$

### 7.  Ch1 Thm 4.9
+ Question: $x=\sup\{y\ge 0: y^2<2\}$, 求证 $x^2=2$ (从而 $\sqrt{2}$ 存在).
+ good idea:
  + $x^2<2$ 时取 $h=\min\bigl\{1,(2-x^2)/(2x+1)\bigr\}$, 使 $(x+h)^2<2$, 则 $x+h\in S$
  + $x^2>2$ 时取 $h=\min\bigl\{x,(x^2-2)/(2x)\bigr\}$, 使 $x-h$ 仍为上界且 $<x$

### 8.  Ch2 P1 Thm 5.2
+ Question: 求证 $\lim_{n\to\infty} n^{1/n}=1$.
+ good idea:
  + 二项式只留下二次项: $n=(1+x_n)^n\ge \frac{n(n-1)}{2}x_n^2$, 得 $0\le x_n^2\le\frac{2}{n-1}$ (或 $\frac{2}{n}$), 夹逼

### 9.  TUT04 P3
+ Question: 证明 $\dfrac{1^2}{0!}+\dfrac{2^2}{1!}+\dfrac{3^2}{2!}+\cdots$ 收敛并求其和.
+ good idea:
  + 通项 $\dfrac{(n+1)^2}{n!}$. 分子拆成与 $n(n-1)$ 和 $n$ 相关的项: $(n+1)^2=n(n-1)+3n+1$, 约去 $n!$ 得 $\dfrac{1}{(n-2)!}+\dfrac{3}{(n-1)!}+\dfrac{1}{n!}$
  + 用 $\sum_{n=0}^{\infty}\dfrac{1}{n!}=e$ 求部分和的极限

### 10.  TEST1 P5
+ Question: 求证复数域 $\mathbb{C}$ 上不存在满足有序域公理的序 ($<$).
+ good idea:
  + 先由有序域公理推出: $\forall x\ne 0,\ x^2>0$ (因 $x>0$ 则 $x^2>0$; $x<0$ 则 $-x>0$ 故 $x^2=(-x)^2>0$); 特别地 $1=1^2>0$, 于是 $-1<0$
  + 再取反例 $i\in\mathbb{C}$: $i^2=-1$, 若 $\mathbb{C}$ 有序则 $i^2=-1>0$ (由 $i\ne 0$ 及平方大于 $0$), 与刚证的 $-1<0$ 矛盾
