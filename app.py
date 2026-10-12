```python
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ML Model Evaluator",
    page_icon="📊",
    layout="wide"
)

st.title("Web-Based ML Model Evaluator")
st.write("Upload a CSV dataset to validate its structure and configure evaluation.")

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

CLASSIFICATION_METRICS = [
    "Accuracy",
    "Precision",
    "Recall",
    "F1-score"
]

REGRESSION_METRICS = [
    "MAE",
    "MSE",
    "RMSE",
    "R²"
]

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv"]
)

if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File is too large. Maximum allowed size is 10 MB.")

    else:
        try:
            df = pd.read_csv(uploaded_file)

            if df.empty:
                st.error("The uploaded CSV is empty.")

            elif len(df.columns) == 0:
                st.error("The dataset has no columns.")

            else:
                st.success("CSV uploaded successfully!")

                st.subheader("Dataset preview")
                st.dataframe(df.head(10), use_container_width=True)

                st.subheader("Dataset information")

                col1, col2, col3 = st.columns(3)
                col1.metric("Rows", len(df))
                col2.metric("Columns", len(df.columns))
                col3.metric(
                    "Missing values",
                    int(df.isnull().sum().sum())
                )

                st.subheader("Column validation")

                blank_columns = [
                    str(column)
                    for column in df.columns
                    if str(column).strip() == ""
                    or str(column).startswith("Unnamed:")
                ]

                if blank_columns:
                    st.warning(
                        f"Check these blank or unnamed columns: "
                        f"{blank_columns}"
                    )

                duplicate_columns = df.columns[
                    df.columns.duplicated()
                ].tolist()

                if duplicate_columns:
                    st.error(
                        f"Duplicate column names found: "
                        f"{duplicate_columns}"
                    )
                else:
                    st.success("Column names are unique.")

                target_column = st.selectbox(
                    "Select the target column",
                    options=list(df.columns)
                )

                if target_column:
                    missing_targets = int(
                        df[target_column].isnull().sum()
                    )

                    st.write(f"Selected target: **{target_column}**")

                    if missing_targets:
                        st.warning(
                            f"The target column contains "
                            f"{missing_targets} missing values."
                        )
                    else:
                        st.success(
                            "The selected target column has no "
                            "missing values."
                        )

                    if df[target_column].nunique(dropna=True) < 2:
                        st.warning(
                            "The target column has fewer than "
                            "two distinct non-missing values."
                        )

                st.subheader("Evaluation configuration")

                task_type = st.selectbox(
                    "Select the evaluation task",
                    ["Classification", "Regression"]
                )

                available_metrics = (
                    CLASSIFICATION_METRICS
                    if task_type == "Classification"
                    else REGRESSION_METRICS
                )

                selected_metrics = st.multiselect(
                    "Select evaluation metrics",
                    options=available_metrics,
                    default=[available_metrics[0]]
                )

                if selected_metrics:
                    st.write("### Selected configuration")
                    st.write(f"**Task:** {task_type}")
                    st.write(
                        "**Metrics:** " + ", ".join(selected_metrics)
                    )
                    st.info(
                        "Configuration saved for this session. "
                        "Metric calculation will be added next."
                    )
                else:
                    st.warning("Select at least one evaluation metric.")

        except (pd.errors.ParserError, UnicodeDecodeError):
            st.error(
                "Could not read this CSV. Check that it contains "
                "valid CSV data."
            )

        except Exception:
            st.error(
                "An unexpected error occurred while processing "
                "the file. Check its format and try again."
            )
```
