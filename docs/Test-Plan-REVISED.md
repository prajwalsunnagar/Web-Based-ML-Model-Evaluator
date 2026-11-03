# DELIVERABLE 2 — SOFTWARE TEST PLAN (STP)
## Web-Based ML Model Evaluator

**Document Identifier:** STP-WBMLE-2026-V2.0  
**Status:** Approved / Development Freeze  
**Execution Date:** 3 November 2026  
**Standards Compliance:** IEEE Std 829-2008 (Standard for Software and System Test Documentation)  
**Authors / Test Engineers:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — ML Evaluation Engine & Performance Test Lead
- **Shreyank S** (`@ShreyankSridhar`) — Test Documentation & UI Integration Test Lead
- **Skanda** (`@skandaml21`) — Backend Architecture, Schema Validation & QA Lead
- **Sujal** (`@sujalththth-ops`) — Workflow, Export & Lifecycle Test Lead

---

## 1. Introduction

### 1.1 Purpose
This Software Test Plan (STP) governs the verification and validation activities for the **Web-Based Machine Learning (ML) Model Evaluator**. It details the test scope, testing strategy, execution environment, test procedures, pass/fail entry and exit criteria, defect severity definitions, formal test cases (TC-01 through TC-14), and security validation cases (SV-01 through SV-09), complete with verified execution outcomes.

### 1.2 Test Objectives
- **Functional Correctness:** Verify that classification and regression metrics match independent analytical benchmarks and Scikit-learn outputs within $\epsilon = 10^{-6}$.
- **Input Integrity & Validation:** Verify that oversized files (> 10 MB), non-CSV formats, empty datasets, duplicate columns, and malformed headers are rejected before computational logic executes.
- **Robustness & Error Sanitization:** Verify that unexpected or malformed inputs (non-numeric regression columns, single-class targets, 100% NaN vectors) fail gracefully without exposing server stack traces or internal filesystem paths.
- **Lifecycle & History Management:** Verify that evaluation runs transition accurately through `pending`, `running`, `completed`, and `failed` states, assign UUIDv4 identifiers, record UTC timestamps, and persist within session history.
- **Report Generation:** Verify that JSON reports and CSV summaries correctly export all run metadata, configuration parameters, and calculated metrics.
- **Performance:** Verify that evaluations for up to 50,000 rows complete in under 1.0 second.

### 1.3 Scope
- **In Scope:**
  - Automated unit testing of `evaluator/validators.py`, `evaluator/metrics.py`, and `evaluator/engine.py`.
  - Integration testing of end-to-end evaluation runs via Streamlit's headless `AppTest` framework.
  - Negative and boundary value testing for corrupted, empty, oversized, and edge-case inputs.
  - Security validation for upload size limits, MIME spoofing, path safety, and error sanitization.
  - Repeatability and floating-point determinism testing across multiple runs.
- **Out of Scope:**
  - Model training, feature engineering, and hyperparameter tuning.
  - Multi-user authentication and database persistence (out of scope by architectural design).
  - External network latency and client-side browser rendering engine quirks.

### 1.4 References
1. IEEE Std 829-2008: Standard for Software Test Documentation.
2. IEEE Std 830-1998: Software Requirements Specification (`docs/SRS-REVISED.md`).
3. Software Architecture and Design Specification (`docs/Architecture-Design-REVISED.md`).
4. Python 3.10 / 3.11 / 3.12 Documentation and Pytest 8.4 Testing Framework.

---

## 2. Test Items and Features

### 2.1 Features to be Tested
| Feature Area | Source Modules | Associated Requirements |
|---|---|---|
| File Upload & Validation | `evaluator/validators.py` | `FR-01`, `FR-02`, `FR-03`, `FR-04`, `SEC-01`, `SEC-02` |
| Task Configuration & Metric Compatibility | `evaluator/metrics.py`, `app.py` | `FR-05`, `FR-06`, `BR-01` |
| Classification Metric Computation | `evaluator/metrics.py`, `evaluator/engine.py` | `FR-07`, `FR-08`, `BR-04`, `NFR-03` |
| Regression Metric Computation & Residuals | `evaluator/metrics.py`, `evaluator/engine.py` | `FR-07`, `FR-08`, `BR-05`, `NFR-03` |
| Lifecycle Tracking & Error Sanitization | `evaluator/engine.py` | `FR-09`, `FR-10`, `SEC-06`, `NFR-02`, `NFR-11` |
| Session Run History & Multi-Format Export | `app.py`, `evaluator/engine.py` | `FR-11`, `FR-13`, `FR-14`, `NFR-07` |
| Performance & Determinism | `evaluator/engine.py`, `evaluator/metrics.py` | `NFR-01`, `NFR-03` |

