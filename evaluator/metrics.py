"""Task-aware calculation of classification and regression metrics."""
from __future__ import annotations

import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score, confusion_matrix, f1_score, mean_absolute_error,
    mean_squared_error, precision_score, r2_score, recall_score,
)

SUPPORTED_METRICS = {
    "Classification": ["Accuracy", "Precision", "Recall", "F1-score"],
    "Regression": ["MAE", "MSE", "RMSE", "R²"],
}
CLASSIFICATION_AVERAGES = ["weighted", "macro", "micro", "binary"]


def calculate_metrics(
    task_type: str,
    y_true: pd.Series,
    y_pred: pd.Series,
    selected_metrics: list[str],
    average: str = "weighted",
    positive_label: object | None = None,
) -> tuple[dict[str, float | None], pd.DataFrame | None, int]:
    if task_type not in SUPPORTED_METRICS:
        raise ValueError("Unsupported evaluation task.")
    if set(selected_metrics) - set(SUPPORTED_METRICS[task_type]):
        raise ValueError("Selected metrics do not match the evaluation task.")
    if not selected_metrics:
        raise ValueError("Select at least one metric.")
    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted sequences must have the same length.")

    valid = y_true.notna() & y_pred.notna()
    actual, predicted = y_true[valid], y_pred[valid]
    if len(actual) == 0:
        raise ValueError("No valid rows remain after removing missing values.")

    results: dict[str, float | None] = {}
    matrix = None
    if task_type == "Classification":
        if actual.nunique() < 2:
            raise ValueError("Classification evaluation requires at least two distinct actual classes.")
        if average not in CLASSIFICATION_AVERAGES:
            raise ValueError("Choose a supported classification averaging method.")
        if average == "binary":
            if actual.nunique() != 2:
                raise ValueError("Binary averaging requires exactly two actual classes.")
            if positive_label not in set(actual.unique()):
                raise ValueError("Choose a positive class present in the actual values.")

        common = {"average": average, "zero_division": 0}
        if average == "binary":
            common["pos_label"] = positive_label
        if "Accuracy" in selected_metrics:
            results["Accuracy"] = float(accuracy_score(actual, predicted))
        if "Precision" in selected_metrics:
            results["Precision"] = float(precision_score(actual, predicted, **common))
        if "Recall" in selected_metrics:
            results["Recall"] = float(recall_score(actual, predicted, **common))
        if "F1-score" in selected_metrics:
            results["F1-score"] = float(f1_score(actual, predicted, **common))

        unique_labels = set(actual.unique()) | set(predicted.unique())
        try:
            labels = sorted(unique_labels)
        except TypeError:
            labels = sorted(unique_labels, key=str)
        matrix = pd.DataFrame(
            confusion_matrix(actual, predicted, labels=labels),
            index=pd.Index(labels, name="Actual"),
            columns=pd.Index(labels, name="Predicted"),
        )
    else:
        try:
            actual_n = pd.to_numeric(actual, errors="raise")
            predicted_n = pd.to_numeric(predicted, errors="raise")
        except (ValueError, TypeError) as exc:
            raise ValueError("Regression requires numeric actual and predicted values.") from exc
        if not (np.isfinite(actual_n).all() and np.isfinite(predicted_n).all()):
            raise ValueError("Regression values must be finite numbers.")
        if "MAE" in selected_metrics:
            results["MAE"] = float(mean_absolute_error(actual_n, predicted_n))
        if "MSE" in selected_metrics:
            results["MSE"] = float(mean_squared_error(actual_n, predicted_n))
        if "RMSE" in selected_metrics:
            results["RMSE"] = float(np.sqrt(mean_squared_error(actual_n, predicted_n)))
        if "R²" in selected_metrics:
            results["R²"] = float(r2_score(actual_n, predicted_n)) if len(actual_n) >= 2 else None
    return results, matrix, len(actual)


def regression_residual_summary(
    y_true: pd.Series, y_pred: pd.Series
) -> dict[str, float]:
    """Return signed prediction-error summaries after paired-null filtering."""
    if len(y_true) != len(y_pred):
        raise ValueError("Actual and predicted sequences must have the same length.")
    valid = y_true.notna() & y_pred.notna()
    try:
        actual = pd.to_numeric(y_true[valid], errors="raise")
        predicted = pd.to_numeric(y_pred[valid], errors="raise")
    except (ValueError, TypeError) as exc:
        raise ValueError("Regression requires numeric actual and predicted values.") from exc
    if len(actual) == 0:
        raise ValueError("No valid rows remain after removing missing values.")
    if not (np.isfinite(actual).all() and np.isfinite(predicted).all()):
        raise ValueError("Regression values must be finite numbers.")
    residuals = actual - predicted
    return {
        "Mean Error": float(residuals.mean()),
        "Minimum Error": float(residuals.min()),
        "Maximum Error": float(residuals.max()),
        "Mean Absolute Error": float(residuals.abs().mean()),
    }
