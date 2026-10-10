# Tutorial 1 — 总结

- **来源**: `tut/Tut01.pdf` (题面; 原名 `TUT1-Q.pdf`) + `tut/Tut01 sol.pdf` (官方解; 原名 `TUT1-S.pdf`)
- **课程**: MATH2241 Introduction to Mathematical Analysis
- **对齐**: `Lec/Lec02 chapter1 real numbers 讲义.md` (有序域, 确界, 无理)

> 题意与证明要点; 有官方 sol 可对照. 陈述写清假设与结论.

---

## 题目一览

1. **有序域**: $a<b+\varepsilon$ 对一切 $\varepsilon>0$ $\Rightarrow$ $a\le b$ (反证: 若 $a>b$ 取 $\varepsilon=(a-b)/2$)
2. **求 $\sup/\inf$** (可无证明), 并说明是否为 max/min:
   - $S_1=\{x\neq 0:1/x>2\}$
   - $S_2=\{1/k+2/m+3/n:k,m,n\in\mathbb{N}\}$
   - $S_3=\{3^x:x\in\mathbb{Z}\}$
3. 非空有界 $A$ 且 $\inf A=\sup A$ $\Rightarrow$ $A$ 为单点集
4. $A\subseteq B$ (非空有界) $\Rightarrow$ $\inf B\le\inf A\le\sup A\le\sup B$
5. $A+B$, $AB$ 的 $\sup$: (a) $\sup(A+B)=\sup A+\sup B$? (b) $\sup(AB)=(\sup A)(\sup B)$? (需判断真假并证明/反例; 注意符号)
6. $w$ 为上界且 $\forall n$ 存在 $a_n\in A$ 使 $w-1/n\le a_n$ $\Rightarrow$ $w=\sup A$
7. 例子: 无理集上确界为有理; 有理集上确界为无理
8. 根式无理性: (a) $\sqrt[m]{n}$ 整数或无理; (b) $\sqrt{n}+\sqrt{n+1}$ 无理; (c) $\sqrt{n+\sqrt{n}}$ 无理

---

## 易错点

1. Q1 是有序域命题, 不需要完备性
2. $\sup$ 未必在集合内 (≠ max)
3. 乘积集 $AB$ 的确界对符号敏感, 不可盲目套公式
