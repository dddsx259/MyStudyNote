# Chapter 5  Eigenvalues, Eigenvectors and Diagonalization

Created: 2025年3月15日 17:11
Class: MATH2101

# Eigenvalues and eigenvectors

## Definition:

Let $A$ be a square matrix. If $Ax=\lambda x$ for some non-zero vector $x$ and scalar $t$, is said to be an **eigenvalue** of $A$ ;

$x$ is called an **eigenvector** of $A$ corresponding to the eigenvalue ,or in short, a of $A$.

## Finding eigenvalues

Let $A$ be an $n\times n$ matrix.

The equation $det(A-tI) = 0$ is called the ***characteristic equation*** of $A$.

The LHS of the characteristic equation, is said to be the ***characteristic polynomia**l* of $A$. 

Eigenvalues of $A$ are thus roots of its characteristic equation, or zeros of its characteristic polynomial.

It can be proved by induction on $n$ that the characteristic polynomial of $A$ is indeed a polynomial (with degree n).
P.S. Some authors prefer to use $det(tI-A)$ instead of $det(A-tI)$.

### Then we call $Null(A-tI)$ as *eigenspace* of $A$ corresponding of t, or in shorter, the t-eigenspace of $A$

## Algebraic multiplicity and geometric multiplicity

A degree $n$ polynomial (where $n>1$) with coefficients in $\mathbb{C}$ has exactly $n$ zeros(零点) in $\mathbb{C}$ (counting multiplicities，重根). 

It thus follows that a $n×n$ matrix $A$ has exactly $n$ eigenvalues in  $\mathbb{C}$ (counting multiplicities)

The ***algebraic multiplicity*** (or simply ***multiplicity***) of an eigenvalue is the number of times it appears as a zero of the character polynomial.

The ***geometric multiplicity*** of an eigenvalue is the dimension of its corresponding eigenspace.

It can be shown that

### The algebraic multiplicity of an eigenvalue is always greater than or equal to its geometric multiplicity.

---

### Diagonalization(对角化)
#### diagonalizable:
An $n\times n$ matrix $A$ is **diagonalizable** IFF it has $n$ **linear independent** eigenvectors.
  - Eigenvectors of a matrix $A$ that correspond to distinct eigenvalues are linearly independent.
- If a matrix $A$ has an eigenvalue whose geometric multiplicity is less than the algebraic multiplicity, then $A$ is not diagnosable.    

Thus, A matrix $A$ is diagonalizable if and only if for each of its eigenvalues, the algebraic and geometric  multiplicities are equal.
#### Process
If $A$ is a diagonalizable $n\times n$ matrix, it has $n$ **eigenvalues**:$\{\lambda_1, \lambda_2, ... \lambda_n\}$ and $n$ **corresponding linear independent eigenvectors**:$\{v_1, v_2, ... v_n\}$
$$
(i.e. \forall i\in\mathbb{R}\ Av_i=\lambda_i v_i)
$$
Then we have:
$$A=PDP^-1$$
where $P$ is **eigenvector matrix** and $D$ is **diagonal matrix of eigenvalues**
$$P=
\begin{bmatrix}
v_1 & v_2 & \cdots & v_n
\end{bmatrix},\ 
D=\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0\\
0 & \lambda_2 & \cdots & 0\\
\cdots & \cdots & \cdots & \cdots\\
0 & 0 & \cdots & \lambda_n\\
\end{bmatrix}
$$
