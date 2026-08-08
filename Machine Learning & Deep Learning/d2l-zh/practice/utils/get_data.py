"""兼容层：from utils.get_data import get_data"""

import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location(
    '_practice_utils_flat',
    Path(__file__).resolve().parent.parent / 'utils.py',
)
_flat = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_flat)

get_data = _flat.get_data
load_data_fashion_mnist = _flat.load_data_fashion_mnist

__all__ = ['get_data', 'load_data_fashion_mnist']
