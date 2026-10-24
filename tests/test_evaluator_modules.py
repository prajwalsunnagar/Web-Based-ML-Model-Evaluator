"""Tests for the evaluator modules used by the Streamlit app."""
from __future__ import annotations

import pandas as pd
import pytest

from evaluator.engine import EvaluationRun
from evaluator.metrics import calculate_metrics, regression_residual_summary
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


@pytest.mark.parametrize(
    "mime",
    [
        "text/csv",
        "application/csv",
        "application/vnd.ms-excel",
        "text/plain",
        "application/octet-stream",
        "text/comma-separated-values",
        "application/x-csv",
        "text/x-csv",
    ],
)
def test_csv_upload_accepts_standard_mime_types(mime):
    frame, error = parse_uploaded_csv("rows.csv", b"a,b\n1,2\n", mime)
    assert error is None
    assert frame is not None
    assert len(frame) == 1


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


def test_residual_summary_reports_mean_minimum_and_maximum_error():
    summary = regression_residual_summary(
        pd.Series([1.0, 2.0, 3.0]), pd.Series([1.5, 2.5, 2.0])
    )
    assert summary["Mean Error"] == pytest.approx(0.0)
    assert summary["Minimum Error"] == pytest.approx(-0.5)
    assert summary["Maximum Error"] == pytest.approx(1.0)


def test_mismatched_sequence_lengths_raise_value_error():
    actual = pd.Series([1, 2, 3])
    predicted = pd.Series([1, 2])
    with pytest.raises(ValueError, match="same length"):
        calculate_metrics("Classification", actual, predicted, ["Accuracy"])

    with pytest.raises(ValueError, match="same length"):
        regression_residual_summary(actual, predicted)


def test_classification_sample_file_e2e_evaluation():
    with open("sample_data/classification_sample.csv", "rb") as f:
        content = f.read()
    df, err = parse_uploaded_csv("classification_sample.csv", content)
    assert err is None
    assert df is not None
    assert len(df) == 15

    run = EvaluationRun(
        source_file="classification_sample.csv",
        task_type="Classification",
        actual_column="terrain_actual",
        predicted_column="terrain_predicted",
        selected_metrics=["Accuracy", "Precision", "Recall", "F1-score"],
        average="weighted",
    )
    run.execute(df["terrain_actual"], df["terrain_predicted"])
    assert run.status == "completed"
    assert run.sample_count == 15
    assert run.results["Accuracy"] == pytest.approx(13 / 15, abs=1e-4)
    assert run.confusion_matrix is not None
    assert len(run.confusion_matrix) == 4


def test_regression_sample_file_e2e_evaluation():
    with open("sample_data/regression_sample.csv", "rb") as f:
        content = f.read()
    df, err = parse_uploaded_csv("regression_sample.csv", content)
    assert err is None
    assert df is not None
    assert len(df) == 10

    run = EvaluationRun(
        source_file="regression_sample.csv",
        task_type="Regression",
        actual_column="elevation_actual",
        predicted_column="elevation_predicted",
        selected_metrics=["MAE", "MSE", "RMSE", "R²"],
    )
    run.execute(df["elevation_actual"], df["elevation_predicted"])
    assert run.status == "completed"
    assert run.sample_count == 10
    assert run.results["MAE"] is not None
    assert run.results["R²"] is not None
    residuals = regression_residual_summary(df["elevation_actual"], df["elevation_predicted"])
    assert "Mean Error" in residuals


def test_repeatability_and_determinism():
    actual = pd.Series([10.0, 20.0, 30.0, 40.0])
    predicted = pd.Series([10.5, 19.5, 30.2, 39.8])
    first_res, _, _ = calculate_metrics("Regression", actual, predicted, ["MAE", "MSE", "RMSE", "R²"])
    for _ in range(5):
        repeat_res, _, _ = calculate_metrics("Regression", actual, predicted, ["MAE", "MSE", "RMSE", "R²"])
        for k in first_res:
            assert abs(first_res[k] - repeat_res[k]) < 1e-6


def test_safe_error_response_no_traceback_leakage():
    run = EvaluationRun("corrupt.csv", "Regression", "actual", "predicted", ["MAE"])
    # Pass arbitrary object that causes failure
    run.execute(pd.Series(["invalid_str", "not_num"]), pd.Series([1.0, 2.0]))
    assert run.status == "failed"
    assert run.error_message is not None
    assert "Traceback" not in run.error_message
    assert "/" not in run.error_message
