# OSTEP Ch.2 Introduction to Operating Systems: 阅读讲义

- **来源**: `Lec/OSTEP 2 introduction.pdf` (19 页, 全覆盖; 原名 `intro.pdf`)
- **课程**: COMP3230B; 对应课件 `Lec/Lec03 introduction.pdf` 的 Required Reading
- **原书**: Arpaci-Dusseau, *Operating Systems: Three Easy Pieces* (OSTEP) Ch.2, v1.10
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/intro.pdf

> 本讲覆盖教材全部知识点 (含历史 aside / homework 说明). 概念与设计目标为主; 无非定义数学命题. 术语首次标英文. 与课堂 slides 互补: slides 偏架构分类, 本章偏 **虚拟化 (virtualization)** 三大主题直觉.

---

## 0. 一页速览

| 主题 | 要点 |
|---|---|
| 程序 (program) 在跑什么 | 反复 fetch → decode → execute (冯·诺依曼模型 (von Neumann model)) |
| OS 是什么 | 让系统正确、高效、易用的软件体; 又称 supervisor / master control program (旧名) |
| 核心手法 | **虚拟化**: 把物理资源 (physical resource) 变成更通用、强大、易用的虚拟形态 → OS 有时称 **虚拟机 (virtual machine)** |
| 接口 (interface) | 数百个 **系统调用 (system call)** ≈ 给应用 (application) 的标准库 (standard library) |
| 另一角色 | **资源管理器 (resource manager)** |
| 三大主题 | CPU 虚拟化 / 内存 (memory) 虚拟化 / **并发 (concurrency)**; 加上 **持久化 (persistence)** |
| 设计目标 | 抽象 (abstraction)、性能 (performance) (低开销 (overhead))、保护 (protection)/隔离 (isolation)、可靠性 (reliability); 还有能效 (energy efficiency)、安全 (security)、移动性 (mobility) 等 |
| 历史线索 | 库 (library) → 保护与 syscall → 多道程序 (multiprogramming) → UNIX → PC 回退再回归 → Linux |

---

## 1. 程序如何运行 (开篇)

运行中的程序做一件很简单的事: **执行 (execute) 指令 (instruction)**. 处理器 (processor) 每秒数百万乃至数十亿次:

1. 从内存 **取指 (fetch)**
2. **译码 (decode)**
3. **执行 (execute)** (加减、访存 (memory access)、条件、跳转等)

然后下一条, 直到程序结束. 这就是 **冯·诺依曼计算模型 (von Neumann model)** 的基础.

现代 CPU 底层会乱序 (out-of-order)、并行 (parallel) 执行多条指令, 但程序通常仍假设指令 **看似** 一次一条、按序执行.

程序运行时, 还有大量「野事」发生, 目的是让系统好用. 负责这些的软件体就是 **操作系统 (operating system, OS)**: 让系统以正确、高效、易用的方式运转.

**预备阅读建议** (书中点名): Patt & Patel [PP03]; Bryant & O'Hallaron [BOH10].

---

## 2. The Crux: 如何虚拟化资源

**核心问题 (crux)**: OS **如何** 把资源虚拟化?

- **Why** 不是重点 (答案显然: 更好用)
- 关注 **how**: 用什么 **机制 (mechanism)** 与 **策略 (policy)**? 如何高效? 需要何种硬件 (hardware) 支持?

书中用 shaded box 标出各章要解决的 crux; 章内细节给出解法或解法的基本参数.

### OS 的三重说法

1. **虚拟化**: 把物理资源 (处理器、内存、磁盘 (disk) 等) 变成更通用、强大、易用的虚拟形态 → 有时把 OS 叫做 **虚拟机**
2. **接口 / 标准库**: 导出数百个系统调用, 供运行程序、访存、访问设备等
3. **资源管理器**: 多程序共享 CPU / 内存 / 设备时, 由 OS 管理, 目标可为效率、公平或其他

早期别名: **supervisor**; 甚至 **master control program** (书中玩笑: 见电影 *Tron*).

### Crux: 如何虚拟化资源?

- **自测**: 用一句话区分 mechanism 与 policy, 并各举 CPU 虚拟化一例.
- **参考**: mechanism 如 trap, 上下文保存 (context save); policy 如「时间片 (time slice) 用尽后调度 (scheduling) 谁」. why 显然是为了好用, 本章 focus 在 how.

---

## 3. §2.1 虚拟化 CPU (Virtualizing The CPU)

