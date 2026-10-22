# Sprint 1 Demo Narration Script & Recording Checklist

**Project:** Web-Based ML Model Evaluator  
**Sprint Window:** 19–23 October 2026  
**Target Duration:** 60 Seconds (1 minute)  
**Deliverable File:** `docs/demo/sprint-1-demo.mp4`  

---

## 1. Recording Checklist

### Pre-Recording Setup
- [x] Environment configured with dependencies (`streamlit`, `pandas`, `numpy`, `scikit-learn`, `pytest`).
- [x] Automated test suite verified: 92 passing tests in pytest.
- [x] Flake8 lint checks passing with zero warnings.
- [x] Streamlit app running locally via `streamlit run app.py --server.headless=true`.
- [x] Example datasets prepared in `sample_data/`:
  - `sample_data/classification_sample.csv` (15 rows, 4 classes)
  - `sample_data/regression_sample.csv` (10 rows, numeric targets)

### Recording Execution Checklist
- [x] **Scene 1 (0:00–0:10):** Welcome & Header overview.
- [x] **Scene 2 (0:10–0:25):** Upload `sample_data/classification_sample.csv` and show instant size & schema validation badge, dataset dimensions (15 rows, 4 columns, 0 missing).
- [x] **Scene 3 (0:25–0:38):** Column configuration (`terrain_actual` vs `terrain_predicted`) and metric selection (`Accuracy`, `Precision`, `Recall`, `F1-score`) with weighted averaging.
- [x] **Scene 4 (0:38–0:50):** Execute evaluation. Display real-time KPI metric cards (Accuracy 0.8667), results table, and multiclass confusion matrix.
- [x] **Scene 5 (0:50–1:00):** Validation / error handling demonstration: select identical columns (`terrain_actual` for both) to trigger immediate actionable validation error guard. Wrap up Sprint 1 demonstration.

---

## 2. Timed Narration Script

### [0:00 – 0:10] Introduction
> *"Hello! This is the Sprint 1 demonstration for the Web-Based ML Model Evaluator, developed by our team for the Software Engineering project. The application allows data scientists and engineers to upload model predictions and compute deterministic evaluation metrics through an intuitive web interface."*

### [0:10 – 0:25] Dataset Ingestion & Validation
> *"We begin by uploading our sample dataset: `classification_sample.csv`. The file size and MIME type are verified immediately against our 10 MB limit. Once validated, the system renders a clean preview of the first ten records alongside summary metrics: 15 rows, 4 columns, and zero missing values."*

### [0:25 – 0:38] Configuration & Metric Selection
> *"Under the Evaluation Configuration section, we confirm the task is Classification. We map the ground-truth column to `terrain_actual` and the prediction column to `terrain_predicted`. We select our evaluation metrics: Accuracy, Precision, Recall, and F1-score with weighted averaging."*

### [0:38 – 0:50] Execution & Results Display
> *"Clicking 'Calculate evaluation metrics' generates a unique evaluation run ID and executes the core engine. Prominent KPI metric cards display our accuracy of 86.67%, along with precision, recall, and F1 scores. Below, a complete 4-by-4 confusion matrix breaks down true versus predicted labels."*

### [0:50 – 1:00] Validation Guard & Conclusion
> *"Finally, to verify validation error handling, selecting identical columns triggers an immediate error banner: 'Actual and predicted columns must be different'. All 92 automated tests pass in our CI workflow, concluding our Sprint 1 deliverables."*
