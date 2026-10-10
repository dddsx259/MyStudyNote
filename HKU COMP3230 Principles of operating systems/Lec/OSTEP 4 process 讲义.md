# OSTEP Ch.4 The Abstraction: The Process: 阅读讲义

- **来源**: `Lec/OSTEP 4 process.pdf` (13 页, 全覆盖; 原名 `cpu-intro.pdf`)
- **课程**: COMP3230B; 对应课件 `Lec/Lec04 process abstraction.pdf` 的 Required Reading
- **原书**: Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP) Ch.4, v1.10
- **在线**: [http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf](http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-intro.pdf)

> 本讲覆盖教材全部知识点 (含 TIP / ASIDE / Homework 说明). 概念与抽象为主; 无非定义数学命题. 术语首次标英文. 与课堂 slides 互补: slides 有状态机细节 / PCB 字段 / signal; 本章偏 **进程 (process)** 抽象定义, 状态转换表, **时间共享 (time sharing)** / **空间共享 (space sharing)**, xv6 `context` / `proc` 结构直觉. `fork` **细节留给 Ch.5.**

---



## 0. 一页速览


| 主题                   | 要点                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------- |
| Process 是什么          | **正在运行的程序 (running program)**; 程序本身是死的 (disk 上的指令 + 静态数据)                                |
| Crux                 | 物理 CPU (central processing unit) 很少 → 如何制造「几乎无限多 CPU」的幻觉?                                |
| 手法                   | **时间共享** 虚拟化 CPU: 跑一会儿 A, 停, 再跑 B                                                        |
| Mechanism vs Policy  | 机制 (mechanism) = how (如上下文切换 (context switch)); 策略 (policy) = which (如调度 (scheduling) 谁) |
| 机器状态 (machine state) | 地址空间 (address space) + 寄存器 (register) (含 PC / 栈指针) + I/O 信息 (如打开文件)                      |
| API 概览               | Create / Destroy / Wait / Suspend·Resume / Status (具体 API 见 Ch.5)                        |
| 创建过程                 | 加载代码与静态数据 → 建栈 (stack) / 堆 (heap) → 默认 fd → 跳到 `main()`                                  |
| 三态                   | Running / Ready / Blocked; + 创建初态 / Zombie 终态                                            |
| 内核结构                 | 进程表 (process list) / PCB (Process Control Block); xv6 的 `struct context` + `struct proc` |


---



## 1. 开篇: 程序 → 进程

**进程** 的非正式定义很简单: 它是一个 **正在运行的程序** [V+65, BH70].

- **程序 (program)** 本身是没有生命的东西: 躺在磁盘 (disk) (或现代系统的闪存 SSD) 上, 一堆指令 (instruction), 可能还有一些静态数据 (static data), 等着被唤醒.
- 是 **操作系统 (operating system, OS)** 把这些字节拿起来跑起来, 把程序变成有用的东西.

现实中往往要 **同时** 跑很多程序: 浏览器, 邮件, 游戏, 音乐播放器… 典型系统表面上可能同时有几十甚至上百个进程. 这样用起来方便: 不用操心「现在有没有空闲 CPU」, 直接跑程序就行. 于是挑战来了.

---



## 2. The Crux: 如何提供「许多 CPU」的幻觉?

**核心问题 (crux)**: 物理 CPU 只有少数几个, OS 如何提供「几乎用不完的 CPU」的幻觉?

OS 通过 **虚拟化 CPU (virtualizing the CPU)** 制造幻觉: 跑一个进程, 停掉它, 再跑另一个, 如此反复. 这种基本技术叫 CPU 的 **时间共享**: 用户可以跑任意多的并发 (concurrent) 进程; 潜在代价是性能 — 若必须共享 CPU, 每个进程都会跑得更慢.

要把 CPU 虚拟化做好, OS 需要:

