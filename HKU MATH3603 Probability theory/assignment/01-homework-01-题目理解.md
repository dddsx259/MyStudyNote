# Homework 1 — 题目理解

- **来源**: `assignment/01-homework-01.pdf`
- **Due**: 2026-09-23
- **课程**: MATH3603 Probability Theory

## 题意摘要

| 题 | 内容 |
|---|---|
| 1 | 用归纳证明容斥原理 (inclusion-exclusion) 一般式 |
| 2 | 链式法则: $P(E_1\cap\cdots\cap E_n)=P(E_1)P(E_2\|E_1)\cdots P(E_n\|E_1\cap\cdots\cap E_{n-1})$ |
| 3 | 证明 Boole 不等式 $P(\bigcup_{i=1}^n E_i)\le\sum P(E_i)$; hint: 互斥化 $F_1=E_1$, $F_i=E_i\cap(\cap_{j<i} E_j^c)$ |
| 4 | 两厂尺子次品: I 产 2 倍于 II; I 次品 20%, II 5%. (i) 随机一根合格概率; (ii) 已知次品来自 I 的概率 (Bayes) |
| 5 | $A,B,C$ 独立 ⇒ 证明 (i) $A$ 与 $B^c$ 独立; (ii) $A$ 与 $B\cap C$ 独立; (iii) $A$ 与 $B\cup C$ 独立 |

## 预备

Ch.1 概率公理、条件概率、独立性、Bayes. Tutorial 1 的 Boole / 互斥化技巧可直接用到第 3 题.
