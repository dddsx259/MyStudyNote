### 1. Learning Problem:
+ Input: Given
  + **examples $S$** drawn i.i.d. according to some **unknown distribution $D$**, with labels based on a **specific target $c\in C$**.
  + A fixed set of possible concepts: **hypothesis set $H$**
+ Task:
  + Find a **hypothesis $h_S\in H$** with small **generalization error**

### 2. Generalization error:
$$
R(h) = P[h(x)\neq c(x)] = E[1_{h(x)\neq c(x)}]
$$

### 3. Empirical error:
$$
\hat{R}_S(h) = \frac{1}{m}\sum_{i=1}^m 1_{h(x_i)\neq c(x_i)} = 1-Accuracy_{train}
$$

### 4. PAC learning
+ A **concept class $C$** is **PAC-learnable** if there exists:
  + An **algorithm $A$**
  + A **polynomial function $poly(\cdot, \cdot, \cdot, \cdot)$**
  + **Accuracy parameter $\epsilon$**
  + **Confidence parameter $\delta$**
+ So that:
  + For all $D$ on $X$, for any **target $c\in C$**, for any **sample size $m\geq poly(\epsilon^{-1}, \delta^{-1}, n, size(c))$**, we have:
  + $$P[R(h_S)\leq\epsilon]\geq 1-\delta$$
    + $n$: The computational cost of representing any element $x\in X$ is at most $O(n)$
    + $size(c)$: The maximal cost of the computational representation of $c\in C$
+ $C$ is **efficiently PAC-learnable** if $A$ runs in $poly(\epsilon^{-1}, \delta^{-1}, n, size(c))$

### 5. Learning bound of finite hypothesis set and consistent case.
+ Consider the **hypothesis set $H$** is **finite**, and the **learning algorithm $A$** is **consistent**.
  + The learning algorithm $A$ is consistent if it can find a hypothesis $h_S\in H$ that has zero empirical error.
+ The learning bound is:
  + $\forall \epsilon, \delta > 0$, with probability at least $1-\delta$, we have $R(h_S)\le \epsilon$ if $m\geq \frac{1}{\epsilon}(\log |H| + \log\frac{1}{\delta})$
  + Equivalently, $R(h_S)\le \frac{1}{m}(\log |H| + \log\frac{1}{\delta})$ with probability at least $1-\delta$
+ **Proof**:
  + For any $\epsilon\ge 0$, we define: $H_{\epsilon}=\{h\in H: R(h)>\epsilon\}$
  + We have $P[h\in H_{\epsilon}: \hat{R}_S(h)=0]\le (1-\epsilon)^m$
  + So we have:
  + $$
    \begin{aligned}
        P[\exists h\in H_{\epsilon}: \hat{R}_S(h)=0] &\le\sum_{h\in H_{\epsilon}}P[\hat{R}_S(h)=0] \\
        &\le\sum_{h\in H_{\epsilon}} (1-\epsilon)^m \\
        &\le |H|(1-\epsilon)^m \\
        &\le |H|e^{-m\epsilon}
    \end{aligned}
    $$
  + Set $RHS = \delta$, then we have: $R(h_S)\le \epsilon = \frac{1}{m}(\log |H| + \log\frac{1}{\delta})$

### 6. Generalization bound of single hypothesis
+ Fixed **hypothesis $h:X\rightarrow \{0, 1\}$**, we have:
  + $$P[\hat{R}_S-R(h)\ge \epsilon]\le e^{-2m\epsilon^2}$$
  + $$P[\hat{R}_S-R(h)\le -\epsilon]\le e^{-2m\epsilon^2}$$
+ Which means:
  + $$P[\mid\hat{R}_S-R(h)\mid\ge \epsilon]\le 2e^{-2m\epsilon^2}$$
+ Proof:
  + $$\begin{aligned}P[\hat{R}_S-R(h)\ge \epsilon]&=P[m\hat{R}_S-mR(h)\ge m\epsilon]\\&=P[m\hat{R}_S-mE[\hat{R}_S]\ge m\epsilon]\\&\le\exp(-\frac{2m^2\epsilon^2}{m\cdot (1-0)^2})\\&=e^{-2m\epsilon^2}\end{aligned}$$
+ Set $\delta=RHS=2e^{-2m\epsilon^2}$, we have such corollary:
  + For any $\delta>0$, the following inequality holds with probability at least $1-\delta$:
    + $$R(h)\le \hat{R}_S(h)+\epsilon=\hat{R}_S(h)+\sqrt{\frac{\log\frac{2}{\delta}}{2m}}$$

### 7. Generalization bound of multiple hypotheses
+ Consider a **finite hypothesis set $H$**, for any $\delta>0$, with probability at least $1-\delta$, we have:
  + $$\forall h\in H, R(h)\le \hat{R}_S(h)+\sqrt{\frac{\log\frac{2}{\delta} + \log |H|}{2m}}$$
+ Proof:
  + $$\begin{aligned}P[\exists h\in H: R(h)-\hat{R}_S(h)\ge \epsilon]&=P[\lor_{h\in H} R(h)-\hat{R}_S(h)\ge \epsilon]\\&\le\sum_{h\in H}P[R(h)-\hat{R}_S(h)\ge \epsilon]\\&\le 2|H|e^{-2m\epsilon^2}\end{aligned}$$