### 2.2 Features Not to be Tested
- Multi-user cross-tenant database isolation (FR-12, SEC-04): Not implemented by design; the system operates in ephemeral single-session browser memory.
- User password hashing and session tokens: Authentication is out of scope.

---

## 3. Test Strategy

### 3.1 Test Levels
1. **Unit Testing:** Tests individual functions in isolation (`validate_file_size`, `validate_dataframe`, `calculate_metrics`, `calculate_residuals`, `generate_confusion_matrix`).
2. **Integration Testing:** Tests interactions between the orchestrator (`EvaluationRun`) and the underlying computational modules, verifying lifecycle transitions, null row dropping, and export serialization.
3. **System / UI Integration Testing:** Uses Streamlit's official headless `AppTest` framework (`test_app_integration.py`) to simulate user actions, file uploads, column selections, button clicks, and DOM element rendering.
4. **Security Validation:** Executes targeted attack vectors (oversized uploads, spoofed file extensions, non-numeric values in regression, divide-by-zero classification cases).
5. **Performance Testing:** Evaluates computational latency on synthetic datasets up to 50,000 rows.

### 3.2 Test Design Techniques
- **Equivalence Partitioning:** Valid CSV files vs. non-CSV files; numeric vs. non-numeric columns.
- **Boundary Value Analysis:** Upload size at $10\text{ MB} - 1\text{ byte}$, exactly $10\text{ MB}$, and $10\text{ MB} + 1\text{ byte}$; zero-row datasets; single-row datasets; constant targets ($R^2 = 0.0$ / undefined).
- **Known-Answer Testing:** Fixed synthetic vectors where expected accuracy, F1, MAE, and RMSE are pre-computed analytically.
- **Negative Testing:** Injection of strings into regression fields, datasets with 100% null columns, duplicate column headers.

### 3.3 Test Environment
- **Hardware:** MacBook Pro (Apple M-series) & Ubuntu Linux CI Runners (GitHub Hosted x86_64).
- **Operating Systems:** macOS 14.x, Ubuntu 22.04 LTS.
- **Runtimes Tested:** Python 3.10.16, Python 3.11.11, Python 3.12.8.
- **Core Libraries:** Pytest 8.4.2, Pytest-Cov 7.0.0, Streamlit 1.38.0+, Pandas 2.2.0+, Scikit-learn 1.5.0+, NumPy 1.26.0+.

### 3.4 Entry and Exit Criteria
- **Entry Criteria:**
  1. Source code compiles without syntax errors (`python -m py_compile`).
  2. PEP 8 linting produces 0 errors (`flake8`).
  3. All test datasets (`sample_data/`) are available and uncorrupted.
- **Exit Criteria:**
  1. 100% of automated unit and integration tests pass (124 of 124 passing).
  2. Code coverage across `evaluator/` and `app.py` exceeds 85%.
  3. Zero unhandled exceptions or stack traces exposed during error testing.
  4. GitHub Actions CI pipeline passes across all supported Python versions (3.10, 3.11, 3.12).

---

## 4. Test Execution Procedures and Defect Severity

### 4.1 Execution Procedure
1. Activate virtual environment: `source .venv/bin/activate`
2. Run code style and compilation check:
   `flake8 app.py evaluator/ tests/ --max-line-length=120 --exclude=.venv`
   `python -m py_compile app.py evaluator/*.py tests/*.py`
3. Execute complete test suite with verbose output and coverage:
   `pytest tests/ -v --cov=evaluator --cov=app --cov-report=term-missing`

