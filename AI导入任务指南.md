# My Todo: AI 导入任务指南

给其他 AI / agent 阅读. 你的任务是根据用户需求生成可导入的待办文件, 不要改应用源码, 不要写 journal 事件.

用户会把你生成的文件放进 OneDrive 数据目录的 `inbox/`, 或在 Mac 应用菜单「数据 → 导入...」中选择该文件.

更完整的运行时数据说明见同目录 `data-format.md`. 导入时只需要遵守本文.

---

## 你要产出什么

二选一 (推荐 Markdown, 更好写; JSON 更适合批量/带 id 合并):

| 格式 | 扩展名 | 适用 |
| --- | --- | --- |
| Markdown | `.md` | 课程作业, 阅读清单, 临时任务 |
| JSON | `.json` | 结构化批量导入, 需要稳定 `id` 时 |

文件名建议: `inbox-YYYYMMDD-简短主题.md` 或 `.json`.

---

## 交付方式 (告诉用户怎么用)

生成文件后, 用下面任一方式即可导入 (导入不会覆盖已有专注记录):

1. 复制到数据目录: `<OneDrive>/TodoList/inbox/你的文件.md`
2. 打开 My Todo → 菜单「数据」→「处理 inbox」 (或下次启动应用时也会扫 inbox)
3. 或菜单「数据」→「导入...」直接选文件

---

## Markdown 格式 (推荐)

### 骨架

```md
# 清单名 (大分类, 如课号)

- [ ] 任务标题 @section(assignment) @ddl(2026-10-20) @priority(med) @est(25)
  - [ ] 子任务一
  - [ ] 子任务二
- [ ] 另一条任务 @section(slides) @repeat(daily) @remind(dayBefore 09:00)
```

### 硬性规则

1. 用 `# 空格 + 清单名` 开始一个**大分类/清单**. 没有清单标题的任务会被忽略. 一门课通常一个清单 (如 `COMP3230`).
2. 清单内用 `@section(...)` 做**小分类** (如 `assignment`, `slides`, `reading`). 同一清单下相同 section 名会在应用里分到同一组.
3. 父任务行必须以 `- [ ]` 或 `- [x]` 开头 (行首可无缩进).
4. 子任务必须相对行首缩进至少 2 个空格, 且同样是 `- [ ]` / `- [x]`. **只能一层子任务**, 不要再缩进套娃.
5. 标签写在任务标题同一行, 用空格分隔. 标签名区分大小写, 按下列拼写.
6. 不要写 HTML, 不要用 `* ` 或 `1. ` 列表代替 checkbox.
7. 导入时 `[x]` 与 `[ ]` 都会建成未完成任务模板; 勾选状态以应用内完成为准. 写清单时默认用 `- [ ]`.
8. 中文标点可以出现在标题里; **标签参数里的日期/时间用 ASCII**, 不要用全角冒号或全角括号.
9. **不要**用导入表达「我的一天」. 「我的一天」是用户在应用里点太阳图标加入今天想做的事, 不是 DDL, 也不写进导入文件.

### 支持的标签

| 标签 | 示例 | 含义 |
| --- | --- | --- |
| `@section(...)` | `@section(assignment)` / `@section(slides)` | 清单内小分类. 建议短英文或短中文, 同一课程内命名稳定 |
| `@ddl(...)` | `@ddl(2026-10-20)` 或 `@ddl(2026-10-20T23:59)` | 截止日期 (DDL). 可只有日期, 也可带时刻. **不是**「我的一天」 |
| `@priority(...)` | `@priority(none\|low\|med\|high)` | 优先级, 默认可不写 (= none) |
| `@est(...)` | `@est(25)` | 预估分钟数, 整数 |
| `@repeat(...)` | `@repeat(daily)` 或 `@repeat(weekly mon)` | 重复. weekly 的星期: `sun mon tue wed thu fri sat` |
| `@remind(...)` | 见下表 | 提醒 |

#### `@remind` 写法

| 写法 | 含义 |
| --- | --- |
| `@remind(dayBefore 09:00)` | DDL / 出现日的前一天 09:00 提醒 |
| `@remind(2026-10-19T18:00)` | 非重复任务: 指定绝对时刻 |
| `@remind(09:00)` | 重复任务: 在每次出现日当天的 09:00 |

没有 DDL 时, 不要写 `@remind(dayBefore ...)`, 因为没有可提前的期限.

### Markdown 完整示例

```md
# COMP3230

- [ ] 读 OSTEP Ch2 @section(reading) @ddl(2026-10-14T23:59) @remind(dayBefore 09:00) @priority(med) @est(50)
  - [ ] 2.1 笔记
  - [ ] 2.2 练习题
- [ ] Lec03 slides @section(slides) @est(40)
- [ ] Tut03 交卷 @section(assignment) @ddl(2026-10-16) @priority(high) @est(90)

# 每日

- [ ] 背单词 @repeat(daily) @remind(09:00) @est(20)
- [ ] 周报 @repeat(weekly fri) @ddl(2026-10-17T18:00) @remind(dayBefore 20:00) @priority(med)
```

---

## JSON 格式

### 骨架

