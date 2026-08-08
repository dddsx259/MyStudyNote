"""d2l practice 可复用工具集。

汇总自 practice 下各章 notebook 的最新可用版本。
章节专属网络架构（LeNet / AlexNet / ResNet / Seq2SeqEncoder 等）留在对应 notebook。

在 IDE 中将光标放在函数名上即可看到 Args / Returns / Notes 约定。
导入示例::

    import utils
    device = utils.try_gpu()
    train_iter, test_iter = utils.load_data_fashion_mnist(256)
"""

from __future__ import annotations

import collections
import hashlib
import math
import os
import random
import re
import time
import warnings
from urllib import request

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torchvision
from IPython import display
from torch import nn
from torch.nn import functional as F
from torch.utils import data
from torchvision import transforms

warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# 设备
# ---------------------------------------------------------------------------

def try_gpu(i: int = 0) -> torch.device:
    """选择可用计算设备。

    Args:
        i: GPU 编号，从 0 开始。默认 0。

    Returns:
        torch.device: 存在第 i 块 GPU 时返回 ``cuda:i``，否则 ``cpu``。
    """
    if torch.cuda.device_count() >= i + 1:
        return torch.device(f'cuda:{i}')
    return torch.device('cpu')


# ---------------------------------------------------------------------------
# 累加器 / 指标
# ---------------------------------------------------------------------------

class Accumulator:
    """在固定数量的标量上累加（loss / 正确数 / token 数等）。

    Args:
        n: 累加槽位数。

    Notes:
        典型用法::

            metric = Accumulator(2)
            metric.add(loss_sum, n_samples)
            avg = metric[0] / metric[1]
    """

    def __init__(self, n: int):
        """创建长度为 ``n`` 的累加器，初值全 0。

        Args:
            n: 槽位数。
        """
        self.data = [0.0] * n

    def add(self, *args):
        """将本批数值加到对应槽位。

        Args:
            *args: 长度须等于 ``n`` 的标量序列。
        """
        self.data = [a + float(b) for a, b in zip(self.data, args)]

    def reset(self):
        """将所有累加值清零。"""
        self.data = [0.0] * len(self.data)

    def __getitem__(self, idx):
        """按索引读取累加值。

        Args:
            idx: 槽位下标，``0 .. n-1``。

        Returns:
            float: 该槽当前累加值。
        """
        return self.data[idx]


class Timer:
    """多次计时工具（接口与 d2l.Timer 一致）。

    Notes:
        构造时自动 ``start()``。``stop()`` 返回秒数并记入 ``times``。
    """

    def __init__(self):
        """初始化并立即开始计时。"""
        self.times = []
        self.start()

    def start(self):
        """启动或重新启动计时，记录当前时间戳到 ``self.tik``。"""
        self.tik = time.time()

    def stop(self):
        """停止计时，将本次耗时（秒）追加到 ``times``。

        Returns:
            float: 自上次 ``start()`` 起的秒数。
        """
        self.times.append(time.time() - self.tik)
        return self.times[-1]

    def avg(self):
        """已记录各次耗时的平均值（秒）。

        Returns:
            float: ``sum(times) / len(times)``。
        """
        return sum(self.times) / len(self.times)

    def sum(self):
        """已记录各次耗时之和（秒）。"""
        return sum(self.times)

    def cumsum(self):
        """累计耗时前缀和。

        Returns:
            list[float]: 与 ``times`` 等长的前缀和列表。
        """
        return np.array(self.times).cumsum().tolist()


def accuracy(y_hat, y):
    """统计预测正确的样本个数（不是准确率比例）。

    Args:
        y_hat: 预测。``(N,)`` 为类别；``(N, C)`` 时对最后一维 ``argmax``。
        y: 真实标签，形状 ``(N,)``。

    Returns:
        float: 正确样本数；准确率 = 本返回值 / ``y.numel()``。
    """
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())


def evaluate_accuracy(net, data_iter, device=None):
    """在整个 ``data_iter`` 上评估分类准确率。

    Args:
        net: 模型；若为 ``nn.Module`` 会设为 ``eval()``。
        data_iter: 迭代 ``(X, y)``。
        device: 若给定则把 batch 搬到该设备；``None`` 不搬迁。

    Returns:
        float: 正确数 / 样本数，约在 ``[0, 1]``。
    """
    if isinstance(net, nn.Module):
        net.eval()
    metric = Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            if device is not None:
                X, y = X.to(device), y.to(device)
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]


def evaluate_loss(net, data_iter, loss, device=None):
    """在整个 ``data_iter`` 上评估按样本平均的损失。

    Args:
        net: 模型；若为 ``nn.Module`` 会设为 ``eval()``。
        data_iter: 迭代 ``(X, y)``。
        loss: 可调用对象，约定 ``loss(net(X), y)``，再对其 ``.sum()``。
        device: 可选设备。

    Returns:
        float: ``总损失 / 样本数``。
    """
    if isinstance(net, nn.Module):
        net.eval()
    metric = Accumulator(2)
    with torch.no_grad():
        for X, y in data_iter:
            if device is not None:
                X, y = X.to(device), y.to(device)
            metric.add(float(loss(net(X), y).sum()), y.numel())
    return metric[0] / metric[1]


# ---------------------------------------------------------------------------
# 动画：双子图 / 单图 d2l 风格 / RNN 困惑度
# ---------------------------------------------------------------------------

class Animator:
    """Jupyter 双子图训练曲线（上 loss、下 acc），供 CNN 等分类任务。

    Notes:
        - 若提供 ``acc_legend`` 则画双子图，否则只画 loss 单图。
        - 追加点：``add(epoch, loss=(tr, te), acc=(tr, te))``。
        - 与 d2l 单图 ``Animator`` 不同；单图请用 ``AnimatorSimple``。
    """

    def __init__(self, xlabel='epoch', xlim=None,
                 loss_legend=None, acc_legend=None, acc_ylim=(0, 1),
                 fmts=('-', 'm--', 'g-.', 'r:', 'c-', 'y--', 'k-.', 'b:'),
                 figsize=(5, 6)):
        """创建 Animator。

        Args:
            xlabel: x 轴标签。
            xlim: x 轴范围，如 ``[1, num_epochs]``；``None`` 自适应。
            loss_legend: loss 曲线图例列表，如 ``['train loss', 'test loss']``。
            acc_legend: acc 曲线图例；非空则启用下方准确率子图。
            acc_ylim: 准确率子图 y 范围，默认 ``(0, 1)``。
            fmts: 各条曲线的 matplotlib 线型循环使用。
            figsize: 整图大小 ``(宽, 高)``；无 acc 子图时高度约减半。
        """
        self.xlabel = xlabel
        self.xlim = xlim
        self.loss_legend = list(loss_legend) if loss_legend else []
        self.acc_legend = list(acc_legend) if acc_legend else []
        self.acc_ylim = acc_ylim
        self.fmts = list(fmts)
        self.loss_X, self.loss_Y = None, None
        self.acc_X, self.acc_Y = None, None

        if self.acc_legend:
            self.fig, (self.ax_loss, self.ax_acc) = plt.subplots(
                2, 1, figsize=figsize, sharex=True)
        else:
            self.fig, self.ax_loss = plt.subplots(
                1, 1, figsize=(figsize[0], figsize[1] / 2))
            self.ax_acc = None

    @staticmethod
    def _as_lines(values):
        if values is None:
            return []
        if isinstance(values, (list, tuple)):
            return list(values)
        return [values]

    def _ensure_lines(self, storage, n):
        X, Y = storage
        if X is None:
            return [[] for _ in range(n)], [[] for _ in range(n)]
        if n > len(X):
            X.extend([] for _ in range(n - len(X)))
            Y.extend([] for _ in range(n - len(Y)))
        return X, Y

    def _append_points(self, storage, x, values):
        values = self._as_lines(values)
        if not values:
            return storage
        x = self._as_lines(x)
        if len(x) == 1:
            x = x * len(values)
        elif len(x) != len(values):
            raise ValueError(
                f'x 与 values 长度不一致: len(x)={len(x)}, len(values)={len(values)}'
            )
        X, Y = self._ensure_lines(storage, len(values))
        for i, (xi, yi) in enumerate(zip(x, values)):
            if xi is not None and yi is not None:
                X[i].append(xi)
                Y[i].append(yi)
        return X, Y

    def _plot_panel(self, ax, X, Y, legend, ylim=None, show_xlabel=False):
        ax.cla()
        if X is None:
            return
        for i, (xs, ys) in enumerate(zip(X, Y)):
            fmt = self.fmts[i % len(self.fmts)]
            label = legend[i] if i < len(legend) else None
            ax.plot(xs, ys, fmt, label=label)
        if self.xlim:
            ax.set_xlim(self.xlim)
        if ylim:
            ax.set_ylim(ylim)
        if show_xlabel and self.xlabel:
            ax.set_xlabel(self.xlabel)
        if legend:
            ax.legend(legend)
        ax.grid(True)

    def add(self, x, loss=None, acc=None):
        """追加一个 epoch 的点并刷新显示。

        Args:
            x: 横轴值（通常为 epoch）。可为标量，或与曲线条数等长的序列。
            loss: loss 曲线的 y；标量或 ``(train, test, ...)``。
            acc: acc 曲线的 y；仅当构造时提供了 ``acc_legend`` 时有效。
        """
        self.loss_X, self.loss_Y = self._append_points(
            (self.loss_X, self.loss_Y), x, loss)
        if self.ax_acc is not None:
            self.acc_X, self.acc_Y = self._append_points(
                (self.acc_X, self.acc_Y), x, acc)

        self._plot_panel(self.ax_loss, self.loss_X, self.loss_Y,
                         self.loss_legend, show_xlabel=self.ax_acc is None)
        if self.ax_acc is not None:
            self._plot_panel(self.ax_acc, self.acc_X, self.acc_Y,
                             self.acc_legend, ylim=self.acc_ylim, show_xlabel=True)

        self.fig.tight_layout()
        display.clear_output(wait=True)
        display.display(self.fig)

    def close(self):
        """关闭图窗，释放资源。"""
        plt.close(self.fig)


