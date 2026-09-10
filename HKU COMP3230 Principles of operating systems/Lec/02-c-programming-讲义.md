# C Programming 预备: 归纳汇总

- **来源**: `Lec/02-c-programming.pdf` (28 页, 全覆盖)
- **课程**: COMP3230B Principles of Operating Systems
- **用途**: OS 课前 C / UNIX 系统编程热身 (服务 Lab1、PA 中的进程/线程/系统调用)

> 本讲以语言与 API **约定**为主; 无非定义数学命题. 语义/接口视为定义, 无需证明. 按 PDF Contents 四大块 + 文末补充专题归纳.

---

## 0. 一页速览 (汇总)

| 主题 | 你要会什么 |
|---|---|
| 为何学 C | OS 多用 C/汇编; PA 要指针与手动内存 |
| 编译运行 | `gcc file.c -o out` → `./out` |
| Formatted I/O | `printf` / `scanf` / `sprintf`; `man 3 printf` |
| Compatibility | 声明前置; `for` 内声明变量在旧 C 非法 |
| 字符串 | 无 string 类型; `char[]` + `'\0'`; `<string.h>`; `strtok` |
| 动态内存 | `malloc`/`calloc` + `free`; 先分配再写 |
| 参数传递 | 仅传值; 用指针模拟引用 (`swap`) |
| 文件 I/O | 高层 `FILE*` 流 vs 底层 **fd**; `fopen`/`read`/`write` |
| 工具 | `man` / `man -f` / section 编号 |
| 命令行 | `main(int argc, char *argv[])` |
| 布尔 | 传统 0/NULL 为假; C99 `<stdbool.h>` |

**参考站点** (p.3): Marshall *Programming in C*; GNU libc manual; *The C Book*.

---

## 1. 为何需要 C (p.4)

- 多数 OS 用**较低级语言**实现; **C** 与 **assembly** 是常见选择
- 你已有 Python 基础; 本讲给 C 编程概览, 为后续系统调用 / 进程 / Pthread 铺路

---

## 2. 程序结构与编译 (p.5)

C 与 C++ 程序结构几乎相同. 编译与运行:

```bash
gcc Example1.c -o example1
./example1
```

最小例子要点:

```c
#include <stdio.h>
int main(void) {
    printf("Beware the differences between C & C++ !!\n");
    getchar();
    return 0;
}
```

**易混**: C 不是 C++ (无引用、无 `cout` 重载等习惯用法).

---

## 3. Formatted I/O (p.6–9)

### 3.1 `printf` (输出到 stdout)

```c
int printf(char *format, /* arg list */ ...);
```

- 可变参数; 按 **format string** 打印后续参数
- 细节: `man 3 printf`

Format 中 `%` 后跟类型说明:

| 说明符 | 类型 |
|---|---|
| `%d` | `int` |
| `%f` | `float` |
| `%s` | 字符串 |
| `%c` | `char` |

还可带宽度/精度, 如 `%4d`, `%.2f`. 例:

```c
int abc = 10;
float efg = 6.54321f;
printf("integer is: %4d, float is: %.2f, string is: \" %s \" \n",
       abc, efg, "So what");
/* 输出类似: integer is:   10, float is: 6.54, string is: " So what " */
```

### 3.2 `scanf` (从 stdin 读入)

```c
int scanf(char *format, /* args */ ...);
```

- 按 format 解释输入, **写入变量** — 参数必须是**地址** (`&number`)
- `man 3 scanf`

```c
int number;
float fnum;
scanf("%d %f", &number, &fnum);
```

### 3.3 `sprintf` (写入字符数组)

与 `printf` 相同, 但输出写入 `s` 指向的缓冲区, 而非 stdout:

```c
int sprintf(char *s, const char *format, ...);
```

典型流程: `scanf` 读入 → `sprintf` 格式化进 `mystr[]` → 再 `printf("%s", mystr)`.

---

## 4. Compatibility 兼容性 (p.10–12)

### 4.1 声明位置