```json
{
  "schemaVersion": 1,
  "lists": [
    {
      "name": "课程",
      "color": "blue",
      "tasks": [
        {
          "title": "读 Lec03",
          "notes": "",
          "section": "slides",
          "priority": "med",
          "ddl": "2026-10-12T23:59:00",
          "remind": { "kind": "dayBefore", "time": "09:00" },
          "repeat": { "kind": "weekly", "weekday": "mon" },
          "estimateMin": 25,
          "subtasks": [
            { "title": "第 1 节" },
            { "title": "第 2 节" }
          ]
        }
      ]
    }
  ]
}
```

### 字段约定

**清单 `lists[]`**

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `name` | 是 | 清单名 |
| `color` | 否 | `gray blue green orange pink purple red yellow teal indigo` |
| `id` | 否 | 有则按 id 合并; 无则新建 |
| `tasks` | 否 | 任务数组 |

**任务 `tasks[]`**

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `title` | 是 | 标题 |
| `notes` | 否 | 备注 |
| `section` | 否 | 清单内小分类, 如 `assignment` / `slides` |
| `priority` | 否 | `none` / `low` / `med` / `high` |
| `ddl` | 否 | ISO 日期或日期时间字符串 |
| `ddlHasTime` | 否 | 是否包含时刻; 省略时若 `ddl` 带时间则视为 true |
| `remind` | 否 | 见下 |
| `repeat` | 否 | 见下; 省略 = 不重复 |
| `estimateMin` | 否 | 预估分钟 |
| `startDate` | 否 | 重复系列开始日; 省略则用导入当天 |
| `subtasks` | 否 | 仅一层: `{ "title": "..." }` 或带 `id` |
| `id` | 否 | 有则按 id 合并更新; 无则新建 |

**`remind`**

```json
{ "kind": "none" }
{ "kind": "dayBefore", "time": "09:00" }
{ "kind": "custom", "at": "2026-10-19T18:00:00" }
{ "kind": "custom", "time": "09:00" }
```

最后一种给重复任务用: 出现日当天的时刻.

**`repeat`**

```json
{ "kind": "none" }
{ "kind": "daily" }
{ "kind": "weekly", "weekday": "mon" }
```

### JSON 完整示例

```json
{
  "schemaVersion": 1,
  "lists": [
    {
      "name": "MATH3603",
      "color": "teal",
      "tasks": [
        {
          "title": "Ch02 习题选做",
          "notes": "只做标星题",
          "priority": "med",
          "ddl": "2026-10-18T23:59:00",
          "remind": { "kind": "dayBefore", "time": "09:00" },
          "repeat": { "kind": "none" },
          "estimateMin": 120,
          "subtasks": [
            { "title": "Q1" },
            { "title": "Q3" },
            { "title": "Q5" }
          ]
        }
      ]
    }
  ]
}
```

---

## 语义说明 (生成时要理解)

1. **大分类** = `# 清单` (一门课一个清单). **小分类** = `@section` / JSON `section` (如 assignment, slides).
2. **DDL** 就是截止日期. 不重复任务按 DDL 出现在「今天/日历」; 重复任务按出现日出现. DDL **不是**「我的一天」.
3. **我的一天** 只在应用里用太阳图标加入, 表示「今天想做」, 与 DDL 无关. 导入文件不要写 myDay.
4. **重复** 存的是一条系列模板, 不会预生成未来每一天的行. `daily` = 每天; `weekly` + weekday = 每周那天.
5. **子任务** 只有标题和完成状态, 没有自己的 DDL/重复/提醒. 计时可以绑在父任务或某个子任务上, 耗时都算进父任务.
6. **导入只追加/合并任务定义**, 不要在导入文件里写专注时长, 完成历史, journal 事件.
7. 同一文件里可以有多个 `# 清单`. 清单名应简短稳定 (如课号 `COMP3230`), 便于用户以后继续往同一清单加任务.
8. 若用户要求「更新已有任务」, JSON 里带上之前导出的 `id`; Markdown 导入无法按 id 合并, 会新建.

---

## 生成检查清单 (输出前自检)

- [ ] 每个任务都在某个 `# 清单` 下面
- [ ] 子任务缩进 >= 2 空格, 且没有第二层子任务
- [ ] `@priority` / `@repeat` / `weekday` / `color` 拼写在允许集合内
- [ ] 课程内小分类用 `@section`, 命名稳定 (如 `assignment` / `slides` / `reading`)
- [ ] 没有把「今天想做」写成 DDL; 没有虚构 `@myday` 标签
- [ ] 日期形如 `YYYY-MM-DD` 或 `YYYY-MM-DDTHH:mm` / `YYYY-MM-DDTHH:mm:ss`
- [ ] 用了 `dayBefore` 提醒的任务确实有 DDL (或不重复任务有可提前的期限)
- [ ] 没有 invent 不存在的标签 (如 `@tag`, `@project`, `@myday`)
- [ ] 文件是合法 UTF-8; JSON 通过标准 JSON 解析

---

## 给 AI 的默认工作流

当用户说「帮我做一份 todolist / 导入任务」时:

1. 问清或从上下文提取: 清单名, 任务标题, DDL, 是否每日/每周, 子步骤, 预估时间.
2. 优先输出 **一个完整 `.md` 代码块** (或写入约定路径的文件).
3. 用两三句话告诉用户: 把文件放进 `TodoList/inbox/` 后, 在 My Todo 里「处理 inbox」或「导入」.
4. 不要同时塞进无关说明长文; 需要说明时放在代码块外.
