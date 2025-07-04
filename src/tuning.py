import optuna
from sklearn.model_selection import cross_val_score
from sklearn.base import clone

def objective(trial, pipe, X, y, cv):
    # Clone to avoid state carryover
    pipe = clone(pipe)

    # Suggest hyperparameters for XGBoost
    pipe.set_params(
        clf__n_estimators=trial.suggest_int("n_estimators", 100, 500),
        clf__max_depth=trial.suggest_int("max_depth", 3, 6),
        clf__learning_rate=trial.suggest_float("learning_rate", 1e-3, 0.1),
        clf__subsample=trial.suggest_float("subsample", 0.5, 1.0),
        clf__gamma=trial.suggest_float("gamma", 1, 9),
        clf__reg_alpha=trial.suggest_float("reg_alpha", 2, 6)
    )

    # Evaluate using cross-validation
    score = cross_val_score(pipe, X, y, cv=cv, scoring="roc_auc", n_jobs=-1).mean()

    # Save best model
    trial.set_user_attr("best_pipeline", pipe)

    return score