# OSTEP Ch.5 Interlude: Process API — 阅读讲义

- **来源**: `Lec/OSTEP 5 process api.pdf` (15 页, 全覆盖; 原名 `cpu-api.pdf`)
- **课程**: COMP3230B; 对应课件 `Lec/Lec04 process abstraction.pdf` 的 Required Reading (共用编号 **04**)
- **原书**: Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP) Ch.5, v1.10
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-api.pdf

> 本讲是 **插曲 (interlude)**: 偏 UNIX 进程创建与控制的实用 API, 与课堂 slides 的进程抽象 (process abstraction) 互补. 术语首次标英文. **Final 必记**: `fork` 后父子变量独立, 但打印出的 **虚拟地址 (virtual address)** 可以相同 (2023 Final Q1e).

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| Crux | OS 应提供怎样的进程创建/控制接口? 要强功能, 易用, 高性能 |
| `fork()` | 几乎完整复制调用进程 → 子进程 (child); 返回值区分父子 |
| `wait()` / `waitpid()` | 父进程 (parent) 阻塞等待子进程结束; 输出可变确定性 |
| `exec()` 族 | **不**新建进程; 用新可执行映像 **替换** 当前地址空间 (address space) |
| 为何拆开 | shell 可在 `fork` 与 `exec` 之间改环境 → 重定向 (redirection), 管道 (pipe) |
| 控制 | 信号 (signal): `kill`, Ctrl-c / Ctrl-z; 用户 (user) / 超级用户 (superuser, root) |
| 工具 | `ps`, `top`, `kill` / `killall` |

---

## 1. Aside: Interludes 与本章 Crux

**Interlude** 讲更偏实践的内容 (尤其 OS API 怎么用). 本章讨论 UNIX 进程创建: 核心一对系统调用 (system call) 是 `fork()` 与 `exec()`, 加上父进程可用的 `wait()`.

### Crux: 如何创建与控制进程?

OS 应提供怎样的接口做进程创建与控制? 如何设计才能强功能, 易用, 又高性能?

- **自测**: 用一句话说明为何「只 `fork`」或「只 `exec`」都不够完成 shell 里跑一条新命令.
- **参考**: `fork` 只克隆当前程序; `exec` 只替换映像不创建新进程. shell 需要 **新进程 + 新程序**, 故两者组合; 中间还可改文件描述符 (file descriptor, fd).

---

## 2. §5.1 The `fork()` System Call — 例子 `p1.c`

### 程序要点 (Figure 5.1)

