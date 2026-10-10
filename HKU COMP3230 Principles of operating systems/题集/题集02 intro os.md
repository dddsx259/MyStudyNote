# 题集 — Intro OS (虚拟化直觉)

> 对齐: `Lec/Lec03 introduction 讲义.md`, `Lec/OSTEP 2 introduction 讲义.md`, `lec2_code_example/`.
> 含: (1) 课件证明 (2) 练习题.

---

## 课件证明

### P1. 并发 `counter++` 可丢失更新

- **陈述**: 同地址空间内两线程各对共享 `counter` 执行 $N$ 次 `counter++`, 终值可能 **小于** $2N$ 且随调度不稳定.
- **证明**: 源码级 `counter++` 在机器上通常非原子, 至少三步: (1) 从内存 load 到寄存器; (2) 寄存器加 1; (3) store 回内存. 两线程交错时, 两次 load 可读到同一旧值, 各自 +1 后写回, 等价于只加一次. 故丢失更新. `threads_mutex` 用互斥锁串行化临界区可避免.
- **来源**: `Lec/OSTEP 2 introduction 讲义.md` §2.3 / `threads.c` 演示

### P2. 系统调用须提升特权级 (相对库函数)

- **陈述**: 应用不能当作普通库函数任意调用「写磁盘任意扇区」等操作; 须经 **system call** 进入 OS, 同时硬件 **提升特权级** (user → kernel).
- **证明**: 若任意用户态代码可直接发磁盘 I/O 或访问任意物理页, 则进程间 **无隔离**, 文件系统无法保证隐私与保护. 故 OS 代表系统的代码须更高权限; 受控入口 = 特殊 trap 指令 + 预设 handler. 完成后 **return-from-trap** 回到用户态与原中断点. 这与普通过程调用 (不改变特权级) 不同.
- **来源**: OSTEP 讲义 §2.6 超越库: 保护; 对照 `Lec/Lec03 introduction 讲义.md` trap 机制

---

## 练习题

## Mini-Lab

### 1. Warm up: Linux 与 auth log

- **题目**: (Task 1) 经 HKUVPN SSH 到 `workbench2.cs.hku.hk`, 熟悉课方 lab 仓库. (Task 2) 练习 `cd`, `touch`, `mkdir`, `ls`, `grep`, 管道/重定向, `wc`, `cat`, `ps`, `kill`, `htop`, `man`. (Task 3) 解压认证日志, 用命令行找出 **可疑 SSH 失败登录的 IP**.
- **思路**: 管道 + `grep`/`awk` 过滤 `Failed`/`Invalid` 等字段; 统计 IP 出现次数 (`sort | uniq -c`). 评分以 workbench2 为准.
- **来源**: `lab/Mini-lab/Lab00 warmup welcome to linux 题目理解.md`

---

## OSTEP / 课件演示

### 2. 多进程共享单 CPU (`cpu.c`)

- **题目**: 编译运行 `lec2_code_example/cpu.c`. 单实例与 `./cpu A & ./cpu B & ./cpu C & ./cpu D &` 输出有何不同? 物理 CPU 只有一个时, OS 提供了什么抽象?
- **思路**: 多进程输出交错; **CPU 虚拟化** — 调度制造「多程序同时跑」的幻觉. 可配合 `taskset -c 0` 绑单核观察.
- **来源**: `Lec/OSTEP 2 introduction 讲义.md` §2.1, `lec2_code_example/README.md`

### 3. 虚拟地址相同 (`mem.c`)

- **题目**: 运行 `mem.c` 单进程记录打印地址; 再同时跑两个实例. 两进程打印的虚拟地址能否相同? 各自递增是否独立? 为何要 `setarch x86_64 -R` 关 ASLR?
- **思路**: 相同虚拟地址映射到不同物理页 → **内存虚拟化**, 每进程私有地址空间. ASLR 会随机化基址, 演示需关闭以便对比.
- **来源**: OSTEP 讲义 §2.2, `lec2_code_example/README.md`

### 4. 并发竞态 (`threads.c`)

- **题目**: 运行 `./threads 1000` 与 `./threads 100000`. 期望终值 $2\times\texttt{loops}$, 大 loops 时实际如何? 对比 `./threads_mutex`. 解释为何 `counter++` 会错.
- **思路**: 见 **P1**; mutex 保护后应恒为 $2N$. 对应 Crux: 如何写正确并发程序?
- **来源**: OSTEP 讲义 §2.3, `lec2_code_example/README.md`

### 5. 持久化三 syscall (`io.c`)

- **题目**: `io.c` 通过哪三个系统调用把数据写到文件? 与「每进程私有虚拟磁盘」说法是否一致?
- **思路**: `open` → `write` → `close`; 文件系统管理共享持久存储, 通常 **不** 为每应用造私有盘, 用户文件共享命名空间.
- **来源**: OSTEP 讲义 §2.4

---

## Crux / 概念

### 6. OS 设计焦点 (how)

- **题目**: 课程强调 OS 研究/设计时少问「为何需要 OS」, 应多回答哪三类问题?
- **思路**: 用什么 **mechanism** 与 **policy**; 如何高效; 需要何种 **硬件支持**.
- **来源**: `Lec/Lec03 introduction 讲义.md` §2.2, OSTEP 导读

### 7. 虚拟化 CPU 的 Crux

- **题目**: 用一句话说明: 只有一个物理 CPU 时, 如何让多个程序 **看似** 同时运行? 谁先跑由谁决定?
- **思路**: OS (硬件协助) 分时/调度 → 虚拟 CPU 幻觉; **policy** (调度器) 决定就绪进程顺序.
- **来源**: OSTEP 讲义 §2.1

### 8. 虚拟化内存的 Crux

- **题目**: 什么是 **virtual address space**? 一进程访存为何通常不影响另一进程?
- **思路**: OS 为每进程维护独立虚拟地址到物理页的映射; 映射隔离.
- **来源**: OSTEP 讲义 §2.2

### 9. 持久化的 Crux

- **题目**: DRAM 断电后数据如何? 文件系统除「写数据块」外还要解决哪些正确性/性能问题 (举 1–2 个)?
- **思路**: 内存易失; 需 journaling 或 copy-on-write 等应对崩溃; 延迟写/批处理换性能; B-tree 等索引.
- **来源**: OSTEP 讲义 §2.4
