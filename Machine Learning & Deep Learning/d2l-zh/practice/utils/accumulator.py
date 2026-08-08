"""兼容层：from utils.accumulator import Accumulator"""

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

__all__ = ['Accumulator']
