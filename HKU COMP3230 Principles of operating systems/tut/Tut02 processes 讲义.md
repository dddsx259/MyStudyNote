# Tutorial 2 — Processes: 讲义

- **来源**: `tut/Tut02 processes.pdf` (50 页)
- **课程**: COMP3230B Principles of Operating Systems
- **对齐**: `Lec/Lec04 process abstraction`; OSTEP Ch.5; Mini-lab 2/3; **PA1 3230yash**
- **短摘要**: 同目录 `Tut02 processes 总结.md`

---

## 0. 本 Tut 要解决什么

把 Tut01 的「API 三角」落到可写代码的细节, 并**逐条对齐 PA1**.

| Part | 内容 |
|---|---|
| 1 | Process 抽象 / PCB / 状态 |
| 2 | `fork` (含 COW, 多 fork 计数, gdb) |
| 3 | `exit` / `wait*` / zombie / `/proc` |
| 4 | `exec` 族与 shell 标准模式 |
| 5 | Signals & pipes (`dup2`) |
| 末 | Assignment 1 规格对照 |

---

## 1. Process Abstraction

**Process** = 运行中的程序 ≈ 地址空间 + CPU 寄存器状态 + 内核跟踪的资源 (打开文件, 信号 disposition 等).

- **PCB**: 内核侧「进程控制块」, 调度与切换时读写
- **状态**直觉: running / ready / blocked (等 I/O 或 `wait`) / zombie (已死未收) …
- 用户态工具: `ps`, `pstree` 看进程树

与 Tut01 衔接: Program 是死映像, Process 是活实例; 同一程序可有多个进程.

---

## 2. `fork()`

### 2.1 接口

```c
#include <unistd.h>
pid_t fork(void);
```

| 返回值 | 含义 |
|---|---|
| `< 0` | 失败 (`errno`) |
| `== 0` | 当前是**子进程** |
| `> 0` | 当前是**父进程**, 值为子 PID |

- 调用**一次**, 返回**两次** (父子各一次)
- 子从 `fork` **之后**继续执行, **不是**从 `main` 重来

### 2.2 复制了什么 / 什么不同

大致复制: 代码, 数据, 堆, 栈, 打开的文件描述符表项等.

通常不同: PID, PPID, `fork` 的返回值; 之后各自独立修改内存与 fd.

**调度非确定性**: 父子谁先跑不保证. 需要「父等子做完」→ 用 `wait*`.

**孤儿 (orphan)**: 父先退出, 子仍在 → 由 init/systemd (PID 1) 收养, `getppid()` 常为 1.

### 2.3 多 `fork` 计数

连续 \(n\) 次无退出的 `fork()` (且每条路径都继续), 进程总数 \(2^n\).

例: 三次 `fork()` → \(2^3 = 8\) 个进程.

### 2.4 小练习 (务必手算)

**Q1**

```c
int c = 100;
fork();
if (c == 100) printf("X");
```

→ **两个 X**: 父子各有一份 `c==100`.

**Q2**

```c
pid_t pid = fork();
if (pid == 0) printf("X");
printf("Y");
```

→ **1 个 X, 2 个 Y**: 只有子打印 X; 父子都打印 Y.

### 2.5 Copy-on-Write (COW)

现代 OS 的 `fork` 不会立刻物理拷贝全部页:

1. 父子先**共享**物理页, 标只读
2. 任一方**首次写入**某页 → page fault → 内核拷贝该页再写

后果 (考试常考):

- 虚拟地址 `&x` 在父子中可以**看起来相同**
- 写入后值可以**不同** (已不共享该页)

好处: `fork` 后立刻 `exec` 时, 多数页从未被写, **几乎不用真拷贝** → fork-then-exec 便宜.

### 2.6 gdb 跟 fork

- 默认常跟父进程, 子被 detach
- `set follow-fork-mode child` — 跟子
- `detach-on-fork off` — 可同时调试父子 (视 gdb 版本)

---

## 3. `exit` / `wait*` / zombie / `/proc`

### 3.1 子进程如何结束

- 正常: `exit(status)` / `main` 里 `return`
- 异常: 被信号杀死 (如未处理的 `SIGINT`, `SIGSEGV`)

### 3.2 Zombie

子已终止, 但父**尚未** `wait*` → 内核保留一份「退出状态」在 PCB 里 → **zombie**.

- 僵尸几乎不占用户内存, 但占 PID / PCB 槽
- 父必须 `wait` / `waitpid` / `waitid` **收尸**
- PA1 要求: shell **不能**留下僵尸

### 3.3 `wait` 族

```c
#include <sys/wait.h>
pid_t wait(int *wstatus);
pid_t waitpid(pid_t pid, int *wstatus, int options);
int waitid(idtype_t idtype, id_t id, siginfo_t *infop, int options);
```

常用宏解码 `wstatus`:

| 宏 | 含义 |
|---|---|
| `WIFEXITED` | 正常 exit |
| `WEXITSTATUS` | 退出码 |
| `WIFSIGNALED` | 被信号杀 |
| `WTERMSIG` | 信号编号 |

