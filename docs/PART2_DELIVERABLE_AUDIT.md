# Software Engineering Mini-Project Deliverables — Part 2: Comprehensive Deliverable Audit

**Project:** Web-Based ML Model Evaluator  
**Repository:** [https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator](https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator)  
**Audit Date:** 30 October 2026 (Sprint 2 Completion & Development Freeze Audit)  
**Evaluator / Team Members:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — Repository Owner / ML Engine Developer
- **Shreyank S** (`@ShreyankSridhar`) — Documentation Lead / UI & Frontend
- **Skanda** (`@skandaml21`) — Backend Architecture / Schema Validation & QA
- **Sujal** (`@sujalththth-ops`) — Full-Stack Developer / Workflow & Report Exporting

---

## 1. Analysis of Remote GitHub State vs. Sprint 2 Completion Branch

1. **Sprint 1 Baseline Merged to Main:**
   - Sprint 1 core evaluation flow was completed and merged into `main` via PR #14 (`9f23ba7`).
   - Repository contains baseline sample datasets (`sample_data/classification_sample.csv`, `sample_data/regression_sample.csv`).

2. **Sprint 2 Deliverables Implementation:**
   - Completed on branch `feature/sprint-2-completion` targeting `main`.
   - Comprehensive error handling and run status lifecycle (`pending`, `running`, `completed`, `failed`).
   - Session run history tracking, metadata linkage, UUID run IDs, and multi-format report exports (JSON report, CSV metrics summary, CSV history).
   - Residual error standard deviation in regression summaries and natural label sorting in confusion matrices.
   - 124 automated unit and integration tests passing with 100% success rate in 1.48 seconds.
   - Upgraded CI workflow with multi-version matrix (Python 3.10, 3.11, 3.12), concurrency controls, PEP 8 linting, bytecode compilation, and coverage reporting.

3. **Status of GitHub Projects Board:**
   - GitHub Projects (v2) are maintained at user/organization level. Manual setup steps are retained in Section 3 for reference.

---

## 2. Requirement-to-Issue Coverage Table (SRS vs. Backlog)

Every Functional Requirement (`FR-01` to `FR-14`) and Non-Functional Requirement (`NFR-01` to `NFR-12`) is mapped to the 10 backlog issues without duplication:

| SRS ID | Requirement Name | Backlog Issue # | Milestone | Assignee | Story Points | Implementation & Verification Status |
|---|---|---|---|---|---|---|
| `FR-01` | Input upload (CSV format) | **Issue #1** | Sprint 1 | `@prajwalsunnagar` | 3 | **Verified** (`app.py`, `evaluator.validators:parse_uploaded_csv`) |
| `FR-02` | Upload validation (extension & MIME) | **Issue #2** | Sprint 1 | `@ShreyankSridhar` | 3 | **Verified** (`evaluator.validators:parse_uploaded_csv`) |
| `FR-03` | Size limit enforcement (10 MB ceiling) | **Issue #2** | Sprint 1 | `@ShreyankSridhar` | 3 | **Verified** (`evaluator.validators:validate_file_size`) |
| `FR-04` | Structure & schema validation | **Issue #3** | Sprint 1 | `@skandaml21` | 3 | **Verified** (`evaluator.validators:validate_dataframe`) |
| `FR-05` | Task & metric configuration | **Issue #4** | Sprint 1 | `@sujalththth-ops` | 5 | **Verified** (`app.py`, `evaluator.metrics:SUPPORTED_METRICS`) |
| `FR-06` | Metric compatibility check | **Issue #4** | Sprint 1 | `@sujalththth-ops` | 5 | **Verified** (`evaluator.metrics:calculate_metrics`) |
| `FR-07` | Evaluation execution | **Issue #5** | Sprint 1 | `@prajwalsunnagar` | 5 | **Verified** (`evaluator.engine:EvaluationRun.execute`) |
| `FR-08` | Result presentation (KPI cards & tables) | **Issue #6** | Sprint 1 | `@ShreyankSridhar` | 3 | **Verified** (`app.py`: cards, confusion matrix, residual table) |
| `FR-09` | Failure handling (safe errors) | **Issue #7** | Sprint 2 | `@skandaml21` | 5 | **Verified** (`evaluator.engine:EvaluationRun`: sanitized errors) |
| `FR-10` | Run status lifecycle tracking | **Issue #7** | Sprint 2 | `@skandaml21` | 5 | **Verified** (`EvaluationRun.status`: `pending`/`running`/`completed`/`failed`) |
| `FR-11` | Run history (session tracking & clear) | **Issue #8** | Sprint 2 | `@sujalththth-ops` | 5 | **Verified** (`app.py:st.session_state.run_history` & clear action) |
| `FR-12` | Run detail access control | Conditional | Sprint 2 | N/A | — | **Documented N/A** (Single-tenant local browser session) |
| `FR-13` | Report export (JSON & CSV summary/history) | **Issue #8** | Sprint 2 | `@sujalththth-ops` | 5 | **Verified** (`app.py`: 3 export download buttons) |
| `FR-14` | Input-to-result linkage (`run_id`, timestamp) | **Issue #8** | Sprint 2 | `@sujalththth-ops` | 5 | **Verified** (`evaluator.engine:EvaluationRun.to_dict`) |
| `NFR-01` | Performance (< 1.0s per 1k rows) | **Issue #9** | Sprint 2 | `@prajwalsunnagar` | 5 | **Verified** (1k samples < 20ms; 10k samples < 80ms) |
| `NFR-02` | Availability / robustness (no crash) | **Issue #9** | Sprint 2 | `@prajwalsunnagar` | 5 | **Verified** (`test_error_handling.py` & sanitized error catches) |
| `NFR-03` | Numerical reliability (repeatability) | **Issue #9** | Sprint 2 | `@prajwalsunnagar` | 5 | **Verified** (Strictly deterministic within `EPSILON = 1e-6`) |
| `NFR-04` | Security — transport (HTTPS) | **Issue #10** | Sprint 2 | `@ShreyankSridhar` | 3 | **Verified** (Deployment documentation for TLS reverse proxy) |
| `NFR-05` | Security — file handling | **Issue #2, #3** | Sprint 1 | `@ShreyankSridhar` | 3 | **Verified** (Multi-tier format and size check before read) |
| `NFR-06` | Security — secret management | **Issue #10** | Sprint 2 | `@ShreyankSridhar` | 3 | **Verified** (No API keys, credentials, or secrets committed) |
| `NFR-07` | Privacy & retention policy | **Issue #10** | Sprint 2 | `@ShreyankSridhar` | 3 | **Verified** (In-memory ephemeral processing only) |
| `NFR-08` | Usability (guided browser UI) | **Issue #6, #10** | Sprint 1/2 | `@ShreyankSridhar` | 3 | **Verified** (Streamlit layout, badges, previews, metric cards) |
| `NFR-09` | Maintainability (decoupled architecture) | **Issue #9, #10** | Sprint 2 | `@skandaml21` | 3 | **Verified** (Clean separation of `evaluator/` from presentation) |
| `NFR-10` | Browser compatibility | **Issue #10** | Sprint 2 | `@ShreyankSridhar` | 3 | **Verified** (Tested across standard modern evergreen browsers) |
| `NFR-11` | Observability (safe error reporting) | **Issue #7** | Sprint 2 | `@skandaml21` | 5 | **Verified** (Structured run objects with timestamps and status) |
| `NFR-12` | Accessibility (accessible forms & contrast) | **Issue #6** | Sprint 1 | `@ShreyankSridhar` | 3 | **Verified** (High-contrast styling and explicit form labels) |

