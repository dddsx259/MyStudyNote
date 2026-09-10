# Process Abstraction: 归纳汇总

- **来源**: `Lec/04-process-abstraction.pdf` (30 页, 全覆盖; 原名 `02-ProcessAbstraction.pdf`)
- **课程**: COMP3230B Principles of Operating Systems
- **学习成果**: ILO2a – 解释 OS 如何管理进程/线程, 以及高效共享 CPU 的机制与策略

> 本讲以定义、数据结构与系统调用约定为主; 无非定义数学命题. 术语首次标英文.

**必读**: OSTEP Ch.4 [cpu-intro.pdf](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf); Ch.5 [cpu-api.pdf](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf).

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| Process vs Program | 程序是「死」的; **进程 (process)** = 执行中的程序实例 |
| 抽象四件套 | 内存视图 / 使用中的资源 / 执行状态 / 程序代码与数据 |
| 地址空间 | Text / Data / Heap / Stack |
| 状态 | new → ready ⇄ running → blocked → ready; terminated (zombie) |
| 关键结构 | **PCB (Process Control Block)**; 进程表; ready/blocked 列表 |
| 工具 | `ps`, `pstree` |
| 创建/终止 | Unix: `fork` + `exec`; Windows: `CreateProcess`; `exit` / `wait*` |
| Zombie | 已退出但 PCB 仍保留给父进程 `wait` |
| Suspend vs Block | block 多由进程自身活动触发; suspend 来自外部 |
| Signal | 软件中断式通知; sync / async; catch / ignore / mask; `SIGKILL`/`SIGSTOP` 不可捕获 |

---

## 1. Process vs Program (p.5–6)

- **程序 (program)** 本身是无生命的 (lifeless)
- **进程 (process)** 是:
  - 正在执行的程序 / 程序在计算机上的一个运行实例
  - 可被指派到 CPU 上执行的实体
  - 由「指令序列的执行 + 执行状态 + 一组关联系统资源」刻画的活动单元

OS 要为运行中的程序维护大致四类信息 (抽象):

| 类别 | 例子 |
|---|---|
| Memory | 进程可访问/引用的内存是进程的一部分 |
| Resources in use | I/O、物理内存等 |
| Execution state | 寄存器组 (含 PC、栈指针等); 当前进程状态 |
| Program code / Data | 代码与数据 |

---

## 2. 地址空间 (Address Space) (p.7)

进程对自己内存的视图称为 **地址空间 (address space)**: 一段内存位置 (地址) 的范围. 典型区域:

| 区域 | 存放 |
|---|---|
| **Text segment (代码段)** | 处理器执行的程序代码 |
| **Data segment (数据段)** | 全局 / 静态变量 |
| **Heap (堆)** | 动态分配内存 |
| **Stack (栈)** | 局部变量、函数参数、活动过程调用的返回值 |

示意: 从地址 `0` 到 `max` 排布上述区域 (具体布局因系统而异).

---

## 3. 进程状态与生命周期 (p.8–9)

**进程状态 (process state)**: 指示进程当前活动性质的标志.

| 状态 | 含义 |
|---|---|
| **new (initial)** | 正在创建 |
| **running** | 正在某处理器上执行 |
| **blocked** | 等待某事件 (如 I/O、通信) 后才能继续 |
| **ready** | 已可运行, 等待被调度到处理器 |
| **terminated (final / zombie)** | 已执行完但尚未完全清理; 为何不立刻丢掉? → 见 zombie / wait |

**典型转换** (生命周期图要点):

1. 分配好进程及其数据结构后 → 进入 **ready**
2. **dispatch (调度派发)**: ready → running
3. OS 决定切换: running → ready (如时间片用尽)
4. 等待资源: running → blocked
5. 等待事件发生: blocked → ready
6. 结束后进入 **terminated**; 保留该状态可让父进程检查返回码, 判断是否成功执行

---

## 4. 关键数据结构 (p.10–13)

### 4.1 Process Control Block (PCB)

为管理进程, OS 用数据结构维护进程信息: **进程控制块 (Process Control Block, PCB)** 或 **进程描述符 (process descriptor)**.

PCB 通常包含:

- **PID (process identification number)**: 唯一 ID
- 当前进程状态
- **程序计数器 (program counter, PC)**: 下一条指令地址
- **寄存器上下文 (register context)**: 上次离开 running 时的寄存器快照
- **调度信息 (scheduling information)**: 优先级、调度队列指针等
- **凭证 (credentials)**: 决定可访问哪些资源
- **内存管理信息**: 已分配内存区域
- **记账信息 (accounting)**: CPU 用量、时限等
- 指向父进程 / 子进程的指针
- 指向已分配资源的指针
- …

Linux 例子: `struct task_struct` (`include/linux/sched.h`, 规模可达约数百行量级).

### 4.2 Process Table

- 为快速访问各进程 PCB, OS 用表存放指向 PCB 的指针
- Linux「进程表」常以哈希表等形式组织
- 进程 **完全** 终止后: 从表中移除并释放全部资源

### 4.3 Process List Structures

- OS 维护 **ready list** 与 **blocked list**, 存放当前未在跑的进程引用
- **Current** 指向正在跑的 PCB
- 多核时: 可 **per core** 维护相关结构

---

## 5. 观察工具: `ps` / `pstree` (p.14–15)

### `ps`

- 列出进程信息: `ps [option]`
- 无选项时通常只显示与当前终端相关的进程
- 常用 (Linux): `-e` 全部; `-f` 完整格式; `w` 宽输出; `f` ASCII 进程树 (forest)
- 细节用 `man`

### `pstree`