### 例子 `cpu.c` (Figure 2.1)

循环: `Spin(1)` 空转 (spin) 约 1 秒 → `printf` 打印命令行 (command line) 字符串 → 永远重复. `Ctrl-c` 可终止前台 (foreground) 程序.

教材完整程序 (官方 `ostep-code/intro/cpu.c`; `Spin` / `common.h` 见同仓库 `include/`):

```c
#include <stdio.h>
#include <stdlib.h>
#include "common.h"   // 提供 Spin(seconds): 忙等约指定秒数

int main(int argc, char *argv[])
{
    if (argc != 2) {                          // 必须带一个要反复打印的字符串
        fprintf(stderr, "usage: cpu <string>\n");
        exit(1);
    }
    char *str = argv[1];                      // 如 "A" / "B"

    while (1) {                               // 故意死循环: 持续「占用」CPU
        printf("%s\n", str);                  // 打印一次参数
        Spin(1);                              // 空转约 1s, 放慢输出便于观察交错
    }
    return 0;                                 // 正常达不到; Ctrl-c 杀进程
}
```

| 要点 | 说明 |
|---|---|
| 编译运行 | 需与 `common.h` 一起编; 例: `./cpu A` |
| 单实例 | 输出规则地每秒一行 `A` |
| 多实例 | `./cpu A & ./cpu B & ...` 时输出交错 → 见下 |

单实例运行很无聊; 若一次启动多个:

```text
./cpu A & ./cpu B & ./cpu C & ./cpu D &
```

输出交错出现 A/B/C/D. **只有一个 (或少量) 物理 CPU**, 却仿佛有很多程序同时在跑.

这就是 **CPU 虚拟化**: OS (借助硬件) 制造「有极多虚拟 CPU」的幻觉, 让许多程序 **看似** 同时运行. 本书第一大部分即围绕此主题.

要启动/停止/指定跑谁, 需要与 OS 通信的 **API**. 多程序同时想跑时, **谁先跑** 由 OS 的 **policy** 回答 → 再次体现资源管理器角色.

(`&` 在 zsh 等 shell 中把作业 (job) 放到后台 (background); 不同 shell 细节略异.)

### 示例 `cpu.c` — 多进程「同时」跑

- **实验**: 按 Figure 2.2 启动多个 `./cpu` 实例 (shell 后台 `&`). 观察输出交错.
- **讲解**: 物理 CPU 很少, OS+硬件制造多虚拟 CPU 幻觉; 谁先跑是 scheduling policy 问题.

---

## 4. §2.2 虚拟化内存 (Virtualizing Memory)

### 物理内存 (physical memory) 模型

内存可看成字节数组: 读要给地址 (address); 写还要给数据. 程序运行时不断访存 (数据结构 (data structure) 的 load/store); **每条指令本身也在内存里**, 取指也要访存.

### 例子 `mem.c` (Figure 2.3–2.4)

教材完整程序 (官方 `ostep-code/intro/mem.c`):

```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include "common.h"   // Spin; 另需 assert 头 (书/仓库版可能含 assert.h)

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: mem <value>\n");
        exit(1);
    }
    int *p;
    p = malloc(sizeof(int));                  // 在堆上分配一个 int 的空间
    assert(p != NULL);
    printf("(%d) addr pointed to by p: %p\n",
           (int) getpid(), p);                // 打印本进程 PID + 指针的虚拟地址
    *p = atoi(argv[1]);                       // 把命令行初值写入 *p
    while (1) {
        Spin(1);
        *p = *p + 1;                          // 每秒自增一次
        printf("(%d) value of p: %d\n", getpid(), *p);
    }
    return 0;
}
```

| 观察 | 含义 |
|---|---|
| 单进程 | 地址如 `0x200000`, 值 1,2,3,… 递增 |
| 两进程同时跑 | 两者打印的 **虚拟地址 (virtual address)** 可以 **相同**, 但各自独立递增 → 仿佛每进程有私有内存 |

实际上: OS 在做 **内存虚拟化**. 每进程有私有 **虚拟地址空间 (virtual address space)** (常简称 address space), 由 OS 映射 (map) 到物理内存. 一进程内的访存不影响其他进程 (或 OS) 的地址空间; 对进程而言仿佛独占物理内存, 现实却是共享资源由 OS 管理.

注: 演示需关闭 **地址空间随机化 (address-space randomization)** (安全特性, 可防部分攻击; 书中建议自行了解, 勿鼓励搞破坏).

