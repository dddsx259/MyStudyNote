### 1. Markov Inequality
+ If:
  + $X\ge 0$
  + $E[X]$ is finite.
+ Then for all $a>0$, we have: $P[X>a]\le \frac{E[X]}{a}$
+ Proof: 
  + Consider $E[X]=\sum x\cdot P(X=x) = \sum_{x>a} x\cdot P(X=x) + \sum_{x<=a} x\cdot P(X=x)$
  + So we have $E[X]\ge \sum_{x>a} x\cdot P(X=x) \ge \sum_{x>a} a\cdot P(X=x)$
  + i.e. $\sum_{x>a}P(X=x) \le \frac{E[X]}{a}$
  + Q.E.D.


### 2. Hoeffding Lemma
+ Assume $X\in [a,b]$ and $E[X]=0$, for all $t>0$, we have:
+ $$E[e^{tX}]\le \exp(\frac{t^2(b-a)^2}{8})$$
+ Proof:
  + Since $e^x$ is convex, we have:
  + $$e^{tx}\le \frac{(b-x)e^{ta} + (x-a)e^{tb}}{b-a}$$
  + i.e. 
  + $$\begin{aligned}E[e^{tX}]&\le E[\frac{(b-X)e^{ta} + (X-a)e^{tb}}{b-a}]\\&=E[\frac{(b-X)}{b-a}e^{ta} + \frac{(X-a)}{b-a}e^{tb}]\\&=E[\frac{be^{ta}-ae^{tb}}{b-a}]\\&=\alpha e^{ta} + (1-\alpha)e^{tb}\text{, where }\alpha = \frac{b}{b-a}\end{aligned}$$
  + We want to find the maximum of $RHS$, so let $f(t) = RHS = \alpha e^{ta} + (1-\alpha)e^{tb}$, by 2nd-order Taylor expansion, we have: $f(t)\le \exp(\frac{t^2(b-a)^2}{8})$, so $E[e^{tX}]\le \exp(\frac{t^2(b-a)^2}{8})$
  + Q.E.D

### 3. Chernoff Bounding Technique
+ For random variables $X$ and any $\epsilon > 0$, we have:
+ $$P[X>\epsilon]=P[e^{tX}>e^{t\epsilon}]\le e^{-t\epsilon}E[e^{tX}]$$
+ The upper bound is given by Hoeffding Lemma, so we just need to choose a proper $t$ to minimize the upper bound of $P[X>\epsilon]$.

### 4. Hoeffding Inequality
+ There are $m$ i.i.d. random variables $X_i$, $X_i\in [a_i, b_i]\forall i$. Let $S$ be the sum of them: $S=\sum_i X_i$, for any $\epsilon>0$ we have:
  + $$P[S-E[S]\ge \epsilon]\le \exp(-\frac{2\epsilon^2}{\sum_i(b_i-a_i)^2})$$
  + $$P[S-E[S]\le -\epsilon]\le \exp(-\frac{2\epsilon^2}{\sum_i(b_i-a_i)^2})$$
+ Proof:
  + Following CBT, we have $P[S-E[S]\ge \epsilon]=P[e^{t(S-E[S])}\ge e^{t\epsilon}]\le e^{-t\epsilon}E[e^{t(S-E[S])}]$
  + $E[e^{t(S-E[S])}] = \prod_i E[e^{t(X_i-E[X_i])}]\le \exp(\frac{t^2\sum_i(b_i-a_i)^2}{8})$
  + So $P[S-E[S]\ge \epsilon]\le \exp(-t\epsilon + \frac{t^2\sum_i(b_i-a_i)^2}{8})$
  + Choose $t=\frac{4\epsilon}{\sum_i(b_i-a_i)^2}$ then we have:
  + $P[S-E[S]\ge \epsilon]\le \exp(-\frac{2\epsilon^2}{\sum_i(b_i-a_i)^2})$

### 4. McDiarmid's Inequality
+ Let:
  + $X_1, X_2, \dots, X_n$ be an i.i.d. sequence of random variables
  + $f: \mathbb{R}^n \rightarrow \mathbb{R}$
+ If for all $i$, whenever $x_i$ is changed to $x_i'$, the change in $f(x)$ is bounded by $c_i$
  + i.e. $|f(x)-f(x')|\le c_i$ for all $x, x'$
+ Then for any $\epsilon > 0$, we have:
  + $P[|f(\mathbb{X})-\mathbb{E}[f(\mathbb{X})]|\ge \epsilon]\le 2\exp(-\frac{2\epsilon^2}{\sum_i(c_i)^2})$