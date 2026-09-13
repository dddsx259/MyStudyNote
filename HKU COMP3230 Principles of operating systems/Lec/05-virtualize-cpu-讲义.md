# Virtualizing the CPU: CPU 虚拟化机制

- **来源**: `Lec/05-virtualize-cpu.pdf` (24 页; 原名 `03-VirtualizeCPU.pdf`)
- **课程**: COMP3230B Principles of Operating Systems
- **学习成果**: ILO 2a — 解释 OS 如何管理进程/线程, 以及高效共享 CPU 的机制与策略
- **必读**: OSTEP Ch.6 *Mechanism: Limited Direct Execution*  
  [cpu-mechanisms.pdf](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-mechanisms.pdf)

> 本讲以机制为主 (system call / context switch / interrupt); 与 `04-process-abstraction` 的进程抽象衔接. 术语首次标英文.

---

## 本节在课程中的位置

进程抽象给出「每个进程像独占机器」的接口; 本讲回答 **如何在真实单/少核 CPU 上实现该幻觉**: 受限操作走系统调用 (system call), 多进程分时靠上下文切换 (context switch), OS 夺回控制靠中断 (interrupt) (尤其 timer).

---

## 0. 一页速览

| 问题 | 机制 |
|---|---|
| 如何做特权操作? | System call (+ API 封装) |
| 如何假装有很多 CPU? | 分时运行 + context switch |
| OS 如何夺回 CPU? | 自愿: syscall; 非自愿: interrupt (timer 等) |
| 透明性 (transparency) | 进程不知何时被切走; 程序员不必手写调度 |

---

## 1. Process control 三问 (p.5)

1. **受限操作** → Mechanism: **system calls**
2. **多 CPU 幻觉 (virtualizing the CPU)** → Mechanism: **context switching** (轮流跑进程, 并非给虚拟 CPU 芯片)
3. **夺回控制**:
   - 自愿释放: 仍常经 system call
   - 非自愿: **interrupt** (硬件定时器等)

**直接执行 (direct execution)**: 用户程序在真实 CPU 上跑; OS 仍需能随时介入.

---

## 2. System calls (p.6–11)

### 2.1 角色与 API

- 系统调用让内核**谨慎暴露**关键服务; 常见 OS 有数百个
- 应用多经高层 **API** (Windows API / POSIX), 而非直接写 trap 指令
- Unix 上 API 常在运行时库 (如 C 库 / glibc)

**为何用 API 而非直接 syscall**:

- 调用者不必知道该 OS/硬件上如何 trap
- 不同 OS 实现细节不同, 常含汇编
- API 隐藏细节, 并统一传参与返回约定

### 2.2 实现要点

典型路径: 应用 → 库函数 → 特殊指令 (`INT` / `SYSCALL` / `SYSENTER`) **trap** 进内核 → 按编号查表调 `sys_*` → `IRET` / `SYSRET` / `SYSEXIT` **return-from-trap** 回用户态.

- 每个 syscall 有编号; trap 前库把编号与参数放在约定寄存器/栈位置
- 内核维护 **syscall 表** (编号 → 处理函数地址)
- 硬件或软件须保存足够寄存器上下文以便正确返回

**例子直觉** (`open`): 编译到汇编可见参数进 `RDI`/`ESI` 等, 经 PLT 进 glibc; glibc 里 `mov` 系统调用号到 `EAX`/`RAX` 后执行 `syscall`.

### 2.3 与 mode switch

System call 触发 **mode switch** (user → kernel). 此时内核「代表该进程」执行, 地址空间等仍属该进程; 返回后可继续用户态.

---

## 3. Virtualizing the CPU 与 context switch (p.12–18)

### 3.1 含义

- 目标: 每个进程以为自己有 CPU
- **不是**另造一颗虚拟 CPU; 程序仍直接跑在物理 CPU 上
- 做法: 跑 A → 停 A → 跑 B → …
- **Crux**: 如何透明地暂停并恢复? 直接执行时 OS 如何夺回 CPU?

### 3.2 Context switch 定义

**上下文切换 (context switch)**: 把当前进程执行上下文换成另一进程的上下文.

