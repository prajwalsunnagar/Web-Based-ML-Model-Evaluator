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


def parse_uploaded_csv(filename: str, raw: bytes) -> tuple[pd.DataFrame | None, str | None]:
    """Validate the extension and raw header, then parse and validate the table."""
    if Path(filename).suffix.lower() != ".csv":
        return None, "Unsupported file format. Only .csv files are supported."
    size_error = validate_file_size(len(raw))
    if size_error:
        return None, size_error
    try:
        text = raw.decode("utf-8-sig")
        header = next(csv.reader(io.StringIO(text)), [])
        if len(header) != len(set(header)):
            return None, "Duplicate column names found. Rename them and retry."
        df = pd.read_csv(io.BytesIO(raw))
    except (pd.errors.ParserError, UnicodeDecodeError, csv.Error):
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
        return "Duplicate column names found. Rename them and retry."
    blank = [str(c) for c in df.columns if not str(c).strip() or str(c).startswith("Unnamed:")]
    if blank:
        return f"Blank or unnamed columns found: {blank}"
    return None