class AnimatorSimple:
    """单图 d2l 风格 Animator，API 为 ``add(x, y)``。

    Notes:
        供 ``train_net`` / Kaggle / seq2seq 等使用。多条曲线时
        ``y`` 传元组/列表，``legend`` 与之对应。
    """

    def __init__(self, xlabel=None, ylabel=None, legend=None, xlim=None,
                 ylim=None, xscale='linear', yscale='linear',
                 fmts=('-', 'm--', 'g-.', 'r:'), nrows=1, ncols=1,
                 figsize=(3.5, 2.5)):
        """创建单图 Animator。

        Args:
            xlabel, ylabel: 轴标签。
            legend: 图例列表，长度应匹配曲线条数。
            xlim, ylim: 轴范围。
            xscale, yscale: ``'linear'`` / ``'log'`` 等。
            fmts: 线型循环。
            nrows, ncols: 子图网格（通常均为 1）。
            figsize: 图大小。
        """
        if legend is None:
            legend = []
        self.fig, self.axes = plt.subplots(nrows, ncols, figsize=figsize)
        if nrows * ncols == 1:
            self.axes = [self.axes]

        def config_axes():
            ax = self.axes[0]
            if xlabel:
                ax.set_xlabel(xlabel)
            if ylabel:
                ax.set_ylabel(ylabel)
            if xscale:
                ax.set_xscale(xscale)
            if yscale:
                ax.set_yscale(yscale)
            if xlim:
                ax.set_xlim(xlim)
            if ylim:
                ax.set_ylim(ylim)
            if legend:
                ax.legend(legend)
            ax.grid(True)

        self.config_axes = config_axes
        self.X, self.Y, self.fmts = None, None, fmts

    def add(self, x, y):
        """追加数据点并重绘。

        Args:
            x: 横轴。标量会广播到与 ``y`` 相同条数。
            y: 纵轴。标量表示 1 条曲线；序列表示多条，如
                ``(train_loss, test_loss)``。
        """
        if not hasattr(y, '__len__'):
            y = [y]
        n = len(y)
        if not hasattr(x, '__len__'):
            x = [x] * n
        if not self.X:
            self.X = [[] for _ in range(n)]
        if not self.Y:
            self.Y = [[] for _ in range(n)]
        for i, (a, b) in enumerate(zip(x, y)):
            if a is not None and b is not None:
                self.X[i].append(a)
                self.Y[i].append(b)
        self.axes[0].clear()
        for xs, ys, fmt in zip(self.X, self.Y, self.fmts):
            self.axes[0].plot(xs, ys, fmt)
        self.config_axes()
        display.clear_output(wait=True)
        display.display(self.fig)

    def close(self):
        """关闭图窗。"""
        plt.close(self.fig)


class AnimatorNoTest:
    """单图实时刷新：适合 RNN 困惑度等只有训练曲线的场景。

    Notes:
        调用 ``add(x, y)``；``y`` 可为标量或序列。
    """

    def __init__(self, xlabel='epoch', ylabel=None, xlim=None, ylim=None,
                 legend=None,
                 fmts=('-', 'm--', 'g-.', 'r:', 'c-', 'y--', 'k-.', 'b:'),
                 figsize=(5, 3)):
        """创建 AnimatorNoTest。

        Args:
            xlabel, ylabel: 轴标签。
            xlim, ylim: 轴范围。
            legend: 图例列表。
            fmts: 线型。
            figsize: 图大小。
        """
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim
        self.legend = list(legend) if legend else []
        self.fmts = list(fmts)
        self.X, self.Y = None, None
        self.fig, self.ax = plt.subplots(figsize=figsize)

    @staticmethod
    def _as_lines(values):
        if values is None:
            return []
        if isinstance(values, (list, tuple)):
            return list(values)
        return [values]

    def _ensure_lines(self, n):
        if self.X is None:
            self.X = [[] for _ in range(n)]
            self.Y = [[] for _ in range(n)]
        elif n > len(self.X):
            self.X.extend([] for _ in range(n - len(self.X)))
            self.Y.extend([] for _ in range(n - len(self.Y)))

    def add(self, x, y):
        """追加点并刷新（无测试集的单曲线/多曲线）。

        Args:
            x: 横轴值或序列。
            y: 纵轴值或序列；长度须与 ``x`` 广播后一致。
        """
        y = self._as_lines(y)
        x = self._as_lines(x)
        if len(x) == 1:
            x = x * len(y)
        elif len(x) != len(y):
            raise ValueError(
                f'x 与 y 长度不一致: len(x)={len(x)}, len(y)={len(y)}'
            )
        self._ensure_lines(len(y))
        for i, (xi, yi) in enumerate(zip(x, y)):
            if xi is not None and yi is not None:
                self.X[i].append(xi)
                self.Y[i].append(yi)

        self.ax.cla()
        for i, (xs, ys) in enumerate(zip(self.X, self.Y)):
            fmt = self.fmts[i % len(self.fmts)]
            label = self.legend[i] if i < len(self.legend) else None
            self.ax.plot(xs, ys, fmt, label=label)
        if self.xlim:
            self.ax.set_xlim(self.xlim)
        if self.ylim:
            self.ax.set_ylim(self.ylim)
        if self.xlabel:
            self.ax.set_xlabel(self.xlabel)
        if self.ylabel:
            self.ax.set_ylabel(self.ylabel)
        if self.legend:
            self.ax.legend(self.legend)
        self.ax.grid(True)
        self.fig.tight_layout()
        display.clear_output(wait=True)
        display.display(self.fig)

    def close(self):
        """关闭图窗。"""
        plt.close(self.fig)


# ---------------------------------------------------------------------------
# 优化器 / 正则
# ---------------------------------------------------------------------------

