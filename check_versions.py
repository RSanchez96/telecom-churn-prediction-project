# check_versions.py
import importlib
import json

pkgs = ['pandas', 'sklearn', 'xgboost', 'optuna']
print(json.dumps({p: importlib.import_module(p).__version__ for p in pkgs}, indent=2))