import numpy as np
import random
import os

def set_global_seed(seed: int) -> None:
    """Force reproducible behaviour across numpy, Python, and hash-based ops."""
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)