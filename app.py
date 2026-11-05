
"""Streamlit interface for evaluating paired actual/predicted CSV values."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd
import streamlit as st

from evaluator.engine import EvaluationRun
from evaluator.metrics import (
    CLASSIFICATION_AVERAGES,
    SUPPORTED_METRICS,
    regression_residual_summary,
)
from evaluator.validators import parse_uploaded_csv


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="ML Model Evaluator",
    page_icon="📊",
    layout="wide",
)


# --------------------------------------------------
# LOAD CUSTOM CSS
# --------------------------------------------------

def load_css():
    css_path = Path(__file__).parent / "styles" / "style.css"

    with open(css_path, encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )


load_css()


# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------



# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown(
    '<div class="hero-tag">✦ MACHINE LEARNING ANALYTICS</div>',
    unsafe_allow_html=True,
)

st.title("Model Evaluator.")

st.markdown(
    """
    <p class="hero-description">
        Evaluate, analyze and understand your machine learning
        models with comprehensive performance metrics.
    </p>

    <div class="hero-badges">
        <span>📊 Classification</span>
        <span>📈 Regression</span>
        <span>⚡ Instant Evaluation</span>
    </div>
    """,
    unsafe_allow_html=True,
)



# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "run_history" not in st.session_state:
    st.session_state.run_history = []


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.markdown("## Session run history")

    st.caption("Your recent evaluation activity.")

    if st.session_state.run_history:
        for saved_run in st.session_state.run_history:
            st.write(
                f"{saved_run['status'].title()} · "
                f"{saved_run['task_type']} · "
                f"{saved_run['run_id'][:8]}"
            )

        if st.button("Clear run history", type="secondary"):
            st.session_state.run_history = []
            st.rerun()

    else:
        st.caption(
            "Completed and failed evaluations will appear here."
        )


# --------------------------------------------------
# CSV UPLOAD
# --------------------------------------------------

st.markdown(
    """
    <div class="section-heading">
        <span class="section-icon">⇧</span>
        <span>Upload Dataset</span>
    </div>

    <p class="section-description">
        Upload a CSV file containing actual and predicted values
        to begin your model evaluation.
    </p>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Upload evaluation CSV",
    type=["csv"],
)


# --------------------------------------------------
# DATASET VALIDATION AND OVERVIEW
# --------------------------------------------------