def sgd(params, lr, batch_size):
    """手写小批量 SGD：``param -= lr * grad / batch_size``。

    Args:
        params: 可迭代的参数张量（需已有 ``.grad``）。
        lr: 学习率。
        batch_size: 用于把 ``loss.sum()`` 反传的梯度平均化。

    Notes:
        在 ``torch.no_grad()`` 中更新，并 ``grad.zero_()``。
        若损失已 ``mean()``，通常应令 ``batch_size=1``。
    """
    with torch.no_grad():
        for param in params:
            if param.grad is not None:
                param.data -= lr * param.grad / batch_size
                param.grad.zero_()


def l2_penalty(w):
    """计算 L2 惩罚 ``||w||^2 / 2``。

    Args:
        w: 权重张量。

    Returns:
        Tensor: 标量惩罚项，可加到损失上：``loss + lambd * l2_penalty(w)``。
    """
    return torch.sum(w.pow(2)) / 2


def sgd_with_l2(params, lr, batch_size, lambd):
    """手写带 L2 的 SGD：``param -= lr * (grad/batch_size + lambd * param)``。

    Args:
        params: 参数迭代器。
        lr: 学习率。
        batch_size: 与 ``loss.sum()`` 反传配套的批量大小。
        lambd: L2 系数（权重衰减）。
    """
    params = list(params)
    with torch.no_grad():
        for param in params:
            param -= lr * (param.grad / batch_size + lambd * param)
            param.grad.zero_()


def dropout(X, drop_prob):
    """手写 Dropout（仅训练阶段调用；推理勿用）。

    Args:
        X: 输入张量，任意形状。
        drop_prob: 丢弃概率，``0 <= drop_prob <= 1``。
            ``0`` 恒等；``1`` 返回全 0。

    Returns:
        Tensor: 与 ``X`` 同形；保留元素按 ``1/(1-drop_prob)`` 缩放。
    """
    assert 0 <= drop_prob <= 1
    if drop_prob == 1:
        return torch.zeros_like(X)
    mask = (torch.rand(X.shape, device=X.device) > drop_prob).float()
    return mask * X / (1.0 - drop_prob)


def grad_clipping(net, theta):
    """按全局 L2 范数裁剪梯度：若 ``||g|| > theta`` 则缩放至 ``theta``。

    Args:
        net: ``nn.Module``，或带 ``.params`` 列表的从零实现模型。
        theta: 梯度范数上限（正数），如 ``1``。

    Notes:
        应在 ``loss.backward()`` 之后、``optimizer.step()`` 之前调用。
    """
    if isinstance(net, nn.Module):
        params = [p for p in net.parameters() if p.requires_grad]
    else:
        params = net.params
    norm = torch.sqrt(sum(torch.sum((p.grad ** 2)) for p in params))
    if norm > theta:
        for param in params:
            param.grad[:] *= theta / norm


# ---------------------------------------------------------------------------
# 数据加载
# ---------------------------------------------------------------------------

def load_data_fashion_mnist(batch_size, resize=None, root='./data'):
    """下载 Fashion-MNIST，返回训练/测试 DataLoader。

    Args:
        batch_size: 批量大小。
        resize: 若给定（如 ``224``），先 ``Resize`` 再 ``ToTensor``。
        root: 数据根目录。

    Returns:
        tuple: ``(train_iter, test_iter)``；batch 为 ``(X, y)``，
        ``X`` 形状约 ``(B, 1, H, W)``，``y`` 为类别下标。
    """
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    train_set = torchvision.datasets.FashionMNIST(
        root, train=True, transform=trans, download=True)
    test_set = torchvision.datasets.FashionMNIST(
        root, train=False, transform=trans, download=True)
    train_iter = data.DataLoader(
        train_set, batch_size, shuffle=True, num_workers=0)
    test_iter = data.DataLoader(
        test_set, batch_size, shuffle=False, num_workers=0)
    return train_iter, test_iter


def get_data(dataset='fashion_mnist', batch_size=256, train_shuffle=True,
             test_shuffle=False, n_workers=0, root='../data/'):
    """按数据集名称返回 ``(train_iter, test_iter)``。

    Args:
        dataset: 目前仅 ``'fashion_mnist'``。
        batch_size: 批量大小。
        train_shuffle: 训练集是否打乱。
        test_shuffle: 测试集是否打乱。
        n_workers: DataLoader 进程数。
        root: 数据根目录。

    Returns:
        tuple[DataLoader, DataLoader]: 训练与测试迭代器。

    Raises:
        NotImplementedError: 未知 ``dataset``。
    """
    if dataset == 'fashion_mnist':
        trans = transforms.ToTensor()
        train_set = torchvision.datasets.FashionMNIST(
            root=root, train=True, download=True, transform=trans)
        test_set = torchvision.datasets.FashionMNIST(
            root=root, train=False, download=True, transform=trans)
        train_iter = data.DataLoader(
            train_set, batch_size, shuffle=train_shuffle, num_workers=n_workers)
        test_iter = data.DataLoader(
            test_set, batch_size, shuffle=test_shuffle, num_workers=n_workers)
        return train_iter, test_iter
    raise NotImplementedError(f'Dataset not implemented: {dataset}')


