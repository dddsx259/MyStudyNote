# Mini-Lab 1: C Basics & Address Space — 题目理解

- **来源**: `lab/01-lab-c-basics-address-space.pdf` (5 页, 1 pt)
- **Starter**: `lab/01-lab1-stack.c`, `lab/01-lab1-heap.c`
- **课程**: COMP3230B

## 目标

- 复习 C 的编写 / 编译 / 调试
- 理解 **栈 (stack)** 与 **堆 (heap)** 变量的差异与正确管理

## 要点 (题面)

| | Stack | Heap |
|---|---|---|
| 分配 | 函数/块内声明即可 | `malloc` / `calloc` 等 |
| 释放 | 离开作用域自动释放 | 必须 `free` |
| 特点 | 快、大小受限、常需编译期可知大小 | 灵活、较慢、需防泄漏与碎片 |

- 全局变量: 在所有函数外声明, 各函数可共享
- `lab1-stack.c`: 返回局部数组指针 → **悬空指针** (离开函数栈帧已失效); 观察错误行为
- `lab1-heap.c` TODO: `malloc(n * sizeof(int))` → 填 `arr[i]=i*i` → `free(arr)`
- 命令行: `./prog <n>`; `argc`/`argv` + `atoi`

## 提交

完成 TODO 后按 PDF 要求命名提交 (如 `lab1-heap_<student_id>.c`).
