# Lec02 Numbers — 数是什么

- **来源**: `Lec/Lec02-Numbers/` (`slides-live-discussion*.pdf`, `slides-part1` … `part5`)
- **对应 notes**: `notes/Lec/02-Lec02-Numbers-讲义.md`

> 本讲以概念叙述为主; 出现的数学命题处已附证明/思路.

---

## 本节在课程中的位置

导论之后的第一块实质内容: 从「日常生活中的数」出发, 展示数学的 **道** (Way) — 概括 (generalization) 与抽象 (abstraction); 为后续无穷, 证明, 文化比较打基础. (材料中无独立 Lec03.)

---

## 核心论点 / 主题

### Part 1: 数与抽象

- 「三」的意义不依赖具体苹果或羊, 而在于 **一一对应** (one-to-one correspondence) 与刻痕计数 (tally).
- **数学之道** (Way of Mathematics): 从特例概括, 从具体抽象; 把问题「搬到」更易处理的数学世界.
- 考古线索: 伊尚戈骨 (Ishango bone) (课件称 >20000 年), 刻痕棒 (tally sticks) (single / split).

### Part 2: 书写数学

不同文化用不同符号系统记数:

| 系统 | 要点 (课件) |
|---|---|
| 埃及 (Egyptian) | 笔画, 脚跟骨, 绳, 睡莲等象形量级符号 |
| 巴比伦 (Babylonian) | **六十进制** (sexagesimal / hexagesimal) |
| 希腊 (Greek) | 字母表记数 |
| 罗马 (Roman) | 非进位制; 加减规则复杂, 算术困难 (如 XXXVI + XIX) |

### Part 3: 进位制与零

- **进位制** (positional system): 同一符号因位置而有不同权; 拉普拉斯 (Laplace) 赞叹十进制之精妙 (称连阿基米德 (Archimedes) 也未达此简便).
  - 十进制值 (定义): 数字串 $d_nd_{n-1}\cdots d_0$ 表示 $\sum_{k=0}^n d_k\cdot 10^k$. (定义, 无需证明.)
  - 一般基数 $b$: $\sum_{k} d_k b^k$, 其中 $0\le d_k<b$. (定义, 无需证明.)
- **零** 的必要性: 占位, 避免「空格」歧义 (34 vs 304); 玛雅 (Maya) 较早有零; 印度引入我们熟知的系统; 欧洲接受较晚.
- 多进制: 二进制 (binary), 十六进制 (hex), 六十进制 (base 60), 以及年/月/日的混合进制; 计算机用二进制, 八/十六进制作简写.

### Part 4: 其他种类的数

- 分数: 埃及特殊分数; 希腊撇号记法; 印度较近现代形式.
- **可通约** (commensurable): 毕达哥拉斯学派 (Pythagoreans) 相信任意两量可找到公共度量 → 实质认为「一切皆有理」. (信念/历史主张, 非定理.)
- $\sqrt{2}$ 不可通约 → 哲学冲击; 传说与希帕索斯 (Hippasus); 课件给出 $\sqrt{2}$ 无理性的 **反证** (reductio ad absurdum).

**命题**: $\sqrt{2}$ 不是有理数.

**证明** (反证): 设 $\sqrt{2}=p/q$, 其中 $p,q\in\mathbb{Z}^+$, $\gcd(p,q)=1$. 两边平方得 $p^2=2q^2$, 故 $p^2$ 为偶数, 从而 $p$ 为偶数 (若 $p$ 奇则 $p^2$ 奇). 令 $p=2r$, 则 $4r^2=2q^2$ 即 $q^2=2r^2$, 故 $q$ 亦偶数. 于是 $2\mid p$ 且 $2\mid q$, 与 $\gcd(p,q)=1$ 矛盾. 故 $\sqrt{2}$ 无理.

- 虚数 / 复数: $i=\sqrt{-1}$; 二次方程判别式为负时出现; 历史动机与三次方程有关. ($i$ 的引入是记号/定义扩展, 无需证明; 判别式 $b^2-4ac$ 来自配方法, 见下.)

**证明思路** (二次方程求根公式): 对 $ax^2+bx+c=0$ ($a\neq 0$),
$$
ax^2+bx+c=a\Bigl(x+\frac{b}{2a}\Bigr)^2-\frac{b^2-4ac}{4a}=0
$$
\Rightarrow $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$. 当 $b^2-4ac<0$ 时在实数内无解, 引入 $i$ 后可在复数中解.

### Part 5: 运算与抽象再升级

- 从「三加二等于五」到一般运算与 **函数** (function) (输入唯一决定输出). (函数定义: 关系 $f$ 使每个 $x$ 恰对应一个 $f(x)$; 定义, 无需证明.)
- **对数** (logarithm) (纳皮尔 (Napier)): 把乘法化为加法, 便于手算大数; $\log$ 与指数互逆.

**定义 / 恒等式**: 取定底 $b>0,b\neq 1$, 则 $\log_b(xy)=\log_b x+\log_b y$ (对 $x,y>0$).

**证明思路**: 令 $\log_b x=u$, $\log_b y=v$, 即 $b^u=x$, $b^v=y$. 则 $xy=b^u b^v=b^{u+v}$, 故 $\log_b(xy)=u+v$. 指数与对数互逆: $\log_b(b^t)=t$ 与 $b^{\log_b x}=x$ 是同一对应关系的两面 (定义层面的互逆, 无需另证).

- 总结线索: 数的种类愈广 → 理论更丰 → 反过来更理解原概念 → 更多应用; 但新数往往起初不被接受.

现场讨论 (Live discussion) 还问: 我们如何处理数? 数有文化含义吗? 数有什么用?

---

## 与课程学习成果 (Course Learning Outcomes, CLO) 的联系

| CLO | 联系 |
|---|---|
| 1 美 / 用 / 「道」 | 抽象与概括即「道」; 对数等体现「用」 |
| 2 人类文化 | 埃及 / 巴比伦 / 希腊 / 罗马 / 玛雅 / 印度书写系统 |
| 3 跨领域 | 音乐比例 (毕达哥拉斯 (Pythagoras)), 计算机进制 |
| 4 文明角色 | 计数, 贸易, 测量需求推动记数与运算 |

---

## 关键例子 / 阅读线索

- 视频: 《一的故事》 (*The Story of 1*) (英国广播公司 (BBC), 2005) — 课件标注多处时间码
- 麦克利什 (McLeish), 《数的故事》 (*The Story of Numbers*), "The language of number", p.7–20
- 克里斯滕·麦奎林 (Kristen McQuillin), 《零的简史》 (*A Brief History of Zero*)
- 《经济学人》(Economist): "Numbers: Easy as 1, 2, 3" (导论周 reading)
- 可选: 《科学美国人》(Scientific American) 脑内数字地图; 《数学从何处来》 (*Where Mathematics Comes From*)

---

## 易错点 / 讨论提示

- 把「三」等同于某个具体物体, 忽略对应关系这一抽象内核.
- 以为罗马数字「也能轻松算」; 课件强调其算术困难.
- 把「零」只当「没有」, 忽略占位功能.
- 把无理数冲击当成单纯「算错了」, 忽略对毕达哥拉斯世界观的打击.
- 课堂问卷: 自评数学能力与成因 — 可对接后文数学焦虑 (math anxiety) / 教育.