要保证逻辑正确:

1. 停进程前 **保存** 其上下文 (寄存器等)
2. 恢复时把即将运行进程的上下文装回 CPU
3. 上下文存在何处? → 与 **PCB** / 内核栈等相关 (详见 OSTEP Ch.6)

### 3.3 Mode switch vs context switch

| | Mode switch | Context switch |
|---|---|---|
| 含义 | user ↔ kernel | 进程 A → 进程 B |
| 地址空间 | 通常仍是同一进程 | 切换到另一进程的内存信息 |
| 场景 | syscall / interrupt 进入内核 | 调度决定换进程 |

进入内核处理 syscall/中断 **不一定** 换进程; 调度器决定后才做完整 context switch.

### 3.4 步骤 (示意)

1. 保存当前进程用户/内核相关寄存器等到内核栈 / PCB
2. 更新 PCB 状态, 挂到合适队列 (ready / blocked 等)
3. 按 **调度策略 (scheduling policy)** 选就绪进程
4. 装载新进程内存信息与寄存器, 切到其内核栈
5. 从 syscall/中断返回路径恢复用户寄存器并继续

### 3.5 开销 (overhead)

- 切换期间 CPU **不在**做应用「有用计算」 → 切太频会拖慢完成时间
- OS 应尽量缩短切换时间; 部分架构有硬件辅助指令
- **间接开销**: 新进程可能缺页 / 缓存冷启动 (cache / TLB 等失效)

---

## 4. 夺回 CPU: 被动 vs 主动 (p.19)

- **被动**: 等进程 syscall 或非法操作. 多数时候够用; 若死循环且从不 trap → OS 失控
- **主动** (非协作进程): 需硬件支持 — **timer** 周期性产生中断, 强制进入内核, OS 可调度

---

## 5. Interrupts (p.20–23)

### 5.1 何谓中断

**中断 (interrupt)**: 软/硬件需要 CPU 注意时发出的事件, 使 OS 能立即响应.

- 设备经中断线或 **APIC (Advanced Programmable Interrupt Controller)** 通知 CPU
- 相对当前进程往往 **异步 (asynchronous)** (如按键、网卡)

### 5.2 与异常 (exception)

由**当前指令流**触发、与执行 **同步 (synchronous)** 的常称 **exception** (课件亦归入 interrupt 讨论):

| 类 | 直觉 | 例 |
|---|---|---|
| **Fault** | 指令执行前发现可修复问题 | page fault, segfault (部分可修复后重试) |
| **Trap** | 指令执行后故意陷入 | `INT` / syscall |
| **Abort** | 不可恢复 | 严重硬件故障等 |

### 5.3 处理流程 (timer 调度场景)

1. CPU 完成当前指令后跳入内核
2. 用中断控制器给出的向量号索引 **interrupt vector** (启动时 OS 填好的处理函数表)
3. 保存剩余状态 (如内核栈), 跑 **interrupt handler**
4. 调度器决定: 恢复原进程, 或 **context switch** 到另一就绪进程

---

## 6. Summary (p.24)

三大机制:

1. **System call**: 用户获得 OS 服务; 伴随 user↔kernel mode switch
2. **Context switch**: CPU 虚拟化的关键动作; 保存/恢复全套寄存器上下文; 有直接与间接开销
3. **Interrupt**: 设备/定时器告警; 给 OS 夺回 CPU 并可能调度的机会

---

## 易错点

1. Mode switch ≠ context switch: 进内核处理 syscall 后仍可回到同一进程
2. Virtualizing CPU ≠ 仿真一颗假 CPU; 是分时 + 保存/恢复
3. 仅靠被动等 syscall 不够对付死循环 → 需要 timer interrupt
4. Context switch 开销不只「几条 mov」, 还有 cache/TLB 等间接成本
5. Trap (故意陷入) 与 Fault (可修复异常) / Abort 勿混

## 与前后章

- 前: Process abstraction (PCB / 状态 / fork-exec); OSTEP Ch.2 虚拟化直觉
- 并行必读: OSTEP Ch.6 Limited Direct Execution
- 后: 调度策略 (policy), 线程, 更多中断与 I/O
