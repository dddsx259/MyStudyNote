# Mini-Lab 2: Signal — 题目理解

- **来源**: `lab/02-lab-signal.pdf` (约 3 页, 1 pt)
- **Starter**: `lab/02-lab2-signal.c`
- **课程**: COMP3230B

## 目标

动手使用信号相关接口: 注册 handler、处理 `SIGUSR1`、理解不可重定义的 `SIGKILL` 等.

## TODO 摘要

1. 用 `signal()` (或题面指定 API) 将 `SIGUSR1` 绑定到 `sigusrHandler`
2. 在 handler 内终止程序 (如 `exit`)
3. 程序把 `getpid()` 写入 `pid.txt`, 便于另一终端 `kill -USR1 $(cat pid.txt)` 测试

## 与讲义对照

见 `Lec/04-process-abstraction-讲义.md` 信号节: sync/async、catch/ignore/mask、`SIGKILL`/`SIGSTOP` 不可捕获.

## 提交

`lab2-signal_<student_id>.c` (以 PDF 为准).
