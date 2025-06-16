from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_selector as selector

def build_preprocessor(df):
    """
    • Pass numeric columns straight through (XGBoost handles NaNs).
    • One-hot-encode categoricals (no NaNs there, but we keep handle_unknown='ignore'
      for safety when scoring on future data).
    """
    num_cols = selector(dtype_include="number")(df)
    cat_cols = selector(dtype_include="object")(df)

    cat_pipe = Pipeline([
        ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
    ])

    pre = ColumnTransformer(
        transformers=[
            ("num", "passthrough", num_cols),   # no scaler / imputer
            ("cat", cat_pipe,      cat_cols)
        ],
        remainder="drop"
    )
    return pre, num_cols, cat_cols