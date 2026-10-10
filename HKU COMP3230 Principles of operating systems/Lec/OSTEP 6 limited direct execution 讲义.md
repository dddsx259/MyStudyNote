# OSTEP Ch.6 Mechanism: Limited Direct Execution: 阅读讲义

- **来源**: `Lec/OSTEP 6 limited direct execution.pdf` (16 页, 全覆盖; 原名 `cpu-mechanisms.pdf`)
- **课程**: COMP3230B; 对应课件 `Lec/Lec05 virtualize cpu.pdf` 的 Required Reading (共用编号 **05**)
- **原书**: Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP) Ch.6, v1.10
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf

> 本讲覆盖教材全部知识点 (含 Tip / Aside / xv6 `swtch` / Homework 测量说明). 术语首次标英文. 与课堂 `Lec05 virtualize cpu` 互补: slides 偏 API/中断分类与 mode↔context 对照; 本章偏 **受限直接执行 (limited direct execution, LDE)** 协议时间线与硬件陷阱表. **Final 考点**: trap 后是重做本条还是下一条; mode switch ≠ context switch — 见 §8.

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| 目标 | 分时 (time sharing) 共享物理中央处理器 (central processing unit, CPU), 同时保住性能与控制 (control) |
| Crux | 如何 **高效** 虚拟化 CPU, 同时 OS 仍掌控机器? |
| 基本手法 | **直接执行 (direct execution)**: 用户码直接跑在真实 CPU 上; **受限**: 特权操作与抢占靠硬件+OS |
| Problem #1 | 受限操作 → 用户态 (user mode) / 内核态 (kernel mode) + 系统调用 (system call) / 陷入 (trap) |
| Problem #2 | OS 不在跑时如何夺回 CPU → 协作 (cooperative) 等 syscall, 或定时器中断 (timer interrupt) 抢占 (preemption) |
| 换进程 | 上下文切换 (context switch): 保存/恢复寄存器 (register); xv6 的 `swtch` |
| 两次保存 | 硬件把用户寄存器压到内核栈 (kernel stack); OS 软件把内核寄存器存进进程结构体 (process structure) |
| Final | TLB miss / page fault → **重做同一条**; syscall 完成 / timer → **下一条**; mode switch ≠ context switch |

---

## 1. 开篇: 为何需要机制

要把中央处理器虚拟化 (virtualize the CPU), 操作系统 (operating system, OS) 须在多个作业 (job) 间分时: 跑一会儿 A, 再跑 B, …. 挑战有二:

1. **性能 (performance)**: 虚拟化开销 (overhead) 不能过大
2. **控制**: 进程不能永远霸占 CPU, 也不能越权访问不该碰的资源

获得高性能同时保住控制, 是构建 OS 的核心难题之一.

### Crux: 如何高效虚拟化 CPU 并保留控制?

- **自测**: 若只有「直接在 CPU 上跑用户程序」, 缺哪两类能力会让 OS 「沦为库」?
- **参考**: (1) 限制特权操作 (I/O 等); (2) 能强制停掉当前进程并切换. 二者都要硬件协助 + OS 协议.

---

## 2. §6.1 基本技术: 受限直接执行 (Limited Direct Execution)

**直接执行** 很简单: 程序直接在 CPU 上跑. OS 要启动程序时大致:

1. 在进程表 (process list) 建项
2. 分配内存, 从磁盘装入代码
3. 找到入口 (如 `main()`)
4. 跳转过去开始执行

Figure 6.1 是 **尚无限制** 的直接执行协议: 用普通调用/返回进出 `main()`, 像一次过程调用 (procedure call).

问题随之而来:

- 如何在高效运行的同时, 阻止程序做不该做的事?
- 如何停掉当前进程并切换到另一个, 以实现分时?

名字里的 **limited** 由此而来: 不加限制, OS 就无法掌控任何事, 只剩「很悲哀的库」.

---

## 3. §6.2 Problem #1: 受限操作 (Restricted Operations)

