# Programming Assignment One — 解答 (3230yash)

- **来源**: `assignment/PA01 programming assignment 1.pdf`
- **Due**: 2026-10-16 10:29; 15 pts
- **提交名**: `3230yash_{UID}.c` (可 zip/tgz 上传 Moodle)
- **平台**: 必须在 **workbench2.cs.hku.hk** 用 `gcc` 通过 (经 HKUVPN)
- **对照**: Tutorial 2 (`pipe`/`dup2`/`waitid`/`/proc`); Mini-lab 2 (signal)
- **说明**: **中文 = 说明** (设计/验收/易错); **English = Answer** (规格要点, 伪代码, 与题面一致的英文原文). 多实现并列. 本文不替代你自己在 workbench2 上的完整 `.c` 交稿.

---

## 0. 文首必须写的注释

**说明**: 缺文档扣 1 分. 行内注释要能让人跟住 `fork`/`pipe`/`wait` 路径.

**Answer** (file header comment):

```c
/*
 * Name: ...
 * UID: ...
 * Platform: workbench2.cs.hku.hk (develop on WSL2/Ubuntu Docker, final test on workbench2)
 * Completed: process exec / PATH; pipes (<=4); SIGINT; watch; exit; no zombies
 */
```

---

## 1. 总体结构

**说明**: 主循环: 打提示符 → 读行 (EINTR 重试) → 分派 exit / watch / pipeline / simple. 每条子进程都要 `wait*` 收尸.

**Answer**:

```text
install SIGINT handler for shell (do not exit)
loop forever:
  print "## 3230yash >> "
  read line (retry on EINTR)
  if empty: continue
  tokenize (<=30 tokens, line <=1024)
  if parse error (pipe): print exact message; continue
  if first token == "exit":
    handle_exit(rest); continue or terminate
  if first token == "watch":
    handle_watch(rest); continue
  if has '|':
    run_pipeline(commands)
  else:
    run_simple(argv)
  // every child reaped; no zombies
```

> Exact prompt (including the trailing space):
>
> ```text
> ## 3230yash >> 
> ```

---

## 2. 进程创建与执行 (4.5)

### 2.1 查找可执行文件

**说明**: `/` 与 `./` 直接 exec; 否则走 PATH. `execvp` 最省事; 自己拼 PATH 也合格.

**Answer**:

| Input form | Behavior |
|---|---|
| starts with `/` | absolute path → `execv` directly |
| starts with `./` | relative path → `execv` directly |
| otherwise | search directories in `$PATH` |

> **Answer A (recommended)**: `execvp(argv[0], argv)` — library PATH search; absolute/relative paths also work.
>
> **Answer B**: `getenv("PATH")`, split on `:`, for each dir `snprintf(buf, …, "%s/%s", dir, cmd)`, then `execv(buf, argv)`.
>
> Both are acceptable. On failure, use `errno` to choose the exact error string.

### 2.2 错误字符串 (逐字)

**说明**: `%s` 用用户输入的那个命令词 (如 `simp`, `/bin/simp`, `./start.sh`).

**Answer**:

| Case | Print exactly |
|---|---|
| not found | `3230yash: '%s': No such file or directory\n` |
| permission / not executable | `3230yash: '%s': Permission denied\n` |

### 2.3 单命令流程

**说明**: 父必须 `wait*` → 无僵尸. 子被信号杀时打印「程序名: 信号名」.

**Answer**:

```text
pid = fork()
if child:
  signal(SIGINT, SIG_DFL)   // recommended: child can die on Ctrl-C
  execvp(...)
  // on exec failure: print the fixed messages above; _exit(127)
if parent:
  waitpid(pid, &status, 0)   // or waitid
  if WIFSIGNALED(status):
    print "%s: %s\n"  (basename, Interrupt/Killed/...)
```

> Signal-termination message: program name + signal type, e.g. `loopf: Interrupt`, `forever: Killed`.
>
> **Answer A**: `strsignal(WTERMSIG(status))` (platform English names; commonly `Interrupt` / `Killed`).
>
> **Answer B**: map `SIGINT→Interrupt`, `SIGKILL→Killed`; others via `strsignal` or `Signal %d`.
>
> Parent must `wait*` → **no zombies**.

### 2.4 多参数

**说明**: 空白分 token; `argv` 以 `NULL` 结尾; 总 token ≤30.

**Answer**:

> Tokenize on whitespace; pass a `NULL`-terminated `argv` to `exec*`. Any argument count is fine as long as the total token count is ≤30.

---

## 3. 管道 `|` (4)

### 3.1 合法约束

**说明**: 最多 4 个 `|` (5 段命令); 不能首尾 `|`; 不能空命令.

**Answer**:

> - At most **4** `|` → at most **5** commands
> - `|` must not be at the start or end of the line
> - No empty commands (consecutive `|` or `| |`)

### 3.2 非法文案 (逐字)

**Answer**:

| Illegal case | Print exactly |
|---|---|
| `|` at start or end | `3230yash: Incorrect pipe sequence` |
| consecutive `|` with no command | `3230yash: should not have two consecutive | without in-between command` |

### 3.3 连接方式

**说明**: 卡住常见原因是父或子没关写端 → `read` 永不 EOF. 两种 pipe 数组写法都合格.

**Answer**:

> For \(N\) commands use \(N-1\) `pipe()`s. For child \(i\) (0-based):
>
> - if \(i>0\): `dup2(pipes[i-1][0], STDIN_FILENO)`
> - if \(i<N-1\): `dup2(pipes[i][1], STDOUT_FILENO)`
> - **close all** pipe fds (including unused ends), then `exec`
>
> Parent: after all forks, **close all pipe fds**, then `wait*` **N** times.
>
> **Answer A**: array `int pipes[4][2]`.
>
> **Answer B**: chain creation, keep only fds linking adjacent commands (still close thoroughly).
>
> Both are acceptable. A common hang is leaving a write end open so `read` never sees EOF.

### 3.4 伪代码

**Answer**:

```text
split line by '|' into cmd[0..n-1]
validate pipes
for i in 0..n-2: pipe(p[i])
for i in 0..n-1:
  if fork()==0:
    if i>0: dup2(p[i-1][0], 0)
    if i<n-1: dup2(p[i][1], 1)
    close_all_pipe_fds()
    exec_command(cmd[i])
    _exit(127)
close_all_pipe_fds()
for i in 0..n-1: wait_one_child_and_report_signal()
```

---

## 4. SIGINT (2)

### 4.1 Shell 自身

**说明**: handler **不能** `exit`. 等输入时 Ctrl-C → 重打提示符继续 loop.

**Answer**:

> - `sigaction(SIGINT, …)`: handler must **not** `exit`.
> - While blocked in `read`/`fgets`, Ctrl-C usually makes the read return `-1`/`EINTR`.
> - Handle by optionally printing a newline, **reprinting the prompt**, clearing the current line buffer, and continuing the loop.
>
> **Answer A**: handler only sets `volatile sig_atomic_t got_sigint`; main loop checks the flag and redraws the prompt.
>
> **Answer B**: handler is a no-op or only `write(1, "\n", 1)`; main loop retries on `EINTR` and redraws the prompt.
>
> Spec example: after repeated `^C`, a new `## 3230yash >> ` still appears.

### 4.2 子进程

**说明**: 推荐子在 `exec` 前恢复 `SIG_DFL`, 否则 forever/loopf 可能杀不掉.

**Answer**:

> Do not let the shell's handler make all children ignore SIGINT unless each child explicitly resets it. **Recommended**: parent uses a custom handler or ignores; **before `exec`**, the child does `signal(SIGINT, SIG_DFL)` so `./forever` / `./loopf` respond as usual. If the parent sees a child killed by a signal, print the §2.3 message.

---

## 5. 内建 `watch` (4)

### 5.1 语法与拒绝

**说明**: `watch` 不能跟管道.

**Answer**:

> Form: `watch <cmd> [args…]`.
> If the `watch` line also contains `|`, print exactly:
>
> ```text
> 3230yash: Cannot watch a pipe sequence
> ```

### 5.2 监控流程

**说明**: 关键是「exec 前先抓一帧」需要 barrier; 然后每 500ms 抓帧; 子输出结束后再打印统计.

**Answer**:

