# Sprint 2 Demo Narration Script & Final Deliverable Checklist

**Project:** Web-Based ML Model Evaluator  
**Sprint Window:** 26–30 October 2026  
**Target Duration:** Exactly 120 Seconds (2 minutes)  
**Deliverable Scope:** SE Mini-Project Deliverables — Part 2 Final Submission  
**Video Target Location:** `docs/demo_videos/sprint2_demo.mp4`  

---

## 1. Recording Setup & Verification Checklist

### Pre-Recording Setup
- [x] Python environment active with all production and development dependencies (`pip install -r requirements.txt -r requirements-dev.txt`).
- [x] Automated test suite verified locally: 124 passed in ~1.5 seconds (`pytest tests/ -v`).
- [x] Flake8 code linting verified with 0 errors (`flake8 app.py evaluator/ tests/ --max-line-length=120 --exclude=.venv`).
- [x] Bytecode compilation verified with 0 errors (`python -m py_compile app.py evaluator/*.py tests/*.py`).
- [x] Sample datasets available:
  - `sample_data/classification_sample.csv` (15 rows, 4 classes)
  - `sample_data/regression_sample.csv` (10 rows, numeric targets)
- [x] Streamlit web application running at `http://localhost:8501` (`streamlit run app.py`).
- [x] Terminal split or terminal window ready for live test execution demonstration.
- [x] Browser recording set to 1080p, 100% zoom, clean browser window without bookmark bar clutter.

---

## 2. Timed Scene & Narration Script (120 Seconds)

### [0:00 – 0:25] Classification Evaluation & Report Export
**Visual Actions:**
1. Open Streamlit app in browser.
2. Drag and drop `sample_data/classification_sample.csv`.
3. Point out instant upload validation badge and dataset preview with row health metrics (15 rows, 4 columns, 0 missing, 15 complete rows).
4. Configure task: `Classification`, actual column: `terrain_actual`, predicted column: `terrain_predicted`. Metrics: Accuracy, Precision, Recall, F1-score.
5. Click **Calculate evaluation metrics**.
6. Show generated UUID `run_id`, KPI metric cards (Accuracy: 0.8667), and the sorted 4x4 confusion matrix.
7. Scroll down to the export section and click **Download latest run (JSON)** and **Download metrics summary (CSV)**. Show the downloaded files in the browser tray.

**Spoken Narration:**
> *"Welcome to the Sprint 2 demonstration of the Web-Based ML Model Evaluator. We begin with our end-to-end classification workflow. Uploading `classification_sample.csv`, the system immediately validates file size, MIME type, and schema integrity, rendering a dataset preview and health metrics.*
>
> *We configure our evaluation task for Classification, mapping `terrain_actual` against `terrain_predicted` with weighted averaging. Clicking 'Calculate evaluation metrics' generates a unique evaluation UUID, computing KPI cards and an ordered confusion matrix.*
>
> *Sprint 2 introduces comprehensive report exporting: with one click, users can download the full evaluation report as JSON and the metrics summary as CSV for offline analysis."*

---

### [0:25 – 0:55] Regression Evaluation & Residual Metrics
**Visual Actions:**
1. Upload `sample_data/regression_sample.csv`.
2. Select evaluation task: `Regression`.
3. Map actual column: `elevation_actual` and predicted column: `elevation_predicted`.
4. Select all metrics: `MAE`, `MSE`, `RMSE`, `R²`.
5. Click **Calculate evaluation metrics**.
6. Highlight the generated KPI cards (MAE: 0.8200, MSE: 0.9840, RMSE: 0.9920, R²: 0.9996).
7. Scroll to the new **Regression residual summary** table showing: Mean Error, Residual Standard Deviation, Minimum Error, Maximum Error, and Mean Absolute Error.

**Spoken Narration:**
> *"Next, we demonstrate our full regression evaluation workflow. Uploading `regression_sample.csv`, we map `elevation_actual` to `elevation_predicted` and select all four regression metrics: MAE, MSE, RMSE, and R-squared.*
>
> *Upon execution, the engine deterministically computes model error metrics with four decimal precision, confirming near-perfect fit with an R-squared of 0.9996.*
>
> *Sprint 2 adds an in-depth signed residual error summary, reporting mean prediction error, residual standard deviation, minimum error, and maximum error, giving practitioners immediate diagnostic insight into prediction bias and variance."*

