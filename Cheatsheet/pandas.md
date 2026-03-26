Pandas 是 Python 数据分析的核心库，其函数非常多。为了让你快速上手，我将最常用的函数按**数据处理的流程**（从读取到保存）进行了分类整理。

你可以把这份清单当作“速查表” (Cheat Sheet)。

### 1. 导入与导出 (I/O)
*数据的入口和出口，最基础的操作。*

| 函数 | 说明 | 常用参数示例 |
| :--- | :--- | :--- |
| **`pd.read_csv()`** | 读取 CSV 文件 (最常用) | `sep=','`, `encoding='utf-8'`, `usecols=['a','b']` |
| **`pd.read_excel()`** | 读取 Excel 文件 | `sheet_name='Sheet1'`, `engine='openpyxl'` |
| **`pd.read_sql()`** | 从数据库读取 SQL 查询结果 | `con=connection_object` |
| **`pd.read_json()`** | 读取 JSON 文件/字符串 | `orient='records'` |
| **`df.to_csv()`** | 保存为 CSV | `index=False` (不保存行索引), `encoding='utf-8-sig'` |
| **`df.to_excel()`** | 保存为 Excel | `sheet_name='Result'`, `index=False` |
| **`df.to_pickle()`** | 保存为二进制格式 (加载速度快) | - |

---

### 2. 查看与概览 (Inspection)
*拿到数据后的第一步：看看长什么样，有没有缺失。*

| 函数/属性 | 说明 |
| :--- | :--- |
| **`df.head(n)`** | 查看前 n 行 (默认 5 行) |
| **`df.tail(n)`** | 查看后 n 行 |
| **`df.shape`** | 返回行列数 `(rows, cols)` |
| **`df.info()`** | **极重要**：查看数据类型、非空值数量、内存占用 |
| **`df.describe()`** | **极重要**：查看数值列的统计摘要 (均值、标准差、最大最小值等) |
| **`df.columns`** | 返回所有列名 (Index 对象) |
| **`df.dtypes`** | 查看每列的数据类型 |
| **`df['col'].unique()`** | 查看某列的唯一值 (去重) |
| **`df['col'].value_counts()`** | **极重要**：统计某列每个值出现的次数 (常用于分类变量) |

---

### 3. 数据选择与过滤 (Selection & Filtering)
*提取你需要的数据子集。*

| 语法/函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`df['col']`** | 选择单列 (返回 Series) | `df['age']` |
| **`df[['col1', 'col2']]`** | 选择多列 (返回 DataFrame) | `df[['name', 'age']]` |
| **`df.loc[]`** | **基于标签**的选择 (行/列名) | `df.loc[0:5, ['name', 'age']]` |
| **`df.iloc[]`** | **基于位置**的选择 (整数索引) | `df.iloc[0:5, 0:2]` (前5行，前2列) |
| **`df[df['col'] > val]`** | **条件过滤** (布尔索引) | `df[df['age'] > 18]` |
| **`df.query()`** | 使用字符串表达式过滤 (代码更简洁) | `df.query('age > 18 and city == "Beijing"')` |
| **`df.sample()`** | 随机抽样 | `df.sample(n=100)` (随机取100行) |

---

### 4. 数据清洗 (Cleaning)
*处理缺失值、重复值和异常值。*

| 函数 | 说明 | 常用参数 |
| :--- | :--- | :--- |
| **`df.isnull()`** | 判断是否为空 (返回布尔表) | 常配合 `.sum()` 使用：`df.isnull().sum()` |
| **`df.dropna()`** | 删除包含缺失值的行/列 | `axis=1` (删列), `how='all'` (全空才删) |
| **`df.fillna()`** | 填充缺失值 | `value=0`, `method='ffill'` (前向填充), `df['col'].mean()` |
| **`df.drop_duplicates()`** | 删除重复行 | `subset=['col1']` (指定列), `keep='first'` |
| **`df.rename()`** | 重命名列名 | `columns={'old_name': 'new_name'}` |
| **`df.replace()`** | 替换特定值 | `df['col'].replace({0: 1, 2: 3})` |
| **`df.astype()`** | 转换数据类型 | `df['col'].astype('str')`, `astype('category')` |

