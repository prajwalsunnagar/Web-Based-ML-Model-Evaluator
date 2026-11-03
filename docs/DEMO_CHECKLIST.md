# Sprint Demo Video & Release Checklist

**Project:** Web-Based ML Model Evaluator  
**Deliverable Scope:** SE Mini-Project Deliverables — Part 2 (Sprints 1 & 2)  
**Status of Demo Videos:** **PENDING RECORDING** (No video recordings exist in the repository yet)

---

## 1. Sprint 1 Demo Video Checklist (One-Minute Walkthrough)

- **Target Duration:** Exactly 60 seconds (1 minute).
- **Scheduled Window:** 19 October – 23 October 2026.
- **Recording Video Status:** `PENDING RECORDING`
- **Goal:** Demonstrate the working core evaluation flow: CSV upload, schema/column validation, metric selection, calculation, and KPI cards.
- **Narration Script:** [`docs/demo/sprint-1-narration-script.md`](demo/sprint-1-narration-script.md)

### Pre-Demo Setup & Environment Checklist
- [x] Python 3.10+ active environment with dependencies installed (`pip install -r requirements.txt`).
- [x] Run automated tests locally to verify baseline health (`pytest -v tests/`).
- [x] Sample dataset ready: `sample_data/classification_sample.csv`.
- [x] Launch Streamlit application in a clean browser window: `streamlit run app.py`.
- [x] Ensure browser is at 100% zoom with readable fonts and full-screen / 1080p recording area.

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
- **Recording Video Status:** `PENDING RECORDING`
- **Goal:** Demonstrate completed working product, regression evaluation, error handling & robustness, run history, report export, CI automation, and development freeze.
- **Narration Script:** [`docs/demo/sprint-2-narration-script.md`](demo/sprint-2-narration-script.md)

### Pre-Demo Setup & Environment Checklist
- [x] Dependencies installed (`pip install -r requirements.txt -r requirements-dev.txt`).
- [x] Automated test suite verified (`124 passed in 1.48s`).
- [x] Flake8 linting verified (`0 errors`).
- [x] Datasets ready: `sample_data/classification_sample.csv` and `sample_data/regression_sample.csv`.
- [x] Streamlit app launched: `streamlit run app.py`.

### Script & Timestamp Outline (120 Seconds)

| Timestamp | Phase / Action | Audio / Visual Description | Requirements Demonstrated |
|---|---|---|---|
| **0:00 – 0:25** | **Classification Run & Report Export** | Complete a classification run with `classification_sample.csv`. Inspect KPI cards and confusion matrix. Download `evaluation-<run_id>.json` and `metrics_summary_<id>.csv`. Show files downloaded locally. | `FR-08`, `FR-13`, `FR-14` |
| **0:25 – 0:55** | **Regression Task Support & Residuals** | Switch task to `Regression`. Upload `sample_data/regression_sample.csv`. Map `elevation_actual` to `elevation_predicted`. Select `MAE`, `MSE`, `RMSE`, `R²`. Click **Run Evaluation**. Show metric cards and residual error stats (Mean Error, Std Dev, Min, Max). | `FR-05`, `FR-06`, `FR-07`, `FR-08` |
| **0:55 – 1:20** | **Error Handling & Run History** | Test invalid inputs live: upload a non-numeric regression file, single-class classification input, or empty CSV to demonstrate safe user-actionable error messages without crashes. Highlight sidebar **Session Run History** showing prior runs with status badges (`Completed`, `Failed`) and the clear history action. | `FR-09`, `FR-10`, `FR-11`, `NFR-02` |
| **1:20 – 1:40** | **Automated Testing Suite** | Execute `pytest tests/ -v` live. Show all 124 tests passing across 6 test modules in ~1.5s with >90% coverage on core evaluator logic. | `NFR-01`, `NFR-03`, `TC-01`–`TC-09` |
| **1:40 – 2:00** | **CI Automation & Development Freeze** | Show GitHub Actions CI pipeline running matrix on Python 3.10, 3.11, and 3.12. Point out completed documentation and declare development officially frozen for Part-2 submission. | Deliverable Part C, Freeze |

---

## 3. Documentation Checklist for Final Demo

- [x] `README.md` updated with accurate technology stack, install steps, run command, and test guide.
- [x] `docs/SPRINT-PLAN.md` with complete functional/non-functional backlog items and story points.
- [x] `docs/TEST-EXECUTION-REPORT.md` with verified execution evidence for test cases TC-01 to TC-10 (124 tests).
- [x] `docs/PART2_DELIVERABLE_AUDIT.md` with full requirements coverage matrix and deliverable audit.
- [x] `docs/DEVIATIONS-AND-NOTES.md` explaining architectural alignment with SAD and documented decisions.
- [x] `docs/demo/sprint-1-narration-script.md` 60-second walkthrough script.
- [x] `docs/demo/sprint-2-narration-script.md` 120-second walkthrough script.
- [x] `.github/pull_request_template.md` configured for team member PR workflow.
- [ ] Recorded Sprint 1 video (`sprint1_demo.mp4`) added to repo / releases.
- [ ] Recorded Sprint 2 video (`sprint2_demo.mp4`) added to repo / releases.

---

## 4. Instructions for Adding Recorded Videos to Repository

Once recorded using screen recording software (e.g., OBS Studio, QuickTime, macOS Screen Capture `Cmd+Shift+5`):
1. **Compress the video files** to keep repository size minimal (< 25 MB):
   ```bash
   ffmpeg -i raw_sprint1.mov -vcodec libx264 -crf 28 docs/demo_videos/sprint1_demo.mp4
   ffmpeg -i raw_sprint2.mov -vcodec libx264 -crf 28 docs/demo_videos/sprint2_demo.mp4
   ```
2. **Store in the repository:**
   Place the files in the dedicated directory:
   ```text
   docs/
   └── demo_videos/
       ├── sprint1_demo.mp4
       └── sprint2_demo.mp4
   ```
3. **Alternatively, use GitHub Releases / Drive Link:**
   If repository storage is constrained, create a GitHub Release titled `Deliverables Part 2 - Sprint Demos`, attach the MP4 files, and embed the release links in `README.md` and `docs/DEMO_CHECKLIST.md`.

---

## 5. Development Freeze Checklist

- [x] Code freeze: No new features introduced; only verified bug fixes and documentation.
- [x] Core modular engine separated in `evaluator/` (`validators.py`, `metrics.py`, `engine.py`).
- [x] Full automated test suite executed (124 passed in 1.48s, 0 failures).
- [x] PEP 8 linting executed (0 flake8 errors/warnings).
- [x] CI workflow in `.github/workflows/ci.yml` verified and active across Python 3.10, 3.11, 3.12.
- [ ] Both demo videos recorded and placed in `docs/demo_videos/` or linked in release.
- [ ] Final tag created (`git tag v1.0.0-part2-freeze`).
