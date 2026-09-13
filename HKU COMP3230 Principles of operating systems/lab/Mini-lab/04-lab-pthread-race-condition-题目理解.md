# Mini-Lab 4: Pthread & Race Condition — 题目理解

- **来源**: `lab/04-lab-pthread-race-condition.pdf` (3 页, 1 pt)
- **Starter**: `lab/04-lab4-pthread.c`
- **课程**: COMP3230B

## 目标

- 使用 **Pthread** 创建/汇合线程
- 识别 `counter++` **竞态 (race condition)**, 用条件变量或信号量修复

## 要点

- 线程共享地址空间; 比 `fork` 轻, 但需同步
- 期望: 4 线程各加 `1e6` 次 → `counter == 4e6`
- 无保护时终值偏小且不稳定 (`++` 非原子: load / add / store)
- 编译: `gcc … -pthread`

## TODO 摘要

1. `pthread_create` → `count_up`
2. `pthread_join` 等待全部结束
3. 用 mutex / 条件变量 / semaphore 保护 `counter++` (题面允许 CV 或 semaphore)

## 与现有讲义

- OSTEP Ch.2 / Intro 讲义给 race 直觉
- **Pthread API 与同步原语** 主要靠本题面 + Tutorial 3 (Pthread); `04-process-abstraction` 几乎不讲 Pthread

## 提交

`lab4-pthread_<student_id>.c` (以 PDF 为准).