def generate_data_of_linear_regression_with_noise(
        n_inputs, n_train, n_test, batch_size=256, W=None, b=None, noise=None):
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
        tuple: ``(W, b, train_iter, test_iter)``。
    """
    if W is None:
        W = torch.normal(0, 1, (n_inputs, 1))
    if b is None:
        b = torch.zeros(1)
    if noise is None:
        noise = torch.normal(0, 0.01, (n_train + n_test, 1))
    Xs = torch.normal(0, 1, (n_train + n_test, n_inputs))
    Ys = Xs @ W + b + noise
    train_iter = data.DataLoader(
        data.TensorDataset(Xs[:n_train], Ys[:n_train]),
        batch_size=batch_size, shuffle=True)
    test_iter = data.DataLoader(
        data.TensorDataset(Xs[n_train:], Ys[n_train:]),
        batch_size=batch_size, shuffle=False)
    return W, b, train_iter, test_iter


DATA_URL = 'http://d2l-data.s3-accelerate.amazonaws.com/'
DATA_HUB = {
    'time_machine': (
        DATA_URL + 'timemachine.txt',
        '090b5e7e70c295757f55df93cb0a180b9691891a',
    ),
}


def download(name, cache_dir='./data'):
    """按 ``DATA_HUB`` 下载并缓存文件；已存在且 SHA1 匹配则跳过。

    Args:
        name: ``DATA_HUB`` 中的键，如 ``'time_machine'``。
        cache_dir: 本地缓存目录。

    Returns:
        str: 本地文件路径。
    """
    assert name in DATA_HUB, f'{name} 不存在于 {DATA_HUB}'
    url, sha1_hash = DATA_HUB[name]
    os.makedirs(cache_dir, exist_ok=True)
    fname = os.path.join(cache_dir, url.split('/')[-1])
    if os.path.exists(fname):
        sha1 = hashlib.sha1()
        with open(fname, 'rb') as f:
            while True:
                chunk = f.read(1048576)
                if not chunk:
                    break
                sha1.update(chunk)
        if sha1.hexdigest() == sha1_hash:
            return fname
    print(f'正在从 {url} 下载 {fname}...')
    request.urlretrieve(url, fname)
    return fname


def read_time_machine():
    """下载并读取《时间机器》全书为文本行列表。

    Returns:
        list[str]: 每行一个字符串（含换行符，与 ``readlines()`` 一致）。
    """
    with open(download('time_machine'), 'r') as f:
        lines = f.readlines()
    return lines


# ---------------------------------------------------------------------------
# 文本：分词 / 词表 / 序列迭代器
# ---------------------------------------------------------------------------

def tokenize(lines, token='word', clean_en=False):
    """将文本行列表拆成词元列表的列表。

    Args:
        lines: ``list[str]``，每行一段文本。
        token: ``'word'`` 按空白分词；``'char'`` 按字符。
        clean_en: 为 True 时先把非英文字母替换为空格并转小写。

    Returns:
        list[list[str]]: 与 ``lines`` 对齐的词元序列。
    """
    if clean_en:
        lines = [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]
    if token == 'word':
        return [line.split() for line in lines]
    if token == 'char':
        return [list(line) for line in lines]
    print(f"错误: 未知词元类型: '{token}'")
    return []


def count_corpus(tokens):
    """统计词元出现频率。

    Args:
        tokens: 一维 ``list[str]``，或二维 ``list[list[str]]``（会展平）。

    Returns:
        collections.Counter: ``{token: freq}``。
    """
    if isinstance(tokens, list) and tokens and isinstance(tokens[0], list):
        tokens = [tk for line in tokens for tk in line]
    return collections.Counter(tokens)


class Vocab:
    """文本词表。

    Notes:
        - ``<unk>`` 固定索引 0。
        - 构造顺序：``['<unk>'] + reserved_tokens + 高频词``。
        - ``vocab[token]`` / ``vocab[list]`` 查索引；未知 -> 0。
        - ``vocab.to_tokens(ids)`` 索引还原为词。
    """

    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        """根据语料构建词表。

        Args:
            tokens: 词元或词元序列的序列；``None`` 则仅含保留词。
            min_freq: 低于该频次的词不进入词表。
            reserved_tokens: 保留词列表，如 ``['<pad>', '<bos>', '<eos>']``，
                紧接在 ``<unk>`` 之后、语料词之前。
        """
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []
        counter = count_corpus(tokens)
        self._token_freqs = sorted(
            counter.items(), key=lambda x: x[1], reverse=True)
        self.idx_to_token = ['<unk>'] + list(reserved_tokens)
        self.token_to_idx = {
            token: idx for idx, token in enumerate(self.idx_to_token)
        }
        for token, freq in self._token_freqs:
            if freq < min_freq:
                break
            if token not in self.token_to_idx:
                self.idx_to_token.append(token)
                self.token_to_idx[token] = len(self.idx_to_token) - 1

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        """词元 -> 索引；未知词返回 ``unk`` (0)。

        Args:
            tokens: 单个 ``str``，或 ``list/tuple[str]``。

        Returns:
            int | list[int]: 索引或索引列表。
        """
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        """索引 -> 词元。

        Args:
            indices: 单个 ``int``，或 ``list/tuple[int]``。

        Returns:
            str | list[str]: 词元或词元列表。
        """
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

    @property
    def unk(self):
        """未知词索引，恒为 0。"""
        return 0

    @property
    def token_freqs(self):
        """语料词频表 ``list[(token, freq)]``，按频率降序。"""
        return self._token_freqs


class SeqDataLoader:
    """语言模型用序列数据迭代器。

    Notes:
        迭代产出 ``(X, Y)``，形状均为 ``(batch_size, num_steps)``，
        ``Y`` 为 ``X`` 向后错一位的下一个词元。
        ``mode='random'`` 随机采样子序列；``'sequential'`` 顺序划分。
    """

    def __init__(self, batch_size, num_steps, corpus=None, vocab=None,
                 mode='random'):
        """构造迭代器。

        Args:
            batch_size: 批量大小。
            num_steps: 每个样本的时间步长度。
            corpus: 一维词元索引列表（整本语料）。
            vocab: 词表对象（保留引用，本类迭代主要用 ``corpus``）。
            mode: ``'random'`` 或其它（走 sequential）。
        """
        assert corpus is not None and vocab is not None
        self.corpus = corpus
        self.vocab = vocab
        if mode == 'random':
            self.data_iter_fn = self.seq_data_iter_random
        else:
            self.data_iter_fn = self.seq_data_iter_sequential
        self.batch_size = batch_size
        self.num_steps = num_steps

    def __iter__(self):
        return self.data_iter_fn(self.corpus, self.batch_size, self.num_steps)

    def seq_data_iter_random(self, corpus, batch_size, num_steps):
        """随机采样子序列的迭代器。

        Yields:
            tuple[Tensor, Tensor]: ``(X, Y)``，形状 ``(batch_size, num_steps)``。
        """
        corpus = corpus[random.randint(0, num_steps - 1):]
        num_subseqs = (len(corpus) - 1) // num_steps
        initial_indices = list(range(0, num_subseqs * num_steps, num_steps))
        random.shuffle(initial_indices)

        def data_slice(pos):
            return corpus[pos: pos + num_steps]

        num_batches = num_subseqs // batch_size
        for i in range(0, batch_size * num_batches, batch_size):
            initial_indices_per_batch = initial_indices[i: i + batch_size]
            X = [data_slice(j) for j in initial_indices_per_batch]
            Y = [data_slice(j + 1) for j in initial_indices_per_batch]
            yield torch.tensor(X), torch.tensor(Y)

    def seq_data_iter_sequential(self, corpus, batch_size, num_steps):
        """顺序划分子序列的迭代器。

        Yields:
            tuple[Tensor, Tensor]: ``(X, Y)``，形状 ``(batch_size, num_steps)``。
        """
        offset = random.randint(0, num_steps)
        num_tokens = ((len(corpus) - offset - 1) // batch_size) * batch_size
        Xs = torch.tensor(corpus[offset: offset + num_tokens])
        Ys = torch.tensor(corpus[offset + 1: offset + 1 + num_tokens])
        Xs, Ys = Xs.reshape(batch_size, -1), Ys.reshape(batch_size, -1)
        num_batches = Xs.shape[1] // num_steps
        for i in range(0, num_steps * num_batches, num_steps):
            X = Xs[:, i: i + num_steps]
            Y = Ys[:, i: i + num_steps]
            yield X, Y


# ---------------------------------------------------------------------------
# 机器翻译 / Seq2Seq 通用工具（自 CH9；Encoder/Decoder 架构留在 notebook）
# ---------------------------------------------------------------------------

def truncate_pad(line, num_steps, padding_token):
    """将序列截断或填充到长度 ``num_steps``。

    Args:
        line: 一维序列（词元或索引列表）。
        num_steps: 目标长度。
        padding_token: 填充值（索引或词元，与 ``line`` 元素类型一致）。

    Returns:
        list: 长度为 ``num_steps`` 的新序列（过长截断，过短右侧 pad）。
    """
    if len(line) > num_steps:
        return line[:num_steps]
    return line + [padding_token] * (num_steps - len(line))


def build_array_nmt(lines, num_steps, pad=0):
    """批量索引序列 -> 定长张量与有效长度。

    Args:
        lines: ``list[list[int]]``，每行一句的索引。
        num_steps: 截断/填充长度。
        pad: 填充索引，默认 0（常为 ``<unk>``；有 ``<pad>`` 时请传入其 id）。

    Returns:
        tuple:
            - array: ``LongTensor``，形状 ``(num_lines, num_steps)``。
            - valid_len: ``IntTensor``，形状 ``(num_lines,)``，非 pad 个数。
    """
    array = torch.tensor([truncate_pad(l, num_steps, pad) for l in lines])
    valid_len = (array != pad).type(torch.int32).sum(1)
    return array, valid_len


def load_data_cmn_eng(data_path):
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
        - 别名：``load_data_TdBSP``。
    """
    with open(data_path, 'r', encoding='utf-8') as f:
        Xs, Ys = [], []
        for line in f:
            parts = line.split('\t')
            if len(parts) >= 2:
                x = parts[0].split(' ')
                x[-1] = x[-1][:-1]
                x.append('<eos>')
                Xs.append(x)

                y = list(parts[1])
                y = y[:-1]
                y.append('<eos>')
                Ys.append(y)
        return Xs, Ys


# 兼容 CH9 notebook 旧名
load_data_TdBSP = load_data_cmn_eng


