# 给 AI: COMP3230 命题重点与以后怎么写材料

> 读者是以后的 course-learning / 讲义生成, 不是给学生背的 cheatsheet.
> 依据: `test&quiz/Final01 2023-12-13.pdf` (2023 Final, 开卷 3 小时, 100 分) + `docs/Required Readings.html` + 当前 `Lec/` slides.
> 学生 todo **不要** 因为这份分析自动加入 Final/Quiz. 等用户点名再列入.

## 2023 Final 题型 (按分)

| 题 | 分 | 考点 | 对应以后的 slides / OSTEP |
|---|---|---|---|
| Q1 选择 | 10 | TLB miss 重执行同一条指令; 非法访存是硬件 trap 再由 OS 处理; 碎片不是技术; 替换看 reference bit; `fork` 后值与虚拟地址 | Virtualize CPU; Address translation / TLB; Process API |
| Q2 判断+理由 | 10 | 单核解法不能自动拿到多核; 写者独占; `sem_wait/post` 不必同线程; cond 不记历史信号; sem 记计数 | Concurrency, locks, CV, semaphores |
| Q3 模拟 | 20 | 4 帧, LFU 与 Clock, 平局换最老页, 要画出每步内存 | Page replacement policies (OSTEP Ch.22) |
| Q4 计算 | 15 | 由 PTE 位数推出页大小, 级数, VPN 切分; TLB 项宽度 | Multi-level paging, TLB (OSTEP Ch.20, Ch.19) |
| Q5 改代码 | 10 | 有界缓冲, 一次放/取 $k$ 个; `while` + broadcast | CV (OSTEP Ch.30) |
| Q6 银行家 | 20 | Need, Available, 安全序列; 请求要试分配后再判安全; 新进程独立于上一问 | Deadlock avoidance (课上 deadlock; OSTEP Ch.32 偏 bug, 银行家以 slides 为准) |
| Q7 文件系统算 | 15 | FAT 占多少块, bitmap 占多少块, 删中间块的磁盘 I/O 次数 | Files / FS implementation (OSTEP Ch.39–40) |

选择和判断分不高, 但概念要准. **大分在: 页替换手算, 多级页表/TLB 位数, 银行家, 同步改代码, FAT/bitmap 算术.**

## 写讲义时要重点写清的 slides 内容

当前已有 slides 里, Final 真正会考、且容易只写定义不写「能做题」的部分:

1. **Virtualize CPU** (`Lec/05`): trap 之后是重做本条还是下一条; TLB miss / page fault / syscall / timer / 除零的分类; mode switch 不等于 context switch.
2. **Process** (`Lec/04`): `fork` 复制地址空间, 父子虚拟地址相同, 变量副本独立; 返回值谁是 0.
3. 尚未入库、但 2023 卷子已考, slides 一到就按下面标准写, 不要只翻译定义:
   - **Scheduling**: 策略对比和量化 (本卷没有大题, 但是课程主线; 讲义仍要有可算的例子).
   - **Locks / CV / semaphore**: 每个原语「记不记历史状态」, 谁 wait 谁 signal, Mesa `while`, 多核不能只关中断.
   - **Readers-writers, bounded buffer**: 要有能改的代码骨架, 不是只讲故事.
   - **Deadlock**: 银行家算法要有完整数字例子 (Max, Allocation, Need, Available, 试分配).
   - **Paging / TLB / multilevel**: 从 PTE 宽度和物理地址位数推出 offset 和每级 index; TLB 项 = VPN + PFN + 控制位.
   - **Page replacement**: 至少会逐步演示 LRU, Clock, LFU; 写明平局规则 (本卷: 最老的页).
   - **File system**: 块数, FAT 项宽, bitmap 位数, 「元数据已在内存时删一块要几次写回」.

课程导论和 C 语法 **不是** Final 的得分点. C 只作为读 `fork` / pthread 代码的工具.

## OSTEP 本地 PDF

