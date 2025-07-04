import pandas as pd
import numpy as np
from sklearn.preprocessing import FunctionTransformer


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Binary mappings
    bin_map = {'No': 0, 'Yes': 1}
    service_map = {'No': 0, 'No internet service': 0, 'Yes': 1}
    phone_map = {'No': 0, 'No phone service': 0, 'Yes': 1}

    df['MultipleLines'] = df['MultipleLines'].map(phone_map)
    df['OnlineSecurity'] = df['OnlineSecurity'].map(service_map)
    df['OnlineBackup'] = df['OnlineBackup'].map(service_map)
    df['DeviceProtection'] = df['DeviceProtection'].map(service_map)
    df['TechSupport'] = df['TechSupport'].map(service_map)
    df['StreamingTV'] = df['StreamingTV'].map(service_map)
    df['StreamingMovies'] = df['StreamingMovies'].map(service_map)
    df['Partner'] = df['Partner'].map(bin_map)
    df['Dependents'] = df['Dependents'].map(bin_map)
    df['PhoneService'] = df['PhoneService'].map(bin_map)
    df['PaperlessBilling'] = df['PaperlessBilling'].map(bin_map)
    df['Churn'] = df['Churn'].map(bin_map)

    # ChargesAmount: create new column
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['ChargesAmount'] = df['TotalCharges'] / df['MonthlyCharges']

    return df


# Scikit-learn compatible transformer
fe_transformer = FunctionTransformer(feature_engineering, validate=False)