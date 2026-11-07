# Web-Based ML Model Evaluator

## 1. Project Overview

The **Web-Based ML Model Evaluator** is a web-based system designed to provide a structured platform for evaluating Machine Learning models.

The project evaluates predictions supplied in a CSV; it does not load or run trained model files. Users upload actual and predicted values, select classification or regression metrics, and view evaluation results.

The application includes CSV upload validation, file-size and format checks, duplicate and invalid header detection, dataset structure validation, and validation of selected actual and predicted columns. It also checks that both selected columns contain at least one overlapping non-empty row before evaluation.

The application maintains session-scoped run history, assigns each run a unique UUID and UTC timestamp, and provides multi-format export downloads (JSON evaluation report, CSV metrics summary, and CSV run history).

The project follows a structured software engineering approach covering requirements analysis, system architecture, implementation, automated testing, and continuous integration.

---

## 2. Project Objectives

The main objectives of the project are:

- Provide a web-based platform for Machine Learning model evaluation.
- Provide a user-friendly interface for interacting with the system.
- Support evaluation of Machine Learning models using appropriate evaluation metrics.
- Present evaluation results in a clear and understandable manner.
- Define a structured software architecture for the system.
- Document functional and non-functional requirements.
- Define a systematic testing approach for the application.
- Maintain consistency between requirements, architecture, and testing documentation.

---

## 3. Project Scope

The project focuses on the design and development of a web-based Machine Learning model evaluation system.

The project documentation covers:

- System requirements
- User interaction and system workflow
- Dataset and model evaluation
- Performance evaluation metrics
- System architecture
- Functional and non-functional requirements
- Testing strategy and test cases
- Project documentation

---

## 4. Key Deliverables

The major project deliverables are:

1. Software Requirements Specification (SRS)
2. Architecture and Design Document (SAD)
3. Test Plan & Execution Report
4. Web-Based ML Model Evaluator application
5. Automated unit & integration test suite (132 tests, 100% pass rate)
6. Supporting agile project documentation & sprint demo narration scripts

---

## 5. Repository Structure

