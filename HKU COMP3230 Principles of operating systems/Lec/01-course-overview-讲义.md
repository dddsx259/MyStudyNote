# Lec00 Course Overview: 课程导论 (归纳汇总)

- **来源**: `Lec/01-course-overview.pdf` (21 页, 全覆盖)
- **课程**: COMP3230B Principles of Operating Systems, 2026–27
- **授课**: Prof. Zuming Jiang (`jzuming@hku.hk`); 办公室 Chow Yei Ching Building Rm 301F
- **Office hour**: Monday 9:00–10:00 (需预约)

> 本讲以课程政策与学习安排为主; 权重/迟交属政策陈述, 无需数学证明. 下表按 PDF 页序归纳全部知识点.

---

## 0. 一页速览 (汇总)

| 维度 | 内容 |
|---|---|
| 分班 | Subclass **B** |
| 目标 | 现代 OS 组件 + mechanism/policy + 设计取舍 |
| 连续评估 50% | Lab 4% + PS 18% + PA 28%; **无 midterm** |
| Final 50% | 3h **开卷 (open-book)** |
| 教材 | OSTEP (必读, 免费在线) + 若干参考书 |
| 环境 | Ubuntu 22.04/24.04; 系 Linux; WSL2; 课程 Docker |
| Moodle | `COMP3230_1B_2026` (id=139745) |

---

## 1. 课程信息与师资 (p.2–5)

### 1.1 Instructor

- Prof. Zuming Jiang; Email / Office / OH 见文首元信息.

### 1.2 研究方向简介 (p.3–4)

Instructor 研究侧重 OS / 驱动 / 并发相关测试与 fuzzing, 例如:

- TDSC 2023: 错误处理代码测试 (fault injection + error-coverage-guided fuzzing)
- NDSS 2022: 上下文敏感、有向的并发 fuzzing (data-race)
- TSE 2022 / ISSRE 2019 / SANER 2019: 设备驱动中的 data race / 错误处理 fuzzing

Slides 鼓励: 有 OS 研究想法可找老师讨论; 文献调研可借助 LLM, 但仍需弄清与已有工作的差异.

### 1.3 Tutors (p.5)

| Tutor | Email | 负责 |
|---|---|---|
| Mr. Yu, Miao | miaoyu.hku@connect.hku.hk | Tutorial 2 + PA1 + PS2 |
| Mr. Pei, Yuxing | yuxing.pei@connect.hku.hk | Tutorial 3 + PA2 + PS1 |
| Miss Gao, Mingyan | mingyan.gao@connect.hku.hk | Tutorials 1 & 4 + PS3 |

**术语**: PA = Programming Assignment; PS = Problem Set.

---

## 2. Moodle 站点 (p.6)

- Course ID: `COMP3230_1B_2026`
- URL: https://moodle.hku.hk/course/view.php?id=139745

站点内容包括: Homepage, Course Information, **Teaching plan**, Reading List, Lecture Notes, Assignments (说明与提交), Announcements, Web references, **Discussion Forum** (同学互答与提问).

---

## 3. 课程目标与 ILO (p.7–11)

### 3.1 Course Objectives (p.7)

1. 介绍 OS 基础, 学习各组件操作与设计原则的细节
2. **理解**现代 OS 的主要组成部分
3. **学习**底层 **mechanisms (机制)** 与 **policies (策略)**, 以及设计选择带来的含义 / 取舍

(p.8–9 「Daily life problem」为课堂例子页, PDF 无额外文字要点.)

### 3.2 Intended Learning Outcomes (ILO)

**ILO1 – Fundamentals**: 讨论不同 OS 结构特征 (如 microkernel, layered, virtualization 等), 并识别 OS 的核心功能.

**ILO2 – Principles**: 解释核心功能背后的原则, 并比较其上算法.

| 子项 | 主题 |
|---|---|
| ILO 2a | 管理 process/thread 与 CPU 共享 |
| ILO 2b | 有效管理与分配 memory |
| ILO 2c | 支持 concurrency 与 process/thread 间 synchronization |
| ILO 2d | 管理与分配 persistent data storage |

**ILO3 – Performance**: 分析/评估核心功能相关算法, 解释主要性能问题.

**ILO4 – Practicability**: 能运用现代 OS 中的系统软件与工具 (threads, system calls, semaphores 等) 做软件开发.

---

## 4. 教材与参考文献 (p.12)

### 必读 (Required online textbook)

*Operating Systems: Three Easy Pieces* (OSTEP), Remzi & Andrea Arpaci-Dusseau  
http://pages.cs.wisc.edu/~remzi/OSTEP/