- **早期 C**: 声明只能出现在块开头, **任何语句之前**
- **C99 / 现代 gcc**: 允许声明与代码混排
- **课程建议**: 仍尽量「声明在前」, 避免旧编译器不兼容, 也更易读

反例 (旧规则下错误): 先 `printf`, 再 `int x;`.

### 4.2 `for` 循环内声明

```c
for (int ind = 0; ind < 10; ind++)
    printf("%d\t", ind);
```

- 早期 C **不允许**在 `for` 里声明循环变量
- 现代 gcc 支持; 若需最大可移植性, 把 `int ind` 提到循环外

---

## 5. C 字符串与动态内存 (p.13–17)

### 5.1 没有 `string` 类型 (p.13)

- 字符串 = **`char` 数组**, 以 `'\0'` 结尾
- 操作依赖 C 库: `#include <string.h>`
- 常用: `strcat`, `strcmp`, `strcpy`, `strlen`, `strtok`, `memcpy`, `memset`, …
- 参考: Marshall 站点 string 一节 (slides 链接)

### 5.2 `strtok` 分词 (p.14)

```c
char *strtok(char *s1, const char *s2);
```

- 按 `s2` 中的分隔符把 `s1` 切成 token
- **首次**调用传原字符串; **后续**调用第一个参数传 `NULL`
- 注意: `strtok` **会修改**原字符串; 且一般**非可重入**

例: `fgets` 读入一句 → `strtok(mystr, " ")` → 循环 `strtok(NULL, " ")` 打印各词.

### 5.3 `malloc` / `free` (p.15–16)

```c
void *malloc(size_t size);   /* man malloc */
void free(void *ptr);
```

- `void *`: 通用指针, 可与其他指针类型互相转换赋值
- 分配时用 `sizeof` 保证可移植性:

```c
int *data = (int *)malloc(sizeof(int) * 10);
/* ... */
free(data);
```

也可用 `calloc` (slides 提及).

### 5.4 典型错误: 未分配就写数组 (p.16)

```c
char *Aarray;
for (i = 0; i < length; i++)
    Aarray[i] = '\0';   /* 错误: 未 malloc */
```

- 错误可能**不立刻崩溃**, 极难调试
- **原则**: 使用数组/指针前先分配; 用完 `free`

正确模式:

```c
charray = (char *)malloc(sizeof(char) * 256);
intarray = (int *)malloc(sizeof(int) * 64);
/* use ... */
free(charray);
free(intarray);
```

### 5.5 参数传递 (p.17)

- C **只有传值 (pass-by-value)**
- 要「传引用」效果: 传**指针**, 在函数内解引用修改

```c
void swap(int *x, int *y) {
    int temp = *x;
    *x = *y;
    *y = temp;
}
int a = 3, b = 5;
swap(&a, &b);
```

---

## 6. File I/O (p.18–23)

### 6.1 高层: `FILE` 流 (p.18–20)

用 `FILE *` 跟踪打开的文件; 打开 → 读/写 → `fclose`.

常用接口 (slides 列出):

| 函数 | 作用 |
|---|---|
| `fopen(filename, mode)` | 打开, 返回 `FILE*` |
| `fclose(stream)` | 关闭 |
| `fgetc` / `fputc` | 读/写单字符 |
| `fgets` / `fputs` | 读/写字符串 |
| `fprintf` / `fscanf` | 格式化读写 |

**`fopen` 模式**:

| mode | 含义 |
|---|---|
| `r` | 读 |
| `w` | 写 (文件可不存在) |
| `a` | 追加 |
| `r+` | 读写, 从开头 |
| `w+` | 读写 (覆盖) |
| `a+` | 读写 (存在则追加) |

**细节**:

- `fgetc`: 以 `unsigned char` 读下一字符, **返回 `int`** (便于用 `EOF` 区分)
- `fgets(s, count, stream)`: 读到换行或最多 `count-1` 字符, 并加 `'\0'`; 串长至多 `count-1`

**标准流** (已打开可用):

