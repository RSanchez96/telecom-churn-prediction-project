import sys
from pathlib import Path  # <- ESTA LÍNEA FALTABA

# Añadir la raíz del proyecto al path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from src.prep import build_preprocessor
import pandas as pd

def test_num_encoded_dims():
    df = pd.DataFrame({
        "num": [1, 2, None],
        "cat": ["a", "b", "a"]
    })
    pre, *_ = build_preprocessor(df)
    out = pre.fit_transform(df)
    assert out.shape[1] == 3  # 1 numeric passthrough + 2 OHE for 'cat'