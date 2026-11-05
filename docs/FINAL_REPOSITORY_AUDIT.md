# Software Engineering Mini-Project — Comprehensive Repository Audit Report

**Project Title:** Web-Based ML Model Evaluator  
**Repository:** [prajwalsunnagar/Web-Based-ML-Model-Evaluator](https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator)  
**Audit Target Branch:** `feature/sprint-2-completion` (Targeting `main` via PR #16)  
**Audit Date:** 3 November 2026  
**Auditor Roles:** Senior Software Engineering Project Auditor, IEEE Documentation Specialist, QA Engineer, Technical Lead  
**Team Members & Roles:**
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — Repository Owner / ML Evaluation Engine Developer
- **Shreyank S** (`@ShreyankSridhar`) — Documentation Lead / UI & Frontend Developer
- **Skanda** (`@skandaml21`) — Backend Architecture / Schema Validation & QA Engineer
- **Sujal** (`@sujalththth-ops`) — Full-Stack Developer / Workflow & Reporting Engineer

---

## 1. Executive Summary

This audit assesses the Web-Based ML Model Evaluator repository against the requirements of the **Software Engineering Mini-Project Deliverables (Part 1 and Part 2)**, the baseline IEEE Software Requirements Specification (SRS), Software Architecture and Design (SAD) document, Software Test Plan, and the two-sprint development plan.

The audit evaluates all software engineering artifacts across:
1. Requirements specification and IEEE alignment.
2. Architecture and design documentation vs. actual system reality.
3. Test planning, execution evidence, and automated test coverage.
4. Sprint backlog management and story point reconciliation.
5. Implementation quality, error handling, session run history, and report export.
6. CI/CD automation pipeline.
7. Demonstration video scripts and recording readiness.
8. Submission checklist compliance and development freeze declaration.

---

## 2. Deliverable Audit Matrix

| Deliverable ID | Academic Deliverable Item | Target Artifact / File Path | Status | Summary of Content & Remediation |
|---|---|---|---|---|
| **DEL-01** | Software Requirements Specification (SRS) | `docs/SRS.docx`, `docs/SRS-REVISED.md`, `docs/SRS-REVISED.docx` | **COMPLETE** | Original `SRS.docx` was a baseline template with placeholders ("TBD", "proposed"). Created revised IEEE 830 compliant version (`docs/SRS-REVISED.md` and `docs/SRS-REVISED.docx`) resolving all thresholds (10 MB upload ceiling, $T_{\text{eval}} < 1.0\text{s}$, $\epsilon = 10^{-6}$), specifying FR-01 through FR-14, NFR-01 through NFR-12, SO-01 through SO-04, SEC-01 through SEC-08, and Mermaid UML use-case diagram. |
| **DEL-02** | Software Test Plan | `docs/Test-Plan.docx`, `docs/Test-Plan-REVISED.md`, `docs/Test-Plan-REVISED.docx` | **COMPLETE** | Original `Test-Plan.docx` had unexecuted test cases with "[Fill after execution]" placeholders. Created revised IEEE 829 document (`docs/Test-Plan-REVISED.md` and `docs/Test-Plan-REVISED.docx`) documenting 14 formal test cases (TC-01 to TC-14) and 9 security validation cases (SV-01 to SV-09) with actual execution results from our 124 passing automated tests. |
| **DEL-03** | Software Architecture & Design (SAD) | `docs/Architecture-Design.docx`, `docs/Architecture-Design-REVISED.md`, `docs/Architecture-Design-REVISED.docx` | **COMPLETE** | Original `Architecture-Design.docx` contained proposed REST endpoints and generic database references that did not exist. Created revised SAD (`docs/Architecture-Design-REVISED.md` and `docs/Architecture-Design-REVISED.docx`) accurately documenting Streamlit single-process reactive architecture, decoupled `evaluator` package, 4 detailed Mermaid diagrams (architecture, upload validation, classification sequence, regression sequence), and security trust boundaries. |
| **DEL-04** | Sprint 1 & 2 Planning & Backlog | `docs/SPRINT-PLAN.md` | **COMPLETE** | Defines 10 backlog issues (#1 to #10) mapped to 40 Story Points across Sprint 1 (22 SP) and Sprint 2 (18 SP), using standard Fibonacci sizing and balanced team allocations. |
| **DEL-05** | Sprint 1 Video Demonstration | `docs/demo/SPRINT-1-RECORDING-GUIDE.md`, `docs/demo_videos/sprint1_demo.mp4` | **NEEDS MANUAL ACTION** | Created a comprehensive 1-minute recording guide with second-by-second narration script, visual actions, and setup instructions. Video recording file is pending actual physical screen capture by the team; placeholder directory `docs/demo_videos/` maintained with `.gitkeep` and clear notes. |
| **DEL-06** | Working Implementation (Sprint 1 & 2) | `app.py`, `evaluator/validators.py`, `evaluator/metrics.py`, `evaluator/engine.py` | **COMPLETE** | Full evaluation workflow operational for Classification and Regression. Sprint 2 features completed: structured run status lifecycle (`pending`, `running`, `completed`, `failed`), UUIDv4 run IDs, session run history, multi-format exports (JSON report, CSV metrics summary, CSV history), residual statistics (std dev), natural label sorting, and sanitized user-facing error messages without stack trace leakage. |
| **DEL-07** | Automated Test Suites | `tests/test_validation.py`, `tests/test_classification.py`, `tests/test_regression.py`, `tests/test_error_handling.py`, `tests/test_evaluator_modules.py`, `tests/test_app_integration.py` | **COMPLETE** | 124 comprehensive automated unit and integration tests covering all validation, classification, regression, error handling, session state, and AppTest UI flows. 100% pass rate in 1.48 seconds. |
| **DEL-08** | Continuous Integration Pipeline | `.github/workflows/ci.yml` | **COMPLETE** | Multi-version CI matrix testing Python 3.10, 3.11, and 3.12 on pushes and PRs to `main`. Executes PEP 8 linting (`flake8`), bytecode compilation (`py_compile`), and automated testing (`pytest`) with branch-level coverage enforcement. |
| **DEL-09** | Test Execution Report | `docs/TEST-EXECUTION-REPORT.md` | **COMPLETE** | Updated with fresh execution evidence from the 124-test suite, execution times, coverage statistics (87% across `app.py` and `evaluator/`), and environmental metadata. |
| **DEL-10** | Requirement Traceability Matrix (RTM) | `docs/REQUIREMENT-TRACEABILITY-MATRIX.md` | **COMPLETE** | Standalone RTM linking every SRS requirement (FR-01 to FR-14, NFR-01 to NFR-12, SEC-01 to SEC-08) to its GitHub Backlog Issue, implementation file, test case ID, and automated test function. |
| **DEL-11** | Architectural Deviations Document | `docs/DEVIATIONS-AND-NOTES.md` | **COMPLETE** | Updated using strict 8-point engineering format (Original requirement, Actual implementation, Reason for change, Technical impact, Functional impact, Risk analysis, Mitigation strategy, Approval status) for all deviations from baseline proposals. |
| **DEL-12** | GitHub Project Board | GitHub Projects v2 (Organization/User level) | **NEEDS MANUAL ACTION** | GitHub Projects v2 requires personal access tokens with user-level scopes or manual browser interaction. Detailed step-by-step setup guide with custom fields and issue mapping is documented in `docs/SPRINT-PLAN.md` and `docs/PART2_DELIVERABLE_AUDIT.md`. |
| **DEL-13** | Sprint 2 Video Demonstration | `docs/demo/SPRINT-2-RECORDING-GUIDE.md`, `docs/demo_videos/sprint2_demo.mp4` | **NEEDS MANUAL ACTION** | Comprehensive 2-minute narration script with time-coded cues (0:00 to 2:00) provided in `docs/demo/SPRINT-2-RECORDING-GUIDE.md`. Actual MP4 video file pending physical recording; no fake video files committed. |
| **DEL-14** | Deliverable Audit & Verification | `docs/PART2_DELIVERABLE_AUDIT.md` | **COMPLETE** | Reconciled story point allocation from 43 SP to canonical 40 SP (removing phantom Issue #12), aligned backlog assignees, and confirmed all Sprint 2 acceptance criteria. |
| **DEL-15** | Final Submission Checklist & Freeze | `docs/FINAL_SUBMISSION_CHECKLIST.md` | **COMPLETE** | Complete verification of all Part 1 and Part 2 submission deliverables, team member roles, Git branch hygiene, and formal development freeze declaration. |

---

## 3. Detailed Audit Findings & Remediation Summary

### 3.1 Requirements Specification (SRS)
- **Original State:** `docs/SRS.docx` was generated as an initial project baseline. It contained multiple "TBD" flags regarding supported formats, upload size limits ($M_{\text{UPLOAD}}$), maximum row counts ($N_{\text{ROWS}}$), evaluation timeout thresholds ($T_{\text{EVAL}}$), and hypothetical user authentication.
- **Issues Identified:**
  - $M_{\text{UPLOAD}}$, $N_{\text{ROWS}}$, and $T_{\text{EVAL}}$ were unquantified.
  - Multi-tenant user login and access control (FR-12, SEC-04) were proposed but not applicable to our lightweight, privacy-preserving, single-session browser architecture.
  - No UML use-case diagram was rendered in text-accessible form.
- **Remediation Performed:**
  - Authored `docs/SRS-REVISED.md` and compiled `docs/SRS-REVISED.docx` complying with IEEE 830 standard.
  - Quantified all measurable thresholds: $M_{\text{UPLOAD}} = 10\text{ MB}$, $N_{\text{ROWS}} = 50,000\text{ rows}$, $T_{\text{EVAL}} \le 1.0\text{s}$, $\epsilon = 10^{-6}$.
  - Clearly documented FR-12 and SEC-04 as single-tenant session scoped (N/A for multi-user authentication).
  - Included a Mermaid UML use-case diagram modeling core user interactions.
  - Distinguished Security Objectives (SO-01 to SO-04) from testable Security Requirements (SEC-01 to SEC-08).

### 3.2 Software Architecture & Design (SAD)
- **Original State:** `docs/Architecture-Design.docx` contained speculative REST API endpoints (`/api/datasets`, `/api/evaluations`) and a hypothetical database repository layer.
- **Issues Identified:**
  - Real implementation is a Python Streamlit application with in-memory DataFrame processing and session state, not a separate client/server REST architecture.
  - Missing actual sequence diagrams reflecting the Streamlit execution model and modular engine orchestration.
- **Remediation Performed:**
  - Authored `docs/Architecture-Design-REVISED.md` and compiled `docs/Architecture-Design-REVISED.docx`.
  - Documented the real 3-tier logical architecture (Presentation Layer `app.py`, Evaluation Orchestrator `evaluator/engine.py`, Validation & Metric Engines `evaluator/validators.py` and `evaluator/metrics.py`).
  - Added four detailed Mermaid diagrams:
    1. Overall Application Architecture.
    2. CSV Upload and Schema Validation Workflow.
    3. Classification Evaluation Sequence.
    4. Regression Evaluation Sequence.
  - Documented trust boundaries, error sanitization, ephemeral session data handling, and reverse proxy deployment pattern.

### 3.3 Software Test Plan & Execution Evidence
- **Original State:** `docs/Test-Plan.docx` contained 10 proposed test cases with placeholder values ("[Fill after execution]") and no verified execution evidence.
- **Issues Identified:**
  - Test cases were unexecuted in the specification document.
  - Did not reflect the full automated test suite or cover Sprint 2 features (run history, report export, residual statistics).
- **Remediation Performed:**
  - Authored `docs/Test-Plan-REVISED.md` and compiled `docs/Test-Plan-REVISED.docx` following IEEE 829.
  - Documented 14 comprehensive test cases (TC-01 through TC-14) and 9 security validation cases (SV-01 through SV-09).
  - Populated all Actual Results, Statuses (100% PASS / N/A), Execution Dates, and Test Case Evidence linked directly to automated pytest functions.
  - Updated `docs/TEST-EXECUTION-REPORT.md` with complete 124-test execution breakdown and coverage statistics.

### 3.4 Backlog & Story Point Reconciliation
- **Original State:** `docs/SPRINT-PLAN.md` defined 40 Story Points across 10 backlog issues. However, `docs/PART2_DELIVERABLE_AUDIT.md` listed a total of 43 Story Points due to a duplicate attribution of 3 story points to `@skandaml21`.
- **Issues Identified:** Discrepancy between documentation files (40 SP vs. 43 SP).
- **Remediation Performed:**
  - Reconciled `docs/PART2_DELIVERABLE_AUDIT.md` and `docs/SPRINT-PLAN.md` to canonical **40 Story Points**:
    - **Sprint 1 (22 SP):** Issues #1 (3 SP), #2 (3 SP), #3 (3 SP), #4 (5 SP), #5 (5 SP), #6 (3 SP).
    - **Sprint 2 (18 SP):** Issues #7 (5 SP), #8 (5 SP), #9 (5 SP), #10 (3 SP).
    - **Member Allocations:** Prajwal (13 SP), Shreyank (9 SP), Skanda (8 SP), Sujal (10 SP).

### 3.5 Demonstration Videos
- **Current State:** Video recording scripts exist for Sprint 1 and Sprint 2. Physical MP4 video recordings are pending manual screencast capture by the student team.
- **Remediation Performed:**
  - Created `docs/demo/SPRINT-1-RECORDING-GUIDE.md` (1-minute script) and `docs/demo/SPRINT-2-RECORDING-GUIDE.md` (2-minute script) with exact second-by-second cues.
  - Set up `docs/demo_videos/` with `.gitkeep` and a clear README indicating video status is PENDING manual recording.
  - Strictly avoided committing fabricated MP4 files.

---

## 4. Remaining Manual Actions for Team Members

| # | Action Item | Responsible Team Member | Instructions |
|---|---|---|---|
| 1 | **Create GitHub Project Board** | Prajwal Sunnagar (`@prajwalsunnagar`) | Follow the step-by-step instructions in `docs/PART2_DELIVERABLE_AUDIT.md` to create `Web-Based ML Model Evaluator Board`, add custom fields (`Sprint`, `Story Points`, `Status`), and link Issues #1 to #10. |
| 2 | **Record Sprint 1 Demo Video** | Shreyank S / Prajwal Sunnagar | Follow `docs/demo/SPRINT-1-RECORDING-GUIDE.md` to record the 1-minute video; export to `docs/demo_videos/sprint1_demo.mp4`. |
| 3 | **Record Sprint 2 Demo Video** | Shreyank S / Skanda / Sujal | Follow `docs/demo/SPRINT-2-RECORDING-GUIDE.md` to record the 2-minute video; export to `docs/demo_videos/sprint2_demo.mp4`. |
| 4 | **PR Review & Merge** | Team | Review PR #16 on GitHub and merge `feature/sprint-2-completion` into `main` after video attachments are finalized. |

---

## 5. Auditor Sign-Off & Submission Readiness Verdict

- **Code Quality:** Passed (Zero PEP 8 errors, zero syntax errors, 124 passing unit/integration tests).
- **CI Status:** Passed (GitHub Actions green across Python 3.10, 3.11, 3.12).
- **Documentation:** Complete & IEEE 830 / IEEE 829 Compliant.
- **Traceability:** Complete (100% of SRS requirements traceable to implementation and automated test cases).
- **Submission Readiness Verdict:** **READY FOR FINAL SUBMISSION** (subject only to manual video recording and GitHub Project Board linking).

