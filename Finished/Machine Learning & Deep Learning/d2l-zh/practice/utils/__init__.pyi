# Auto-generated stub for IDE IntelliSense (Pylance).
# Runtime still loads symbols from ../utils.py via utils/__init__.py.
from __future__ import annotations
from typing import Any

def try_gpu(i: Any = ...) -> Any:
    """选择可用计算设备。

Args:
    i: GPU 编号，从 0 开始。默认 0。

Returns:
    torch.device: 存在第 i 块 GPU 时返回 ``cuda:i``，否则 ``cpu``。"""
    ...

class Accumulator:
    """在固定数量的标量上累加（loss / 正确数 / token 数等）。

Args:
    n: 累加槽位数。

Notes:
    典型用法::

        metric = Accumulator(2)
        metric.add(loss_sum, n_samples)
        avg = metric[0] / metric[1]"""
    def __init__(self, n: Any) -> None: ...
    def __getitem__(self, idx: Any) -> Any:
        """按索引读取累加值。

Args:
    idx: 槽位下标，``0 .. n-1``。

Returns:
    float: 该槽当前累加值。"""
        ...
    def add(self, *args: Any) -> Any:
        """将本批数值加到对应槽位。

Args:
    *args: 长度须等于 ``n`` 的标量序列。"""
        ...
    def reset(self) -> Any:
        """将所有累加值清零。"""
        ...

class Timer:
    """多次计时工具（接口与 d2l.Timer 一致）。

Notes:
    构造时自动 ``start()``。``stop()`` 返回秒数并记入 ``times``。"""
    def __init__(self) -> None: ...
    def avg(self) -> Any:
        """已记录各次耗时的平均值（秒）。

Returns:
    float: ``sum(times) / len(times)``。"""
        ...
    def cumsum(self) -> Any:
        """累计耗时前缀和。

Returns:
    list[float]: 与 ``times`` 等长的前缀和列表。"""
        ...
    def start(self) -> Any:
        """启动或重新启动计时，记录当前时间戳到 ``self.tik``。"""
        ...
    def stop(self) -> Any:
        """停止计时，将本次耗时（秒）追加到 ``times``。

Returns:
    float: 自上次 ``start()`` 起的秒数。"""
        ...
    def sum(self) -> Any:
        """已记录各次耗时之和（秒）。"""
        ...

def accuracy(y_hat: Any, y: Any) -> Any:
    """统计预测正确的样本个数（不是准确率比例）。

Args:
    y_hat: 预测。``(N,)`` 为类别；``(N, C)`` 时对最后一维 ``argmax``。
    y: 真实标签，形状 ``(N,)``。

Returns:
    float: 正确样本数；准确率 = 本返回值 / ``y.numel()``。"""
    ...

def evaluate_accuracy(net: Any, data_iter: Any, device: Any = ...) -> Any:
    """在整个 ``data_iter`` 上评估分类准确率。

Args:
    net: 模型；若为 ``nn.Module`` 会设为 ``eval()``。
    data_iter: 迭代 ``(X, y)``。
    device: 若给定则把 batch 搬到该设备；``None`` 不搬迁。

Returns:
    float: 正确数 / 样本数，约在 ``[0, 1]``。"""
    ...

def evaluate_loss(net: Any, data_iter: Any, loss: Any, device: Any = ...) -> Any:
    """在整个 ``data_iter`` 上评估按样本平均的损失。

Args:
    net: 模型；若为 ``nn.Module`` 会设为 ``eval()``。
    data_iter: 迭代 ``(X, y)``。
    loss: 可调用对象，约定 ``loss(net(X), y)``，再对其 ``.sum()``。
    device: 可选设备。

Returns:
    float: ``总损失 / 样本数``。"""
    ...

class Animator:
    """Jupyter 双子图训练曲线（上 loss、下 acc），供 CNN 等分类任务。

Notes:
    - 若提供 ``acc_legend`` 则画双子图，否则只画 loss 单图。
    - 追加点：``add(epoch, loss=(tr, te), acc=(tr, te))``。
    - 与 d2l 单图 ``Animator`` 不同；单图请用 ``AnimatorSimple``。"""
    def __init__(self, xlabel: Any = ..., xlim: Any = ..., loss_legend: Any = ..., acc_legend: Any = ..., acc_ylim: Any = ..., fmts: Any = ..., figsize: Any = ...) -> None: ...
    def add(self, x: Any, loss: Any = ..., acc: Any = ...) -> Any:
        """追加一个 epoch 的点并刷新显示。

Args:
    x: 横轴值（通常为 epoch）。可为标量，或与曲线条数等长的序列。
    loss: loss 曲线的 y；标量或 ``(train, test, ...)``。
    acc: acc 曲线的 y；仅当构造时提供了 ``acc_legend`` 时有效。"""
        ...
    def close(self) -> Any:
        """关闭图窗，释放资源。"""
        ...

class AnimatorSimple:
    """单图 d2l 风格 Animator，API 为 ``add(x, y)``。

Notes:
    供 ``train_net`` / Kaggle / seq2seq 等使用。多条曲线时
    ``y`` 传元组/列表，``legend`` 与之对应。"""
    def __init__(self, xlabel: Any = ..., ylabel: Any = ..., legend: Any = ..., xlim: Any = ..., ylim: Any = ..., xscale: Any = ..., yscale: Any = ..., fmts: Any = ..., nrows: Any = ..., ncols: Any = ..., figsize: Any = ...) -> None: ...
    def add(self, x: Any, y: Any) -> Any:
        """追加数据点并重绘。

Args:
    x: 横轴。标量会广播到与 ``y`` 相同条数。
    y: 纵轴。标量表示 1 条曲线；序列表示多条，如
        ``(train_loss, test_loss)``。"""
        ...
    def close(self) -> Any:
        """关闭图窗。"""
        ...

class AnimatorNoTest:
    """单图实时刷新：适合 RNN 困惑度等只有训练曲线的场景。

Notes:
    调用 ``add(x, y)``；``y`` 可为标量或序列。"""
    def __init__(self, xlabel: Any = ..., ylabel: Any = ..., xlim: Any = ..., ylim: Any = ..., legend: Any = ..., fmts: Any = ..., figsize: Any = ...) -> None: ...
    def add(self, x: Any, y: Any) -> Any:
        """追加点并刷新（无测试集的单曲线/多曲线）。

Args:
    x: 横轴值或序列。
    y: 纵轴值或序列；长度须与 ``x`` 广播后一致。"""
        ...
    def close(self) -> Any:
        """关闭图窗。"""
        ...

def sgd(params: Any, lr: Any, batch_size: Any) -> Any:
    """手写小批量 SGD：``param -= lr * grad / batch_size``。

Args:
    params: 可迭代的参数张量（需已有 ``.grad``）。
    lr: 学习率。
    batch_size: 用于把 ``loss.sum()`` 反传的梯度平均化。

Notes:
    在 ``torch.no_grad()`` 中更新，并 ``grad.zero_()``。
    若损失已 ``mean()``，通常应令 ``batch_size=1``。"""
    ...

def l2_penalty(w: Any) -> Any:
    """计算 L2 惩罚 ``||w||^2 / 2``。

Args:
    w: 权重张量。

Returns:
    Tensor: 标量惩罚项，可加到损失上：``loss + lambd * l2_penalty(w)``。"""
    ...

def sgd_with_l2(params: Any, lr: Any, batch_size: Any, lambd: Any) -> Any:
    """手写带 L2 的 SGD：``param -= lr * (grad/batch_size + lambd * param)``。

Args:
    params: 参数迭代器。
    lr: 学习率。
    batch_size: 与 ``loss.sum()`` 反传配套的批量大小。
    lambd: L2 系数（权重衰减）。"""
    ...

def dropout(X: Any, drop_prob: Any) -> Any:
    """手写 Dropout（仅训练阶段调用；推理勿用）。

Args:
    X: 输入张量，任意形状。
    drop_prob: 丢弃概率，``0 <= drop_prob <= 1``。
        ``0`` 恒等；``1`` 返回全 0。

Returns:
    Tensor: 与 ``X`` 同形；保留元素按 ``1/(1-drop_prob)`` 缩放。"""
    ...

