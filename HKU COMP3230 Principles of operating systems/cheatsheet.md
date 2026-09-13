# COMP3230 Cheatsheet

> 词条/概念速查; 对话中学到的内容会增量追加.
> 约定: **定义** 写清设定与含义; 若有命题式结论则写 **假设** + **结论**; 证明/细节见对应讲义. 本课多为机制与约定而非数学定理, 仍须标明「在什么设定下指什么」.

---

## 课程组织

+ **Assessment** / **评分构成**:
    + **含义**: Labs 4% + PS 18% + PA 28% + Final 50%; Final 为 open-book, 无 midterm
    + **注**: 开卷仍考 mechanism/policy 理解, 不能只靠翻书

+ **Slip days** / **宽限日**:
    + **设定**: 适用于 PS / PA 迟交
    + **含义**: 全学期共 5 天额度; 单次作业最多额外 +3 天; 超额后每天扣该作业分的 20%

+ **OSTEP**:
    + **含义**: *Operating Systems: Three Easy Pieces* (Remzi & Andrea Arpaci-Dusseau); 本课 required online textbook
    + **注**: 课堂 slides 与 OSTEP 章节互补 (如 slides 偏架构分类, Ch.2 偏虚拟化直觉)

+ **PA / PS**:
    + **含义**: PA = Programming Assignment (编程作业); PS = Problem Set (书面题集)
    + **注**: 评分权重不同 (见 Assessment); 迟交规则共用 slip days

---

## 名词

+ **Mechanism vs policy** / **机制 vs 策略**:
    + **设定**: 讨论 OS 如何支撑某类服务 (调度, 内存分配, 保护等)
    + **定义**: mechanism = 系统「能做什么 / 用什么原语做」; policy = 「如何选择 / 如何分配」(在机制之上做决策)
    + **注**: 好设计常把二者分离, 以便换策略而不改底层机制

+ **Kernel / User mode** / **内核态 / 用户态**:
    + **设定**: CPU 提供至少两级特权 (privilege / supervisor vs user)
    + **定义**:
        + **内核态 (kernel mode)**: 执行内核代码时; 可执行机器上任意指令, 可直接访硬件与受保护资源
        + **用户态 (user mode)**: 执行应用代码时; 仅允许非特权指令子集; 非法特权操作会 trap
    + **注**: 系统调用经 trap 升到内核态, 再经 return-from-trap 降回用户态 (见 Trap)

+ **System call** / **系统调用**:
    + **设定**: 用户进程需要 OS 提供的服务 (I/O, 进程控制, 文件等), 且自身处于用户态
    + **定义**: 应用向 OS 请求服务的受控接口 (API); 全体系统调用构成该 OS 对应用暴露的服务面
    + **注**: 与普通过程调用不同: 须经 trap 进入内核, 由内核校验并执行, 再 return-from-trap

+ **OS architectures** / **操作系统架构**:
    + **设定**: 如何组织内核代码与特权边界
    + **含义** (四类常见):
        + **Monolithic (单体)**: 多数服务在内核态同一大地址空间; 效率高, 改动牵连大, 一处错易拖垮内核
        + **Layered (分层)**: 按层组织, 下层为上层提供服务; 利于信息隐藏与替换, 层间调用可能增开销
        + **Microkernel (微内核)**: 内核态只留极少核心 (如 IPC, 基本调度); 其余以用户态 server 经消息传递协作; 更安全可扩展, 常因 IPC 有性能代价
        + **Modular (模块化)**: 现代常见形态 — 仍以单体为底, 但以动态可加载 **kernel modules** 扩展; 模块有受保护接口
    + **注**: Linux / 传统 Unix 等多为「单体 + 模块」; 勿把 modular 与纯 microkernel 混为一谈

+ **Process** / **进程**:
    + **设定**: 多道程序 / 分时系统中, OS 把「正在执行的程序」作为调度与资源分配单位
    + **定义**: 执行中的程序实例; 至少包含私有 **地址空间** (典型 Text / Data / Heap / Stack) + 所占资源 (打开文件, 设备等) + **执行状态** (寄存器含 PC, 栈指针; 以及进程状态标志)
    + **注**: Program 是磁盘上的「死」映像; Process 是运行时的「活」实例. 同一程序可对应多个进程

+ **PCB** / **进程控制块** (Process Control Block / process descriptor):
    + **设定**: OS 要管理多个进程
    + **定义**: 内核为每个进程维护的数据结构, 保存管理与切换所需信息. 典型字段含: PID, 父 PID, PC 与通用寄存器上下文, 进程状态, 调度信息 (优先级等), 内存管理信息, 打开文件 / I/O, 信号相关指针等
    + **注**: 进程表 (process table) 常存指向各 PCB 的指针; ready/blocked 等列表链的是 PCB

+ **Process states** / **进程状态**:
    + **设定**: 进程生命周期中, OS 用状态标志刻画「当前在做什么」
    + **定义** (课堂常用五态 + zombie 语义):
        + **new**: 正在创建, 尚未可调度
        + **ready**: 可运行, 等待获得 CPU
        + **running**: 正在 CPU 上执行
        + **blocked** (waiting): 等待某事件 (I/O, 锁, `wait` 等), 暂不能跑
        + **terminated** (含 **zombie**): 已结束执行, 但可能尚未完全清理 (见 Zombie)
    + **注**: 典型转换: new → ready ⇄ running; running → blocked → ready; running → terminated. Suspend 与 Blocked 不同: suspend 常指被显式挂起/换出, 未必在等同一类事件