直接执行很快 (原生硬件执行), 但进程若要发磁盘 I/O, 或要更多 CPU/内存等资源, 怎么办?

### Crux: 如何执行受限操作?

进程必须能做 I/O 等受限操作, 又不能获得对系统的完全控制. OS 与硬件如何协作?

### Aside: 为何系统调用看起来像过程调用?

`open()` / `read()` 在 C 里写法与普通函数调用一样. 原因: **它确实是过程调用**, 但库内部藏了 trap 指令.

典型路径:

1. 应用调用 `open(...)` → 进入 C 库 (C library)
2. 库按与内核约定的调用约定 (calling convention): 参数放到约定位置 (栈或寄存器), 系统调用号 (system call number) 也放到约定位置
3. 执行 **trap** 进入内核
4. 返回后库解包返回值, 再返回给应用

因此「发系统调用」的库片段常是手写汇编 (assembly): 要严格遵守传参/返回约定, 并执行该架构特有的 trap. 你本人不必写汇编来 trap 进 OS — 别人已经写好了.

这正对应课堂 slides: 用 API (POSIX / glibc) 而非自己发 `SYSCALL` 的原因.

### 用户态与内核态

若任意进程都能随便发磁盘 I/O, 就无法做带权限检查的文件系统 (file system) — 进程可读/写整盘, 保护全失.

硬件引入至少两种处理器模式 (processor mode):

| 模式 | 谁跑 | 能力 |
|---|---|---|
| **用户态 (user mode)** | 典型应用 | 受限; 发 I/O 等特权指令会触发异常 (exception), OS 常杀进程 |
| **内核态 (kernel mode)** | OS / 内核 (kernel) | 可发 I/O, 执行各类特权指令 |

用户进程需要特权服务时走 **系统调用**: 由 Atlas 等早期机器开创, 让内核谨慎暴露关键能力 (访文件, 创建/销毁进程, 进程间通信, 分配内存等). POSIX 有数百个调用; 早期 Unix 约二十个左右.

### Trap 与 return-from-trap

执行系统调用须发特殊 **trap** 指令: **同时** 跳进内核 **并** 提升特权到内核态. 内核做完允许的工作后, 执行 **return-from-trap**: 回到调用方用户程序, 并降回用户态.

硬件在 trap 时须保存足够调用方寄存器, 以便 return-from-trap 正确恢复. 例如 x86: 把程序计数器 (program counter, PC), 标志 (flags) 等压到 **每进程内核栈**; return-from-trap 再弹出. 不同架构约定不同, 思想相同.

### Tip: 使用受保护的控制转移 (Protected Control Transfer)

硬件为 OS 提供:

- 不同执行模式 (user / kernel)
- trap 进入内核, return-from-trap 回用户态
- 让 OS 告知硬件 **陷阱表 (trap table)** 在内存何处的指令

### 陷阱表 (Trap Table): 不能让用户指定跳转地址

过程调用可指定目标地址; trap **不能** 让用户指定内核内任意地址 (Very Bad Idea: 可跳过权限检查或拼接任意内核指令序列).

开机时机器处于特权态. OS 早期动作之一: 配置硬件 — 硬盘中断, 键盘中断, 系统调用等发生时, **跑哪段代码**. OS 用特权指令登记这些 **陷阱处理程序 (trap handler)** 的位置; 硬件记住, 直到下次重启.

精确指定「哪个系统调用」: 用户把 **系统调用号** 放进约定寄存器/栈位置; 内核 trap handler 检查合法性后分派. 这种间接层本身就是一种保护: 用户只能按号请求服务, 不能指定任意内核地址.

设置 trap table 位置本身也是特权操作; 用户态执行会被硬件拒绝.

- **思考**: 若用户能安装自己的 trap table, 能对机器做什么?
- **参考**: 可劫持所有中断/syscall 入口, 实质接管机器.

### Tip: 安全系统须警惕用户输入

即使有硬件 trap 路径, 系统调用边界上的参数仍须校验. 例: `write()` 的缓冲区地址若指向内核地址空间, OS 必须拒绝 — 否则用户可读内核内存 (常映射全部物理内存), 进而读其他进程内存. **安全系统须高度怀疑用户输入.**

