# Tutorial 3 — Pthread 总结

- **来源**: `tut/Tut03 pthread.pdf` (26 页)
- **详细讲义**: [`Tut03 pthread 讲义.md`](Tut03%20pthread%20讲义.md)
- **主题**: POSIX threads — create/join → mutex 保护共享数据 → condition variable 等待条件
- **对齐**: `Lec/Lec07 thread concept` · `Lec/Lec08 synchronization` · OSTEP Ch.26–28, 30 · MiniLab4

---

## 结构

| Part | 内容 |
|---|---|
| Map | 今日三块: create·join / mutex / cond |
| I | Pthread API: 同进程共享地址空间; `create` / `join` / `self` / `cancel` |
| II | Mutex: `counter++` 丢失更新; lock/unlock; trylock |
| III | Condition variables: `done` 标志 + `while` + `signal` |
| Ref | C11 atomics; local vs static; cancellation 细节 |

---

## Part I — The Pthread API

- Thread 在**同一进程**内: 共享 code / globals / heap / 打开文件; **各自** stack · registers · PC
- 对比 Tut2: `fork` 复制地址空间; `pthread_create` 共享地址空间, 可用指针交换数据
- 编译: `#include <pthread.h>`, 链接 `-pthread`
- 生命周期对照:

| 任务 | Process | Pthread |
|---|---|---|
| 创建 | `fork()` | `pthread_create()` |
| 标识 | `getpid()` | `pthread_self()` / `pthread_t` |
| 结束自己 | `exit()` | `return` / `pthread_exit()` |
| 等待并收结果 | `waitpid()` | `pthread_join()` |
| 交换数据 | IPC / 显式共享内存 | 指向共享对象的指针 |

- **易错**: `pthread_join` 收到的是指针, **不会**延长局部变量寿命 — 不要 `return &local`
- 模式: 先 create 两个 worker, 再分别 join (不要 create–join–create–join 串成假并行, 除非有意)
- `pthread_cancel`: 默认在 cancellation point (如 `pthread_testcancel`) 才生效

---

## Part II — Mutexes

- 两线程各 `counter++` 一百万次, 期望 `2000000`, 无锁时常更少
- 原因: `counter++` = read → add → write; 两线程可读到同一旧值再各自写回
- `pthread_mutex_lock` / `unlock`: 临界区互斥; 另一线程在 `lock` 处等待
- 多共享量 (`processed` / `remaining`) 用**同一把**锁保护一致性
- `pthread_mutex_trylock`: 拿不到锁立刻返回, 可改做无关工作 B
- 生命周期: `init` → 使用 → 所有用户结束后 `destroy`

---

## Part III — Condition Variables

- 场景: main 要在 workers **仍有后续工作**时, 先等到两段数组都写完
- 三件套: `done[]` 标志 + mutex + condition variable
- `pthread_cond_wait(&cv, &mutex)`: 原子地释放 mutex 并睡眠; 被唤醒后重新持锁
- Worker: 写完切片 → 持锁设 `done` → `pthread_cond_signal` (或 broadcast)
- **必须用 `while` 再检查条件**: wakeup ≠ 条件已真 (虚假唤醒 / 只完成一半)
- 典型 main 循环: `while (!(done[0] && done[1])) pthread_cond_wait(...)`

---

## Recap 速查

| 目标 | 调用 |
|---|---|
| 启动 worker | `pthread_create` |
| 结束自己 | `return` / `pthread_exit` |
| 等待并收结果 | `pthread_join` |
| 保护共享读写 | `mutex_lock` / `unlock` |
| 等到状态就绪 | `cond_wait` (在 `while` 里) + `signal`/`broadcast` |

构建加 `-pthread`, 检查返回码; 参数与共享对象在使用者结束前保持存活.

---

## 参考附录 (slides)

- **A**: C11 `atomic_fetch_add` (`<stdatomic.h>`) 可保护单计数器, 与 Pthread API 独立
- **B**: 函数内 `int i` 每调用一份; `static int total` 全调用共享
- **C**: cancellation 默认 enabled, 在 cancellation point 处理