> 1. `fork` a child; parent already knows `pid`.
> 2. **Before the child `exec`s**, parent reads one `/proc/{pid}/stat` snapshot. Sync options (all valid):
>
> **Answer A (recommended)**: pipe barrier — child `read`s one byte before `exec`; parent writes after the first snapshot.
>
> **Answer B**: child `raise(SIGSTOP)`; parent `waitpid(…, WUNTRACED)`, snapshot, then `kill(pid, SIGCONT)`.
>
> **Answer C**: parent briefly spins reading `/proc` until the file appears (weaker; race-prone).
>
> 3. Child `exec`s the target command.
> 4. Parent snapshots every **500 ms** until the child terminates.
> 5. Use non-blocking `waitid` / `waitpid(…, WNOHANG)` to detect death.
> 6. After the child's stdout finishes, parent **then** prints all collected stat lines (display after child finished producing output).

### 5.3 `/proc/{pid}/stat` 字段

**说明**: utime/stime 除以 CLK_TCK 变秒; vsize 用字节.

**Answer**:

| Output column | Typical field | Processing |
|---|---|---|
| STATE | state (field 3, e.g. `R`/`S`/`Z`) | as-is or mapped |
| CPUID | processor | integer |
| UTIME | utime | divide by `sysconf(_SC_CLK_TCK)` → **seconds**, print like `0.00` |
| STIME | stime | same |
| VSIZE | vsize | **bytes** |
| MINFLT | minflt | |
| MAJFLT | majflt | |

> Header line:
>
> ```text
> STATE CPUID UTIME STIME VSIZE     MINFLT MAJFLT
> ```
>
> Alignment should be readable for TAs; sample uses space-separated columns.

### 5.4 500ms 循环伪代码

**Answer**:

```text
snapshots = []
sync_child_before_exec()
snapshots.append(read_proc(pid))   // pre-exec / early
child starts
while true:
  sleep 500ms  (nanosleep / usleep)
  if waitid(P_PID, pid, &info, WEXITED|WNOHANG) says dead:
    snapshots.append(read_proc(pid))  // may be Z
    break
  snapshots.append(read_proc(pid))
print_all(snapshots)
```

---

## 6. 内建 `exit` (0.5)

**说明**: 仅 `argv[0]=="exit"` 且无后续参数才真正退出; `exit now` 只报错不退; `not exit` 当普通命令.

**Answer**:

| Input | Behavior |
|---|---|
| bare `exit` | free resources, print `3230yash: Terminated`, `exit(0)` |
| `exit` with other args | print `3230yash: "exit" with other arguments!!!`, do **not** exit |
| `exit` not first token (e.g. `not exit`) | **not** a builtin; treat as normal command → usually `No such file or directory` |

> Rule: after tokenize, truly exit only if `argv[0]=="exit"` and `argv[1]==NULL`.

---

## 7. 评分对照清单

**说明**: 交稿前自检用; 不必写进 `.c`.

| Pts | Item | Self-check |
|---|---|---|
| 4.5 | prompt / fork-exec / PATH / args / error strings / wait / signal msgs / loop / no zombies | |
| 4 | legal 2–5 stage pipes; both illegal messages | |
| 2 | Ctrl-C cannot kill yash; new prompt while waiting; children can be killed | |
| 4 | `watch` single cmd; reject pipe; pre+periodic+post snapshots; non-blocking `waitid` | |
| 0.5 | `exit` / `exit now` | |
| −1 | header info + comments | |

---

## 8. 提交与 GenAI

**说明**: 文件名与平台硬性要求.

**Answer**:

> - Filename: `3230yash_{UID}.c`
> - If GenAI was used: attach a report (model, prompts, marked adopted snippets)
> - Do not use academy11/21; use workbench2 only

---

## 9. 最小可运行骨架 (示意, 非完整交稿)

**说明**: 把 §2–§6 填进分支, 在 workbench2 上按题目理解验收清单逐项测.

**Answer** (skeleton):

```c
#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <errno.h>

static volatile sig_atomic_t got_sigint = 0;
static void on_sigint(int sig) { (void)sig; got_sigint = 1; }

int main(void) {
    struct sigaction sa = {0};
    sa.sa_handler = on_sigint;
    sigaction(SIGINT, &sa, NULL);

    char line[1024];
    for (;;) {
        fputs("## 3230yash >> ", stdout);
        fflush(stdout);
        if (!fgets(line, sizeof line, stdin)) {
            if (feof(stdin)) break;
            if (errno == EINTR) { clearerr(stdin); got_sigint = 0; continue; }
            break;
        }
        if (got_sigint) { got_sigint = 0; }
        /* tokenize → exit / watch / pipeline / simple */
        /* ... implement §§2–6 ... */
    }
    return 0;
}
```
