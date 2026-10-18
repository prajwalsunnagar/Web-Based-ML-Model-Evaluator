# Sprint Demo Video & Release Checklist

**Project:** Web-Based ML Model Evaluator  
**Deliverable Scope:** SE Mini-Project Deliverables — Part 2 (Sprints 1 & 2)  
**Status of Demo Videos:** **PENDING RECORDING** (No video recordings exist in the repository yet)

---

## 1. Sprint 1 Demo Video Checklist (One-Minute Walkthrough)

- **Target Duration:** Exactly 60 seconds (1 minute).
- **Scheduled Window:** 19 October – 23 October 2026.
- **Recording Video Status:** `PENDING`
- **Goal:** Demonstrate the working core evaluation flow: CSV upload, schema/column validation, metric selection, calculation, and KPI cards.

### Pre-Demo Setup & Environment Checklist
- [ ] Python 3.9+ active environment with dependencies installed (`pip install -r requirements.txt`).
- [ ] Run automated tests locally to verify baseline health (`pytest -v tests/`).
- [ ] Sample dataset ready: `sample_data/classification_sample.csv`.
- [ ] Launch Streamlit application in a clean browser window: `streamlit run app.py`.
- [ ] Ensure browser is at 100% zoom with readable fonts and full-screen / 1080p recording area.

### Script & Timestamp Outline (60 Seconds)

| Timestamp | Phase / Action | Audio / Visual Description | Requirements Demonstrated |
|---|---|---|---|
| **0:00 – 0:10** | **Introduction** | Introduce project: *Web-Based ML Model Evaluator*, highlighting that it simplifies verifying model outputs against ground truth. Show app header. | Project Overview |
| **0:10 – 0:25** | **Dataset Ingestion & Validation** | Drag & drop `classification_sample.csv`. Show instant file size check (< 10 MB), schema validation badge, dataset summary metrics (15 rows, 4 columns, 0 missing). | `FR-01`, `FR-02`, `FR-03`, `FR-04` |
| **0:25 – 0:40** | **Configuration & Mapping** | Map Ground Truth column to `terrain_actual` and Prediction column to `terrain_predicted`. In sidebar, select `Classification` and metrics: `Accuracy`, `Precision`, `Recall`, `F1 Score`. | `FR-04`, `FR-05`, `FR-06` |
| **0:40 – 0:55** | **Execution & KPI Results** | Click **Run Evaluation**. Show the generated `run_id`, selected metric KPI cards, and the confusion matrix crosstab. | `FR-07`, `FR-08` |
| **0:55 – 1:00** | **Conclusion** | Mention Sprint 1 core workflow is fully operational and verified by automated unit tests. | Sprint 1 DoD |

---

## 2. Sprint 2 Demo Video Checklist (Two-Minute Walkthrough)

- **Target Duration:** Exactly 120 seconds (2 minutes).
- **Scheduled Window:** 26 October – 30 October 2026.
- **Recording Video Status:** `PENDING`
- **Goal:** Demonstrate completed working product, regression evaluation, error handling & robustness, run history, report export, CI automation, and development freeze.

### Script & Timestamp Outline (120 Seconds)

| Timestamp | Phase / Action | Audio / Visual Description | Requirements Demonstrated |
|---|---|---|---|
| **0:00 – 0:25** | **Classification Run & Report Export** | Complete a classification run with `classification_sample.csv`. Switch to the **Export Report** tab and download `evaluation_report.json` and `metrics_summary.csv`. Show files downloaded locally. | `FR-08`, `FR-13`, `FR-14` |
| **0:25 – 0:55** | **Regression Task Support** | Switch sidebar to `Regression`. Upload `sample_data/regression_sample.csv`. Map `elevation_actual` to `elevation_predicted`. Select `MAE`, `MSE`, `RMSE`, `R²`. Click **Run Evaluation**. Show metric cards and residual error stats. | `FR-05`, `FR-06`, `FR-07`, `FR-08` |
| **0:55 – 1:20** | **Error Handling & Robustness** | Test invalid inputs live: upload a non-CSV or empty file to demonstrate safe user-actionable error messages without crashes. Highlight sidebar **Session Run History** showing prior runs with status badges. | `FR-09`, `FR-10`, `FR-11`, `NFR-02` |
| **1:20 – 1:40** | **Automated Testing Suite** | Show the current GitHub Actions run for the latest commit, or run `pytest -v tests/` locally and show its actual result. Include the direct evaluator-module tests and report the observed count and duration; do not reuse historical counts. | `NFR-01`, `NFR-03`, `TC-01`–`TC-09` |
| **1:40 – 2:00** | **CI Automation & Development Freeze** | Show GitHub repository with green GitHub Actions CI badge, all 10 backlog issues closed/tracked, and declare development frozen for Part-2 submission. | Deliverable Part C, Freeze |

---

## 3. Documentation Checklist for Final Demo

- [x] `README.md` updated with accurate technology stack, install steps, run command, and test guide.
- [x] `docs/SPRINT-PLAN.md` with complete functional/non-functional backlog items and story points.
- [x] `docs/TEST-EXECUTION-REPORT.md` with verified execution evidence for test cases TC-01 to TC-09.
- [x] `docs/DEVIATIONS-AND-NOTES.md` explaining architectural alignment with SAD and documented decisions.
- [x] `.github/pull_request_template.md` configured for team member PR workflow.
- [ ] Recorded Sprint 1 video (`sprint1_demo.mp4`) added to repo / releases.
- [ ] Recorded Sprint 2 video (`sprint2_demo.mp4`) added to repo / releases.

---

## 4. Instructions for Adding Recorded Videos to Repository

Once recorded using screen recording software (e.g., OBS Studio, QuickTime, macOS Screen Capture `Cmd+Shift+5`):
1. **Compress the video files** to keep repository size minimal (< 25 MB):
   ```bash
   # Optional ffmpeg compression if installed:
   ffmpeg -i raw_sprint1.mov -vcodec libx264 -crf 28 docs/demo_videos/sprint1_demo.mp4
   ffmpeg -i raw_sprint2.mov -vcodec libx264 -crf 28 docs/demo_videos/sprint2_demo.mp4
   ```
2. **Store in the repository:**
   Place the files in a dedicated directory:
   ```text
   docs/
   └── demo_videos/
       ├── sprint1_demo.mp4
       └── sprint2_demo.mp4
   ```
3. **Alternatively, use GitHub Releases / Drive Link:**
   If the repository size limit is constrained, create a GitHub Release titled `Deliverables Part 2 - Sprint Demos`, attach the MP4 files, and embed the release links in `README.md` and `docs/DEMO_CHECKLIST.md`.

---

## 5. Development Freeze Checklist

- [x] Code freeze: No new features introduced; only verified bug fixes and documentation.
- [x] Core modular engine separated in `evaluator/` (`validators.py`, `metrics.py`, `engine.py`).
- [ ] Run the current test suite, including `tests/test_evaluator_modules.py`, and record the verified result.
- [ ] Re-run linting against the current source and record the verified result.
- [x] CI workflow in `.github/workflows/ci.yml` updated and ready.
- [ ] Both demo videos recorded and linked.
- [ ] Final tag created (e.g., `git tag v1.0.0-part2-freeze`).