def grad_clipping(net: Any, theta: Any) -> Any:
    """按全局 L2 范数裁剪梯度：若 ``||g|| > theta`` 则缩放至 ``theta``。

Args:
    net: ``nn.Module``，或带 ``.params`` 列表的从零实现模型。
    theta: 梯度范数上限（正数），如 ``1``。

Notes:
    应在 ``loss.backward()`` 之后、``optimizer.step()`` 之前调用。"""
    ...

def load_data_fashion_mnist(batch_size: Any, resize: Any = ..., root: Any = ...) -> Any:
    """下载 Fashion-MNIST，返回训练/测试 DataLoader。

Args:
    batch_size: 批量大小。
    resize: 若给定（如 ``224``），先 ``Resize`` 再 ``ToTensor``。
    root: 数据根目录。

Returns:
    tuple: ``(train_iter, test_iter)``；batch 为 ``(X, y)``，
    ``X`` 形状约 ``(B, 1, H, W)``，``y`` 为类别下标。"""
    ...

def generate_data_of_linear_regression_with_noise(n_inputs: Any, n_train: Any, n_test: Any, batch_size: Any = ..., W: Any = ..., b: Any = ..., noise: Any = ...) -> Any:
    """合成带噪声的线性回归数据：``y = XW + b + noise``。

Args:
    n_inputs: 特征维数。
    n_train: 训练样本数。
    n_test: 测试样本数。
    batch_size: DataLoader 批量。
    W: 真实权重 ``(n_inputs, 1)``；默认 ``N(0,1)``。
    b: 真实偏置；默认 0。
    noise: 噪声 ``(n_train+n_test, 1)``；默认 ``N(0, 0.01)``。

Returns:
    tuple: ``(W, b, train_iter, test_iter)``。"""
    ...

DATA_HUB: Any

def download(name: Any, cache_dir: Any = ...) -> Any:
    """按 ``DATA_HUB`` 下载并缓存文件；已存在且 SHA1 匹配则跳过。

Args:
    name: ``DATA_HUB`` 中的键，如 ``'time_machine'``。
    cache_dir: 本地缓存目录。

Returns:
    str: 本地文件路径。"""
    ...

def read_time_machine() -> Any:
    """下载并读取《时间机器》全书为文本行列表。

Returns:
    list[str]: 每行一个字符串（含换行符，与 ``readlines()`` 一致）。"""
    ...

def tokenize(lines: Any, token: Any = ..., clean_en: Any = ...) -> Any:
    """将文本行列表拆成词元列表的列表。

Args:
    lines: ``list[str]``，每行一段文本。
    token: ``'word'`` 按空白分词；``'char'`` 按字符。
    clean_en: 为 True 时先把非英文字母替换为空格并转小写。

Returns:
    list[list[str]]: 与 ``lines`` 对齐的词元序列。"""
    ...

def count_corpus(tokens: Any) -> Any:
    """统计词元出现频率。

Args:
    tokens: 一维 ``list[str]``，或二维 ``list[list[str]]``（会展平）。

Returns:
    collections.Counter: ``{token: freq}``。"""
    ...

class Vocab:
    """文本词表。

Notes:
    - ``<unk>`` 固定索引 0。
    - 构造顺序：``['<unk>'] + reserved_tokens + 高频词``。
    - ``vocab[token]`` / ``vocab[list]`` 查索引；未知 -> 0。
    - ``vocab.to_tokens(ids)`` 索引还原为词。"""
    def __init__(self, tokens: Any = ..., min_freq: Any = ..., reserved_tokens: Any = ...) -> None: ...
    def __getitem__(self, tokens: Any) -> Any:
        """词元 -> 索引；未知词返回 ``unk`` (0)。

Args:
    tokens: 单个 ``str``，或 ``list/tuple[str]``。

Returns:
    int | list[int]: 索引或索引列表。"""
        ...
    def __len__(self) -> Any:
        ...
    def to_tokens(self, indices: Any) -> Any:
        """索引 -> 词元。

Args:
    indices: 单个 ``int``，或 ``list/tuple[int]``。

Returns:
    str | list[str]: 词元或词元列表。"""
        ...
    @property
    def token_freqs(self) -> Any: ...
    @property
    def unk(self) -> Any: ...

class SeqDataLoader:
    """语言模型用序列数据迭代器。

Notes:
    迭代产出 ``(X, Y)``，形状均为 ``(batch_size, num_steps)``，
    ``Y`` 为 ``X`` 向后错一位的下一个词元。
    ``mode='random'`` 随机采样子序列；``'sequential'`` 顺序划分。"""
    def __init__(self, batch_size: Any, num_steps: Any, corpus: Any = ..., vocab: Any = ..., mode: Any = ...) -> None: ...
    def seq_data_iter_random(self, corpus: Any, batch_size: Any, num_steps: Any) -> Any:
        """随机采样子序列的迭代器。

Yields:
    tuple[Tensor, Tensor]: ``(X, Y)``，形状 ``(batch_size, num_steps)``。"""
        ...
    def seq_data_iter_sequential(self, corpus: Any, batch_size: Any, num_steps: Any) -> Any:
        """顺序划分子序列的迭代器。

Yields:
    tuple[Tensor, Tensor]: ``(X, Y)``，形状 ``(batch_size, num_steps)``。"""
        ...

def truncate_pad(line: Any, num_steps: Any, padding_token: Any) -> Any:
    """将序列截断或填充到长度 ``num_steps``。

Args:
    line: 一维序列（词元或索引列表）。
    num_steps: 目标长度。
    padding_token: 填充值（索引或词元，与 ``line`` 元素类型一致）。

Returns:
    list: 长度为 ``num_steps`` 的新序列（过长截断，过短右侧 pad）。"""
    ...

def build_array_nmt(lines: Any, num_steps: Any, pad: Any = ...) -> Any:
    """批量索引序列 -> 定长张量与有效长度。

Args:
    lines: ``list[list[int]]``，每行一句的索引。
    num_steps: 截断/填充长度。
    pad: 填充索引，默认 0（常为 ``<unk>``；有 ``<pad>`` 时请传入其 id）。

Returns:
    tuple:
        - array: ``LongTensor``，形状 ``(num_lines, num_steps)``。
        - valid_len: ``IntTensor``，形状 ``(num_lines,)``，非 pad 个数。"""
    ...

def load_data_cmn_eng(data_path: Any) -> Any:
    """读取 Tatoeba 中英平行语料（``cmn.txt``）。

Args:
    data_path: 语料路径；每行用制表符分隔为「英文、中文、版权信息」。

Returns:
    tuple[list, list]:
        - Xs: 英文词元序列列表；每句为「词列表 + ``'<eos>'``」。
        - Ys: 中文字符序列列表；每句为「字列表 + ``'<eos>'``」。

Notes:
    - 会去掉句末标点（英文去末词最后一字符，中文去掉最后一字）。
    - **不含** ``<bos>``；``<bos>`` 只在 ``train_seq2seq`` / 解码时使用。
    - 别名：``load_data_TdBSP``。"""
    ...

def load_data_TdBSP(data_path: Any) -> Any:
    """读取 Tatoeba 中英平行语料（``cmn.txt``）。

Args:
    data_path: 语料路径；每行用制表符分隔为「英文、中文、版权信息」。

Returns:
    tuple[list, list]:
        - Xs: 英文词元序列列表；每句为「词列表 + ``'<eos>'``」。
        - Ys: 中文字符序列列表；每句为「字列表 + ``'<eos>'``」。

Notes:
    - 会去掉句末标点（英文去末词最后一字符，中文去掉最后一字）。
    - **不含** ``<bos>``；``<bos>`` 只在 ``train_seq2seq`` / 解码时使用。
    - 别名：``load_data_TdBSP``。"""
    ...

