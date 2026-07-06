### 1. Empirical Rademacher complexity
+ Let:
  + $G$ be **a family of functions**: $g\in G: Z \rightarrow [a,b]$
  + $Z$ be **fixed sample of size $m$**: $Z = (z_1, z_2, \dots, z_m)$
+ We define the **empirical Rademacher complexity** of $G$ as:
  $$
   \hat{\mathcal{R}}_S(G) = \mathbb{E}_{\sigma} \left[ \sup_{g\in G} \frac{1}{m} \sum_{i=1}^m \sigma_i g(z_i) \right]=\mathbb{E}_{\sigma} \left[ \sup_{g\in G} \frac{\vec{\sigma}\cdot\vec{g}_S}{m}\right]
  $$
  where $\sigma_i$ are **Rademacher variables**: $\sigma_i \in \{1, -1\}$ with probability $1/2$.
+ We can interpret the empirical Rademacher complexity as the average **maximum deviation** of the functions in $G$ from the expected value.
+ The empirical Rademacher complexity is a **lower bound** on the generalization error of $G$.

### 2. Rademacher complexity
+ Let:
  + $D$ be the **distribution of the samples**.
  + The other parameters are the same as above.
+ We define the **Rademacher complexity** of $G$ as:
  $$
  \hat{\mathcal{R}}_S(G) = \mathbb{E}_{S\sim D^m} \left[ \hat{\mathcal{R}}_S(G) \right] 
  $$

### 3. The upper bound of the expectation of a single loss function
+ Let:
  + $G$ be **a family of functions**: $g\in G: Z \rightarrow [0,1]$
+ For any $\delta > 0, g\in G$, with probability at least $1-\delta$, we have:
  $$
  \begin{aligned}
  &\mathbb{E}(g(z))\leq \frac{1}{m}\sum_{i=1}^m g(z_i) + 2\mathcal{R}_m(G) + \sqrt{\frac{2\log\frac{1}{\delta}}{m}}\\
  \text{and }&\mathbb{E}(g(z))\leq \frac{1}{m}\sum_{i=1}^m g(z_i) + 2\hat{\mathcal{R}}_S(G) + 3\sqrt{\frac{2\log\frac{2}{\delta}}{m}}
  \end{aligned}
  $$
+ Proof:
  + Let $\hat{\mathbb{E}}_S[g]=\frac{1}{m}\sum_{i=1}^m g(z_i)$
  + The we define $\Phi(S)=\sup_{g\in G}(\mathbb{E}_S[g]-\hat{\mathbb{E}}_S[g])$
  + Let $S$ and $S′$ be two samples diﬀering by exactly one point
    + The only difference is $z_m\in S$ and $z_{m}'\in S'$
  + Then we have:
    + $$\Phi(S')-\Phi(S)\le \sup_{g\in G}\left(\mathbb{E}_S[g]-\hat{\mathbb{E}}_{S'}[g]\right)=\sup_{g\in G}\frac{g(z_m)-g(z_{m}')}{m}\le \frac{1}{m}$$
  + Similarly, we have $$\Phi(S)-\Phi(S')\le \frac{1}{m}$$
    + i.e. $\mid\Phi(S')-\Phi(S)\mid\le \frac{1}{m}$
    + Which means $\Phi(S)$ is a 1-Lipschitz function.
  + By McDiarmid's Inequality, we have:
    + For any $\delta > 0$, with probability at least $1-\frac{\delta}{2}$, we have:
    + $$\Phi(S)\le \mathbb{E}[\Phi(S)] + \sqrt{\frac{2\log\frac{2}{\delta}}{m}}$$
  + Then we bound the expectation of $\Phi(S)$ as follows:
  + $$\begin{aligned}\mathbb{E}_S[\Phi(S)]&=\mathbb{E}_S\left[\sup_{g\in G}\left(\mathbb{E}[g]-\hat{\mathbb{E}}_S(g)\right)\right]\\&=\mathbb{E}_S\left[\sup_{g\in G}\mathbb{E}_{S'}\left(\hat{\mathbb{E}}_{S'}[g]-\hat{\mathbb{E}}_S(g)\right)\right]\\&\le\mathbb{E}_{S,S'}\left[\sup_{g\in G}\left(\hat{\mathbb{E}}_{S'}[g]-\hat{\mathbb{E}}_S(g)\right)\right]\\&=\mathbb{E}_{S,S'}\left[\sup_{g\in G}\frac{1}{m}\sum_{i=1}^m(g(z_i')-g(z_i))\right]\\&=\mathbb{E}_{\sigma,S,S'}\left[\sup_{g\in G}\frac{1}{m}\sum_{i=1}^m\sigma_i(g(z_i')-g(z_i))\right]\\&\le\mathbb{E}_{\sigma,S'}\left[\sup_{g\in G}\frac{1}{m}\sum_{i=1}^m\sigma_ig(z_i')\right] + \mathbb{E}_{\sigma,S}\left[\sup_{g\in G}\frac{1}{m}\sum_{i=1}^m-\sigma_ig(z_i)\right]\\&=2\mathbb{E}_{\sigma,S}\left[\sup_{g\in G}\frac{1}{m}\sum_{i=1}^m\sigma_ig(z_i)\right]=2\mathcal{R}_m(G)\end{aligned}$$