### Figure 6.2: LDE 协议时间线

每进程有内核栈, 进出内核时由硬件保存/恢复寄存器 (含通用寄存器与 PC).

**两阶段**:

**Boot (内核态)**:

1. 初始化 trap table (特权)
2. 硬件记住 syscall handler 等地址

**Run**:

1. OS 建进程表项, 分配内存, 装程序, 设用户栈 `argv`
2. 在内核栈填好寄存器/PC, **return-from-trap** → 用户态, 跳到 `main`
3. 用户跑 `main`; 需要服务时 **Call system call** → trap: 硬件保存寄存器到内核栈, 升内核态, 跳 trap handler
4. OS 处理 syscall, 再 return-from-trap → 用户态, **跳到 trap 之后的 PC** (下一条用户指令)
5. `main` 返回后经 stub 调 `exit()` 再 trap; OS 释放内存, 移出进程表

特权指令在书中用粗体标出 (设 trap table, return-from-trap 启动进程等).

### Crux / 自测: 受限操作与 trap

- **自测**: 一次 `open()` 从应用到内核再返回, 特权级如何变? 返回后 PC 指向哪?
- **参考**: user → (trap) kernel → (return-from-trap) user; PC 是 **trap 指令之后** 的下一条, **不是** 重做这条 trap/syscall 指令.

---

## 4. §6.3 Problem #2: 进程间切换

问题: 直接执行时如何实现进程切换? 「OS 决定停 A 开 B」听起来简单, 但 **若进程正在 CPU 上跑, 定义上 OS 就不在跑**. OS 不在 CPU 上就无法采取任何动作.

### Crux: 如何夺回 CPU 控制权?

OS 如何重新获得 CPU, 以便在进程间切换?

### 协作式方法 (Cooperative Approach): 等系统调用

历史上部分系统 (早期 Mac OS, Xerox Alto) 采用 **协作式**: 信任进程表现合理, 跑太久的进程应周期性让出 CPU.

友好进程如何让出?

- 频繁经 **系统调用** 把控制交给 OS (`open`/`read`, 发消息, 创建进程等)
- 显式 **`yield` 系统调用**: 除把控制交给 OS 外什么也不做
- 做非法事也会 trap: 除零, 非法访存 → OS 夺回 CPU (常终止违规进程)

协作式调度下, OS 靠 **等待 syscall 或非法操作** 夺回控制. 若进程恶意或有 bug 陷入 **死循环 (infinite loop)** 且从不 syscall — OS 能做什么? 在纯协作世界里, 往往只能 **重启 (reboot)** 机器.

### Tip: 处理应用不当行为

现代 OS 对越权/非法指令等常采取「一次出局」: **终止** 违规进程. 粗暴, 但非法访存或非法指令时 OS 还能怎样?

### 非协作: OS 主动夺回 — 定时器中断

### Crux: 无协作时如何获得控制?

即使进程不合作, OS 如何确保流氓进程无法霸占机器?

答案: **定时器中断 (timer interrupt)** (多年前多系统独立发现). 可编程定时设备每隔若干毫秒引发中断; 当前进程被打断, 预先配置的 OS 中断处理程序运行 → OS 夺回 CPU, 可停当前进程、启动另一个.

Boot 时 OS 须:

1. 登记 timer handler 到 trap/中断机制 (与 syscall handler 同类)
2. **启动定时器** (特权操作)

之后可放心跑用户程序: 控制终将回到 OS. 关闭定时器也是特权操作 (并发章节再详谈).

中断发生时硬件责任类似显式 syscall trap: 保存足够状态到内核栈, 使日后 return-from-trap 能正确恢复.

### Tip: 用 timer interrupt 夺回控制

Timer 让 OS 即使面对非协作进程也能再次跑在 CPU 上 — 维持机器控制的关键硬件特性.

### Tip: 重启也有用

