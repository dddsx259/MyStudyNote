import torch
import torch.nn as nn

class corr2D(nn.Module):
    def __init__(self, kernel = None, kernel_size = (1, 1)):
        super().__init__()
        if kernel is None:
            kernel =torch.randn(kernel_size)
        else:
            kernel_size = kernel.shape
        self.kernel_size = kernel_size
        self.weight = nn.Parameter(kernel)
        self.bias = nn.Parameter(torch.zeros(1))

    def forward(self, X):
        h, w = X.shape
        Y = torch.zeros(
            h - self.kernel_size[0] + 1,
            w - self.kernel_size[1] + 1
        )
        for i in range(Y.shape[0]):
            for j in range(Y.shape[1]):
                Y[i, j] = (X[i:i+self.kernel_size[0], j:j+self.kernel_size[1]] * self.weight).sum()
        return Y + self.bias

import matplotlib.pyplot as plt
from IPython import display
class Animator:
    """在 Jupyter 训练循环中实时刷新曲线。分类任务用双子图：上 loss、下 acc。"""

    def __init__(self, xlabel='epoch', xlim=None,
                 loss_legend=None, acc_legend=None, acc_ylim=(0, 1),
                 fmts=('-', 'm--', 'g-.', 'r:', 'c-', 'y--', 'k-.', 'b:'),
                 figsize=(5, 6)):
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
            self.fig, self.ax_loss = plt.subplots(1, 1, figsize=(figsize[0], figsize[1] / 2))
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
        """追加数据并重绘。分类: add(epoch, loss=(tr, te), acc=(tr, te))。"""
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
        plt.close(self.fig)
        
def train_cnn(net, train_iter, test_iter, loss=None, optimizer=None, num_epochs=10, lr=0.01, device=None, task='classification'):
    if loss is None:
        loss = nn.CrossEntropyLoss() if task == 'classification' else nn.MSELoss()
    if device is None:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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
        print(f"训练损失: {final_score[0]:.3f}, 训练准确率: {final_score[1]:.3f}, "
              f"测试损失: {final_score[2]:.3f}, 测试准确率: {final_score[3]:.3f}")
    else:
        print(f"训练损失: {final_score[0]:.3f}, 测试损失: {final_score[1]:.3f}")
    return final_score

import torchvision
from torchvision import transforms
from torch.utils import data
def load_data_fashion_mnist(batch_size):
    trans = transforms.ToTensor()
    train_set = torchvision.datasets.FashionMNIST(
        './data', train=True, transform=trans, download=True)
    test_set = torchvision.datasets.FashionMNIST(
        './data', train=False, transform=trans, download=True)
    train_iter = data.DataLoader(train_set, batch_size, shuffle=True, num_workers=0)
    test_iter = data.DataLoader(test_set, batch_size, shuffle=False, num_workers=0)
    return train_iter, test_iter

def vgg_block(num_convs, in_channels, out_channels):
    layers = []
    for _ in range(num_convs):
        layers.append(nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, padding=1))
        layers.append(nn.ReLU())
        in_channels = out_channels
    layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
    return nn.Sequential(*layers)        

class vggNet(nn.Module):
    def __init__(self, arch, in_channels, pic_size, num_classes=10):
        super().__init__()
        blocks = []
        h, w = pic_size
        for num_convs, out_channels in arch:
            blocks.append(vgg_block(num_convs=num_convs, in_channels=in_channels, out_channels=out_channels))
            in_channels = out_channels
            h //= 2
            w //= 2
        self.net = nn.Sequential(
            *blocks, nn.Flatten(),
            nn.Linear(in_channels * h * w, 4096), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(4096, 4096), nn.ReLU(), nn.Dropout(0.5),
            nn.Linear(4096, num_classes)
            )
        
    def forward(self, X):
        return self.net(X)

def tokenize(lines, token='word'):
    """将文本行拆分为单词或字符词元。"""
    if token == 'word':
        return [line.split() for line in lines]
    elif token == 'char':
        return [list(line) for line in lines]
    else:
        print(f"错误: 未知词元类型: '{token}'")
import collections

def count_corpus(tokens):
    if isinstance(tokens, list):
        tokens = [tk for line in tokens for tk in line]
    return collections.Counter(tokens)

class Vocab:
    """文本词表"""
    def __init__(self, tokens=None, min_freq=0, reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens is None:
            reserved_tokens = []
        # 按出现频率排序
        counter = count_corpus(tokens)
        self._token_freqs = sorted(counter.items(), key=lambda x: x[1],
                                   reverse=True)
        # 未知词元的索引为0
        self.idx_to_token = ['<unk>'] + reserved_tokens
        self.token_to_idx = {token: idx
                             for idx, token in enumerate(self.idx_to_token)}
        for token, freq in self._token_freqs:
            if freq < min_freq:
                break
            if token not in self.token_to_idx:
                self.idx_to_token.append(token)
                self.token_to_idx[token] = len(self.idx_to_token) - 1

    def __len__(self):
        return len(self.idx_to_token)

    def __getitem__(self, tokens):
        if not isinstance(tokens, (list, tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]

    def to_tokens(self, indices):
        if not isinstance(indices, (list, tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]

    @property
    def unk(self):  # 未知词元的索引为0
        return 0

    @property
    def token_freqs(self):
        return self._token_freqs