- 目录: `Lec/textbook/ostep/` (2026-09-21 从 https://pages.cs.wisc.edu/~remzi/OSTEP/ 下的章节 PDF, 约 68 个文件).
- 官方希望链接到网站; 这里留本地副本是为了离线写讲义. 不要把这 68 章全部写进学生 todo.
- **todo 粒度 (用户 2026-10-07)**: 已列入的 slides / OSTEP **一节或一章一条**, **不要**按 part / 小节再拆子条. Tut / PS / PA / Lab 仍按题拆.
- **Lec 对齐副本**: 拷到 `Lec/` 供阅读时命名为 **`OSTEP {章} {title}.pdf`**, 讲义为 **`OSTEP {章} {title} 讲义.md`**. **不要**写成 `Lec{NN}-reading-ostep-ch{章}-…` (slides 用 `Lec{NN}`, 教材用 `OSTEP {章}`, **编号互不共享**). 标题**空格**分词. 写讲义时优先用 Lec 这份; `textbook/ostep/` 仍作全书仓.
- **何时写讲义**: 用户放入新的 Lec slides 后, 打开 `docs/Required Readings.html`, 找到该讲对应的章节, 用本地 PDF 写 `OSTEP {章} {title} 讲义.md`. 内容和 **该次 slides 对齐** (slides 没讲的小节可短, slides 强调的机制要写全, 并带一个能对上 Final 题型的小例子). 不要一次为所有 PDF 生成讲义.
- **已有 slides 且阅读讲义已齐或部分齐**: Ch.2 / Ch.4–9 / Ch.26–27 等; 旧名 `Lec0X-reading-ostep-…` 扫描时应迁为 `OSTEP {章} …`.
- 章节文件名对照 (必读表, 不是全书):

| 课 | OSTEP | textbook 仓 | Lec 对齐副本 (独立 OSTEP 编号) |
|---|---|---|---|
| Introduction | Ch.2 | `intro.pdf` | `OSTEP 2 introduction.pdf` |
| Process | Ch.4, Ch.5 | `cpu-intro.pdf`, `cpu-api.pdf` | `OSTEP 4 process.pdf`, `OSTEP 5 process api.pdf` |
| Virtualize CPU | Ch.6 | `cpu-mechanisms.pdf` | `OSTEP 6 limited direct execution.pdf` |
| Scheduling | Ch.7, Ch.8, Ch.9.1 | `cpu-sched.pdf`, `cpu-sched-mlfq.pdf`, `cpu-sched-lottery.pdf` | `OSTEP 7 scheduling.pdf`, `OSTEP 8 mlfq.pdf`, `OSTEP 9 lottery.pdf` |
| Threads | Ch.26, Ch.27 | `threads-intro.pdf`, `threads-api.pdf` | `OSTEP 26 threads intro.pdf`, `OSTEP 27 threads api.pdf` |
| Locks | Ch.28 (不含 28.10, 28.11, 28.15, 28.16) | `threads-locks.pdf` | (slides 入库后再拷为 `OSTEP 28 …`) |
| CV / sem | Ch.30, Ch.31 | `threads-cv.pdf`, `threads-sema.pdf` | (slides 入库后再拷) |
| Deadlock 课 | Ch.32 | `threads-bugs.pdf` | (slides 入库后再拷) |
| Address space | Ch.13, Ch.14 | `vm-intro.pdf`, `vm-api.pdf` | (slides 入库后再拷) |
| Translation | Ch.15 | `vm-mechanism.pdf` | (slides 入库后再拷) |
| Segmentation / free space | Ch.16, Ch.17 (不含 17.2) | `vm-segmentation.pdf`, `vm-freespace.pdf` | (slides 入库后再拷) |
| Paging | Ch.18 | `vm-paging.pdf` | (slides 入库后再拷) |
| TLB / small tables | Ch.19, Ch.20 | `vm-tlbs.pdf`, `vm-smalltables.pdf` | (slides 入库后再拷) |
| Replacement | Ch.21, Ch.22 | `vm-beyondphys.pdf`, `vm-beyondphys-policy.pdf` | (slides 入库后再拷) |
| Files | Ch.39, Ch.40 | `file-intro.pdf`, `file-implementation.pdf` | (slides 入库后再拷) |

## 生成时还要遵守

- 专有名词在 **每一份讲义内第一次** 写成 `中文 (English)`.
- Exercise / Crux 跟 slides 顺序, 不堆在文末.
- 这份 2023 卷的逐步答案在 `test&quiz/Final01 2023-12-13 解析.md`. 新讲义里的例题可以模仿它的问法 (手算, 改代码, 安全序列), 不要整卷抄进讲义.

### OSTEP 讲义: 教材代码必须入库 (强制)

凡 `Lec/OSTEP *讲义.md` 及以后新生成的 OSTEP 阅读讲义 (旧名 `*-reading-ostep-*-讲义.md` 扫描时应迁名):

1. **教材中出现的示例程序 / 代码片段全部写入讲义**, 不得只写「见 Figure x.y」或只概括行为.
   - 含完整 `.c` 程序 (如 `cpu.c`, `p1.c`, `t0.c`, `lottery.c`)
   - 含书中给出的关键结构体 / 伪代码片段 (如 xv6 `struct proc`, `swtch` 保存列表)
   - 官方源码优先对照 https://github.com/remzi-arpacidusseau/ostep-code (目录与章对应, 如 `intro/`, `cpu-api/`, `threads-intro/`)
2. **每段代码须附注释解析**:
   - 代码块内: 关键行用简体中文行内注释 (半角标点)
   - 代码块后: 用表或 bullet 说明入口参数, 返回值分支, 与本章 crux / 课件考点的对应
   - 若书中有运行输出样例, 一并写入并标「次序可能不确定」等注意点
3. **禁止**: 只留实验 checklist 而无源码; 把多文件挤成「要点伪代码」替代教材正文; 省略 `#include` / `main` 以致无法对照编译.
4. 本章若 **无** 程序代码 (纯调度仿真图, 如部分 Ch.7–8), 在讲义注明「本章无教材 `.c` 示例」, 图中算法步骤仍须逐步讲解.
