# Tutorial 2 — Processes 总结

- **来源**: `tut/Tut02 processes.pdf` (50 页)
- **详细讲义**: [`Tut02 processes 讲义.md`](Tut02%20processes%20讲义.md)
- **主题**: 进程抽象 → `fork` / `exit`/`wait` → `exec` → signals & pipes → **PA1 3230yash 规格对齐**

---

## 结构

| Part | 内容 |
|---|---|
| 1 | Process abstraction / PCB / 状态 |
| 2 | `fork()` (含 COW, 多 fork 计数, gdb) |
| 3 | `exit` & `wait*` / zombie / `/proc` |
| 4 | `exec` 族与 fork–gap–exec–wait |
| 5 | Signals & pipes (`dup2`) |
| 末 | Assignment 1 逐条对照 |

---

## Part 1 — Process Abstraction

- Process = 运行中程序 = 地址空间 + 寄存器 + 资源; PCB 跟踪; 调度器在状态间搬迁
- 工具: `ps`, 进程树直觉

---

## Part 2 — `fork()`

```c
pid_t fork(void);  // <0 失败; ==0 子; >0 父(值为子 PID)
```

- 调用一次, **返回两次**; 子从 `fork` 后继续, 不是从 `main`
- 复制: 代码/数据/堆/栈/打开 fd 等; PID/PPID/返回值不同
- **非确定性**: 谁先跑由调度器决定; 需要顺序用 `wait`
- **孤儿 (orphan)**: 父先退出 → 子被 init/systemd (PID 1) 收养 (`getppid()==1`)
- 三次 `fork()` → $2^3=8$ 进程

### 小练习解答

**Q1**: `c=100; fork(); if(c==100) print X` → **两个 X** (父子各一份 `c`).

**Q2**: `pid=fork(); if(pid==0) print X; print Y` → **1 个 X, 2 个 Y**.

### Copy-on-Write (COW)

- 页先共享只读; 首次写 → fault → 拷贝该页
- 故 `&x` 虚拟地址可相同而值不同 (Final 常考)
- 使 fork-then-exec 廉价

### gdb

- 默认跟父、detach 子; `set follow-fork-mode child`; `detach-on-fork off` 可双持

---

## Part 3 — `exit` / `wait*` / `/proc`

- 子 `exit` 或被信号杀 → 若父未 wait → **zombie** (PCB 留退出状态)
- `wait` / `waitpid` / `waitid` 收尸; 用 `WIFEXITED` / `WIFSIGNALED` / `WTERMSIG` 解码
- `WNOHANG`: 非阻塞 (PA1 `watch` 需要)
- `/proc/{pid}/stat`: PCB 的文本视图 (STATE, 时间, VSIZE, 缺页计数等) — **PA1 watch 数据源**

---

## Part 4 — `exec`

- `exec*` **替换** 当前映像, PID 与多数 fd 保留; 成功不返回
- Shell 模式: `fork` → (中间改 fd/环境) → `exec` → 父 `wait`
- PATH 查找: `execvp` 等

---

## Part 5 — Signals & Pipes

### Signals

- `kill` / `sigaction`; disposition: `fork` 继承, **`exec` 后自定义 handler 复位默认**
- PA1: shell 忽略/自处理 SIGINT; 子按自己逻辑; 若子被信号终止则打印名字+信号

### Pipes

```c
pipe(fd);           // fd[0] read, fd[1] write
dup2(oldfd, newfd); // 重定向
```

- 两命令: 左写端→右读端; **关掉所有不用的 pipe 端**, 否则 EOF 不来、可能死锁
- N 命令: N−1 个 pipe; 子 i 接好 stdin/stdout 后 close 全部 pipe fd 再 exec; 父 close 全部再 wait×N

---

## Summary 口诀

```text
shell --fork--> child --[gap]--> exec --> new program
                     exit/signal --> zombie --wait*--> 收尸
signals: 控制; pipes: 数据; /proc: PCB 文本
```

---

## Assignment 1 (3230yash) 对照

| 需求 | Tut 位置 | 分 |
|---|---|---|
| 跑命令; wait; 报信号 | Parts 2–4 | 4.5 |
| 路径 / `./` / `$PATH` | exec 族 | (含上) |
| 管道 `\|` | Part 5 pipes | 4 |
| SIGINT | Part 5 signals | 2 |
| `watch` + `/proc` + `waitid` | Part 3 | 4 |
| `exit` 内建 | — | 0.5 |
| 无僵尸 | Part 3 | (含上) |

Due / 提交细节见 `assignment/PA01 programming assignment 1 题目理解.md`. 错误字符串必须与规格 **逐字** 一致.

---

## Cheat sheet (tut 末)

| 头文件 | 调用 |
|---|---|
| `unistd.h` | fork, getpid, exec*, pipe, dup2, … |
| `sys/wait.h` | wait, waitpid, waitid, WIF* |
| `signal.h` | kill, sigaction, … |
| `sys/resource.h` | rusage |
| man | `man 2 fork`, `waitid`, `man 7 signal`, `man 5 proc` |
