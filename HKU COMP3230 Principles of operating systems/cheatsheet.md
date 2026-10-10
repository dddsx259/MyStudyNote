# COMP3230 Cheatsheet

> 词条/概念速查; 对话中学到的内容会增量追加.
> 约定: **定义** 写清设定与含义; 若有命题式结论则写 **假设** + **结论**; 证明/细节见对应讲义. 本课多为机制与约定而非数学定理, 仍须标明「在什么设定下指什么」.
> 命名: 优先讲义/OSTEP 用语; 须附英文全称; 自行整理的概括名须标 `(自拟)`.
> 勾选: 每条顶层词条前的 `- [ ]` 用于标记是否已手写整理入 HandCS, 或已决定省略; `[x]` = 已处理.

---

## 课程组织

- [ ] **Assessment** / **评分构成**:
    + **含义**: Labs 4% + PS 18% + PA 28% + Final 50%; Final 为 open-book, 无 midterm
    + **注**: 开卷仍考 mechanism/policy 理解, 不能只靠翻书

- [ ] **Slip days** / **宽限日**:
    + **设定**: 适用于 PS / PA 迟交
    + **含义**: 全学期共 5 天额度; 单次作业最多额外 +3 天; 超额后每天扣该作业分的 20%

- [ ] **OSTEP**:
    + **含义**: *Operating Systems: Three Easy Pieces* (Remzi & Andrea Arpaci-Dusseau); 本课 required online textbook
    + **注**: 课堂 slides 与 OSTEP 章节互补 (如 slides 偏架构分类, Ch.2 偏虚拟化直觉)

- [ ] **PA / PS**:
    + **含义**: PA = Programming Assignment (编程作业); PS = Problem Set (书面题集)
    + **注**: 评分权重不同 (见 Assessment); 迟交规则共用 slip days

---

## 名词

- [ ] **Mechanism vs policy** / **机制 vs 策略**:
    + **设定**: 讨论 OS 如何支撑某类服务 (调度, 内存分配, 保护等)
    + **定义**: mechanism = 系统「能做什么 / 用什么原语做」; policy = 「如何选择 / 如何分配」(在机制之上做决策)
    + **注**: 好设计常把二者分离, 以便换策略而不改底层机制

- [ ] **Kernel / User mode** / **内核态 / 用户态**:
    + **设定**: CPU 提供至少两级特权 (privilege / supervisor vs user)
    + **定义**:
        + **内核态 (kernel mode)**: 执行内核代码时; 可执行机器上任意指令, 可直接访硬件与受保护资源
        + **用户态 (user mode)**: 执行应用代码时; 仅允许非特权指令子集; 非法特权操作会 trap
    + **注**: 系统调用经 trap 升到内核态, 再经 return-from-trap 降回用户态 (见 Trap)

- [ ] **System call** / **系统调用**:
    + **设定**: 用户进程需要 OS 提供的服务 (I/O, 进程控制, 文件等), 且自身处于用户态
    + **定义**: 应用向 OS 请求服务的受控接口 (API); 全体系统调用构成该 OS 对应用暴露的服务面
    + **注**: 与普通过程调用不同: 须经 trap 进入内核, 由内核校验并执行, 再 return-from-trap

- [ ] **OS architectures** / **操作系统架构**:
    + **设定**: 如何组织内核代码与特权边界
    + **含义** (四类常见):
        + **Monolithic (单体)**: 多数服务在内核态同一大地址空间; 效率高, 改动牵连大, 一处错易拖垮内核
        + **Layered (分层)**: 按层组织, 下层为上层提供服务; 利于信息隐藏与替换, 层间调用可能增开销
        + **Microkernel (微内核)**: 内核态只留极少核心 (如 IPC, 基本调度); 其余以用户态 server 经消息传递协作; 更安全可扩展, 常因 IPC 有性能代价
        + **Modular (模块化)**: 现代常见形态 — 仍以单体为底, 但以动态可加载 **kernel modules** 扩展; 模块有受保护接口
    + **注**: Linux / 传统 Unix 等多为「单体 + 模块」; 勿把 modular 与纯 microkernel 混为一谈