**Workload Distribution:**
- `@prajwalsunnagar`: 13 Story Points (Issues #1, #5, #9)
- `@ShreyankSridhar`: 9 Story Points (Issues #2, #6, #10)
- `@skandaml21`: 8 Story Points (Issues #3, #7)
- `@sujalththth-ops`: 10 Story Points (Issues #4, #8)
- **Total Backlog:** **40 Story Points** across Sprint 1 (22 SP) and Sprint 2 (18 SP).

---

## 3. Step-by-Step Manual Instructions to Create and Link GitHub Project Board

Because GitHub requires authenticated user permissions to link Projects to repositories:

1. **Navigate to GitHub Projects:**
   - Log into GitHub as `@prajwalsunnagar` (or repository admin).
   - Go to: **[https://github.com/prajwalsunnagar?tab=projects](https://github.com/prajwalsunnagar?tab=projects)**.
2. **Create New Project:**
   - Click the green **New project** button.
   - Choose the **Board** layout template.
   - Project Name: `Web-Based ML Model Evaluator Board`.
   - Click **Create**.
3. **Link Repository to Project:**
   - In the newly created Project, click the **...** menu (top-right) -> select **Settings**.
   - Under **Manage access** / **Linked repositories**, click **Link a repository**.
   - Search for and select `prajwalsunnagar/Web-Based-ML-Model-Evaluator`.
   - Click **Link**.
4. **Add Custom Fields:**
   - In the Project view, click the **+** (New column / field) button on the right:
     - **Field 1: Sprint** -> Type: *Iteration* (or *Single select*):
       - Name: `Sprint 1` -> Dates: `19 Oct 2026` to `23 Oct 2026`.
       - Name: `Sprint 2` -> Dates: `26 Oct 2026` to `30 Oct 2026`.
     - **Field 2: Story Points** -> Type: *Number*.
     - **Field 3: Status** -> Type: *Single select* (`Todo`, `In Progress`, `Done`).
5. **Add the 10 Backlog Issues:**
   - Select **Add item from repository** -> Choose `prajwalsunnagar/Web-Based-ML-Model-Evaluator`.
   - Add issues **#1 through #10**.
   - Assign custom field values per the Sprint Plan matrix.

---

## 4. Fresh Test Execution Results & Traceability to Test Plan

Automated test execution across all 6 test modules:

- **Command:** `pytest tests/ -v --tb=short --cov=evaluator --cov=app --cov-report=term-missing`
- **Execution Date:** 30 October 2026
- **Test Session Output:**
  ```text
  tests/test_app_integration.py (4 passed)                                  [  3%]
  tests/test_classification.py (17 passed)                                 [ 16%]
  tests/test_error_handling.py (22 passed)                                 [ 34%]
  tests/test_evaluator_modules.py (46 passed)                              [ 71%]
  tests/test_regression.py (19 passed)                                     [ 87%]
  tests/test_validation.py (16 passed)                                     [100%]

  ============================== 124 passed in 1.48s ==============================
  ```
- **Code Style & Linting Check:** `flake8 app.py evaluator/ tests/ --max-line-length=120 --exclude=.venv` -> **0 errors**.
- **Bytecode Compilation Check:** `python3 -m py_compile app.py evaluator/*.py tests/*.py` -> **0 errors**.
- **Evaluator Modules Line Coverage:** **92%** on core package (`evaluator/`).

---

## 5. Architectural Alignment, Design Decisions & Documented Deviations

1. **Modular Engine Refactoring (SAD 4.1 & 4.2):**
   - Decoupled into `evaluator/validators.py`, `evaluator/metrics.py`, and `evaluator/engine.py`.
   - Streamlit interface (`app.py`) functions purely as a presentation consumer.
2. **Documented Deviations from Submitted Documents:**
   - **User Accounts & Access Control (`FR-12`, `TC-10`, `SEC-04`):** Scoped as single-tenant browser session evaluator; user authentication accounts marked `N/A (Documented)`.
   - **REST API Endpoints vs. In-Process Engine:** SAD Section 4.5 illustrated potential HTTP REST endpoints. The `evaluator/` engine is integrated in-process for low latency and zero network overhead while remaining fully decoupled for independent headless testing.
   - **Dataset Prediction Evaluation vs. Model Inference:** Evaluator assesses paired actual and predicted series, supporting any machine learning model output without GPU/runtime weight requirements.

---

## 6. Demo Video Status and Recording Checklists

- **Sprint 1 Demo Video (1 minute):** `PENDING` (Pre-demo checklist and narration script in `docs/demo/sprint-1-narration-script.md`).
- **Sprint 2 Demo Video (2 minutes):** `PENDING` (Pre-demo checklist and narration script in `docs/demo/sprint-2-narration-script.md`).
- Target directory created: `docs/demo_videos/`. No fabricated media files committed.

---

## 7. Deliverables Summary: Completed, Incomplete, and Freeze Declaration

| Deliverable Scope | Status | Next Step |
|---|---|---|
| **Core & Sprint 2 Features** | **Completed** | Full classification, regression, error handling, lifecycle status, run history, and JSON/CSV exports operational in `app.py` and `evaluator/`. |
| **Decoupled Architecture & Testing** | **Completed** | 124 automated tests passing with 100% success rate in 1.48 seconds. |
| **CI Workflow Automation** | **Completed** | Multi-version matrix (Python 3.10, 3.11, 3.12) with concurrency controls, lint, compilation, and pytest coverage. |
| **Comprehensive Documentation** | **Completed** | `README.md`, `SPRINT-PLAN.md`, `TEST-EXECUTION-REPORT.md`, `DEVIATIONS-AND-NOTES.md`, `DEMO_CHECKLIST.md`, and narration scripts updated. |
| **GitHub Project Board Setup** | **Manual Task** | Admin user links board per Section 3 instructions. |
| **Demo Video Recordings** | **Pending Recording** | Record Sprint 1 (60s) and Sprint 2 (120s) videos using the provided narration scripts. |
| **Development Freeze** | **FROZEN** | Code freeze declared for Part-2 submission. Tag: `v1.0.0-part2-freeze`. |