### 其他参考

| 书 | 备注 |
|---|---|
| Deitel et al., *Operating Systems*, 3e | Prentice Hall |
| Silberschatz et al., *Operating System Concepts*, 10e | Wiley |
| Stallings, *Operating Systems: Internals and Design Principles*, 9e | Prentice Hall |
| Bovet et al., *Understanding the Linux Kernel*, 3e | O'Reilly |
| Russinovich et al., *Windows Internals*, 7e | Microsoft Press |
| Other online references | Moodle / 课堂补充 |

---

## 5. 评分与作业政策 (p.13–14, p.16–17)

### 5.1 Assessment 结构 (汇总表)

| 类别 | 权重 | 细节 |
|---|---|---|
| Continuous Assessment | **50%** | 见下三行 |
| └ take-home labs | 4% | 4 个计分 lab (slides: 「4 take-home lab exercises – 4%」) |
| └ problem-set (PS) ×3 | 18% | 书面问题集 |
| └ programming (PA) ×2 | 28% | Ass1 15% + Ass2 13% |
| Midterm | **无** | — |
| Final examination | **50%** | 3 小时, **open-book** |

权重合计: $4\%+18\%+28\%+50\%=100\%$. (算术核对.)

### 5.2 两个 Programming Assignments (p.16)

| PA | 权重 | 内容 |
|---|---|---|
| **Ass 1** Job Submission | 15% | 类 shell 的作业提交程序; 多进程执行/管理, 收集进程执行统计 |
| **Ass 2** 多线程计算 | 13% | 用 **Pthread** 写计算密集型多线程程序; 涉及线程同步与协调 |

### 5.3 Slip Days / 迟交 (p.14)

Moodle 专节: https://moodle.hku.hk/course/section.php?id=1603507

| 规则 | 内容 |
|---|---|
| 适用范围 | **仅** PS 与 PA (**不**适用于 labs) |
| 额度 | 每人 **5** slip days |
| 用法 | 1 slip day = 截止日期延后 1 天 |
| 单次上限 | 同一作业最多延后 **3** 天 |
| 超额惩罚 | slip 用尽后, 未覆盖的迟交天每天 **−20%** (仍批改但重罚) |

### 5.4 Plagiarism (p.17)

- 抄袭属纪律处分事项
- 会用软件查重; 可疑个案会约谈解释
- 按院系 plagiarism 处理指引执行

---

## 6. Teaching Plan (p.15)

Teaching plan / schedule 在 Moodle HTML 资源 (slides 链至 `C3230B-Teaching Plan.html`). 具体周次主题以该页为准, 本讲义不臆造未在 PDF 出现的周表内容.

---

## 7. 如何达成学习目标 (p.18–19)

### 7.1 阅读与投入

- 多数主题讨论 **mechanisms vs policies**, 技术性强、含底层细节, 需要投入时间
- 有 **reading list**: **课前预习**对应章节效果最好
- 建议每周 **6–7 小时**读 lecture notes + readings
- 通过进一步探索 OS 系统来学习

### 7.2 课堂与作业习惯

- 主动参与 lecture; 不懂就问 (课后亦可)
- 作业与考试题 **不总是**课堂例子的直接映射 — 目标是能把概念用到新情境
- 作业 **尽早开始**; 给自己规划时间; 卡住不要空转, 及时提问
- 有效使用 **discussion forum** 分享信息

---

## 8. 计算环境与账号 (p.20–21)

### 8.1 Computing Platform

- Ubuntu **22.04 / 24.04**
- Department's Linux Servers
- **WSL 2** (Windows Subsystem for Linux)
- Course Docker Ubuntu image (Windows & Apple)
- 细节: https://moodle.hku.hk/course/section.php?id=1689298

### 8.2 CS Account

新 CS / 非 CS / 交换生: 从  
https://intranet.cs.hku.hk/csintranet/newstudent.jsp  
申请 CS account.

---

## 易错点

1. **无 midterm**, 但连续评估已占 50% — 勿拖 PA/PS
2. Final 开卷仍需理解 mechanism/policy, 不能只靠翻书
3. Slip days **不**覆盖 labs
4. Ass1 偏进程/shell; Ass2 偏 Pthread/同步 — 与 C 预备 (下一讲) 直接相关
5. 评分以 Moodle / 最新公告为准; 本讲义对齐 Overview PDF

## 与后续材料

- `Lec/02-c-programming.pdf` / 同目录讲义: C 与系统 I/O 热身 (服务 Lab/PA)
- Teaching plan, reading list: Moodle
