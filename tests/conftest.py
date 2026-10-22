"""
conftest.py — Shared pytest fixtures for the ML Model Evaluator test suite.
"""

import io
import pytest
import pandas as pd


# ---------------------------------------------------------------------------
# CSV byte-stream helpers
# ---------------------------------------------------------------------------

def _df_to_bytes(df: pd.DataFrame) -> bytes:
    """Serialise a DataFrame to UTF-8 CSV bytes."""
    return df.to_csv(index=False).encode("utf-8")


# ---------------------------------------------------------------------------
# Classification fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def binary_clf_df() -> pd.DataFrame:
    """Perfect binary classification: actual == predicted."""
    return pd.DataFrame({
        "actual":    [0, 1, 0, 1, 0, 1, 0, 1],
        "predicted": [0, 1, 0, 1, 0, 1, 0, 1],
    })


@pytest.fixture()
def imperfect_clf_df() -> pd.DataFrame:
    """Imperfect binary classification with known metrics."""
    return pd.DataFrame({
        "actual":    [0, 0, 1, 1, 0, 1],
        "predicted": [0, 1, 1, 0, 0, 1],
    })


@pytest.fixture()
def multiclass_clf_df() -> pd.DataFrame:
    """Three-class classification dataset."""
    return pd.DataFrame({
        "actual":    ["cat", "dog", "bird", "cat", "dog", "bird"],
        "predicted": ["cat", "dog", "bird", "dog", "dog", "cat"],
    })


@pytest.fixture()
def single_class_df() -> pd.DataFrame:
    """Only one distinct class — should trigger validation error."""
    return pd.DataFrame({
        "actual":    [1, 1, 1, 1],
        "predicted": [1, 1, 0, 0],
    })


# ---------------------------------------------------------------------------
# Regression fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def perfect_reg_df() -> pd.DataFrame:
    """Perfect regression: actual == predicted → MSE/MAE = 0, R² = 1."""
    values = [1.0, 2.0, 3.0, 4.0, 5.0]
    return pd.DataFrame({"actual": values, "predicted": values})


@pytest.fixture()
def imperfect_reg_df() -> pd.DataFrame:
    """Regression dataset with known, manually verifiable errors."""
    return pd.DataFrame({
        "actual":    [1.0, 2.0, 3.0, 4.0],
        "predicted": [1.5, 2.5, 2.5, 3.5],
    })


@pytest.fixture()
def single_row_reg_df() -> pd.DataFrame:
    """Single-row regression — R² is undefined with < 2 samples."""
    return pd.DataFrame({"actual": [5.0], "predicted": [3.0]})


# ---------------------------------------------------------------------------
# Validation / edge-case fixtures
# ---------------------------------------------------------------------------

@pytest.fixture()
def valid_csv_bytes(binary_clf_df) -> bytes:
    return _df_to_bytes(binary_clf_df)


@pytest.fixture()
def missing_values_df() -> pd.DataFrame:
    """DataFrame with NaN in both columns."""
    return pd.DataFrame({
        "actual":    [1.0, None, 3.0, None],
        "predicted": [1.0, 2.0, None, None],
    })


@pytest.fixture()
def non_numeric_reg_df() -> pd.DataFrame:
    """Regression columns containing non-numeric strings."""
    return pd.DataFrame({
        "actual":    ["one", "two", "three"],
        "predicted": [1.0, 2.0, 3.0],
    })


@pytest.fixture()
def duplicate_cols_df() -> pd.DataFrame:
    """Raw CSV bytes with duplicate column names."""
    raw = b"col,col\n1,2\n3,4\n"
    return pd.read_csv(io.BytesIO(raw), header=0)


@pytest.fixture()
def empty_df() -> pd.DataFrame:
    return pd.DataFrame()


@pytest.fixture()
def single_col_df() -> pd.DataFrame:
    return pd.DataFrame({"only_column": [1, 2, 3]})