- [ ] **Process** / **进程**:
    + **设定**: 多道程序 / 分时系统中, OS 把「正在执行的程序」作为调度与资源分配单位
    + **定义**: 执行中的程序实例; 至少包含私有 **地址空间** (典型 Text / Data / Heap / Stack) + 所占资源 (打开文件, 设备等) + **执行状态** (寄存器含 PC, 栈指针; 以及进程状态标志)
    + **注**: Program 是磁盘上的「死」映像; Process 是运行时的「活」实例. 同一程序可对应多个进程. OSTEP 称其 **机器状态 (machine state)** = 地址空间 + 寄存器 + I/O 信息
    + **来源**: slides `Lec04 process abstraction`; OSTEP Ch.4 `OSTEP 4 process`

- [ ] **Time sharing / Space sharing** / **时间共享 / 空间共享**:
    + **设定**: 物理资源少, 要给多使用者「私有」幻觉
    + **定义**:
        + **Time sharing**: 同一资源在时间上轮流占用 (典型: 单核 CPU 多进程)
        + **Space sharing**: 资源在空间上切开分给不同使用者 (典型: 磁盘块分给文件)
    + **结论**: CPU 虚拟化主靠 time sharing + context switch; 勿把「同时看起来在跑」说成 space sharing
    + **来源**: OSTEP Ch.4 TIP

- [ ] **fork 后值独立 vs 虚拟地址可相同** `(自拟)`:
    + **设定**: `fork` 后父子各有变量副本; 2023 Final Q1e
    + **假设**: `fork` 前有 `a = A`; 之后父改 `a`, 子另改或不改
    + **结论**: **值** 独立 (各写各的物理页副本); **打印 `&a` 的虚拟地址可以相同** (`fork` 不改 VA 布局). 勿答「地址也必须不同」
    + **来源**: OSTEP Ch.5; `OSTEP 5 process api` §2

- [ ] **PCB** / **进程控制块** (Process Control Block / process descriptor):
    + **设定**: OS 要管理多个进程
    + **定义**: 内核为每个进程维护的数据结构, 保存管理与切换所需信息. 典型字段含: PID, 父 PID, PC 与通用寄存器上下文, 进程状态, 调度信息 (优先级等), 内存管理信息, 打开文件 / I/O, 信号相关指针等
    + **注**: 进程表 (process table) 常存指向各 PCB 的指针; ready/blocked 等列表链的是 PCB

- [ ] **Process states** / **进程状态**:
    + **设定**: 进程生命周期中, OS 用状态标志刻画「当前在做什么」
    + **定义** (课堂常用五态 + zombie 语义):
        + **new**: 正在创建, 尚未可调度
        + **ready**: 可运行, 等待获得 CPU
        + **running**: 正在 CPU 上执行
        + **blocked** (waiting): 等待某事件 (I/O, 锁, `wait` 等), 暂不能跑
        + **terminated** (含 **zombie**): 已结束执行, 但可能尚未完全清理 (见 Zombie)
    + **注**: 典型转换: new → ready ⇄ running; running → blocked → ready; running → terminated. Suspend 与 Blocked 不同: suspend 常指被显式挂起/换出, 未必在等同一类事件

- [ ] **fork / exec / wait**:
    + **设定**: Unix/Linux 进程创建与同步 API (用户态经系统调用进入内核)
    + **定义**:
        + **`fork()`**: 复制调用进程, 创建几乎相同的子进程 (独立地址空间副本 + 继承部分资源); 父子从 `fork` 返回处继续, 靠返回值区分 (子为 0, 父为子 PID)
        + **`exec` 族**: 用新程序映像 **替换** 当前进程的地址空间与执行映像; PID 不变, 不创建新进程; **成功则不返回**
        + **`wait` / `waitpid` 等**: 父进程等待子进程结束 (或状态变化), 取 exit status 等, 并让内核清除对应 zombie
    + **结论**: 拆开 `fork`/`exec` 的收益: shell 可在二者之间改 fd → 重定向 / 管道, 且不必改被运行程序
    + **注 (易混)**: `fork` = 造新进程 (复制); `exec` = 同 PID 换程序; Windows `CreateProcess` 大致相当于 `fork`+`exec` 合一. 只 `fork` 不 `exec` 会跑同一段代码的两个副本; 只 `exec` 不 `fork` 则当前进程被替换掉
    + **来源**: OSTEP Ch.5 `OSTEP 5 process api`

