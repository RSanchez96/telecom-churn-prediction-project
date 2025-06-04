# Telecom Churn Prediction Project

This repository contains my predictive modeling work for identifying potential customer churn in a fictional telecom company.

## 🔧 How to Run This Project

To ensure that relative paths and module imports work correctly:

1. Clone this repository.
2. Always execute notebooks from the **root of the project**, not from within subfolders.
3. Activate your virtual environment and launch the notebook:
jupyter notebook churn-xgb.ipynb

Expected project structure:
    telecom-churn-prediction-project/
    ├── churn-xgb.ipynb
    ├── src/
    │   └── config.py
    ├── data/
    │   └── WA_telco_data.csv
    ├── models/
    ├── requirements.txt

This setup ensures the following imports work without errors:
    from src.config import DATA_DIR