"""Streamlit interface for evaluating paired actual/predicted CSV values."""
from __future__ import annotations

import json

import pandas as pd
import streamlit as st

from evaluator.engine import EvaluationRun
from evaluator.metrics import CLASSIFICATION_AVERAGES, SUPPORTED_METRICS
from evaluator.validators import parse_uploaded_csv

st.set_page_config(page_title="ML Model Evaluator", page_icon="📊", layout="wide")
st.title("Web-Based ML Model Evaluator")
st.write("Upload a CSV containing actual and predicted values, then choose metrics to calculate.")

if "run_history" not in st.session_state:
    st.session_state.run_history = []

with st.sidebar:
    st.header("Session run history")
    if st.session_state.run_history:
        for saved_run in st.session_state.run_history:
            st.write(
                f"{saved_run['status'].title()} · {saved_run['task_type']} · "
                f"{saved_run['run_id'][:8]}"
            )
    else:
        st.caption("Completed and failed evaluations will appear here.")

uploaded_file = st.file_uploader("Upload evaluation CSV", type=["csv"])
if uploaded_file is not None:
    df, error = parse_uploaded_csv(
        uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type
    )
    if error:
        st.error(error)
        st.stop()

    st.success("CSV uploaded and validated.")
    st.subheader("Dataset preview")
    st.dataframe(df.head(10), use_container_width=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Rows", len(df))
    c2.metric("Columns", len(df.columns))
    c3.metric("Missing values", int(df.isnull().sum().sum()))

    st.subheader("Evaluation configuration")
    task_type = st.selectbox("Evaluation task", list(SUPPORTED_METRICS))
    col1, col2 = st.columns(2)
    actual_column = col1.selectbox("Actual values column", list(df.columns), index=0)
    predicted_column = col2.selectbox("Predicted values column", list(df.columns), index=1)
    selected_metrics = st.multiselect(
        "Select metrics", SUPPORTED_METRICS[task_type],
        default=[SUPPORTED_METRICS[task_type][0]],
    )

    average = "weighted"
    positive_label = None
    if task_type == "Classification":
        classes = list(pd.unique(df[actual_column].dropna()))
        average_options = list(CLASSIFICATION_AVERAGES)
        if len(classes) != 2:
            average_options.remove("binary")
        average = st.selectbox(
            "Classification averaging", average_options, index=0,
            help="Weighted accounts for class frequency; macro treats classes equally; "
                 "micro aggregates decisions; binary scores one selected positive class.",
        )
        if average == "binary" and len(classes) == 2:
            positive_label = st.selectbox("Positive class", classes)

    if actual_column == predicted_column:
        st.error("Actual and predicted columns must be different.")
    elif not selected_metrics:
        st.warning("Select at least one metric.")
    elif st.button("Calculate evaluation metrics", type="primary"):
        run = EvaluationRun(
            source_file=uploaded_file.name,
            task_type=task_type,
            actual_column=actual_column,
            predicted_column=predicted_column,
            selected_metrics=selected_metrics,
            average=average,
            positive_label=positive_label,
        )
        run.execute(df[actual_column], df[predicted_column])
        run_data = run.to_dict()
        st.session_state.run_history.insert(0, run_data)

        if run.status == "failed":
            st.error(run.error_message or "Evaluation failed.")
        else:
            st.success(f"Evaluation completed. Run ID: {run.run_id}")
            st.subheader("Evaluation results")
            metric_cols = st.columns(max(1, len(run.results)))
            for col, (name, value) in zip(metric_cols, run.results.items()):
                col.metric(name, "N/A" if value is None else f"{value:.4f}")
            st.caption(f"Evaluated {run.sample_count} valid row(s).")
            result_table = pd.DataFrame(
                [{"Metric": name, "Value": value} for name, value in run.results.items()]
            )
            st.dataframe(result_table, hide_index=True, use_container_width=True)

            if task_type == "Classification" and run.confusion_matrix is not None:
                st.subheader("Confusion matrix")
                matrix = pd.DataFrame(
                    run.confusion_matrix,
                    index=pd.Index(run.confusion_labels, name="Actual"),
                    columns=pd.Index(run.confusion_labels, name="Predicted"),
                )
                st.dataframe(matrix, use_container_width=True)
            elif task_type == "Regression":
                st.subheader("Regression residual summary")
                valid = df[actual_column].notna() & df[predicted_column].notna()
                actual = pd.to_numeric(df.loc[valid, actual_column], errors="coerce")
                predicted = pd.to_numeric(df.loc[valid, predicted_column], errors="coerce")
                residuals = actual - predicted
                residual_summary = pd.DataFrame([{
                    "Mean Error": float(residuals.mean()),
                    "Minimum Error": float(residuals.min()),
                    "Maximum Error": float(residuals.max()),
                    "Mean Absolute Error": float(residuals.abs().mean()),
                }])
                st.dataframe(residual_summary, hide_index=True, use_container_width=True)

if st.session_state.run_history:
    st.divider()
    st.subheader("Run history")
    history_rows = []
    for item in st.session_state.run_history:
        row = {
            "Run ID": item["run_id"], "Timestamp (UTC)": item["timestamp"],
            "Status": item["status"], "File": item["source_file"],
            "Task": item["task_type"], "Actual": item["actual_column"],
            "Predicted": item["predicted_column"], "Samples": item["sample_count"],
            "Averaging": item["average"],
        }
        row.update(item["results"])
        if item["error_message"]:
            row["Error"] = item["error_message"]
        history_rows.append(row)
    st.dataframe(pd.DataFrame(history_rows), hide_index=True, use_container_width=True)

    latest = st.session_state.run_history[0]
    st.download_button(
        "Download latest run (JSON)",
        data=json.dumps(latest, indent=2, ensure_ascii=False, allow_nan=False),
        file_name=f"evaluation-{latest['run_id']}.json",
        mime="application/json",
    )
    st.download_button(
        "Download run history (CSV)", data=pd.DataFrame(history_rows).to_csv(index=False),
        file_name="evaluation-history.csv", mime="text/csv",
    )