- [ ] **Zombie** / **僵尸进程**:
    + **设定**: Unix; 子进程已调用 `exit` (或异常终止), 父进程尚未 `wait*`
    + **定义**: 处于 terminated 的进程: 用户态映像与多数资源已释放, 但 **PCB (及 exit status 等摘要) 仍保留**, 供父进程日后取得
    + **注 (易混)**: zombie ≠ 仍在跑的「死循环进程」; 也 ≠ orphan (父先死, 子被 init/ systemd 收养). 父 `wait*` 后内核才彻底删掉该 PCB; 大量未 wait 的子进程会占满进程表项

- [ ] **Signal** / **信号**:
    + **设定**: Unix 进程间 / 内核向进程通知事件
    + **定义**: 软件中断式通知机制. 进程可对多数信号选择: 默认动作 / 忽略 / 捕获 (注册 signal handler); 也可用 mask 暂时阻塞投递
    + **分类**:
        + **同步 (synchronous)**: 由当前指令直接触发 (如非法访存 → `SIGSEGV`, 除零), OS 立即投递给该进程
        + **异步 (asynchronous)**: 由外部事件产生, 相对目标进程到达时刻不可预测 (如 timer, 他进程 `kill()`)
    + **假设 / 例外**: `SIGKILL` 与 `SIGSTOP` **不可** 被捕获, 阻塞或忽略
    + **注**: `fork` 后子进程继承 handler 设置; 随后 `exec` 会把曾自定义的 handler **重置为默认**

- [ ] **Virtualization (OSTEP)** / **虚拟化**:
    + **设定**: OSTEP 对 OS 角色的核心叙事; 物理资源有限且共享
    + **含义**: OS 把物理 CPU / 内存等变成每个进程看来「易用、私有」的虚拟形态. 书中把 OS 说成: 虚拟机 + 系统调用库 + 资源管理器 (三者同一对象的不同侧面)
    + **注**: 此处 virtualization 指 OS 对资源的抽象, 不特指硬件虚拟机监视器 (hypervisor); 后者可作分层架构的例子

- [ ] **Three Easy Pieces** / **三大主题**:
    + **设定**: OSTEP 全书组织
    + **含义**: (1) **Virtualization** — CPU 与 memory 的虚拟化; (2) **Concurrency** — 交错执行下的正确性; (3) **Persistence** — 设备与文件系统上的持久存储
    + **注**: 与课堂「进程/内存/并发/文件」四大职能叙述对应, 用词略不同但主题重合

- [ ] **Trap / return-from-trap**:
    + **设定**: 需从用户态进入内核处理 (系统调用, 异常, 部分中断路径)
    + **定义**:
        + **trap**: 特殊指令/事件使硬件保存用户上下文, 转入预设 **trap handler**, 并提升到内核态
        + **return-from-trap**: 内核处理完毕后恢复用户上下文, 降回用户态, 从中断点附近继续
    + **注 (易混)**: trap 常强调 **同步** 陷入 (由当前指令引发, 含 syscall); interrupt 常强调 **异步** 外部事件. 二者都可能经类似「进内核 → 处理 → 返回」路径, 课堂把 syscall 路径概括为 trap / return-from-trap

