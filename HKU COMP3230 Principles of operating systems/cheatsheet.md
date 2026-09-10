# COMP3230 Cheatsheet

> 词条/概念速查; 对话中学到的内容会增量追加.

---

## 课程组织

+ **Assessment**:
    + Labs 4% + PS 18% + PA 28% + Final 50% (open-book, 无 midterm)
+ **Slip days**:
    + 5 天额度; 单次 PS/PA 最多 +3 天; 超额每天 −20%
+ **OSTEP**:
    + *Operating Systems: Three Easy Pieces* (必读 online textbook)

## 名词

+ **Mechanism vs policy** / **机制 vs 策略**:
    + mechanism: 能做什么; policy: 如何选择/分配
+ **PA / PS**:
    + Programming Assignment / Problem Set
+ **Kernel / User mode**:
    + 内核态可执行任意指令; 用户态仅子集; 系统调用触发 mode switch (trap / return-from-trap)
+ **System call**:
    + 应用向 OS 请求服务的 API; 集合即 OS 服务接口
+ **OS architectures**:
    + Monolithic / Layered / Microkernel / Modular (现代常为单体 + 动态内核模块)
+ **Process**:
    + 执行中的程序实例; 含地址空间 (Text/Data/Heap/Stack) + 资源 + 状态
+ **PCB**:
    + Process Control Block; PID / PC / 寄存器上下文 / 调度与内存信息等
+ **Process states**:
    + new / ready / running / blocked / terminated (zombie)
+ **fork / exec / wait**:
    + Unix 创建: fork 复制进程; exec 替换映像; wait* 收子进程状态并清 zombie
+ **Zombie**:
    + 已退出但 PCB 仍保留给父进程 wait
+ **Signal**:
    + Unix 软件中断式通知; sync (本指令触发) / async (外部); SIGKILL/SIGSTOP 不可捕获
+ **Virtualization (OSTEP)**:
    + 把物理 CPU/内存等变成易用的虚拟形态; OS ≈ 虚拟机 + 系统调用库 + 资源管理器
+ **Three Easy Pieces**:
    + Virtualization (CPU/memory) / Concurrency / Persistence (devices + file system)
+ **Trap / return-from-trap**:
    + 系统调用时提升到内核态; 返回时降回用户态
