"""Integration tests for the Streamlit application interface."""
from __future__ import annotations

from streamlit.testing.v1 import AppTest


def test_app_initial_render():
    """Verify that the application launches cleanly with headers and empty history."""
    at = AppTest.from_file("app.py")
    at.run()
    assert len(at.title) == 1
    assert "Web-Based ML Model Evaluator" in at.title[0].value
    assert not at.exception
    # Verify empty history caption
    assert any("appear here" in c.value for c in at.caption)


def test_app_session_history_completed_run_render():
    """Verify that completed evaluation runs appear in sidebar and history table."""
    at = AppTest.from_file("app.py")
    at.session_state["run_history"] = [
        {
            "run_id": "test-run-12345678",
            "timestamp": "2026-11-03T10:00:00Z",
            "status": "completed",
            "source_file": "sample_data/classification_sample.csv",
            "task_type": "Classification",
            "actual_column": "terrain_actual",
            "predicted_column": "terrain_predicted",
            "sample_count": 15,
            "average": "weighted",
            "results": {"Accuracy": 0.8667, "F1-score": 0.8667},
            "error_message": None,
        }
    ]
    at.run()
    assert not at.exception
    assert len(at.dataframe) >= 1
    # Check that sidebar lists the run
    sidebar_texts = [w.value for w in at.sidebar.markdown]
    assert any("Completed" in t and "Classification" in t for t in sidebar_texts)


def test_app_session_history_failed_run_render():
    """Verify that failed runs are retained in history with error details."""
    at = AppTest.from_file("app.py")
    at.session_state["run_history"] = [
        {
            "run_id": "failed-run-99999999",
            "timestamp": "2026-11-03T10:05:00Z",
            "status": "failed",
            "source_file": "corrupt.csv",
            "task_type": "Regression",
            "actual_column": "target",
            "predicted_column": "prediction",
            "sample_count": 0,
            "average": "weighted",
            "results": {},
            "error_message": "Regression requires numeric actual and predicted values.",
        }
    ]
    at.run()
    assert not at.exception
    assert len(at.dataframe) >= 1
    sidebar_texts = [w.value for w in at.sidebar.markdown]
    assert any("Failed" in t for t in sidebar_texts)


def test_app_clear_history_action():
    """Verify that clicking clear run history empties session state."""
    at = AppTest.from_file("app.py")
    at.session_state["run_history"] = [
        {
            "run_id": "run-to-clear",
            "timestamp": "2026-11-03T10:10:00Z",
            "status": "completed",
            "source_file": "test.csv",
            "task_type": "Regression",
            "actual_column": "a",
            "predicted_column": "b",
            "sample_count": 5,
            "average": "weighted",
            "results": {"MAE": 0.1},
            "error_message": None,
        }
    ]
    at.run()
    assert len(at.session_state["run_history"]) == 1
    # Locate clear button in sidebar and click
    clear_buttons = [b for b in at.sidebar.button if "Clear" in b.label]
    assert len(clear_buttons) == 1
    clear_buttons[0].click()
    at.run()
    assert len(at.session_state["run_history"]) == 0
