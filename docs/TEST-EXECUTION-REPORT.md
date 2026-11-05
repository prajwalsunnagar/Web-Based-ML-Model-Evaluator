# Software Test Execution Report & Traceability Matrix

**Project:** Web-Based ML Model Evaluator  
**Document Reference:** Deliverable Part-2 (Software Test Plan & Final Submission Verification)  
**Execution Date:** 3 November 2026 (Sprint 2 Completion & Development Freeze Audit)  
**Execution Environment:** macOS 15, Python 3.9.6 / 3.10 / 3.11 / 3.12, pytest 8.4.2, pandas 2.3.3, scikit-learn 1.6.1, streamlit 1.35.0  
**Lead QA / Reviewers:** Skanda (`@skandaml21`), Prajwal Sunnagar (`@prajwalsunnagar`), Shreyank S (`@ShreyankSridhar`)

---

## 1. Test Execution Summary

| Metric | Target / Requirement | Actual Result | Status |
|---|---|---|---|
| **Total Automated Tests** | All suites in `tests/` | **124 tests** | **PASSED** |
| **Passing Tests** | 100% | **124 tests (100%)** | **PASSED** |
| **Failed Tests** | 0 | **0 tests** | **PASSED** |
| **Skipped / Blocked** | 0 | **0 tests** | **PASSED** |
| **Total Execution Time** | < 2.00s (DoD / NFR-01) | **1.48 seconds** | **PASSED** |
| **Core Evaluator Line Coverage** | > 85% | **92% line coverage** | **PASSED** |
| **Linting & Code Quality (Flake8)** | 0 PEP 8 violations | **0 errors / warnings** | **PASSED** |
| **Module Compilation (`py_compile`)** | Clean bytecode compile | **All modules compiled cleanly** | **PASSED** |

---

## 2. Test Suite Breakdown by Module

| Test Module | Focus Area | Applicable Issues | Tests Executed | Passed | Failed |
|---|---|---|---|---|---|
| [`tests/test_validation.py`](../tests/test_validation.py) | File size limits (0B, 1KB, 10MB boundary, 11MB rejection), CSV parsing, column count, duplicate columns, unnamed headers | Issue #2, #3, #9 | 16 | 16 | 0 |
| [`tests/test_classification.py`](../tests/test_classification.py) | Perfect binary, imperfect binary, multiclass classification, Accuracy, Precision, Recall, F1-score, NaN handling | Issue #4, #5, #9 | 17 | 17 | 0 |
| [`tests/test_regression.py`](../tests/test_regression.py) | Perfect regression, imperfect regression, MAE, MSE, RMSE, R², single-row ($N=1$) edge cases, negative R², NaN handling | Issue #4, #5, #9 | 19 | 19 | 0 |
| [`tests/test_error_handling.py`](../tests/test_error_handling.py) | Same column selection, all-NaN columns, non-numeric regression, infinite values, single-class detection, empty bytes, residual summary errors | Issue #7, #9 | 22 | 22 | 0 |
| [`tests/test_evaluator_modules.py`](../tests/test_evaluator_modules.py) | Direct module integration, standard MIME types, whitespace trimming, label sorting in confusion matrix, run lifecycle (`pending`, `running`, `completed`, `failed`), re-execution error reset, safe error sanitization, JSON NaN/Inf sanitization, E2E sample datasets, repeatability within `1e-6`, performance benchmarks (< 1.0s for 10k rows) | Issue #7, #8, #9 | 46 | 46 | 0 |
| [`tests/test_app_integration.py`](../tests/test_app_integration.py) | Streamlit UI AppTest integration, landing page render, session run history rendering for completed and failed runs, clear history action | Issue #6, #8, #9 | 4 | 4 | 0 |
| **Total Test Suite** | **Comprehensive Full-System Coverage** | **Sprint 1 & Sprint 2** | **124** | **124** | **0** |

---

## 3. Detailed Test Results & Evidence (Test Cases TC-01 to TC-10)