- [ ] **Limited Direct Execution (LDE)** / **受限直接执行**:
    + **设定**: OS 要在「让用户程序高速跑在 CPU 上」与「仍能控制/保护」之间折中
    + **定义**: 多数时间让用户代码 **直接** 在 CPU 上执行 (无解释器逐条翻译); 仅在特权操作 / 需 OS 介入时经 trap 进入内核
    + **结论**: 性能接近裸机运行, 控制靠硬件特权 + 系统调用边界实现
    + **来源**: OSTEP Ch.6; `OSTEP 6 limited direct execution-…讲义.md`

- [ ] **Protected Control Transfer** / **受保护的控制转移**:
    + **设定**: 用户程序不能随意跳进内核任意地址
    + **定义**: 硬件提供 user/kernel 模式, trap / return-from-trap, 以及由 OS 在 boot 时装好的 **trap table** (用户只能按 syscall 号请求服务)
    + **结论**: syscall 像过程调用是因为库内藏 trap; 跳转目标由硬件+trap table 决定, 非用户指定地址

- [ ] **Trap table** / **陷阱表**:
    + **设定**: trap / 中断发生时硬件须知道跑哪段内核代码
    + **定义**: boot 时 OS 用特权指令登记各 handler 入口; 硬件记住直至重启; 用户态不可改
    + **结论**: 与中断向量表同类思想; 是 LDE 协议的启动阶段

- [ ] **两类寄存器保存 (LDE context switch)** `(自拟)`:
    + **设定**: timer/syscall 后若调度器决定换进程
    + **定义**: (1) **硬件** 把用户寄存器压到当前进程 **内核栈**; (2) **OS 软件** (`swtch`) 把内核寄存器写入 **进程结构体**, 再装入目标进程并切换内核栈
    + **结论**: return-from-trap 最终恢复的是 **目标进程** 内核栈上的用户寄存器

- [ ] **Resume after trap: same vs next instruction** `(自拟)` / **trap 后重做本条 vs 下一条**:
    + **设定**: Final 易考「从哪条指令继续」
    + **定义**:
        + **重做同一条**: TLB miss, 可处理的 page fault (指令尚未成功完成)
        + **返回下一条**: syscall 完成, timer interrupt (当前指令通常已做完)
        + **不重做**: 除零等不可恢复 → 常杀进程
    + **结论**: 与 fault vs trap 分类一致; 见 `OSTEP 6 limited direct execution-…讲义.md` §8

- [ ] **Context switch vs Mode switch** / **上下文切换 vs 模式切换**:
    + **设定**: 同一 CPU 上多进程 / 用户态与内核态切换
    + **定义**:
        + **Mode switch**: 同一进程内用户态 ⇄ 内核态 (trap / return-from-trap); 不必换进程
        + **Context switch**: OS 把 CPU 从一进程交给另一进程; 保存/恢复寄存器与 PCB 等上下文, 通常伴随地址空间切换
    + **结论**: 每次 context switch 往往含 mode switch; 反之 mode switch (如 syscall) **不必** 换进程

- [ ] **Timer interrupt** / **时钟中断**:
    + **设定**: 分时 / 抢占式调度; 用户进程可能长时间不主动让出 CPU
    + **定义**: 硬件定时器周期性发中断, 强制进入内核, 使调度器有机会切换进程
    + **结论**: 是 OS **主动夺回** CPU 的关键机制 (相对协作式等「等 syscall」被动让出); 纯用户态死循环时必须依赖它


- [ ] **Interrupt vector** / **中断向量**:
    + **设定**: CPU 收到中断/异常后需找到对应处理例程
    + **定义**: 按中断号索引的表 (或等价结构), 存放各 handler 入口地址; 硬件据此跳转
    + **结论**: 不同中断类型 (timer, 设备, 异常等) 经向量表分发到不同内核处理路径

---

## Processor Scheduling (Lec06)

- [ ] **Turnaround / Waiting / Response time** / **周转 / 等待 / 响应时间**:
    + **设定**: 评估 CPU 调度策略
    + **定义**:
        + **Turnaround**: $T_{\mathrm{completion}}-T_{\mathrm{arrival}}$
        + **Waiting**: 在 ready 队列等待的时间
        + **Response**: $T_{\mathrm{firstrun}}-T_{\mathrm{arrival}}$ (交互关键)
    + **注**: 吞吐 = 单位时间完成作业数; 公平含防饿死. 来源: `Lec06 scheduling` §3

