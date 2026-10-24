"""CSV upload and dataset validation helpers."""
from __future__ import annotations

import csv
import io
from pathlib import Path

import pandas as pd

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_file_size(file_size: int) -> str | None:
    if file_size > MAX_FILE_SIZE:
        return "File is too large. Maximum allowed size is 10 MB."
    return None


def _duplicates(header: list[str]) -> list[str]:
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
    """Validate upload metadata and raw headers before loading the full table."""
    if Path(filename).suffix.lower() != ".csv":
        return None, "Unsupported file format. Only .csv files are supported."
    accepted_types = {
        "text/csv", "application/csv", "application/vnd.ms-excel",
        "text/plain", "application/octet-stream",
        "text/comma-separated-values", "application/x-csv", "text/x-csv",
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
        duplicates = _duplicates(header)
        if duplicates:
            return None, f"Duplicate column names found: {duplicates}. Rename them and retry."
        df = pd.read_csv(io.BytesIO(raw))
        df.columns = [str(c).strip() for c in df.columns]
    except (pd.errors.ParserError, pd.errors.EmptyDataError, UnicodeDecodeError, csv.Error):
        return None, "Invalid CSV format. Please upload a valid CSV."
    except Exception:
        return None, "Unable to read this file."

    error = validate_dataframe(df)
    if error:
        return None, error
    return df, None


def validate_dataframe(df: pd.DataFrame) -> str | None:
    if df.empty or len(df.columns) < 2:
        return "Upload a non-empty CSV with at least two columns."
    if df.columns.duplicated().any():
        duplicates = list(dict.fromkeys(str(name) for name in df.columns[df.columns.duplicated()]))
        return f"Duplicate column names found: {duplicates}. Rename them and retry."
    blank = [
        str(name) for name in df.columns
        if not str(name).strip() or str(name).startswith("Unnamed:")
    ]
    if blank:
        return f"Blank or unnamed columns found: {blank}"
    return None
