
"""CSV upload and dataset validation helpers."""
from __future__ import annotations

import csv
import io
from pathlib import Path

import pandas as pd

from evaluator.metrics import SUPPORTED_METRICS

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_metric_compatibility(
    task_type: str, selected_metrics: list[str]
) -> str | None:
    """Validate that selected metrics are compatible with the
    evaluation task."""
    if task_type not in SUPPORTED_METRICS:
        return "Unsupported evaluation task."

    if not selected_metrics:
        return "Select at least one metric."

    if set(selected_metrics) - set(SUPPORTED_METRICS[task_type]):
        return "Selected metrics do not match the evaluation task."

    return None


def validate_file_size(file_size: int) -> str | None:
    """Validate that the uploaded file does not exceed the size limit."""
    if file_size > MAX_FILE_SIZE:
        return "File is too large. Maximum allowed size is 10 MB."
    return None


def _duplicates(header: list[str]) -> list[str]:
    """Identify duplicate column names in a CSV header."""
    seen: set[str] = set()
    duplicates: list[str] = []

    for raw_name in header:
        name = str(raw_name).strip()
        if name in seen and name not in duplicates:
            duplicates.append(name)
        seen.add(name)

    return duplicates


def parse_uploaded_csv(
    filename: str, raw: bytes, mime_type: str | None = None
) -> tuple[pd.DataFrame | None, str | None]:
    """Validate upload metadata and raw headers before loading
the full table."""

    if Path(filename).suffix.lower() != ".csv":
        return None, "Unsupported file format. Only .csv files are supported."

    accepted_types = {
        "text/csv",
        "application/csv",
        "application/vnd.ms-excel",
        "text/plain",
        "application/octet-stream",
        "text/comma-separated-values",
        "application/x-csv",
        "text/x-csv",
    }

    if mime_type and mime_type.lower() not in accepted_types:
        return None, "Unsupported file content type. Please upload a CSV file."

    size_error = validate_file_size(len(raw))
    if size_error:
        return None, size_error

    if not raw or not raw.strip():
        return None, "Uploaded file is empty. Please upload a CSV with data."

    try:
        text = raw.decode("utf-8-sig")
        header = next(csv.reader(io.StringIO(text)), [])

        # Detect duplicate headers before pandas automatically renames them.
        duplicates = _duplicates(header)

        if duplicates:
            return None, (
                f"Duplicate column names found: {duplicates}. "
                "Rename them and retry."
            )

        df = pd.read_csv(io.BytesIO(raw))
        df.columns = [str(column).strip() for column in df.columns]

    except (
        pd.errors.ParserError,
        pd.errors.EmptyDataError,
        UnicodeDecodeError,
        csv.Error,
    ):
        return None, "Invalid CSV format. Please upload a valid CSV."

    except Exception:
        return None, "Unable to read this file."

    error = validate_dataframe(df)
    if error:
        return None, error

    return df, None


def validate_dataframe(df: pd.DataFrame) -> str | None:
    """Validate the basic structure and column names of a dataset."""

    if df.empty or len(df.columns) == 0:
        return "Upload a non-empty CSV with at least two columns."

    if len(df.columns) < 2:
        return "Upload a CSV with at least two columns."

    if df.columns.duplicated().any():
        duplicates = list(
            dict.fromkeys(
                str(name)
                for name in df.columns[df.columns.duplicated()]
            )
        )
        return (
            f"Duplicate column names found: {duplicates}. "
            "Rename them and retry."
        )

    blank = [
        str(name)
        for name in df.columns
        if not str(name).strip()
        or str(name).strip().lower().startswith("unnamed:")
    ]

    if blank:
        return f"Blank or unnamed columns found: {blank}"

    return None


def validate_evaluation_columns(
    df: pd.DataFrame,
    actual_column: str,
    predicted_column: str,
) -> str | None:
    """
    Validate selected ground-truth and prediction columns.

    Checks that both columns exist, are distinct, and contain at least
    one overlapping row with non-empty values.
    """

    if actual_column not in df.columns:
        return f"Ground truth column '{actual_column}' was not found."

    if predicted_column not in df.columns:
        return f"Prediction column '{predicted_column}' was not found."

    if actual_column == predicted_column:
        return "Ground truth and prediction columns must be different."

    actual_values = df[actual_column]
    predicted_values = df[predicted_column]

    # Identify non-empty values in both columns.
    actual_present = actual_values.notna()
    predicted_present = predicted_values.notna()

    # Treat whitespace-only strings as empty values.
    if (
        pd.api.types.is_object_dtype(actual_values)
        or pd.api.types.is_string_dtype(actual_values)
    ):
        actual_present &= (
            actual_values.astype("string").str.strip().ne("")
        )

    if (
        pd.api.types.is_object_dtype(predicted_values)
        or pd.api.types.is_string_dtype(predicted_values)
    ):
        predicted_present &= (
            predicted_values.astype("string").str.strip().ne("")
        )

    # At least one row must contain both actual and predicted values.
    overlapping_rows = actual_present & predicted_present

    if not overlapping_rows.any():
        return (
            "No overlapping non-empty rows found between the ground "
            "truth and prediction columns."
        )

    return None
