"""
test_classification.py — Unit tests for classification metric calculations.

Covers Sprint 1 task #5: Calculate selected evaluation metrics
(Classification: Accuracy, Precision, Recall, F1-score)
"""

from __future__ import annotations

import pytest
import pandas as pd
from evaluator.metrics import SUPPORTED_METRICS, calculate_metrics


def compute_classification_metrics(
    actual: pd.Series,
    predicted: pd.Series,
    selected_metrics: list[str],
) -> dict[str, float]:
    """Delegate to evaluator.metrics.calculate_metrics."""
    valid_metrics = [m for m in selected_metrics if m in SUPPORTED_METRICS["Classification"]]
    if not valid_metrics:
        valid = actual.notna() & predicted.notna()
        act = actual[valid]
        if len(act) == 0:
            raise ValueError("No valid rows remain after removing missing values.")
        if act.nunique() < 2:
            raise ValueError("Classification evaluation requires at least two distinct actual classes.")
        return {}
    results, _, _ = calculate_metrics(
        "Classification",
        actual,
        predicted,
        valid_metrics,
        average="weighted",
    )
    return results


ALL_METRICS = ["Accuracy", "Precision", "Recall", "F1-score"]


# ---------------------------------------------------------------------------
# Tests — perfect binary classification
# ---------------------------------------------------------------------------

class TestPerfectBinaryClassification:

    def test_accuracy_is_one(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ["Accuracy"]
        )
        assert r["Accuracy"] == pytest.approx(1.0)

    def test_precision_is_one(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ["Precision"]
        )
        assert r["Precision"] == pytest.approx(1.0)

    def test_recall_is_one(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ["Recall"]
        )
        assert r["Recall"] == pytest.approx(1.0)

    def test_f1_is_one(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ["F1-score"]
        )
        assert r["F1-score"] == pytest.approx(1.0)

    def test_all_metrics_computed(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ALL_METRICS
        )
        assert set(r.keys()) == set(ALL_METRICS)

    def test_all_values_are_floats(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ALL_METRICS
        )
        for v in r.values():
            assert isinstance(v, float)


# ---------------------------------------------------------------------------
# Tests — imperfect binary classification
# ---------------------------------------------------------------------------

class TestImperfectBinaryClassification:

    def test_accuracy_is_between_zero_and_one(self, imperfect_clf_df):
        r = compute_classification_metrics(
            imperfect_clf_df["actual"],
            imperfect_clf_df["predicted"],
            ["Accuracy"],
        )
        assert 0.0 <= r["Accuracy"] <= 1.0

    def test_accuracy_value(self, imperfect_clf_df):
        # actual:    [0, 0, 1, 1, 0, 1]
        # predicted: [0, 1, 1, 0, 0, 1]
        # correct: 0✓ 0✗ 1✓ 1✗ 0✓ 1✓ → 4/6
        r = compute_classification_metrics(
            imperfect_clf_df["actual"],
            imperfect_clf_df["predicted"],
            ["Accuracy"],
        )
        assert r["Accuracy"] == pytest.approx(4 / 6)

    def test_precision_is_between_zero_and_one(self, imperfect_clf_df):
        r = compute_classification_metrics(
            imperfect_clf_df["actual"],
            imperfect_clf_df["predicted"],
            ["Precision"],
        )
        assert 0.0 <= r["Precision"] <= 1.0

    def test_f1_less_than_perfect(self, imperfect_clf_df):
        r = compute_classification_metrics(
            imperfect_clf_df["actual"],
            imperfect_clf_df["predicted"],
            ["F1-score"],
        )
        assert r["F1-score"] < 1.0


# ---------------------------------------------------------------------------
# Tests — multiclass classification
# ---------------------------------------------------------------------------

class TestMulticlassClassification:

    def test_multiclass_accuracy_computed(self, multiclass_clf_df):
        r = compute_classification_metrics(
            multiclass_clf_df["actual"],
            multiclass_clf_df["predicted"],
            ["Accuracy"],
        )
        # cat✓ dog✓ bird✓ cat✗ dog✓ bird✗  → 4/6
        assert r["Accuracy"] == pytest.approx(4 / 6)

    def test_all_metrics_work_for_multiclass(self, multiclass_clf_df):
        r = compute_classification_metrics(
            multiclass_clf_df["actual"],
            multiclass_clf_df["predicted"],
            ALL_METRICS,
        )
        assert len(r) == 4

    def test_string_labels_handled(self, multiclass_clf_df):
        r = compute_classification_metrics(
            multiclass_clf_df["actual"],
            multiclass_clf_df["predicted"],
            ["Accuracy"],
        )
        assert isinstance(r["Accuracy"], float)


# ---------------------------------------------------------------------------
# Tests — metric selection
# ---------------------------------------------------------------------------

class TestMetricSelection:

    def test_no_metrics_selected_returns_empty_dict(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], []
        )
        assert r == {}

    def test_single_metric_selected(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"], binary_clf_df["predicted"], ["Recall"]
        )
        assert list(r.keys()) == ["Recall"]

    def test_unknown_metric_name_ignored(self, binary_clf_df):
        r = compute_classification_metrics(
            binary_clf_df["actual"],
            binary_clf_df["predicted"],
            ["Accuracy", "NonExistentMetric"],
        )
        assert "Accuracy" in r
        assert "NonExistentMetric" not in r


# ---------------------------------------------------------------------------
# Tests — NaN handling
# ---------------------------------------------------------------------------

class TestNaNHandling:

    def test_nan_rows_are_dropped_before_calculation(self):
        df = pd.DataFrame({
            "actual":    [0,   1,   None, 1],
            "predicted": [0,   1,   0,    None],
        })
        r = compute_classification_metrics(
            df["actual"], df["predicted"], ["Accuracy"]
        )
        # Only 2 valid rows remain (first two), both correct → accuracy = 1.0
        assert r["Accuracy"] == pytest.approx(1.0)