+ **fork / exec / wait**:
    + **设定**: Unix/Linux 进程创建与同步 API (用户态经系统调用进入内核)
    + **定义**:
        + **`fork()`**: 复制调用进程, 创建几乎相同的子进程 (独立地址空间副本 + 继承部分资源); 父子从 `fork` 返回处继续, 靠返回值区分 (子为 0, 父为子 PID)
        + **`exec` 族**: 用新程序映像 **替换** 当前进程的地址空间与执行映像; PID 不变, 不创建新进程
        + **`wait` / `waitpid` 等**: 父进程等待子进程结束 (或状态变化), 取 exit status 等, 并让内核清除对应 zombie
    + **注 (易混)**: `fork` = 造新进程 (复制); `exec` = 同 PID 换程序; Windows `CreateProcess` 大致相当于 `fork`+`exec` 合一. 只 `fork` 不 `exec` 会跑同一段代码的两个副本; 只 `exec` 不 `fork` 则当前进程被替换掉

+ **Zombie** / **僵尸进程**:
    + **设定**: Unix; 子进程已调用 `exit` (或异常终止), 父进程尚未 `wait*`
    + **定义**: 处于 terminated 的进程: 用户态映像与多数资源已释放, 但 **PCB (及 exit status 等摘要) 仍保留**, 供父进程日后取得
    + **注 (易混)**: zombie ≠ 仍在跑的「死循环进程」; 也 ≠ orphan (父先死, 子被 init/ systemd 收养). 父 `wait*` 后内核才彻底删掉该 PCB; 大量未 wait 的子进程会占满进程表项

+ **Signal** / **信号**:
    + **设定**: Unix 进程间 / 内核向进程通知事件
    + **定义**: 软件中断式通知机制. 进程可对多数信号选择: 默认动作 / 忽略 / 捕获 (注册 signal handler); 也可用 mask 暂时阻塞投递
    + **分类**:
        + **同步 (synchronous)**: 由当前指令直接触发 (如非法访存 → `SIGSEGV`, 除零), OS 立即投递给该进程
        + **异步 (asynchronous)**: 由外部事件产生, 相对目标进程到达时刻不可预测 (如 timer, 他进程 `kill()`)
    + **假设 / 例外**: `SIGKILL` 与 `SIGSTOP` **不可** 被捕获, 阻塞或忽略
    + **注**: `fork` 后子进程继承 handler 设置; 随后 `exec` 会把曾自定义的 handler **重置为默认**

+ **Virtualization (OSTEP)** / **虚拟化**:
    + **设定**: OSTEP 对 OS 角色的核心叙事; 物理资源有限且共享
    + **含义**: OS 把物理 CPU / 内存等变成每个进程看来「易用、私有」的虚拟形态. 书中把 OS 说成: 虚拟机 + 系统调用库 + 资源管理器 (三者同一对象的不同侧面)
    + **注**: 此处 virtualization 指 OS 对资源的抽象, 不特指硬件虚拟机监视器 (hypervisor); 后者可作分层架构的例子

+ **Three Easy Pieces** / **三大主题**:
    + **设定**: OSTEP 全书组织
    + **含义**: (1) **Virtualization** — CPU 与 memory 的虚拟化; (2) **Concurrency** — 交错执行下的正确性; (3) **Persistence** — 设备与文件系统上的持久存储
    + **注**: 与课堂「进程/内存/并发/文件」四大职能叙述对应, 用词略不同但主题重合

+ **Trap / return-from-trap**:
    + **设定**: 需从用户态进入内核处理 (系统调用, 异常, 部分中断路径)
    + **定义**:
        + **trap**: 特殊指令/事件使硬件保存用户上下文, 转入预设 **trap handler**, 并提升到内核态
        + **return-from-trap**: 内核处理完毕后恢复用户上下文, 降回用户态, 从中断点附近继续
    + **注 (易混)**: trap 常强调 **同步** 陷入 (由当前指令引发, 含 syscall); interrupt 常强调 **异步** 外部事件. 二者都可能经类似「进内核 → 处理 → 返回」路径, 课堂把 syscall 路径概括为 trap / return-from-trap

+ **Limited Direct Execution (LDE)** / **受限直接执行**:
    + **设定**: OS 要在「让用户程序高速跑在 CPU 上」与「仍能控制/保护」之间折中
    + **定义**: 多数时间让用户代码 **直接** 在 CPU 上执行 (无解释器逐条翻译); 仅在特权操作 / 需 OS 介入时经 trap 进入内核
    + **结论**: 性能接近裸机运行, 控制靠硬件特权 + 系统调用边界实现

+ **Context switch vs Mode switch** / **上下文切换 vs 模式切换**:
    + **设定**: 同一 CPU 上多进程 / 用户态与内核态切换
    + **定义**:
        + **Mode switch**: 同一进程内用户态 ⇄ 内核态 (trap / return-from-trap); 不必换进程
        + **Context switch**: OS 把 CPU 从一进程交给另一进程; 保存/恢复寄存器与 PCB 等上下文, 通常伴随地址空间切换
    + **结论**: 每次 context switch 往往含 mode switch; 反之 mode switch (如 syscall) **不必** 换进程

+ **Timer interrupt** / **时钟中断**:
    + **设定**: 分时 / 抢占式调度; 用户进程可能长时间不主动让出 CPU
    + **定义**: 硬件定时器周期性发中断, 强制进入内核, 使调度器有机会切换进程
    + **结论**: 是 OS **主动夺回** CPU 的关键机制 (相对阻塞式 I/O 等「被动让出」)

+ **Interrupt vector** / **中断向量**:
    + **设定**: CPU 收到中断/异常后需找到对应处理例程
    + **定义**: 按中断号索引的表 (或等价结构), 存放各 handler 入口地址; 硬件据此跳转
    + **结论**: 不同中断类型 (timer, 设备, 异常等) 经向量表分发到不同内核处理路径