```
Web-Based-ML-Model-Evaluator/
│
├── app.py                        # Streamlit interface and result presentation
├── evaluator/                    # CSV validation, metric engine, run lifecycle
│   ├── validators.py             # Upload type, size, header, and dataset checks
│   ├── metrics.py                # Classification and regression calculations
│   └── engine.py                 # Run IDs, status lifecycle, metadata, safe errors
├── requirements.txt              # Core runtime dependencies
├── requirements-dev.txt          # Testing, coverage, and linting tools
├── README.md                     # Project documentation & execution guide
│
├── sample_data/                  # Verification datasets
│   ├── classification_sample.csv # Classification test data (15 rows, 4 classes)
│   └── regression_sample.csv     # Regression test data (10 rows, numeric targets)
│
├── docs/                         # Specifications & deliverables
│   ├── SRS-REVISED.docx          # Revised Software Requirements Specification (IEEE 830)
│   ├── SRS-REVISED.md            # Markdown source for revised SRS
│   ├── Architecture-Design-REVISED.docx # Revised Architecture & Design Specification (IEEE 1016)
│   ├── Architecture-Design-REVISED.md   # Markdown source for revised SAD
│   ├── Test-Plan-REVISED.docx    # Revised Software Test Plan (IEEE 829)
│   ├── Test-Plan-REVISED.md      # Markdown source for revised STP
│   ├── TEST-CASE-DOCUMENT.md     # Standalone Test Case Document (TC-01–TC-14, SV-01–SV-09)
│   ├── UNIT-TEST-REPORT.md       # Comprehensive Unit Test Execution Report
│   ├── SYSTEM-VALIDATION-REPORT.md # End-to-end System Validation Report (IEEE 1012)
│   ├── CODE-COVERAGE-REPORT.md   # Line coverage report (76% project / 92% core engine)
│   ├── BRANCH-COVERAGE-REPORT.md # Branch coverage report (126 branches / 91.1% core engine)
│   ├── REQUIREMENT-TRACEABILITY-MATRIX.md # Standalone Requirement Traceability Matrix
│   ├── TEST-EXECUTION-REPORT.md  # Test results & Requirement Traceability Matrix
│   ├── SPRINT-PLAN.md            # Agile sprint plan, user stories & 40 SP backlog
│   ├── PART2_DELIVERABLE_AUDIT.md# Part-2 deliverables audit matrix
│   ├── DEVIATIONS-AND-NOTES.md   # 8-point architectural deviations & freeze declaration
│   ├── FINAL_REPOSITORY_AUDIT.md # Master audit matrix across Parts 1, 2, and 3
│   ├── FINAL_SUBMISSION_CHECKLIST.md # Academic submission checklist & quality gates
│   ├── FINAL_REMEDIATION_REPORT.md # Summary report of all remediations performed
│   ├── DEMO_CHECKLIST.md         # Sprint demo outlines & video release checklists
│   ├── demo/                     # Sprint demo assets and scripts
│   │   ├── SPRINT-1-RECORDING-GUIDE.md  # 60-second narration script & checklist
│   │   ├── SPRINT-2-RECORDING-GUIDE.md  # 120-second narration script & checklist
│   │   ├── sprint-1-narration-script.md # Baseline Sprint 1 script
│   │   └── sprint-2-narration-script.md # Baseline Sprint 2 script
│   └── demo_videos/              # Sprint video demo target directory
│       └── README.md             # Video recording instructions (pending manual recording)
│
├── htmlcov/                      # HTML Code Coverage reports (generated via pytest-cov)
│   └── index.html                # Interactive browser coverage viewer
│
├── tests/                        # Automated unit and integration test suites
│   ├── conftest.py               # Shared pytest fixtures
│   ├── test_validation.py        # File and column validation tests (16 tests)
│   ├── test_classification.py    # Classification metric tests (17 tests)
│   ├── test_regression.py        # Regression metric tests (20 tests)
│   ├── test_error_handling.py    # Error path and edge case tests (22 tests)
│   ├── test_evaluator_modules.py # Evaluator service & end-to-end sample tests (46 tests)
│   └── test_app_integration.py   # Streamlit UI integration tests (AppTest) (4 tests)
│
├── scripts/                      # Automation & sync scripts
│   ├── md_to_docx.py             # Markdown to DOCX document compiler
│   └── update_github_backlog.py  # GitHub issues updater script
│
└── .github/
    ├── pull_request_template.md  # Standard PR review template
    └── workflows/
        └── ci.yml                # GitHub Actions CI multi-version pipeline (lint, build, test)
```

---

## 6. Project Documentation & Academic Deliverables

### Comprehensive Repository Audit
- [View Final Repository Audit](docs/FINAL_REPOSITORY_AUDIT.md) — Comprehensive audit matrix across all Part 1 and Part 2 deliverables.

### Software Requirements Specification (SRS)
The SRS documents system requirements, project scope, functional requirements (`FR-01` to `FR-14`), non-functional requirements (`NFR-01` to `NFR-12`), security objectives (`SO-01` to `SO-04`), security requirements (`SEC-01` to `SEC-08`), and UML use case model adhering to IEEE Std 830-1998.
- [View Revised SRS (DOCX)](docs/SRS-REVISED.docx) | [View Revised SRS (Markdown)](docs/SRS-REVISED.md)
- [Original Baseline SRS (DOCX)](docs/SRS.docx)

### Software Architecture and Design (SAD)
The Architecture and Design document details the 3-tier modular reactive architecture, component decomposition, four Mermaid sequence and architecture diagrams, security boundaries, and design decisions adhering to IEEE Std 1016-2009.
- [View Revised SAD (DOCX)](docs/Architecture-Design-REVISED.docx) | [View Revised SAD (Markdown)](docs/Architecture-Design-REVISED.md)
- [Original Baseline SAD (DOCX)](docs/Architecture-Design.docx)

