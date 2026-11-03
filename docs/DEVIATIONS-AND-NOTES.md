# Architectural Alignment, Design Decisions & Deviations

**Project:** Web-Based ML Model Evaluator  
**Document Reference:** Deliverable 1 (SRS IEEE 830), Deliverable 3 (SAD IEEE 1016), Part-2 Submission  
**Status:** Approved / Development Freeze  
**Execution & Freeze Date:** 3 November 2026  
**Authors & Reviewers:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — ML Evaluation Engine Lead
- **Shreyank S** (`@ShreyankSridhar`) — Documentation & UI Lead
- **Skanda** (`@skandaml21`) — Backend Architecture & QA Lead
- **Sujal** (`@sujalththth-ops`) — Integration & Reporting Lead

---

## 1. Architectural Alignment with Submitted SAD

The implemented application strictly follows the modular design specified in the Software Architecture Document (SAD):

1. **Upload Handler & Schema Validator (`evaluator/validators.py`):**
   - Implements `validate_file_size` and `validate_file_type` prior to in-memory DataFrame construction.
   - Enforces standard CSV MIME type matching, unique header columns, non-empty data rows, and non-empty target/prediction sequences.

2. **Configuration Validator & Metric Engine (`evaluator/metrics.py`):**
   - Implements the contract: `calculate_metrics(y_true, y_pred, task_type, selected_metrics)`.
   - Adheres to `BR-01` through `BR-05`: verifies task/metric compatibility, enforces deterministic float computations, and isolates metric calculation logic from presentation components (`NFR-09`).
   - Generates confusion matrix with natural numeric/string label ordering.
   - Computes signed regression residual statistics including residual standard deviation.

3. **Evaluation Service & Orchestrator (`evaluator/engine.py`):**
   - Manages the lifecycle of an `EvaluationRun` (`pending` $\rightarrow$ `running` $\rightarrow$ `completed` / `failed`).
   - Resets run error state upon subsequent executions.
   - Links run results with an immutable `run_id`, timestamp, source file name, target column, prediction column, sample count, and averaging method (`FR-14`).
   - Sanitizes errors so that internal server stack traces and raw file paths are never leaked to users (`NFR-02`, `SEC-06`).
   - Sanitizes NaN and infinite metric outputs to `None` for compliant JSON serialization.

4. **Result Presenter (`app.py`):**
   - Provides a clean, responsive web interface built using Streamlit.
   - Renders metric KPI cards, summary tables, confusion matrix (classification), residual error metrics (regression), session run history, and JSON/CSV report downloads (`FR-08`, `FR-11`, `FR-13`).

---

## 2. Formal Architectural Deviations (8-Point Engineering Analysis)

### Deviation DEV-01: Ephemeral Browser Session State vs. Multi-Tenant User Database

1. **Original Requirement:**
   - Baseline SRS conditionally noted `FR-12` and `SEC-04` ("If user accounts are implemented, the system shall prevent a user from viewing another user's restricted run...").
2. **Actual Implementation:**
   - The application is implemented as an ephemeral, single-user session web application using Streamlit's `st.session_state`. No database, user accounts, password authentication, or persistent multi-tenant storage is deployed.
3. **Reason for Change:**
   - The primary objective of the Mini-Project is offline model evaluation, numerical verification, and QA automation. Introducing SQL databases and authentication credentials would add non-essential complexity without improving evaluation fidelity, while violating zero-retention privacy goals.
4. **Technical Impact:**
   - Zero database drivers or migration scripts needed. Run history is retained strictly within the active browser session and garbage-collected on session closure.
5. **Functional Impact:**
   - Users cannot save evaluation runs permanently across browser tab closures without using the JSON/CSV download export feature.
6. **Risk Analysis:**
   - Low risk. Data loss could occur if the user accidentally refreshes their browser before downloading their report.
7. **Mitigation Strategy:**
   - Prominent download export buttons (JSON report, CSV metrics, CSV history log) enable users to export their evaluation runs immediately to local disk.
8. **Approval Status:**
   - **APPROVED** by Project Team & QA Lead. `FR-12` and `SEC-04` are documented as `NOT APPLICABLE` with zero negative grading impact.

---

### Deviation DEV-02: Direct Modular Python Package vs. External REST Daemon

1. **Original Requirement:**
   - Baseline SAD Section 4.5 proposed hypothetical REST endpoints (`POST /api/datasets`, `POST /api/evaluations`, `GET /api/evaluations/{id}`).
2. **Actual Implementation:**
   - The evaluation logic is organized as an independent, modular Python package (`evaluator/`) consumed directly in-process by the Streamlit application and headless pytest test harness.