def preprocess_nmt(Xs, Ys, reserved_tokens=None):
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
        别名：``preprocess_data``。
    """
    if reserved_tokens is None:
        reserved_tokens = ['<bos>', '<eos>']
    if Xs and isinstance(Xs[0], str):
        Xs = tokenize(Xs, token='word')
        Ys = tokenize(Ys, token='word')
    src_vocab = Vocab(Xs, reserved_tokens=list(reserved_tokens))
    tgt_vocab = Vocab(Ys, reserved_tokens=list(reserved_tokens))
    X = [[src_vocab[tk] for tk in line] for line in Xs]
    Y = [[tgt_vocab[tk] for tk in line] for line in Ys]
    return X, Y, src_vocab, tgt_vocab


# 兼容旧名
preprocess_data = preprocess_nmt


def data_loader_nmt(X, Y, batch_size, num_steps, pad=0, shuffle=True):
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
        别名：``data_loader_TdBSP``。
    """
    X_array, X_valid_len = build_array_nmt(X, num_steps, pad)
    Y_array, Y_valid_len = build_array_nmt(Y, num_steps, pad)
    dataset = data.TensorDataset(X_array, X_valid_len, Y_array, Y_valid_len)
    return data.DataLoader(dataset, batch_size, shuffle=shuffle)


data_loader_TdBSP = data_loader_nmt


def sequence_mask(X, valid_len, value=0):
    """按有效长度遮蔽序列第二维（常用于 mask loss 权重）。

    Args:
        X: 张量，至少二维，形状 ``(batch, seq_len, ...)``；本函数按
            ``X.size(1)`` 与 ``valid_len`` 比较。
        valid_len: ``(batch,)``，每个样本的有效长度。
        value: 无效位置（padding）要写入的值。

    Returns:
        Tensor: 与 ``X`` 同形的克隆；位置 ``j >= valid_len[i]`` 被设为 ``value``。

    Notes:
        别名：``seq_mask``。
    """
    X = X.clone()
    maxlen = X.size(1)
    mask = (torch.arange(maxlen, dtype=torch.float32, device=X.device)[None, :]
            < valid_len[:, None])
    X[~mask] = value
    return X


seq_mask = sequence_mask


class MaskedSoftmaxCELoss(nn.CrossEntropyLoss):
    """带长度遮蔽的 Softmax 交叉熵（机器翻译常用）。

    Notes:
        padding 位置权重为 0；对时间维做 ``mean`` 后返回每样本损失。
    """

    def forward(self, pred, label, valid_len):
        """计算 batch 内逐样本的 masked CE。

        Args:
            pred: logits，``(batch, seq_len, vocab_size)``。
            label: 类别下标，``(batch, seq_len)``。
            valid_len: 有效长度，``(batch,)``。

        Returns:
            Tensor: 形状 ``(batch,)``，每个样本一个标量损失。
        """
        weights = torch.ones_like(label)
        weights = sequence_mask(weights, valid_len)
        self.reduction = 'none'
        unweighted_loss = super().forward(pred.permute(0, 2, 1), label)
        return (unweighted_loss * weights).mean(dim=1)


class EncoderDecoder(nn.Module):
    """编码器-解码器组合外壳。

    Notes:
        要求 ``decoder`` 实现 ``init_state(enc_outputs, *args)``。
        前向：``encode -> init_state -> decode``。
    """

    def __init__(self, encoder, decoder):
        """保存子模块。

        Args:
            encoder: 可调用 ``encoder(enc_X, *args)``。
            decoder: 需有 ``init_state`` 与 ``forward(dec_X, state)``。
        """
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder

    def forward(self, enc_X, dec_X, *args):
        """一次编码-解码前向。

        Args:
            enc_X: 源序列，通常 ``(batch, src_len)``。
            dec_X: 解码器输入（训练时为强制教学序列）。
            *args: 传给 encoder / ``init_state`` 的额外参数，如 ``X_valid_len``。

        Returns:
            decoder 的返回值，常见为 ``(Y_hat, state)``。
        """
        enc_outputs = self.encoder(enc_X, *args)
        dec_state = self.decoder.init_state(enc_outputs, *args)
        return self.decoder(dec_X, dec_state)


def train_seq2seq(net, data_iter, lr, num_epochs, tgt_vocab, device):
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
        - 损失为 ``MaskedSoftmaxCELoss``；更新前 ``grad_clipping(net, 1)``。
    """

    def xavier_init_weights(m):
        if type(m) == nn.Linear:
            nn.init.xavier_uniform_(m.weight)
        if type(m) == nn.GRU:
            for param in m._flat_weights_names:
                if 'weight' in param:
                    nn.init.xavier_uniform_(m._parameters[param])

    net.apply(xavier_init_weights)
    net.to(device)
    optimizer = torch.optim.Adam(net.parameters(), lr=lr)
    loss = MaskedSoftmaxCELoss()
    net.train()
    animator = AnimatorSimple(
        xlabel='epoch', ylabel='loss', xlim=[10, num_epochs])
    for epoch in range(num_epochs):
        timer = Timer()
        metric = Accumulator(2)  # loss 总和, 有效 token 数
        for batch in data_iter:
            optimizer.zero_grad()
            X, X_valid_len, Y, Y_valid_len = [x.to(device) for x in batch]
            bos = torch.tensor(
                [tgt_vocab['<bos>']] * Y.shape[0], device=device
            ).reshape(-1, 1)
            dec_input = torch.cat([bos, Y[:, :-1]], 1)  # 强制教学
            Y_hat, _ = net(X, dec_input, X_valid_len)
            l = loss(Y_hat, Y, Y_valid_len)
            l.sum().backward()
            grad_clipping(net, 1)
            num_tokens = Y_valid_len.sum()
            optimizer.step()
            with torch.no_grad():
                metric.add(l.sum(), num_tokens)
        if (epoch + 1) % 10 == 0:
            animator.add(epoch + 1, (metric[0] / metric[1],))
    print(
        f'loss {metric[0] / metric[1]:.3f}, '
        f'{metric[1] / timer.stop():.1f} tokens/sec on {str(device)}'
    )


def translate_seq2seq(net, src_sentence, src_vocab, tgt_vocab, num_steps,
                      device, pad=0, src_tokenize='word', tgt_join=''):
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
        别名：``translate``。
    """
    net.eval()
    if src_tokenize == 'word':
        src_tokens = src_sentence.strip().split(' ')
        if src_tokens:
            src_tokens[-1] = src_tokens[-1][:-1]
    elif src_tokenize == 'char':
        src_tokens = list(src_sentence.strip())
        if src_tokens:
            src_tokens = src_tokens[:-1]
    else:
        raise ValueError(f"未知 src_tokenize: {src_tokenize}")
    src_tokens = src_tokens + ['<eos>']
    src_ids = src_vocab[src_tokens]
    enc_valid_len = torch.tensor([len(src_ids)], device=device)
    src_ids = truncate_pad(src_ids, num_steps, pad)

    enc_X = torch.tensor(src_ids, dtype=torch.long, device=device).unsqueeze(0)
    enc_outputs = net.encoder(enc_X, enc_valid_len)
    dec_state = net.decoder.init_state(enc_outputs, enc_valid_len)
    dec_X = torch.tensor(
        [[tgt_vocab['<bos>']]], dtype=torch.long, device=device)

    output_seq = []
    for _ in range(num_steps):
        Y, dec_state = net.decoder(dec_X, dec_state)
        dec_X = Y.argmax(dim=2)
        pred = int(dec_X.squeeze(dim=0).item())
        if pred == tgt_vocab['<eos>']:
            break
        output_seq.append(pred)
    return tgt_join.join(tgt_vocab.to_tokens(output_seq))


# 兼容旧名
translate = translate_seq2seq


# ---------------------------------------------------------------------------
# 训练：MLP / CNN / RNN
# ---------------------------------------------------------------------------