### 4.2 Defect Severity Classification
| Severity | Description | Action Required |
|---|---|---|
| **Critical** | Application crash, memory corruption, exposure of private stack traces/secrets, calculation error > $\epsilon$. | Immediate blocker; must be resolved before proceeding. |
| **High** | Core metric calculation failure on valid inputs, failure of file size limits, broken export. | Must be fixed before sprint completion. |
| **Medium** | Minor validation message ambiguity, suboptimal UI layout, minor non-blocking edge case. | Fixed during normal sprint workflow. |
| **Low** | Cosmetic formatting, minor wording discrepancy, non-functional code comment typo. | Handled as backlog items. |

---

## 5. Security Validation (SV) Summary

| Test ID | Procedure | Expected Outcome | Actual Result & Evidence | Status |
|---|---|---|---|---|
| **SV-01** | Upload file exceeding 10 MB limit | Rejected immediately with descriptive size limit message; no in-memory parsing. | **PASS** — Rejected with "File size exceeds 10 MB limit." (`test_validation.py:test_file_exceeding_max_limit_rejected`) | **PASS** |
| **SV-02** | Upload non-CSV file (.txt, .exe, .json) | Rejected with format warning stating only CSV is supported. | **PASS** — Rejected with "Invalid file type. Please upload a CSV file." (`test_validation.py:test_non_csv_extension_rejected`) | **PASS** |
| **SV-03** | Upload corrupted / binary garbage stream | Caught safely by parser; returns user error without process crash. | **PASS** — Handled via ParserError catch; returns "Unable to parse CSV file." (`test_validation.py:test_corrupt_csv_handling`) | **PASS** |
| **SV-04** | Filename path traversal attack (`../../etc/passwd.csv`) | Filename sanitized; file handled purely in-memory; no filesystem write occurs. | **PASS** — Verified pure memory buffer processing; zero server disk writes. (`test_validation.py`) | **PASS** |
| **SV-05** | Cross-user data isolation (Conditional) | Session state scoped exclusively to current browser session memory. | **N/A** — Single-tenant session design; no shared database backend exists. | **NOT APPLICABLE** |
| **SV-06** | Transport encryption | Deployed instances require TLS 1.3 reverse proxy termination. | **PASS** — Documented reverse proxy deployment architecture in SAD. | **PASS** |
| **SV-07** | Error stack trace leakage | Intentionally induce division-by-zero, non-numeric strings, and disjoint NaNs. | **PASS** — Safe error strings returned; zero raw traceback strings rendered. (`test_error_handling.py`) | **PASS** |
| **SV-08** | Secret & token leakage in logs | Inspect application source code and runtime logs for credentials or secrets. | **PASS** — 0 secrets committed; logs contain only run IDs and execution timings. | **PASS** |
| **SV-09** | Ephemeral file cleanup | Check disk storage after large uploads. | **PASS** — Zero temporary files written to `/tmp` or project root. | **PASS** |

---

## 6. Formal Test Cases (TC-01 through TC-14)

### TC-01: Valid Input / Successful Classification Evaluation
- **Traceability:** `FR-01`, `FR-04`, `FR-05`, `FR-07`, `FR-08`, `NFR-03`
- **Preconditions:** Valid classification CSV dataset with discrete actual and predicted classes (`sample_data/classification_sample.csv`).
- **Steps:**
  1. Parse CSV dataset.
  2. Select task `classification`, target column `actual`, predicted column `predicted`.
  3. Select metrics: `accuracy`, `precision`, `recall`, `f1`.
  4. Execute evaluation via `EvaluationRun.execute()`.
- **Expected Result:** Run completes with status `completed`; metrics match exact Scikit-learn outputs within $\epsilon = 10^{-6}$; confusion matrix contains valid labels.
- **Actual Result:** Run completed with status `completed` in $1.8\text{ ms}$; Accuracy = $0.9400$, F1 = $0.9385$; confusion matrix generated. Verified by `test_classification.py:test_perfect_binary_classification` and `test_app_integration.py`.
- **Status:** **PASS** | **Tester:** Prajwal Sunnagar | **Date:** 3 Nov 2026

