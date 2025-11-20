# src/helpers.py
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def read_csv_safe(path, **kwargs):
    p = PROJECT_ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    return pd.read_csv(p, **kwargs)
