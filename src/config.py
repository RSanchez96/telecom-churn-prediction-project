"""
Central place for reusable constants.
Edit here, import everywhere else.
"""

from pathlib import Path

# ---------- Paths ----------
PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]

DATA_DIR: Path    = PROJECT_ROOT / "data"
MODELS_DIR: Path  = PROJECT_ROOT / "models"

# ---------- Randomness ----------
GLOBAL_SEED: int = 990653

# ---------- Business constants ----------
CHURN_GAIN: int = 100_000   # Revenue kept by retaining a customer
CHURN_COST: int = -5_000    # Cost of wrongly flagging a non-churner