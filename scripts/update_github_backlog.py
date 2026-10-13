"""
Helper script to automatically update GitHub Issues on prajwalsunnagar/Web-Based-ML-Model-Evaluator
with requirements, acceptance criteria, story points, and labels using a GitHub Personal Access Token.

Usage:
    export GITHUB_TOKEN="ghp_your_personal_access_token_here"
    python3 scripts/update_github_backlog.py
"""
import os
import sys
import json
import urllib.request

REPO = "prajwalsunnagar/Web-Based-ML-Model-Evaluator"
TOKEN = os.environ.get("GITHUB_TOKEN")

if not TOKEN:
    print("ERROR: GITHUB_TOKEN environment variable is not set.")
    print("Please run: export GITHUB_TOKEN='ghp_...' and rerun this script.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "BacklogUpdater"
}

UPDATES = {
    1: {
        "title": "Implement evaluation input upload",
        "labels": ["enhancement", "sprint-1"],
        "body": """**Requirement:** FR-01 — Input upload

**Description:**
Allow users to upload an evaluation input dataset in standard `.csv` format.

**Acceptance criteria:**
- The user can select and upload a `.csv` dataset through the web UI.
- The system accepts valid files and displays a preview of the first 10 rows.
- The system immediately displays summary metrics (total rows, columns, missing values).
- Unsupported or malformed files are rejected safely.

**Story points:** 3
**Assigned:** @prajwalsunnagar"""
    },
    2: {
        "title": "Validate uploaded file type and size",
        "labels": ["enhancement", "security", "sprint-1"],
        "body": """**Requirements:** FR-02, FR-03, NFR-05, SEC-01, SEC-02

**Description:**
Validate uploaded files before processing them in memory.

**Acceptance criteria:**
- Accept only `.csv` file extensions and content types.
- Reject unsupported extensions (e.g., `.xlsx`, `.json`) with an actionable error.
- Enforce the 10 MB maximum upload size limit; reject larger files and display the permitted limit.
- Run validations before full parsing occurs.

**Story points:** 3
**Assigned:** @ShreyankSridhar"""
    },
    3: {
        "title": "Validate required dataset columns",
        "labels": ["enhancement", "sprint-1"],
        "body": """**Requirements:** FR-04, BR-02, BR-03, NFR-05

**Description:**
Validate the uploaded dataset structure and schema before evaluation begins.

**Acceptance criteria:**
- Reject empty datasets (0 rows or 0 columns) without server crash.
- Detect duplicate column headers and prompt the user to resolve them.
- Flag blank or unnamed columns (`Unnamed:`).
- Verify that ground truth target and prediction columns are present, distinct, and contain non-empty overlapping rows.

**Story points:** 3
**Assigned:** @skandaml21"""
    },
    4: {
        "title": "Implement task type and metric selection",
        "labels": ["enhancement", "ui", "sprint-1"],
        "body": """**Requirements:** FR-05, FR-06, BR-01

**Description:**
Allow users to select a machine learning task type (Classification or Regression) and dynamically choose compatible metrics.

**Acceptance criteria:**
- User can toggle between `Classification` and `Regression` in the setup sidebar.
- Dynamically display compatible metrics:
  - Classification: Accuracy, Precision, Recall, F1 Score (with configurable averaging: weighted, macro, micro, binary).
  - Regression: MAE, MSE, RMSE, R² Score.
- Incompatible task/metric combinations are rejected programmatically (`validate_metric_compatibility`).

**Story points:** 5
**Assigned:** @sujalththth-ops"""
    },
    5: {
        "title": "Calculate selected evaluation metrics",
        "labels": ["enhancement", "sprint-1"],
        "body": """**Requirements:** FR-07, BR-04, BR-05, NFR-03, NFR-09

**Description:**
Calculate the requested evaluation metrics deterministically using decoupled calculation logic.

**Acceptance criteria:**
- Decouple metric calculation logic into `evaluator/metrics.py`.
- Compute all selected metrics accurately and deterministically within `EPSILON = 1e-6`.
- Filter paired null values before metric computation.
- Cover metric calculation with unit tests for binary/multiclass classification and regression.

**Story points:** 5
**Assigned:** @prajwalsunnagar"""
    },
    6: {
        "title": "Display evaluation results",
        "labels": ["enhancement", "ui", "sprint-1"],
        "body": """**Requirements:** FR-08, NFR-08, NFR-12

**Description:**
Present computed evaluation results with visual KPI cards, summary tables, and task-specific breakdown views.

**Acceptance criteria:**
- Display each computed metric's name and rounded value in high-contrast visual KPI cards.
- Provide a summary table of all calculated metrics.
- Display a Confusion Matrix crosstab for classification evaluations.
- Display residual metrics (Mean Error, Min, Max) for regression evaluations.
- Ensure interface elements are keyboard-accessible with descriptive labels.

**Story points:** 3
**Assigned:** @ShreyankSridhar"""
    },
    7: {
        "title": "Handle evaluation errors and run status",
        "labels": ["bug", "reliability", "sprint-2"],
        "body": """**Requirements:** FR-09, FR-10, NFR-02, NFR-11, SEC-06

**Description:**
Manage evaluation execution states and safely map internal errors to user-friendly messages without leaking stack traces.

**Acceptance criteria:**
- Maintain evaluation lifecycle status (`pending`, `running`, `completed`, `failed`).
- When evaluation fails, mark run as `failed` and display an actionable error message.
- Ensure internal stack traces, credentials, and raw server paths are never exposed.
- Application process does not crash on malformed inputs or calculation errors.

**Story points:** 5
**Assigned:** @skandaml21"""
    },
    8: {
        "title": "Link results to input and configuration",
        "labels": ["enhancement", "reporting", "sprint-2"],
        "body": """**Requirements:** FR-11, FR-13, FR-14

**Description:**
Link each evaluation result to an immutable run ID and configuration, track session run history, and enable report exports.

**Acceptance criteria:**
- Generate an immutable `run_id` (e.g. `eval-1234abcd`) and timestamp for each evaluation.
- Track completed and failed runs in the sidebar session history.
- Allow downloading full evaluation run report as JSON.
- Allow downloading metric results summary as CSV.

**Story points:** 5
**Assigned:** @sujalththth-ops"""
    },
    9: {
        "title": "Test invalid inputs and application robustness",
        "labels": ["testing", "qa", "sprint-2"],
        "body": """**Requirements:** NFR-01, NFR-02, NFR-03, SEC-01, SEC-02, SEC-03

**Description:**
Implement and execute automated test suites covering all boundary conditions, invalid inputs, and repeatability.

**Acceptance criteria:**
- Implement test suite covering Test Plan cases TC-01 through TC-09 in `tests/test_evaluator.py`.
- 100% test pass rate in local execution and CI pipeline.
- Verify repeatability across repeated identical runs within `EPSILON = 1e-6`.
- Benchmark evaluation execution to complete within < 1 second for standard test datasets.

**Story points:** 5
**Assigned:** @prajwalsunnagar"""
    },
    10: {
        "title": "Complete project documentation and deployment instructions",
        "labels": ["documentation", "sprint-2"],
        "body": """**Requirements:** NFR-04, NFR-06, NFR-07, NFR-08, NFR-10

**Description:**
Finalize repository documentation, deployment notes, test execution reports, and development freeze.

**Acceptance criteria:**
- README updated with project architecture, setup guide, testing instructions, and team roles.
- `docs/SPRINT-PLAN.md` documents complete backlog, story points, and sprint allocations.
- `docs/TEST-EXECUTION-REPORT.md` details test case results and RTM evidence.
- `docs/DEVIATIONS-AND-NOTES.md` documents architectural alignment and design decisions.
- Formally declare development freeze for Part 2 submission.

**Story points:** 3
**Assigned:** @ShreyankSridhar"""
    }
}


def update_issues():
    for num, data in UPDATES.items():
        url = f"https://api.github.com/repos/{REPO}/issues/{num}"
        req = urllib.request.Request(
            url,
            data=json.dumps(data).encode("utf-8"),
            headers=HEADERS,
            method="PATCH"
        )
        try:
            with urllib.request.urlopen(req) as resp:
                print(f"✅ Successfully updated Issue #{num}: {data['title']}")
        except Exception as e:
            print(f"❌ Failed to update Issue #{num}: {e}")

if __name__ == "__main__":
    update_issues()
