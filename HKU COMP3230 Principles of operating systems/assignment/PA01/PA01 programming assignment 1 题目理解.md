# Programming Assignment One — 题目理解 (3230yash)

- **来源**: `assignment/PA01 programming assignment 1.pdf`
- **Due**: 2026-10-16 10:29 am
- **分值**: 15 points
- **版本**: 1.0
- **程序名**: `3230yash` / 提交 `3230yash_{UID}.c`
- **平台**: 必须在 **workbench2.cs.hku.hk** 可编译运行 (经 HKUVPN); 推荐本地 WSL2/Ubuntu Docker 开发后再上传
- **相关**: Tutorial 2 (pipe/`dup`/`waitid`/`/proc`); Mini-lab 2 (signal)

---

## 目标一句话

实现交互 shell **3230yash**: 解析命令行 → `fork`/`exec` 跑外部程序; 支持管道 `|`; 内建 `exit` / `watch`; 自身忽略 Ctrl-C 不被杀; 子进程被信号杀死时打印原因.

---

## 功能清单与评分对齐

| 模块 | 分 | 必须做到 |
|---|---|---|
| 进程创建与执行 | 4.5 | 提示符; 新进程执行; 绝对/`./`/`$PATH` 查找; 多参数; 错误信息; wait 后再下一提示符; 报告杀子信号; 循环多命令; **无僵尸** |
| 管道 `\|` | 4 | ≤4 个管道 (5 命令); 参数任意; 非法序列报错文案 |
| SIGINT | 2 | yash 不被 Ctrl-C 终止; 等输入时 Ctrl-C → 新提示符; 子进程各自处理 |
| `watch` | 4 | 监控单命令 (非管道); `/proc/{pid}/stat`; 启动前+每 500ms+结束后快照; 非阻塞 `waitid`; 结束后再打印 |
| `exit` | 0.5 | 仅单独 `exit` 退出并打印 `3230yash: Terminated`; 带参拒绝 |
| 文档 | −1 若缺 | 文首姓名学号平台完成度; 行内注释 |

---

## 提示符与输入限制

- 提示符精确: `## 3230yash >> `
- 一行 ≤1024 字符; ≤30 个字符串 (含 `|`)
- 跑完子进程 (或管道中全部) 再显示下一提示符

---

## 外部命令查找

1. 以 `/` 开头 → 绝对路径
2. 以 `./` 开头 → 相对路径
3. 否则在 `$PATH` 各目录查找

失败示例文案须一致:

- `3230yash: 'simp': No such file or directory`
- `3230yash: '/bin/simp': No such file or directory`
- `3230yash: './start.sh': Permission denied`

---

## 管道

- `cmd1 | cmd2 | …` (最多 5 个命令): 前命令 stdout → 后命令 stdin (`pipe` + `dup2`)
- 非法:
  - `|` 在行首/行尾 → `3230yash: Incorrect pipe sequence`
  - 连续 `|` → `3230yash: should not have two consecutive | without in-between command`
- Tutorial 2: N 命令用 N−1 个 pipe; 子进程关掉所有不用的 pipe fd 再 `exec`

---

## 内建 `exit`

- 单独 `exit` → 释放资源, 打印 `3230yash: Terminated`, 退出
- `exit now` → `3230yash: "exit" with other arguments!!!`, 不退出
- `not exit` → 当普通命令查找 (会失败报 No such file)

---

## 内建 `watch`

- 形式: `watch <cmd> [args…]` — **不能** 监控管道 (`watch a | b` → `3230yash: Cannot watch a pipe sequence`)
- 流程:
  1. `fork` 出子进程后, **exec 前** 父进程已能读到子 PID, 先抓一帧 `/proc/pid/stat`
  2. 子 `exec` 跑命令
  3. 父每 **500 ms** 再抓一帧, 直到子终止 (非阻塞 `waitid`)
  4. 子输出结束后, 父打印所有快照行

列: `STATE CPUID UTIME STIME VSIZE MINFLT MAJFLT` (含义见题面; UTIME/STIME 为秒).

---

## SIGINT

- **3230yash**: 注册 handler, **不退出**; 在 `readline`/等待输入时收到 → 打印新提示符
- **子进程**: 默认或程序自定义; 若因信号终止, yash 打印如 `loopf: Interrupt` / `forever: Killed` (`strsignal` / 题面约定名)
- 参考 Mini-lab 2

---

## 实现建议骨架

```text
loop:
  print prompt
  read line / handle EINTR from SIGINT
  parse tokens; detect builtins / pipes
  if exit: ...
  if watch: fork+monitor loop with waitid WNOHANG; parent reads /proc
  else if pipes: create pipes; fork N children; dup2; exec; parent close+wait all
  else: fork; child exec; parent wait*; if signaled print message
```

- 用 `execvp` / 自己搜 PATH + `execv`
- 每个 `fork` 路径注意 **关闭多余 fd**, 避免管道卡住
- 所有子进程都要 `wait*` 收尸

---

## 提交

- Moodle; 文件名 `3230yash_{UID}.c`; 可 zip/tgz
- GenAI 允许但须附报告 (模型, prompt, 采用片段)
- 抄袭严查; 可能要求口述代码

---

## 验收自检清单

- [ ] workbench2 上 `gcc` 无错误
- [ ] 提示符与错误字符串与题面 **逐字** 一致
- [ ] 单命令 / 多参数 / PATH
- [ ] 2～5 段管道 + 非法管道
- [ ] Ctrl-C 杀不掉 shell; 能杀/不杀子进程两种表现
- [ ] `watch ./add` 有多行统计; `watch a | b` 拒绝
- [ ] `exit` / `exit now`
- [ ] `ps` 无残留 zombie
