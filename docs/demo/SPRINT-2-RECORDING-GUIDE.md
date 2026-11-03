# Sprint 2 Demonstration Recording Guide & Narration Script

**Project Title:** Web-Based ML Model Evaluator  
**Milestone:** Sprint 2 Review & Final Academic Submission  
**Target Duration:** Exactly 120 Seconds (2 Minutes)  
**Target Output File:** `docs/demo_videos/sprint2_demo.mp4`  
**Recording Status:** **PENDING MANUAL RECORDING** (Use this guide for screencast capture)  
**Team Members:** Prajwal Sunnagar, Shreyank S, Skanda, Sujal

---

## 1. Recording Setup & Technical Requirements

- **Resolution:** 1080p ($1920 \times 1080$) at 30 fps.
- **Audio:** Clear voiceover with noise suppression; no background music.
- **Format:** MP4 (H.264 video codec, AAC audio).
- **Target File Size:** $< 25\text{ MB}$.
- **Local Application Command:**
  ```bash
  streamlit run app.py
  ```
- **Prepared Datasets:**
  - `sample_data/classification_sample.csv` (15 rows, 4 classes)
  - `sample_data/regression_sample.csv` (10 rows, numeric targets)

---

## 2. Timed Scene-by-Scene Script (120 Seconds)

### [0:00 – 0:25] Classification Evaluation & Report Export
- **Visual Action:**
  1. Open application in browser (`http://localhost:8501`).
  2. Upload `sample_data/classification_sample.csv`.
  3. Select `Classification`, map `terrain_actual` and `terrain_predicted`.
  4. Select `Accuracy`, `Precision`, `Recall`, `F1-score` and click **Calculate evaluation metrics**.
  5. Show KPI cards (Accuracy: 0.8667) and naturally sorted confusion matrix.
  6. Click **Download latest run (JSON)** and **Download metrics summary (CSV)**; show files downloaded in browser tray.
- **Spoken Narration:**
  > *"Welcome to the Sprint 2 demonstration of the Web-Based ML Model Evaluator. We begin with our end-to-end classification workflow. Uploading `classification_sample.csv`, the application immediately validates file format, size, and schema integrity, rendering a 10-row dataset preview.*
  >
  > *We configure our evaluation for Classification, mapping `terrain_actual` against `terrain_predicted` with weighted averaging. Clicking calculate generates a unique UUIDv4 run identifier, computing high-visibility KPI cards and a sorted confusion matrix.*
  >
  > *Sprint 2 adds comprehensive report export capabilities: with one click, users can download the full evaluation report as JSON and the metrics summary as CSV for offline auditing."*

---

### [0:25 – 0:55] Regression Evaluation & Residual Diagnostics
- **Visual Action:**
  1. Upload `sample_data/regression_sample.csv`.
  2. Select `Regression`, map `elevation_actual` to `elevation_predicted`.
  3. Select all metrics: `MAE`, `MSE`, `RMSE`, `R²` and click **Calculate evaluation metrics**.
  4. Display KPI cards (MAE: 0.8200, MSE: 0.9840, RMSE: 0.9920, R²: 0.9996).
  5. Scroll to the new **Regression residual summary** table showing: Mean Error, Residual Standard Deviation, Minimum Error, and Maximum Error.
- **Spoken Narration:**
  > *"Next, we demonstrate our full regression workflow. Uploading `regression_sample.csv`, we map `elevation_actual` to `elevation_predicted` and select all four regression metrics: MAE, MSE, RMSE, and R-squared.*
  >
  > *Upon execution, the engine deterministically computes model errors with four-decimal precision, confirming near-perfect fit with an R-squared of 0.9996.*
  >
  > *Sprint 2 adds an in-depth residual error analysis, reporting mean prediction error, residual standard deviation, minimum error, and maximum error, providing immediate diagnostic insight into prediction bias and variance."*

---

### [0:55 – 1:20] Invalid Input Handling & Session Run History
- **Visual Action:**
  1. Select identical columns to trigger the validation guard banner.
  2. Trigger non-numeric regression input rejection to display the safe, actionable error banner without stack trace leakage.
  3. Expand the **Sidebar Session Run History** showing prior runs with status badges (`Completed`, `Failed`), task types, and truncated run IDs.
  4. Show the full history table at the bottom of the page, click **Download run history (CSV)**, and click **Clear run history** to show session state reset.
- **Spoken Narration:**
  > *"A primary focus of Sprint 2 is error handling robustness. If invalid inputs, non-numeric strings, or identical column mappings are supplied, the application catches the condition gracefully. As seen here, user-friendly banners provide actionable guidance without ever exposing internal stack traces, system paths, or raw server exceptions.*
  >
  > *All evaluation runs—both completed and failed—are tracked in session history with unique run IDs, timestamps, and execution parameters. Users can download the entire session run history as CSV, or clear the history at any time."*

---

### [1:20 – 1:40] Automated Test Execution
- **Visual Action:**
  1. Switch to terminal window.
  2. Run:
     ```bash
     pytest tests/ -v --tb=short --cov=evaluator --cov=app
     ```
  3. Highlight terminal output: 124 passed in ~1.5s, 0 failures, >90% coverage on core evaluator.
- **Spoken Narration:**
  > *"Turning to automated quality assurance: our test suite has expanded to 124 automated unit and integration tests across six test modules, covering upload validation, classification, regression, edge cases, lifecycle states, and Streamlit UI flows.*
  >
  > *Running pytest live, all 124 tests pass in under 1.5 seconds, satisfying our performance requirement of less than 2 seconds, while achieving over 90% line coverage on our core evaluator business logic. Numerical determinism is verified to within 1e-6 across repeated runs."*

---

### [1:40 – 2:00] GitHub Actions, Documentation & Development Freeze
- **Visual Action:**
  1. Switch to GitHub repository in browser.
  2. Display the GitHub Actions tab showing green passing checks across Python 3.10, 3.11, and 3.12.
  3. Show synchronized documentation: `README.md`, `SRS-REVISED.docx`, `Architecture-Design-REVISED.docx`, `Test-Plan-REVISED.docx`, and `FINAL_REPOSITORY_AUDIT.md`.
  4. Highlight the formal development freeze declaration.
- **Spoken Narration:**
  > *"In our continuous integration pipeline, GitHub Actions automatically executes our multi-version matrix across Python 3.10, 3.11, and 3.12 on every push and pull request, enforcing flake8 PEP 8 linting, bytecode compilation, and pytest coverage.*
  >
  > *All project documentation—including the SRS, SAD, Test Execution Report with full Requirement Traceability Matrix, and Sprint Plan—is fully synchronized.*
  >
  > *With all Sprint 1 and Sprint 2 backlog items verified and Definition of Done fulfilled, we formally declare development frozen for the Part-2 submission. Thank you!"*

---

## 3. Post-Recording Compression Command

```bash
ffmpeg -i raw_sprint2_recording.mov -vcodec libx264 -crf 28 -pix_fmt yuv420p docs/demo_videos/sprint2_demo.mp4
```
