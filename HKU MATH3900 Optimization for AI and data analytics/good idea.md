### 1.  TUT03 P1(d)
+ Question: $f$ 可微凸, $p$ 为下降方向, $\alpha$ 满足 Armijo 条件 $f(x+\alpha p)\le f(x)+c_A\alpha\nabla f(x)^T p$. 求证 $\alpha/2$ 也满足 Armijo.
+ good idea:
  + 用中点凸性 (可微凸 $\Rightarrow$ 凸): $f(x+\frac\alpha2 p)\le \frac12 f(x)+\frac12 f(x+\alpha p)$
  + 再把 Armijo 条件代入右端的 $f(x+\alpha p)$: $\le \frac12 f(x)+\frac12[f(x)+c_A\alpha\nabla f(x)^T p]=f(x)+\frac{c_A\alpha}{2}\nabla f(x)^T p$, 即 $\alpha/2$ 的 Armijo 形式
  + 关键: 论证全程只用 $p$ 为下降方向 + 凸性, 不需要 $p=-\nabla f$, 所以 Armijo 是关于"沿下降方向走多远"的步长准则, 不绑定梯度下降