1. **底层机制 (mechanisms)**: 低层方法或协议, 实现所需功能. 例: 后续会学的 **上下文切换** — 停下一个程序, 在同一 CPU 上启动另一个; 所有现代 OS 都用这套时间共享机制.
2. **高层策略 (policies)**: OS 内部做决策的算法. 例: 有多个可跑程序时, **调度策略 (scheduling policy)** 决定跑谁 — 常结合历史信息 (谁最近跑得多), 负载知识 (workload), 性能指标 (交互延迟 vs 吞吐 (throughput)) 等.



### TIP: 使用时间共享 (与空间共享)

- **时间共享**: 资源先被一个实体用一小会儿, 再被另一个用一小会儿… 从而被多方共享. 例: CPU; 也可用于网络链路 (network link).
- **空间共享 (space sharing)** 是对应面: 资源在 **空间上** 被切开分给使用者. 例: 磁盘空间 — 某块 (block) 一旦分给某文件, 通常在用户删除该文件前不会再分给别的文件.



### TIP: 分离策略与机制

许多 OS 的常见设计范式: **把高层策略与底层机制分开** [L+75].


|               | 回答的问题     | 例子                  |
| ------------- | --------- | ------------------- |
| **Mechanism** | **how**   | 如何做 context switch? |
| **Policy**    | **which** | 现在该跑哪个进程?           |


分开的好处: 改策略不必重做机制 → 一种 **模块化 (modularity)** (通用软件设计原则). Hydra 等研究系统较早强调这一点.

### Crux: 许多 CPU 的幻觉

- **自测 (Final 向)**: 单核机器上同时「看着」有浏览器与编译器在跑. (a) 这主要靠 time sharing 还是 space sharing? (b) context switch 是 mechanism 还是 policy? (c) 「交互进程优先于批处理」是 mechanism 还是 policy?
- **参考**: (a) CPU 上是 **time sharing** (磁盘文件占用才是典型 space sharing); (b) **mechanism** (how to stop/start); (c) **policy** (which to run). Final 概念题常考这种划分, 不要混成「调度 = 一次切换」.

---



## 3. §4.1 抽象: 进程 (The Abstraction: A Process)

OS 对「正在运行的程序」提供的抽象, 就叫 **进程**. 任意时刻, 可以通过清点它执行过程中触及或影响的系统部件, 来概括一个进程.

要理解进程由什么构成, 就要理解它的 **机器状态**: 程序运行时能读/改的东西. 哪些机器部件对这次执行重要?


| 组成部分              | 含义                                                                                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **内存 / 地址空间**     | 指令在内存里; 程序读写的数据也在内存里. 进程能寻址的那片内存叫它的 **地址空间**                                                                                                                     |
| **寄存器**           | 许多指令显式读/写寄存器, 显然是执行的一部分                                                                                                                                          |
| **特殊寄存器**         | **程序计数器 (program counter, PC)** (有时称 **指令指针 (instruction pointer, IP)**): 下一条要执行的指令; **栈指针 (stack pointer)** 与相关 **帧指针 (frame pointer)**: 管理函数参数, 局部变量, 返回地址所用的栈 |
| **持久存储 / I/O 信息** | 程序常访问持久存储设备; 例如当前打开了哪些文件的列表                                                                                                                                      |


---



## 4. §4.2 进程 API (Process API) (概览)

真实进程 API 细节放到后续章 (COMP3230 对应 OSTEP Ch.5 / 课堂 `fork`·`exec`). 这里先给出 **任何现代 OS 接口大致必须包含** 的能力:


| 类别                        | 作用                                                      |
| ------------------------- | ------------------------------------------------------- |
| **Create**                | 创建新进程. 在 shell 敲命令或双击图标时, OS 被调用来为你指定的程序建进程             |
| **Destroy**               | 强制销毁. 多数进程会自己跑完退出; 失控时用户需要能杀掉                           |
| **Wait**                  | 等待某进程停止运行                                               |
| **Miscellaneous Control** | 除杀死/等待外, 常见还有 **挂起 (suspend)** (暂时不跑) 与 **恢复 (resume)** |
| **Status**                | 查询状态信息: 已跑多久, 当前处于何种状态等                                 |