### 示例 `mem.c` — 相同虚拟地址

- **实验**: 单进程与双进程各跑一份, 对比打印的地址与计数是否独立.
- **讲解**: 相同虚拟地址可映射到不同物理页 (physical page) → **地址空间隔离**; 演示常需关闭 ASLR (书中 aside).

---

## 5. §2.3 并发 (Concurrency)

**并发**: 在同一程序里「同时做很多事」时出现的一整类问题. 问题最初出现在 OS 自身 (在进程间切换); 现代 **多线程 (multi-threaded)** 程序同样面对.

### 例子 `threads.c` (Figure 2.5)

教材完整程序 (官方 `ostep-code/intro/threads.c`; `Pthread_*` 为大写 wrapper, 见 `common_threads.h`):

```c
#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "common_threads.h"

volatile int counter = 0;                     // 两线程共享的全局计数; volatile 防过度优化
int loops;

void *worker(void *arg) {                     // 每个工人线程的入口
    int i;
    for (i = 0; i < loops; i++) {
        counter++;                            // 看似一行, 机器上常是 load→inc→store, 非原子
    }
    return NULL;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "usage: threads <loops>\n");
        exit(1);
    }
    loops = atoi(argv[1]);
    pthread_t p1, p2;
    printf("Initial value : %d\n", counter);
    Pthread_create(&p1, NULL, worker, NULL);  // 创建线程 1
    Pthread_create(&p2, NULL, worker, NULL);  // 创建线程 2
    Pthread_join(p1, NULL);                   // 等待两线程都跑完
    Pthread_join(p2, NULL);
    printf("Final value   : %d\n", counter);  // 期望 2*loops; 大 loops 时常更小
    return 0;
}
```

| `loops` | 常见现象 |
|---|---|
| `1000` | 终值常为 2000 (期望 `2N`) |
| `100000` | 终值可能是 143012、137298 等 **错误且不稳定**; 有时又碰巧正确 |

### Crux: 如何构造正确的并发程序?

同地址空间内多线程并发时, 如何写正确程序? OS 需提供什么原语 (primitive)? 硬件提供什么机制? 如何用来解并发问题?

**原因直觉**: `counter++` 在机器上通常是三条指令 (load → increment → store), **非原子 (not atomic)**. 交错 (interleaving) 执行会丢更新. 本书第二部分详论.

(书中 `Pthread_*` 大写是作者 wrapper, 实际调用小写 `pthread_create` 等.)

### 示例 `threads.c` — 并发正确性 (Figure 2.5)

- **实验**: `loops=1000` vs `loops=100000`, 看 `Final value` 是否稳定为 `2*loops`.
- **讲解**: `counter++` 非原子 (load / add / store), 交错会丢更新; 对应 Crux「如何构造正确并发程序」— 全书第二部分主题.

---

## 6. §2.4 持久化 (Persistence)

- DRAM 等内存 **易失 (volatile)**: 断电/崩溃 (crash) 则数据没
- 需要硬件 + 软件 **持久存储 (persistent storage)**: 硬盘 (HDD)、固态盘 (SSD) 等 **I/O 设备 (device)**
- OS 中管理磁盘的软件通常叫 **文件系统 (file system)**: 可靠、高效地把用户文件存到盘上

与 CPU/内存抽象不同: OS **通常不为每个应用造私有虚拟磁盘**; 用户往往要 **共享文件**. 例: 编辑器写 `.c` → 编译器 (compiler) 读入生成可执行文件 (executable) → 再运行.

### 例子 `io.c` (Figure 2.6)

三次系统调用: `open` → `write` → `close` (官方仓库还多了 `fsync`). 请求路由到文件系统. 完整程序 (官方 `ostep-code/intro/io.c`):

```c
#include <stdio.h>
#include <unistd.h>
#include <assert.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <string.h>

int main(int argc, char *argv[]) {
    // 只写打开 /tmp/file; 无则创建; 有则截断为空
    // 权限: 属主可读可写 (S_IRUSR | S_IWUSR)
    int fd = open("/tmp/file", O_WRONLY | O_CREAT | O_TRUNC, S_IRUSR | S_IWUSR);
    assert(fd >= 0);                          // open 失败返回 -1; 成功得文件描述符 fd

    char buffer[20];
    sprintf(buffer, "hello world\n");         // 准备要写的字节 (含换行)
    int rc = write(fd, buffer, strlen(buffer));
    assert(rc == (strlen(buffer)));           // 要求一次写满; 真实代码常需循环

    fsync(fd);                                // 尽量把缓冲刷到持久存储 (教材/仓库版有此调用)
    close(fd);                                // 关闭 fd, 释放打开文件表项
    return 0;
}
```

