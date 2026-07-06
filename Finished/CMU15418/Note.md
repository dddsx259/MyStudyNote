# Chapter 1 - A journey of program "Hello, world!"

Consider the following C program:

```c
#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

## 1. Translation(1.1-1.3)
The first step of it's life cycle is to be translated into an executable file.

We only need a simple command to do it:
```bash
linux> gcc -o hello hello.c
```
Bur the whole process is not that simple. There are 5 steps:
### 1. Preprocessing
+ From `hello.c` to `hello.i`:
+ The preprocessor modifies the original C program(`hello.c`) according to directives that begin with the `#` character. The result is stored in `hello.i`.
+ e.g. `#include <stdio.h>` will be replaced with the content of `stdio.h`.
+ The preprocessing is a simple text-level operation.

### 2. Compilation
+ From `hello.i` to `hello.s`:
+ The compiler translates the preprocessed C program(`hello.i`) into an assembly language program(`hello.s`), which is a low-level language that is close to the machine language.
+ The compilation is a compile-time operation.

### 3. Assembly
+ From `hello.s` to `hello.o`:
+ The assembler translates the assembly language program(`hello.s`) into a object file(`hello.o`), which is a binary file that contains the machine code of the program.
+ The relocatable object file can't be executed directly. It needs to be linked with the standard library to form an executable file.
+ The assembly is a compile-time operation.

### 4. Linking
+ From `hello.o` to `hello`:
+ The linker links the object file(`hello.o`) with the standard library to form an executable file(`hello`).
+ The executable file can be executed directly.
+ The linking is a link-time operation.

### 5. Execution
+ From `hello` to the output:
+ The executable file(`hello`) is executed and the output is printed.
+ The execution is a run-time operation.

> Now, the executable file `hello` is created and stored in the disk.

## 2. 