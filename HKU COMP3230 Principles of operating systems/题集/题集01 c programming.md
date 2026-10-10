# 题集 — C Programming

> 对齐: `Lec/Lec02 c programming 讲义.md`. 含 Mini-Lab 1 与课件要点练习.
> 含: (1) 课件证明 (2) 练习题.

---

## 课件证明

本章以 C 语言约定与 API **定义**为主; 讲义明确无非定义数学命题, **无可考完整证明**.

---

## 练习题

## Mini-Lab

### 1. Lab1 堆上动态数组

- **题目**: 在 starter `lab/Mini-lab/Lab01 heap.c` 中完成 `initialize_array(int n)`: (1) 用 `malloc` 分配 $n$ 个 `int`; (2) 令 `heap_arr[i]=i^2`; 在 `main` 中用 `./prog <n>` (`argc`/`argv`, `atoi`) 打印数组; 退出前 `free`. 对照 `Lab01 stack.c`: 若函数返回局部数组指针, 解释为何是悬空指针.
- **思路**: 堆分配生命周期跨函数; 栈数组在返回后失效. `malloc(n*sizeof(int))`, 失败检 NULL, 用后 `free` 防泄漏.
- **来源**: `lab/Mini-lab/Lab01 c basics address space 题目理解.md`, PDF `Lab01 c basics address space.pdf`

### 2. 栈 vs 堆 (概念)

- **题目**: 比较 stack 与 heap: 分配方式, 释放方式, 速度/大小/典型用途. 全局变量声明位置与可见性?
- **思路**: 栈 = 块内声明, 出作用域自动回收, 快但受限; 堆 = `malloc`/`calloc`, 必须 `free`, 灵活. 全局在函数外, 全程序共享.
- **来源**: Mini-Lab 1 PDF 要点表

---

## 讲义练习

### 3. C99 声明位置反例

- **题目**: 下列写法在「声明必须在块首」的旧 C 规则下为何非法? 先 `printf(...)`, 再 `int x;`.
- **思路**: 旧标准要求块内所有声明在任何语句之前; 课程建议仍声明在前以便兼容与可读.
- **来源**: `Lec/Lec02 c programming 讲义.md` §4.1 Compatibility

### 4. `strtok` 分词

- **题目**: 用 `fgets` 读一行到缓冲区, 以空格为分隔符用 `strtok` 逐个打印 token. 说明首次与后续调用时第一个参数应传什么.
- **思路**: 首次传原串; 后续传 `NULL`. `strtok` 会改写原串且一般不可重入, 多线程慎用.
- **来源**: `Lec/Lec02 c programming 讲义.md` §5.2

### 5. `man` 查系统调用

- **题目**: 要查 `open` 的内核系统调用手册 (非 libc 包装), 应使用 `man` 的哪个 section? 与 `man 3 open` 有何区别?
- **思路**: 系统调用通常在 section 2 (`man 2 open`); section 3 是用户库 API. 易错: 看错 section.
- **来源**: `Lec/Lec02 c programming 讲义.md` §6 / 易错点
