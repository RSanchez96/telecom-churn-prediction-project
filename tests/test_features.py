import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

import pandas as pd
from src.features import fe_transformer

def test_charges_amount_creation():
    df = pd.DataFrame({
        "MonthlyCharges": [50, 100, 0],
        "TotalCharges": [150, 200, 0],
        "MultipleLines": ["Yes", "No", "No phone service"],
        "OnlineSecurity": ["Yes", "No", "No internet service"],
        "OnlineBackup": ["No", "Yes", "No internet service"],
        "DeviceProtection": ["No", "Yes", "No internet service"],
        "TechSupport": ["No", "Yes", "No internet service"],
        "StreamingTV": ["No", "Yes", "No internet service"],
        "StreamingMovies": ["No", "Yes", "No internet service"],
        "Partner": ["Yes", "No", "Yes"],
        "Dependents": ["No", "Yes", "No"],
        "PhoneService": ["Yes", "No", "Yes"],
        "PaperlessBilling": ["Yes", "No", "Yes"],
        "Churn": ["Yes", "No", "Yes"]
    })

    df_out = fe_transformer.fit_transform(df)

    assert "ChargesAmount" in df_out.columns, "ChargesAmount not created"
    assert pd.api.types.is_numeric_dtype(df_out["ChargesAmount"]), "ChargesAmount is not numeric"