协作式下死循环只能重启, 看似 hack; 研究显示 reboot (或广义「软件重来」) 对健壮系统很有用: 回到已知更测试过的状态, 回收泄漏资源, 易自动化. 大规模集群常周期性重启机器子集.

### 保存与恢复上下文 (Saving and Restoring Context)

OS 夺回控制后 (协作经 syscall, 或强制经 timer), **调度器 (scheduler)** 决定: 继续当前进程, 还是换另一个. (调度策略见后续章.)

若决定切换, 执行底层 **上下文切换**: 概念上保存当前进程若干寄存器 (如到其内核栈/进程结构), 恢复即将运行进程的寄存器. 最终执行 return-from-trap 时, 恢复的是 **另一进程** 而非原进程.

典型软件步骤 (低级汇编):

1. 保存当前进程的通用寄存器, PC, 内核栈指针
2. 恢复目标进程的上述寄存器, **切换到其内核栈**
3. 因栈已切换: 进入 `switch` 时仍在被中断进程的上下文, **返回时已在另一进程上下文**
4. return-from-trap → 目标进程成为 running

### Figure 6.3: 带 Timer 的 LDE 协议

Boot 额外: 初始化 timer handler, **start interrupt timer**.

运行中 Process A 被 timer 打断:

1. 硬件: `save regs(A) → k-stack(A)`, 升内核态, 跳 trap handler
2. OS 处理 trap, 决定 A→B, 调用 `switch()`:
   - `save regs(A) → proc_t(A)` (进程结构)
   - `restore regs(B) ← proc_t(B)`
   - `switch to k-stack(B)`
3. `return-from-trap` into B: 从 B 的内核栈恢复用户寄存器, 降用户态, 跳到 **B 的 PC**

### 两类寄存器保存/恢复 (必记)

| 时机 | 谁保存 | 保存什么 | 存到哪里 |
|---|---|---|---|
| Timer/syscall **陷入** 时 | **硬件** (隐式) | 当时用户寄存器 | 该进程的 **内核栈** |
| OS 决定 A→B 时 | **OS 软件** (显式) | 内核寄存器上下文 | **进程结构体** (PCB 一类) |

后者把系统从「刚从 A trap 进内核」变成「仿佛刚从 B trap 进内核」. 最后 return-from-trap 弹出的是 B 内核栈上的用户寄存器.

### Figure 6.4: xv6 的 `swtch` (保存寄存器)

教材汇编 (Figure 6.4; x86). 原型: `void swtch(struct context *old, struct context *new);` — 把当前寄存器上下文存入 `*old`, 再从 `*new` 装入.

```asm
# void swtch(struct context *old, struct context *new);
# 保存当前寄存器到 old, 再从 new 加载
.globl swtch
swtch:
  # ---- 保存旧上下文 *old ----
  movl 4(%esp), %eax   # eax ← old 指针 (注意: 此时栈布局因即将 popl 而敏感)
  popl 0(%eax)         # 弹出返回地址 → 存为 old->eip
  movl %esp, 4(%eax)   # 保存当前栈指针 → old->esp
  movl %ebx, 8(%eax)   # 保存其余寄存器到 context 各槽
  movl %ecx, 12(%eax)
  movl %edx, 16(%eax)
  movl %esi, 20(%eax)
  movl %edi, 24(%eax)
  movl %ebp, 28(%eax)

  # ---- 加载新上下文 *new (参数在栈上相对位置已变) ----
  movl 4(%esp), %eax   # eax ← new 指针
  movl 28(%eax), %ebp  # 先恢复除 esp 外的寄存器
  movl 24(%eax), %edi
  movl 20(%eax), %esi
  movl 16(%eax), %edx
  movl 12(%eax), %ecx
  movl 8(%eax), %ebx
  movl 4(%eax), %esp   # ★ 栈指针在此切换到新进程内核栈
  pushl 0(%eax)        # 把 new->eip 压栈, 充当「返回地址」
  ret                  # 跳到新上下文当初调用 swtch 的下一指令
```

要点:

- `old` / `new` 分别来自旧/新进程的 process structure (`struct context`)
- 先把当前内核寄存器写入 `*old`, 再从 `*new` 装入
- **栈指针切换** (`movl 4(%eax), %esp`) 是上下文真正换人的关键一步
- `ret` 返回到 **新上下文** 里当初调用 `swtch` 的下一指令

不必背每条 opcode; 要能说清: **软件保存的是内核上下文到 proc 结构, 与硬件压用户寄存器到内核栈是两层.**

> 本章其余内容多为协议时间线 (Figure 6.1–6.3), 无独立用户态 `.c` 示例; Homework 测量代码需自行编写, 见文末.

### Crux / 自测: 夺回控制与切换

- **自测**: 协作式 vs timer 抢占, 各靠什么入口进内核? 死循环时哪种失效?
- **参考**: 协作靠 syscall/非法操作/yield; 抢占靠 timer. 纯用户态死循环使协作失效, 须 timer.
- **自测**: mode switch 是否等于 context switch?
- **参考**: **否**. Timer/syscall 必然 mode switch (进内核); 仅当调度器选另一进程才 context switch. 见课堂 `Lec05 virtualize cpu` §3.3.

---

## 5. §6.4 并发担忧 (Concurrency Preview)

若 syscall 处理中又来 timer? 或处理一个中断时又来另一个? OS 必须关心 — 这正是全书第二部分 **并发 (concurrency)** 主题; 本章只勾轮廓:

- 处理中断时可 **关中断 (disable interrupts)**, 避免嵌套投递; 关太久会丢中断 (bad)
- 多处理器上用更复杂的锁 (locking) 保护内核数据结构, 允许多活动并行; 锁本身难写, 易出隐蔽 bug

---

## 6. §6.5 Summary 与关键术语

LDE 基本思想: 想跑的程序直接在 CPU 上跑, 但先配置硬件 **限制** 进程在无 OS 协助时能做什么.

类比 **儿童防护 (baby proofing)**: 锁危险柜子, 封插座后, 可让孩子较自由活动. OS 在 boot 时设 trap handler, 开 timer, 再只以受限模式跑进程 → 进程高效运行, 仅在特权操作或霸占 CPU 过久时才需 OS 介入.

机制齐备后, 大问题留给调度器: **给定时刻该跑哪个进程?** (下一章起)

### Aside: 上下文切换要多久?

可用 `lmbench` 等测 syscall 与 context switch 成本. 例: 1996 年 Linux 1.3.37 / 200 MHz P6, syscall ~4 μs, context switch ~6 μs; 现代 2–3 GHz 上常可到亚微秒量级. 注意: 并非所有 OS 操作都随 CPU 频率等比变快 — 许多操作偏内存密集, 内存带宽进步慢于处理器 (Ousterhout). Context switch 还有 **间接开销**: cache / TLB 冷启动等 (课堂 slides 亦强调).

### Aside: Key CPU Virtualization Terms (Mechanisms)

- CPU 至少两种模式: 受限 **user mode**, 特权 **kernel mode**
- 应用经 **system call** trap 进内核请求服务
- **trap** 保存寄存器状态, 改内核态, 跳到 trap table 预定入口
- 服务完经 **return-from-trap** 降特权, 回到 **trap 之后** 的指令
- Trap table 开机由 OS 设置, 用户程序不能随意改 — LDE 协议一部分
- **Timer interrupt** 保证非协作调度下 OS 仍能夺回 CPU
- 需要换进程时做底层 **context switch**

---

## 7. Homework (Measurement) 说明

本章 Homework 是 **测量类**: 在真实机器上写代码测 OS/硬件性能的一面.

1. **测系统调用开销**: 反复调简单 syscall (如 0 字节 `read`), 总时间 / 次数. 注意计时器精度: 先连续两次 `gettimeofday()` 看分辨率, 决定迭代次数; 不够可用 x86 `rdtsc`.
2. **测上下文切换开销**: 更难. `lmbench` 思路: 两进程绑同一 CPU, 用一对管道 (pipe) (或 socket) 来回读写, 迫使阻塞与切换; 多次往返估切换成本. 多核须 `sched_setaffinity` 等绑核, 否则测到的可能是核间迁移而非同核 context switch.