- [ ] **FIFO / FCFS** / **先来先服务 (First-In-First-Out / First Come First Served)**:
    + **假设**: 非抢占; 按到达顺序
    + **结论**: 实现简单公平; 长作业在前导致护航 (convoy), 交互差
    + **来源**: 讲义 §7; OSTEP Ch.7

- [ ] **SJF** / **最短作业优先 (Shortest Job First)**:
    + **假设**: 非抢占; CPU burst 已知; 选最短就绪作业
    + **结论**: 同时到达时平均周转优于 FIFO (交换论证最优直觉); 长作业可能饿死; 不知长度时无法直接用
    + **来源**: 讲义 §8

- [ ] **HRRN** / **最高响应比优先 (Highest Response Ratio Next)**:
    + **假设**: 非抢占; $\mathrm{priority}=(W+S)/S$
    + **结论**: 兼顾短作业与老化防饿死
    + **来源**: 讲义 §9

- [ ] **STCF / PSJF** / **最短完成时间优先 (Shortest Time-to-Completion First)**:
    + **假设**: 抢占; 按剩余时间选
    + **结论**: 周转优于非抢占 SJF (可打断长作业); 响应未必好; 切换更多
    + **来源**: 讲义 §10

- [ ] **Round Robin (RR)** / **时间片轮转**:
    + **假设**: 抢占; 量子 $q$; ready 队列轮转
    + **结论**: 响应好; 周转常差; $q$ 过大→FIFO, 过小→切换开销主导
    + **来源**: 讲义 §11

- [ ] **MLFQ** / **多级反馈队列 (Multi-Level Feedback Queue)**:
    + **假设**: 多层优先级队列; 同层 RR; 动态优先级
    + **规则要点**: 新作业进顶层; 累计 allotment 用尽降级; 周期 boost 防饿死; 下层可更长 quantum
    + **结论**: 近似「不知长度的 SJF + 好响应」; 须防 gaming 与配参 (voo-doo constants)
    + **来源**: 讲义 §14; OSTEP Ch.8

- [ ] **Lottery Scheduling** / **彩票调度**:
    + **假设**: 票数表示份额; 每片随机抽赢家
    + **结论**: 长期按比例分享 CPU (概率意义); 实现简单; 短窗有偏差. 相关: ticket transfer/currency/inflation; Stride 为确定性替代
    + **来源**: 讲义 §15; OSTEP Ch.9

- [ ] **Cache affinity vs single-queue MP** `(自拟)` / **多核单队列问题**:
    + **假设**: 多核共享一个 ready 队列
    + **结论**: 锁争用差扩展; 作业跨核破坏缓存亲和. 对策: 每核队列 + work stealing
    + **来源**: 讲义 §16

---

## Threads & Concurrency Intro (Lec07)

- [ ] **Thread** / **线程**:
    + **设定**: 多线程进程内
    + **定义**: 可独立调度的执行序列; 私有 PC/寄存器/栈/TCB; 共享进程地址空间与多数进程级资源
    + **注**: 亦称轻量进程 (LWP); Linux 上常经 `clone` 实现
    + **来源**: `Lec07 thread concept`

- [ ] **Race condition** / **竞态条件**:
    + **假设**: 多线程并发访问并修改共享数据且无充分同步
    + **结论**: 结果依赖交错次序 → 非确定性; 典型如非原子 `x++` 丢更新
    + **来源**: 讲义 §5; OSTEP Ch.26

- [ ] **Critical section & Mutual exclusion** / **临界区与互斥**:
    + **设定**: 保护共享数据的代码块
    + **定义**: CS 内同一时刻至多一线程; 互斥 = 加锁串行化访问
    + **注**: 复杂 CS 需要锁等原语, 仅单次原子指令不够
    + **来源**: 讲义 §6–7