def preprocess_nmt(Xs: Any, Ys: Any, reserved_tokens: Any = ...) -> Any:
    """为平行语料构建源/目标词表并转为索引。

Args:
    Xs: 源语言句子，``list[list[str]]``；若 ``Xs[0]`` 为 ``str`` 则先
        ``tokenize(..., token='word')``。
    Ys: 目标语言句子，格式同 ``Xs``。
    reserved_tokens: 写入两个词表的保留词，默认 ``['<bos>', '<eos>']``。
        ``<unk>`` 仍由 ``Vocab`` 自动插在最前（索引 0）。

Returns:
    tuple:
        - X: ``list[list[int]]`` 源索引。
        - Y: ``list[list[int]]`` 目标索引。
        - src_vocab, tgt_vocab: 两个 ``Vocab``。

Notes:
    别名：``preprocess_data``。"""
    ...

def preprocess_data(Xs: Any, Ys: Any, reserved_tokens: Any = ...) -> Any:
    """为平行语料构建源/目标词表并转为索引。

Args:
    Xs: 源语言句子，``list[list[str]]``；若 ``Xs[0]`` 为 ``str`` 则先
        ``tokenize(..., token='word')``。
    Ys: 目标语言句子，格式同 ``Xs``。
    reserved_tokens: 写入两个词表的保留词，默认 ``['<bos>', '<eos>']``。
        ``<unk>`` 仍由 ``Vocab`` 自动插在最前（索引 0）。

Returns:
    tuple:
        - X: ``list[list[int]]`` 源索引。
        - Y: ``list[list[int]]`` 目标索引。
        - src_vocab, tgt_vocab: 两个 ``Vocab``。

Notes:
    别名：``preprocess_data``。"""
    ...

def data_loader_nmt(X: Any, Y: Any, batch_size: Any, num_steps: Any, pad: Any = ..., shuffle: Any = ...) -> Any:
    """将平行语料索引打成训练用 DataLoader。

Args:
    X, Y: ``list[list[int]]``，已索引化的源/目标句。
    batch_size: 批量大小。
    num_steps: 截断/填充长度。
    pad: 填充索引，默认 0；若词表有 ``<pad>`` 请传 ``vocab['<pad>']``。
    shuffle: 是否打乱。

Returns:
    DataLoader: 每个 batch 为
    ``(X, X_valid_len, Y, Y_valid_len)``，
    形状 ``(B,T) / (B,) / (B,T) / (B,)``。

Notes:
    别名：``data_loader_TdBSP``。"""
    ...

def data_loader_TdBSP(X: Any, Y: Any, batch_size: Any, num_steps: Any, pad: Any = ..., shuffle: Any = ...) -> Any:
    """将平行语料索引打成训练用 DataLoader。

Args:
    X, Y: ``list[list[int]]``，已索引化的源/目标句。
    batch_size: 批量大小。
    num_steps: 截断/填充长度。
    pad: 填充索引，默认 0；若词表有 ``<pad>`` 请传 ``vocab['<pad>']``。
    shuffle: 是否打乱。

Returns:
    DataLoader: 每个 batch 为
    ``(X, X_valid_len, Y, Y_valid_len)``，
    形状 ``(B,T) / (B,) / (B,T) / (B,)``。

Notes:
    别名：``data_loader_TdBSP``。"""
    ...

def sequence_mask(X: Any, valid_len: Any, value: Any = ...) -> Any:
    """按有效长度遮蔽序列第二维（常用于 mask loss 权重）。

Args:
    X: 张量，至少二维，形状 ``(batch, seq_len, ...)``；本函数按
        ``X.size(1)`` 与 ``valid_len`` 比较。
    valid_len: ``(batch,)``，每个样本的有效长度。
    value: 无效位置（padding）要写入的值。

Returns:
    Tensor: 与 ``X`` 同形的克隆；位置 ``j >= valid_len[i]`` 被设为 ``value``。

Notes:
    别名：``seq_mask``。"""
    ...

def seq_mask(X: Any, valid_len: Any, value: Any = ...) -> Any:
    """按有效长度遮蔽序列第二维（常用于 mask loss 权重）。

Args:
    X: 张量，至少二维，形状 ``(batch, seq_len, ...)``；本函数按
        ``X.size(1)`` 与 ``valid_len`` 比较。
    valid_len: ``(batch,)``，每个样本的有效长度。
    value: 无效位置（padding）要写入的值。

Returns:
    Tensor: 与 ``X`` 同形的克隆；位置 ``j >= valid_len[i]`` 被设为 ``value``。

Notes:
    别名：``seq_mask``。"""
    ...

class MaskedSoftmaxCELoss:
    """带长度遮蔽的 Softmax 交叉熵（机器翻译常用）。

Notes:
    padding 位置权重为 0；对时间维做 ``mean`` 后返回每样本损失。"""
    def __init__(self, weight: Any = ..., size_average: Any = ..., ignore_index: Any = ..., reduce: Any = ..., reduction: Any = ..., label_smoothing: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, pred: Any, label: Any, valid_len: Any) -> Any:
        """计算 batch 内逐样本的 masked CE。

Args:
    pred: logits，``(batch, seq_len, vocab_size)``。
    label: 类别下标，``(batch, seq_len)``。
    valid_len: 有效长度，``(batch,)``。

Returns:
    Tensor: 形状 ``(batch,)``，每个样本一个标量损失。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

class EncoderDecoder:
    """编码器-解码器组合外壳。

Notes:
    要求 ``decoder`` 实现 ``init_state(enc_outputs, *args)``。
    前向：``encode -> init_state -> decode``。"""
    def __init__(self, encoder: Any, decoder: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, enc_X: Any, dec_X: Any, *args: Any) -> Any:
        """一次编码-解码前向。

Args:
    enc_X: 源序列，通常 ``(batch, src_len)``。
    dec_X: 解码器输入（训练时为强制教学序列）。
    *args: 传给 encoder / ``init_state`` 的额外参数，如 ``X_valid_len``。

Returns:
    decoder 的返回值，常见为 ``(Y_hat, state)``。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

def train_seq2seq(net: Any, data_iter: Any, lr: Any, num_epochs: Any, tgt_vocab: Any, device: Any) -> Any:
    """训练 Seq2Seq：Xavier 初始化、Adam、强制教学、梯度裁剪。

Args:
    net: ``EncoderDecoder``（或同接口模型）。
    data_iter: 产出 ``(X, X_valid_len, Y, Y_valid_len)``。
    lr: Adam 学习率。
    num_epochs: 训练轮数；每 10 轮画一次 loss。
    tgt_vocab: 目标词表，须含 ``'<bos>'``。
    device: ``torch.device``。

Notes:
    - 标签 ``Y`` 应为「内容 + ``<eos>``」，**不要**自带 ``<bos>``。
    - 解码输入：``dec_input = [<bos>] + Y[:, :-1]``。
    - 损失为 ``MaskedSoftmaxCELoss``；更新前 ``grad_clipping(net, 1)``。"""
    ...

def translate_seq2seq(net: Any, src_sentence: Any, src_vocab: Any, tgt_vocab: Any, num_steps: Any, device: Any, pad: Any = ..., src_tokenize: Any = ..., tgt_join: Any = ...) -> Any:
    """贪心解码：将源句翻译成目标字符串。

Args:
    net: 含 ``encoder`` / ``decoder`` 的 Seq2Seq 模型（已训练）。
    src_sentence: 源语言字符串。
    src_vocab, tgt_vocab: 源/目标 ``Vocab``；目标须含 ``'<bos>'``/``'<eos>'``。
    num_steps: 编码 pad 长度与最大解码步数。
    device: 计算设备。
    pad: 源序列填充索引，默认 0。
    src_tokenize: ``'word'`` 空格分词并去掉末词最后一字符标点；
        ``'char'`` 按字符并去掉最后一个字符（标点）。
    tgt_join: 目标词元拼接符；中文常用 ``''``，英文常用 ``' '``。

Returns:
    str: 解码得到的目标文本（不含 ``<eos>``）。

Notes:
    别名：``translate``。"""
    ...

