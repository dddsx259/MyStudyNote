"""practice/utils 包：从同级 utils.py 再导出，并保留子模块以兼容旧 import。"""

from __future__ import annotations

import importlib.util
from pathlib import Path

_FLAT = Path(__file__).resolve().parent.parent / 'utils.py'
_spec = importlib.util.spec_from_file_location('_practice_utils_flat', _FLAT)
_flat = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_flat)

# 从扁平 utils.py 再导出全部公开符号
for _name in getattr(_flat, '__all__', []):
    globals()[_name] = getattr(_flat, _name)

__all__ = list(getattr(_flat, '__all__', []))

# 兼容: from utils.train_model import ... / from utils.animator import ...
from . import accumulator  # noqa: E402,F401
from . import animator  # noqa: E402,F401
from . import get_data  # noqa: E402,F401
from . import train_model  # noqa: E402,F401

__all__ += ['accumulator', 'animator', 'get_data', 'train_model']
