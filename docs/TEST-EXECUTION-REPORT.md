# Software Test Execution Report & Traceability Matrix

**Project:** Web-Based ML Model Evaluator  
**Document Reference:** Deliverable 2 & 4 (Software Test Plan & Final Submission Checklist)  
**Execution Date:** 12 October 2026  
**Execution Environment:** macOS 15, Python 3.9.6, pytest 8.4.2, pandas 2.3.3, scikit-learn 1.6.1  
**Lead Tester / Reviewer:** Skanda (`@skandaml21`) & Shreyank (`@ShreyankSridhar`)

---

## 1. Test Execution Summary

| Total Test Cases | Passed | Failed | Blocked / Skipped | Overall Pass Rate |
|---|---|---|---|---|
| **10** | **9 (Automated)** | **0** | **1 (TC-10 N/A)** | **100% (of applicable)** |

---

## 2. Detailed Test Results & Evidence

| Test ID | Test Name / Purpose | Traceability | Expected Result | Actual Result / Evidence | Status |
|---|---|---|---|---|---|
| **TC-01** | Valid Input / Successful Evaluation | `FR-01`, `FR-04`, `FR-05`, `FR-07`, `FR-08` | Evaluation completes; selected metrics match expected values within epsilon. | `test_tc01_classification_evaluation` & `test_tc01_regression_evaluation` PASSED. Accuracy: 0.8, MAE: 2.0, MSE: 4.5. Run ID generated. | **PASSED** |
| **TC-02** | Unsupported File Type | `FR-02`, `SEC-02` | Reject non-CSV files (e.g., `.xlsx`, `.json`) with an actionable validation error. | `test_tc02_unsupported_file_type` PASSED. Output: `"Unsupported file format. Only .csv files are supported."` | **PASSED** |
| **TC-03** | Oversized Input | `FR-03`, `SEC-01` | Reject files exceeding 10 MB limit prior to processing. | `test_tc03_oversized_file` PASSED. 11 MB input rejected: `"exceeds maximum allowed limit of 10 MB."` | **PASSED** |
| **TC-04** | Missing Required Field | `FR-04`, `FR-09` | Identify missing target/prediction columns; prevent metric calculation. | `test_tc04_missing_required_column` PASSED. Error returned: `"Target (ground truth) column 'ground_truth' is not present in the dataset."` | **PASSED** |
| **TC-05** | Incompatible Task and Metric | `FR-05`, `FR-06` | System rejects task/metric mismatch (e.g. MSE for classification). | `test_tc05_incompatible_task_metric` PASSED. Run marked `failed` with safe error response. | **PASSED** |
| **TC-06** | Empty Input / Zero Rows | `FR-04`, `FR-09`, `NFR-02` | Empty CSV handled safely without server crash or division by zero. | `test_tc06_empty_dataset` PASSED. Validated: `"The uploaded CSV dataset is empty (zero data rows)."` | **PASSED** |
| **TC-07** | Mismatched / Zero Valid Rows | `FR-04`, `FR-09` | Reject input with no overlapping valid non-null rows. | `test_tc07_zero_overlapping_valid_rows` PASSED. Error: `"No valid overlapping non-null rows between target and prediction columns."` | **PASSED** |
| **TC-08** | Repeatability / Known Answer | `FR-07`, `FR-08`, `FR-14`, `NFR-03` | Repeated identical runs produce identical values within `EPSILON = 1e-6`. | `test_tc08_repeatability_and_known_answer` PASSED. Delta: `< 1e-9`. Result strictly repeatable. | **PASSED** |
| **TC-09** | Safe Error Response | `FR-09`, `SEC-06`, `NFR-02` | Handled error displays safe message; no stack trace or secret disclosure. | `test_tc09_safe_error_response` PASSED. Error sanitized and returned via `EvaluationRun.error_message`. App remains responsive. | **PASSED** |
| **TC-10** | Private Run Access Control | `FR-12`, `SEC-04`, `SEC-07` | Prevent cross-account access to private runs (conditional on user accounts). | Single-tenant local/browser session application without user authentication accounts. | **N/A (Documented)** |

---

## 3. Requirement Traceability Matrix (RTM)

| Requirement ID | Requirement Name | Test Cases | Implementation Module | Verification Status |
|---|---|---|---|---|
| `FR-01` | Input upload | TC-01 | `app.py`, `evaluator.validators` | Verified |
| `FR-02` | Upload validation | TC-02 | `evaluator.validators:validate_file_type` | Verified |
| `FR-03` | Size limit enforcement | TC-03 | `evaluator.validators:validate_file_size` | Verified |
| `FR-04` | Structure validation | TC-01, TC-04, TC-06, TC-07 | `evaluator.validators:validate_dataset_schema` | Verified |
| `FR-05` | Task & metric configuration | TC-01, TC-05 | `evaluator.metrics:SUPPORTED_METRICS` | Verified |
| `FR-06` | Metric compatibility check | TC-05 | `evaluator.metrics:validate_metric_compatibility` | Verified |
| `FR-07` | Evaluation execution | TC-01, TC-08 | `evaluator.engine:EvaluationRun.execute` | Verified |
| `FR-08` | Result presentation | TC-01, TC-08 | `app.py` (Metric KPI cards, summary table) | Verified |
| `FR-09` | Failure handling | TC-04, TC-05, TC-06, TC-07, TC-09 | `evaluator.engine:EvaluationRun` | Verified |
| `FR-10` | Run status | TC-01, TC-09 | `evaluator.engine:EvaluationRun.status` | Verified |
| `FR-11` | Run history | TC-01 | `app.py:st.session_state.run_history` | Verified |
| `FR-12` | Run detail access | TC-10 | N/A (Single-tenant web app) | Documented N/A |
| `FR-13` | Report export | TC-01 | `app.py` (JSON & CSV download) | Verified |
| `FR-14` | Input-to-result linkage | TC-01, TC-08 | `evaluator.engine:EvaluationRun.to_dict` | Verified |
| `NFR-01` | Performance | TC-01, TC-08 | Evaluates 1,000 samples in < 50ms | Verified |
| `NFR-02` | Robustness / availability | TC-06, TC-07, TC-09 | Exception wrapping without process crash | Verified |
| `NFR-03` | Numerical reliability | TC-08 | Deterministic within `EPSILON = 1e-6` | Verified |
| `NFR-05` | Security file handling | TC-02, TC-03 | Size and extension checks before parse | Verified |
| `NFR-06` | Secret protection | TC-09 | No credentials stored or logged | Verified |
| `NFR-09` | Maintainability | TC-01 through TC-09 | Clean separation of `evaluator/` from UI | Verified |