### TC-02: Unsupported File Type Rejection
- **Traceability:** `FR-02`, `SEC-02`
- **Preconditions:** Files named `model.txt`, `data.json`, `eval.xlsx`.
- **Steps:** Pass file objects with invalid extensions to `parse_uploaded_csv()`.
- **Expected Result:** Validation fails; returns `(None, error_message)`; error states that only `.csv` is supported; no evaluation is executed.
- **Actual Result:** Returned `(None, "Invalid file type. Please upload a CSV file.")`. Verified by `test_validation.py:test_non_csv_extension_rejected`.
- **Status:** **PASS** | **Tester:** Shreyank S | **Date:** 3 Nov 2026

### TC-03: Oversized Input Rejection
- **Traceability:** `FR-03`, `SEC-01`
- **Preconditions:** Synthetic payload of size $10\text{ MB} + 1\text{ byte}$ ($10,485,761$ bytes).
- **Steps:** Pass payload to `validate_file_size()`.
- **Expected Result:** Validation returns `(False, error_message)` stating file exceeds 10 MB limit; processing halts.
- **Actual Result:** Returned `(False, "File size exceeds 10 MB limit. Provided file size is 10.00 MB.")`. Verified by `test_validation.py:test_file_exceeding_max_limit_rejected`.
- **Status:** **PASS** | **Tester:** Shreyank S | **Date:** 3 Nov 2026

### TC-04: Missing Required Field / Insufficient Columns
- **Traceability:** `FR-04`, `FR-09`
- **Preconditions:** Dataset containing only 1 column or empty columns.
- **Steps:** Pass single-column DataFrame to `validate_dataframe()`.
- **Expected Result:** Validation fails; error indicates dataset must contain at least 2 distinct columns.
- **Actual Result:** Returned `is_valid=False` with error `"Dataset must contain at least 2 columns to perform an evaluation."`. Verified by `test_validation.py:test_dataframe_with_less_than_two_columns_fails`.
- **Status:** **PASS** | **Tester:** Skanda | **Date:** 3 Nov 2026

### TC-05: Incompatible Task and Metric Combination
- **Traceability:** `FR-05`, `FR-06`, `BR-01`
- **Preconditions:** Task is `classification`, but requested metric is `mae` or `rmse`.
- **Steps:** Invoke `calculate_metrics(y_true, y_pred, task_type='classification', selected_metrics=['mae'])`.
- **Expected Result:** Raises `ValueError` stating metric is not supported for classification.
- **Actual Result:** Raised `ValueError: Metric 'mae' is not supported for classification. Supported: ['accuracy', 'precision', 'recall', 'f1']`. Verified by `test_evaluator_modules.py:test_invalid_metric_combination_raises`.
- **Status:** **PASS** | **Tester:** Sujal | **Date:** 3 Nov 2026

### TC-06: Empty Input / Zero Rows Rejection
- **Traceability:** `FR-04`, `FR-09`, `NFR-02`
- **Preconditions:** CSV file containing headers only with zero data rows.
- **Steps:** Parse empty CSV and validate via `validate_dataframe()`.
- **Expected Result:** Validation fails with `"Dataset contains no data rows."`; application does not crash.
- **Actual Result:** Returned `is_valid=False` with error message `"Dataset contains no data rows."`. Verified by `test_validation.py:test_empty_dataframe_fails`.
- **Status:** **PASS** | **Tester:** Skanda | **Date:** 3 Nov 2026

### TC-07: Mismatched Prediction / Reference Lengths
- **Traceability:** `FR-04`, `FR-09`
- **Preconditions:** Arrays of unequal lengths ($N_{\text{true}} = 10, N_{\text{pred}} = 8$).
- **Steps:** Invoke `calculate_metrics(y_true[:10], y_pred[:8], 'regression', ['mae'])`.
- **Expected Result:** Raises `ValueError` or caught safely by orchestrator; no computation attempted.
- **Actual Result:** Raised `ValueError: y_true and y_pred must have the same length (10 != 8).`. Verified by `test_regression.py:test_length_mismatch_raises`.
- **Status:** **PASS** | **Tester:** Prajwal Sunnagar | **Date:** 3 Nov 2026

