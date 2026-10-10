# Tutorial 1 — Warm Up 总结

- **来源**: `tut/Tut01 warmup.pdf` (41 页)
- **Tutor**: Mingyan Gao · 2026
- **主题**: Lec01–03 概念复习 + Linux 工作流 + C for OS + 信号/调试就绪检查

---

## 日程四块

| Part | 内容 |
|---|---|
| 01 Lecture Review | user/kernel, process, syscall/switch/interrupt |
| 02 Linux Workflow | workbench, GCC/Make/Git, 本地→远程 |
| 03 C for OS | 指针/数组/字符串/结构体/内存/底层 I/O |
| 04 Put Together | 信号, 调试, readiness |

---

## Part I — Lecture Review (核心图)

三问:

1. App 如何请求 OS 服务? → **system call**
2. 多进程如何共享一 CPU? → **context switch**
3. OS 如何夺回 CPU? → **interrupt**

### User vs Kernel Mode

- User: 受限, 无特权指令, 不能自由访硬件/他进程内存
- Kernel: 特权, 控硬件与受保护资源
- 路径: 用户程序 → syscall → kernel → return

### Process

- Program = 磁盘上被动映像; Process = 执行中的主动实例 (状态+资源+可调度)
- 地址空间: Text / Data / Heap / Stack (高地址栈 → 低地址代码); **指针变量与所指对象可分属不同区** (如 `p` 在栈, `*p` 在堆)

### PCB 与状态

PCB 记: PID, state, PC, 寄存器, 调度信息, 内存信息, 父子, 资源指针. 恢复被暂停进程必须有足够上下文.

### UNIX API 三角

| 调用 | 作用 |
|---|---|
| `fork` | 造进程 (子初为父的副本) |
| `exec` | **换映像**, 不造新进程 |
| `wait`/`waitpid` | 父等子, 取终止状态 |

口诀: `fork` 造进程; `exec` 改它在跑什么.

### Signals

- 内核通知进程事件; 同步 (如 SIGSEGV) vs 异步 (如 timer, `kill`)
- 到达后可: catch / ignore / mask
- **SIGKILL / SIGSTOP** 不可捕获、阻塞、忽略

### Virtualize CPU / Mode ≠ Context

- Context switch: 挂起→存上下文→选 ready→恢复→继续
- Mode switch: **同一进程** user⇄kernel (syscall); **不必**换进程
- Interrupt (硬件/CPU 注意力) ≠ Signal (内核→进程通知); 相关但不同层

---

## Part II — Linux Workflow

- 评分环境 **workbench2 (Ubuntu)** = 最终权威
- 推荐: 本地 Linux 开发调试 → 拷到 workbench 终测提交; 或远程开发
- 常用: 文件命令, 管道 `|`, 重定向, 后台 `&`, 组合

### 编译

- 无 Make: 直接 `gcc`
- 有 Make: `Makefile` → gcc → 可执行文件
- 分清: compiler error / warning / runtime error

---

## Part III — C for OS (要点)

- 指针与数组/字符串关系; 结构体布局
- **勿猜类型大小**; 用 `sizeof` / 固定宽度类型
- 低级 I/O: `open/read/write/close` vs stdio
- 常见声明与内存错误 (越界, 悬空, 泄漏) — 为 Lab/PA 打底

---

## Part IV — Signals & Debugging / Readiness

- 复习 `signal`/`sigaction` 注册; 与后续 Mini-lab 2 / PA1 SIGINT 衔接
- 调试: `gdb`, 打印 `errno`/`perror`
- Readiness: 能在 workbench 登录, 编译运行 C, 理解 user/kernel 与 process API 三角

---

## 关键练习/自测 (tut 内嵌思想)

1. **Mode vs Context**: syscall 只有 mode switch 还是一定 context switch? → 仅当调度器换进程才有后者.
2. **Interrupt vs Signal**: Ctrl-C 路径大致是 键盘中断 → 内核 → 向前台进程组递送 SIGINT.
3. **栈上指针 vs 堆对象**: 画 `malloc` 例子分清两区.

---

## 与后续作业关系

- Lab / PA 必须在 Linux + gcc 流程下完成
- 概念块直接服务 PS1 Q2 (mode/context) 与 Process 题