- 按层次显示进程关系 (每进程有父进程)
- 例: `pstree -s PID`, `pstree -sp PID` 可看到 `systemd → sshd → … → bash → pstree`

---

## 6. 进程上的操作 (p.16)

OS 提供的基本服务包括: 创建 / 销毁 / 挂起 / 恢复 / 改优先级 / 等待子进程 / 查状态 / **进程间通信 (IPC, Interprocess Communication)** 等.

---

## 7. 创建进程 (p.17–19)

### 7.1 父子与进程树

- 某进程 **派生 (spawn)** 新进程: 创建者称 **父进程 (parent)**, 新生称 **子进程 (child)**
- 子进程还可再创建 → **进程树 (tree of processes)**
- 现代 OS 典型行为: 父进程终止后, **子进程通常可继续独立运行** (不随之强制全部结束)

### 7.2 创建时 OS 做什么

1. 为进程分配内存 (含 PCB 空间)
2. 初始化 PCB: 分配唯一 PID; 保存 PID / 父 PID; 设置合适的 PC 与栈指针
3. 创建其他结构 (内存、文件、记账等)
4. 将状态设为 **Ready** 并放入 Ready 队列

### 7.3 API

| 系统 | API | 含义 |
|---|---|---|
| Unix | `fork()` | 复制调用进程以创建新进程 |
| Unix | `exec` 族 | 用新程序映像替换当前程序映像 |
| Windows | `CreateProcess()` | 创建新进程及其主线程并加载程序; 类似 `fork` + `exec` |

---

## 8. 终止与 Zombie (p.20–21)

### 8.1 终止方式

- **自愿**: 执行最后语句后请求删除自身 — `exit()` 或从 `main` return
- **非自愿**: 父进程发终止信号; 或各类错误/故障导致终止
- 子进程把 **终止状态 (termination status)** 返回给父进程; 父进程用 `wait()` / `wait4()` / `waitid()` / `waitpid()` 取得
- 随后 OS 释放该进程资源

### 8.2 Zombie Process (UNIX)

- 处于 terminated 状态时常称 **僵尸进程 (zombie process)**
- 退出后 OS **仍保留 PCB**, 以便父进程必要时取得: exit status、资源用量等
- 父进程调用 `waitpid()` 等后, OS 才彻底移除 zombie 子进程

---

## 9. 挂起 (Suspend) (p.22–24)

- **挂起**: 暂时停用进程, 使其不再被处理器调度考虑
- 原因示例: 用户请求; 父进程请求; OS 可能挂起某 **blocked** 进程以腾出内存给 ready 进程
- 挂起进程须由另一进程 **恢复 (resume)**

**Suspend vs Blocked**:

| | Blocked | Suspend |
|---|---|---|
| 触发 | 多由进程 **内部活动** (如自己发起的 I/O 等待) | 多来自 **外部** |
| 含义 | 等事件才能继续 | 暂不参与调度 (可能为换出等) |

p.23–24 为状态转换图 (文字极少); 复习时对照「ready/running/blocked + suspended 变体」图示.

---

## 10. 信号 (Signals) (p.25–29)

UNIX 中用 **信号 (signal)** 通知进程某事件已发生; 有时称 **软件中断 (software interrupt)**.

相关系统调用示例: `kill()`, `signal()`, `sigaction()`, `raise()`, `pause()`, `sigsuspend()` 等.

每个信号有编号/符号名, 例如:

- `SIGINT` (=2): Ctrl-c
- `SIGCHLD` (=17): 子进程结束或被终止

### 10.1 同步 vs 异步

| 类型 | 含义 | 例子 |
|---|---|---|
| **同步信号 (synchronous signal)** | 由当前运行进程的当前指令触发, OS 立即投递给该进程 | 非法内存访问、除零 → 如 `SIGSEGV` |
| **异步信号 (asynchronous signal)** | 由外部事件产生, 到达时刻相对目标进程不可预测 | timer alarm; 父进程 `kill()` 杀子进程 |

同步例子链路 (p.26): 解引用 NULL → 内存保护异常 → 陷入 OS 中断处理 → 识别原因 → 投递 `SIGSEGV`.

异步例子 (p.27): 进程 X 执行 `kill(Y, SIGKILL)` → 切内核态 → 向 Y 投递 `SIGKILL`.

### 10.2 进程对信号的处置

进程可决定: **捕获 (catch)** / **忽略 (ignore)** / **屏蔽 (mask)**.

- **捕获**: 预先指定处理例程 (**signal handler**); 收到该信号时 OS 调用之 (`signal` / `sigaction`)
- **忽略**: 告知 OS 不处理该信号
- **屏蔽 (mask)**: 指示 OS 暂时不投递该类型信号, 直到清除 mask

注意: slides 在「Catching」条目旁另写了一句 “Using OS's default action”; 按标准 UNIX 语义, **Default / Ignore / Catch** 三者并列更清晰 — **默认动作** 与 **自定义 handler 捕获** 不同. 复习以「可设 handler / 可忽略 / 可 mask」为准.

**例外**: `SIGKILL` 与 `SIGSTOP` **不能** 被捕获、阻塞或忽略.

### 10.3 Handler 向量与继承 (p.29)

- PCB 含指向 **信号处理器向量** 的指针 (按信号编号逻辑排序); 每项对应一 handler
- 子进程 **继承** 父进程的设置
- 若随后 `exec…()` 加载新程序映像: 曾设自定义 handler 的信号会 **重置为默认**

---

## 11. Summary (p.30)

1. 为管理控制运行中进程, OS 需机制跟踪其当前状态.
2. 关键数据结构: PCB、进程表与各类列表.
3. OS 提供一组进程操作 API.
4. Unix **信号** 支持用户态进程间交互; 内核也用信号通知系统事件.