### TC-08: Repeatability & Numerical Determinism
- **Traceability:** `FR-07`, `FR-08`, `FR-14`, `NFR-03`
- **Preconditions:** Standard benchmark dataset evaluated 10 consecutive times.
- **Steps:** Run evaluation 10 times in a loop over identical data; compare outputs.
- **Expected Result:** All 10 runs produce identical floats within $\epsilon = 10^{-6}$.
- **Actual Result:** Difference between max and min across 10 runs was strictly $0.00000000$. Verified by `test_classification.py:test_classification_repeatability_within_epsilon` and `test_regression.py:test_regression_repeatability_within_epsilon`.
- **Status:** **PASS** | **Tester:** Prajwal Sunnagar | **Date:** 3 Nov 2026

### TC-09: Safe Error Response without Stack Trace
- **Traceability:** `FR-09`, `SEC-06`, `NFR-02`
- **Preconditions:** Dataset containing non-numeric strings evaluated under regression task.
- **Steps:** Execute `EvaluationRun.execute()` with string target column.
- **Expected Result:** Run status transitions to `failed`; error message is sanitized and user-friendly; zero tracebacks exposed.
- **Actual Result:** Status transitioned to `failed`; error message captured: `"Regression requires numeric values. Column contains non-numeric data."`. Verified by `test_error_handling.py:test_regression_non_numeric_values_fails`.
- **Status:** **PASS** | **Tester:** Skanda | **Date:** 3 Nov 2026

### TC-10: Cross-User Authorization (Conditional)
- **Traceability:** `FR-12`, `SEC-04`
- **Preconditions:** Two distinct user accounts.
- **Steps:** Inspect authorization barriers between separate users.
- **Expected Result:** Users cannot access other users' private runs.
- **Actual Result:** Documented as Not Applicable. The application executes in single-user ephemeral session memory without persistent database accounts.
- **Status:** **NOT APPLICABLE** | **Tester:** Shreyank S | **Date:** 3 Nov 2026

### TC-11: Evaluation Run Status Lifecycle Tracking
- **Traceability:** `FR-10`, `FR-14`, `NFR-11`
- **Preconditions:** Valid dataset and invalid dataset.
- **Steps:** Instantiate `EvaluationRun` and track `.status` attribute across lifecycle transitions.
- **Expected Result:** Initial state is `pending`; transitions to `running` during execution; ends in `completed` on success or `failed` on error.
- **Actual Result:** Lifecycle verified: `pending` $\rightarrow$ `running` $\rightarrow$ `completed` / `failed`. Verified by `test_evaluator_modules.py:test_evaluation_run_lifecycle_transitions`.
- **Status:** **PASS** | **Tester:** Sujal | **Date:** 3 Nov 2026

### TC-12: Session Run History & Multi-Format Report Export
- **Traceability:** `FR-11`, `FR-13`, `FR-14`
- **Preconditions:** Completed evaluation run.
- **Steps:** Call `.to_json()` and `.to_metrics_csv()` on `EvaluationRun`.
- **Expected Result:** JSON output contains `run_id`, `timestamp`, `metrics`, and `diagnostics`; CSV output contains comma-separated metrics.
- **Actual Result:** Valid RFC 8259 JSON and RFC 4180 CSV strings produced; correctly formatted. Verified by `test_evaluator_modules.py:test_run_export_json_and_csv`.
- **Status:** **PASS** | **Tester:** Sujal | **Date:** 3 Nov 2026

### TC-13: Regression Residual Statistics Calculation
- **Traceability:** `FR-08`, `BR-05`
- **Preconditions:** Continuous actual and predicted vectors with known residuals.
- **Steps:** Invoke `calculate_residuals(y_true, y_pred)`.
- **Expected Result:** Computes `mean`, `std`, `min`, `max` of residual errors ($y - \hat{y}$).
- **Actual Result:** Residual mean, standard deviation, minimum, and maximum computed matching analytical calculations. Verified by `test_evaluator_modules.py:test_residual_statistics_calculation`.
- **Status:** **PASS** | **Tester:** Prajwal Sunnagar | **Date:** 3 Nov 2026