### Software Test Plan (STP), Test Cases & RTM
The Test Plan defines the test scope, strategy, test levels, 14 formal test cases (TC-01 through TC-14), 9 security validations (SV-01 through SV-09), and verified execution evidence adhering to IEEE Std 829-2008.
- [View Revised Test Plan (DOCX)](docs/Test-Plan-REVISED.docx) | [View Revised Test Plan (Markdown)](docs/Test-Plan-REVISED.md)
- [View Formal Test Case Document](docs/TEST-CASE-DOCUMENT.md) — Comprehensive positive, negative, boundary & security test specifications.
- [View Requirement Traceability Matrix (RTM)](docs/REQUIREMENT-TRACEABILITY-MATRIX.md)
- [View Test Execution Report](docs/TEST-EXECUTION-REPORT.md)
- [Original Baseline Test Plan (DOCX)](docs/Test-Plan.docx)

### Part 3 Testing & Quality Verification Reports
- [View Unit Test Report](docs/UNIT-TEST-REPORT.md) — Detailed unit test execution logs, module breakdowns, pass counts, and defect resolutions.
- [View System Validation Report](docs/SYSTEM-VALIDATION-REPORT.md) — End-to-end functional (FR-01–14), non-functional (NFR-01–12), and security (SEC-01–08) validation matrix.
- [View Code Coverage Report](docs/CODE-COVERAGE-REPORT.md) — Real statement coverage via pytest-cov: 76% project line coverage, 92% core evaluator package coverage, and 76% vs 87% discrepancy resolution.
- [View Branch Coverage Report](docs/BRANCH-COVERAGE-REPORT.md) — Conditional decision coverage via pytest-cov `--cov-branch`: 126 branches, 91.1% core engine branch coverage, and uncovered path analysis.
- [View Interactive HTML Coverage](htmlcov/index.html) — Local interactive browser coverage viewer.

### Agile Sprint Plan & Backlog
The Sprint Plan defines the delivery milestones, Fibonacci story point scale (40 SP total across Sprint 1 & 2), Definition of Done, user stories for Issues #1 to #10, and GitHub Project Board setup instructions.
- [View Sprint Plan](docs/SPRINT-PLAN.md)
- [View Part-2 Deliverable Audit](docs/PART2_DELIVERABLE_AUDIT.md)

### Architectural Alignment & Formal Deviations
Documents the alignment of the implementation with SAD Section 4.1/4.2, 8-point engineering analysis for deviations, and the formal development freeze declaration.
- [View Deviations & Architecture Notes](docs/DEVIATIONS-AND-NOTES.md)

### Demonstration Guides & Narration Scripts
Provides 60-second (Sprint 1) and 120-second (Sprint 2) timestamped narration scripts, visual screen action tables, and video recording checklists.
- [View Sprint 1 Recording Guide](docs/demo/SPRINT-1-RECORDING-GUIDE.md)
- [View Sprint 2 Recording Guide](docs/demo/SPRINT-2-RECORDING-GUIDE.md)
- [View Demo Checklists & Video Status](docs/DEMO_CHECKLIST.md)
- [View Demo Videos Directory](docs/demo_videos/)

### Final Submission Checklist
- [View Final Submission Checklist](docs/FINAL_SUBMISSION_CHECKLIST.md)

---

## 7. Team Members

| Name | Role |
|------|------|
| Shreyank S | Project Development / Documentation Lead |
| Prajwal Sunnagar | Repository Owner / ML Engine Developer |
| Sujal | Full-Stack Developer / Workflow & Reporting |
| Skanda | Backend Architecture / Schema Validation & QA |

---

## 8. Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ (tested on 3.10, 3.11, 3.12) |
| Web Framework | Streamlit >= 1.35.0 |
| Data Processing | pandas >= 2.2.0, numpy >= 1.26.0 |
| ML Metrics | scikit-learn >= 1.4.0 |
| Testing & Coverage | pytest >= 8.0.0, pytest-cov >= 5.0.0 |
| Code Quality / Linting | flake8 >= 7.0.0 |
| CI/CD | GitHub Actions (Matrix: Python 3.10, 3.11, 3.12) |

---

## 9. Running the Application

### 1. Set up a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt
```

### 3. Start the application

```bash
streamlit run app.py
```

The application will launch and open in your browser at `http://localhost:8501`.

### 4. Upload and evaluate a dataset