def translate(net: Any, src_sentence: Any, src_vocab: Any, tgt_vocab: Any, num_steps: Any, device: Any, pad: Any = ..., src_tokenize: Any = ..., tgt_join: Any = ...) -> Any:
    """贪心解码：将源句翻译成目标字符串。

Args:
    net: 含 ``encoder`` / ``decoder`` 的 Seq2Seq 模型（已训练）。
    src_sentence: 源语言字符串。
    src_vocab, tgt_vocab: 源/目标 ``Vocab``；目标须含 ``'<bos>'``/``'<eos>'``。
    num_steps: 编码 pad 长度与最大解码步数。
    device: 计算设备。
    pad: 源序列填充索引，默认 0。
    src_tokenize: ``'word'`` 空格分词并去掉末词最后一字符标点；
        ``'char'`` 按字符并去掉最后一个字符（标点）。
    tgt_join: 目标词元拼接符；中文常用 ``''``，英文常用 ``' '``。

Returns:
    str: 解码得到的目标文本（不含 ``<eos>``）。

Notes:
    别名：``translate``。"""
    ...

def train_epoch(net: Any, train_iter: Any, loss: Any, net_type: Any = ..., updater: Any = ..., device: Any = ...) -> Any:
    """训练一个 epoch。

Args:
    net: 模型。
    train_iter: 迭代 ``(X, y)``。
    loss: 损失函数 ``loss(y_hat, y)``。
    net_type: ``'Classification'`` 或 ``'Regression'``。
    updater: ``torch.optim.Optimizer``，或自定义 ``updater(batch_size)``
        （配合 ``loss.sum()`` + 手写 ``sgd``）。
    device: 可选设备。

Returns:
    Classification: ``(train_loss, train_acc)``。
    Regression: ``(train_loss,)``。"""
    ...

def train_net(net: Any, train_iter: Any, test_iter: Any, loss: Any, num_epochs: Any, net_type: Any = ..., updater: Any = ..., animate: Any = ..., device: Any = ...) -> Any:
    """通用 MLP/Softmax 训练循环，使用 ``AnimatorSimple`` 画曲线。

Args:
    net: 模型。
    train_iter, test_iter: 数据迭代器。
    loss: 损失函数。
    num_epochs: 轮数。
    net_type: ``'Classification'`` 或 ``'Regression'``。
    updater: 优化器或自定义更新函数；**必填**。
    animate: 是否动态绘图。
    device: 可选设备。

Returns:
    tuple: 最后一轮指标。分类为
    ``(train_loss, train_acc, test_acc)``；回归为
    ``(train_loss, test_loss)``。"""
    ...

def train_cnn(net: Any, train_iter: Any, test_iter: Any, loss: Any = ..., optimizer: Any = ..., num_epochs: Any = ..., lr: Any = ..., device: Any = ..., task: Any = ...) -> Any:
    """CNN 训练循环：双子图 ``Animator``，默认 Adam。

Args:
    net: CNN 模型。
    train_iter, test_iter: 迭代 ``(X, y)``。
    loss: 默认分类 ``CrossEntropyLoss``，回归 ``MSELoss``。
    optimizer: 默认 ``Adam(lr=lr)``。
    num_epochs: 轮数。
    lr: 仅在未传入 optimizer 时使用。
    device: 默认 ``try_gpu()``。
    task: ``'classification'`` 或其它（回归，只画 loss）。

Returns:
    tuple: 分类 ``(train_loss, train_acc, test_loss, test_acc)``；
    回归 ``(train_loss, test_loss)``。"""
    ...

def predict_rnn(prefix: Any, num_preds: Any, net: Any, vocab: Any, device: Any) -> Any:
    """给定前缀，用 RNN 自回归生成后续词元。

Args:
    prefix: 字符串前缀（按字符迭代；与字符级词表配套）。
    num_preds: 在预热 prefix 后要生成的词元个数。
    net: 需实现 ``begin_state`` 与 ``net(X, state) -> (y, state)``。
    vocab: ``Vocab``。
    device: 设备。

Returns:
    str: 生成文本（词元以空格拼接的简单格式）。"""
    ...

def train_epoch_rnn(net: Any, train_iter: Any, loss: Any, updater: Any, device: Any, use_random_iter: Any) -> Any:
    """训练 RNN 一个 epoch。

Args:
    net: RNN 模型（``nn.Module`` 或从零实现）。
    train_iter: 产出 ``(X, Y)``，``X`` 为 ``(batch, num_steps)``。
    loss: 通常 ``nn.CrossEntropyLoss()``。
    updater: Optimizer 或 ``lambda batch_size: sgd(...)``。
    device: 设备。
    use_random_iter: True 时每 batch 重置隐状态（配合随机采样迭代器）。

Returns:
    float: 本 epoch 困惑度 ``exp(平均交叉熵)``。"""
    ...

def train_rnn(net: Any, train_iter: Any, vocab: Any, lr: Any, num_epochs: Any, device: Any, use_random_iter: Any = ..., prefix: Any = ...) -> Any:
    """RNN 完整训练：画困惑度、早停、结束时生成示例。

Args:
    net: RNN 模型。
    train_iter: 语言建模数据迭代器。
    vocab: 词表。
    lr: SGD 学习率（``nn.Module``）或手写 sgd 的 lr。
    num_epochs: 最大轮数。
    device: 设备。
    use_random_iter: 是否按随机子序列训练。
    prefix: 训练结束后 ``predict_rnn`` 使用的前缀。

Returns:
    float: 最终（或早停时）困惑度。

Notes:
    若连续 5 次困惑度下降小于 ``1e-3`` 则早停。"""
    ...

def normal(shape: Any, device: Any) -> Any:
    """从 ``N(0, 0.01)`` 采样初始化张量。

Args:
    shape: 形状，传给 ``torch.randn``。
    device: 设备。

Returns:
    Tensor: 标准差 0.01 的正态随机张量。"""
    ...

class RNNModelScratch:
    """从零实现 RNN 的薄包装（参数/状态/前向均由外部函数提供）。

Notes:
    调用：``output, state = model(X, state)``，其中 ``X`` 为
    ``(batch, num_steps)`` 的词索引，内部会 one-hot 成
    ``(num_steps, batch, vocab_size)``。"""
    def __init__(self, vocab_size: Any, num_hiddens: Any, device: Any, get_params: Any, init_state: Any, forward_fn: Any) -> None: ...
    def __call__(self, X: Any, state: Any) -> Any:
        """Args:
    X: 词索引 ``(batch_size, num_steps)``。
    state: 由 ``begin_state`` 得到的隐状态。

Returns:
    forward_fn 的返回值，通常为 ``(output, new_state)``。"""
        ...
    def begin_state(self, batch_size: Any, device: Any) -> Any:
        """返回初始隐状态。

Args:
    batch_size: 批量大小。
    device: 设备。"""
        ...

