# Web-Based ML Model Evaluator

## 1. Project Overview

The **Web-Based ML Model Evaluator** is a web-based system designed to provide a structured platform for evaluating Machine Learning models.

The project evaluates predictions supplied in a CSV; it does not load or run trained model files. Users upload actual and predicted values, select classification or regression metrics, and view results. The current app also keeps session-scoped run history, assigns each run an ID and timestamp, and offers JSON/CSV report downloads.

The project follows a structured software engineering approach covering requirements analysis, system architecture, implementation, and testing.

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
2. Architecture and Design Document
3. Test Plan
4. Web-Based ML Model Evaluator application
5. Automated unit test suite
6. Supporting project documentation

---

## 5. Repository Structure

```
Web-Based-ML-Model-Evaluator/
│
├── app.py                        # Streamlit interface and result presentation
├── evaluator/                    # CSV validation, metric engine, run lifecycle
│   ├── validators.py             # Upload type, size, header, and dataset checks
│   ├── metrics.py                 # Classification and regression calculations
│   └── engine.py                  # Run IDs, status, metadata, safe errors
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
│   └── demo/                     # Sprint demo assets and scripts
│       └── sprint-1-narration-script.md # 60-second narration script & checklist
│
├── tests/                        # Automated unit and evaluator-module tests
│   ├── conftest.py               # Shared pytest fixtures
│   ├── test_validation.py        # File and column validation tests
│   ├── test_classification.py    # Classification metric tests
│   ├── test_regression.py        # Regression metric tests
│   ├── test_error_handling.py    # Error path and edge case tests
│   └── test_evaluator_modules.py # Evaluator service & end-to-end sample tests
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

### Sprint 1 Deviations & Document Compliance
Provides a comprehensive clause-by-clause comparison of the Sprint 1 implementation against the approved SRS, SAD, and Test Plan, detailing verified architectural decisions, single-tenant session scope, and justification for direct module integration.
- [View Sprint 1 Deviations & Compliance](docs/sprint-1-deviations.md)

### Agile Sprint Plan & Backlog
The Sprint Plan defines the delivery milestones, Fibonacci story point scale, team allocations, Definition of Done, demonstration requirements, and detailed user stories for all 10 GitHub backlog issues across Sprint 1 and Sprint 2.
- [View Sprint Plan](docs/SPRINT-PLAN.md)

### Part 2 Deliverables Audit & Traceability
The Deliverables Audit details the complete verification checklist across all Part-2 requirements, remote vs. local analysis, GitHub project setup instructions, and upcoming milestone deliverables.
- [View Part-2 Deliverable Audit](docs/PART2_DELIVERABLE_AUDIT.md)

### Architectural Alignment & Deviations
Documents the alignment of the implementation with SAD Section 4.1/4.2, single-tenant local scoping, and the formal development freeze declaration.
- [View Deviations & Architecture Notes](docs/DEVIATIONS-AND-NOTES.md)

### Demonstration Checklists & Video Scripts
Provides 60-second (Sprint 1) and 120-second (Sprint 2) timestamped walkthrough outlines, pre-demo setup steps, video upload guidelines, and narration scripts.
- [View Demo Checklists](docs/DEMO_CHECKLIST.md)
- [View Sprint 1 Demo Narration Script & Checklist](docs/demo/sprint-1-narration-script.md)

---

## 7. Team Members

| Name | Role |
|------|------|
| Shreyank S | Project Development / Documentation |
| Prajwal | Project Development |
| Sujal | Project Development |
| Skanda | Project Development |

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
2. Verify the instant upload feedback, file size guard (< 10 MB), and dataset summary preview (rows, columns, missing values, complete rows).
3. Select the evaluation task (**Classification** or **Regression**).
4. Map the **Actual values column** (ground truth) and **Predicted values column** (model predictions).
5. Select desired metrics (e.g., Accuracy, Precision, Recall, F1-score for classification; MAE, MSE, RMSE, R² for regression).
6. Click **Calculate evaluation metrics** to execute the evaluation run.
7. Inspect the generated KPI metric cards, detailed table, confusion matrix with natural label ordering (classification) or residual error summary with residual standard deviation (regression), and session run history (with clear history capability).

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

Tests verify:
- **File & Upload Validation (`test_validation.py`, `test_evaluator_modules.py`):** File format (.csv), standard MIME type validation (`text/csv`, `application/x-csv`, etc.), 10 MB size limits, empty and whitespace byte rejection, header whitespace stripping.
- **Data Structure Validation (`test_validation.py`, `test_evaluator_modules.py`):** Column count ($\ge 2$), duplicate column detection and deduplicated reporting, unnamed/blank header handling.
- **Classification Engine (`test_classification.py`, `test_evaluator_modules.py`):** Binary and multiclass accuracy, precision, recall, F1-score with weighted/macro/micro averaging, confusion matrix with natural numeric label sorting.
- **Regression Engine (`test_regression.py`, `test_evaluator_modules.py`):** MAE, MSE, RMSE, R² calculation, signed residual summaries including sample standard deviation, $N < 2$ edge cases.
- **Robustness & Error Handling (`test_error_handling.py`):** Same column guard, non-numeric regression inputs, infinite values, single-class detection, sequence length matching, sanitized error messages without traceback leakage, and safe JSON serialization of NaN values.
- **End-to-End Verification (`test_evaluator_modules.py`):** Direct testing using committed sample datasets (`sample_data/classification_sample.csv` and `sample_data/regression_sample.csv`).
- **Repeatability & Determinism (`test_evaluator_modules.py`):** Verified repeatable floating-point outputs across repeated runs within `1e-6`.

---

## 11. CI/CD & Testing Status

- **Automated Tests:** 113 automated tests passing with 100% pass rate.
- **Evaluator Modules Coverage:** >90% line coverage on core business logic (`evaluator/`).
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