1. In the file uploader, upload a valid `.csv` file (e.g., `sample_data/classification_sample.csv` or `sample_data/regression_sample.csv`).
2. Verify the instant upload feedback, file size guard (< 10 MB), and dataset summary preview (Rows, Columns, Missing values, Complete rows).
3. Select the evaluation task (**Classification** or **Regression**).
4. Map the **Actual values column** (ground truth) and **Predicted values column** (model predictions).
5. Select desired metrics (e.g., Accuracy, Precision, Recall, F1-score for classification; MAE, MSE, RMSE, R² for regression).
6. Click **Calculate evaluation metrics** to execute the evaluation run.
7. Inspect the generated KPI metric cards, detailed metrics table, confusion matrix with natural label sorting (classification) or regression residual summary with standard deviation (regression), and session run history.
8. Export results as needed:
   - **Download latest run (JSON):** Full evaluation run metadata, parameters, status, and confusion matrix.
   - **Download metrics summary (CSV):** Computed metric names and rounded values.
   - **Download run history (CSV):** Complete session run history with status, parameters, and errors.
   - **Clear run history:** Reset the session run history via the sidebar action.

---

## 10. Code Quality, Linting & Testing

### Run Code Quality & Lint Checks
```bash
flake8 app.py evaluator/ tests/ --max-line-length=120 --exclude=.venv
```

### Run Build & Compilation Checks
```bash
python3 -m py_compile app.py evaluator/*.py tests/*.py
```

### Run the Automated Test Suite with Line & Branch Coverage
```bash
pytest tests/ -v --tb=short --cov=app --cov=evaluator --cov-branch --cov-report=term-missing --cov-report=html
```

### Test Suite Breakdown (132 Tests, 100% Pass Rate):
- **File & Upload Validation (`test_validation.py` - 16 tests):** File format (.csv), MIME types (`text/csv`, `application/x-csv`, etc.), 10 MB ceiling, 0-byte/empty bytes rejection, duplicate column detection, and dataframe validation.
- **Classification Engine (`test_classification.py` - 17 tests):** Binary and multiclass accuracy, precision, recall, F1-score with weighted/macro/micro averaging, binary positive class selection, and NaN handling.
- **Regression Engine (`test_regression.py` - 20 tests):** MAE, MSE, RMSE, R² calculation, signed residual summaries, $N < 2$ single-row edge cases, and NaN dropping.
- **Robustness & Error Handling (`test_error_handling.py` - 24 tests):** Same column guard, non-numeric regression inputs, infinite values, single-class detection, column count guards, empty upload bytes, and residual summary error handling.
- **Evaluator Modules & Lifecycle (`test_evaluator_modules.py` - 51 tests):** Upload validation, header whitespace stripping, natural confusion matrix sorting, run lifecycle states (`pending`, `running`, `completed`, `failed`), error state reset on re-execution, safe error responses without traceback leakage, JSON export NaN/Inf sanitization, end-to-end evaluation on committed sample datasets, repeatability within `1e-6`, and performance benchmarks (< 1.0s for 1,000 and 10,000 rows).
- **Streamlit UI Integration (`test_app_integration.py` - 4 tests):** Application launch and landing page rendering, session run history rendering for completed and failed runs, and clear history action.

---

## 11. CI/CD & Testing Status

- **Automated Tests:** 132 automated tests passing with 100% pass rate.
- **Execution Time:** ~8.16 seconds locally (132 tests).
- **Application Coverage:** 45% (`app.py`).
- **Evaluator Module Coverage:** Engine 87%, metrics 90%, validators 74%.
- **Overall Project Coverage:** 72% line coverage in the latest local test run.
- **GitHub Actions Pipeline:** Configured in `.github/workflows/ci.yml` across Python 3.10, 3.11, and 3.12 with concurrency controls. Each workflow run executes:
  1. Dependency installation (`requirements.txt` + `requirements-dev.txt`)
  2. Flake8 PEP 8 linting
  3. Python module compilation check
  4. Pytest test suite with line and branch coverage reporting
  5. HTML coverage artifact upload (`actions/upload-artifact@v4`)

---

## 12. Documentation Consistency

The project documentation maintains consistency between:

- Software requirements
- System architecture
- Implementation
- Test cases

Changes to requirements should be reviewed against the Architecture and Design document and the Test Plan to ensure affected components and test cases are updated accordingly.

---

## 13. Academic Project

This project is developed as part of an academic software engineering project.
