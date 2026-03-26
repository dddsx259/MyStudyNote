`NumPy` 是 Python 科学计算的基石，几乎所有数据分析库（Pandas, Scikit-learn）和深度学习框架（PyTorch, TensorFlow）都基于它。

核心概念是 **`ndarray` (N-dimensional array)**，它是一个同构的多维数组，运算速度极快（底层是 C 语言）。

以下是按功能分类的常用函数速查表：

### 0. 基础导入
```python
import numpy as np
```

---

### 1. 创建数组 (Creation)
*如何生成数据。*

| 函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`np.array()`** | 从列表/元组创建 | `np.array([1, 2, 3])` |
| **`np.zeros()`** | 全 0 数组 | `np.zeros((3, 4))` (3行4列) |
| **`np.ones()`** | 全 1 数组 | `np.ones((2, 2))` |
| **`np.full()`** | 填充指定值 | `np.full((2, 2), 7)` (全是7) |
| **`np.arange()`** | 类似 Python `range` | `np.arange(0, 10, 2)` -> `[0, 2, 4, 6, 8]` |
| **`np.linspace()`** | **等间距数列** (含端点) | `np.linspace(0, 1, 5)` -> `[0., 0.25, 0.5, 0.75, 1.]` |
| **`np.eye()`** | 单位矩阵 | `np.eye(3)` (3x3 对角线为1) |
| **`np.random.rand()`** | 0-1 均匀分布随机数 | `np.random.rand(3, 3)` |
| **`np.random.randn()`** | 标准正态分布随机数 | `np.random.randn(3, 3)` (均值0, 方差1) |
| **`np.random.randint()`**| 整数随机数 | `np.random.randint(0, 10, size=(2, 2))` |
| **`np.empty()`** | 未初始化数组 (速度快) | `np.empty((3, 3))` (内容是内存残留垃圾值) |

---

### 2. 数组属性与形状 (Shape & Info)
*查看数组长什么样。*

| 属性/函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`arr.shape`** | **形状** (行数, 列数, ...) | `(3, 4)` |
| **`arr.ndim`** | 维度数量 | `2` (二维) |
| **`arr.size`** | 元素总个数 | `12` |
| **`arr.dtype`** | 数据类型 | `float64`, `int32` |
| **`arr.reshape()`** | **改变形状** (元素总数需一致) | `arr.reshape(4, 3)` |
| **`arr.flatten()`** | 展平为一维数组 | `arr.flatten()` |
| **`arr.T`** | **转置** (行列互换) | `arr.T` |
| **`np.expand_dims()`**| 增加维度 (常用于深度学习) | `np.expand_dims(arr, axis=0)` (加一个批次维) |
| **`np.squeeze()`** | 删除长度为 1 的维度 | `np.squeeze(arr)` |

---

### 3. 索引与切片 (Indexing & Slicing)
*提取数据，语法与列表类似但更强大。*

| 语法 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`arr[0]`** | 取第一行 (一维取第一个) | - |
| **`arr[0, 1]`** | 取第 0 行第 1 列的元素 | - |
| **`arr[:, 1]`** | 取**所有行**的第 1 列 | `:` 代表全选 |
| **`arr[0:2, :]`** | 取前 2 行，所有列 | - |
| **`arr[arr > 5]`** | **布尔索引** (筛选) | 返回所有大于 5 的元素组成的 1 维数组 |
| **`np.where()`** | 返回满足条件的索引 | `np.where(arr > 5)` |
| **`np.take()`** | 按指定索引取值 | `np.take(arr, [0, 2], axis=0)` |

---

### 4. 数学运算 (Math Operations)
*NumPy 的核心优势：**向量化运算** (无需写 for 循环)。*

| 类别 | 函数/操作符 | 说明 |
| :--- | :--- | :--- |
| **基本运算** | `+`, `-`, `*`, `/`, `**` | 对应元素运算 (Element-wise)  `arr * 2` (所有元素乘2) |
| **三角/指数** | `np.sin()`, `np.cos()`, `np.exp()`, `np.log()` | 对每个元素应用函数 |
| **舍入** | `np.round()`, `np.floor()`, `np.ceil()` | 四舍五入，向下取整，向上取整 |
| **统计 (全局)** | `np.mean()`, `np.sum()`, `np.std()`, `np.min()`, `np.max()` | 计算整个数组的统计量 |
| **统计 (轴向)** | `np.sum(arr, axis=0)` | `axis=0`: 按列求和 (压缩行)`axis=1`: 按行求和 (压缩列) |
| **累积** | `np.cumsum()`, `np.cumprod()` | 累积和，累积积 |
| **差分** | `np.diff()` | 后一项减前一项 |
| **矩阵乘法** | **`np.dot()`** 或 **`@`** | **重要！** 线性代数矩阵乘法  `A @ B` 等价于 `np.dot(A, B)` |