if uploaded_file is not None:

    df, error = parse_uploaded_csv(
        uploaded_file.name,
        uploaded_file.getvalue(),
        uploaded_file.type,
    )

    if error:
        st.error(error)
        st.stop()

    st.success("CSV uploaded and validated.")

    st.markdown(
        """
        <div class="section-heading">
            <span class="section-icon">▦</span>
            <span>Dataset Overview</span>
        </div>

        <p class="section-description">
            Explore your uploaded data before evaluating
            model performance.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # Dataset statistics
    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total Rows", len(df))
    c2.metric("Total Columns", len(df.columns))
    c3.metric("Missing Values", int(df.isnull().sum().sum()))
    c4.metric("Complete Rows", int(df.dropna().shape[0]))

    # Dataset preview
    st.markdown("#### Dataset Preview")

    st.dataframe(
        df.head(10),
        use_container_width=True,
    )


    # --------------------------------------------------
    # EVALUATION CONFIGURATION
    # --------------------------------------------------

    st.markdown("---")

    st.markdown(
        """
        <div class="section-heading">
            <span class="section-icon">⚙</span>
            <span>Evaluation Configuration</span>
        </div>

        <p class="section-description">
            Configure your evaluation task and select
            the metrics you want to calculate.
        </p>
        """,
        unsafe_allow_html=True,
    )

    task_type = st.selectbox(
        "Evaluation task",
        list(SUPPORTED_METRICS),
    )

    col1, col2 = st.columns(2)

    actual_column = col1.selectbox(
        "Actual values column",
        list(df.columns),
        index=0,
    )

    predicted_column = col2.selectbox(
        "Predicted values column",
        list(df.columns),
        index=1,
    )

    selected_metrics = st.multiselect(
        "Select evaluation metrics",
        SUPPORTED_METRICS[task_type],
        default=[SUPPORTED_METRICS[task_type][0]],
    )

    average = "weighted"
    positive_label = None

    # Classification-specific configuration
    if task_type == "Classification":

        classes = list(
            pd.unique(df[actual_column].dropna())
        )

        average_options = list(CLASSIFICATION_AVERAGES)

        if len(classes) != 2:
            average_options.remove("binary")

        average = st.selectbox(
            "Classification averaging",
            average_options,
            index=0,
            help=(
                "Weighted accounts for class frequency; "
                "macro treats classes equally; micro aggregates "
                "decisions; binary scores one selected positive class."
            ),
        )

        if average == "binary" and len(classes) == 2:
            positive_label = st.selectbox(
                "Positive class",
                classes,
            )


    # --------------------------------------------------
    # EVALUATION EXECUTION
    # --------------------------------------------------

    if actual_column == predicted_column:

        st.error(
            "Actual and predicted columns must be different."
        )

    elif not selected_metrics:

        st.warning(
            "Select at least one evaluation metric."
        )

    elif st.button(
        "Calculate Evaluation Metrics",
        type="primary",
        use_container_width=True,
    ):

        run = EvaluationRun(
            source_file=uploaded_file.name,
            task_type=task_type,
            actual_column=actual_column,
            predicted_column=predicted_column,
            selected_metrics=selected_metrics,
            average=average,
            positive_label=positive_label,
        )

        run.execute(
            df[actual_column],
            df[predicted_column],
        )

        run_data = run.to_dict()

        st.session_state.run_history.insert(
            0,
            run_data,
        )

        # Evaluation result
        st.markdown("---")

        if run.status == "failed":

            st.error(
                run.error_message or "Evaluation failed."
            )

        else:

            st.success(
                f"Evaluation completed. Run ID: {run.run_id}"
            )

            st.markdown(
                """
                <div class="section-heading">
                    <span class="section-icon">✦</span>
                    <span>Evaluation Results</span>
                </div>

                <p class="section-description">
                    Performance metrics calculated for your model.
                </p>
                """,
                unsafe_allow_html=True,
            )

            # Metric cards
            metric_cols = st.columns(
                max(1, len(run.results))
            )

            for col, (name, value) in zip(
                metric_cols,
                run.results.items(),
            ):

                col.metric(
                    name,
                    "N/A" if value is None else f"{value:.4f}",
                )

            st.caption(
                f"Evaluated {run.sample_count} valid row(s)."
            )

            # Metrics table
            result_table = run.to_metrics_dataframe()

            st.dataframe(
                result_table,
                hide_index=True,
                use_container_width=True,
            )

            # Classification confusion matrix
            if (
                task_type == "Classification"
                and run.confusion_matrix is not None
            ):

                st.markdown("#### Confusion Matrix")

                matrix = pd.DataFrame(
                    run.confusion_matrix,
                    index=pd.Index(
                        run.confusion_labels,
                        name="Actual",
                    ),
                    columns=pd.Index(
                        run.confusion_labels,
                        name="Predicted",
                    ),
                )

                st.dataframe(
                    matrix,
                    use_container_width=True,
                )

            # Regression residual summary
            elif task_type == "Regression":

                st.markdown(
                    "#### Regression Residual Summary"
                )

                residual_summary = pd.DataFrame(
                    [
                        regression_residual_summary(
                            df[actual_column],
                            df[predicted_column],
                        )
                    ]
                )

                st.dataframe(
                    residual_summary,
                    hide_index=True,
                    use_container_width=True,
                )


# --------------------------------------------------
# RUN HISTORY AND DOWNLOADS
# --------------------------------------------------

if st.session_state.run_history:

    st.markdown("---")

    st.markdown(
        """
        <div class="section-heading">
            <span class="section-icon">◷</span>
            <span>Evaluation Run History</span>
        </div>

        <p class="section-description">
            Review your previous evaluation results and
            download reports.
        </p>
        """,
        unsafe_allow_html=True,
    )

    history_rows = []

    for item in st.session_state.run_history:

        row = {
            "Run ID": item["run_id"],
            "Timestamp (UTC)": item["timestamp"],
            "Status": item["status"],
            "File": item["source_file"],
            "Task": item["task_type"],
            "Actual": item["actual_column"],
            "Predicted": item["predicted_column"],
            "Samples": item["sample_count"],
            "Averaging": item["average"],
        }

        row.update(item["results"])

        if item.get("error_message"):
            row["Error"] = item["error_message"]

        history_rows.append(row)

    st.dataframe(
        pd.DataFrame(history_rows),
        hide_index=True,
        use_container_width=True,
    )

    # Download section
    latest = st.session_state.run_history[0]

    st.markdown("#### Download Reports")

    dl_col1, dl_col2, dl_col3 = st.columns(3)

    dl_col1.download_button(
        "Download Latest Run (JSON)",
        data=json.dumps(
            latest,
            indent=2,
            ensure_ascii=False,
            allow_nan=False,
        ),
        file_name=f"evaluation-{latest['run_id']}.json",
        mime="application/json",
        use_container_width=True,
    )

    if latest.get("results"):

        summary_rows = [
            {
                "Metric": k,
                "Value": "N/A" if v is None else f"{v:.4f}",
            }
            for k, v in latest["results"].items()
        ]

        dl_col2.download_button(
            "Download Metrics Summary (CSV)",
            data=pd.DataFrame(
                summary_rows
            ).to_csv(index=False),
            file_name=(
                f"metrics_summary_{latest['run_id'][:8]}.csv"
            ),
            mime="text/csv",
            use_container_width=True,
        )

    dl_col3.download_button(
        "Download Run History (CSV)",
        data=pd.DataFrame(
            history_rows
        ).to_csv(index=False),
        file_name="evaluation-history.csv",
        mime="text/csv",
        use_container_width=True,
    )
