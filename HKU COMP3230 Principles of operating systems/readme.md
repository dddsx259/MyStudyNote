# COMP3230 Principles of Operating Systems

> 最后更新: 2026-10-10 — Tut03 pthread 入库; 根目录重复 slides 已删

## 结构规范

本课使用父目录 [`文件结构参考.md`](../文件结构参考.md); 命名见 skill `reference-naming.md`.

## 目录结构

| 路径 | 用途 |
|---|---|
| `Lec/` | lecture slides (`Lec{NN} …`) + OSTEP 阅读 (`OSTEP {章} …`) |
| `assignment/` | Problem Set / Programming Assignment |
| `tut/` | Tutorial slides + 总结 |
| `lab/Mini-lab/` | Mini-Lab 题面 + starter `.c` + 题目理解 |
| `lab/Mini-lab/submission/` | 已提交稿 (`lab*_3036292116.c`) |
| `题集/` | 按章节练习题 + 课件证明 |
| `docs/` | cache / 官网 HTML·webarchive / Final 生成约定 |
| `课程信息.md` | 全课唯一课程信息 (课程根) |
| `cheatsheet.md` | 词条速查 |
| `index.md` | AI md 跳转索引 |
| `readme.md` | 本文件 |

## 产出索引

| 文件 | 原始材料 | 说明 |
|---|---|---|
| `课程信息.md` | Overview + Moodle HTML | 评分 / ILO / 政策 / due |
| `Lec/Lec01 course overview 讲义.md` | `Lec/Lec01 course overview.pdf` | 导论 |
| `Lec/Lec02 c programming 讲义.md` | `Lec/Lec02 c programming.pdf` | C 预备 |
| `Lec/Lec03 introduction 讲义.md` | `Lec/Lec03 introduction.pdf` | OS 导论 / 架构 |
| `Lec/OSTEP 2 introduction 讲义.md` | `Lec/OSTEP 2 introduction.pdf` | OSTEP Ch.2 必读 |
| `Lec/Lec04 process abstraction 讲义.md` | `Lec/Lec04 process abstraction.pdf` | 进程 / 信号 |
| `Lec/OSTEP 4 process 讲义.md` | `Lec/OSTEP 4 process.pdf` | OSTEP Ch.4 |
| `Lec/OSTEP 5 process api 讲义.md` | `Lec/OSTEP 5 process api.pdf` | OSTEP Ch.5 |
| `Lec/Lec05 virtualize cpu 讲义.md` | `Lec/Lec05 virtualize cpu.pdf` | LDE / 中断 |
| `Lec/OSTEP 6 limited direct execution 讲义.md` | `Lec/OSTEP 6 limited direct execution.pdf` | OSTEP Ch.6 |
| `Lec/Lec06 scheduling 讲义.md` | `Lec/Lec06 scheduling.pdf` | FIFO/SJF/RR/MLFQ/… |
| `Lec/OSTEP 7 scheduling 讲义.md` | `Lec/OSTEP 7 scheduling.pdf` | OSTEP Ch.7 |
| `Lec/OSTEP 8 mlfq 讲义.md` | `Lec/OSTEP 8 mlfq.pdf` | OSTEP Ch.8 |
| `Lec/OSTEP 9 lottery 讲义.md` | `Lec/OSTEP 9 lottery.pdf` | OSTEP Ch.9 |
| `Lec/Lec07 thread concept 讲义.md` | `Lec/Lec07 thread concept.pdf` | 线程 / 竞态 |
| `Lec/Lec08 synchronization 讲义.md` | `Lec/Lec08 synchronization.pdf` | 锁 / CV / 信号量 / 生产者-消费者 / 读者-写者 |
| `Lec/Lec09 deadlock 讲义.md` | `Lec/Lec09 deadlock.pdf` | 死锁四条件 / 预防 / 避免 / 银行家 / 检测恢复 |
| `Lec/OSTEP 26 threads intro 讲义.md` | `Lec/OSTEP 26 threads intro.pdf` | OSTEP Ch.26 |
| `Lec/OSTEP 27 threads api 讲义.md` | `Lec/OSTEP 27 threads api.pdf` | OSTEP Ch.27 |
| `Lec/OSTEP 28 locks 讲义.md` | `Lec/OSTEP 28 locks.pdf` | OSTEP Ch.28 (锁硬件实现) |
| `Lec/OSTEP 30 condition variables 讲义.md` | `Lec/OSTEP 30 condition variables.pdf` | OSTEP Ch.30 (CV + join/生产者-消费者) |
| `Lec/OSTEP 31 semaphores 讲义.md` | `Lec/OSTEP 31 semaphores.pdf` | OSTEP Ch.31 (信号量 + 读者-写者/哲学家) |
| `Lec/OSTEP 32 common concurrency problems 讲义.md` | `Lec/OSTEP 32 common concurrency problems.pdf` | OSTEP Ch.32 (并发 bug 模式 + 死锁) |
| `assignment/PS01 problem set 1 题目理解.md` | PS1 | due 2026-10-09 10:29; 6 pts |
| `assignment/PS01 problem set 1 解答.md` | PS1 | 完整解答 (中文说明 + 英文 Answer; 多解全列) |
| `assignment/PA01 programming assignment 1 题目理解.md` | PA1 yash | due 2026-10-16 10:29; 15 pts |
| `assignment/PA01 programming assignment 1 解答.md` | PA1 | 设计/伪代码解答 (中文说明 + 英文 Answer; 多实现并列) |
| `tut/Tut01 warmup 总结.md` | Tut1 | Warm Up |
| `tut/Tut02 processes 总结.md` | Tut2 | Processes + PA1 对照 |
| `tut/Tut03 pthread 总结.md` | Tut3 | Pthread create/join · mutex · cond |
| `lab/Mini-lab/Lab0x … 题目理解.md` | Lab0–4 | Mini-labs |

## 备注

- Mini-Lab 在 `lab/Mini-lab/`; 已提交稿在 `submission/`
- OSTEP 全书仓: `Lec/textbook/ostep/`; **对齐阅读用 `OSTEP {章}`**, 与 slides 的 `Lec{NN}` **不共享编号**
- 写讲义前置约定: `docs/给AI-final考点与生成约定.md`