| 步骤 | 含义 |
|---|---|
| `open` | 得到 `fd`; 用户态不直接碰磁盘 |
| `write` | 经文件系统写数据; 返回实际写入字节数 |
| `fsync` | 降低「已 write 但未落盘」的窗口 (仍非万能) |
| `close` | 释放资源; 进程退出时内核也会关未关的 fd |

运行后 `/tmp/file` 内容应为一行 `hello world`.

**课内要点**:

1. **用户态 (user mode) 不直接碰磁盘**. 程序只调系统调用; 真正布局盘块、发设备命令由 **OS + 文件系统 (+ 设备驱动)** 完成 → 「系统调用 ≈ 标准库」.
2. 之后读写靠 **`fd`**, 不再反复传路径.
3. 三 flag `O_WRONLY|O_CREAT|O_TRUNC` 合用很常见: 「写、没有就建、有就清空再写」.

文件系统实际写盘很繁琐: 决定数据落在盘上何处、维护元数据 (metadata)、对设备发 I/O. **设备驱动 (device driver)** 懂具体设备接口.

性能上常先 **延迟写 (delayed write)、批处理 (batch processing)**; 为应对写过程中崩溃, 常用 **journaling (日志)** 或 **copy-on-write (写时复制)** 等写协议 (write protocol), 仔细排序写盘以便恢复. 数据结构从简单链表 (linked list) 到复杂 B-tree 等.

### 示例 `io.c` — 持久化最小路径

- **实验**: 编译运行后 `cat /tmp/file`, 确认内容为 `hello world`.
- **讲解**: `open`→`write`→`close` 是用户可见的持久化接口; 磁盘布局 / 驱动 / journaling 对应用隐藏.

### Crux: 如何持久存储数据?

文件系统负责持久数据. 正确性要什么技术? 高性能要什么机制与策略? 硬件/软件失败下如何可靠?

### Crux: 持久化与文件系统

- **思考题**: 为何 OS 通常不为每应用造「私有虚拟磁盘」, 却为 CPU/内存 造私有抽象?
- **参考**: 文件常需 **共享** (编译链: `.c` → 可执行文件); 磁盘管理侧重命名空间 (namespace), 权限 (permission), 性能 (延迟写, journaling 等).

---

## 7. §2.5 设计目标 (Design Goals)

OS 做: 虚拟化物理资源、处理并发、持久保存文件. 设计时要有目标以便做 **权衡 (trade-off)**.

| 目标 | 含义 |
|---|---|
| **抽象 (abstraction)** | 方便易用; CS 处处依赖抽象 (高级语言 (high-level language)、汇编 (assembly)、门电路 (logic gate) 分层等) |
| **高性能 / 低开销** | 虚拟化值得, 但不能任意贵; 开销含额外时间 (指令) 与空间 (内存/磁盘) |
| **保护 (protection)** | 应用之间、应用与 OS 之间; 恶意或意外行为不伤害他者/OS |
| **隔离 (isolation)** | 保护的核心原则: 隔离进程 |
| **可靠性 (reliability)** | OS 尽量不停机; OS 挂则应用全挂; 现代 OS 代码庞大, 可靠性仍是研究热点 |
| 其他 | **能效**; **安全** (保护的延伸); **移动性** (小设备) 等 — 场景不同目标权重不同 |

原则常跨设备通用.

---

## 8. §2.6 简史 (Some History)

更丰富材料见 Brinch Hansen [BH00].

### 早期: 几乎只是库

- OS 起初主要是常用函数库 (如底层 I/O API), 方便开发者
- 大型机 (mainframe) 上常由人工操作员一次跑一个程序; **批处理 (batch processing)**: 作业成批提交. 机器太贵, 不宜交互闲置

### 超越库: 保护

- OS 代表系统跑的代码特殊 (控制设备), 不能当普通库随便调
- 若任意应用可读磁盘任意处 → 无隐私; 文件系统不宜纯库实现
- **系统调用** 思想 (Atlas 等先行): 特殊硬件指令 + 硬件状态, 使进入 OS 成为受控过程

**系统调用 vs 过程调用 (procedure call)**:

- 系统调用转入 OS, 同时 **提升硬件特权级 (privilege level)**
- 应用跑在 **用户态 (user mode)**: 硬件限制 (通常不能随意发磁盘 I/O、访问任意物理页、发包 (send packets) 等)
- 经 **trap** 等特殊指令: 硬件转到预设 **trap handler**, 并升到 **内核态 (kernel mode)**; OS 可满权限操作
- 完成后经 **return-from-trap** 回到用户态与原中断 (interrupt) 点

### 多道程序时代 (Multiprogramming)

- 小型机 (minicomputer) 降价 → 更多人能碰计算机 → 创新加速
- **多道程序设计**: 内存中装多个作业并快速切换, 提高 CPU 利用率 (utilization); I/O 慢时切到别的作业
- 推动: **内存保护 (memory protection)**、中断下的 **并发正确性** 等
- 实践上重大进展: **UNIX** (Ken Thompson, Dennis Ritchie, Bell Labs); 吸收 Multics 等思想但更简; 源码 (source code) 磁带流传

### Aside: UNIX 的重要性

- 小而强的程序可组合; **shell** 与 **管道 (pipe)** 做元级编程 (metaprogramming), 如 `grep foo file.txt | wc -l`
- 对程序员友好, 带 C 编译器; 早期近乎开源分发
- 内核小、可读 → 他人可改; Berkeley **BSD** (Bill Joy 等) 推进 VM、文件系统、网络 (network); Joy 后参与创办 Sun
- 商业化与法律纠纷曾拖慢传播 (SunOS, AIX, HPUX, IRIX 等); Windows 崛起于 PC

### 现代与 PC

- PC (Apple II, IBM PC) 普及桌面; 早期 OS 曾 **倒退**: 如 DOS 弱内存保护; 早期 Mac OS 协作式调度 (cooperative scheduling), 死循环 (infinite loop) 可拖死整机
- 后来桌面重新吸收小型机教训: macOS 以 UNIX 为核心; Windows NT 起大幅前进; 手机 (如 Android/Linux) 更像 1970s 小型机 OS 而非 1980s PC

### Aside: Linux

- Linus Torvalds 自写 UNIX 风格系统 (借思想不借受版权纠缠的代码基), 结合 GNU 工具 → **Linux** 与现代开源 (open source) 运动
- 互联网公司广泛用 Linux; Android 亦基于 Linux; Jobs 把 NeXTStep (UNIX 系) 带到 Apple → 桌面也有 UNIX

---

## 9. §2.7 Summary

- 今日 OS 让系统相对易用; 几乎都受本书将讨论的发展影响
- 本书 **不** 深讲: 网络栈 (network stack)、图形设备 (graphics device)、深层安全课内容 (会涉及保护与文件权限层面的安全)
- **会** 覆盖: CPU/内存虚拟化基础、并发、经设备与文件系统的持久化

文末 Homework: 仿真 (simulation) 作业 + 与真实 UNIX/C 交互的小实验; 推荐配合更大项目 (见 ostep-projects). 环境: Linux/macOS 等 + `gcc` + Python + 正经编辑器.

### Homework 节 (meta)

原 PDF 第 19 页 **Homework** 节说明全书作业分「仿真」与「真实 UNIX/C 代码」两类, 并指向 [ostep-projects](https://github.com/remzi-arpacidusseau/ostep-projects); **本章无编号 Exercise 题单**. 文中 **Crux 框** 与 **Figure 示例程序** 对应的自测/实验见各节末 (建议在 Linux/macOS + `gcc` 环境做).

- **仿真类**: 用简单程序近似系统行为 (如磁盘请求延迟), 便于探索「若硬件更快会怎样」; 结果须警惕模型遗漏.
- **代码类**: 在真实 UNIX 上测/写小程序; 与 COMP3230 Lab/PA 技能衔接. Ch.2 本身不布置具体仿真题号.

---

## 与课堂 `Lec03 introduction` 对照

| OSTEP Ch.2 | 课堂 slides |
|---|---|
| 虚拟化 CPU/内存 + 例子 | 进程/内存管理「要回答的问题」 |
| 并发 + `counter++` 非原子 | 并发与同步 (synchronization) 原语职责 |
| 持久化 + 文件系统 | 文件管理 (file management) 职责 |
| 设计目标 | Goals of OS |
| syscall / user·kernel mode 历史 | 同主题的机制页 |
| 三大主题叙事 | 架构 (architecture) 分类 (monolithic 等) 更细 |
