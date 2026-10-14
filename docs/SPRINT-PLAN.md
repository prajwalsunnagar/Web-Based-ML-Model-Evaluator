# Sprint Plan & Backlog — Web-Based ML Model Evaluator

## 1. Project Timeline & Delivery Milestones

| Sprint / Phase | Dates | Goals & Key Deliverables |
|---|---|---|
| **Sprint Dry Run Period** | 12 October – 16 October 2026 | Environment setup, backlog calibration, baseline CI pipeline, initial test dry runs |
| **Sprint 1** | 19 October – 23 October 2026 | Core evaluation flow: CSV upload, schema/column validation, task type selection, metric computation, results presentation, 1-minute demo video |
| **Sprint 2** | 26 October – 30 October 2026 | Reliability, error handling, run tracking & report export, robustness testing, documentation completion, 2-minute demo video, development freeze |

---

## 2. Estimation Scale & Story Point Allocation

Story points are estimated using the standard **Fibonacci scale** (`1, 2, 3, 5, 8`):
- **1 SP:** Trivial configuration or minor documentation adjustment (< 2 hours).
- **2 SP:** Minor feature or isolated test script (half day).
- **3 SP:** Standard feature module with input validation and unit tests (~1 day).
- **5 SP:** Complex multi-component feature requiring numerical validation, calculation logic, and integration tests (~2 days).
- **8 SP:** Architecture-level refactoring or cross-cutting subsystems.