(COMP3230 未必布置本题; 理解「syscall 与 context switch 都有可测成本」即可.)

---

## 8. Final / 课堂对齐: 重做本条 vs 返回下一条

OSTEP Ch.6 正文强调 syscall 的 return-from-trap 回到 **trap 之后** 的 PC; 课堂 `Lec05 virtualize cpu` 与 2023 Final 进一步按 **异常/中断类型** 分类. 下表考试易考, 须与 LDE 协议一起记.

| 事件 | 典型归类 | 处理完后从哪里继续? | 直觉 |
|---|---|---|---|
| **TLB miss** (快表未命中) | 故障类 / 需补翻译 | **重做同一条** 访存指令 | 该指令尚未成功完成; 填好 TLB 后再试 |
| **Page fault** (可处理的缺页) | 故障 (fault) | 常 **重做同一条** 触发缺页的指令 | 装入页/修页表后指令才应成功 |
| **System call 完成** | Trap (故意陷入) | **下一条** 用户指令 | `syscall` 指令本身已执行完 |
| **Timer interrupt** | 异步中断 | **下一条** (当前指令通常已完成后再进 handler) | 不是「重做触发中断的那条」 |
| **除零** 等不可恢复 | 常 abort / 杀进程 | **不** 重做同一条除法 | 进程被终止, 无「修复后再试」 |

### 自测 (Final 风格)

- **问**: 下列哪件事让系统从 **触发事件的同一条指令** 重新执行? (A) syscall 完成 (B) 除零 (C) TLB miss (D) 时钟中断
- **答**: **(C) TLB miss**. A/D 回下一条; B 通常杀进程不重做.

### Mode switch ≠ Context switch (再强调)

| | Mode switch | Context switch |
|---|---|---|
| 含义 | user ↔ kernel | 进程 A → 进程 B |
| 是否每次 syscall/timer 都发生? | 是 (进内核) | **否**; 仅调度器换人时 |
| 地址空间 | 仍属当前进程 | 换成另一进程的内存信息 |

`read()` 成功返回同一进程: 有 mode switch, **无** context switch.

---

## 9. 与课堂 `Lec05 virtualize cpu` 对照

| OSTEP Ch.6 | 课堂 slides |
|---|---|
| LDE 协议 Figure 6.1–6.3 时间线 | Process control 三问 + 直接执行 |
| Aside: syscall 像过程调用 | 为何用 API / glibc 封装 trap |
| User/kernel + trap table | System call 实现与 syscall table |
| Cooperative vs timer | 被动等 syscall vs 主动 timer |
| 两类寄存器保存 + `swtch` | Context switch 步骤与 PCB/内核栈 |
| Context switch 耗时 Aside | 直接/间接开销 (cache, TLB) |
| (本章略) 异常细分类 | Fault / Trap / Abort; Final 重做 vs 下一条 |
| Mode/context 在切换叙事中隐含 | 显式对照表 + 自测 |

---

## 章节结构 (写完索引)

| 节 | 内容 |
|---|---|
| 0 | 一页速览 |
| 1 | 开篇 + Crux (高效虚拟化且保留控制) |
| 2 | §6.1 LDE 基本技术 / Figure 6.1 |
| 3 | §6.2 受限操作: user·kernel, syscall 像过程调用, protected control transfer, trap table, Figure 6.2 |
| 4 | §6.3 夺回 CPU: 协作 vs timer, context switch, 两类保存, xv6 `swtch`, Figure 6.3–6.4 |
| 5 | §6.4 并发预告 (关中断 / 锁) |
| 6 | §6.5 Summary, 关键术语, 切换开销 |
| 7 | Homework 测量说明 |
| 8 | **Final 对齐**: 重做本条 vs 下一条; mode ≠ context |
| 9 | 与 `Lec05 virtualize cpu` 对照表 |