- [ ] **Pthread create/join/exit** / **POSIX 线程基本 API**:
    + **设定**: IEEE 1003.1c Pthreads
    + **定义**: `pthread_create` 建线程; `pthread_join` 等待结束; `pthread_exit` 终止自身 (不关进程级打开文件)
    + **来源**: 讲义 §4; OSTEP Ch.27

---

## Synchronization (Lec08)

- [ ] **Lock / Mutex** / **锁 / 互斥锁 (mutual exclusion)**:
    + **设定**: 多线程进入临界区前需互斥
    + **定义**: 锁有两种状态 available / held; `acquire` 获锁进入 CS, 不可得则阻塞或自旋; `unlock` 释放并唤醒一个等待者
    + **来源**: 讲义 §1; OSTEP Ch.28

- [ ] **Disabling interrupts** / **关中断**:
    + **设定**: 单核, 内核特权态
    + **结论**: CS 内关中断可防抢占; **多核无效** (他核线程仍可进 CS); 用户态不应使用
    + **来源**: 讲义 §2.1

- [ ] **Test-and-Set** / **测试并设置 (atomic instruction)**:
    + **定义**: 原子地「读旧值 + 写新值 + 返回旧值」; 可构造自旋锁 `while (TestAndSet(&flag,1)==1);`
    + **来源**: 讲义 §2.2, §3.1

- [ ] **Compare-and-Swap (CAS)** / **比较并交换 (atomic instruction)**:
    + **定义**: 仅当变量当前值 == expected 才更新为 new, 整条原子; Intel `CMPXCHG`; 可构造自旋锁 `while (CAS(&flag,0,1));`
    + **来源**: 讲义 §2.2, §3.2

- [ ] **Spin-lock / Busy waiting** / **自旋锁 / 忙等**:
    + **假设**: 多核共享内存; 用原子指令实现
    + **结论**: 等待时空转 `while` 循环, **浪费 CPU**; **无公平保证** (可能饥饿); 单核上自旋会死锁
    + **来源**: 讲义 §3.3

- [ ] **Pthread mutex** / **POSIX 互斥锁**:
    + **设定**: `pthread_mutex_t`; `PTHREAD_MUTEX_INITIALIZER` 静态初始化
    + **定义**: `pthread_mutex_lock` 获锁, 不可用时线程转 **blocked** (不占 CPU); `unlock` 唤醒一个; `destroy` 销毁
    + **来源**: 讲义 §4

- [ ] **Condition Variable (CV)** / **条件变量**:
    + **设定**: 等待某条件/事件成立, 不浪费 CPU
    + **定义**: 内部有等待队列; `pthread_cond_wait(&cond,&mutex)` 原子地释放 mutex + 入队 + 阻塞, 醒来后重新获 mutex 返回; `signal` 唤醒一个, `broadcast` 唤醒全部
    + **注 (Mesa 语义)**: 醒来后条件不一定仍成立, 须用 `while` 重新检查 (非 `if`)
    + **来源**: 讲义 §5; OSTEP Ch.30

- [ ] **Semaphore** / **信号量**:
    + **设定**: 含受保护整数变量, 仅经 `sem_wait`/`sem_post` 两条原子操作访问
    + **定义**: `sem_wait` (P/down) 减 1, <0 则入队阻塞; `sem_post` (V/up) 加 1, 有等待者则唤醒一个
    + **分类**: **binary** (0/1, 当互斥锁); **counting** (初值=资源池大小, 管多同类资源)
    + **来源**: 讲义 §7; OSTEP Ch.31

- [ ] **Producer-Consumer / Bounded Buffer** / **生产者-消费者 / 有界缓冲**:
    + **设定**: 有限缓冲池, 多生产者多消费者共享; 满→生产者等, 空→消费者等; 互斥 + FIFO
    + **CV 解法**: `while(count==MAX) cond_wait(notFULL,mv)` / `while(count==0) cond_wait(notEMPTY,mv)`; 用 `while` 非 `if` (Mesa)
    + **信号量解法**: `empty`(MAX) / `full`(0) / `mutex`(1); **先 wait 资源信号量, 再 wait mutex** (否则死锁)
    + **来源**: 讲义 §6, §7.4; 2023 Final Q5