> **⚠️ 注意 `axis` 参数**：
> - `axis=0`：沿着**行**的方向操作（结果是每列的统计值）。
> - `axis=1`：沿着**列**的方向操作（结果是每行的统计值）。
> - 口诀：**“axis 是哪个，哪个就被压缩没了”。**

---

### 5. 数组变形与合并 (Manipulation)
*拼接、分裂、堆叠数组。*

| 函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`np.concatenate()`** | 通用拼接 | `np.concatenate([a, b], axis=0)` |
| **`np.vstack()`** | 垂直堆叠 (上下拼) | 相当于 `axis=0` 的 concatenate |
| **`np.hstack()`** | 水平堆叠 (左右拼) | 相当于 `axis=1` 的 concatenate |
| **`np.split()`** | 均等分割 | `np.split(arr, 3)` (分成3份) |
| **`np.tile()`** | 重复平铺 | `np.tile([1, 2], 3)` -> `[1, 2, 1, 2, 1, 2]` |
| **`np.repeat()`** | 重复元素 | `np.repeat([1, 2], 3)` -> `[1, 1, 1, 2, 2, 2]` |

---

### 6. 线性代数 (`np.linalg`)
*专门处理矩阵运算的子模块。*

```python
import numpy as np

# 假设 A 是一个方阵
A = np.array([[1, 2], [3, 4]])

np.linalg.det(A)      # 行列式
np.linalg.inv(A)      # 逆矩阵
np.linalg.eig(A)      # 特征值和特征向量
np.linalg.norm(A)     # 范数 (默认 L2 范数)
np.linalg.solve(A, b) # 解线性方程组 Ax = b
```

---

### 7. 广播机制 (Broadcasting)
*NumPy 最强大的特性之一：不同形状的数组可以进行运算。*

**规则**：如果两个数组在后缘维度（从末尾开始数）上长度相同，或者其中一个长度为 1，则可以广播。

**经典案例**：
```python
arr = np.array([[1, 2, 3], 
                [4, 5, 6]]) # shape (2, 3)

bias = np.array([10, 20, 30]) # shape (3,)

# 自动广播：bias 会被复制成 (2, 3) 然后相加
result = arr + bias 
# 结果:
# [[11, 22, 33],
#  [14, 25, 36]]
```
*应用场景：在深度学习中，给一批数据（Batch）加上同一个偏置项（Bias）。*

---

### 💡 高频组合技 (Copy-Paste Ready)

#### 1. 归一化 (Normalization)
将数据缩放到 0-1 之间。
```python
data = np.random.rand(100, 5)
# (X - min) / (max - min)
data_norm = (data - data.min(axis=0)) / (data.max(axis=0) - data.min(axis=0))
```

#### 2. 标准化 (Standardization / Z-score)
将数据转换为均值 0，方差 1。
```python
# (X - mean) / std
data_std = (data - data.mean(axis=0)) / data.std(axis=0)
```

#### 3. One-Hot 编码 (手动版)
虽然 sklearn 有现成的，但有时需要手写。
```python
labels = np.array([0, 2, 1, 2, 0]) # 类别标签
num_classes = 3
one_hot = np.eye(num_classes)[labels]
# 结果 shape: (5, 3)
```

#### 4. 计算欧氏距离矩阵
计算一组向量两两之间的距离。
```python
# X shape: (N, D)
# 利用广播: (N, 1, D) - (1, N, D) -> (N, N, D) -> sum -> sqrt
diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
dist_matrix = np.sqrt(np.sum(diff**2, axis=-1))
```

#### 5. 安全地加载数据 (处理缺失值)
```python
# 如果 csv 里有空值，loadtxt 会报错，建议用 genfromtxt
data = np.genfromtxt('data.csv', delimiter=',', filling_values=0)
```

掌握这些，你就掌握了 NumPy 的核心。记住：**尽量避免写 `for` 循环遍历数组，多用向量化操作和广播机制**，这样代码不仅简洁，速度还能快几十倍甚至上百倍。