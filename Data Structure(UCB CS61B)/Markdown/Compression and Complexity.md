# Compression
## 1. 文字压缩
我们考虑将字符串压缩. 我们知道Java中的每个字符被一个8-bit二进制数所表示, 那么我们如何尝试利用更少的bit数去表示字符呢?

### The problem that Morse Code meet
![](https://cs61b-2.gitbook.io/cs61b-textbook/~gitbook/image?url=https%3A%2F%2F2316889115-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCLYj7ccqvV6l4Pt9R0w5%252Fuploads%252F4s5DkbcGzBoxpRc8Bb3y%252FScreen%2520Shot%25202023-04-24%2520at%25205.44.37%2520PM.png%3Falt%3Dmedia%26token%3Dbf521f7d-02f5-4c7e-95bb-a5159e9231c7&width=768&dpr=2&quality=100&sign=b50700cb&sv=2)

我们注意到摩斯电码是一个从字符到由{长 dash, 点 dot}组成的长度不定的二元序列. 但这样就出现了一个问题, 对于一长段摩斯电码, 会存在歧义.
e.g. `MEME` 与 `GG` 具有相同的序列, 我们无法分辨.

在实际操作中, 操作员会在每个字符之间添加一个适当长度的停顿, 这实际上是引入了第三个字符, 但在二进制中我们很难进行“停顿”的操作. 我们注意到Morse Code遇到的问题实际上是因为许多序列具有 **相同的前缀** , 换而言之, 如果我们有一种匹配方式可以让不同的字符间具有不同的前缀, 那么我们就不会遇见这个问题!

### Prefix-free Codes
我们考虑以 **前缀🌲** 的视角来看待这个问题:

下图是前缀树视角下的Morse Code
![111111](https://cs61b-2.gitbook.io/cs61b-textbook/~gitbook/image?url=https%3A%2F%2F2316889115-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCLYj7ccqvV6l4Pt9R0w5%252Fuploads%252FjFQrGPOHJtKo7EvY3GaL%252Fimage.png%3Falt%3Dmedia%26token%3Dd25e6cd8-3b6f-4868-adfb-8b976526d363&width=768&dpr=2&quality=100&sign=819fd819&sv=2)

很明显的看到, 当我们沿某条路径向下遍历时, 具有相同前缀串的字符会被依次遍历到. 但是我们考虑构建一个无相同前缀的匹配方式, 也即只有叶子结点表示字符, 这样我们就可以直接读取任意字符串的二进制映射了.

也即, 对于一长度为 $n$ 的字符串 $S$, 我们就将原本的 $8n$ 长度压缩为:
$$
\sum_{c\in S}l_cf_c
$$
其中, $f_c$ 表示 $c$ 出现的频率, $l_c$ 表示 $c$ 在我们的匹配中的长度.
不难看出, 我们压缩字符串成功程度, 取决于字符出现频率与表示长度.

不难想到, 我们只要让字符出现频率高的字符匹配表示长度低, 就可以显著的降低压缩后的大小.

#### Shannon-Dano Codes
 Step1. 统计文本中所有字符的出现频率
 Step2. 根据频率大小分配Code
 Step3. 压缩
![](https://cs61b-2.gitbook.io/cs61b-textbook/~gitbook/image?url=https%3A%2F%2F2316889115-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCLYj7ccqvV6l4Pt9R0w5%252Fuploads%252F9D5OVxQfZUCbTv0pBzif%252FScreen%2520Shot%25202023-04-24%2520at%25206.06.15%2520PM.png%3Falt%3Dmedia%26token%3D1ca46da8-df1e-4bff-ba42-2f564d571a21&width=768&dpr=1&quality=100&sign=f7bfc503&sv=2)

但这种压缩方式不是最优的, 所以较少被使用.

#### Huffman Coding
Huffman编码采取 **自底向上** 的编码方式(区别于Shannon-Dano自顶向下的编码). 

Step1. 同Shannon-Dono, 统计每个字符出现频率
Step2. 合并两个频率最小的字符到同一个父结点
Step3. 重复Step2, 然后递归的直到所有节点都合并到同一个root上

![](https://cs61b-2.gitbook.io/cs61b-textbook/~gitbook/image?url=https%3A%2F%2F2316889115-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCLYj7ccqvV6l4Pt9R0w5%252Fuploads%252FHdCgQXuYkkNEwyzj9eRQ%252FScreen%2520Shot%25202023-04-24%2520at%25206.12.04%2520PM.png%3Falt%3Dmedia%26token%3D5310b79d-899a-4a9f-a708-9d049f968c74&width=768&dpr=1&quality=100&sign=860934a4&sv=2)
![](https://cs61b-2.gitbook.io/cs61b-textbook/~gitbook/image?url=https%3A%2F%2F2316889115-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FCLYj7ccqvV6l4Pt9R0w5%252Fuploads%252FSgwaQBso7fWo4Smc2EX9%252FScreen%2520Shot%25202023-04-24%2520at%25206.12.56%2520PM.png%3Falt%3Dmedia%26token%3Df36bd7a2-c9a4-4af3-bd47-61d4ad4e5a7d&width=768&dpr=1&quality=100&sign=9ef68633&sv=2)

##### Encode
对于编码环节, 我们考虑使用两种数据结构: HashMap or Array
显然使用Array会有最快的访问速度, 但是会有大量的无意义编码占据空间造成空间浪费

##### Decode
对于解码环节, 我们考虑采用 **字典树 Trie**去快捷的以 $O(n)$ 时间解码整个二进制序列.

##### In Practice
在实际操作中, 每次编码都统计该文件的字符出现频率过于繁琐, 我们有如下方式: 利用 **语料库 Corpus**:
> 我们考虑利用对各个语言的大数据统计, 提前给出频率, 设计好现成的编码规则.

但是, 不同的文件文本字符出现频率是不一样的, 所以目前主流的文件压缩方式还是提前预扫描文件作出针对该文件的encode方式. 这也是zip, gzip的工作原理.

## 2. Compression Theory

### Compression Ratios
我们用 **压缩率 Compression Ratios** $ = \frac{压缩后bit数}{原bit数}$ 来衡量压缩的效果.
有时也会使用 **节省率** $ = 1-压缩率=1-\frac{压缩后bit数}{原bit数}$ 来表示.

通常来说, 有如下几种压缩方式:
#### 1. Huffman Code
具体方式如前文所述. 通过为高频出现的符号分配code, 从而实现压缩.

#### 2. 行程长度编码 Run-Length Encoding, RLE
通过为重复出现的字符, 替换为“字符+重复次数”, 实现压缩
e.g. 
$$
啊啊啊啊啊啊啊啊宝宝你是一个宝宝\\
\rightarrow 啊8宝2你1是1一1个1宝2
$$

### 3. LZW(Lempel-Ziv-Welch) 编码
动态构建字典, 将 **重复出现的** 字符串模式替换成较短的代码. 

LZW的核心在于 **利用冗余**. i.e. 利用原文件中重复出现的pattern, 来减小储存成本. 与传统的的Huffman Code针对每个字符进行编码不同, LZW的每个Code可能对应着一串经常出现的字符串.

e.g.
`ABCABCABCBA`
如果在传统的编码中, A-1, B-2, C-3, 那么这串字符串会被压缩成`12312312321`
但LZW识别到了字符串ABC大量出现, 被编码成4, 这串字符就变成了`44421`

具体Encode步骤如下:
Step1. 先根据字符种类, 构建一个包含所有单个字符的字典.
Step2. 从输入字符串 `S` 中逐个读取字符, 直到读取到已在字典中最长的字符串 `P`
Step3. 输出 `P` 对应的Code, 并将该字符串 `P` 与其下一个字符 `c` 组合成一个新的pattern: `P+c`存入字典
Step4. 重复Step3. 直至完成压缩.

而解压过程不需要额外传输字典, 而是按照压缩的逆过程进行.
简而言之: 先初始化单字符字典, 然后逐渐解码获得原字符串与原字典.

e.g. 对字符串`ABABABA`的压缩过程
1. 初始化
   1. 字典初始化为`dic = {'A'=0, 'B'=1}`
   2. 输出压缩字符串`result = []`
2. 第一步: 读取到A
   1. `result += [0]`
   2. `dic['AB'] = 2`
3. 读取到B
   1. `result += [1]`
   2. `dic['BA'] = 3`
1. 读取到AB
   1. `result += [2]`
   2. `dic['ABA'] = 4`
1. 读取到ABA
   1. `result += [3]`
   2. `dic['ABAB'] = 4`
1. 最后输出 [0,1,2,3]
i.e. 我们完成了 ‘ABABABA->[0,1,2,3]`的压缩