> 与 slides 对照: 课堂会展开 Unix `fork`+`exec`, Windows `CreateProcess`, zombie / `wait*`, signal. **本章只建立 API 分类直觉; 不要在此深挖** `fork` **返回值.**

---



## 5. §4.3 进程创建: 再细一点 (Process Creation)

程序如何变成进程? OS 怎样把程序拉起来跑?

### 5.1 加载 (Loading): 从磁盘程序到地址空间 (Figure 4.1)

OS 要做的第一件事: 把 **代码** 与 **静态数据** (如已初始化变量) 装入该进程的地址空间. 程序起初以某种可执行格式 (executable format) 存在磁盘上; 加载就是从盘读字节, 放到内存某处.

- **早期 / 简单 OS**: **急切加载 (eager loading)** — 跑之前一次性全部装入.
- **现代 OS**: 常 **惰性加载 (lazy loading)** — 执行中需要某段代码/数据时再装. 真正理解惰性加载需要后面的 **分页 (paging)** / **交换 (swapping)** (内存虚拟化). 现在只需记住: 跑之前 OS 至少要把关键程序比特从盘弄进内存.



### 5.2 栈, 堆, I/O 初始化

代码与静态数据就位后, OS 还要:

1. **分配运行时栈 (run-time stack / stack)**: C 用栈放局部变量, 函数参数, 返回地址. OS 还会用参数初始化栈 — 填好 `main()` 的 `argc` 与 `argv`.
2. **可能分配堆 (heap)**: C 里显式动态分配 (`malloc` / `free`) 用堆 (链表, 哈希表, 树等). 起初堆可以很小; 程序不断 `malloc` 时, OS 可能介入再给进程更多内存.
3. **I/O 相关初始化**: 如 UNIX 下默认三个打开的 **文件描述符 (file descriptor)**: 标准输入 / 输出 / 错误, 方便从终端读、往屏幕写. (持久化部分后文详谈.)



### 5.3 跳到入口 `main()`

上述就绪后, OS 最后一步: 从入口点开始执行, 即 `main()`. 通过某种专门机制 (下一章) 把 CPU 控制权交给新进程, 程序开始执行.

---



## 6. §4.4 进程状态 (Process States)

进程在某一时刻可处于不同 **状态** — 这一想法来自早期系统 [DV66, V+65]. **简化三态视图**:


| 状态               | 含义                                                                    |
| ---------------- | --------------------------------------------------------------------- |
| **Running (运行)** | 正在某个处理器上执行指令                                                          |
| **Ready (就绪)**   | 已可运行, 但此刻 OS **选择** 不让它跑                                              |
| **Blocked (阻塞)** | 做了某种操作后, 在某事件发生前 **不能** 再跑. 常见例: 向磁盘发起 I/O 请求后进入 blocked, 好让别的进程用 CPU |




### 6.1 状态转换图 (Figure 4.2)

```text
        Scheduled                Descheduled
  Ready ----------> Running ------------------> Ready
                      |  ^
           I/O: initiate |  | I/O: done
                      v  |
                   Blocked
```

要点:

- **Ready ⇄ Running**: 由 OS 裁量. Ready→Running = 被 **调度 (scheduled)**; Running→Ready = 被 **取消调度 (descheduled)** (如时间片用尽).
- **Running → Blocked**: 进程自己发起会等待的操作 (如 I/O).
- **Blocked → Ready**: 等待事件发生 (如 I/O 完成); 之后 **可能** 马上再进 Running, 取决于调度策略.



### 6.2 轨迹例 1: 纯 CPU (Figure 4.3)

两进程都只吃 CPU, 不做 I/O:


| Time | Process 0 | Process 1 | Notes          |
| ---- | --------- | --------- | -------------- |
| 1–4  | Running   | Ready     |                |
| 4 末  | 结束        |           | Process 0 done |
| 5–8  | –         | Running   | Process 1 随后结束 |


直觉: 单核上 **交替占有** CPU; 一个跑完另一个才从 Ready 变 Running (本例简化为顺序跑完).

### 6.3 轨迹例 2: CPU + I/O (Figure 4.4)


| Time | Process 0   | Process 1 | Notes                |
| ---- | ----------- | --------- | -------------------- |
| 1–3  | Running     | Ready     |                      |
| 3 末  | 发起 I/O      |           |                      |
| 4–6  | **Blocked** | Running   | P0 等 I/O, P1 用 CPU   |
| 7–8  | Ready       | Running   | I/O 完成; **未立刻切回 P0** |
| 8 末  |             | 结束        |                      |
| 9–10 | Running     | –         | P0 收尾                |


更细一点: Process 0 因读盘或等网络包等变为 blocked; OS 发现它不用 CPU, 就跑 Process 1. I/O 完成后 Process 0 回到 **ready**; Process 1 跑完后 Process 0 再跑完.

即便如此简单, OS 已在做决策:

1. P0 做 I/O 时改跑 P1 → 提高 **利用率 (utilization)**, CPU 不闲着.
2. P0 的 I/O 完成时 **不立刻切回** P0 — 好不好并不显然. 这类决策属于 **调度器 (scheduler)** (后续章).



### 自测: 状态机与利用率 (Final 向)

- **问**: 单核. P0 在 `read()` 上等磁盘; 磁盘完成后 P0 先进入哪一态? 若调度器选择让正在跑的 P1 继续跑完当前时间片, P0 会停在哪? 这与「I/O 一完成就立刻跑发行者」差在 **mechanism** 还是 **policy**?
- **参考**: I/O 完成 → **Ready** (不是直接 Running; Running 要经调度). 若 P1 继续, P0 停在 **Ready**. 「完成 I/O 后是否立即抢占」是 **policy**; Ready/Blocked/Running 之间的合法转换与「如何切换」才是 mechanism 侧. (Homework 的 `-I IO_RUN_IMMEDIATE` vs `IO_RUN_LATER` 正是在玩这个策略旋钮.)

---



## 7. §4.5 数据结构 (Data Structures)

OS 自身也是程序, 要用关键数据结构跟踪信息. 对进程而言:

- 某种 **进程列表 (process list)** (也称 **任务列表 (task list)**): 跟踪就绪进程等; 还要知道 **当前谁在跑**.
- 还要以某种方式跟踪 **blocked** 进程: I/O 完成时要唤醒 **正确** 的那个, 让它重新 Ready.



### ASIDE: 数据结构 — 进程列表 / PCB

能同时跑多程序的 OS, 都会有类似结构来登记系统中的运行程序. 存放单个进程信息的结构常称 **进程控制块 (Process Control Block, PCB)** — 说白了就是含该进程信息的 C 结构 (有时也称 **进程描述符 (process descriptor)**).

### 7.1 xv6 直觉: `context` 与 `proc` (Figure 4.5)

书中给出 xv6 内核 [CK+08] 里跟踪每进程信息的类型. 真实 Linux / macOS / Windows 的结构远更复杂, 可自行对照.

**寄存器上下文 (**`struct context`**)** — 停止后再启动进程时, xv6 要保存/恢复的寄存器 (Figure 4.5):

```c
// xv6 停下/重启进程时要保存与恢复的寄存器
struct context {
  int eip;   // 指令指针 (返回后从哪继续)
  int esp;   // 栈指针
  int ebx;   // 其余被调用者保存 / 切换时需保留的通用寄存器
  int ecx;
  int edx;
  int esi;
  int edi;
  int ebp;
};
```

