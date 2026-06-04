from .accumulator import Accumulator
from .animator import Animator
import torch

def accuracy(y_hat, y):
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())

def evaluate_accuracy(net, data_iter):
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]

def train_epoch_perceptron(net, train_iter, loss, updater):
    metric = Accumulator(3) # Sum of loss, Sum of accuracy, num of samples
    if isinstance(updater, torch.nn.Module):
        net.train()
    for X, y in train_iter:
        y_hat = net(X)
        l = loss(y_hat, y)
        l_sum = l.sum()
        if isinstance(updater, torch.optim.Optimizer):
            updater.zero_grad()
            l_sum.backward()
            updater.step()
        else:
            l_sum.backward()
            updater(X.shape[0])
        metric.add(float(l_sum), accuracy(y_hat, y), y.numel())
    return metric[0] / metric[2], metric[1] / metric[2]

def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            if param.grad is not None:
                param.data -= lr * param.grad / batch_size
                param.grad.zero_()

def train_perceptron(net, train_iter, test_iter, loss, num_epochs, updater = None, animate = True, alart = False):
    animator = None
    if animate:
        animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0.3, 0.9],
                            legend=['train loss', 'train acc', 'test acc'])
    if updater is None:
        raise ValueError('Plaease specify an updater, e.g., sgd')
    print_interval = max(1, num_epochs // 5)
    for epoch in range(num_epochs):
        train_metrics = train_epoch_perceptron(net, train_iter, loss, updater)
        test_acc = evaluate_accuracy(net, test_iter)
        if animator is not None:
            animator.add(epoch + 1, train_metrics + (test_acc,))
        if (epoch + 1) % print_interval == 0:
             print(f'epoch {epoch + 1}, train loss {train_metrics[0]:.3f}, '
                   f'train acc {train_metrics[1]:.3f}, test acc {test_acc:.3f}')
    train_loss, train_acc = train_metrics
    if alart:
        assert train_loss < 0.5, train_loss
        assert train_acc <= 1 and train_acc > 0.7, train_acc
        assert test_acc <= 1 and test_acc > 0.7, test_acc
