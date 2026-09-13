# Mini-Lab 3: Process — 题目理解

- **来源**: `lab/03-lab-process.pdf` (4 页, 1 pt)
- **Starter**: `lab/03-lab3-process.c`
- **课程**: COMP3230B

## 目标

- 使用 `fork()` / `wait()` / `exec()` 族
- 理解父子进程关系与 `pstree` 所见进程树

## 题面要点

- `fork()`: 子进程返回 0, 父进程返回子 PID; 不分支则父子跑同一段代码, 易混乱
- `exec*()`: 用新程序映像替换当前进程 (PID 不变); `exec` 成功后其后代码不执行
- 实验步骤: Terminal1 记 shell PID → 编译运行 lab3 → 子进程 `sleep 20` 期间 Terminal2 用 `pstree -sp` 观察 `SSH → bash → lab3 → sleep`

## TODO 摘要

1. `pid = fork()`
2. 子进程: `exec` 跑 `sleep` / `20`
3. 父进程: `wait` (或 `waitpid`) 等子进程结束

## 提交

`lab3-process_<student_id>.c` (以 PDF 为准).
