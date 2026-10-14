# Tut06 总结

- **来源**: `tut/Tut06.pdf` (Tutorial 6; 本学期; **尚无官方 sol**)
- **课程**: MATH3603 Probability Theory
- **对齐**: 期望 / 方差 / 协方差; Poisson 与 Gamma 可加性 (Ch2 矩 + 分布族)

---

## 1. Hat check (配对问题)

$N$ 人扔帽子后随机领取. $M=$ 拿到自己帽子的人数. 求 $E[M]$, $\mathrm{Var}(M)$.

**思路**: 示性 $I_i=\mathbf{1}_{\{\text{人 }i\text{ 拿回自己的帽子}\}}$, $M=\sum I_i$.

- $E[I_i]=P(I_i=1)=1/N$, 故 $E[M]=1$ (对 $N\ge1$).
- $\mathrm{Var}(M)=\sum\mathrm{Var}(I_i)+2\sum_{i<j}\mathrm{Cov}(I_i,I_j)$.
- $\mathrm{Var}(I_i)=E[I_i^2]-(E I_i)^2=\frac1N-\frac1{N^2}$.
- $i\neq j$: $E[I_i I_j]=P(\text{双固定点})=\frac{1}{N(N-1)}$ (对 $N\ge2$), 故
  $\mathrm{Cov}(I_i,I_j)=\frac{1}{N(N-1)}-\frac1{N^2}=\frac{1}{N^2(N-1)}$.
- 整理得 $\mathrm{Var}(M)=1$ (经典结论; 交稿前再核代数).

---

## 2. Sample mean

$X_1,\ldots,X_n$ i.i.d., 均值 $\mu$, 方差 $\sigma^2$. $\bar X=\frac1n\sum X_i$.

### (a) $E[\bar X]$

线性性 (不必独立): $E[\bar X]=\mu$.

### (b) $\mathrm{Var}(\bar X)$

独立同分布: $\mathrm{Var}(\bar X)=\sigma^2/n$.

### (c) $\mathrm{Cov}(\bar X, X_i-\bar X)$

展开: $\mathrm{Cov}(\bar X, X_i)-\mathrm{Var}(\bar X)$.

- $\mathrm{Cov}(\bar X, X_i)=\mathrm{Cov}(\frac1n\sum_j X_j, X_i)=\frac1n\mathrm{Var}(X_i)=\sigma^2/n$.
- 故 $\mathrm{Cov}(\bar X, X_i-\bar X)=\sigma^2/n-\sigma^2/n=0$.

(残差与样本均值不相关; 正态时还可得独立.)

---

## 3. 可加性

### (a) 独立 Poisson 之和

$X_k\sim\mathrm{Poisson}(\lambda_k)$ 独立. 证 $Y=\sum X_k\sim\mathrm{Poisson}(\sum\lambda_k)$.

**思路**: 用 PGF $G_{X_k}(s)=e^{\lambda_k(s-1)}$, 独立则乘积 $G_Y(s)=e^{(\sum\lambda_k)(s-1)}$; 或对 $n=2$ 卷积再归纳.

### (b) i.i.d. Exponential 之和

$X_k\sim\mathrm{Exp}(\lambda)$ i.i.d. 证 $Y=\sum_{k=1}^n X_k\sim\mathrm{Gamma}(n,\lambda)$ (形状 $n$, 率 $\lambda$; 即 Erlang).

**思路**: 密度卷积归纳; 或 MGF $( \lambda/(\lambda-t) )^n$.

---

## 做题顺序

Q2 最快练公式 → Q1 示性+协方差 → Q3 写清工具 (PGF/MGF/卷积).

**scope (todo)**: `[scope: Ch2 期望/方差/协方差 / 分布可加性]`
