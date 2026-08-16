"""兼容层：from utils.animator import Animator（单图 d2l 风格 = AnimatorSimple）。"""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    '_practice_utils_flat',
    Path(__file__).resolve().parent.parent / 'utils.py',
)
_flat = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_flat)

# CH4 kaggle / 旧 train_net 使用的单图 API
Animator = _flat.AnimatorSimple
AnimatorSimple = _flat.AnimatorSimple
AnimatorNoTest = _flat.AnimatorNoTest
AnimatorTwin = _flat.Animator  # 双子图版

__all__ = ['Animator', 'AnimatorSimple', 'AnimatorNoTest', 'AnimatorTwin']
