# Flow-based Deep Generative Models（Lilian Weng）

## 元信息

| 项目 | 内容 |
|---|---|
| 标题 | Flow-based Deep Generative Models |
| 作者 | Lilian Weng |
| 类型 | 技术博文（Lil’Log） |
| 发表日期 | 2018-10-13 |
| 原文链接 | https://lilianweng.github.io/posts/2018-10-13-flow-models/ |
| 本地目录 | `MIT 6.S978 Deep Generative Models/Lec2/Flow-based Deep Generative Models (Lilian Weng)/` |
| 课题语境 | MIT 6.S978 Lec2 · Normalizing Flow 全景导读 |

## 本地文件

| 文件 | 说明 |
|---|---|
| [README.md](README.md) | 本文件：元信息与链接 |
| [中文总结.md](中文总结.md) | 按博文结构梳理的 Flow 全景中文笔记 |
| [中文详解-博文梳理.md](中文详解-博文梳理.md) | 分节详解（非论文式「逐节」，按博文章节） |

## 引用（原文提供）

```bibtex
@article{weng2018flow,
  title   = {Flow-based Deep Generative Models},
  author  = {Weng, Lilian},
  journal = {lilianweng.github.io},
  year    = {2018},
  url     = {https://lilianweng.github.io/posts/2018-10-13-flow-models/}
}
```

## 说明

- 博文为 2018 年综述向笔记，**不含**作者自跑的新实验表；本目录笔记不伪造实验数字。
- 原文主线含：换元 / NF 定义、NICE、RealNVP、Glow、自回归流（MADE / PixelRNN / WaveNet / MAF / IAF）、VAE+Flows。
- **FFJORD**（Grathwohl et al., ICLR 2019）发表晚于该博文，原文未专节讲解；中文笔记仅在 Lec2 对照处作简短外延，并标明非原文内容。

## 建议读法（Lec2）

先读 [中文总结.md](中文总结.md) 开头的 **「建模目的导读」**，再按「换元公式 → 耦合（NICE/RealNVP/Glow）→ MAF/IAF → VAE+Flows」扫详解；PixelRNN/WaveNet 通识可略，细节数字以各论文专文笔记为准。