def train_epoch(net, train_iter, loss, net_type='Classification',
                updater=None, device=None):
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
        Regression: ``(train_loss,)``。
    """
    metric = Accumulator(3)
    if isinstance(net, nn.Module):
        net.train()
    for X, y in train_iter:
        if device is not None:
            X, y = X.to(device), y.to(device)
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            updater.zero_grad()
            l.mean().backward()
            updater.step()
        else:
            l.sum().backward()
            updater(X.shape[0])
        if net_type == 'Classification':
            metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
        elif net_type == 'Regression':
            metric.add(float(l.sum()), y.numel())
    if net_type == 'Classification':
        return metric[0] / metric[2], metric[1] / metric[2]
    if net_type == 'Regression':
        return (metric[0] / metric[1],)
    return (0,)


def train_net(net, train_iter, test_iter, loss, num_epochs,
              net_type='Classification', updater=None, animate=True,
              device=None):
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
        ``(train_loss, test_loss)``。
    """
    if updater is None:
        raise ValueError('Please specify an updater, e.g., sgd')
    animator = None
    if animate:
        if net_type == 'Classification':
            animator = AnimatorSimple(
                xlabel='epoch', xlim=[1, num_epochs], ylim=[0, 1],
                legend=['train loss', 'train acc', 'test acc'])
        elif net_type == 'Regression':
            animator = AnimatorSimple(
                xlabel='epoch', xlim=[1, num_epochs], ylim=None,
                legend=['train loss', 'test loss'])
    for epoch in range(num_epochs):
        train_metrics = train_epoch(
            net, train_iter, loss, net_type=net_type,
            updater=updater, device=device)
        if net_type == 'Classification':
            test_acc = evaluate_accuracy(net, test_iter, device=device)
            train_metrics = train_metrics + (test_acc,)
        elif net_type == 'Regression':
            test_loss = evaluate_loss(net, test_iter, loss, device=device)
            train_metrics = train_metrics + (test_loss,)
        if animator is not None:
            animator.add(epoch + 1, train_metrics)
    if net_type == 'Classification':
        print(f'epoch {epoch + 1}, train loss {train_metrics[0]:.3f}, '
              f'train acc {train_metrics[1]:.3f}, test acc {test_acc:.3f}')
    elif net_type == 'Regression':
        print(f'epoch {epoch + 1}, train loss {train_metrics[0]:.3f}, '
              f'test loss {test_loss:.3f}')
    if animate:
        animator.close()
    return train_metrics