- [ ] **Readers-Writers** / **读者-写者**:
    + **设定**: 读者并发读, 写者独占写, 至多一个写者
    + **解法**: `readcount` + `readMutex`(保护计数) + `semMutex`(保护数据); 第一个读者 `P(semMutex)`, 最后一个读者 `V(semMutex)`
    + **注**: 此解法偏向读者, 写者可能饥饿
    + **来源**: 讲义 §8

- [ ] **Order synchronization via semaphore** / **顺序同步 (自拟)**:
    + **设定**: 约束线程间执行顺序 (A 等 B/C 完成后再继续)
    + **方法**: 信号量初始化为 0; 完成方 `post`, 等待方 `wait` (等几次就 wait 几次)
    + **来源**: 讲义 §9

- [ ] **sem_wait 顺序错用 → 死锁** `(自拟)`:
    + **设定**: 生产者-消费者信号量解法
    + **假设**: 缓冲池满 (`empty=0`); Producer 先 `sem_wait(&mutex)` 再 `sem_wait(&empty)`
    + **结论**: Producer 持 mutex 等 empty 阻塞; Consumer 等 mutex 阻塞 → **循环等待 → 死锁**
    + **正确顺序**: 先 wait 资源信号量 (`empty`/`full`), 再 wait `mutex`
    + **来源**: 讲义 §11; Lec09 死锁四条件伏笔

- [ ] **Zemaphore** / **Zemaphore (用锁+CV 实现的信号量)**:
    + **设定**: 用一把锁 + 一个 CV + 一个 `value` 状态变量实现信号量
    + **定义**: `Zem_wait`: `lock; while(value<=0) cond_wait; value--; unlock`; `Zem_post`: `lock; value++; cond_signal; unlock`
    + **注**: 与 Dijkstra 原版差异 — `value` 不低于 0 (不靠负值记等待者数), 与 Linux 实现一致
    + **来源**: OSTEP Ch.31 §8

- [ ] **Thread throttling via semaphore** / **线程节流 (自拟)**:
    + **设定**: 限制同时进入某区域 (如内存密集区) 的线程数, 防止资源超用 (thrash)
    + **方法**: 信号量初值 = 最大并发数; 进入区 `sem_wait`, 出区 `sem_post`
    + **来源**: OSTEP Ch.31 §7

- [ ] **Atomicity violation** / **原子性违反**:
    + **定义**: 一段代码本应原子执行 (如「检查非 NULL + 使用指针」), 但执行时未强制原子 → 中间可被插入他线程修改 → 崩溃/竞态
    + **修复**: 加锁包住「检查 + 使用」整个区域
    + **来源**: OSTEP Ch.32 §2.1 (Lu et al. 研究中 ~半数非死锁 bug)

- [ ] **Order violation** / **顺序违反**:
    + **定义**: 两组内存访问期望顺序 A before B, 但执行时未强制 (如子线程入口用未初始化的指针)
    + **修复**: 用条件变量 + 状态变量 (或信号量) 强制顺序: 完成方 `signal`, 等待方 `while(state) wait`
    + **来源**: OSTEP Ch.32 §2.2 (Lu et al. 研究中 ~半数非死锁 bug)

- [ ] **trylock + livelock** / **trylock 与活锁**:
    + **设定**: 破坏「不可抢占」条件 — 用 `pthread_mutex_trylock` 试获, 失败则释放已有锁重试
    + **定义**: `trylock` 成功返回 0, 失败返回错误码 (不阻塞); 失败时 `unlock` 已持锁, `goto top` 重试
    + **活锁 (livelock)**: 两线程可能反复同时失败重试, 都在跑但无进展; 缓解: 重试前加随机延迟
    + **来源**: OSTEP Ch.32 §3.3