class RNNModel:
    """封装 ``nn.RNN`` / ``GRU`` / ``LSTM`` + 线性词表投影。

Notes:
    ``forward(inputs, state)`` 中 ``inputs`` 为 ``(batch, num_steps)``；
    返回 ``(output, state)``，``output`` 形状 ``(batch*num_steps, vocab)``。"""
    def __init__(self, rnn_layer: Any, vocab_size: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def begin_state(self, device: Any, batch_size: Any = ...) -> Any:
        """构造零初始状态。

Args:
    device: 设备。
    batch_size: 批量大小，默认 1。

Returns:
    Tensor | tuple[Tensor, Tensor]: GRU/RNN 为隐状态；LSTM 为 ``(h, c)``。"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, inputs: Any, state: Any) -> Any:
        """前向计算。

Args:
    inputs: 词索引，形状 ``(batch_size, num_steps)``。
    state: RNN/GRU 隐状态，或 LSTM 的 ``(h, c)``。

Returns:
    tuple: ``(output, state)``；``output`` 形状
    ``(batch_size * num_steps, vocab_size)``。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

def vgg_block(num_convs: Any, in_channels: Any, out_channels: Any) -> Any:
    """构造一个 VGG 卷积块：``num_convs`` 个 3x3 Conv-ReLU + MaxPool2d。

Args:
    num_convs: 卷积层个数。
    in_channels: 输入通道。
    out_channels: 输出通道（块内各卷积相同）。

Returns:
    nn.Sequential: 该块；空间尺寸经池化后约为原来 1/2。"""
    ...

class VGGNet:
    """按 ``arch`` 描述堆叠的 VGG 分类网络。

Notes:
    ``arch`` 形如 ``((num_convs, out_channels), ...)``。
    别名：``vggNet``。"""
    def __init__(self, arch: Any, in_channels: Any, pic_size: Any, num_classes: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, X: Any) -> Any:
        """Args:
    X: 图像张量 ``(batch, in_channels, H, W)``，``H,W`` 应与构造时
        ``pic_size`` 一致。

Returns:
    Tensor: logits，形状 ``(batch, num_classes)``。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

class vggNet:
    """按 ``arch`` 描述堆叠的 VGG 分类网络。

Notes:
    ``arch`` 形如 ``((num_convs, out_channels), ...)``。
    别名：``vggNet``。"""
    def __init__(self, arch: Any, in_channels: Any, pic_size: Any, num_classes: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, X: Any) -> Any:
        """Args:
    X: 图像张量 ``(batch, in_channels, H, W)``，``H,W`` 应与构造时
        ``pic_size`` 一致。

Returns:
    Tensor: logits，形状 ``(batch, num_classes)``。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

class Corr2D:
    """二维互相关（卷积教学实现，无 padding/stride）。

Notes:
    输入 ``X`` 为二维 ``(H, W)``；输出尺寸
    ``(H-kh+1, W-kw+1)``。别名：``corr2D``。"""
    def __init__(self, kernel: Any = ..., kernel_size: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, X: Any) -> Any:
        """二维互相关前向。

Args:
    X: 二维输入 ``(H, W)``（教学示例，无 batch/channel 维）。

Returns:
    Tensor: ``(H-kh+1, W-kw+1)``，已加 bias。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

class corr2D:
    """二维互相关（卷积教学实现，无 padding/stride）。

Notes:
    输入 ``X`` 为二维 ``(H, W)``；输出尺寸
    ``(H-kh+1, W-kw+1)``。别名：``corr2D``。"""
    def __init__(self, kernel: Any = ..., kernel_size: Any = ...) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        ...
    def add_module(self, name: Any, module: Any) -> Any:
        """Add a child module to the current module.

The module can be accessed as an attribute using the given name.

Args:
    name (str): name of the child module. The child module can be
        accessed from this module using the given name
    module (Module): child module to be added to the module."""
        ...
    def apply(self, fn: Any) -> Any:
        """Apply ``fn`` recursively to every submodule (as returned by ``.children()``) as well as self.

Typical use includes initializing the parameters of a model
(see also :ref:`nn-init-doc`).

Args:
    fn (:class:`Module` -> None): function to be applied to each submodule

Returns:
    Module: self

Example::

    >>> @torch.no_grad()
    >>> def init_weights(m):
    >>>     print(m)
    >>>     if type(m) is nn.Linear:
    >>>         m.weight.fill_(1.0)
    >>>         print(m.weight)
    >>> net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
    >>> net.apply(init_weights)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Linear(in_features=2, out_features=2, bias=True)
    Parameter containing:
    tensor([[1., 1.],
            [1., 1.]], requires_grad=True)
    Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )"""
        ...
    def bfloat16(self) -> Any:
        """Casts all floating point parameters and buffers to ``bfloat16`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def buffers(self, recurse: Any = ...) -> Any:
        """Return an iterator over module buffers.

Args:
    recurse (bool): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module.

Yields:
    torch.Tensor: module buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for buf in model.buffers():
    >>>     print(type(buf), buf.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def children(self) -> Any:
        """Return an iterator over immediate children modules.

Yields:
    Module: a child module"""
        ...
    def compile(self, *args: Any, **kwargs: Any) -> Any:
        """Compile this Module's forward using :func:`torch.compile`.

This Module's `__call__` method is compiled and all arguments are passed as-is
to :func:`torch.compile`.

See :func:`torch.compile` for details on the arguments for this function."""
        ...
    def cpu(self) -> Any:
        """Move all model parameters and buffers to the CPU.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def cuda(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the GPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on GPU while being optimized.

.. note::
    This method modifies the module in-place.

Args:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def double(self) -> Any:
        """Casts all floating point parameters and buffers to ``double`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def eval(self) -> Any:
        """Set the module in evaluation mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e. whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

This is equivalent with :meth:`self.train(False) <torch.nn.Module.train>`.

See :ref:`locally-disable-grad-doc` for a comparison between
`.eval()` and several similar mechanisms that may be confused with it.

Returns:
    Module: self"""
        ...
    def extra_repr(self) -> Any:
        """Return the extra representation of the module.

To print customized extra information, you should re-implement
this method in your own modules. Both single-line and multi-line
strings are acceptable."""
        ...
    def float(self) -> Any:
        """Casts all floating point parameters and buffers to ``float`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def forward(self, X: Any) -> Any:
        """二维互相关前向。

Args:
    X: 二维输入 ``(H, W)``（教学示例，无 batch/channel 维）。

Returns:
    Tensor: ``(H-kh+1, W-kw+1)``，已加 bias。"""
        ...
    def get_buffer(self, target: Any) -> Any:
        """Return the buffer given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the buffer
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.Tensor: The buffer referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not a
        buffer"""
        ...
    def get_extra_state(self) -> Any:
        """Return any extra state to include in the module's state_dict.

Implement this and a corresponding :func:`set_extra_state` for your module
if you need to store extra state. This function is called when building the
module's `state_dict()`.

Note that extra state should be picklable to ensure working serialization
of the state_dict. We only provide backwards compatibility guarantees
for serializing Tensors; other objects may break backwards compatibility if
their serialized pickled form changes.

Returns:
    object: Any extra state to store in the module's state_dict"""
        ...
    def get_parameter(self, target: Any) -> Any:
        """Return the parameter given by ``target`` if it exists, otherwise throw an error.

See the docstring for ``get_submodule`` for a more detailed
explanation of this method's functionality as well as how to
correctly specify ``target``.

Args:
    target: The fully-qualified string name of the Parameter
        to look for. (See ``get_submodule`` for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Parameter: The Parameter referenced by ``target``

Raises:
    AttributeError: If the target string references an invalid
        path or resolves to something that is not an
        ``nn.Parameter``"""
        ...
    def get_submodule(self, target: Any) -> Any:
        """Return the submodule given by ``target`` if it exists, otherwise throw an error.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(16, 33, kernel_size=(3, 3), stride=(2, 2))
            )
            (linear): Linear(in_features=100, out_features=200, bias=True)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` which has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To check whether or not we have the ``linear`` submodule, we
would call ``get_submodule("net_b.linear")``. To check whether
we have the ``conv`` submodule, we would call
``get_submodule("net_b.net_c.conv")``.

The runtime of ``get_submodule`` is bounded by the degree
of module nesting in ``target``. A query against
``named_modules`` achieves the same result, but it is O(N) in
the number of transitive modules. So, for a simple check to see
if some submodule exists, ``get_submodule`` should always be
used.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)

Returns:
    torch.nn.Module: The submodule referenced by ``target``

Raises:
    AttributeError: If at any point along the path resulting from
        the target string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def half(self) -> Any:
        """Casts all floating point parameters and buffers to ``half`` datatype.

.. note::
    This method modifies the module in-place.

Returns:
    Module: self"""
        ...
    def ipu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the IPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on IPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def load_state_dict(self, state_dict: Any, strict: Any = ..., assign: Any = ...) -> Any:
        """Copy parameters and buffers from :attr:`state_dict` into this module and its descendants.

If :attr:`strict` is ``True``, then
the keys of :attr:`state_dict` must exactly match the keys returned
by this module's :meth:`~torch.nn.Module.state_dict` function.

.. warning::
    If :attr:`assign` is ``True`` the optimizer must be created after
    the call to :attr:`load_state_dict` unless
    :func:`~torch.__future__.get_swap_module_params_on_conversion` is ``True``.

Args:
    state_dict (dict): a dict containing parameters and
        persistent buffers.
    strict (bool, optional): whether to strictly enforce that the keys
        in :attr:`state_dict` match the keys returned by this module's
        :meth:`~torch.nn.Module.state_dict` function. Default: ``True``
    assign (bool, optional): When set to ``False``, the properties of the tensors
        in the current module are preserved whereas setting it to ``True`` preserves
        properties of the Tensors in the state dict. The only
        exception is the ``requires_grad`` field of :class:`~torch.nn.Parameter`
        for which the value from the module is preserved. Default: ``False``