- 进程被停下时: 寄存器内容 **写入** 这块内存.
- 恢复时: 把值 **装回** 物理寄存器 → 这就是日后详谈的 **上下文切换** 的核心直觉.

**进程状态枚举** (比三态更细):

```c
enum proc_state {
  UNUSED,    // 空闲槽, 可分配给新进程
  EMBRYO,    // 正在创建
  SLEEPING,  // 阻塞等待 (≈ Blocked)
  RUNNABLE,  // 就绪可跑 (≈ Ready)
  RUNNING,   // 正在 CPU 上跑
  ZOMBIE     // 已退出, 等父进程 wait 清理
};
```

对照简化三态: `RUNNING` ≈ Running; `RUNNABLE` ≈ Ready; `SLEEPING` ≈ Blocked; `EMBRYO` 一类是 **创建中初态**; `ZOMBIE` 是 **已退出尚未清理的终态**.

**完整** `struct proc` **(Figure 4.5)** — PCB 直觉:

```c
// xv6 为每个进程跟踪的信息 (寄存器上下文 + 状态等)
struct proc {
  char *mem;                  // 进程用户内存起点
  uint sz;                    // 进程内存大小
  char *kstack;               // 本进程内核栈底
  enum proc_state state;      // 当前状态 (上表)
  int pid;                    // 进程 ID
  struct proc *parent;        // 父进程
  void *chan;                 // 非零: 在该 channel 上 sleep
  int killed;                 // 非零: 已被标记杀死
  struct file *ofile[NOFILE]; // 打开文件表
  struct inode *cwd;          // 当前工作目录
  struct context context;     // 切到此处即可继续跑该进程
  struct trapframe *tf;       // 当前中断的 trap frame
};
```


| 字段               | 直觉                        |
| ---------------- | ------------------------- |
| `mem`, `sz`      | 进程内存起点与大小                 |
| `kstack`         | 该进程内核栈底                   |
| `state`          | 当前进程状态                    |
| `pid` / `parent` | 进程 ID; 父进程指针              |
| `chan`           | 非零则在该 channel 上睡眠 (sleep) |
| `killed`         | 非零表示已被标记杀死                |
| `ofile[]`, `cwd` | 打开文件; 当前目录                |
| `context`        | 切到此处即可继续跑该进程              |
| `tf`             | 当前中断的 trap frame          |




### 7.2 初态与 Zombie

除 Running / Ready / Blocked 外, 系统常有:

- **创建时初态**: 进程正在被创建.
- **终态 / Zombie (UNIX)**: 已退出但尚未清理. 作用: 让其他进程 (通常是创建它的 **父进程 (parent)**) 检查 **返回码 (return code)**, 看子进程是否成功 (UNIX 惯例: 成功常返回 0, 否则非 0). 父进程最后调用如 `wait()`, 既等待子进程结束, 也告知 OS 可以清理与该已消亡进程相关的数据结构.

(书中玩笑: zombie 相对好「杀」; 但手法与电影僵尸不同.)

### 自测: PCB / 进程表直觉 (Final 向)

- **问**: (1) PCB 与 process list 是什么关系? (2) 进程已 `exit` 但父进程尚未 `wait` 时, 为何还不能从进程表里把该条目彻底扔掉? (3) `context` 里的寄存器快照, 是给 **正在 Running 的** 进程用, 还是给 **被切走的** 进程用?
- **参考**: (1) process list / 进程表是「所有进程的登记册」; **每个条目** 常是一个 PCB (或指向 PCB 的指针). (2) 还要保留退出状态等给父进程查看 → **Zombie** 仍占一个 PCB 槽, 直到 `wait`* 后才清理. (3) 主要服务 **被停止 / 将被恢复** 的进程: Running 时真值在硬件寄存器里; 切走时写入 `context`, 再调度回来时写回. (Final 的 `fork` 题目在 Ch.5 / slides API 节练; 本章先把「状态 + PCB 还在」钉死.)

