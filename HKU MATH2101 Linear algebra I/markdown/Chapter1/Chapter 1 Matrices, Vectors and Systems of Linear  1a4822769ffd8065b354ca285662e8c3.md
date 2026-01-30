# Chapter 1 Matrices, Vectors and Systems of Linear Equations

Created: 2025年2月24日 18:59    
Class: MATH2101    

### **Triangular matrix:**

A matrix that only upper or lower triangular entry is non-zero.

A matrix is **upper triangular** if the (i j)-entry is 0 whenever $i>j$.

A matrix is **lower triangular** if the (i j)-entry is 0 whenever $i<j$.

### **Diagonal matrix:**

A square matrix that both upper and lower triangular

(i.e.Only diagonal entries is non-zero)

### **Standard vectors**

A vector in whose only i-th entry is 1 is denoted by $e_i:\ e_1, e_2, ..., e_n$ are collectively known as the **standard vectors** $e_i$ (also called **standard unit vectors** or **standard basis vectors**) 

### **Identity Matrix I**:

A matrix that only diagonal entries are 1, others are all 0

### The two systems are **equivalent** if they have the same solution set.

### A **linear equation** can be written in the form $A\vec{x}=\vec{b}$:

A: **coefficient matrix**  
**x**: **unknows**  
**b**: **RHS constants**

### **Augmented matrix**:

We append RHS constants vector to coefficient matrix, written as the following form:
$ [A\ |\ b] $

### **EROs**: **elementary row operations**

(I) **Exchange** two rows

(II) **Multiply** a row by a nonzero constant

(III) **Add** a multiple of a row to another row

### **REF row echelon matrix:**

(1)  Zero rows must be at the bottom of the matrix (if any)

(2) The **leading entry** (i.e. first non-zero entry, also called **pivot**) of non-zero row must be on the right of the leading entries in the rows above (i.e. the entries below a leading entry must be 0)

We call it is in **row echelon form (REF)**

### **RREF reduced row echelon matrix:**

(3) The column that each leading entry in only has one non-zero entry (i.e. pivot itself)

(4) Every leading entry of non-zero rows are 1

We call it is in **reduced** **row echelon form (RREF)**, or **row canonical form**

### **Inconsistent:**

If there is a linear system with no solution at all, it’s **inconsistent.**

&emsp;i.e. It's RREF has $[0\ 0\ ...\ 0\ |\ 1]$

### Given the system A**x** = **b**, the following statements are **equivalent.**

(a) The system is consistent.

(b) The vector $b$ is a linear combination of the columns of $A$.

(c) The reduced row echelon form of the augmented matrix of the system has no row of the form $[0\ 0\ …\ 0\ |\ 1]$.

### 更一般地，在解决具有无限多解的线性系统时，我们可以将增广矩阵转换为简化行最简形式。设定那些对应于非主元列的变量为**自由变量(free variables)**，而那些对应于主元列的变量为**基础变量(basic variables)**。需要注意的是，简化行最简形式使得基础变量很容易用自由变量表示出来。

c

If system $Ax=b$ is consistent, the **rank** and **nullity** of $A$ indicate the **number of basic variables** and **number of free variables** respectively.

### **Span** and **Generation set**:

Let $S$ be a finite non-empty set of vectors in $\mathbb{R}^n$, the **span** of $S$ (denoted by **$span(S)$**) is defined to be the set of all linear combinations of the vectors in S

If $V⊆\mathbb{R}^n$ and $S$ is a set of vectors in $\mathbb{R}^n$, then $S$ **is said to be a **generating set** for V (or simply $S$ generates $V$) if every vector in $V$ can be expressed as a linear combination of the vectors in $S$

### Let A be an $m\times n$ matrix. The following statements are equivalent.

(a) $Ax = b$ is consistent for every **$b\subseteq \mathbb{R}^m$**.

(b) The span of the columns of $A$  is $\mathbb{R}^m$.

(c) The RREF of $A$  has no zero row.

(c’) The RREF of $[A\ |\ b]$ has no row of the form $[0\ 0\ …\ 0\ |\ 1]$ for every **$b⊆\mathbb{R}^m$**

(d) rank(A) = m

### Let A be an $m\times n$ matrix. The following statements are equivalent.

(a) The columns of $A$ are linearly independent.

(b) $Ax = b$ has at most one solution for every **$b⊆\mathbb{R}^m$**.

(c) $nullity(A) = 0$

(d) $rank(A) = n$

(e) The RREF of A is $[e_1\ e_2\ …\ e_n]$

(f) The system $Ax = 0$ only has the **trivial solution**.