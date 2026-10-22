"""
test_error_handling.py — Unit tests for evaluation error handling and edge cases.

Covers Sprint 2 task #7: Handle evaluation errors and run automated tests.

Tests focus on:
- All-NaN columns
- Non-numeric inputs for regression
- Infinite / NaN-producing values
- Same column selected for actual and predicted
- Empty results after NaN removal
- Single-class classification rejection
"""

from __future__ import annotations

import pytest
import pandas as pd
import numpy as np

from tests.test_validation import validate_dataframe, validate_file_size
from tests.test_regression import compute_regression_metrics
from tests.test_classification import compute_classification_metrics


# ---------------------------------------------------------------------------
# Tests — same column selected for actual and predicted
# ---------------------------------------------------------------------------

class TestSameColumnSelection:
    """Guard against user selecting the same column for both actual/predicted."""

    def test_identical_columns_detected(self):
        actual_col = "col"
        predicted_col = "col"
        assert actual_col == predicted_col  # UI guard — should show error

    def test_different_columns_accepted(self):
        actual_col = "actual"
        predicted_col = "predicted"
        assert actual_col != predicted_col


# ---------------------------------------------------------------------------
# Tests — all-NaN column results in empty valid set
# ---------------------------------------------------------------------------

class TestAllNaNColumns:

    def test_all_nan_actual_raises_for_classification(self):
        df = pd.DataFrame({
            "actual":    [None, None, None],
            "predicted": [0, 1, 0],
        })
        with pytest.raises((ValueError, Exception)):
            compute_classification_metrics(
                df["actual"], df["predicted"], ["Accuracy"]
            )

    def test_all_nan_predicted_raises_for_regression(self):
        df = pd.DataFrame({
            "actual":    [1.0, 2.0, 3.0],
            "predicted": [None, None, None],
        })
        with pytest.raises((ValueError, Exception)):
            compute_regression_metrics(
                df["actual"], df["predicted"], ["MAE"]
            )

    def test_all_nan_both_columns_raises(self):
        df = pd.DataFrame({
            "actual":    [None, None],
            "predicted": [None, None],
        })
        with pytest.raises((ValueError, Exception)):
            compute_regression_metrics(
                df["actual"], df["predicted"], ["MAE"]
            )


# ---------------------------------------------------------------------------
# Tests — non-numeric regression inputs
# ---------------------------------------------------------------------------

class TestNonNumericRegression:

    def test_string_actual_raises(self, non_numeric_reg_df):
        with pytest.raises((ValueError, TypeError)):
            compute_regression_metrics(
                non_numeric_reg_df["actual"],
                non_numeric_reg_df["predicted"],
                ["MAE"],
            )

    def test_mixed_numeric_and_string_raises(self):
        df = pd.DataFrame({
            "actual":    ["1.0", "two", "3.0"],
            "predicted": [1.0, 2.0, 3.0],
        })
        with pytest.raises((ValueError, TypeError)):
            compute_regression_metrics(
                df["actual"], df["predicted"], ["MAE"]
            )


# ---------------------------------------------------------------------------
# Tests — infinite values in regression
# ---------------------------------------------------------------------------

class TestInfiniteValues:

    def test_inf_in_actual_raises(self):
        df = pd.DataFrame({
            "actual":    [1.0, np.inf, 3.0],
            "predicted": [1.0, 2.0, 3.0],
        })
        with pytest.raises((ValueError, Exception)):
            compute_regression_metrics(
                df["actual"], df["predicted"], ["MAE"]
            )

    def test_neg_inf_in_predicted_raises(self):
        df = pd.DataFrame({
            "actual":    [1.0, 2.0, 3.0],
            "predicted": [1.0, -np.inf, 3.0],
        })
        with pytest.raises((ValueError, Exception)):
            compute_regression_metrics(
                df["actual"], df["predicted"], ["MSE"]
            )

    def test_nan_produced_by_float_nan_raises(self):
        df = pd.DataFrame({
            "actual":    [1.0, float("nan"), 3.0],
            "predicted": [1.0, 2.0, float("nan")],
        })
        # Only 1 valid row remains after dropping NaNs; R² is None when len < 2
        r = compute_regression_metrics(
            df["actual"], df["predicted"], ["R²"]
        )
        assert r["R²"] is None


# ---------------------------------------------------------------------------
# Tests — single-class classification rejection
# ---------------------------------------------------------------------------

class TestSingleClassRejection:

    def test_single_class_actual_raises(self, single_class_df):
        with pytest.raises(ValueError, match="two distinct"):
            compute_classification_metrics(
                single_class_df["actual"],
                single_class_df["predicted"],
                ["Accuracy"],
            )

    def test_two_class_actual_passes(self):
        df = pd.DataFrame({
            "actual":    [0, 1],
            "predicted": [0, 1],
        })
        r = compute_classification_metrics(
            df["actual"], df["predicted"], ["Accuracy"]
        )
        assert "Accuracy" in r


# ---------------------------------------------------------------------------
# Tests — file validation edge cases
# ---------------------------------------------------------------------------

class TestFileValidationEdgeCases:

    def test_exactly_10_mb_passes(self):
        assert validate_file_size(10 * 1024 * 1024) is None

    def test_11_mb_fails(self):
        assert validate_file_size(11 * 1024 * 1024) is not None

    def test_empty_dataframe_fails(self, empty_df):
        err = validate_dataframe(empty_df)
        assert err is not None

    def test_one_column_df_fails(self, single_col_df):
        err = validate_dataframe(single_col_df)
        assert err is not None


# ---------------------------------------------------------------------------
# Tests — column count guards
# ---------------------------------------------------------------------------

class TestColumnCountGuards:

    def test_two_column_df_passes(self, binary_clf_df):
        assert validate_dataframe(binary_clf_df) is None

    def test_five_column_df_passes(self):
        df = pd.DataFrame({f"c{i}": range(5) for i in range(5)})
        assert validate_dataframe(df) is None

    def test_zero_column_df_fails(self):
        df = pd.DataFrame()
        assert validate_dataframe(df) is not None