+ Using again **McDiarmid's Inequality**, we have:
  + For any $\delta > 0$, with probability at least $1-\frac{\delta}{2}$, we have:
  + $$\mathcal{R}_m(G)\le \hat{\mathcal{R}}_S(G)+\sqrt{\frac{2\log\frac{2}{\delta}}{m}}$$
+ Finally we have:
  + $$\Phi(S)\le 2\hat{\mathcal{R}}_S(G)+3\sqrt{\frac{\log\frac{2}{\delta}}{m}}$$
  + $$\mathbb{E}[g(z)]\le \hat{\mathbb{E}}[g(z)]+ 2\hat{\mathcal{R}}_S(G) + 3\sqrt{\frac{\log\frac{2}{\delta}}{m}}=\frac{1}{m}\sum_{i=1}^m g(z_i) + 2\hat{\mathcal{R}}_S(G) + 3\sqrt{\frac{\log\frac{2}{\delta}}{m}}$$
  + Q.E.D.

### 4. The bridge between empirical Rademacher complexity and hypothesis space
+ Let:
  + $H$ be **a family of functions**: $h\in H: X \rightarrow \{-1,+1\}$
  + $G$ be **zero-one loss**: $G=\{(x,y)\mapsto 1_{h(x)\neq y}:h\in H\}$
  + $S$ be **sample space**: $S=\{(x_1,y_1), (x_2,y_2), \dots, (x_m,y_m)\}\subset X\times \{-1, +1\}$
  + $S_X$ be $S$'s **projection over X**: $S_X=\{x_1, x_2, \dots, x_m\}$
+ Then we have:
  + $$\hat{\mathcal{R}}_S(G) = \frac{1}{2}\hat{\mathcal{R}}_{S_X}(H)$$
+ Proof: Using the fact $1_{h(x_i)\neq y_i}=\frac{1-y_ih(x_i)}{2}$ (for $h(x_i), y_i\in\{-1,+1\}$):
  + $$\begin{aligned}\hat{\mathcal{R}}_S(G)&=\mathbb{E}_\sigma\left[\sup_{h\in H}\frac{1}{m}\sum_{i=1}^m\sigma_i\cdot 1_{h(x_i)\neq y_i}\right]\\&=\mathbb{E}_\sigma\left[\sup_{h\in H}\frac{1}{2m}\sum_{i=1}^m\sigma_i(1-y_ih(x_i))\right]\\&=\mathbb{E}_\sigma\left[\frac{1}{2m}\sum_{i=1}^m\sigma_i\right]+\mathbb{E}_\sigma\left[\sup_{h\in H}\left(-\frac{1}{2m}\sum_{i=1}^m\sigma_i y_i h(x_i)\right)\right]\end{aligned}$$
  + The first term equals $0$ since $\mathbb{E}[\sigma_i]=0$.
  + For the second term, let $\sigma_i'=-\sigma_i y_i$. Since $y_i$ is fixed and $\sigma_i\in\{-1,+1\}$, $\sigma_i'$ are also Rademacher variables.
  + $$\mathbb{E}_\sigma\left[\sup_{h\in H}\left(-\frac{1}{2m}\sum_{i=1}^m\sigma_i y_i h(x_i)\right)\right]=\mathbb{E}_{\sigma'}\left[\sup_{h\in H}\frac{1}{2m}\sum_{i=1}^m\sigma_i' h(x_i)\right]=\frac{1}{2}\hat{\mathcal{R}}_{S_X}(H)$$
  + Q.E.D.

### 5. Rademacher complexity bounds – binary classification
+ Let:
  + $H$ be **a family of functions**: $h\in H: X \rightarrow \{-1,+1\}$
  + $D$ be **a distribution over $X$**
+ Then for any $\delta > 0$, with probability at least $1-\delta$, we have:
  + $$R(h)\leq \hat{\mathcal{R}}_S(H) + \mathcal{R}_m(H) + \sqrt{\frac{\log\frac{1}{2\delta}}{m}}$$
  + $$R(h)\leq \hat{\mathcal{R}}_S(H) + \mathcal{R}_S(H) + 3\sqrt{\frac{\log\frac{1}{2\delta}}{m}}$$

### 6. Growth function

### 7. Massart’s lemma

### 8. An upper bound of the Rademacher complexity by the growth function

### 9. An upper bound of the Generalization error by the growth function

### 10. VC dimension

### 11. Radon Theorem

### 12. Sauer Lemma

### 13. An upper bound of the growth function

### 14. VC-dimension generalization bounds

### 15. Lower bound of the generalization error, realizable case

### 16. Lemma 3.21

### 17. Lemma 3.22

### 18. Lower bound of the generalization error, non-realizable case