def train_cnn(net, train_iter, test_iter, loss=None, optimizer=None,
              num_epochs=10, lr=0.01, device=None, task='classification'):
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
        回归 ``(train_loss, test_loss)``。
    """
    if loss is None:
        loss = nn.CrossEntropyLoss() if task == 'classification' else nn.MSELoss()
    if device is None:
        device = try_gpu()

    net = net.to(device)
    if optimizer is None:
        optimizer = torch.optim.Adam(net.parameters(), lr=lr)

    if task == 'classification':
        animator = Animator(
            xlabel='epoch', xlim=[1, num_epochs],
            loss_legend=['train loss', 'test loss'],
            acc_legend=['train acc', 'test acc'],
        )
    else:
        animator = Animator(
            xlabel='epoch', xlim=[1, num_epochs],
            loss_legend=['train loss', 'test loss'],
        )
    final_score = None

    for epoch in range(num_epochs):
        net.train()
        train_loss, train_acc, n = 0.0, 0, 0
        for X, y in train_iter:
            X, y = X.to(device), y.to(device)
            optimizer.zero_grad()
            y_hat = net(X)
            l = loss(y_hat, y)
            l.backward()
            optimizer.step()
            bs = X.shape[0]
            train_loss += l.item() * bs
            n += bs
            if task == 'classification':
                train_acc += (y_hat.argmax(dim=1) == y).sum().item()

        train_loss /= n
        if task == 'classification':
            train_acc /= n

        net.eval()
        test_loss, test_acc, m = 0.0, 0, 0
        with torch.no_grad():
            for X, y in test_iter:
                X, y = X.to(device), y.to(device)
                y_hat = net(X)
                bs = X.shape[0]
                test_loss += loss(y_hat, y).item() * bs
                m += bs
                if task == 'classification':
                    test_acc += (y_hat.argmax(dim=1) == y).sum().item()

        test_loss /= m
        if task == 'classification':
            test_acc /= m
            final_score = (train_loss, train_acc, test_loss, test_acc)
            animator.add(epoch + 1, loss=(train_loss, test_loss),
                         acc=(train_acc, test_acc))
        else:
            final_score = (train_loss, test_loss)
            animator.add(epoch + 1, loss=(train_loss, test_loss))

    animator.close()
    if task == 'classification':
        print(f'训练损失: {final_score[0]:.3f}, 训练准确率: {final_score[1]:.3f}, '
              f'测试损失: {final_score[2]:.3f}, 测试准确率: {final_score[3]:.3f}')
    else:
        print(f'训练损失: {final_score[0]:.3f}, 测试损失: {final_score[1]:.3f}')
    return final_score


def predict_rnn(prefix, num_preds, net, vocab, device):
    """给定前缀，用 RNN 自回归生成后续词元。

    Args:
        prefix: 字符串前缀（按字符迭代；与字符级词表配套）。
        num_preds: 在预热 prefix 后要生成的词元个数。
        net: 需实现 ``begin_state`` 与 ``net(X, state) -> (y, state)``。
        vocab: ``Vocab``。
        device: 设备。

    Returns:
        str: 生成文本（词元以空格拼接的简单格式）。
    """
    state = net.begin_state(batch_size=1, device=device)
    outputs = [vocab[prefix[0]]]
    get_input = lambda: torch.tensor(
        [outputs[-1]], device=device).reshape((1, 1))
    for y in prefix[1:]:
        _, state = net(get_input(), state)
        outputs.append(vocab[y])
    for _ in range(num_preds):
        y, state = net(get_input(), state)
        outputs.append(int(y.argmax(dim=1).reshape(1)))
    return ''.join(vocab.idx_to_token[i] + ' ' for i in outputs)


def train_epoch_rnn(net, train_iter, loss, updater, device, use_random_iter):
    """训练 RNN 一个 epoch。

    Args:
        net: RNN 模型（``nn.Module`` 或从零实现）。
        train_iter: 产出 ``(X, Y)``，``X`` 为 ``(batch, num_steps)``。
        loss: 通常 ``nn.CrossEntropyLoss()``。
        updater: Optimizer 或 ``lambda batch_size: sgd(...)``。
        device: 设备。
        use_random_iter: True 时每 batch 重置隐状态（配合随机采样迭代器）。

    Returns:
        float: 本 epoch 困惑度 ``exp(平均交叉熵)``。
    """
    state = None
    metric = Accumulator(2)
    for X, y in train_iter:
        if state is None or use_random_iter:
            state = net.begin_state(batch_size=X.shape[0], device=device)
        else:
            if isinstance(net, nn.Module) and not isinstance(state, tuple):
                state.detach_()
            else:
                for s in state:
                    s.detach_()
        y = y.T.reshape(-1)
        X, y = X.to(device), y.to(device)
        y_hat, state = net(X, state)
        l = loss(y_hat, y.long()).mean()
        if isinstance(updater, torch.optim.Optimizer):
            updater.zero_grad()
            l.backward()
            grad_clipping(net, 1)
            updater.step()
        else:
            l.backward()
            grad_clipping(net, 1)
            updater(batch_size=1)
        metric.add(l.detach() * y.numel(), y.numel())
    return math.exp(metric[0] / metric[1])


def train_rnn(net, train_iter, vocab, lr, num_epochs, device,
              use_random_iter=False, prefix='time traveller'):
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
        若连续 5 次困惑度下降小于 ``1e-3`` 则早停。
    """
    last_perplexity = float('inf')
    count = 0
    loss = nn.CrossEntropyLoss()
    animator = AnimatorNoTest(
        xlabel='epoch', ylabel='perplexity', legend=['train'],
        xlim=[10, num_epochs])
    if isinstance(net, nn.Module):
        net = net.to(device)
        updater = torch.optim.SGD(net.parameters(), lr)
    else:
        updater = lambda batch_size: sgd(net.params, lr, batch_size)
    predict = lambda p: predict_rnn(p, 50, net, vocab, device)
    print_every = max(1, num_epochs // 100)
    perplexity = float('inf')
    for epoch in range(num_epochs):
        perplexity = train_epoch_rnn(
            net, train_iter, loss, updater, device, use_random_iter)
        if (epoch + 1) % print_every == 0:
            print(f'epoch {epoch + 1}, perplexity {perplexity:.1f}')
            animator.add(epoch + 1, [perplexity])
        if 0 < last_perplexity - perplexity < 1e-3:
            count += 1
            if count >= 5:
                print(f'早停于 epoch {epoch + 1}: 困惑度连续5次下降小于1e-3, '
                      f'当前 {perplexity:.1f}')
                break
        else:
            count = 0
        last_perplexity = perplexity
    print(f'困惑度: {perplexity:.1f}')
    print(predict(prefix))
    animator.close()
    return perplexity


# ---------------------------------------------------------------------------
# RNN 模型封装
# ---------------------------------------------------------------------------

def normal(shape, device):
    """从 ``N(0, 0.01)`` 采样初始化张量。

    Args:
        shape: 形状，传给 ``torch.randn``。
        device: 设备。

    Returns:
        Tensor: 标准差 0.01 的正态随机张量。
    """
    return torch.randn(size=shape, device=device) * 0.01


class RNNModelScratch:
    """从零实现 RNN 的薄包装（参数/状态/前向均由外部函数提供）。

    Notes:
        调用：``output, state = model(X, state)``，其中 ``X`` 为
        ``(batch, num_steps)`` 的词索引，内部会 one-hot 成
        ``(num_steps, batch, vocab_size)``。
    """

    def __init__(self, vocab_size, num_hiddens, device, get_params,
                 init_state, forward_fn):
        """
        Args:
            vocab_size: 词表大小。
            num_hiddens: 隐状态维数。
            device: 参数所在设备。
            get_params: ``(vocab_size, num_hiddens, device) -> params``。
            init_state: ``(batch_size, num_hiddens, device) -> state``。
            forward_fn: ``(X_onehot, state, params) -> (output, state)``。
        """
        self.vocab_size = vocab_size
        self.num_hiddens = num_hiddens
        self.init_state = init_state
        self.forward_fn = forward_fn
        self.params = get_params(vocab_size, num_hiddens, device)

    def __call__(self, X, state):
        """
        Args:
            X: 词索引 ``(batch_size, num_steps)``。
            state: 由 ``begin_state`` 得到的隐状态。

        Returns:
            forward_fn 的返回值，通常为 ``(output, new_state)``。
        """
        X = F.one_hot(X.T, self.vocab_size).type(torch.float32)
        return self.forward_fn(X, state, self.params)

    def begin_state(self, batch_size, device):
        """返回初始隐状态。

        Args:
            batch_size: 批量大小。
            device: 设备。
        """
        return self.init_state(batch_size, self.num_hiddens, device)


class RNNModel(nn.Module):
    """封装 ``nn.RNN`` / ``GRU`` / ``LSTM`` + 线性词表投影。

    Notes:
        ``forward(inputs, state)`` 中 ``inputs`` 为 ``(batch, num_steps)``；
        返回 ``(output, state)``，``output`` 形状 ``(batch*num_steps, vocab)``。
    """

    def __init__(self, rnn_layer, vocab_size, **kwargs):
        """
        Args:
            rnn_layer: 已构造的 ``nn.RNN/GRU/LSTM``。
            vocab_size: 输出词表大小。
        """
        super().__init__(**kwargs)
        self.rnn = rnn_layer
        self.vocab_size = vocab_size
        self.num_hiddens = self.rnn.hidden_size
        if not self.rnn.bidirectional:
            self.num_directions = 1
            self.linear = nn.Linear(self.num_hiddens, self.vocab_size)
        else:
            self.num_directions = 2
            self.linear = nn.Linear(self.num_hiddens * 2, self.vocab_size)

    def forward(self, inputs, state):
        """前向计算。

        Args:
            inputs: 词索引，形状 ``(batch_size, num_steps)``。
            state: RNN/GRU 隐状态，或 LSTM 的 ``(h, c)``。

        Returns:
            tuple: ``(output, state)``；``output`` 形状
            ``(batch_size * num_steps, vocab_size)``。
        """
        X = F.one_hot(inputs.T.long(), self.vocab_size).to(torch.float32)
        Y, state = self.rnn(X, state)
        output = self.linear(Y.reshape((-1, Y.shape[-1])))
        return output, state

    def begin_state(self, device, batch_size=1):
        """构造零初始状态。

        Args:
            device: 设备。
            batch_size: 批量大小，默认 1。

        Returns:
            Tensor | tuple[Tensor, Tensor]: GRU/RNN 为隐状态；LSTM 为 ``(h, c)``。
        """
        if not isinstance(self.rnn, nn.LSTM):
            return torch.zeros(
                (self.num_directions * self.rnn.num_layers,
                 batch_size, self.num_hiddens),
                device=device)
        return (
            torch.zeros(
                (self.num_directions * self.rnn.num_layers,
                 batch_size, self.num_hiddens),
                device=device),
            torch.zeros(
                (self.num_directions * self.rnn.num_layers,
                 batch_size, self.num_hiddens),
                device=device),
        )


# ---------------------------------------------------------------------------
# VGG 积木（跨 notebook 复用的块）
# ---------------------------------------------------------------------------

def vgg_block(num_convs, in_channels, out_channels):
    """构造一个 VGG 卷积块：``num_convs`` 个 3x3 Conv-ReLU + MaxPool2d。

    Args:
        num_convs: 卷积层个数。
        in_channels: 输入通道。
        out_channels: 输出通道（块内各卷积相同）。

    Returns:
        nn.Sequential: 该块；空间尺寸经池化后约为原来 1/2。
    """
    layers = []
    for _ in range(num_convs):
        layers.append(nn.Conv2d(
            in_channels=in_channels, out_channels=out_channels,
            kernel_size=3, padding=1))
        layers.append(nn.ReLU())
        in_channels = out_channels
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
    return nn.Sequential(*layers)


class VGGNet(nn.Module):
    """按 ``arch`` 描述堆叠的 VGG 分类网络。

    Notes:
        ``arch`` 形如 ``((num_convs, out_channels), ...)``。
        别名：``vggNet``。
    """

    def __init__(self, arch, in_channels, pic_size, num_classes=10):
        """
        Args:
            arch: 各 VGG 块配置 ``((num_convs, out_ch), ...)``。
            in_channels: 输入图像通道数（如 1 或 3）。
            pic_size: ``(H, W)``，用于推算 Flatten 后特征维。
            num_classes: 分类数，默认 10。
        """
        super().__init__()
        blocks = []
        h, w = pic_size
        for num_convs, out_channels in arch:
            blocks.append(vgg_block(
                num_convs=num_convs, in_channels=in_channels,
                out_channels=out_channels))
            in_channels = out_channels
            h //= 2
            w //= 2
        self.net = nn.Sequential(
            *blocks, nn.Flatten(),
            nn.Linear(in_channels * h * w, 4096), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(4096, 4096), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(4096, num_classes),
        )

    def forward(self, X):
        """
        Args:
            X: 图像张量 ``(batch, in_channels, H, W)``，``H,W`` 应与构造时
                ``pic_size`` 一致。

        Returns:
            Tensor: logits，形状 ``(batch, num_classes)``。
        """
        return self.net(X)


# 兼容旧名
vggNet = VGGNet


# ---------------------------------------------------------------------------
# 卷积教学：二维互相关（7.2）
# ---------------------------------------------------------------------------

class Corr2D(nn.Module):
    """二维互相关（卷积教学实现，无 padding/stride）。

    Notes:
        输入 ``X`` 为二维 ``(H, W)``；输出尺寸
        ``(H-kh+1, W-kw+1)``。别名：``corr2D``。
    """

    def __init__(self, kernel=None, kernel_size=(1, 1)):
        """
        Args:
            kernel: 初始核张量；``None`` 则按 ``kernel_size`` 随机初始化。
            kernel_size: 当 ``kernel is None`` 时使用的 ``(kh, kw)``。
        """
        super().__init__()
        if kernel is None:
            kernel = torch.randn(kernel_size)
        else:
            kernel_size = kernel.shape
        self.kernel_size = kernel_size
        self.weight = nn.Parameter(kernel)
        self.bias = nn.Parameter(torch.zeros(1))

    def forward(self, X):
        """二维互相关前向。

        Args:
            X: 二维输入 ``(H, W)``（教学示例，无 batch/channel 维）。

        Returns:
            Tensor: ``(H-kh+1, W-kw+1)``，已加 bias。
        """
        h, w = X.shape
        Y = torch.zeros(
            h - self.kernel_size[0] + 1,
            w - self.kernel_size[1] + 1,
        )
        for i in range(Y.shape[0]):
            for j in range(Y.shape[1]):
                Y[i, j] = (
                    X[i:i + self.kernel_size[0],
                      j:j + self.kernel_size[1]] * self.weight
                ).sum()
        return Y + self.bias


# 兼容旧名
corr2D = Corr2D


# ---------------------------------------------------------------------------
# Kaggle 房价：预处理与 K 折
# ---------------------------------------------------------------------------

def preprocess_kaggle_house(train_data, test_data, label='SalePrice'):
    """Kaggle 房价特征预处理：标准化数值列、one-hot 类别、标签取 log。

    Args:
        train_data: 训练 DataFrame（含 ``Id`` 与标签列）。
        test_data: 测试 DataFrame（含 ``Id``）。
        label: 标签列名，默认 ``'SalePrice'``。

    Returns:
        tuple[Tensor, Tensor, Tensor]:
            ``Xs_train, ys_train(log1p 价格), Xs_test``，均为 float32。
    """
    all_features = pd.concat((
        train_data.drop(columns=['Id', label]),
        test_data.drop(columns=['Id']),
    ))
    numeric_features = all_features.select_dtypes(include=['number']).columns
    all_features[numeric_features] = all_features[numeric_features].apply(
        lambda x: (x - x.mean()) / x.std()
    )
    all_features[numeric_features] = all_features[numeric_features].fillna(0)
    all_features = pd.get_dummies(all_features, dummy_na=True)
    Xs_train = all_features[:train_data.shape[0]]
    Xs_test = all_features[train_data.shape[0]:]
    ys_train = train_data[label].apply(np.log)
    return (
        torch.from_numpy(Xs_train.values.astype(np.float32)),
        torch.from_numpy(ys_train.values.astype(np.float32)),
        torch.from_numpy(Xs_test.values.astype(np.float32)),
    )


def train_kaggle_mlp(Xs, ys, num_epochs, batch_size, lr, dropouts,
                     hidden_layers, weight_decay, device, is_display=False):
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
        tuple: ``(net, final_train_loss)``。
    """
    animator = None
    if is_display:
        animator = AnimatorSimple(
            xlabel='epoch', xlim=[1, num_epochs], legend=['train loss'])
    layers = [
        nn.Linear(Xs.shape[1], hidden_layers[0]),
        nn.ReLU(),
        nn.Dropout(dropouts[0]),
    ]
    for i in range(1, len(hidden_layers)):
        layers.extend([
            nn.Linear(hidden_layers[i - 1], hidden_layers[i]),
            nn.ReLU(),
            nn.Dropout(dropouts[i]),
        ])
    layers.append(nn.Linear(hidden_layers[-1], 1))
    net = nn.Sequential(*layers).to(device)
    loss = nn.MSELoss()
    optimizer = torch.optim.Adam(
        net.parameters(), lr=lr, weight_decay=weight_decay)
    train_iter = data.DataLoader(
        data.TensorDataset(Xs, ys), batch_size=batch_size, shuffle=True)
    display_epoch = max(1, num_epochs // 500) if is_display else None
    epoch_loss = 0.0
    for epoch in range(num_epochs):
        net.train()
        for X, y in train_iter:
            X, y = X.to(device), y.to(device).reshape(-1, 1)
            optimizer.zero_grad()
            l = loss(net(X), y)
            l.backward()
            optimizer.step()
        net.eval()
        with torch.no_grad():
            epoch_loss = loss(
                net(Xs.to(device)), ys.to(device).reshape(-1, 1)).item()
        if is_display and epoch % display_epoch == 0:
            animator.add(epoch + 1, (epoch_loss,))
    if is_display:
        animator.close()
    return net, epoch_loss


def f_fold_data(k, Xs: torch.Tensor, ys: torch.Tensor):
    """生成 K 折中的各「训练折」数据（每折去掉一块验证段）。

    Args:
        k: 折数。
        Xs: 特征 ``(N, ...)``。
        ys: 标签 ``(N, ...)``。

    Returns:
        list[tuple[Tensor, Tensor]]: 长度 ``k``；第 i 项是去掉第 i 块后的
        ``(Xs_train, ys_train)``。

    Notes:
        每块大小为 ``N // k``，尾部不足一块的样本不会进入任何折。
    """
    folds = []
    fold_size = Xs.shape[0] // k
    for i in range(k):
        parts_X, parts_y = [], []
        for j in range(k):
            if j == i:
                continue
            idx = slice(j * fold_size, (j + 1) * fold_size)
            parts_X.append(Xs[idx])
            parts_y.append(ys[idx])
        folds.append((torch.cat(parts_X), torch.cat(parts_y)))
    return folds


def k_fold(trainer, Xs, ys, num_epochs, batch_size, K, lr, dropouts,
           hidden_layers, weight_decay, device, is_display=False):
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
        tuple: ``(models, avg_loss)``，``models`` 为各折模型列表。
    """
    val_loss, models = [], []
    for i, (Xs_fold, ys_fold) in enumerate(f_fold_data(K, Xs, ys)):
        show = is_display and i == 0
        model, fold_loss = trainer(
            Xs_fold, ys_fold, num_epochs, batch_size, lr, dropouts,
            hidden_layers, weight_decay, device, show)
        models.append(model)
        val_loss.append(fold_loss)
    avg_loss = sum(val_loss) / len(val_loss)
    return models, avg_loss


# ---------------------------------------------------------------------------
# 杂项
# ---------------------------------------------------------------------------

def tensor2str(t):
    """把张量压平后格式化为短字符串（便于打印）。

    Args:
        t: ``torch.Tensor`` 或其它；非 Tensor 原样返回。

    Returns:
        str | Any: 形如 ``"0.1234, 0.5678"`` 的字符串。
    """
    if isinstance(t, torch.Tensor):
        return np.array2string(
            t.detach().cpu().flatten().numpy(),
            formatter={'float_kind': '{:.4f}'.format},
            separator=', ',
        )
    return t


__all__ = [
    'try_gpu',
    'Accumulator', 'Timer',
    'accuracy', 'evaluate_accuracy', 'evaluate_loss',
    'Animator', 'AnimatorSimple', 'AnimatorNoTest',
    'sgd', 'l2_penalty', 'sgd_with_l2', 'dropout', 'grad_clipping',
    'load_data_fashion_mnist', 'get_data',
    'generate_data_of_linear_regression_with_noise',
    'DATA_HUB', 'download', 'read_time_machine',
    'tokenize', 'count_corpus', 'Vocab', 'SeqDataLoader',
    'truncate_pad', 'build_array_nmt',
    'load_data_cmn_eng', 'load_data_TdBSP',
    'preprocess_nmt', 'preprocess_data',
    'data_loader_nmt', 'data_loader_TdBSP',
    'sequence_mask', 'seq_mask', 'MaskedSoftmaxCELoss',
    'EncoderDecoder', 'train_seq2seq',
    'translate_seq2seq', 'translate',
    'train_epoch', 'train_net', 'train_cnn',
    'predict_rnn', 'train_epoch_rnn', 'train_rnn',
    'normal', 'RNNModelScratch', 'RNNModel',
    'vgg_block', 'VGGNet', 'vggNet',
    'Corr2D', 'corr2D',
    'preprocess_kaggle_house', 'train_kaggle_mlp', 'f_fold_data', 'k_fold',
    'tensor2str',
]
