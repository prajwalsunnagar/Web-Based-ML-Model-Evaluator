"""Tests for the evaluator modules used by the Streamlit app."""
from __future__ import annotations

import pandas as pd
import pytest

from evaluator.engine import EvaluationRun
from evaluator.metrics import calculate_metrics
from evaluator.validators import MAX_FILE_SIZE, parse_uploaded_csv


def test_upload_validation_rejects_type_and_size_before_parsing():
    _, type_error = parse_uploaded_csv("rows.xlsx", b"not a csv")
    _, size_error = parse_uploaded_csv("rows.csv", b"x" * (MAX_FILE_SIZE + 1))
    assert "Only .csv" in type_error
    assert "10 MB" in size_error


def test_duplicate_header_message_names_duplicate():
    frame, error = parse_uploaded_csv("rows.csv", b"actual,predicted,actual\n1,1,1\n")
    assert frame is None
    assert "actual" in error


def test_csv_upload_rejects_invalid_mime_type():
    frame, error = parse_uploaded_csv("rows.csv", b"a,b\n1,2\n", "application/json")
    assert frame is None
    assert "content type" in error


def test_csv_upload_rejects_header_without_data_rows():
    frame, error = parse_uploaded_csv("rows.csv", b"a,b\n")
    assert frame is None
    assert "non-empty" in error


def test_paired_missing_rows_are_excluded():
    actual = pd.Series([0, 1, None, 1])
    predicted = pd.Series([0, 1, 0, None])
    results, _, count = calculate_metrics("Classification", actual, predicted, ["Accuracy"])
    assert count == 2
    assert results["Accuracy"] == pytest.approx(1.0)


@pytest.mark.parametrize("average", ["weighted", "macro", "micro"])
def test_classification_average_modes_are_available(average):
    actual = pd.Series(["cat", "cat", "cat", "dog"])
    predicted = pd.Series(["cat", "dog", "dog", "dog"])
    results, _, _ = calculate_metrics(
        "Classification", actual, predicted, ["Precision", "Recall", "F1-score"],
        average=average,
    )
    assert set(results) == {"Precision", "Recall", "F1-score"}


def test_binary_average_accepts_string_positive_class():
    actual = pd.Series(["no", "no", "yes", "yes"])
    predicted = pd.Series(["no", "yes", "yes", "no"])
    results, _, _ = calculate_metrics(
        "Classification", actual, predicted, ["Precision"], average="binary",
        positive_label="yes",
    )
    assert results["Precision"] == pytest.approx(0.5)


def test_binary_average_requires_positive_class():
    with pytest.raises(ValueError, match="positive class"):
        calculate_metrics(
            "Classification", pd.Series([0, 1]), pd.Series([0, 1]),
            ["Precision"], average="binary",
        )


def test_regression_metrics_and_row_count():
    results, matrix, count = calculate_metrics(
        "Regression", pd.Series([1.0, 2.0]), pd.Series([1.5, 2.5]),
        ["MAE", "MSE", "RMSE", "R²"],
    )
    assert count == 2
    assert matrix is None
    assert results["MAE"] == pytest.approx(0.5)
    assert results["MSE"] == pytest.approx(0.25)
    assert results["RMSE"] == pytest.approx(0.5)


def test_invalid_metric_task_pair_is_rejected():
    with pytest.raises(ValueError, match="do not match"):
        calculate_metrics(
            "Classification", pd.Series([0, 1]), pd.Series([0, 1]), ["MAE"]
        )


def test_run_records_completed_metadata_and_confusion_matrix():
    run = EvaluationRun("sample.csv", "Classification", "actual", "predicted", ["Accuracy"])
    run.execute(pd.Series([0, 1]), pd.Series([0, 1]))
    exported = run.to_dict()
    assert run.status == "completed"
    assert run.sample_count == 2
    assert run.confusion_matrix == [[1, 0], [0, 1]]
    assert exported["run_id"] and exported["timestamp"]


def test_run_records_failed_status_with_safe_validation_error():
    run = EvaluationRun("sample.csv", "Classification", "actual", "predicted", ["Accuracy"])
    run.execute(pd.Series([1, 1]), pd.Series([1, 1]))
    assert run.status == "failed"
    assert "two distinct actual classes" in run.error_message