- [ ] **Lock-free CAS list insert** / **无锁 CAS 链表头插 (自拟)**:
    + **设定**: 用 CAS 实现无锁链表头插, 避免互斥锁
    + **方法**: `do { n->next = head; } while (CAS(&head, n->next, n) == 0);` — CAS 失败说明期间 head 被改, 用新 head 重试
    + **注**: 无锁 → 无死锁 (但仍可能活锁); 删除/查找的无锁实现复杂, 通用性受限
    + **来源**: OSTEP Ch.32 §3.3

---

## Deadlock (Lec09)

- [ ] **Deadlock** / **死锁**:
    + **定义**: 一组线程各持资源并互相等待对方资源, 全体阻塞, 系统停摆
    + **来源**: 讲义 §1; OSTEP Ch.32

- [ ] **Four necessary conditions for deadlock** / **死锁四必要条件**:
    + **假设**: 死锁发生当且仅当四条同时成立
    + **结论**: (1) **互斥 (mutual exclusion)** 资源独占; (2) **持有并等待 (hold-and-wait)** 持有资源同时等额外资源; (3) **不可抢占 (no-preemption)** 资源不能被强制夺走; (4) **循环等待 (circular-wait)** 环中每个线程等下一个线程持有的资源
    + **注**: 破坏任一条 → 死锁不可能发生 (预防的依据)
    + **来源**: 讲义 §4

- [ ] **Resource-allocation graph** / **资源分配图**:
    + **定义**: 节点=线程+资源, 边=hold/wait; 有环 → 循环等待成立 → 检测死锁的依据
    + **来源**: 讲义 §4.1, §7.1

- [ ] **Deadlock prevention** / **死锁预防**:
    + **定义**: 用限制性规则破坏四条件之一, 使死锁不可能发生
    + **破坏循环等待**: 资源全序, 按递增顺序申请 (缺点: 利用率低)
    + **破坏持有并等待**: 一次性申请全部资源 (缺点: 利用率低 + 可能饥饿)
    + **破坏互斥**: 仅对可共享资源 (多数资源不支持非互斥)
    + **破坏不可抢占**: 申请新资源不可得时释放已持有资源 (缺点: 回滚开销 + 可能饥饿)
    + **来源**: 讲义 §5

- [ ] **Deadlock avoidance** / **死锁避免**:
    + **定义**: 不破坏条件; 用全局资源需求知识调度, 使死锁不发生
    + **方法**: (1) 基于调度的避免 (保守, 资源利用不足); (2) 银行家算法
    + **来源**: 讲义 §6

- [ ] **Banker's Algorithm** / **银行家算法**:
    + **假设**: 事先知道各线程最大资源需求 (max); 当前已分配 (loan); claim = max − loan; available = total − Σloan
    + **结论**: 仅当授予后状态 **安全** 才分配; 安全 = 存在一种顺序能让所有线程依次完成并归还资源
    + **安全性检查**: 试分配 → 找 claim ≤ available 的线程, 假设完成归还 loan → 重复直到全部完成 (安全) 或找不到 (不安全)
    + **弱点**: 须事先知道 max; 线程/资源数须固定; 资源变化 (设备故障) 时失效
    + **来源**: 讲义 §6.2; 2023 Final Q6

- [ ] **Detection & Recovery** / **检测与恢复**:
    + **定义**: 允许死锁偶发, 周期检查资源分配图有无环; 恢复靠终止进程
    + **恢复**: 方案1 终止所有死锁进程; 方案2 逐个终止直到环消除; 牺牲者须从头或从 checkpoint 重启
    + **来源**: 讲义 §7

- [ ] **Dining Philosophers** / **哲学家就餐**:
    + **设定**: 五人围圆桌, 五叉, 吃面需同时拿左右两叉; 设计无死锁/无饥饿/高并发的解
    + **朴素解**: 全拿左叉 → 循环等待 → 死锁; 预防: 给叉编号按序拿
    + **来源**: 讲义 §3

