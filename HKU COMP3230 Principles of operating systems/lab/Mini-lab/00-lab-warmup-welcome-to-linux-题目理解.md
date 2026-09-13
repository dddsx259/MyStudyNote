# Mini-Lab 0: Warm up! Welcome to Linux — 题目理解

- **来源**: `lab/00-lab-warmup-welcome-to-linux.pdf` (9 页, 0 pt)
- **课程**: COMP3230B

## 目标

1. 在 **workbench2** 上搭好远程环境
2. 熟悉常用 Linux 命令
3. 用日志找可疑 SSH 失败 IP (管理员角色扮演)

## Tasks 摘要

| Task | 内容 |
|---|---|
| 1 Setup | HKUVPN → SSH `workbench2.cs.hku.hk` (Termius / VS Code Remote-SSH); 可选 Codespaces; **评分以 workbench2 为准** |
| 2 Commands | `cd` / `touch` / `mkdir` / `ls` / `grep` / 管道与重定向 / `wc` / `cat` / `ps` / `kill` / `htop`; 可用 `man` |
| 3 Practice | 解压 auth log, 用命令找出可疑失败登录 IP |

## 环境提示

- **macOS**: 用本机 Terminal 练习即可, **不需要 WSL**; 提交前仍建议在 workbench2 验证
- **Windows**: 可用 WSL 开发, 评分机仍是 workbench2
- git clone 课方 tutorial/lab 仓库 (见 PDF); subclass B 可参考 README
