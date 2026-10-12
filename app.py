```python
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ML Model Evaluator",
    page_icon="📊",
    layout="wide"
)

st.title("Web-Based ML Model Evaluator")
st.write("Upload a CSV dataset to validate its structure.")

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

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

            # Validate dataset structure
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

                st.subheader("Required column validation")

                # Check column names
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

                # Check duplicate column names
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

                # Select target column
                target_column = st.selectbox(
                    "Select the target column",
                    options=list(df.columns)
                )

                if target_column:
                    missing_targets = int(
                        df[target_column].isnull().sum()
                    )

                    st.write(f"Selected target: **{target_column}**")

                    if missing_targets > 0:
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
                            "two distinct non-missing values. "
                            "Check whether it is suitable for evaluation."
                        )

        except (pd.errors.ParserError, UnicodeDecodeError):
            st.error(
                "Could not read this CSV. Check that the file "
                "contains valid CSV data."
            )

        except Exception:
            st.error(
                "An unexpected error occurred while processing "
                "the file. Check its format and try again."
            )
```
