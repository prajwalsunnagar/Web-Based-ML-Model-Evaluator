# Web-Based ML Model Evaluator

## 1. Project Overview

The **Web-Based ML Model Evaluator** is a web-based system designed to provide a structured platform for evaluating Machine Learning models.

The project evaluates predictions supplied in a CSV; it does not load or run trained model files. Users upload actual and predicted values, select classification or regression metrics, and view results. The application maintains session-scoped run history, assigns each run a unique UUID and UTC timestamp, and provides multi-format export downloads (JSON evaluation report, CSV metrics summary, and CSV run history).

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
5. Automated unit & integration test suite (124 tests, 100% pass rate)
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
│   ├── SRS.docx                  # Software Requirements Specification
│   ├── Architecture-Design.docx  # Architecture and Design Document
│   ├── Test-Plan.docx            # Test Plan
│   ├── SPRINT-PLAN.md            # Agile sprint plan & user stories
│   ├── PART2_DELIVERABLE_AUDIT.md# Part-2 deliverables audit matrix
│   ├── TEST-EXECUTION-REPORT.md  # Test results & Requirement Traceability Matrix
│   ├── DEVIATIONS-AND-NOTES.md   # Architectural alignment & design decisions
│   ├── sprint-1-deviations.md    # Verified document compliance & Sprint 1 deviations
│   ├── DEMO_CHECKLIST.md         # Sprint demo outlines & video release checklists
│   ├── demo/                     # Sprint demo assets and scripts
│   │   ├── sprint-1-narration-script.md # 60-second narration script & checklist
│   │   └── sprint-2-narration-script.md # 120-second narration script & checklist
│   └── demo_videos/              # Sprint video demo target directory
│
├── tests/                        # Automated unit and integration test suites
│   ├── conftest.py               # Shared pytest fixtures
│   ├── test_validation.py        # File and column validation tests
│   ├── test_classification.py    # Classification metric tests
│   ├── test_regression.py        # Regression metric tests
│   ├── test_error_handling.py    # Error path and edge case tests
│   ├── test_evaluator_modules.py # Evaluator service & end-to-end sample tests
│   └── test_app_integration.py   # Streamlit UI integration tests (AppTest)
│
├── scripts/                      # Automation & sync scripts
│   └── update_github_backlog.py  # GitHub issues updater script
│
└── .github/
    ├── pull_request_template.md  # Standard PR review template
    └── workflows/
        └── ci.yml                # GitHub Actions CI multi-version pipeline (lint, build, test)
```

---

## 6. Project Documentation

### Software Requirements Specification
The SRS documents system requirements, project scope, functional requirements (`FR-01` to `FR-14`), non-functional requirements (`NFR-01` to `NFR-12`), constraints, and business rules.
- [View SRS](docs/SRS.docx)

### Architecture and Design
The Architecture and Design document describes the proposed layered web architecture, major components, system interactions, data flow, and design decisions.
- [View Architecture Design](docs/Architecture-Design.docx)

### Test Plan & Test Execution Report
The Test Plan defines the testing approach, test objectives, scenarios, test cases (TC-01 through TC-10), and expected results. The Test Execution Report documents verified execution evidence and the Requirement Traceability Matrix (RTM).
- [View Test Plan](docs/Test-Plan.docx)
- [View Test Execution Report & Traceability Matrix](docs/TEST-EXECUTION-REPORT.md)

### Agile Sprint Plan & Backlog
The Sprint Plan defines the delivery milestones, Fibonacci story point scale, team allocations, Definition of Done, demonstration requirements, and detailed user stories for all 10 GitHub backlog issues across Sprint 1 and Sprint 2.
- [View Sprint Plan](docs/SPRINT-PLAN.md)

### Part 2 Deliverables Audit & Traceability
The Deliverables Audit details the complete verification checklist across all Part-2 requirements, remote vs. local analysis, GitHub project setup instructions, and milestone deliverables.
- [View Part-2 Deliverable Audit](docs/PART2_DELIVERABLE_AUDIT.md)

### Architectural Alignment & Deviations
Documents the alignment of the implementation with SAD Section 4.1/4.2, single-tenant local scoping, and the formal development freeze declaration.
- [View Deviations & Architecture Notes](docs/DEVIATIONS-AND-NOTES.md)

### Demonstration Checklists & Video Scripts
Provides 60-second (Sprint 1) and 120-second (Sprint 2) timestamped walkthrough outlines, pre-demo setup steps, video upload guidelines, and narration scripts.
- [View Demo Checklists](docs/DEMO_CHECKLIST.md)
- [View Sprint 1 Demo Narration Script](docs/demo/sprint-1-narration-script.md)
- [View Sprint 2 Demo Narration Script](docs/demo/sprint-2-narration-script.md)

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

### Run the Automated Test Suite with Coverage
```bash
pytest tests/ -v --tb=short --cov=evaluator --cov=app --cov-report=term-missing
```

### Test Suite Breakdown (124 Tests, 100% Pass Rate):
- **File & Upload Validation (`test_validation.py` - 16 tests):** File format (.csv), MIME types (`text/csv`, `application/x-csv`, etc.), 10 MB ceiling, 0-byte/empty bytes rejection, duplicate column detection, and dataframe validation.
- **Classification Engine (`test_classification.py` - 17 tests):** Binary and multiclass accuracy, precision, recall, F1-score with weighted/macro/micro averaging, binary positive class selection, and NaN handling.
- **Regression Engine (`test_regression.py` - 19 tests):** MAE, MSE, RMSE, R² calculation, signed residual summaries, $N < 2$ single-row edge cases, and NaN dropping.
- **Robustness & Error Handling (`test_error_handling.py` - 22 tests):** Same column guard, non-numeric regression inputs, infinite values, single-class detection, column count guards, empty upload bytes, and residual summary error handling.
- **Evaluator Modules & Lifecycle (`test_evaluator_modules.py` - 46 tests):** Upload validation, header whitespace stripping, natural confusion matrix sorting, run lifecycle states (`pending`, `running`, `completed`, `failed`), error state reset on re-execution, safe error responses without traceback leakage, JSON export NaN/Inf sanitization, end-to-end evaluation on committed sample datasets, repeatability within `1e-6`, and performance benchmarks (< 1.0s for 1,000 and 10,000 rows).
- **Streamlit UI Integration (`test_app_integration.py` - 4 tests):** Application launch and landing page rendering, session run history rendering for completed and failed runs, and clear history action.

---

## 11. CI/CD & Testing Status

- **Automated Tests:** 124 automated tests passing with 100% pass rate.
- **Execution Time:** ~1.5 seconds locally and in CI (< 2.0s requirement).
- **Evaluator Line Coverage:** >90% line coverage on core business logic (`evaluator/`).
- **GitHub Actions Pipeline:** Configured in `.github/workflows/ci.yml` across Python 3.10, 3.11, and 3.12 with concurrency controls. Each workflow run executes:
  1. Dependency installation (`requirements.txt` + `requirements-dev.txt`)
  2. Flake8 PEP 8 linting
  3. Python module compilation check
  4. Pytest test suite with line-by-line coverage reporting

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
