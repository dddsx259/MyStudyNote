# Chapter 4 Subspaces and Their Properties

Created: 2025年3月20日 09:44
Class: MATH2101

# Subspaces of $\mathbb{R}^n$

## Subspace:

A subset $W\subseteq \mathbb{R}^n$ is said to be a ***subspace*** of $\mathbb{R}^n$ if it satisfies the following:

- $\vec{0}\in W$
- If $\vec{x},\vec{y}\in W$, then $\vec{x}+\vec{y}\in W$(i.e. W is closed under addition)
- If $\vec{x}\in W$and $c\in \mathbb{R}$, then $c\vec{x}\in W$(i.e. W is closed under scalar multiplication)

For each $m\times n$ matrix $A$, we have:

### Row space

Notion: $Row\ A$

Subspace of $\mathbb{R}^n$

**Span** of the rows of $A$

### Column space

Notion: $Col\ A$

Subspace of $\mathbb{R}^m$

**Span** of the columns of $A$

### Null space

Notion: $Null\ A$

Subspace of $\mathbb{R}^n$

**Solution set** of $A\vec{x}=0$

---

## Basis:

Let $V$ be a subspace of $\mathbb{R}^n$. A linearly independent generating set for $V$ is called a basis for $V$.

Remarks:

- The plural for basis is ***bases***. (单词basis的复数形式是bases)
- A basis for V must be a subset of V.

### Every basis for $\mathbb{R}^n$ consists of exactly $n$ vectors.

### How to find a basis for each of the row space, column space and the null space of a matrix $A$:

If $R$ is the RREF of $A$

1. The set of non-zero rows of $R$ will form a basis for $Row\ A$.
    
    i.e. $dim(Row\ A)$ is equal to the numbers of non-zero rows of $R$ 
    
2. The set of leading columns will form a basis for $Col\ A$.
3. The set of **special solution vectors corresponding to the free variables in R** will form a basis for $Null\ A$.

---

## **Reduction Theorem (约简定理) and Extension Theorem (扩展定理):**

 Let $V$ be a non-zero subspace of $\mathbb{R}^n$. We have the following:

- (Reduction theorem) Every finite generating set of $V$ contains a basis.
- (Extension theorem) Every linearly independent subset of $V$ can be extended to a basis.

(By convention we say that only basis of the zero subspace is the empty set.)

## Dimension

Any two bases for $V$ contain the same number of vectors. This number is said to be the dimension of $V$ and is denoted by $dim(V)$.

(By convention the zero subspace is defined to have dimension 0.)

### If $V$ and $W$ are subspaces of $\mathbb{R}^n$ such that $V\subseteq W$, then $dim(V)\le dim(W)$. Equality holds if and only if $V=W$.

## Coordinate vector:

### lemma:

Let $B =\{b_1,b_2...b_k\}$ be an ***ordered basis*** for a subspace V.
Then each $v\in V$ can be written as a unique linear combination of the vectors in $B$.

In the forms as:

$$
 v =c_1b_1 +c_2b_2 +...+c_kb_k
$$

### Hence we define :

$$
[v]_B=\begin{bmatrix}c_1\\c_2\\c_3\\…\\c_k\end{bmatrix}=B^{-1}v
$$

### to be the ***coordinate vector of v relative to B*** (or ***B-coordinate vector of v***).

For a linear transformation $T_A$, we have:

$$
[T(v)]_B=[T]_B[v]_B
$$

$$
[T]_B=\left[[T(b_1)]_B\ [T(b_2)]_B\ ...\ [T(b_k)]_B\right]
$$

## Similarity of matrices

Let $A$ and $B$ be square matrices. We say $A$ is **similar** to $B$ if

$$
B=P^{−1}AP
$$

for some invertible matrix $P$.

### Thus in some sense, similar matrices can be seen as matrices representing the same linear transformation with respect to different bases.