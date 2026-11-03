# Software Engineering Mini-Project — Requirement Traceability Matrix (RTM)

**Project Title:** Web-Based ML Model Evaluator  
**Document Identifier:** RTM-WBMLE-2026-V2.0  
**Status:** Approved / Development Freeze  
**Execution Date:** 3 November 2026  
**Repository:** [prajwalsunnagar/Web-Based-ML-Model-Evaluator](https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator)  
**Authors / Reviewers:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — ML Evaluation Engine Lead
- **Shreyank S** (`@ShreyankSridhar`) — Documentation & UI Lead
- **Skanda** (`@skandaml21`) — Backend Architecture & QA Lead
- **Sujal** (`@sujalththth-ops`) — Full-Stack Workflow & Reporting Lead

---

## 1. Traceability Overview

This Requirement Traceability Matrix (RTM) provides forward and backward traceability between the System Requirements (SRS IEEE 830), Backlog Issues (Sprint Plan), Software Architecture & Design (SAD IEEE 1016), Software Test Plan (STP IEEE 829), and concrete automated test execution evidence from our 124-test suite.

---

## 2. Functional Requirements Traceability (FR-01 through FR-14)

| SRS ID | Requirement Name | Backlog Issue # | Implementation Source File & Function | Test Plan ID | Automated Pytest Function(s) | Verification Status |
|---|---|---|---|---|---|---|
| **FR-01** | Input Upload | Issue #1 (Sprint 1) | `app.py:st.file_uploader`, `evaluator/validators.py:parse_uploaded_csv` | TC-01 | `tests/test_validation.py:test_valid_csv_parses_successfully`, `tests/test_app_integration.py:test_app_initial_render` | **PASS** |
| **FR-02** | Upload Validation | Issue #2 (Sprint 1) | `evaluator/validators.py:parse_uploaded_csv` | TC-02, SV-02 | `tests/test_validation.py:test_non_csv_extension_rejected`, `tests/test_validation.py:test_corrupt_csv_handling` | **PASS** |
| **FR-03** | Upload Size Ceiling | Issue #2 (Sprint 1) | `evaluator/validators.py:validate_file_size` | TC-03, SV-01 | `tests/test_validation.py:test_file_exceeding_max_limit_rejected`, `tests/test_error_handling.py:test_11_mb_fails` | **PASS** |
| **FR-04** | Schema & Structure Validation | Issue #3 (Sprint 1) | `evaluator/validators.py:validate_dataframe` | TC-04, TC-06, TC-07 | `tests/test_validation.py:test_empty_df_fails`, `tests/test_validation.py:test_duplicate_columns_fail`, `tests/test_validation.py:test_single_column_df_fails` | **PASS** |
| **FR-05** | Task & Metric Configuration | Issue #4 (Sprint 1) | `app.py`, `evaluator/metrics.py:SUPPORTED_METRICS` | TC-01, TC-05 | `tests/test_evaluator_modules.py:test_supported_metrics_dictionary`, `tests/test_app_integration.py:test_app_initial_render` | **PASS** |
| **FR-06** | Metric Compatibility Enforcement | Issue #4 (Sprint 1) | `evaluator/metrics.py:calculate_metrics` | TC-05 | `tests/test_evaluator_modules.py:test_invalid_metric_combination_raises` | **PASS** |
| **FR-07** | Evaluation Execution | Issue #5 (Sprint 1) | `evaluator/engine.py:EvaluationRun.execute`, `evaluator/metrics.py:calculate_metrics` | TC-01, TC-08 | `tests/test_classification.py:test_perfect_binary_classification`, `tests/test_regression.py:test_perfect_regression` | **PASS** |
| **FR-08** | Result Presentation | Issue #6 (Sprint 1) | `app.py:st.metric`, `evaluator/metrics.py:calculate_residuals`, `generate_confusion_matrix` | TC-01, TC-13 | `tests/test_evaluator_modules.py:test_residual_statistics_calculation`, `tests/test_app_integration.py` | **PASS** |
| **FR-09** | Failure Handling & Safe Errors | Issue #7 (Sprint 2) | `evaluator/engine.py:EvaluationRun.execute` | TC-04, TC-09, SV-07 | `tests/test_error_handling.py:test_regression_non_numeric_values_fails`, `tests/test_evaluator_modules.py:test_safe_error_response_no_traceback_leakage` | **PASS** |
| **FR-10** | Run Status Lifecycle Tracking | Issue #7 (Sprint 2) | `evaluator/engine.py:EvaluationRun.status` | TC-11 | `tests/test_evaluator_modules.py:test_evaluation_run_lifecycle_transitions` | **PASS** |
| **FR-11** | Session Run History | Issue #8 (Sprint 2) | `app.py:st.session_state.run_history`, `evaluator/engine.py:EvaluationRun` | TC-12 | `tests/test_app_integration.py:test_app_session_history_completed_run_render`, `tests/test_app_integration.py:test_app_clear_history_action` | **PASS** |
| **FR-12** | Multi-Tenant Run Isolation | Conditional | Single-tenant ephemeral session memory | TC-10, SV-05 | Documented Not Applicable (No shared multi-tenant database) | **NOT APPLICABLE** |
| **FR-13** | Multi-Format Report Export | Issue #8 (Sprint 2) | `evaluator/engine.py:to_json`, `to_metrics_csv`, `app.py:st.download_button` | TC-12 | `tests/test_evaluator_modules.py:test_run_export_json_and_csv`, `tests/test_evaluator_modules.py:test_json_export_round_trip` | **PASS** |
| **FR-14** | Input-to-Result Linkage | Issue #8 (Sprint 2) | `evaluator/engine.py:EvaluationRun.to_dict` | TC-01, TC-11, TC-12 | `tests/test_evaluator_modules.py:test_evaluation_run_uuid_and_timestamp_generation`, `tests/test_evaluator_modules.py:test_evaluation_run_to_metrics_dataframe` | **PASS** |