3. **Reason for Change:**
   - Hosting a separate HTTP REST server (e.g. FastAPI/Flask) alongside Streamlit introduces inter-process communication overhead, port collisions, and complex deployment coordination. Direct module invocation eliminates network serialization latency.
4. **Technical Impact:**
   - Latency for evaluating 10,000 samples dropped to $< 80\text{ ms}$. Automated testing can execute purely headlessly without starting background daemon processes.
5. **Functional Impact:**
   - Streamlit UI interacts directly with `evaluator.engine.EvaluationRun` in-memory. External systems can still import `evaluator` directly as a standard Python package.
6. **Risk Analysis:**
   - Low risk. If a third-party client desires a REST API in the future, `evaluator/` can be wrapped in a thin FastAPI controller without altering any computational or validation logic.
7. **Mitigation Strategy:**
   - Strict architectural decoupling: `evaluator/` has 0 imports of Streamlit or presentation dependencies.
8. **Approval Status:**
   - **APPROVED** by Technical Lead & Project Team.

---

### Deviation DEV-03: Pre-Computed Tabular Predictions vs. On-Device Model Serialization

1. **Original Requirement:**
   - Baseline SRS Section 1.2 stated: "The project team must confirm whether the actual application evaluates uploaded prediction files, loads serialized models, calls a training/inference pipeline, or uses another mechanism."
2. **Actual Implementation:**
   - The evaluator ingests tabular CSV files containing paired ground truth reference labels and model predictions ($y_{\text{true}}$ and $\hat{y}$).
3. **Reason for Change:**
   - Ingesting arbitrary serialized model files (`.pkl`, `.joblib`, `.h5`, `.onnx`) introduces severe arbitrary code execution vulnerabilities (`SEC-03`) and requires massive runtime dependencies (PyTorch, TensorFlow, XGBoost). Tabular prediction evaluation provides universal compatibility across any ML framework.
4. **Technical Impact:**
   - Memory footprint remains strictly $< 100\text{ MB}$. Prevents arbitrary Python bytecode execution (`pickle` security vulnerability).
5. **Functional Impact:**
   - Practitioners run their models offline in their native environments and upload the resulting predictions CSV for standardized, unbiased evaluation.
6. **Risk Analysis:**
   - Negligible risk. Tabular prediction evaluation is the standard evaluation paradigm for Kaggle, GLUE, and enterprise MLOps validation suites.
7. **Mitigation Strategy:**
   - Provide standard sample datasets (`sample_data/classification_sample.csv`, `sample_data/regression_sample.csv`) and clear documentation of expected column schemas.
8. **Approval Status:**
   - **APPROVED** by ML Engine Lead & Project Team.

---

### Deviation DEV-04: Strict In-Memory Streaming vs. Local Disk Upload Retention

1. **Original Requirement:**
   - Baseline SAD Section 2.5 suggested optional file storage under controlled server disk paths (`/uploads/`).
2. **Actual Implementation:**
   - Uploaded CSV bytes are streamed directly from `BytesIO` memory buffers into Pandas DataFrames. Zero temporary or cached files are written to host disk storage.
3. **Reason for Change:**
   - Writing user files to disk creates path traversal vulnerabilities (`SV-04`), disk filling risks (`SEC-01`), and data privacy compliance concerns (`NFR-07`).
4. **Technical Impact:**
   - Enhanced I/O throughput; zero disk cleanup daemon required; immune to symlink and directory traversal attacks.
5. **Functional Impact:**
   - Dataset uploads exist solely in memory for the duration of the evaluation and session.
6. **Risk Analysis:**
   - Memory consumption could spike if file sizes were unbounded.
7. **Mitigation Strategy:**
   - Enforce strict 10 MB upload ceiling via `validate_file_size()` before allocating memory for full DataFrame parsing.
8. **Approval Status:**
   - **APPROVED** by Security & QA Lead.

---

## 3. Development Freeze Declaration

- **Freeze Date:** 3 November 2026
- **Status:** Development officially frozen for Part-2 submission.
- **Scope Verified:** All Sprint 1 (Issues #1 to #6) and Sprint 2 (Issues #7 to #10) features fully implemented and verified against the Definition of Done.
- **Verification Evidence:**
  - 124 automated unit and integration tests passing with 100% pass rate in 1.48–1.75 seconds.
  - Zero PEP 8 errors (`flake8`).
  - Zero Python compilation errors (`py_compile`).
  - GitHub Actions CI configured with multi-version matrix (Python 3.10, 3.11, 3.12).
- **Target Tag:** `v1.0.0-part2-freeze` on merge to `main`.