### Team Members & Allocations:
- **Prajwal Sunnagar** (`@prajwalsunnagar`) — Repository Owner / ML Evaluation Engine (Issues #1, #5, #9: **13 SP**)
- **Shreyank S** (`@ShreyankSridhar`) — Documentation Lead / UI & Frontend (Issues #2, #6, #10: **9 SP**)
- **Skanda** (`@skandaml21`) — Backend Architecture / Schema Validation & QA (Issues #3, #7: **8 SP**)
- **Sujal** (`@sujalththth-ops`) — Full-Stack Integration / Workflow & Reporting (Issues #4, #8: **10 SP**)
- **Total Backlog:** **40 Story Points** (Sprint 1: 22 SP | Sprint 2: 18 SP)

---

## 3. Sprint 1 Backlog Items (19–23 October 2026)

**Goal:** Establish the end-to-end core evaluation workflow.

### Issue #1: Implement evaluation input upload
- **User Story:** As an ML practitioner, I want to upload an evaluation dataset in CSV format through the web interface so that the application can ingest predictions and ground truth labels.
- **SRS Requirement:** `FR-01` (Input upload)
- **Story Points:** 3
- **Assignee:** `@prajwalsunnagar`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. The user can select and upload a `.csv` file via Streamlit file uploader.
  2. The system parses the uploaded file and presents an immediate 10-row dataset preview.
  3. Key summary metrics (total rows, columns, missing values count) are computed and displayed.
  4. Unsupported or corrupt files are rejected safely with user feedback.

### Issue #2: Validate uploaded file type and size
- **User Story:** As a system user, I want uploaded files to be validated for format and size limits before processing so that invalid inputs or oversized payloads are rejected early.
- **SRS Requirements:** `FR-02` (Upload validation), `FR-03` (Size limit), `NFR-05` (Security — file handling), `SEC-01`, `SEC-02`
- **Story Points:** 3
- **Assignee:** `@ShreyankSridhar`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. Only `.csv` extensions and MIME content types are accepted; unsupported files are rejected with a clear message.
  2. Enforce the maximum upload size limit of `10 MB` (`MAX_FILE_SIZE = 10 * 1024 * 1024`).
  3. Rejection message clearly states the permitted upload limit (10 MB).
  4. Validation runs prior to full dataset parsing in memory.

### Issue #3: Validate required dataset columns
- **User Story:** As an evaluator, I want the dataset schema to be checked for required columns, uniqueness, and null distributions so that evaluation is not attempted on malformed data.
- **SRS Requirements:** `FR-04` (Structure validation), `BR-02` (Target/prediction column identification), `BR-03` (Missing value behavior), `NFR-05`
- **Story Points:** 3
- **Assignee:** `@skandaml21`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. Verify the dataset is non-empty and contains at least two distinct columns.
  2. Detect and reject duplicate column headers with a list of duplicate names.
  3. Detect and warn on blank or unnamed headers (`Unnamed:`).
  4. Allow user to select distinct columns for ground truth (actual) and model prediction.

### Issue #4: Implement task type and metric selection
- **User Story:** As an ML practitioner, I want to select the machine learning task type (Classification or Regression) and choose compatible evaluation metrics so that evaluation aligns with my model objectives.
- **SRS Requirements:** `FR-05` (Configuration), `FR-06` (Compatibility), `BR-01` (Task/metric compatibility)
- **Story Points:** 5
- **Assignee:** `@sujalththth-ops`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. User can choose between `Classification` and `Regression` task types.
  2. Dynamically populate compatible metrics:
     - Classification: `Accuracy`, `Precision`, `Recall`, `F1-score`
     - Regression: `MAE`, `MSE`, `RMSE`, `R²`
  3. Ensure user selects at least one metric before calculation.
  4. Prevent selecting incompatible task and metric combinations.

### Issue #5: Calculate selected evaluation metrics
- **User Story:** As a data scientist, I want evaluation metrics calculated accurately, deterministically, and with missing rows filtered so that model performance can be reliably assessed.
- **SRS Requirements:** `FR-07` (Evaluation execution), `BR-04` (Documented metric definitions & averaging), `BR-05` (Finite valid outputs), `NFR-03` (Reliability & repeatability), `NFR-09` (Maintainability)
- **Story Points:** 5
- **Assignee:** `@prajwalsunnagar`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. Calculate selected classification metrics (Accuracy, Precision, Recall, F1-score with weighted averaging and zero_division=0).
  2. Calculate selected regression metrics (MAE, MSE, RMSE, R² with safe handling for N < 2).
  3. Drop paired rows where either actual or predicted value is NaN prior to computation.
  4. Verify calculations produce identical values within `EPSILON = 1e-6` across repeated runs.

### Issue #6: Display evaluation results
- **User Story:** As a user, I want computed metrics displayed in clear visual metric cards and tables so that I can easily interpret the evaluation output.
- **SRS Requirements:** `FR-08` (Result presentation), `NFR-08` (Usability), `NFR-12` (Accessibility)
- **Story Points:** 3
- **Assignee:** `@ShreyankSridhar`
- **Milestone:** Sprint 1
- **Acceptance Criteria:**
  1. Display each selected metric's name and rounded float value (to 4 decimal places) in prominent visual cards.
  2. Provide tabular overview of all calculated results.
  3. UI adheres to accessibility best practices with readable labels and high-contrast styling.

### Sprint 1 Review & Demonstration Requirements:
- **Demonstration:** Record a 1-minute video demonstrating:
  1. Application launch via `streamlit run app.py`.
  2. Upload of valid classification dataset (`sample_data/classification_sample.csv`).
  3. Instant file size and schema validation.
  4. Column selection, task configuration, and metric calculation.
  5. Presentation of calculated KPI metric cards.
- **Video Upload:** Upload video to repository root or `docs/demo_videos/sprint1_demo.mp4`.

---

## 4. Sprint 2 Backlog Items (26–30 October 2026)

**Goal:** Improve reliability, error handling, test automation, reporting, and prepare final submission.

### Issue #7: Handle evaluation errors and run status
- **User Story:** As a user, I want the application to handle edge cases and invalid inputs gracefully with clear error messages rather than unhandled crashes.
- **SRS Requirements:** `FR-09` (Failure handling), `FR-10` (Run status), `NFR-02` (Availability / robustness), `NFR-11` (Observability), `SEC-06` (No secret or internal stack trace leakage)
- **Story Points:** 5
- **Assignee:** `@skandaml21`
- **Milestone:** Sprint 2
- **Acceptance Criteria:**
  1. Reject non-numeric inputs in regression with a safe, actionable error message.
  2. Reject single-class inputs in classification where at least 2 classes are required.
  3. Catch expected runtime exceptions and display user-friendly error banners without process crashes.
  4. Ensure raw server stack traces and internal paths are never exposed to the UI.

### Issue #8: Link results to input and configuration
- **User Story:** As a practitioner, I want each evaluation run linked to its input file and configuration with options to export results for reproducibility.
- **SRS Requirements:** `FR-11` (Run history), `FR-13` (Report export), `FR-14` (Input-to-result linkage)
- **Story Points:** 5
- **Assignee:** `@sujalththth-ops`
- **Milestone:** Sprint 2
- **Acceptance Criteria:**
  1. Link each evaluation result with the active input file name, task type, and selected columns.
  2. Support exporting evaluation summary reports in JSON and CSV formats.
  3. Maintain run context throughout the user session.

### Issue #9: Test invalid inputs and application robustness
- **User Story:** As a quality engineer, I want comprehensive automated unit tests covering all validation, classification, regression, and error-handling paths to ensure application reliability.
- **SRS Requirements:** `NFR-01` (Performance), `NFR-02` (Robustness), `NFR-03` (Reliability), `SEC-01`, `SEC-02`, `SEC-03`
- **Story Points:** 5
- **Assignee:** `@prajwalsunnagar`
- **Milestone:** Sprint 2
- **Acceptance Criteria:**
  1. Implement automated test suites in `tests/` covering:
     - `test_validation.py`: File size limits, empty CSVs, duplicate columns, blank headers.
     - `test_classification.py`: Perfect/imperfect binary, multiclass, weighted averaging, zero division.
     - `test_regression.py`: MAE, MSE, RMSE, R², NaN row dropping, single-row edge cases.
     - `test_error_handling.py`: Disjoint NaNs, non-numeric strings, infinite values, single-class inputs.
  2. Achieve 100% test pass rate across all suites.
  3. Tests execute in under 2 seconds locally and in CI.

### Issue #10: Complete project documentation and deployment instructions
- **User Story:** As a new user or evaluator, I want complete project documentation, deployment instructions, and test evidence so that I can easily verify and deploy the application.
- **SRS Requirements:** `NFR-04` (Transport security), `NFR-06` (Secret protection), `NFR-07` (Privacy), `NFR-08` (Usability), `NFR-10` (Browser compatibility)
- **Story Points:** 3
- **Assignee:** `@ShreyankSridhar`
- **Milestone:** Sprint 2
- **Acceptance Criteria:**
  1. `README.md` documents project overview, architecture, tech stack, installation, running instructions, and testing.
  2. `docs/PART2_DELIVERABLE_AUDIT.md` documents requirement-to-deliverable audit and evidence.
  3. `docs/TEST-EXECUTION-REPORT.md` details test case results and Requirement Traceability Matrix.
  4. `docs/DEVIATIONS-AND-NOTES.md` documents architectural alignment and design decisions.
  5. Formally declare development freeze for Part-2 submission.

### Sprint 2 Review & Demonstration Requirements:
- **Demonstration:** Record a 2-minute video demonstrating:
  1. End-to-end classification and regression workflows.
  2. Robustness testing with invalid, non-numeric, or malformed inputs showing safe error feedback.
  3. Execution of full automated test suite via `pytest tests/ -v`.
  4. GitHub Actions CI pipeline running on push/PR with multi-version Python matrix.
  5. Summary of completed documentation and development freeze.
- **Video Upload:** Upload video to repository root or `docs/demo_videos/sprint2_demo.mp4`.

---

## 5. Definition of Done (DoD)

A backlog item or task is officially declared **Done** only when:
1. **Implementation:** Code meets all stated acceptance criteria.
2. **Quality & Linting:** Code adheres to PEP 8 standards with no syntax or import errors.
3. **Automated Testing:** Unit and integration tests pass cleanly with `pytest`.
4. **CI Validation:** GitHub Actions workflow completes with a green check mark.
5. **Peer Review:** Code changes are submitted via pull request and reviewed before merging to `main`.
6. **Documentation:** README, sprint plan, test reports, or audit docs are updated where relevant.
7. **Security:** No secrets, credentials, or internal stack traces are committed or exposed.
