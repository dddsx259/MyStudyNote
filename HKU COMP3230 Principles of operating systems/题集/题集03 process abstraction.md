# 题集 — Process Abstraction

> 对齐: `Lec/Lec04 process abstraction 讲义.md`. 含 Mini-Lab 2–3 与进程/信号概念.
> 含: (1) 课件证明 (2) 练习题.

---

## 课件证明

### P1. 子进程退出后暂留 zombie 的合理性

- **陈述**: 子进程执行完毕进入 **terminated** 状态后, OS **仍保留 PCB** (常称 zombie), 直至父进程 `wait*` 取得退出信息.
- **证明**: 子进程须把 **termination status** (及资源用量等) 交回父进程; 父进程据此判断是否成功执行. 若 exit 后立即销毁 PCB 并释放全部记录, 父进程稍后调用 `waitpid` 将无法取得该状态. 故保留 terminated 条目是 **父–子同步协议** 所需; 父 `wait*` 后 OS 才彻底移除 zombie 并释放剩余资源.
- **来源**: `Lec/Lec04 process abstraction 讲义.md` §3 生命周期第 6 点, §8.2 Zombie

### P2. `fork()` 一次调用、两处返回

- **陈述**: `fork()` 在父进程返回 **子 PID** ($>0$), 在子进程返回 **0**; 同一调用点在代码中「走两次」.
- **证明**: `fork` **复制**调用进程 (新 PCB + 地址空间副本等), 父子从 **同一条返回路径** 继续执行. 内核在返回用户态前按角色写入不同返回值: 子进程寄存器/返回值槽为 0; 父进程为新建子 PID. 故不是函数物理返回两次, 而是 **两个进程各自完成一次返回**, 语义上对应「一次调用, 两个分支」.
- **来源**: `Lec/Lec04 process abstraction 讲义.md` §7.3 API (`fork` 复制进程); 与 Mini-Lab 3 观察一致

### P3. `SIGKILL` / `SIGSTOP` 不可捕获

- **陈述**: 进程不能对 `SIGKILL` 与 `SIGSTOP` 设置自定义 handler, 亦不能阻塞或忽略.
- **证明**: 若可捕获/忽略, 恶意或 buggy 进程可拒绝被终止或暂停, OS 无法保证 **最后手段** 的管控权. 课件将二者列为例外, 保证管理员/内核 `kill` 与 job control 仍有效.
- **来源**: `Lec/Lec04 process abstraction 讲义.md` §10.2 末尾

---

## 练习题

## Mini-Lab

### 1. Signal: 注册 SIGUSR1

- **题目**: 在 `lab/Mini-lab/Lab02 signal.c` 中: (1) 用 `signal()` 将 `SIGUSR1` 绑到 `sigusrHandler`; (2) handler 内终止进程; (3) 将 `getpid()` 写入 `pid.txt`. 另一终端用 `kill -USR1 $(cat pid.txt)` 测试. `SIGKILL` 能否用同样方式「处理」?
- **思路**: `signal(SIGUSR1, sigusrHandler)` + `exit`. 见 **P3**: `SIGKILL`/`SIGSTOP` **不可**捕获/阻塞/忽略.
- **来源**: `lab/Mini-lab/Lab02 signal 题目理解.md`, 讲义信号节

### 2. Process: fork / exec / wait

- **题目**: 完成 `lab/Mini-lab/Lab03 process.c`: `fork()`; 子进程 `execl("/bin/sleep","sleep","20",NULL)`; 父进程 `wait`. 子进程 `sleep 20` 期间用 `pstree -sp` 观察进程树 (SSH → bash → lab3 → sleep). 说明 `fork` 与 `exec` 返回值语义.
- **思路**: 子得 0, 父得子 PID (见 **P2**); `exec` 成功则不返回当前镜像. `wait` 收尸避免 zombie (若父不等).
- **来源**: `lab/Mini-lab/Lab03 process 题目理解.md`

---

## 概念 / 观察

### 3. Program vs Process

- **题目**: 区分 **program** 与 **process**. OS 为运行中程序维护哪四类抽象信息 (各举一例)?
- **思路**: 程序静态; 进程 = 运行实例. 四类: Memory, Resources in use, Execution state (PC/寄存器), Program code/data.
- **来源**: `Lec/Lec04 process abstraction 讲义.md` §1

### 4. 地址空间四区域

- **题目**: 画出典型用户进程地址空间: Text, Data, Heap, Stack 各放什么? 局部变量与 `malloc` 分别在哪?
- **思路**: Text=代码; Data=全局/静态; Heap=动态; Stack=局部/参数/返回地址.
- **来源**: 讲义 §2

### 5. 进程状态与 zombie

- **题目**: 列出 new / ready / running / blocked / terminated 含义. 为何 terminated 子进程可能成 **zombie**? 父进程应如何清理?
- **思路**: 见 **P1**; 父调 `wait`/`waitpid`.
- **来源**: 讲义 §3, §8.2

### 6. 同步 vs 异步信号

- **题目**: 各举讲义中的一例: **同步**信号如何产生? **异步**信号如何投递? 默认/捕获/忽略/屏蔽指什么?
- **思路**: 同步例: NULL 解引用 → `SIGSEGV`. 异步例: `kill(pid, SIGKILL)`. 捕获=handler; 忽略=丢弃; 屏蔽=暂不收.
- **来源**: 讲义 §8 信号