完整程序 (官方 `ostep-code/cpu-api/p1.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    printf("hello world (pid:%d)\n", (int) getpid());  // fork 前只跑一次
    int rc = fork();                                   // 创建子进程; 之后父子都从这里「返回」
    if (rc < 0) {
        // fork 失败
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // 子进程路径: fork 对子返回 0
        printf("hello, I am child (pid:%d)\n", (int) getpid());
    } else {
        // 父进程路径: rc == 子进程 PID
        printf("hello, I am parent of %d (pid:%d)\n",
               rc, (int) getpid());
    }
    return 0;
}
```

运行时典型输出 (次序 **不确定**):

```text
prompt> ./p1
hello world (pid:29146)
hello, I am parent of 29147 (pid:29146)
hello, I am child (pid:29147)
```

或子进程先打印. `hello world` **只出现一次**: 子进程 **不是** 从 `main` 重跑, 而是仿佛自己刚调用完 `fork()` 正在返回.

### `fork` 做了什么

1. OS 创建新进程, 是调用进程的 **几乎完整副本**: 自己的地址空间 (私有内存), 寄存器 (register), 程序计数器 (program counter, PC) 等.
2. 对 OS 而言, 现在像有两份 `p1` 都在从 `fork` 返回.
3. **返回值不同** (这是刻意的非完全相同):
   - **父进程**: 得到子进程的 **进程标识符 (process identifier, PID)**
   - **子进程**: 得到 `0`
   - 失败: 返回负值
4. PID 用来命名进程 (如之后停止它). `getpid()` 取本进程 PID.

### 非确定性 (non-determinism)

单 CPU 上, `fork` 之后父子都可运行; **谁先跑** 由 **CPU 调度器 (CPU scheduler)** 决定. 故 `p1.c` 输出次序不固定. 并发 (concurrency) 部分会大量见到这类非确定性.

### Exam 焦点: 变量独立 vs 虚拟地址相同 (2023 Final Q1e)

设 `fork` 前有变量 `a = A`. 之后:

- 父: `a = a - 5`, 打印 `a` 与 `&a` → 记为 $u$, $v$
- 子: `a = a + 5`, 打印 → 记为 $x$, $y$

则正确关系是:

$$
u = x - 10, \qquad v = y
$$

| 事实 | 含义 |
|---|---|
| **值独立** | 父子各有一份地址空间副本; 改 `a` 互不影响 → $u = A-5$, $x = A+5$ |
| **虚拟地址可相同** | `fork` **不改** 虚拟地址布局; `&a` 打印的是虚拟地址 → $v = y$ |
| 物理页 | 可因写时复制 (copy-on-write, COW) 映射到不同物理页; 考试看的是 `printf` 打出的虚拟地址 |

不要记成「地址也一定不同」或「值同地址同」.

### 示例 `p1.c` — `fork` 返回与次序

- **实验**: 多跑几次 `./p1`, 观察父子打印谁先.
- **讲解**: 子进程从 `fork` 返回点继续; `rc==0` vs `rc==child_pid`; 调度导致输出非确定.

### Crux 回顾: 接口要做什么?

- **自测**: `fork` 之后, 「几乎相同」体现在哪? 「刻意不同」体现在哪?
- **参考**: 相同 — 内存/寄存器/PC 等副本; 不同 — 返回值与新 PID.

---

## 3. §5.2 The `wait()` System Call — 例子 `p2.c`

有时父进程需要等子进程做完. 用 `wait()` (或更完整的 `waitpid()`). 见 Figure 5.2.

### 程序要点 (Figure 5.2)

完整程序 (官方 `ostep-code/cpu-api/p2.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("hello world (pid:%d)\n", (int) getpid());
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // 子进程
        printf("hello, I am child (pid:%d)\n", (int) getpid());
        sleep(1);                             // 故意慢一点, 仍保证父在 wait 后打印
    } else {
        // 父进程: 阻塞直到某个子进程结束
        int wc = wait(NULL);                  // 返回结束的子 PID (常见)
        printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
               rc, wc, (int) getpid());
    }
    return 0;
}
```

`wait` **阻塞 (block)** 父进程, 直到某个子进程结束; 返回时父进程解除阻塞. 典型输出变为 **确定**:

```text
prompt> ./p2
hello world (pid:29266)
hello, I am child (pid:29267)
hello, I am parent of 29267 (wc:29267) (pid:29266)
```

### 为何子进程一定先打印?

1. 若子先跑: 直接先打 `child`.
2. 若父先跑: 立刻进 `wait`, **直到子退出才返回**, 再打 `parent`.

故加了 `wait` 后, 父的打印总在子之后. (man page 有少数例外; 勿把教材绝对化表述当教条.)

`wait(NULL)` 的返回值常是结束的那个子进程 PID (与 `rc` 一致时很常见).

### 示例 `p2.c` — 用 `wait` 消非确定性

- **实验**: 对比 `p1` / `p2` 多次运行输出是否稳定.
- **讲解**: `wait` 把父子打印顺序钉死; 对应 zombie / 取终止状态 (termination status) 的课堂主题.

### 自测: `wait` vs 调度

- **问**: 没有 `wait` 时父一定后打印吗? 有 `wait` 时子一定先跑完再让父继续吗?
- **答**: 无 `wait` — 谁先打印不定. 有 `wait` — 父 **打印消息前** 一定已等过子结束; 子可能先跑完, 也可能父先跑但卡在 `wait` 里.

---

## 4. §5.3 The `exec()` System Call — 例子 `p3.c`

只想跑 **另一份程序** 时, 需要 `exec()` (Linux 上有 `execl` / `execlp` / `execle` / `execv` / `execvp` / `execvpe` 等变体; 见 man).

### 程序要点 (Figure 5.3)

完整程序 (官方 `ostep-code/cpu-api/p3.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    printf("hello world (pid:%d)\n", (int) getpid());
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // 子进程: 用 exec 把自己「变成」wc
        printf("hello, I am child (pid:%d)\n", (int) getpid());
        char *myargs[3];
        myargs[0] = strdup("wc");             // argv[0]: 程序名
        myargs[1] = strdup("p3.c");           // argv[1]: 要统计的文件
        myargs[2] = NULL;                     // argv 必须以 NULL 结尾
        execvp(myargs[0], myargs);            // 成功则不返回
        printf("this shouldn't print out");   // 仅 exec 失败才会看到
    } else {
        int wc = wait(NULL);
        printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
               rc, wc, (int) getpid());
    }
    return 0;
}
```

父仍 `wait`. 输出类似:

```text
hello world ...
hello, I am child ...
29 107 1030 p3.c    # wc 的行/词/字节统计
hello, I am parent of ...
```

### `exec` 语义 (关键)

给定可执行文件名与参数:

1. 从该文件 **加载代码与静态数据**, **覆盖** 当前代码段 (code segment) 与静态数据
2. 堆 (heap), 栈 (stack) 等也 **重新初始化**
3. OS 从新程序入口跑, 参数成为新进程的 `argv`
4. **不创建新进程** — 是把 **当前** 进程 (原 `p3`) **变换** 成另一个程序 (`wc`)
5. **成功的 `exec` 不返回**; 其后的 `printf` 正常情况看不到

`fork` 怪在「造出几乎一样的双生子」; `exec` 怪在「本人变身成别人」.

### Tip: Getting It Right (Lampson's Law)

Lampson (*Hints for Computer Systems Design*): **先做对 (Get it right)**. 抽象与简单不能替代正确. 进程创建 API 有很多设计法; `fork`+`exec` 组合简单且极强 — UNIX 设计者在这里做对了. (书中称 Lampson's Law.)

### 示例 `p3.c` — `fork` + `wait` + `exec`

- **实验**: 跑 `./p3`, 确认出现 `wc` 统计且无 "this shouldn't print out".
- **讲解**: `execvp` 成功则子进程映像已是 `wc`; PID 仍是那个 child PID, 父 `wait` 等的仍是它.

### 自测: `fork` vs `exec` vs `CreateProcess`

- **问**: 谁创建进程? 谁换程序? Windows `CreateProcess` 对应哪两步?
- **答**: `fork` 创建; `exec` 替换映像; `CreateProcess` ≈ 一步做完两者.

---

## 5. §5.4 Why? Motivating The API — 重定向与管道

### 为何接口这么怪?

拆开 `fork` 与 `exec` **对实现 UNIX shell 至关重要**: shell 可在 `fork` **之后**, `exec` **之前** 跑一段代码, 改即将运行程序的环境, 从而轻松做重定向, 管道等, **且不必改被运行的程序本身**.

Shell 本身只是用户程序 (`bash`, `zsh`, `tcsh` 等): 提示符 → 读命令 → 定位可执行文件 → `fork` → (可选改 fd) → `exec` → `wait` → 再提示.

例:

```text
prompt> wc p3.c > newfile.txt
```

### 重定向 (redirection) 怎么做

子进程在 `exec` 前:

1. `close(STDOUT_FILENO)` 关掉标准输出
2. `open("newfile.txt", ...)` — UNIX 从 **0 起** 找空闲 fd, 于是新文件往往拿到原来的 stdout 编号
3. 再 `exec` 跑 `wc`; **打开的 fd 在 `exec` 后仍保持打开** → `printf` 等对 stdout 的写进入文件而非屏幕

### 例子 `p4.c` (Figure 5.4)

完整程序 (官方 `ostep-code/cpu-api/p4.c`):

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <assert.h>
#include <sys/wait.h>

int main(int argc, char *argv[])
{
    int rc = fork();
    if (rc < 0) {
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // 子进程: 在 exec 之前改 stdout → 实现 shell 的 >
        close(STDOUT_FILENO);                 // 关掉 fd 1 (标准输出)
        open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
        // UNIX 从最小空闲号分配 fd → 新文件通常拿到原来的 1

        char *myargs[3];
        myargs[0] = strdup("wc");
        myargs[1] = strdup("p4.c");
        myargs[2] = NULL;
        execvp(myargs[0], myargs);            // wc 的输出进 p4.output, 不进屏幕
    } else {
        int wc = wait(NULL);
        assert(wc >= 0);
    }
    return 0;
}
```

运行 `./p4` 时屏幕上几乎「什么都没发生」(shell 立刻又出提示符), 但 `p4.output` 里有 `wc` 结果; `cat p4.output` 可见统计行.

### 管道 (pipe)

类似思路, 用 `pipe()`: 一进程的 stdout 接到内核里的管道 (队列), 另一进程的 stdin 接同一管道 → `grep -o foo file | wc -l` 这类命令链. **不必改 `grep`/`wc` 源码**.

(文件描述符细节在全书第三部分文件系统还会展开; 本章够用的直觉: `fork`/`exec` 分离 + fd 操作 = 强 shell 功能.)

### 示例 `p4.c` — 重定向

- **实验**: 跑 `./p4`, 对比屏幕与 `p4.output`.
- **讲解**: close stdout → open 文件占回 fd 0/1/2 中空位 → `exec` 后继承 → 这就是 `>` 的本质.

### Crux: 分离 `fork`/`exec` 的收益

- **自测**: 若只有「一步创建并加载」的 API, shell 做 `>` / `|` 会难在哪?
- **参考**: 难以在「已是新程序」之前改 fd; 要么改每个命令, 要么 OS 提供更重的特殊接口. 分离让 shell 在子进程用户态改环境即可.

---

## 6. §5.5 Process Control And Users — 信号与用户

除 `fork` / `exec` / `wait` 外还有大量接口. 例: `kill()` 向进程发 **信号**, 可暂停, 终止等.

| 按键 / 动作 | 典型信号 | 效果直觉 |
|---|---|---|
| Ctrl-c | `SIGINT` | 打断, 常导致终止 |
| Ctrl-z | `SIGTSTP` | 暂停; 之后可用 shell 的 `fg` 等恢复 |

信号子系统可把外部事件交给进程; 进程可用 `signal()` 等 **捕获 (catch)** 信号, 暂停正常执行去跑处理代码. 细节见 Stevens & Rago [SR05].

### 谁能发信号?

多用户系统上, 若任意人可给任意进程发 `SIGINT`, 安全与可用性会垮. 故有 **用户** 概念: 认证登录后启动进程, **通常只能控制自己的进程**. OS 在用户间分配 CPU / 内存 / 磁盘等资源.

### Aside: RTFM

书中多次说「读 man pages」. man 是 Web 之前的 UNIX 文档传统. 系统程序员成长路径之一: 读 shell man, 读你调用的每个系统调用的返回值与错误. 同事回你 **RTFM** = Read The Man pages (中间那个 F 是语气调料).

---

## 7. §5.6 Useful Tools

| 工具 | 用途 |
|---|---|
| `ps` | 看当前有哪些进程 (多读 flag) |
| `top` | 动态看谁吃 CPU/资源 (常自嘲自己最吃资源) |
| `kill` / `killall` | 发信号; 小心别杀了窗口管理器 |
| CPU meter 等 | 一眼看负载 (书中提 MenuMeters 等) |

### Aside: Superuser (root)

需要能管理整机的特殊用户: 杀任意进程, 跑 `shutdown` 等 → **超级用户 / root**. 「能力越大责任越大」. 日常宜普通用户; 真要 root 时格外小心.

---

## 8. §5.7 Summary

- 已介绍 UNIX 进程创建核心: `fork`, `exec`, `wait` — 仍只是皮毛; 深入读 [SR05] 的 Process Control / Relationships / Signals.
- 并非人人热爱 `fork`: Baumann 等 HotOS'19 论文 [*A fork() in the road*](https://www.microsoft.com/en-us/research/publication/a-fork-in-the-road/) 批评 `fork` 并主张 `spawn()` 等更简 API. 书也提醒: 作者有偏好, 宜对照对立观点.

### Aside: Key Process API Terms (术语清单)

- 进程名多为数字 **PID**
- **`fork`**: 父造几乎相同的子
- **`wait`**: 父等子结束
- **`exec` 族**: 子摆脱与父相似, 跑全新程序
- **Shell**: 常用 `fork`+`wait`+`exec`; 分离使能重定向, 管道等
- **信号**: 停 / 续 / 杀等进程控制
- **用户**: 通常只能控自己的进程
- **Superuser**: 可控全部; 少用, 慎用

---

## 9. Homework 节 (meta)

### Simulation (`fork.py`)

用进程树仿真器练 `fork`/`exit` 关系. 题意摘要:

1. `./fork.py -s 10`, 用 `-c` 核对预测; 换 seed / `-a` 加动作
2. `-f` 调 `fork_percentage` (0.1–0.9) + 大 `-a`, 看最终树形态
3. `-t` 看树反推动作
4. 孤儿 (orphan): `./fork.py -A a+b,b+c,c+d,c+e,c-`; 对比 `-R` (再读系统上孤儿如何被 init/systemd 收养)
5. `-F` 只填最终树
6. `-t -F` 由最终树反推动作 — 何时唯一确定, 何时不唯一

### Coding (真实机)

书中建议亲手写的练习方向 (与 COMP3230 Lab/PA 衔接):

1. `fork` 前后改变量 `x` — **值独立** (对照 Final Q1e 的地址问题可加打 `&x`)
2. `open` 后再 `fork` — 父子是否共享同一 fd? 并发写文件怎样?
3. 子打 `hello`, 父打 `goodbye`, **尽量保证子先打印且不用 `wait`**
4. `fork` 后试遍 `exec*` 变体跑 `/bin/ls` — 为何这么多变体?
5. 父用 `wait`; 返回值? 子里调 `wait` 会怎样?
6. 改用 `waitpid` — 何时更有用 (多子进程)?
7. 子 `close(STDOUT_FILENO)` 后再 `printf`?
8. 两子进程 + `pipe()`, 把一个的 stdout 接到另一个的 stdin

### Aside: Coding Homeworks

小练习跑在真机上熟悉 API; 书鼓励多写代码. (理论课也好, 但系统感来自动手.)

---

## 与课堂 `Lec04 process abstraction` 对照

| OSTEP Ch.5 | 课堂 slides |
|---|---|
| `fork` 复制地址空间, 返回值区分父子 | Unix 创建: `fork` + `exec`; 自测「为何拆两步」 |
| 变量副本独立 + 虚拟地址可同 | Final Q1e 同考点; 地址空间隔离直觉 |
| `wait` / zombie 取状态 | terminated/zombie 直到父 `wait*` |
| `exec` 替换映像 | `exec` 族; 与 Windows `CreateProcess` 对比 |
| 重定向 / `pipe` / 保留 fd | shell 管道, 后台作业; Lab process |
| 信号, 用户, root | slides 信号节 (`SIGKILL`/`SIGSTOP` 等) |
| `ps` / `top` | `ps`, `pstree` 工具页 |

---

## Final 速记卡 (本章)

1. **`fork`**: 子 ≈ 父副本; 父得 child PID, 子得 `0`; 输出次序默认可交错.
2. **值 vs 地址**: 父子改同一变量名 → **值独立**; `&var` 的 **虚拟地址可相同** (2023 Q1e: $u=x-10$, $v=y$).
3. **`wait`**: 父阻塞到子结束 → 打印顺序可确定; 回收终止状态 / 清 zombie.
4. **`exec`**: 变身, 不新建 PID; 成功不返回.
5. **Redirect / pipe**: `fork` 后、`exec` 前改 fd (`close`+`open` / `pipe`); fd 跨 `exec` 保持.