**`WNOHANG`**: 非阻塞. 子未结束则立即返回 0. **PA1 `watch`** 轮询时要用非阻塞等待 (题面常用 `waitid`).

### 3.4 `/proc/{pid}/stat`

Linux 把 PCB 信息以文本暴露在 `/proc`.  
`/proc/{pid}/stat` 含状态字母, 时间, 虚拟内存大小, 缺页计数等字段.

**PA1 `watch`**: 在子跑命令期间反复读该文件做快照 (启动前一帧 + 每 500ms + 结束后), 再打印. 数据源就是这里.

---

## 4. `exec` 族

### 4.1 语义

`exec*` **替换**当前进程的程序映像:

- 成功: **不返回** (新程序从它的入口开始)
- 失败: 返回 -1, 旧映像仍在, 查 `errno`
- PID 通常不变; 多数打开的 fd 默认保留 (除非 close-on-exec)

常用变体直觉:

- `execl` / `execv`: 路径直接给
- `execlp` / `execvp`: 按 **`$PATH`** 搜索命令名

### 4.2 Shell 标准模式 (PA1 核心)

```text
父 (shell)
  |  fork
  +----> 子: [gap: 改 fd / 环境 / 信号] --> exec(目标程序)
  |                                            |
  +---- wait* <--------------------------------+ 子 exit 或被信号杀
```

- **gap**: 管道时在这里 `dup2`; 也可改工作目录等
- 父在 `wait*` 之前不应假设子已跑完

### 4.3 路径查找 (对齐 PA1)

1. 命令以 `/` 开头 → 绝对路径
2. 以 `./` 开头 → 相对路径
3. 否则在 `$PATH` 各目录找

失败文案必须与题面**逐字**一致 (见 `assignment/PA01 … 题目理解.md`).

---

## 5. Signals & Pipes

### 5.1 Signals (对 PA1)

- `kill(pid, sig)`, `sigaction` 注册 handler
- disposition: **`fork` 后子继承**; **`exec` 成功后, 自定义 handler 会回到默认** (除非忽略等特殊情况 — 写 PA1 时以题面与 man 为准)
- PA1 要求:
  - **shell 自身**不被 Ctrl-C 干掉 (忽略或自处理 `SIGINT`, 回到提示符)
  - **子进程**各自处理; 若子因信号终止, shell 打印原因 (信号名/编号, 按规格)

### 5.2 Pipes

```c
int fd[2];
pipe(fd);            // fd[0] 读端, fd[1] 写端
dup2(oldfd, newfd);  // 让 newfd 成为 oldfd 的复制 (常用于绑到 0/1)
```

两命令 `cmd1 | cmd2`:

- 左: stdout → pipe 写端
- 右: stdin ← pipe 读端
- **双方及父进程必须关掉所有不再用的 pipe 端**, 否则读端可能永远等不到 EOF → 死锁/挂死

\(N\) 个命令 (\(N-1\) 个 `|`):

- 建 \(N-1\) 条 pipe
- 子 \(i\): 把 stdin/stdout `dup2` 到正确端, **然后 close 全部 pipe fd**, 再 `exec`
- 父: close 全部 pipe fd, 再 `wait` \(N\) 次 (或等价)

非法序列 (PA1): 行首/行尾 `|`, 连续 `|` — 打印题面规定错误串, 不 exec.

---

## 6. Summary 口诀

```text
shell --fork--> child --[gap]--> exec --> new program
                     exit/signal --> zombie --wait*--> 收尸
signals: 控制与通知;  pipes: 数据流;  /proc: PCB 文本视图
```

---

## 7. Assignment 1 (3230yash) 对照表

| 需求 | 本 Tut 位置 | 分 (题面) |
|---|---|---|
| 提示符; fork/exec; PATH; wait; 报杀子信号; 无僵尸 | Parts 2–4 | 4.5 |
| 管道 `\|` (最多 5 命令) | Part 5 pipes | 4 |
| SIGINT 行为 | Part 5 signals | 2 |
| `watch` + `/proc` + 非阻塞 `waitid` | Part 3 | 4 |
| 内建 `exit` | 规格 | 0.5 |

Due / 提交 / 错误字符串: `assignment/PA01 programming assignment 1 题目理解.md`.

---

## 8. Cheat sheet (头文件)

| 头文件 | 典型调用 |
|---|---|
| `unistd.h` | `fork`, `getpid`, `exec*`, `pipe`, `dup2`, `close` |
| `sys/wait.h` | `wait`, `waitpid`, `waitid`, `WIF*` |
| `signal.h` | `kill`, `sigaction`, `SIGINT` … |
| `fcntl.h` | 有时配合 fd 标志 |

man: `man 2 fork`, `man 2 waitid`, `man 7 signal`, `man 5 proc`.

---

## 9. 建议练习顺序 (做 PA1 前)

1. 手写: 单次 fork + 父子打印 PID + 父 wait
2. 手写: fork + execvp(`ls`) + wait
3. 手写: 两进程 pipe + dup2 (先不管 shell 解析)
4. 对照 Mini-lab 2/3 与本题面错误串, 再搭 3230yash 主循环
