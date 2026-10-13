# Sprint Plan — Web-Based ML Model Evaluator

## Sprint 1: 19–23 October 2026

**Goal:** Establish the core evaluation workflow.

- #1 Implement evaluation input upload
- #2 Validate uploaded file type and size
- #3 Validate required dataset columns
- #4 Implement task type and metric selection
- #5 Calculate selected evaluation metrics
- #6 Display evaluation results

**Sprint review:** Demonstrate the working evaluation flow and record a one-minute video.

---

## Sprint 2: 26–30 October 2026

**Goal:** Improve reliability and prepare the final submission.

- #7 Handle evaluation errors and run automated unit tests using pytest
- #8 Update the CI/CD pipeline to install dependencies and execute the test suite on every push
- #9 Pin exact dependency versions in requirements.txt for reproducible builds
- #10 Update README with final technology stack, testing status, and project completion notes

**Sprint review:** Demonstrate all passing tests in CI, review the final application end-to-end, and confirm documentation is consistent with the implementation.

---

## Definition of Done

A task is considered done when:

- The implementation is complete and merged to `main`.
- All related automated tests pass.
- The CI pipeline reports a green build.
- Documentation is updated to reflect the change where applicable.
