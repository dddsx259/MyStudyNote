"""兼容层：from utils.train_model import train_net, sgd, ..."""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    '_practice_utils_flat',
    Path(__file__).resolve().parent.parent / 'utils.py',
)
_flat = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_flat)

Accumulator = _flat.Accumulator
accuracy = _flat.accuracy
evaluate_accuracy = _flat.evaluate_accuracy
evaluate_loss = _flat.evaluate_loss
sgd = _flat.sgd
train_epoch = _flat.train_epoch
train_net = _flat.train_net
train_cnn = _flat.train_cnn
train_rnn = _flat.train_rnn

__all__ = [
    'Accumulator',
    'accuracy',
    'evaluate_accuracy',
    'evaluate_loss',
    'sgd',
    'train_epoch',
    'train_net',
    'train_cnn',
    'train_rnn',
]