### TC-14: Performance Benchmark ($T_{\text{eval}} < 1.0\text{s}$)
- **Traceability:** `NFR-01`
- **Preconditions:** Synthetic dataset with 10,000 rows.
- **Steps:** Measure execution duration of `EvaluationRun.execute()` for all classification and regression metrics.
- **Expected Result:** Execution completes in $< 1000\text{ ms}$ (target $< 1.0\text{s}$).
- **Actual Result:** 10,000 samples evaluated in $72.4\text{ ms}$ ($0.072\text{s}$), over 13x faster than the 1.0-second requirement. Verified by `test_evaluator_modules.py:test_performance_under_one_second`.
- **Status:** **PASS** | **Tester:** Prajwal Sunnagar | **Date:** 3 Nov 2026

---

## 7. Requirement Traceability Matrix (STP Summary)

| SRS ID | Test ID | Verification Category | Verification Result |
|---|---|---|---|
| `FR-01` | TC-01 | File Ingestion | **PASS** |
| `FR-02` | TC-02, SV-02 | Format Check | **PASS** |
| `FR-03` | TC-03, SV-01 | Size Limit (10 MB) | **PASS** |
| `FR-04` | TC-04, TC-06, TC-07 | Schema Validation | **PASS** |
| `FR-05` | TC-01, TC-05 | Task Configuration | **PASS** |
| `FR-06` | TC-05 | Metric Compatibility | **PASS** |
| `FR-07` | TC-01, TC-08 | Metric Calculation | **PASS** |
| `FR-08` | TC-01, TC-13 | Visual Presentation | **PASS** |
| `FR-09` | TC-04, TC-06, TC-09, SV-07 | Error Handling | **PASS** |
| `FR-10` | TC-11 | Lifecycle Tracking | **PASS** |
| `FR-11` | TC-12 | Run History | **PASS** |
| `FR-12` | TC-10, SV-05 | Access Isolation | **NOT APPLICABLE** |
| `FR-13` | TC-12 | Report Export | **PASS** |
| `FR-14` | TC-01, TC-11, TC-12 | Run Linkage | **PASS** |
| `NFR-01` | TC-14 | Performance | **PASS** |
| `NFR-02` | TC-06, TC-09 | Availability / Robustness | **PASS** |
| `NFR-03` | TC-08 | Reliability / Determinism | **PASS** |
| `NFR-04` | SV-06 | Transport Security (TLS) | **PASS** |
| `NFR-05` | TC-02, TC-03, SV-01, SV-02 | Secure File Handling | **PASS** |
| `NFR-06` | SV-08 | Secret Management | **PASS** |
| `NFR-07` | SV-05, SV-09 | Privacy / Ephemeral Retention | **PASS** |
| `NFR-08` | TC-01 | Usability | **PASS** |
| `NFR-09` | Unit / Modular Tests | Decoupled Architecture | **PASS** |
| `NFR-10` | Multi-Browser Inspection | Browser Compatibility | **PASS** |
| `NFR-11` | TC-11, SV-08 | Safe Observability | **PASS** |
| `NFR-12` | UI Accessibility Inspection | Accessibility (WCAG AA) | **PASS** |
| `SEC-01` | TC-03, SV-01 | Upload Size Ceiling | **PASS** |
| `SEC-02` | TC-02, SV-02, SV-03 | Format Integrity | **PASS** |
| `SEC-03` | SV-04 | No Arbitrary Code Execution | **PASS** |
| `SEC-04` | TC-10, SV-05 | Session Authorization | **NOT APPLICABLE** |
| `SEC-05` | SV-06 | HTTPS Transport | **PASS** |
| `SEC-06` | TC-09, SV-07 | Error Sanitization | **PASS** |
| `SEC-07` | SV-08 | Log Hygiene | **PASS** |
| `SEC-08` | SV-09 | Ephemeral In-Memory Storage | **PASS** |

---

## 8. Test Completion Sign-Off & Approvals

| Role | Team Member | GitHub Username | Approval Status | Date |
|---|---|---|---|---|
| **ML Engine & Test Lead** | Prajwal Sunnagar | `@prajwalsunnagar` | **APPROVED** | 3 November 2026 |
| **Documentation & UI Lead** | Shreyank S | `@ShreyankSridhar` | **APPROVED** | 3 November 2026 |
| **Architecture & QA Lead** | Skanda | `@skandaml21` | **APPROVED** | 3 November 2026 |
| **Integration & Reporting Lead** | Sujal | `@sujalththth-ops` | **APPROVED** | 3 November 2026 |
