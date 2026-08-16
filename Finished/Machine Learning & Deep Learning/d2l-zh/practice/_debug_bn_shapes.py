import json
import time
import torch
from torch import nn

LOG = "/Users/dddsx259/Library/CloudStorage/OneDrive-TheUniversityofHongKong-Connect/学习/notes/My Study Notes/.cursor/debug-6f6a97.log"

def log(hypothesis_id, message, data, run_id="post-fix"):
    # region agent log
    entry = {"sessionId": "6f6a97", "runId": run_id, "hypothesisId": hypothesis_id,
             "location": "_debug_bn_shapes.py", "message": message, "data": data,
             "timestamp": int(time.time() * 1000)}
    with open(LOG, "a") as f:
        f.write(json.dumps(entry) + "\n")
    # endregion

def batch_norm(X, gamma, beta, moving_mean, moving_var, eps, momentum):
    if not torch.is_grad_enabled():
        X_hat = (X - moving_mean) / torch.sqrt(moving_var + eps)
    else:
        if len(X.shape) == 2:
            mean = X.mean(dim=0)
            var = ((X - mean) ** 2).mean(dim=0)
        else:
            mean = X.mean(dim=(0, 2, 3), keepdim=True)
            var = ((X - mean) ** 2).mean(dim=(0, 2, 3), keepdim=True)
        X_hat = (X - mean) / torch.sqrt(var + eps)
        moving_mean = momentum * moving_mean + (1.0 - momentum) * mean
        moving_var = momentum * moving_var + (1.0 - momentum) * var
    Y = gamma * X_hat + beta
    return Y, moving_mean.data, moving_var.data

class BatchNorm(nn.Module):
    def __init__(self, num_features, num_dims):
        super().__init__()
        shape = (1, num_features) if num_dims == 2 else (1, num_features, 1, 1)
        self.gamma = nn.Parameter(torch.ones(shape))
        self.beta = nn.Parameter(torch.zeros(shape))
        self.moving_mean = torch.zeros(shape)
        self.moving_var = torch.ones(shape)
    def forward(self, X):
        Y, self.moving_mean, self.moving_var = batch_norm(
            X, self.gamma, self.beta, self.moving_mean, self.moving_var, 1e-5, 0.9)
        return Y

class myLeNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 6, kernel_size=5, padding=2), BatchNorm(6, 4), nn.Sigmoid(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Conv2d(6, 16, kernel_size=5), BatchNorm(16, 4), nn.Sigmoid(),
            nn.AvgPool2d(kernel_size=2, stride=2),
            nn.Flatten(),
            nn.Linear(16 * 5 * 5, 120), BatchNorm(120, 2), nn.Sigmoid(),
            nn.Linear(120, 84), BatchNorm(84, 2), nn.Sigmoid(),
            nn.Linear(84, 10),
        )
    def forward(self, X):
        return self.net(X)

x = torch.randn(128, 1, 28, 28)
net = myLeNet()
shapes = []
for i, m in enumerate(net.net):
    x = m(x)
    shapes.append({"i": i, "layer": type(m).__name__, "shape": list(x.shape)})

log("H2", "fixed myLeNet forward shapes", {"shapes": shapes, "final_shape": list(x.shape)})
log("H3", "training step smoke test", {"ok": False})

net.train()
opt = torch.optim.Adam(net.parameters(), lr=0.01)
loss_fn = nn.CrossEntropyLoss()
X = torch.randn(128, 1, 28, 28)
y = torch.randint(0, 10, (128,))
opt.zero_grad()
out = net(X)
l = loss_fn(out, y)
l.backward()
opt.step()
acc = (out.argmax(1) == y).float().mean().item()
log("H3", "training step smoke test", {"ok": True, "loss": l.item(), "acc": acc})
print("post-fix ok", list(out.shape), l.item())
