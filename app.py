
import csv
import io

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

st.set_page_config(
    page_title="ML Model Evaluator",
    page_icon="\U0001f4ca",
    layout="wide",
)

st.title("Web-Based ML Model Evaluator")
st.write("Upload a CSV containing actual and predicted values.")

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

CLASSIFICATION_METRICS = [
    "Accuracy", "Precision", "Recall", "F1-score"
]
REGRESSION_METRICS = ["MAE", "MSE", "RMSE", "R\u00b2"]

uploaded_file = st.file_uploader(
    "Upload evaluation CSV",
    type=["csv"],
)

if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File is too large. Maximum allowed size is 10 MB.")
        st.stop()

    # pandas may silently rename repeated CSV headers (for example,
    # `name,name` becomes `name,name.1`). Inspect the raw header first so
    # the duplicate-column check below can reject the original input.
    try:
        raw_header = next(
            csv.reader(
                io.StringIO(uploaded_file.getvalue().decode("utf-8-sig"))
            ),
            [],
        )
    except UnicodeDecodeError:
        st.error("Invalid CSV format. Please upload a valid CSV.")
        st.stop()

    if len(raw_header) != len(set(raw_header)):
        st.error("Duplicate column names found. Rename them and retry.")
        st.stop()

    uploaded_file.seek(0)

    try:
        df = pd.read_csv(uploaded_file)
    except (pd.errors.ParserError, UnicodeDecodeError):
        st.error("Invalid CSV format. Please upload a valid CSV.")
        st.stop()
    except Exception:
        st.error("Unable to read this file.")
        st.stop()

    if df.empty or len(df.columns) < 2:
        st.error("Upload a non-empty CSV with at least two columns.")
        st.stop()

    if df.columns.duplicated().any():
        st.error("Duplicate column names found. Rename them and retry.")
        st.stop()

    blank_columns = [
        str(c) for c in df.columns
        if not str(c).strip() or str(c).startswith("Unnamed:")
    ]
    if blank_columns:
        st.error(f"Blank or unnamed columns found: {blank_columns}")
        st.stop()

    st.success("CSV uploaded successfully!")

    st.subheader("Dataset preview")
    st.dataframe(df.head(10), use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", len(df))
    col2.metric("Columns", len(df.columns))
    col3.metric("Missing values", int(df.isnull().sum().sum()))

    st.subheader("Evaluation configuration")

    task_type = st.selectbox(
        "Evaluation task",
        ["Classification", "Regression"],
    )

    actual_column = st.selectbox(
        "Actual values column",
        options=list(df.columns),
        index=0,
    )

    predicted_column = st.selectbox(
        "Predicted values column",
        options=list(df.columns),
        index=1,
    )

    available_metrics = (
        CLASSIFICATION_METRICS
        if task_type == "Classification"
        else REGRESSION_METRICS
    )

    selected_metrics = st.multiselect(
        "Select metrics",
        options=available_metrics,
        default=[available_metrics[0]],
    )

    if actual_column == predicted_column:
        st.error("Actual and predicted columns must be different.")

    elif not selected_metrics:
        st.warning("Select at least one metric.")

    else:
        st.write(f"**Task:** {task_type}")
        st.write(f"**Metrics:** {', '.join(selected_metrics)}")

        if st.button("Calculate evaluation metrics"):
            actual = df[actual_column]
            predicted = df[predicted_column]

            # Remove rows where either value is missing.
            valid_rows = actual.notna() & predicted.notna()
            actual = actual[valid_rows]
            predicted = predicted[valid_rows]

            if len(actual) == 0:
                st.error("No valid rows remain after removing missing values.")

            elif task_type == "Classification":
                if actual.nunique() < 2:
                    st.error(
                        "Classification evaluation requires at least "
                        "two distinct actual classes."
                    )
                else:
                    try:
                        results = {}

                        if "Accuracy" in selected_metrics:
                            results["Accuracy"] = accuracy_score(
                                actual, predicted
                            )

                        if "Precision" in selected_metrics:
                            results["Precision"] = precision_score(
                                actual, predicted,
                                average="weighted",
                                zero_division=0,
                            )

                        if "Recall" in selected_metrics:
                            results["Recall"] = recall_score(
                                actual, predicted,
                                average="weighted",
                                zero_division=0,
                            )

                        if "F1-score" in selected_metrics:
                            results["F1-score"] = f1_score(
                                actual, predicted,
                                average="weighted",
                                zero_division=0,
                            )

                        st.subheader("Evaluation results")
                        for metric, value in results.items():
                            st.metric(metric, f"{value:.4f}")

                    except Exception:
                        st.error(
                            "Classification evaluation failed. "
                            "Check that actual and predicted values "
                            "use compatible labels."
                        )

            else:
                try:
                    actual_numeric = pd.to_numeric(actual, errors="raise")
                    predicted_numeric = pd.to_numeric(
                        predicted, errors="raise"
                    )

                    if not (
                        np.isfinite(actual_numeric).all()
                        and np.isfinite(predicted_numeric).all()
                    ):
                        st.error(
                            "Regression values must be finite numbers."
                        )
                    else:
                        results = {}

                        if "MAE" in selected_metrics:
                            results["MAE"] = mean_absolute_error(
                                actual_numeric, predicted_numeric
                            )

                        if "MSE" in selected_metrics:
                            results["MSE"] = mean_squared_error(
                                actual_numeric, predicted_numeric
                            )

                        if "RMSE" in selected_metrics:
                            results["RMSE"] = np.sqrt(
                                mean_squared_error(
                                    actual_numeric, predicted_numeric
                                )
                            )

                        if "R\u00b2" in selected_metrics:
                            results["R\u00b2"] = (
                                r2_score(actual_numeric, predicted_numeric)
                                if len(actual_numeric) >= 2
                                else None
                            )

                        st.subheader("Evaluation results")
                        for metric, value in results.items():
                            if value is None:
                                st.warning(
                                    "R\u00b2 requires at least two valid rows."
                                )
                            else:
                                st.metric(metric, f"{value:.4f}")

                except (ValueError, TypeError):
                    st.error(
                        "Regression requires numeric actual and "
                        "predicted values."
                    )
                except Exception:
                    st.error("Regression evaluation failed.")
