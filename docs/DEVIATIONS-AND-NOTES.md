# Architectural Alignment, Design Decisions & Deviations

**Project:** Web-Based ML Model Evaluator  
**Document Reference:** Deliverable 1 (SRS), Deliverable 3 (SAD), Part B & C Mini-Project Deliverables  
**Status:** Development Frozen for Deliverables Part 2 Submission  

---

## 1. Architectural Alignment with Submitted SAD

The implemented application strictly follows the modular design specified in **Section 4.1 & 4.2 of the Software Architecture Document (SAD)**:

1. **Upload Handler & Schema Validator (`evaluator/validators.py`):**
   - Implements `validate_file_size` and `validate_file_type` before heavy file processing.
   - Enforces unique header columns, non-empty data rows, and non-empty target/prediction sequences.

2. **Configuration Validator & Metric Engine (`evaluator/metrics.py`):**
   - Implements the testable contract: `calculate_metrics(task_type, y_true, y_pred, selected_metrics, average)`.
   - Adheres to `BR-01` through `BR-05`: verifies task/metric compatibility, enforces deterministic float computations, and isolates metric calculation logic from presentation components (NFR-09).

3. **Evaluation Service & Orchestrator (`evaluator/engine.py`):**
   - Manages the lifecycle of an `EvaluationRun` (`pending` -> `running` -> `completed` / `failed`).
   - Links run results with an immutable `run_id`, timestamp, source file name, target column, prediction column, and sample count (`FR-14`).
   - Sanitizes errors so that internal server stack traces are not leaked to users (`NFR-02`, `SEC-06`).

4. **Result Presenter (`app.py`):**
   - Provides a clean, responsive web interface built using Streamlit.
   - Renders metric cards, summary tables, confusion matrix (classification), residual metrics (regression), and JSON/CSV report downloads (`FR-08`, `FR-13`).

---

## 2. Documented Deviations & Rationale

| Requirement / Item | Submitted Document Baseline | Actual Implementation | Rationale & Engineering Justification |
|---|---|---|---|
| **Multi-tenant Accounts (`FR-12`, `TC-10`, `SEC-04`)** | Mentioned conditionally in SRS as "If user accounts are implemented...". | Implemented as a single-tenant local/browser session application without user authentication. | The mini-project specification scopes the application to standalone evaluation without complex backend user management databases. `TC-10` is therefore marked `N/A (Documented)`. |
| **REST API Server vs. Streamlit Engine** | SAD Section 4.5 illustrated potential REST endpoints (`POST /api/datasets`, `POST /api/evaluations`). | Integrated evaluation service package (`evaluator/`) directly consumed by the Streamlit application and unit test suite. | Avoids redundant network round-trips for local evaluation while preserving strict layer separation (`evaluator/` can be wrapped into FastAPI/Flask if needed without modifying metric logic). |
| **Model Weight Inference vs. Prediction Evaluation** | SRS Section 1.2 noted: "The project team must confirm whether the actual application evaluates uploaded prediction files, loads serialized models...". | Evaluator accepts paired dataset CSVs containing ground truth reference labels and model prediction columns. | Provides universal compatibility across any model family (tabular, deep learning, NLP) without requiring runtime model weights or heavy GPU hardware on the evaluation machine. |

---

## 3. Development Freeze Declaration

- **Freeze Date:** 30 October 2026 (Ready for submission review as of 12 October 2026)
- **Status:** All Sprint 1 and Sprint 2 features implemented, verified with automated unit tests, and documented.
- **Repository Baseline Commit:** Head of `main`.