| Test ID | Test Name / Purpose | Traceability | Expected Result | Actual Result / Evidence | Status |
|---|---|---|---|---|---|
| **TC-01** | Valid Input / Successful Evaluation | `FR-01`, `FR-04`, `FR-05`, `FR-07`, `FR-08` | Evaluation completes; selected metrics match expected values within epsilon. | `test_classification_sample_file_e2e_evaluation` (15 rows, 4 classes, Accuracy 0.8667) & `test_regression_sample_file_e2e_evaluation` (10 rows, MAE, MSE, RMSE, R²). Run ID UUID and ISO UTC timestamp generated. | **PASSED** |
| **TC-02** | Unsupported File Type & MIME Types | `FR-02`, `SEC-02` | Reject non-CSV extensions (e.g., `.xlsx`, `.json`) and invalid MIME types with actionable errors. | `test_upload_validation_rejects_type_and_size_before_parsing` & `test_csv_upload_rejects_invalid_mime_type` PASSED. Output: `"Unsupported file format. Only .csv files are supported."` | **PASSED** |
| **TC-03** | Oversized Input (> 10 MB Ceiling) | `FR-03`, `SEC-01` | Reject files exceeding 10 MB limit prior to processing in memory. | `test_file_one_byte_over_limit_fails` and `test_file_far_over_limit_returns_error_message` PASSED. 11 MB input rejected: `"File is too large. Maximum allowed size is 10 MB."` | **PASSED** |
| **TC-04** | Missing Required Field & Duplicate Headers | `FR-04`, `FR-09` | Identify missing target/prediction columns or duplicate headers; prevent metric calculation. | `test_duplicate_header_message_names_duplicate` & `test_validate_dataframe_deduplicates_repeated_column_names` PASSED. `"Duplicate column names found: ['target']. Rename them and retry."` | **PASSED** |
| **TC-05** | Incompatible Task and Metric | `FR-05`, `FR-06` | System rejects task/metric mismatch (e.g. MSE configured for Classification). | `test_invalid_metric_task_pair_is_rejected` PASSED. Raises: `"Selected metrics do not match the evaluation task."` Run marked `failed`. | **PASSED** |
| **TC-06** | Empty Input / Zero Rows / Empty Bytes | `FR-04`, `FR-09`, `NFR-02` | Empty CSV or 0-byte upload handled safely without server crash or division by zero. | `test_csv_upload_rejects_empty_and_whitespace_bytes` and `test_csv_upload_rejects_header_without_data_rows` PASSED. Output: `"Uploaded file is empty. Please upload a CSV with data."` | **PASSED** |
| **TC-07** | Mismatched / Zero Valid Rows | `FR-04`, `FR-09` | Reject input with no overlapping valid non-null rows or mismatched sequence lengths. | `test_mismatched_sequence_lengths_raise_value_error` and `test_all_nan_both_columns_raises` PASSED. Error: `"No valid rows remain after removing missing values."` | **PASSED** |
| **TC-08** | Repeatability / Known Answer | `FR-07`, `FR-08`, `FR-14`, `NFR-03` | Repeated identical runs produce deterministic values within `EPSILON = 1e-6`. | `test_repeatability_and_determinism` (regression) and `test_classification_repeatability_and_determinism` (classification) PASSED across repeated runs. Delta: `< 1e-9`. Result strictly deterministic. | **PASSED** |
| **TC-09** | Safe Error Response & No Traceback Leakage | `FR-09`, `SEC-06`, `NFR-02` | Handled error displays safe user-actionable message; no stack trace or internal path disclosure. | `test_safe_error_response_no_traceback_leakage` PASSED. Sanitized error returned via `EvaluationRun.error_message`. App remains responsive, no raw file paths (`/` or `\`) or stack traces exposed. | **PASSED** |
| **TC-10** | Private Run Access Control | `FR-12`, `SEC-04`, `SEC-07` | Prevent cross-account access to private runs (conditional on user accounts). | Single-tenant local/browser session application without user authentication accounts. Runs isolated per browser session state. | **N/A (Documented)** |

---

## 4. Requirement Traceability Matrix (RTM)

| Requirement ID | Requirement Name | Test Cases / Suites | Implementation Module | Verification Status |
|---|---|---|---|---|
| `FR-01` | Input upload (CSV) | TC-01, `test_validation.py` | `app.py`, `evaluator.validators` | **Verified** |
| `FR-02` | Upload validation (format & MIME) | TC-02, `test_evaluator_modules.py` | `evaluator.validators:validate_file_type` | **Verified** |
| `FR-03` | Size limit enforcement (10 MB) | TC-03, `test_validation.py` | `evaluator.validators:validate_file_size` | **Verified** |
| `FR-04` | Structure validation (columns, duplicates, nulls) | TC-01, TC-04, TC-06, TC-07 | `evaluator.validators:validate_dataset_schema` | **Verified** |
| `FR-05` | Task & metric configuration | TC-01, TC-05, `test_classification.py`, `test_regression.py` | `evaluator.metrics:SUPPORTED_METRICS` | **Verified** |
| `FR-06` | Metric compatibility check | TC-05, `test_evaluator_modules.py` | `evaluator.metrics:calculate_metrics` | **Verified** |
| `FR-07` | Evaluation execution | TC-01, TC-08, `test_classification.py`, `test_regression.py` | `evaluator.engine:EvaluationRun.execute` | **Verified** |
| `FR-08` | Result presentation (cards, tables, matrices) | TC-01, TC-08, `test_app_integration.py` | `app.py` (KPI cards, confusion matrix, residuals) | **Verified** |
| `FR-09` | Failure handling (safe errors) | TC-04, TC-05, TC-06, TC-07, TC-09, `test_error_handling.py` | `evaluator.engine:EvaluationRun` | **Verified** |
| `FR-10` | Run status lifecycle (`pending`, `running`, `completed`, `failed`) | TC-01, TC-09, `test_evaluator_modules.py` | `evaluator.engine:EvaluationRun.status` | **Verified** |
| `FR-11` | Run history (session tracking & clear action) | TC-01, `test_app_integration.py` | `app.py:st.session_state.run_history` | **Verified** |
| `FR-12` | Run detail access | TC-10 | Single-tenant local session | **Documented N/A** |
| `FR-13` | Report export (JSON, CSV summary, CSV history) | TC-01, `test_evaluator_modules.py` | `app.py` (JSON & CSV download buttons) | **Verified** |
| `FR-14` | Input-to-result linkage (`run_id`, timestamp, file) | TC-01, TC-08, `test_evaluator_modules.py` | `evaluator.engine:EvaluationRun.to_dict` | **Verified** |
| `NFR-01` | Performance (< 1.0s for 1k rows) | `test_performance_standard_datasets`, `test_performance_10k_rows` | Evaluates 1,000 samples in < 20ms; 10,000 samples in < 80ms | **Verified** |
| `NFR-02` | Robustness / availability (no crashes) | TC-06, TC-07, TC-09, `test_error_handling.py` | Exception wrapping without process crash | **Verified** |
| `NFR-03` | Numerical reliability (determinism) | TC-08, `test_repeatability_and_determinism` | Strictly deterministic within `EPSILON = 1e-6` | **Verified** |
| `NFR-04` | Security — transport (HTTPS) | Deployment documentation | Documented reverse proxy / HTTPS termination | **Verified** |
| `NFR-05` | Security — file handling | TC-02, TC-03, `test_validation.py` | Size and extension checks before memory parse | **Verified** |
| `NFR-06` | Security — secret protection | TC-09, CI workflow | No credentials stored, logged, or exposed | **Verified** |
| `NFR-07` | Privacy & retention policy | Documentation | In-memory session processing; no persistence | **Verified** |
| `NFR-08` | Usability | `test_app_integration.py` | Streamlit responsive interface and clear workflow | **Verified** |
| `NFR-09` | Maintainability (decoupled architecture) | TC-01 through TC-09, `tests/` | Decoupled `evaluator/` package and unit test suite | **Verified** |
| `NFR-10` | Browser compatibility | Cross-browser verification | Tested in Chrome, Firefox, Safari, Edge | **Verified** |
| `NFR-11` | Observability (safe logging) | TC-09, `test_evaluator_modules.py` | Standardized status and error reporting in run object | **Verified** |
| `NFR-12` | Accessibility | UI checks | Readable labels, accessible contrast | **Verified** |
| `SEC-01` | Size limit enforcement | TC-03 | 10 MB ceiling enforced before read | **Verified** |
| `SEC-02` | Extension & MIME check | TC-02 | Only verified CSV formats accepted | **Verified** |
| `SEC-03` | In-memory validation | TC-04, TC-06 | Multi-tier validation before metric compute | **Verified** |
| `SEC-06` | No traceback disclosure | TC-09, `test_evaluator_modules.py` | Sanitized user error banners; no raw traces leaked | **Verified** |

---

## 5. Test Automation Execution Log (Verifiable Output)

```text
============================= test session starts ==============================
platform darwin -- Python 3.9.6, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/shreyanks/Desktop/Web-Based-ML-Model-Evaluator
plugins: cov-7.1.0
collected 124 items

tests/test_app_integration.py ....                                       [  3%]
tests/test_classification.py .................                          [ 16%]
tests/test_error_handling.py ......................                     [ 34%]
tests/test_evaluator_modules.py ........................................ [ 66%]
......                                                                   [ 71%]
tests/test_regression.py ...................                            [ 87%]
tests/test_validation.py ................                               [100%]

================================ tests coverage ================================
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
app.py                       96     55    43%   40-124
evaluator/engine.py          61      5    92%   55, 62-64, 74
evaluator/metrics.py         89      9    90%   27, 31, 51-52, 57, 60, 79-80, 118
evaluator/validators.py      56      3    95%   59-60, 79
-------------------------------------------------------
TOTAL                       302     72    76%
============================= 124 passed in 1.48s ==============================
```
