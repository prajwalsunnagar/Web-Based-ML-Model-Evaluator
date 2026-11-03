# Software Engineering Mini-Project — Final Academic Submission Checklist

**Project Title:** Web-Based ML Model Evaluator  
**Document Identifier:** FSC-WBMLE-2026-V2.0  
**Status:** Approved / Development Freeze  
**Verification Date:** 3 November 2026  
**Repository:** [prajwalsunnagar/Web-Based-ML-Model-Evaluator](https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator)  
**Target Branch:** `feature/sprint-2-completion` (PR #16 $\rightarrow$ `main`)  
**Project Team Members:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — Repository Owner / ML Evaluation Engine Lead
- **Shreyank S** (`@ShreyankSridhar`) — Documentation & UI Lead
- **Skanda** (`@skandaml21`) — Backend Architecture & QA Lead
- **Sujal** (`@sujalththth-ops`) — Full-Stack Workflow & Reporting Lead

---

## 1. Master Submission Deliverable Checklist

### Part 1: Requirements, Architecture, Test Planning & Sprint 1

| Deliverable Item | Required Format & Standard | Associated Repository Artifacts | Status |
|---|---|---|---|
| **Software Requirements Specification (SRS)** | IEEE Std 830-1998 format; FR-01–FR-14, NFR-01–NFR-12, SO-01–SO-04, SEC-01–SEC-08, UML Use Case diagram | [`docs/SRS-REVISED.docx`](SRS-REVISED.docx)<br>[`docs/SRS-REVISED.md`](SRS-REVISED.md)<br>[`docs/SRS.docx`](SRS.docx) | **COMPLETE** |
| **Software Architecture & Design (SAD)** | IEEE Std 1016-2009 format; 3-tier modular reactive architecture, 4 Mermaid sequence & component diagrams, security boundaries | [`docs/Architecture-Design-REVISED.docx`](Architecture-Design-REVISED.docx)<br>[`docs/Architecture-Design-REVISED.md`](Architecture-Design-REVISED.md)<br>[`docs/Architecture-Design.docx`](Architecture-Design.docx) | **COMPLETE** |
| **Software Test Plan (STP)** | IEEE Std 829-2008 format; test scope, test strategy, 14 formal test cases (TC-01–TC-14), 9 security validations (SV-01–SV-09) | [`docs/Test-Plan-REVISED.docx`](Test-Plan-REVISED.docx)<br>[`docs/Test-Plan-REVISED.md`](Test-Plan-REVISED.md)<br>[`docs/Test-Plan.docx`](Test-Plan.docx) | **COMPLETE** |
| **Agile Sprint 1 Plan & Backlog** | Delivery milestones, Fibonacci scale, 22 SP across Issues #1 to #6, Definition of Done | [`docs/SPRINT-PLAN.md`](SPRINT-PLAN.md) | **COMPLETE** |
| **Sprint 1 Demonstration Video** | 1-minute video demonstration (0:00–1:00); CSV upload, validation, classification KPI cards | [`docs/demo/SPRINT-1-RECORDING-GUIDE.md`](demo/SPRINT-1-RECORDING-GUIDE.md)<br>[`docs/demo/sprint-1-narration-script.md`](demo/sprint-1-narration-script.md)<br>`docs/demo_videos/sprint1_demo.mp4` | **NEEDS MANUAL ACTION** (Script complete; video pending physical screen capture) |

---

### Part 2: Implementation, Automated Testing, Robustness, CI & Sprint 2

| Deliverable Item | Required Format & Standard | Associated Repository Artifacts | Status |
|---|---|---|---|
| **Working Application** | Python/Streamlit web app; Classification & Regression, residuals, confusion matrix, session history, report export | [`app.py`](../app.py)<br>[`evaluator/`](../evaluator/) (`validators.py`, `metrics.py`, `engine.py`) | **COMPLETE** |
| **Sample Datasets** | Tabular RFC 4180 CSV test data for Classification & Regression | [`sample_data/classification_sample.csv`](../sample_data/classification_sample.csv)<br>[`sample_data/regression_sample.csv`](../sample_data/regression_sample.csv) | **COMPLETE** |
| **Automated Test Suites** | 124 unit and integration tests; 100% pass rate in < 2.0s; >90% coverage on core evaluator logic | [`tests/`](../tests/) (`test_validation.py`, `test_classification.py`, `test_regression.py`, `test_error_handling.py`, `test_evaluator_modules.py`, `test_app_integration.py`) | **COMPLETE** |
| **CI Automation Pipeline** | Multi-version matrix (Python 3.10, 3.11, 3.12); Flake8 PEP 8 linting, bytecode compilation, pytest coverage | [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) | **COMPLETE** |
| **Requirement Traceability Matrix** | Standalone RTM mapping SRS $\rightarrow$ Issues $\rightarrow$ Code $\rightarrow$ Tests $\rightarrow$ Verification evidence | [`docs/REQUIREMENT-TRACEABILITY-MATRIX.md`](REQUIREMENT-TRACEABILITY-MATRIX.md) | **COMPLETE** |
| **Test Execution Report** | Execution logs, 124 passing test summary, coverage breakdown (95% validators, 92% engine, 90% metrics) | [`docs/TEST-EXECUTION-REPORT.md`](TEST-EXECUTION-REPORT.md) | **COMPLETE** |
| **Architectural Deviations** | 8-point engineering analysis for all architectural and scope differences; ADRs | [`docs/DEVIATIONS-AND-NOTES.md`](DEVIATIONS-AND-NOTES.md) | **COMPLETE** |
| **Sprint 2 Demonstration Video** | 2-minute video demonstration (0:00–2:00); Classification, regression, error handling, run history, test run, CI | [`docs/demo/SPRINT-2-RECORDING-GUIDE.md`](demo/SPRINT-2-RECORDING-GUIDE.md)<br>[`docs/demo/sprint-2-narration-script.md`](demo/sprint-2-narration-script.md)<br>`docs/demo_videos/sprint2_demo.mp4` | **NEEDS MANUAL ACTION** (Script complete; video pending physical screen capture) |
| **GitHub Projects Board Setup** | Projects v2 Kanban board setup instructions, custom fields (Sprint, Story Points, Status) | [`docs/SPRINT-PLAN.md`](SPRINT-PLAN.md)<br>[`docs/PART2_DELIVERABLE_AUDIT.md`](PART2_DELIVERABLE_AUDIT.md) | **NEEDS MANUAL ACTION** (User-level GitHub action) |
| **Development Freeze** | Formal development freeze declaration for Part-2 submission | Section 3 below; [`docs/DEVIATIONS-AND-NOTES.md`](DEVIATIONS-AND-NOTES.md) | **COMPLETE** |

---

## 2. Quality Verification Gates (All Passed)

- [x] **Gate 1: Automated Test Suite**
  - **Result:** 124 of 124 tests passed in 1.48–1.75 seconds.
  - **Command:** `pytest tests/ -v`
- [x] **Gate 2: Code Coverage**
  - **Result:** 92.2% average coverage across `evaluator/` core (`validators.py`: 95%, `engine.py`: 92%, `metrics.py`: 90%).
  - **Command:** `pytest --cov=evaluator --cov=app`
- [x] **Gate 3: Code Linting & Style**
  - **Result:** 0 PEP 8 errors.
  - **Command:** `flake8 app.py evaluator/ tests/ --max-line-length=120 --exclude=.venv`
- [x] **Gate 4: Bytecode Compilation**
  - **Result:** 0 syntax or compilation errors.
  - **Command:** `python -m py_compile app.py evaluator/*.py tests/*.py`
- [x] **Gate 5: Continuous Integration**
  - **Result:** All 6 GitHub Actions jobs passing across Python 3.10, 3.11, and 3.12.
- [x] **Gate 6: Secret & Credential Scanning**
  - **Result:** 0 secrets, tokens, or credentials committed.
- [x] **Gate 7: IEEE Documentation Standards**
  - **Result:** SRS revised to IEEE 830, SAD revised to IEEE 1016, STP revised to IEEE 829. Both DOCX and Markdown maintained.

---

## 3. Formal Development Freeze Declaration

We, the development team of the **Web-Based ML Model Evaluator**, hereby declare that development for the Software Engineering Mini-Project Deliverables (Part 1 and Part 2) is **OFFICIALLY FROZEN** as of **3 November 2026**.

No further functional alterations or feature additions will be introduced to `main`. The codebase, test suites, and documentation represent our verified, final academic submission.

| Role | Team Member | GitHub Handle | Signature / Status |
|---|---|---|---|
| **Repository Owner / ML Engine Lead** | Prajwal Sunnagar | `@prajwalsunnagar` | **SIGNED & FROZEN** |
| **Documentation & UI Lead** | Shreyank S | `@ShreyankSridhar` | **SIGNED & FROZEN** |
| **Backend Architecture & QA Lead** | Skanda | `@skandaml21` | **SIGNED & FROZEN** |
| **Full-Stack Integration Lead** | Sujal | `@sujalththth-ops` | **SIGNED & FROZEN** |