- `stdin`, `stdout`, `stderr`
- `putchar(c)` 等可看作对标准流的封装
- 可用「一切皆文件/流」的观点统一理解 I/O

### 6.2 底层: File Descriptor (p.21–23)

| 概念 | 说明 |
|---|---|
| 流 (stream) | 建立在 **file descriptor (fd)** 之上的更高层接口 |
| fd | 每个打开「文件」的**唯一整数**标识 |
| 可表示对象 | 普通文件 / 设备 / pipe / socket |

**何时用低层 fd 而非流**:

1. 需要**设备特定**控制操作
2. 把整个文件读入内存再解析
3. 把描述符传给**子进程** (子进程不能直接继承 `FILE*` 流对象的同一套语义)

**打开/关闭**:

```c
int open(const char *filename, int flags[, mode_t mode]);
int close(int filedes);
```

- `flags`: 位或组合, 如 `O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_APPEND`, `O_EXCL`, …
- `mode`: 权限, **仅在带 `O_CREAT` 时相关**

**块读写**:

```c
ssize_t read(int filedes, void *buffer, size_t size);
ssize_t write(int filedes, const void *buffer, size_t size);
```

- `read`: 从已打开 fd 读至多 `size` 字节到 `buffer`
- `write`: 把内存中连续 `size` 字节写入 fd

**归纳**: Lab/PA 里若只做文本读写, 优先 `FILE*`; 涉及 `fork`/管道/底层控制时用 fd.

---

## 7. `man` 命令 (p.24–25)

```bash
man fork          # 查看手册
man -f open       # 列出所有叫 open 的条目 (whatis)
man 2 open        # 指定 section 2 (系统调用)
man man           # man 本身的用法
```

- 同名可能有多份 manpage; **section 不对**会看到错误页
- 常见: section **2** 系统调用, section **3** 库函数 (`printf` → `man 3 printf`)

---

## 8. 命令行参数 (p.26–27)

```c
int main(int argc, char *argv[]);
/* 或 char **argv */
```

| 符号 | 含义 |
|---|---|
| `argc` | 参数个数 (**含**程序名) |
| `argv[0]` | 程序名 / 路径 |
| `argv[1..]` | 其余参数 |

例: `ls -l -t -r` → `argc=4`, `argv[0]="ls"`, …  
程序内可循环打印 `argv[i]`.

---

## 9. Boolean (p.28)

- **传统**: 条件中 `0` 与 `NULL` 为假; 非零为真
- **C99**: `#include <stdbool.h>` 后可用 `bool`, `true`, `false`
  - `bool` → `_Bool`
  - `true` → `1`, `false` → `0`

---

## 知识结构图 (归纳)

```text
C 预备
├── 工具链: gcc, ./a.out, man
├── I/O
│   ├── 格式化: printf / scanf / sprintf
│   ├── 流 FILE*: fopen 族 + stdin/out/err
│   └── 底层 fd: open / read / write / close
├── 内存与字符串
│   ├── char[] + '\0' + string.h (strtok…)
│   └── malloc / free (先分配再写)
├── 语言细节
│   ├── 仅传值 → 指针模拟引用
│   ├── 声明位置 / for-声明 兼容性
│   └── bool (传统 vs stdbool.h)
└── 程序入口: argc / argv
```

## 易错点

1. `scanf` 忘写 `&`
2. 未 `malloc` 就写指针; 忘 `free` 泄漏
3. `strtok` 破坏原串、不可随意多线程共用
4. 混淆 `FILE*` 与 fd; `fork` 后传流需谨慎
5. `man` 看错 section (2 vs 3)
6. 把 C++ 习惯直接搬进 C
7. `sprintf` 目标缓冲区要足够大, 防溢出

## 与本课后续

- Overview 中的 **Ass1** (多进程 / Job Submission) → 会用到 `fork` 相关 manpage、可能 fd/管道
- **Ass2** (Pthread) → 指针、传参、同步前需扎实 C 基础
- Lab: 先在本讲环境 (Ubuntu / WSL / Docker) 上练熟编译与 `man`