---

### [0:55 – 1:20] Invalid Input Handling & Run History
**Visual Actions:**
1. Demonstrate error handling: upload an invalid file (or select same column for actual and predicted).
2. Show immediate, safe validation banner: *"Actual and predicted columns must be different."*
3. Demonstrate non-numeric regression input rejection: show safe actionable error banner without stack trace disclosure.
4. Point out the **Sidebar Session Run History**, displaying all previous runs with status badges (`Completed`, `Failed`), task types, and truncated run IDs.
5. Point out the full history table at the bottom of the page, download **Download run history (CSV)**, and click **Clear run history** to show session state reset.

**Spoken Narration:**
> *"A primary goal of Sprint 2 is error handling robustness and reliability. If invalid inputs, disjoint missing values, non-numeric strings, or identical column mappings are supplied, the application catches the condition gracefully. As seen here, user-friendly banners provide actionable guidance without ever exposing internal stack traces, system paths, or raw server exceptions.*
>
> *All evaluation runs—both completed and failed—are tracked in session history with unique run IDs, timestamps, and execution parameters. Users can download the entire session run history as CSV, or clear the history at any time."*

---

### [1:20 – 1:40] Automated Test Execution
**Visual Actions:**
1. Switch to terminal window.
2. Execute the test command:
   ```bash
   pytest tests/ -v --tb=short --cov=evaluator --cov=app --cov-report=term-missing
   ```
3. Highlight terminal output:
   - 124 tests collected and passed.
   - 0 failures, 0 errors.
   - Total runtime ~1.5 seconds.
   - Core evaluator package coverage >90%.

**Spoken Narration:**
> *"Turning to automated quality assurance: our comprehensive test suite has expanded from 92 to 124 automated unit and integration tests across six test modules, covering upload validation, classification, regression, edge cases, lifecycle states, and Streamlit UI flows.*
>
> *Running pytest live, all 124 tests pass in under 1.5 seconds, satisfying our performance requirement of less than 2 seconds, while achieving over 90% line coverage on our core evaluator business logic. Numerical determinism is verified to within 1e-6 across repeated runs."*

---

### [1:40 – 2:00] GitHub Actions, Documentation & Development Freeze
**Visual Actions:**
1. Switch to GitHub repository in browser.
2. Show GitHub Actions tab with green workflow runs across Python 3.10, 3.11, and 3.12.
3. Show `README.md`, `docs/SPRINT-PLAN.md`, `docs/TEST-EXECUTION-REPORT.md`, `docs/PART2_DELIVERABLE_AUDIT.md`, and `docs/DEVIATIONS-AND-NOTES.md`.
4. Point out the formal development freeze declaration for Part-2 submission.

**Spoken Narration:**
> *"In our continuous integration pipeline, GitHub Actions automatically executes our multi-version matrix across Python 3.10, 3.11, and 3.12 on every push and pull request, enforcing flake8 PEP 8 linting, bytecode compilation, and pytest coverage.*
>
> *All project documentation—including the SRS, SAD, Test Execution Report with full Requirement Traceability Matrix, and Sprint Plan—is fully synchronized.*
>
> *With all Sprint 1 and Sprint 2 backlog items verified and Definition of Done fulfilled, we formally declare development frozen for the Part-2 submission. Thank you!"*

---

## 3. Post-Recording Deliverable Checklist

- [ ] Video recording duration verified: exactly 120 seconds ($\pm 3$ seconds).
- [ ] Audio clarity verified with no background noise or clipping.
- [ ] Export video to H.264 MP4 format with resolution 1080p (1920x1080) at 30 fps.
- [ ] Compress file size to < 25 MB using ffmpeg:
  ```bash
  ffmpeg -i raw_sprint2.mov -vcodec libx264 -crf 28 docs/demo_videos/sprint2_demo.mp4
  ```
- [ ] Place final video in `docs/demo_videos/sprint2_demo.mp4` or attach to GitHub Release.
