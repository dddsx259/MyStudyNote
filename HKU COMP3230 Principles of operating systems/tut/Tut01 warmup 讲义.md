# Tutorial 1 — Warm Up: 讲义

- **来源**: `tut/Tut01 warmup.pdf` (41 页)
- **Tutor**: Mingyan Gao · 2026
- **课程**: COMP3230B Principles of Operating Systems
- **对齐**: Lec01–Lec03 / Lec05 概念; Linux 工作流; C for OS; 为 Lab/PA/PS1 打底
- **短摘要**: 同目录 `Tut01 warmup 总结.md`

---

## 0. 本 Tut 要解决什么

把「听过课」变成「能在 workbench 上干活」. 四块:

| Part | 目标 |
|---|---|
| I Lecture Review | 分清 user/kernel · process · mode switch · context switch · interrupt · signal |
| II Linux Workflow | 本地开发 → workbench2 终测的标准路径 |
| III C for OS | 指针/内存/底层 I/O, 少踩 Lab/PA 的雷 |
| IV Put Together | 信号注册与调试 readiness |

---

## 1. Part I — Lecture Review

### 1.1 三个核心问题

1. **应用如何请求 OS 服务?** → **system call** (陷入内核, 执行特权代码后返回用户态)
2. **多进程如何共享一颗 CPU?** → **context switch** (保存/恢复足够上下文, 换另一个 ready 进程跑)
3. **OS 如何从用户程序手里夺回 CPU?** → **interrupt** (时钟/设备等硬件打断当前执行流, 进入内核)

这三问贯穿 Intro / Virtualize CPU / Process 各讲.

### 1.2 User Mode vs Kernel Mode

| | User mode | Kernel mode |
|---|---|---|
| 权限 | 受限: 不能随意执行特权指令, 不能自由访问硬件与其他进程内存 | 特权: 控制硬件与受保护资源 |
| 谁在跑 | 普通应用程序 | OS 内核 (处理 syscall / interrupt / 异常) |

典型路径:

```text
用户程序  --syscall-->  内核处理  --return-->  用户程序继续
```

**要点**: 进入内核不等于换了一个进程; 常常是**同一个进程**以 kernel mode 执行内核代码 (mode switch).

### 1.3 Program vs Process; 地址空间

- **Program**: 磁盘上的被动映像 (可执行文件)
- **Process**: 执行中的主动实例 = 地址空间 + 寄存器/PC + 可调度状态 + 资源 (打开文件等)

典型用户地址空间布局 (示意, 高地址在上):

```text
高地址  Stack  (向下增长)
         ↓
         …
         ↑
        Heap   (向上增长)
        Data   (全局/静态)
低地址  Text   (代码)
```

**易错**: 指针变量与所指对象可以分属不同区. 例: `int *p` 本身在 **栈**, `p = malloc(...)` 后 `*p` 在 **堆**.

### 1.4 PCB (Process Control Block) 与状态

PCB 是内核跟踪进程的数据结构, 典型字段包括:

- PID, 状态 (running / ready / blocked / zombie …)
- 程序计数器 PC, 通用寄存器快照
- 调度信息 (优先级, 时间片等)
- 内存信息 (页表/段信息指针)
- 父子关系, 打开文件表等资源指针

**为何必须有 PCB**: 进程被挂起后再恢复时, 必须能还原「当时跑到哪、寄存器是什么」. 没有足够上下文就无法正确 resume.

### 1.5 UNIX 进程 API 三角

| 调用 | 作用 | 是否新建进程 |
|---|---|---|
| `fork` | 复制当前进程, 造出一个子进程 (初为父的副本) | 是 |
| `exec*` | **替换**当前进程的程序映像 | 否 (PID 通常不变) |
| `wait` / `waitpid` | 父进程等待子进程结束并取退出状态 | 否 |

口诀: **`fork` 造进程; `exec` 改它在跑什么; `wait` 收尸取状态.**

细节与练习见 Tut02; 此处只需建立三角关系.

### 1.6 Signals (信号)

- 内核向进程递送的**软件通知**
- **同步**例: 非法访存 → `SIGSEGV` (与当前指令相关)
- **异步**例: 定时器, 另一进程 `kill`, 终端 Ctrl-C → `SIGINT`

进程对信号的处置大致: **catch** (注册 handler) / **ignore** / **mask** (暂时屏蔽).

硬规则: **`SIGKILL` / `SIGSTOP` 不可捕获、不可阻塞、不可忽略**.

### 1.7 Mode switch ≠ Context switch; Interrupt ≠ Signal

| 概念 | 含义 | 是否换进程 |
|---|---|---|
| **Mode switch** | 同一进程在 user ↔ kernel 间切换 (典型: syscall, 或处理 trap) | 通常**不**换 |
| **Context switch** | 挂起当前进程 → 存上下文 → 选另一个 ready → 恢复 → 继续 | **换** |

