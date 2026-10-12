
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ML Model Evaluator",
    page_icon="📊",
    layout="wide"
)

st.title("Web-Based ML Model Evaluator")
st.write("Upload a CSV dataset to validate its structure.")

uploaded_file = st.file_uploader(
    "Upload your dataset",
    type=["csv"]
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

if uploaded_file is not None:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error("File is too large. Maximum allowed size is 10 MB.")
    else:
        try:
            df = pd.read_csv(uploaded_file)

            if df.empty:
                st.error("The uploaded CSV is empty.")
            else:
                st.success("CSV uploaded successfully!")
                st.write("### Dataset preview")
                st.dataframe(df.head(10))

                st.write("### Dataset information")
                col1, col2 = st.columns(2)
                col1.metric("Rows", len(df))
                col2.metric("Columns", len(df.columns))

                st.write("### Required column validation")
                target_column = st.selectbox(
                    "Select the target column",
                    options=list(df.columns)
                )

                if target_column:
                    st.success(
                        f"Target column selected: {target_column}"
                    )

        except Exception as error:
            st.error(f"Could not read the CSV: {error}")
