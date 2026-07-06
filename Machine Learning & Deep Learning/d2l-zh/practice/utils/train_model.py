from .accumulator import Accumulator
from .animator import Animator
import json
import time
import torch
from torch import nn

# #region agent log
_DEBUG_LOG_PATH = '/home/dddsx259/Study/MyStudyNote/.cursor/debug-271739.log'
_DEBUG_SESSION = '271739'
_DEBUG_LOGGED_NETS = set()

def _debug_log(location, message, data, hypothesis_id, run_id='pre-fix'):
    payload = {
        'sessionId': _DEBUG_SESSION,
        'runId': run_id,
        'hypothesisId': hypothesis_id,
        'location': location,
        'message': message,
        'data': data,
        'timestamp': int(time.time() * 1000),
    }
    with open(_DEBUG_LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(payload, default=str) + '\n')
# #endregion

def accuracy(y_hat, y):
    if len(y_hat.shape) > 1 and y_hat.shape[1] > 1:
        y_hat = y_hat.argmax(axis=1)
    cmp = y_hat.type(y.dtype) == y
    return float(cmp.type(y.dtype).sum())

def evaluate_accuracy(net, data_iter, device=None):
    if isinstance(net, nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # 正确预测数、预测总数
    with torch.no_grad():
        for X, y in data_iter:
            if device is not None:
                X, y = X.to(device), y.to(device)
            metric.add(accuracy(net(X), y), y.numel())
    return metric[0] / metric[1]

def evaluate_loss(net, data_iter, loss, device=None):
    if isinstance(net, torch.nn.Module):
        net.eval()  # 将模型设置为评估模式
    metric = Accumulator(2)  # Sum of loss, num of samples
    with torch.no_grad():
        for X, y in data_iter:
            if device is not None:
                X, y = X.to(device), y.to(device)
            metric.add(float(loss(net(X), y).sum()), y.numel())
    return metric[0] / metric[1]

def train_epoch(net, train_iter, loss, net_type='Classification', updater=None, device=None):
    metric = Accumulator(3) # Sum of loss, Sum of accuracy, num of samples
    if isinstance(net, torch.nn.Module):
        net.train()
    batch_count = 0
    for X, y in train_iter:
        batch_count += 1
        if device is not None:
            X, y = X.to(device), y.to(device)
        y_hat = net(X)
        l = loss(y_hat, y)
        if isinstance(updater, torch.optim.Optimizer):
            # When using built-in optimizers, scale the loss by batch size
            # to make gradients comparable to the custom `sgd` updater
            # #region agent log
            if id(net) not in _DEBUG_LOGGED_NETS:
                first_linear = next(m for m in net.modules() if isinstance(m, nn.Linear))
                opt_param_ids = {id(p) for group in updater.param_groups for p in group['params']}
                net_param_ids = {id(p) for p in net.parameters()}
                weight_before = float(first_linear.weight.data[0, 0].item())
                updater.zero_grad()
                l.mean().backward()
                grad_norm = float(first_linear.weight.grad.norm().item()) if first_linear.weight.grad is not None else None
                updater.step()
                weight_after = float(first_linear.weight.data[0, 0].item())
                _debug_log(
                    'train_model.py:train_epoch',
                    'first-batch optimizer/param audit',
                    {
                        'batch_count_so_far': batch_count,
                        'net_name': net.__class__.__name__,
                        'optimizer_param_count': len(opt_param_ids),
                        'net_param_count': len(net_param_ids),
                        'optimizer_matches_net': opt_param_ids == net_param_ids,
                        'optimizer_subset_of_net': opt_param_ids.issubset(net_param_ids),
                        'weight_before': weight_before,
                        'weight_after': weight_after,
                        'weight_delta': weight_after - weight_before,
                        'grad_norm_first_linear': grad_norm,
                        'loss_mean': float(l.mean().item()),
                        'batch_acc': accuracy(y_hat, y) / y.numel(),
                        'y_hat_std': float(y_hat.std().item()),
                    },
                    'H1',
                )
                _DEBUG_LOGGED_NETS.add(id(net))
            else:
                updater.zero_grad()
                l.mean().backward()
                updater.step()
            # #endregion
        else:
            l.sum().backward()
            updater(X.shape[0])
        if net_type == 'Classification':
            metric.add(float(l.sum()), accuracy(y_hat, y), y.numel())
        elif net_type == 'Regression':
            metric.add(float(l.sum()), y.numel())
    # #region agent log
    if net_type == 'Classification':
        _debug_log(
            'train_model.py:train_epoch',
            'epoch batch summary',
            {
                'batch_count': batch_count,
                'total_samples': metric[2],
                'train_acc': metric[1] / metric[2] if metric[2] else None,
            },
            'H5',
        )
    # #endregion
    if net_type == 'Classification':
        return metric[0] / metric[2], metric[1] / metric[2]
    elif net_type == 'Regression':
        return (metric[0] / metric[1],)
    return (0,)

def sgd(params, lr, batch_size):
    with torch.no_grad():
        for param in params:
            if param.grad is not None:
                param.data -= lr * param.grad / batch_size
                param.grad.zero_()

def train_net(net, train_iter, test_iter, loss, num_epochs, net_type='Classification', updater = None, animate = True, device = None):
    animator = None
    if animate:
        if net_type == 'Classification':
            animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=[0, 1],
                                legend=['train loss', 'train acc', 'test acc'])
        elif net_type == 'Regression':
            animator = Animator(xlabel='epoch', xlim=[1, num_epochs], ylim=None,
                            legend=['train loss','test loss'])
    if updater is None:
        raise ValueError('Plaease specify an updater, e.g., sgd')
    for epoch in range(num_epochs):
        train_metrics = train_epoch(net, train_iter, loss, net_type=net_type, updater=updater, device=device)
        if net_type == 'Classification':
            test_acc = evaluate_accuracy(net, test_iter, device=device)
            # #region agent log
            if epoch in (0, num_epochs - 1):
                with torch.no_grad():
                    sample_X, sample_y = next(iter(test_iter))
                    if device is not None:
                        sample_X = sample_X.to(device)
                    logits = net(sample_X[:32])
                    pred = logits.argmax(dim=1)
                    _debug_log(
                        'train_model.py:train_net',
                        'epoch eval snapshot',
                        {
                            'epoch': epoch + 1,
                            'train_acc': train_metrics[1],
                            'test_acc': test_acc,
                            'unique_preds_in_batch': int(pred.unique().numel()),
                            'logits_std': float(logits.std().item()),
                        },
                        'H4',
                    )
            # #endregion
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
        print(f'epoch {epoch + 1}, train loss {train_metrics[0]:.3f}, test loss {test_loss:.3f}')
    if animate:
        animator.close()
