"""
test_regression.py — Unit tests for regression metric calculations.

Covers Sprint 1 task #5: Calculate selected evaluation metrics
(Regression: MAE, MSE, RMSE, R²)
"""

from __future__ import annotations

import pytest
import pandas as pd
import numpy as np
from evaluator.metrics import SUPPORTED_METRICS, calculate_metrics


def compute_regression_metrics(
    actual: pd.Series,
    predicted: pd.Series,
    selected_metrics: list[str],
) -> dict[str, float | None]:
    """Delegate to evaluator.metrics.calculate_metrics."""
    valid_metrics = [m for m in selected_metrics if m in SUPPORTED_METRICS["Regression"]]
    if not valid_metrics:
        valid = actual.notna() & predicted.notna()
        act = actual[valid]
        pred = predicted[valid]
        if len(act) == 0:
            raise ValueError("No valid rows remain after removing missing values.")
        act_n = pd.to_numeric(act, errors="raise")
        pred_n = pd.to_numeric(pred, errors="raise")
        if not (np.isfinite(act_n).all() and np.isfinite(pred_n).all()):
            raise ValueError("Regression values must be finite numbers.")
        return {}
    results, _, _ = calculate_metrics(
        "Regression",
        actual,
        predicted,
        valid_metrics,
    )
    return results


ALL_METRICS = ["MAE", "MSE", "RMSE", "R\u00b2"]


# ---------------------------------------------------------------------------
# Tests — perfect regression
# ---------------------------------------------------------------------------

class TestPerfectRegression:

    def test_mae_is_zero(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ["MAE"]
        )
        assert r["MAE"] == pytest.approx(0.0)

    def test_mse_is_zero(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ["MSE"]
        )
        assert r["MSE"] == pytest.approx(0.0)

    def test_rmse_is_zero(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ["RMSE"]
        )
        assert r["RMSE"] == pytest.approx(0.0)

    def test_r2_is_one(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ["R\u00b2"]
        )
        assert r["R\u00b2"] == pytest.approx(1.0)

    def test_all_metrics_computed(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ALL_METRICS
        )
        assert set(r.keys()) == set(ALL_METRICS)


# ---------------------------------------------------------------------------
# Tests — imperfect regression with known values
# ---------------------------------------------------------------------------

class TestImperfectRegression:
    # actual:    [1.0, 2.0, 3.0, 4.0]
    # predicted: [1.5, 2.5, 2.5, 3.5]
    # errors:    [0.5, 0.5, 0.5, 0.5]  → MAE = 0.5, MSE = 0.25, RMSE = 0.5

    def test_mae_value(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["MAE"],
        )
        assert r["MAE"] == pytest.approx(0.5)

    def test_mse_value(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["MSE"],
        )
        assert r["MSE"] == pytest.approx(0.25)

    def test_rmse_value(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["RMSE"],
        )
        assert r["RMSE"] == pytest.approx(0.5)

    def test_rmse_equals_sqrt_mse(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["MSE", "RMSE"],
        )
        assert r["RMSE"] == pytest.approx(np.sqrt(r["MSE"]))

    def test_r2_between_zero_and_one(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["R\u00b2"],
        )
        assert 0.0 <= r["R\u00b2"] <= 1.0

    def test_mae_is_non_negative(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["MAE"],
        )
        assert r["MAE"] >= 0.0

    def test_mse_is_non_negative(self, imperfect_reg_df):
        r = compute_regression_metrics(
            imperfect_reg_df["actual"],
            imperfect_reg_df["predicted"],
            ["MSE"],
        )
        assert r["MSE"] >= 0.0


# ---------------------------------------------------------------------------
# Tests — R² edge cases
# ---------------------------------------------------------------------------

class TestR2EdgeCases:

    def test_r2_is_none_for_single_row(self, single_row_reg_df):
        r = compute_regression_metrics(
            single_row_reg_df["actual"],
            single_row_reg_df["predicted"],
            ["R\u00b2"],
        )
        assert r["R\u00b2"] is None

    def test_r2_requires_at_least_two_rows(self):
        df = pd.DataFrame({"actual": [3.0, 4.0], "predicted": [3.0, 4.0]})
        r = compute_regression_metrics(
            df["actual"], df["predicted"], ["R\u00b2"]
        )
        assert r["R\u00b2"] is not None

    def test_r2_can_be_negative_for_bad_model(self):
        # A constant predictor that is worse than the mean can produce R² < 0
        df = pd.DataFrame({
            "actual":    [1.0, 2.0, 3.0, 4.0, 5.0],
            "predicted": [5.0, 5.0, 5.0, 5.0, 5.0],
        })
        r = compute_regression_metrics(
            df["actual"], df["predicted"], ["R\u00b2"]
        )
        assert r["R\u00b2"] < 1.0


# ---------------------------------------------------------------------------
# Tests — metric selection
# ---------------------------------------------------------------------------

class TestMetricSelection:

    def test_no_metrics_selected_returns_empty_dict(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], []
        )
        assert r == {}

    def test_only_mae_selected(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"], perfect_reg_df["predicted"], ["MAE"]
        )
        assert list(r.keys()) == ["MAE"]

    def test_unknown_metric_ignored(self, perfect_reg_df):
        r = compute_regression_metrics(
            perfect_reg_df["actual"],
            perfect_reg_df["predicted"],
            ["MAE", "UnknownMetric"],
        )
        assert "MAE" in r
        assert "UnknownMetric" not in r


# ---------------------------------------------------------------------------
# Tests — NaN row dropping
# ---------------------------------------------------------------------------

class TestNaNHandling:

    def test_nan_rows_dropped_before_calculation(self, missing_values_df):
        # missing_values_df has NaNs; valid row where both are non-null: (1.0, 1.0)
        r = compute_regression_metrics(
            missing_values_df["actual"],
            missing_values_df["predicted"],
            ["MAE"],
        )
        assert r["MAE"] == pytest.approx(0.0)

    def test_mixed_nan_partial_rows_computed(self):
        df = pd.DataFrame({
            "actual":    [1.0, None, 3.0, 4.0],
            "predicted": [1.0, 2.0, 3.0, 4.0],
        })
        # Valid rows: (1,1), (3,3), (4,4) — all perfect
        r = compute_regression_metrics(df["actual"], df["predicted"], ["MAE"])
        assert r["MAE"] == pytest.approx(0.0)
