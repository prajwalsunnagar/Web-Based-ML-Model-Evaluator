# Web-Based ML Model Evaluator

## 1. Project Overview

The **Web-Based ML Model Evaluator** is a web-based system designed to provide a structured platform for evaluating Machine Learning models.

The project aims to simplify the process of evaluating ML models by providing a user-friendly web interface through which users can upload CSV datasets, select evaluation metrics, and view evaluation results.

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
├── app.py                        # Main Streamlit application
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation & execution guide
│
├── sample_data/                  # Verification datasets
│   ├── classification_sample.csv # Classification test data (15 rows)
│   └── regression_sample.csv     # Regression test data (15 rows)
│
├── docs/                         # Specifications & deliverables
│   ├── SRS.docx                  # Software Requirements Specification
│   ├── Architecture-Design.docx  # Architecture and Design Document
│   ├── Test-Plan.docx            # Test Plan
│   ├── SPRINT-PLAN.md            # Agile sprint plan & user stories
│   ├── PART2_DELIVERABLE_AUDIT.md# Part-2 deliverables audit matrix
│   ├── TEST-EXECUTION-REPORT.md  # Test results & Requirement Traceability Matrix
│   ├── DEVIATIONS-AND-NOTES.md   # Architectural alignment & design decisions
│   └── DEMO_CHECKLIST.md         # Sprint demo outlines & video release checklists
│
├── tests/                        # Automated unit tests (72 passing tests)
│   ├── conftest.py               # Shared pytest fixtures
│   ├── test_validation.py        # File and column validation tests
│   ├── test_classification.py    # Classification metric tests
│   ├── test_regression.py        # Regression metric tests
│   └── test_error_handling.py    # Error path and edge case tests
│
├── scripts/                      # Automation & sync scripts
│   └── update_github_backlog.py  # GitHub issues updater script
│
└── .github/
    ├── pull_request_template.md  # Standard PR review template
    └── workflows/
        └── ci.yml                # GitHub Actions CI multi-version pipeline
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
The Deliverables Audit details the complete verification checklist across all Part-2 requirements, remote vs. local analysis, GitHub project setup instructions, and upcoming milestone deliverables.
- [View Part-2 Deliverable Audit](docs/PART2_DELIVERABLE_AUDIT.md)

### Architectural Alignment & Deviations
Documents the alignment of the implementation with SAD Section 4.1/4.2, single-tenant local scoping, and the formal development freeze declaration.
- [View Deviations & Architecture Notes](docs/DEVIATIONS-AND-NOTES.md)

### Demonstration Checklists & Video Outlines
Provides 60-second (Sprint 1) and 120-second (Sprint 2) timestamped walkthrough outlines, pre-demo setup steps, and repository video upload guidelines.
- [View Demo Checklists](docs/DEMO_CHECKLIST.md)

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
| Language | Python 3.10+ |
| Web Framework | Streamlit >= 1.35.0 |
| Data Processing | pandas >= 2.2.0, numpy >= 1.26.0 |
| ML Metrics | scikit-learn >= 1.4.0 |
| Testing | pytest |
| CI/CD | GitHub Actions |

---

## 9. Running the Application

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the app

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

### Upload a CSV

The CSV must have at least two columns:
- One column containing **actual** labels or values.
- One column containing **predicted** labels or values.

---

## 10. Testing

Run the automated test suite with:

```bash
pytest tests/ -v
```

Tests cover:
- File type and size validation
- Column validation
- Classification metric calculation (Accuracy, Precision, Recall, F1-score)
- Regression metric calculation (MAE, MSE, RMSE, R²)
- Error handling for edge cases

---

## 11. Testing Status

| Test Module | Status |
|---|---|
| File and column validation | ✅ Passing |
| Classification metrics | ✅ Passing |
| Regression metrics | ✅ Passing |
| Error handling | ✅ Passing |

CI runs automatically on every push and pull request.

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