---

### 5. 数据处理与转换 (Manipulation)
*新增列、排序、应用函数。*

| 函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`df.sort_values()`** | 按值排序 | `by='price', ascending=False` (降序) |
| **`df['new_col'] = ...`** | 新增/修改列 | `df['total'] = df['price'] * df['qty']` |
| **`df.apply()`** | **极强大**：对行或列应用函数 | `df['len'].apply(len)`, `axis=1` (按行应用) |
| **`df.map()`** | 对 Series 元素进行映射转换 | `df['city'].map({'BJ': 'Beijing'})` |
| **`pd.cut()` / `pd.qcut()`** | 分箱 (离散化) | `pd.cut(df['age'], bins=[0, 18, 60, 100])` |
| **`df.drop()`** | 删除行或列 | `columns=['col1']`, `index=[0, 1]` |

---

### 6. 聚合与分组 (Aggregation & Grouping)
*类似 SQL 的 `GROUP BY`，数据分析的核心。*

| 函数 | 说明 | 示例 |
| :--- | :--- | :--- |
| **`df.groupby()`** | 按某列分组 | `df.groupby('city')['price'].mean()` |
| **`df.pivot_table()`** | 透视表 (类似 Excel) | `index='date', columns='city', values='sales', aggfunc='sum'` |
| **`df.agg()`** | 同时计算多个统计量 | `df.groupby('city').agg({'price': ['mean', 'max'], 'qty': 'sum'})` |
| **`df.value_counts()`** | (见上文) 频数统计 | - |
| **`pd.merge()`** | 合并两个 DataFrame (类似 SQL Join) | `on='key', how='left'` (左连接) |
| **`pd.concat()`** | 上下或左右拼接多个 DataFrame | `axis=0` (上下), `axis=1` (左右) |

---

### 7. 时间序列处理 (Time Series)
*如果数据包含日期，这些函数必不可少。*

| 函数 | 说明 |
| :--- | :--- |
| **`pd.to_datetime()`** | 将字符串列转换为 datetime 对象 | `df['date'] = pd.to_datetime(df['date_str'])` |
| **`df.resample()`** | 重采样 (用于时间序列聚合) | `df.set_index('date').resample('M').mean()` (按月平均) |
| **`dt` 访问器** | 提取日期部分 | `df['date'].dt.year`, `.dt.month`, `.dt.dayofweek` |

---

### 💡 几个高频组合技 (Copy-Paste Ready)

1.  **读取并立即查看概况**：
    ```python
    df = pd.read_csv('data.csv')
    print(df.info())
    print(df.describe())
    ```

2.  **检查并填充缺失值**：
    ```python
    # 检查每列缺多少
    print(df.isnull().sum())
    # 用均值填充数值列，用 'Unknown' 填充对象列
    df['age'] = df['age'].fillna(df['age'].mean())
    df['city'] = df['city'].fillna('Unknown')
    ```

3.  **分组聚合 (GroupBy)**：
    ```python
    # 按城市分组，计算平均价格和最大销量
    result = df.groupby('city').agg({
        'price': 'mean',
        'sales': 'max'
    }).reset_index() # reset_index() 把分组列变回普通列
    ```

4.  **条件筛选并修改**：
    ```python
    # 将年龄大于 60 的人标记为 'Senior'
    df.loc[df['age'] > 60, 'group'] = 'Senior'
    ```

5.  **保存结果**：
    ```python
    df.to_csv('cleaned_data.csv', index=False, encoding='utf-8-sig')
    ```

掌握这 20% 的函数，通常能解决 80% 的日常数据分析工作。遇到复杂操作时，再查阅官方文档即可。