---

## 3. Non-Functional Requirements Traceability (NFR-01 through NFR-12)

| SRS ID | Quality Attribute | Target Threshold | Implementation Source | Test Plan ID | Automated Pytest Function / Verification Method | Verification Status |
|---|---|---|---|---|---|---|
| **NFR-01** | Performance | $T_{\text{eval}} \le 1.0\text{s}$ for up to 50,000 rows | Vectorized NumPy / Scikit-learn algorithms | TC-14 | `tests/test_evaluator_modules.py:test_performance_10k_rows` (10,000 rows in $0.072\text{s}$) | **PASS** |
| **NFR-02** | Robustness & Availability | Zero server crashes on dirty/invalid inputs | `evaluator/engine.py:EvaluationRun.execute` | TC-06, TC-09 | `tests/test_error_handling.py` (22 comprehensive edge case tests) | **PASS** |
| **NFR-03** | Reliability & Determinism | Repeatability within $\epsilon = 10^{-6}$ | Deterministic Scikit-learn functions | TC-08 | `tests/test_classification.py:test_classification_repeatability_within_epsilon`, `tests/test_regression.py:test_regression_repeatability_within_epsilon` | **PASS** |
| **NFR-04** | Transport Security | TLS 1.3 HTTPS in deployment | SAD Section 2.4 Reverse Proxy architecture | SV-06 | Deployment configuration inspection | **PASS** |
| **NFR-05** | Secure File Handling | In-memory stream parsing, no disk writes | `evaluator/validators.py:parse_uploaded_csv` | TC-02, TC-03, SV-01 | `tests/test_validation.py` (28 file validation tests) | **PASS** |
| **NFR-06** | Secret Management | Zero hardcoded keys or tokens | Clean repository hygiene | SV-08 | `flake8` and repository scan | **PASS** |
| **NFR-07** | Privacy & Retention | Ephemeral memory, discarded upon tab close | `st.session_state` in-memory store | SV-05, SV-09 | Architectural inspection & code review | **PASS** |
| **NFR-08** | Usability | Intuitive guided workflow < 60s | Two-column layout in `app.py` | TC-01 | Sprint 1 & 2 Video Narration Guides | **PASS** |
| **NFR-09** | Maintainability & Modularity | `evaluator/` core has 0 Streamlit imports | `evaluator/` package decoupling | Modular Tests | `tests/test_evaluator_modules.py` (Headless unit execution) | **PASS** |
| **NFR-10** | Browser Compatibility | Chrome, Firefox, Safari evergreen support | Standard HTML/CSS rendered by Streamlit | Multi-Browser | Cross-browser manual verification | **PASS** |
| **NFR-11** | Observability & Logging | Structured metadata without payload leakage | `evaluator/engine.py:EvaluationRun.to_dict` | TC-11, SV-08 | `tests/test_evaluator_modules.py:test_evaluation_run_lifecycle_transitions` | **PASS** |
| **NFR-12** | Accessibility | Semantic widgets, WCAG AA contrast | Native Streamlit form widgets | UI Review | Accessibility walkthrough | **PASS** |

---

## 4. Security Requirements Traceability (SEC-01 through SEC-08)

| SEC ID | Security Requirement | Implementation Source | Test Plan ID | Automated Pytest Function / Verification Method | Status |
|---|---|---|---|---|---|
| **SEC-01** | Upload Size Ceiling (10 MB) | `evaluator/validators.py:validate_file_size` | TC-03, SV-01 | `tests/test_validation.py:test_file_exceeding_max_limit_rejected` | **PASS** |
| **SEC-02** | File Format & MIME Integrity | `evaluator/validators.py:parse_uploaded_csv` | TC-02, SV-02 | `tests/test_validation.py:test_non_csv_extension_rejected` | **PASS** |
| **SEC-03** | No Arbitrary Code Execution | Data-only parsing via Pandas; zero `eval()` | SV-04 | Static AST inspection & code review | **PASS** |
| **SEC-04** | Session Scoping & Access Control | Ephemeral `st.session_state` | TC-10, SV-05 | Documented Not Applicable (Single-tenant session memory) | **NOT APPLICABLE** |
| **SEC-05** | Transport Encryption (HTTPS) | Reverse proxy TLS termination architecture | SV-06 | SAD Section 2.4 deployment specification | **PASS** |
| **SEC-06** | Error Sanitization (Zero Tracebacks) | `evaluator/engine.py:EvaluationRun.execute` | TC-09, SV-07 | `tests/test_evaluator_modules.py:test_safe_error_response_no_traceback_leakage` | **PASS** |
| **SEC-07** | Log Hygiene (No Raw Data Exposure) | Structured run objects (`to_dict()`) | SV-08 | Code review of console output | **PASS** |
| **SEC-08** | Ephemeral Storage (No Disk Lingering) | In-memory byte streaming | SV-09 | Verification that `/tmp` and local disks receive 0 writes | **PASS** |

---

## 5. Traceability Summary Metrics

- **Total Requirements Mapped:** 34 requirements (14 Functional, 12 Non-Functional, 8 Security).
- **Fully Verified & Passing:** 32 requirements (**94.1%**).
- **Documented Not Applicable:** 2 requirements (`FR-12`, `SEC-04` — Single-tenant session architecture by design: **5.9%**).
- **Failing or Blocked Requirements:** 0 requirements (**0.0%**).
- **Automated Test Coverage:** 124 passing automated tests in 1.48–1.75 seconds.