---



## 8. §4.6 Summary

- 已引入 OS 最基本的抽象: **进程** = 正在运行的程序.
- 接下来要进入细节: 实现进程所需的 **低层机制**, 以及智能调度所需的 **高层策略**.
- **机制 + 策略** 合在一起, 才能理解 OS 如何虚拟化 CPU.



### ASIDE: 关键进程术语 (Key Process Terms)

书末术语盒可当作本章 checklist:

- **Process**: 运行中程序的主要 OS 抽象. 任意时刻可由其状态描述: 地址空间中的内存内容, CPU 寄存器内容 (含 PC, 栈指针等), 以及 I/O 信息 (如可读写的打开文件).
- **Process API**: 程序可发起的与进程相关的调用; 典型含创建, 销毁及其他有用调用.
- **Process states**: 含 running, ready to run, blocked 等; 被调度/取消调度, 或等待 I/O 完成等事件, 会在状态间转换.
- **Process list**: 含系统中所有进程的信息; 每个条目有时称 PCB — 本质就是描述单个进程的结构.

---



## 9. Homework (Simulation) 说明

原 PDF 第 12–13 页为 **Homework (Simulation)**: 用 `process-run.py` 观察进程在「用 CPU」与「做 I/O」时状态如何变化 (详见该作业 README). **本章无课堂必做编号题**; 下列问题意在建立状态机与调度旋钮的直觉 (可选用 `-c` / `-p` 核对).


| #   | 实验意图 (简写)                                                            |
| --- | -------------------------------------------------------------------- |
| 1   | `-l 5:100,5:100`: 两进程皆 CPU 密集 → 想清 CPU **利用率** 该是多少                  |
| 2–3 | 一进程纯 CPU, 一进程只发 I/O; **交换两者顺序** 是否改变完成时间                             |
| 4–5 | `-S SWITCH_ON_END` vs `SWITCH_ON_IO`: I/O 等待期间是否允许切到别的进程             |
| 6–7 | `-I IO_RUN_LATER` vs `IO_RUN_IMMEDIATE`: I/O 完成后是否立刻跑回发行者; 哪个更易提高利用率 |
| 8   | 随机进程 (`-s` + `-l 3:50,3:50` 等): 综合预测轨迹, 并对比上述 `-S` / `-I` 组合         |


与上文自测呼应: `-S` / `-I` 改的是 **policy 旋钮**, 底层状态集合与切换能力仍是 **mechanism**.

---



## 与课堂 `Lec04 process abstraction` 对照


| OSTEP Ch.4                                    | 课堂 slides                                                 |
| --------------------------------------------- | --------------------------------------------------------- |
| Process = running program; machine state      | Process vs Program; 抽象四件套                                 |
| Time / space sharing; policy vs mechanism     | 后文调度章会反复用; 本章先立术语                                         |
| API 五类 (Create…) 概览                           | `fork`/`exec`/`CreateProcess`, `wait*`, signal 细节         |
| Eager vs lazy load; stack/heap/`main`         | 创建时 OS 步骤 (分配 PCB, Ready 队列)                              |
| 三态 + Figure 4.3/4.4 轨迹                        | new/ready/running/blocked/terminated 全图; suspend vs block |
| xv6 `proc` / `context`; process list = PCB 集合 | PCB 字段表; process table; ready/blocked list; `ps`/`pstree` |
| Zombie 用途一句话                                  | Zombie + `wait` 专节                                        |
| (无 signal)                                    | 信号专节 — 以 slides 为准                                        |
| Homework: `process-run.py`                    | 可用作状态机实验补充                                                |


**阅读顺序建议**: 先本讲建立「幻觉 / 三态轨迹 / PCB 直觉」, 再对照 slides 补 suspend·signal 与 API; `fork` **父子返回值与地址空间** 放到 Ch.5 阅读讲义 + Final 解析里的相关选择/判断题.