| 概念 | 层次 |
|---|---|
| **Interrupt** | 硬件/CPU: 「现在必须看我」→ 进入内核 |
| **Signal** | 内核 → 进程: 「有件事通知你」 |

Ctrl-C 粗路径 (直觉): 键盘中断 → 内核处理 → 向前台进程组递送 **SIGINT** → 进程按 disposition 处理.

**PS1 常考**: syscall 本身通常只有 mode switch; 只有调度器决定换人时才有 context switch.

### 1.8 自测三题

1. 一次成功的 `read()` syscall: 一定发生 context switch 吗?  
   → **不一定**. 多数情况是本进程 mode switch 进内核再返回; 若阻塞等待 I/O, 可能被换下 (那时才有 context switch).
2. Interrupt 和 Signal 是一层概念吗?  
   → **不是**. Interrupt 在硬件/CPU 注意力层; Signal 在进程通知层, 常由前者间接导致.
3. `p = malloc(4);` 后 `&p` 与 `p` 各在哪?  
   → `&p` (指针变量地址) 在栈; `p` 的值是堆上对象地址.

---

## 2. Part II — Linux Workflow

### 2.1 评分环境

- **workbench2.cs.hku.hk (Ubuntu)** 是作业最终权威环境 (经 HKUVPN)
- 推荐: 本地 Linux / WSL2 / 课程 Docker 开发调试 → 上传 workbench **终测再交**
- 也可直接在远程开发, 但要熟悉延迟与工具链

### 2.2 常用 shell 技能

- 文件: `ls`, `cd`, `cp`, `mv`, `rm`, `mkdir`, `cat`, `less`
- 管道 `|`, 重定向 `>`, `>>`, `<`
- 后台 `&` (与后续作业「前台 shell wait 子进程」对照理解)

### 2.3 编译

- 无 Make: `gcc -Wall -o prog prog.c`
- 有 Make: 写 `Makefile`, 用 `make` 驱动 `gcc`
- 分清三类问题:
  - **compiler error**: 语法/类型, 无法生成目标文件
  - **warning**: 能编过但可疑 (Lab/PA 建议 `-Wall` 清干净)
  - **runtime error**: 能跑但崩 (如 segfault) — 用 `gdb` / `perror`

---

## 3. Part III — C for OS

OS 课里的 C 更接近「和内核接口说话」, 不是只写上层业务逻辑.

### 3.1 必须熟练

- 指针与数组/字符串的关系 (`char *` vs `char[]`)
- 结构体布局直觉; **不要猜**类型大小 → 用 `sizeof`, 需要固定宽度时用 `<stdint.h>`
- 栈上自动变量 vs `malloc`/`free` 堆对象; 避免: 越界, 悬空指针, 泄漏, 返回局部地址

### 3.2 底层 I/O vs stdio

| | 底层 (POSIX) | 标准库 |
|---|---|---|
| 典型调用 | `open` / `read` / `write` / `close` | `fopen` / `fread` / `printf` |
| 对象 | 文件描述符 `int fd` | `FILE *` |
| 用途 | 作业里管道、重定向、精确控制 | 日常打印方便 |

PA1/Tut2 会大量用到底层 fd + `dup2`.

---

## 4. Part IV — Signals, Debugging, Readiness

### 4.1 信号注册预告

- 了解 `signal` / 更推荐的 `sigaction` 可注册 handler
- 衔接: **Mini-lab 2 (Signal)**; **PA1** 要求 shell 自身不被 Ctrl-C 杀掉, 子进程按自己逻辑处理

### 4.2 调试

- `gdb`: 断点, `run`, `bt`, `print`
- 系统调用失败: 查 `errno`, 用 `perror("msg")` 打印可读原因

### 4.3 Readiness 清单

完成本 Tut 后你应能:

1. 登录 workbench2, 上传/编译/运行简单 C 程序
2. 用自己的话区分 user/kernel、process、mode vs context、interrupt vs signal
3. 说出 `fork` / `exec` / `wait` 各自干什么 (细节留给 Tut02)

---

## 5. 与后续作业的关系

| 后续 | 本 Tut 贡献 |
|---|---|
| Mini-lab / PA 环境 | Linux + gcc/make 工作流 |
| PS1 Q1–Q2 | mode/context · interrupt/signal 概念 |
| Tut02 / PA1 | 进程 API 三角的入口 |

---

## 6. 参考

- 课件: `Lec/Lec01 course overview`, `Lec03 introduction`, `Lec04 process abstraction`, `Lec05 virtualize cpu`
- OSTEP: Ch.2 (与 Intro 对齐), 后续 Ch.4–5 在 Tut02 展开
- man: `man 2 intro` (系统调用概览)
