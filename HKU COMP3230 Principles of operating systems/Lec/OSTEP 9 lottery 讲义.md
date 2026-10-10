# OSTEP Ch.9 Scheduling: Proportional Share — 阅读讲义

- **来源**: `Lec/OSTEP 9 lottery.pdf` (14 页; 原名 `cpu-sched-lottery.pdf`)
- **对齐课件**: Fair Share / Lottery; Linux CFS 案例
- **在线**: http://pages.cs.wisc.edu/~remzi/OSTEP/cpu-sched-lottery.pdf
- **说明**: Required Readings 表列 Ch.9.1; 本讲义覆盖全章主线 (lottery / stride / CFS 摘要) 便于对照课件

---

## Crux

如何按比例共享 CPU? 关键机制?

---

## 1. Lottery Scheduling (§9.1–9.3)

- **票 (ticket)** = 份额. A 75 票, B 25 票 → 长期约 75%/25% CPU
- 每时间片抽随机赢家; **概率正确, 短窗无保证**
- Tip: **随机** 简单、少状态、避免某些确定性最坏情形

**机制**:

- **票币 (ticket currency)**: 用户内部分配再换算全局票
- **转让 (ticket transfer)**: 客户临时把票给服务器
- **膨胀 (ticket inflation)**: 可信进程组内可临时加减票 (不可信环境危险)

**实现**: 链表累加 tickets 直到超过随机 `winner` (可按票数排序加速). 教材配套仿真见官方 `ostep-code/cpu-sched-lottery/lottery.c`:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

int gtickets = 0;                             // 当前所有作业票数总和

struct node_t {
    int            tickets;                   // 该作业持有的票
    struct node_t *next;
};

struct node_t *head = NULL;

void insert(int tickets) {
    struct node_t *tmp = malloc(sizeof(struct node_t));
    assert(tmp != NULL);
    tmp->tickets = tickets;
    tmp->next    = head;                      // 头插
    head         = tmp;
    gtickets    += tickets;
}

void print_list() {
    struct node_t *curr = head;
    printf("List: ");
    while (curr) {
        printf("[%d] ", curr->tickets);
        curr = curr->next;
    }
    printf("\n");
}

int main(int argc, char *argv[])
{
    if (argc != 3) {
        fprintf(stderr, "usage: lottery <seed> <loops>\n");
        exit(1);
    }
    int seed  = atoi(argv[1]);
    int loops = atoi(argv[2]);
    srandom(seed);

    insert(50);                               // 三个作业: 50 / 100 / 25 票
    insert(100);
    insert(25);
    print_list();

    int i;
    for (i = 0; i < loops; i++) {
        int counter = 0;
        int winner  = random() % gtickets;    // 均匀抽一张「中奖彩票」编号
        struct node_t *current = head;

        // 沿链表累加票数, 第一次 counter > winner 的节点即赢家
        while (current) {
            counter = counter + current->tickets;
            if (counter > winner)
                break;
            current = current->next;
        }
        // 真实调度器此处会选中 current 跑一个时间片
        print_list();
        printf("winner: %d %d\n\n", winner, current->tickets);
    }
    return 0;
}
```

| 行含义 | 说明 |
|---|---|
| `winner = random() % gtickets` | 在 `[0, gtickets)` 抽中奖号 |
| 累加直到 `counter > winner` | 票多的作业区间更长 → 中奖概率 ∝ 票数 |
| `seed` / `loops` | 可复现随机序列; 多次调度观察比例趋近 50:100:25 |

---

## 2. Fairness study (§9.4)

两作业同票同长 $R$: 公平度量 $F=$ 先完成时间 / 后完成时间. $R$ 短时平均 $F$ 较差; $R$ 大时趋近 1.

---

## 3. Ticket assignment (§9.5)

如何分票仍是开放问题; 常交给用户/管理员策略.

---

## 4. Stride Scheduling (§9.6)

确定性比例份额: $\mathrm{stride} \propto 1/\mathrm{tickets}$; 每次跑完 $\mathrm{pass} += \mathrm{stride}$; 总选 **pass 最小**.

精确按比例; 但 **新作业的初始 pass** 难定 (全局状态). Lottery 无此包袱.

---

## 5. Linux CFS (§9.7) 摘要

- **虚拟运行时 (vruntime)**; 选最小者
- `sched_latency` / $n$ 得片长; `min_granularity` 防片过短
- **nice** → weight; 片长按权重比例
- 红黑树维护; 课上 Linux 节标非考试重点, 此处了解即可

---

## Summary

比例份额 ≠ 优化周转/响应; 目标是 **按权重分 CPU**. 课件 Lottery 例子与本陈一致.