Returns:
    ``NamedTuple`` with ``missing_keys`` and ``unexpected_keys`` fields:
        * ``missing_keys`` is a list of str containing any keys that are expected
            by this module but missing from the provided ``state_dict``.
        * ``unexpected_keys`` is a list of str containing the keys that are not
            expected by this module but present in the provided ``state_dict``.

Note:
    If a parameter or buffer is registered as ``None`` and its corresponding key
    exists in :attr:`state_dict`, :meth:`load_state_dict` will raise a
    ``RuntimeError``."""
        ...
    def modules(self, remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network.

Args:
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not.

Yields:
    Module: a module in the network

Note:
    Duplicate modules are returned only once by default. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.modules()):
    ...     print(idx, '->', m)

    0 -> Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    )
    1 -> Linear(in_features=2, out_features=2, bias=True)"""
        ...
    def mtia(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the MTIA.

This also makes associated parameters and buffers different objects. So
it should be called before constructing the optimizer if the module will
live on MTIA while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def named_buffers(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module buffers, yielding both the name of the buffer as well as the buffer itself.

Args:
    prefix (str): prefix to prepend to all buffer names.
    recurse (bool, optional): if True, then yields buffers of this module
        and all submodules. Otherwise, yields only buffers that
        are direct members of this module. Defaults to True.
    remove_duplicate (bool, optional): whether to remove the duplicated buffers in the result. Defaults to True.

Yields:
    (str, torch.Tensor): Tuple containing the name and buffer

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, buf in self.named_buffers():
    >>>     if name in ['running_var']:
    >>>         print(buf.size())"""
        ...
    def named_children(self) -> Any:
        """Return an iterator over immediate children modules, yielding both the name of the module as well as the module itself.

Yields:
    (str, Module): Tuple containing a name and child module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, module in model.named_children():
    >>>     if name in ['conv4', 'conv5']:
    >>>         print(module)"""
        ...
    def named_modules(self, memo: Any = ..., prefix: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over all modules in the network, yielding both the name of the module as well as the module itself.

Args:
    memo: a memo to store the set of modules already added to the result
    prefix: a prefix that will be added to the name of the module
    remove_duplicate: whether to remove the duplicated module instances in the result
        or not

Yields:
    (str, Module): Tuple of name and module

Note:
    Duplicate modules are returned only once. In the following
    example, ``l`` will be returned only once.

Example::

    >>> l = nn.Linear(2, 2)
    >>> net = nn.Sequential(l, l)
    >>> for idx, m in enumerate(net.named_modules()):
    ...     print(idx, '->', m)

    0 -> ('', Sequential(
      (0): Linear(in_features=2, out_features=2, bias=True)
      (1): Linear(in_features=2, out_features=2, bias=True)
    ))
    1 -> ('0', Linear(in_features=2, out_features=2, bias=True))"""
        ...
    def named_parameters(self, prefix: Any = ..., recurse: Any = ..., remove_duplicate: Any = ...) -> Any:
        """Return an iterator over module parameters, yielding both the name of the parameter as well as the parameter itself.

Args:
    prefix (str): prefix to prepend to all parameter names.
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.
    remove_duplicate (bool, optional): whether to remove the duplicated
        parameters in the result. Defaults to True.

Yields:
    (str, Parameter): Tuple containing the name and parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for name, param in self.named_parameters():
    >>>     if name in ['bias']:
    >>>         print(param.size())"""
        ...
    def parameters(self, recurse: Any = ...) -> Any:
        """Return an iterator over module parameters.

This is typically passed to an optimizer.

Args:
    recurse (bool): if True, then yields parameters of this module
        and all submodules. Otherwise, yields only parameters that
        are direct members of this module.

Yields:
    Parameter: module parameter

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> for param in model.parameters():
    >>>     print(type(param), param.size())
    <class 'torch.Tensor'> (20L,)
    <class 'torch.Tensor'> (20L, 1L, 5L, 5L)"""
        ...
    def register_backward_hook(self, hook: Any) -> Any:
        """Register a backward hook on the module.

This function is deprecated in favor of :meth:`~torch.nn.Module.register_full_backward_hook` and
the behavior of this function will change in future versions.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_buffer(self, name: Any, tensor: Any, persistent: Any = ...) -> Any:
        """Add a buffer to the module.

This is typically used to register a buffer that should not be
considered a model parameter. For example, BatchNorm's ``running_mean``
is not a parameter, but is part of the module's state. Buffers, by
default, are persistent and will be saved alongside parameters. This
behavior can be changed by setting :attr:`persistent` to ``False``. The
only difference between a persistent buffer and a non-persistent buffer
is that the latter will not be a part of this module's
:attr:`state_dict`.

Buffers can be accessed as attributes using given names.

Args:
    name (str): name of the buffer. The buffer can be accessed
        from this module using the given name
    tensor (Tensor or None): buffer to be registered. If ``None``, then operations
        that run on buffers, such as :attr:`cuda`, are ignored. If ``None``,
        the buffer is **not** included in the module's :attr:`state_dict`.
    persistent (bool): whether the buffer is part of this module's
        :attr:`state_dict`.

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> self.register_buffer('running_mean', torch.zeros(num_features))"""
        ...
    def register_forward_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ..., always_call: Any = ...) -> Any:
        """Register a forward hook on the module.

The hook will be called every time after :func:`forward` has computed an output.

If ``with_kwargs`` is ``False`` or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
output. It can modify the input inplace but it will not have effect on
forward since this is called after :func:`forward` is called. The hook
should have the following signature::

    hook(module, args, output) -> None or modified output

If ``with_kwargs`` is ``True``, the forward hook will be passed the
``kwargs`` given to the forward function and be expected to return the
output possibly modified. The hook should have the following signature::

    hook(module, args, kwargs, output) -> None or modified output

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If ``True``, the provided ``hook`` will be fired
        before all existing ``forward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``forward`` hooks registered with
        :func:`register_module_forward_hook` will fire before all hooks
        registered by this method.
        Default: ``False``
    with_kwargs (bool): If ``True``, the ``hook`` will be passed the
        kwargs given to the forward function.
        Default: ``False``
    always_call (bool): If ``True`` the ``hook`` will be run regardless of
        whether an exception is raised while calling the Module.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_forward_pre_hook(self, hook: Any, prepend: Any = ..., with_kwargs: Any = ...) -> Any:
        """Register a forward pre-hook on the module.

The hook will be called every time before :func:`forward` is invoked.


If ``with_kwargs`` is false or not specified, the input contains only
the positional arguments given to the module. Keyword arguments won't be
passed to the hooks and only to the ``forward``. The hook can modify the
input. User can either return a tuple or a single modified value in the
hook. We will wrap the value into a tuple if a single value is returned
(unless that value is already a tuple). The hook should have the
following signature::

    hook(module, args) -> None or modified input

If ``with_kwargs`` is true, the forward pre-hook will be passed the
kwargs given to the forward function. And if the hook modifies the
input, both the args and kwargs should be returned. The hook should have
the following signature::

    hook(module, args, kwargs) -> None or a tuple of modified input and kwargs

Args:
    hook (Callable): The user defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``forward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``forward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``forward_pre`` hooks registered with
        :func:`register_module_forward_pre_hook` will fire before all
        hooks registered by this method.
        Default: ``False``
    with_kwargs (bool): If true, the ``hook`` will be passed the kwargs
        given to the forward function.
        Default: ``False``

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward hook on the module.

The hook will be called every time the gradients with respect to a module are computed, and its firing rules are as follows:

    1. Ordinarily, the hook fires when the gradients are computed with respect to the module inputs.
    2. If none of the module inputs require gradients, the hook will fire when the gradients are computed
       with respect to module outputs.
    3. If none of the module outputs require gradients, then the hooks will not fire.

The hook should have the following signature::

    hook(module, grad_input, grad_output) -> tuple(Tensor) or None

The :attr:`grad_input` and :attr:`grad_output` are tuples that contain the gradients
with respect to the inputs and outputs respectively. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the input that will be used in place of :attr:`grad_input` in
subsequent computations. :attr:`grad_input` will only correspond to the inputs given
as positional arguments and all kwarg arguments are ignored. Entries
in :attr:`grad_input` and :attr:`grad_output` will be ``None`` for all non-Tensor
arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs or outputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward`` hooks on
        this :class:`torch.nn.Module`. Note that global
        ``backward`` hooks registered with
        :func:`register_module_full_backward_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_full_backward_pre_hook(self, hook: Any, prepend: Any = ...) -> Any:
        """Register a backward pre-hook on the module.

The hook will be called every time the gradients for the module are computed.
The hook should have the following signature::

    hook(module, grad_output) -> tuple[Tensor, ...], Tensor or None

The :attr:`grad_output` is a tuple. The hook should
not modify its arguments, but it can optionally return a new gradient with
respect to the output that will be used in place of :attr:`grad_output` in
subsequent computations. Entries in :attr:`grad_output` will be ``None`` for
all non-Tensor arguments.

For technical reasons, when this hook is applied to a Module, its forward function will
receive a view of each Tensor passed to the Module. Similarly the caller will receive a view
of each Tensor returned by the Module's forward function.

.. warning ::
    Modifying inputs inplace is not allowed when using backward hooks and
    will raise an error.

Args:
    hook (Callable): The user-defined hook to be registered.
    prepend (bool): If true, the provided ``hook`` will be fired before
        all existing ``backward_pre`` hooks on this
        :class:`torch.nn.Module`. Otherwise, the provided
        ``hook`` will be fired after all existing ``backward_pre`` hooks
        on this :class:`torch.nn.Module`. Note that global
        ``backward_pre`` hooks registered with
        :func:`register_module_full_backward_pre_hook` will fire before
        all hooks registered by this method.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook to be run after module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, incompatible_keys) -> None

The ``module`` argument is the current module that this hook is registered
on, and the ``incompatible_keys`` argument is a ``NamedTuple`` consisting
of attributes ``missing_keys`` and ``unexpected_keys``. ``missing_keys``
is a ``list`` of ``str`` containing the missing keys and
``unexpected_keys`` is a ``list`` of ``str`` containing the unexpected keys.

The given incompatible_keys can be modified inplace if needed.

Note that the checks performed when calling :func:`load_state_dict` with
``strict=True`` are affected by modifications the hook makes to
``missing_keys`` or ``unexpected_keys``, as expected. Additions to either
set of keys will result in an error being thrown when ``strict=True``, and
clearing out both missing and unexpected keys will avoid an error.

Returns:
    :class:`torch.utils.hooks.RemovableHandle`:
        a handle that can be used to remove the added hook by calling
        ``handle.remove()``"""
        ...
    def register_load_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook to be run before module's :meth:`~nn.Module.load_state_dict` is called.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata, strict, missing_keys, unexpected_keys, error_msgs) -> None  # noqa: B950

Arguments:
    hook (Callable): Callable hook that will be invoked before
        loading the state dict."""
        ...
    def register_module(self, name: Any, module: Any) -> Any:
        """Alias for :func:`add_module`."""
        ...
    def register_parameter(self, name: Any, param: Any) -> Any:
        """Add a parameter to the module.

The parameter can be accessed as an attribute using given name.

Args:
    name (str): name of the parameter. The parameter can be accessed
        from this module using the given name
    param (Parameter or None): parameter to be added to the module. If
        ``None``, then operations that run on parameters, such as :attr:`cuda`,
        are ignored. If ``None``, the parameter is **not** included in the
        module's :attr:`state_dict`."""
        ...
    def register_state_dict_post_hook(self, hook: Any) -> Any:
        """Register a post-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, state_dict, prefix, local_metadata) -> None

The registered hooks can modify the ``state_dict`` inplace."""
        ...
    def register_state_dict_pre_hook(self, hook: Any) -> Any:
        """Register a pre-hook for the :meth:`~torch.nn.Module.state_dict` method.

It should have the following signature::
    hook(module, prefix, keep_vars) -> None

The registered hooks can be used to perform pre-processing before the ``state_dict``
call is made."""
        ...
    def requires_grad_(self, requires_grad: Any = ...) -> Any:
        """Change if autograd should record operations on parameters in this module.

This method sets the parameters' :attr:`requires_grad` attributes
in-place.

This method is helpful for freezing part of the module for finetuning
or training parts of a model individually (e.g., GAN training).

See :ref:`locally-disable-grad-doc` for a comparison between
`.requires_grad_()` and several similar mechanisms that may be confused with it.

Args:
    requires_grad (bool): whether autograd should record operations on
                          parameters in this module. Default: ``True``.

Returns:
    Module: self"""
        ...
    def set_extra_state(self, state: Any) -> Any:
        """Set extra state contained in the loaded `state_dict`.

This function is called from :func:`load_state_dict` to handle any extra state
found within the `state_dict`. Implement this function and a corresponding
:func:`get_extra_state` for your module if you need to store extra state within its
`state_dict`.

Args:
    state (dict): Extra state from the `state_dict`"""
        ...
    def set_submodule(self, target: Any, module: Any, strict: Any = ...) -> Any:
        """Set the submodule given by ``target`` if it exists, otherwise throw an error.

.. note::
    If ``strict`` is set to ``False`` (default), the method will replace an existing submodule
    or create a new submodule if the parent module exists. If ``strict`` is set to ``True``,
    the method will only attempt to replace an existing submodule and throw an error if
    the submodule does not exist.

For example, let's say you have an ``nn.Module`` ``A`` that
looks like this:

.. code-block:: text

    A(
        (net_b): Module(
            (net_c): Module(
                (conv): Conv2d(3, 3, 3)
            )
            (linear): Linear(3, 3)
        )
    )

(The diagram shows an ``nn.Module`` ``A``. ``A`` has a nested
submodule ``net_b``, which itself has two submodules ``net_c``
and ``linear``. ``net_c`` then has a submodule ``conv``.)

To override the ``Conv2d`` with a new submodule ``Linear``, you
could call ``set_submodule("net_b.net_c.conv", nn.Linear(1, 1))``
where ``strict`` could be ``True`` or ``False``

To add a new submodule ``Conv2d`` to the existing ``net_b`` module,
you would call ``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1))``.

In the above if you set ``strict=True`` and call
``set_submodule("net_b.conv", nn.Conv2d(1, 1, 1), strict=True)``, an AttributeError
will be raised because ``net_b`` does not have a submodule named ``conv``.

Args:
    target: The fully-qualified string name of the submodule
        to look for. (See above example for how to specify a
        fully-qualified string.)
    module: The module to set the submodule to.
    strict: If ``False``, the method will replace an existing submodule
        or create a new submodule if the parent module exists. If ``True``,
        the method will only attempt to replace an existing submodule and throw an error
        if the submodule doesn't already exist.

Raises:
    ValueError: If the ``target`` string is empty or if ``module`` is not an instance of ``nn.Module``.
    AttributeError: If at any point along the path resulting from
        the ``target`` string the (sub)path resolves to a non-existent
        attribute name or an object that is not an instance of ``nn.Module``."""
        ...
    def share_memory(self) -> Any:
        """See :meth:`torch.Tensor.share_memory_`."""
        ...
    def state_dict(self, *args: Any, destination: Any = ..., prefix: Any = ..., keep_vars: Any = ...) -> Any:
        """Return a dictionary containing references to the whole state of the module.

Both parameters and persistent buffers (e.g. running averages) are
included. Keys are corresponding parameter and buffer names.
Parameters and buffers set to ``None`` are not included.

.. note::
    The returned object is a shallow copy. It contains references
    to the module's parameters and buffers.

.. warning::
    Currently ``state_dict()`` also accepts positional arguments for
    ``destination``, ``prefix`` and ``keep_vars`` in order. However,
    this is being deprecated and keyword arguments will be enforced in
    future releases.

.. warning::
    Please avoid the use of argument ``destination`` as it is not
    designed for end-users.

Args:
    destination (dict, optional): If provided, the state of module will
        be updated into the dict and the same object is returned.
        Otherwise, an ``OrderedDict`` will be created and returned.
        Default: ``None``.
    prefix (str, optional): a prefix added to parameter and buffer
        names to compose the keys in state_dict. Default: ``''``.
    keep_vars (bool, optional): by default the :class:`~torch.Tensor` s
        returned in the state dict are detached from autograd. If it's
        set to ``True``, detaching will not be performed.
        Default: ``False``.

Returns:
    dict:
        a dictionary containing a whole state of the module

Example::

    >>> # xdoctest: +SKIP("undefined vars")
    >>> module.state_dict().keys()
    ['bias', 'weight']"""
        ...
    def to(self, *args: Any, **kwargs: Any) -> Any:
        """Move and/or cast the parameters and buffers.

This can be called as

.. function:: to(device=None, dtype=None, non_blocking=False)
   :noindex:

.. function:: to(dtype, non_blocking=False)
   :noindex:

.. function:: to(tensor, non_blocking=False)
   :noindex:

.. function:: to(memory_format=torch.channels_last)
   :noindex:

Its signature is similar to :meth:`torch.Tensor.to`, but only accepts
floating point or complex :attr:`dtype`\\ s. In addition, this method will
only cast the floating point or complex parameters and buffers to :attr:`dtype`
(if given). The integral parameters and buffers will be moved
:attr:`device`, if that is given, but with dtypes unchanged. When
:attr:`non_blocking` is set, it tries to convert/move asynchronously
with respect to the host if possible, e.g., moving CPU Tensors with
pinned memory to CUDA devices.

See below for examples.

.. note::
    This method modifies the module in-place.

Args:
    device (:class:`torch.device`): the desired device of the parameters
        and buffers in this module
    dtype (:class:`torch.dtype`): the desired floating point or complex dtype of
        the parameters and buffers in this module
    tensor (torch.Tensor): Tensor whose dtype and device are the desired
        dtype and device for all parameters and buffers in this module
    memory_format (:class:`torch.memory_format`): the desired memory
        format for 4D parameters and buffers in this module (keyword
        only argument)

Returns:
    Module: self

Examples::

    >>> # xdoctest: +IGNORE_WANT("non-deterministic")
    >>> linear = nn.Linear(2, 2)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]])
    >>> linear.to(torch.double)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1913, -0.3420],
            [-0.5113, -0.2325]], dtype=torch.float64)
    >>> # xdoctest: +REQUIRES(env:TORCH_DOCTEST_CUDA1)
    >>> gpu1 = torch.device("cuda:1")
    >>> linear.to(gpu1, dtype=torch.half, non_blocking=True)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16, device='cuda:1')
    >>> cpu = torch.device("cpu")
    >>> linear.to(cpu)
    Linear(in_features=2, out_features=2, bias=True)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.1914, -0.3420],
            [-0.5112, -0.2324]], dtype=torch.float16)

    >>> linear = nn.Linear(2, 2, bias=None).to(torch.cdouble)
    >>> linear.weight
    Parameter containing:
    tensor([[ 0.3741+0.j,  0.2382+0.j],
            [ 0.5593+0.j, -0.4443+0.j]], dtype=torch.complex128)
    >>> linear(torch.ones(3, 2, dtype=torch.cdouble))
    tensor([[0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j],
            [0.6122+0.j, 0.1150+0.j]], dtype=torch.complex128)"""
        ...
    def to_empty(self, device: Any, recurse: Any = ...) -> Any:
        """Move the parameters and buffers to the specified device without copying storage.

Args:
    device (:class:`torch.device`): The desired device of the parameters
        and buffers in this module.
    recurse (bool): Whether parameters and buffers of submodules should
        be recursively moved to the specified device.

Returns:
    Module: self"""
        ...
    def train(self, mode: Any = ...) -> Any:
        """Set the module in training mode.

This has an effect only on certain modules. See the documentation of
particular modules for details of their behaviors in training/evaluation
mode, i.e., whether they are affected, e.g. :class:`Dropout`, :class:`BatchNorm`,
etc.

Args:
    mode (bool): whether to set training mode (``True``) or evaluation
                 mode (``False``). Default: ``True``.

Returns:
    Module: self"""
        ...
    def type(self, dst_type: Any) -> Any:
        """Casts all parameters and buffers to :attr:`dst_type`.

.. note::
    This method modifies the module in-place.

Args:
    dst_type (type or string): the desired type

Returns:
    Module: self"""
        ...
    def xpu(self, device: Any = ...) -> Any:
        """Move all model parameters and buffers to the XPU.

This also makes associated parameters and buffers different objects. So
it should be called before constructing optimizer if the module will
live on XPU while being optimized.

.. note::
    This method modifies the module in-place.

Arguments:
    device (int, optional): if specified, all parameters will be
        copied to that device

Returns:
    Module: self"""
        ...
    def zero_grad(self, set_to_none: Any = ...) -> Any:
        """Reset gradients of all model parameters.

See similar function under :class:`torch.optim.Optimizer` for more context.

Args:
    set_to_none (bool): instead of setting to zero, set the grads to None.
        See :meth:`torch.optim.Optimizer.zero_grad` for details."""
        ...

def preprocess_kaggle_house(train_data: Any, test_data: Any, label: Any = ...) -> Any:
    """Kaggle 房价特征预处理：标准化数值列、one-hot 类别、标签取 log。

Args:
    train_data: 训练 DataFrame（含 ``Id`` 与标签列）。
    test_data: 测试 DataFrame（含 ``Id``）。
    label: 标签列名，默认 ``'SalePrice'``。

Returns:
    tuple[Tensor, Tensor, Tensor]:
        ``Xs_train, ys_train(log1p 价格), Xs_test``，均为 float32。"""
    ...

def train_kaggle_mlp(Xs: Any, ys: Any, num_epochs: Any, batch_size: Any, lr: Any, dropouts: Any, hidden_layers: Any, weight_decay: Any, device: Any, is_display: Any = ...) -> Any:
    """训练 Kaggle 房价 MLP（Adam + MSE，对 log 价格）。

Args:
    Xs: 特征 ``(N, D)``。
    ys: 标签 ``(N,)``（通常已 log）。
    num_epochs: 轮数。
    batch_size: 批量。
    lr: Adam 学习率。
    dropouts: 与 ``hidden_layers`` 等长的 dropout 概率列表。
    hidden_layers: 各隐藏层宽度列表。
    weight_decay: Adam 权重衰减。
    device: 设备。
    is_display: 是否用 ``AnimatorSimple`` 画训练损失。

Returns:
    tuple: ``(net, final_train_loss)``。"""
    ...

def f_fold_data(k: Any, Xs: Any, ys: Any) -> Any:
    """生成 K 折中的各「训练折」数据（每折去掉一块验证段）。

Args:
    k: 折数。
    Xs: 特征 ``(N, ...)``。
    ys: 标签 ``(N, ...)``。

Returns:
    list[tuple[Tensor, Tensor]]: 长度 ``k``；第 i 项是去掉第 i 块后的
    ``(Xs_train, ys_train)``。

Notes:
    每块大小为 ``N // k``，尾部不足一块的样本不会进入任何折。"""
    ...

def k_fold(trainer: Any, Xs: Any, ys: Any, num_epochs: Any, batch_size: Any, K: Any, lr: Any, dropouts: Any, hidden_layers: Any, weight_decay: Any, device: Any, is_display: Any = ...) -> Any:
    """对 ``trainer``（通常 ``train_kaggle_mlp``）做 K 折训练。

Args:
    trainer: 可调用，签名需兼容
        ``trainer(Xs, ys, num_epochs, batch_size, lr, dropouts,
        hidden_layers, weight_decay, device, is_display) -> (model, loss)``。
    Xs, ys: 全量训练特征/标签。
    num_epochs, batch_size, lr, dropouts, hidden_layers, weight_decay:
        传给 ``trainer`` 的超参。
    K: 折数。
    device: 设备。
    is_display: 仅第 0 折显示曲线。

Returns:
    tuple: ``(models, avg_loss)``，``models`` 为各折模型列表。"""
    ...

def tensor2str(t: Any) -> Any:
    """把张量压平后格式化为短字符串（便于打印）。

Args:
    t: ``torch.Tensor`` 或其它；非 Tensor 原样返回。

Returns:
    str | Any: 形如 ``"0.1234, 0.5678"`` 的字符串。"""
    ...

accumulator: Any
animator: Any
get_data: Any
train_model: Any
