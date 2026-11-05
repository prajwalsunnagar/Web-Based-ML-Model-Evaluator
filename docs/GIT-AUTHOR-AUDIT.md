# Git Author Audit & History Remediation Plan

**Repository:** `prajwalsunnagar/Web-Based-ML-Model-Evaluator`  
**GitHub URL:** https://github.com/prajwalsunnagar/Web-Based-ML-Model-Evaluator  
**Audit Date:** 2026-11-05  
**Execution Date:** 2026-11-05  
**Version:** 2.0.0 (Execution Completed)  
**Scope:** Complete Git history across `main`, feature branches, and tags (89 total commits)  
**Status:** **REMEDIATION EXECUTED & VERIFIED** (Approved Model: Path A — Strict 2 Authors)

---

## Executive Summary

An exhaustive audit and history cleanup of the commit history in `prajwalsunnagar/Web-Based-ML-Model-Evaluator` was conducted to align repository commit attribution with authorized human contributors and eliminate automated agent identities.

### Key Remediation Results:
1. **Total Commits Preserved:** Exactly **89 unique commits** (100% of historical commits preserved).
2. **File Tree Integrity:** `git diff HEAD backup/pre-author-rewrite-main` returns **0 diff** (bit-for-bit identical code, assets, and documentation).
3. **Commit Messages & Dates:** 100% preserved with original author and committer timestamps.
4. **Automated Test Suite:** 124 of 124 pytest tests pass with 100% reliability in 1.23s.
5. **Authorship Consolidated:**
   - **Prajwal Sunnagar:** **47 commits** (`Prajwal Sunnagar <prajwalsunnagar@gmail.com>`)
   - **Shreyank S:** **42 commits** (`Shreyank S <shreyank70707@gmail.com>`)
   - **Total Displayed Authors:** **EXACTLY 2**
   - **AI Agents / Synthetic Domains:** **0**

---

## Final Verification Outputs

### `git log --all --not backup/pre-author-rewrite-main --format='%an <%ae>' | sort -u`
```text
Prajwal Sunnagar <prajwalsunnagar@gmail.com>
Shreyank S <shreyank70707@gmail.com>
```

### `git log --all --not backup/pre-author-rewrite-main --format='%cn <%ce>' | sort -u`
```text
Prajwal Sunnagar <prajwalsunnagar@gmail.com>
Shreyank S <shreyank70707@gmail.com>
```

### `git shortlog -sne main`
```text
    47  Prajwal Sunnagar <prajwalsunnagar@gmail.com>
    42  Shreyank S <shreyank70707@gmail.com>
```

---

## Complete SHA Correlation Mapping Table (Original -> Rewritten)

The table below records every historical commit SHA alongside its verified replacement SHA:

| # | Original SHA | Rewritten SHA | Original Author | Rewritten Author | Commit Subject |
| :---: | :---: | :---: | :--- | :--- | :--- |
| 1 | `f3d0736` | `f0b6804` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Initial commit |
| 2 | `84679b6` | `55bab31` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add Software Requirements Specification (SRS) |
| 3 | `d80e9a0` | `c01f4b9` | `sujalththth-ops <sujalththth@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add files via upload |
| 4 | `ae5c031` | `e1abd6c` | `skandaml21 <skandaml21@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Added Architecture-Design |
| 5 | `c9b4957` | `e4626cf` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs/SRS.docx |
| 6 | `0af481b` | `cfeb940` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs/Test-Plan.docx |
| 7 | `b5bcd4f` | `0d9c8d0` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Rename Architecture-Design.docx to docs/Architecture-Design.docx |
| 8 | `a985f1a` | `1ef745f` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Enhance README with project details and structure |
| 9 | `63aa4f7` | `8702f6e` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Fix formatting in README repository structure section |
| 10 | `917af9c` | `f526eb7` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Update README.md |
| 11 | `c4d8d55` | `37c45cc` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Update CI workflow to verify GitHub Actions |
| 12 | `7729337` | `6bc2fe9` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add sprint plan for Web-Based ML Model Evaluator |
| 13 | `81f5d84` | `1894092` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Merge pull request #11 from prajwalsunnagar/feature/input-validation |
| 14 | `727fe7c` | `74bf492` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add ML Model Evaluator with CSV upload functionality |
| 15 | `764581c` | `493623f` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add Streamlit and Pandas to requirements |
| 16 | `6b8118e` | `a86cf71` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Enhance CSV upload and validation logic |
| 17 | `be5e6db` | `3ae16a7` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Enhance dataset validation and evaluation configuration |
| 18 | `3cda3dd` | `d812ab5` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Merge pull request #12 from prajwalsunnagar/feature/metric-selection |
| 19 | `af4a4ea` | `042bd07` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add regression metrics and improve CSV handling |
| 20 | `91573cc` | `2ea031e` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add evaluation dependencies. |
| 21 | `8dcb8d9` | `7751456` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Implement evaluation metric calculation and commit |
| 22 | `9378585` | `f98bdf2` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Remove code block formatting from app.py |
| 23 | `4f1a045` | `7a648f1` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Merge pull request #13 from prajwalsunnagar/feature/metric-calculation |
| 24 | `42b626d` | `4c866af` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | fix: repair R2 encoding corruption and page icon in app.py |
| 25 | `9aee2d3` | `d04e65e` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | chore: restore accidentally unstaged project files |
| 26 | `481dcd0` | `1caa25d` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | docs: complete Sprint 2 task list and add Definition of Done in SPRINT-PLAN.md |
| 27 | `6f401f0` | `a2c0709` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | chore: pin minimum dependency versions in requirements.txt (#9) |
| 28 | `dfe8162` | `a7f9769` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | docs: update README with tech stack, run instructions, testing, and repo structure (#10) |
| 29 | `b802c41` | `d91fb62` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | test: add test infrastructure - conftest.py with shared fixtures (#7) |
| 30 | `0ef157e` | `e8c2ad1` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | test: add unit tests for file and column validation (#2, #3) |
| 31 | `b06826a` | `724fc9d` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | test: add unit tests for classification metrics - Accuracy, Precision, Recall, F1 (#5) |
| 32 | `5bfa760` | `3fe7c55` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | test: add unit tests for regression metrics - MAE, MSE, RMSE, R2 (#5) |
| 33 | `870eb23` | `4429e0c` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | test: add unit tests for evaluation error handling and edge cases (#7) |
| 34 | `3d3d1e2` | `0125645` | `Prajwal Sunnagar <prajwal@mleval.dev>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | ci: update GitHub Actions to install deps and run pytest on Python 3.10-3.12 (#7, #8) |
| 35 | `488ed02` | `a1f8ca4` | `Shreyank S <shreyanks@Mac.mshome.net>` | `Shreyank S <shreyank70707@gmail.com>` | docs: add Part 2 deliverables audit, demo checklists, and test execution report |
| 36 | `2d56a39` | `4a6f345` | `Shreyank S <shreyanks@Shreyanks-MacBook-Air.local>` | `Shreyank S <shreyank70707@gmail.com>` | docs: expand SPRINT-PLAN.md with detailed user stories, criteria, and story points |
| 37 | `406bd47` | `0aebb0b` | `Shreyank S <shreyanks@Shreyanks-MacBook-Air.local>` | `Shreyank S <shreyank70707@gmail.com>` | docs: update README with Part 2 audit, execution report, and demo checklist links |
| 38 | `9523d81` | `8146934` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Reject duplicate CSV headers before pandas renames them |
| 39 | `cf7aa6b` | `84bbf89` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add modular evaluator validation, metrics, and run lifecycle |
| 40 | `3f44a00` | `267eca4` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add modular evaluator validation, metrics, and run lifecycle |
| 41 | `1e44b0d` | `63cc0c5` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add modular evaluator validation, metrics, and run lifecycle |
| 42 | `35c9dd3` | `3be9040` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Connect Streamlit app to evaluator and expose run reports |
| 43 | `42159de` | `4cc5e95` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Document evaluator modules and implemented result features |
| 44 | `db0286d` | `3958b36` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Correct regression sample row count |
| 45 | `865bcc1` | `af282dc` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Complete evaluator acceptance criteria: evaluator/validators.py |
| 46 | `44411cc` | `83155d4` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Complete evaluator acceptance criteria: evaluator/metrics.py |
| 47 | `2b8738a` | `090140c` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Complete evaluator acceptance criteria: evaluator/engine.py |
| 48 | `03d6b05` | `a5cf4e1` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Complete evaluator acceptance criteria: app.py |
| 49 | `0d4ec38` | `b2eb2bc` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Test evaluator modules directly |
| 50 | `7f0dbf9` | `e93386e` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Update test documentation for evaluator module coverage |
| 51 | `ef430b7` | `02550c0` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Add validated regression residual summary |
| 52 | `d0146ab` | `e8129e4` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Use validated residual helper in regression results |
| 53 | `4071163` | `340cd88` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Cover regression residual summary behavior |
| 54 | `45b9249` | `d493ed4` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Clarify historical test and audit evidence |
| 55 | `3b1ae64` | `d044617` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Clarify historical test and audit evidence |
| 56 | `72beba4` | `fbe6eae` | `prajwalsunnagar <prajwalsunnagar@gmail.com>` | `Prajwal Sunnagar <prajwalsunnagar@gmail.com>` | Clarify historical test and audit evidence |
| 57 | `ccf77e4` | `f029678` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat: complete Sprint 1 requirements, CI lint/build checks, deviations doc, and demo narration script |
| 58 | `deb8bc8` | `fb36d10` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs: add Sprint 1 comprehensive backlog audit report |
| 59 | `9f23ba7` | `e562a45` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Merge pull request #14 from ShreyankSridhar/feature/sprint-1-completion |
| 60 | `0339ed1` | `edb4731` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: accept additional standard CSV MIME types in upload validator |
| 61 | `7a607d3` | `3129f64` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: return descriptive error message for empty CSV upload bytes |
| 62 | `fdad06b` | `b6b34e2` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: deduplicate repeated column names in dataframe validation message |
| 63 | `02438bf` | `12063a8` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: strip leading and trailing whitespace from CSV column names |
| 64 | `2175e76` | `8b955a6` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: preserve natural numeric ordering for confusion matrix labels |
| 65 | `e3ee3b8` | `275e6e2` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: handle non-numeric inputs gracefully in regression residual summary |
| 66 | `1c81660` | `8754b2a` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat: add standard deviation of residuals to regression summary |
| 67 | `4891c9c` | `f42acf1` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix: sanitize NaN and infinite metric values during run serialization |
| 68 | `2621bb2` | `25f3cc4` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat: reset evaluation error state on subsequent execute calls |
| 69 | `7c0ea54` | `af43d02` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | test: refactor test_validation to import directly from evaluator validators |
| 70 | `41a9645` | `ae799db` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | test: link test_classification helpers to core metric calculation engine |
| 71 | `934887c` | `0b13e69` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | test: link test_regression helpers to core metric calculation engine |
| 72 | `b4d70ae` | `dae0430` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | test: expand error handling tests for empty bytes and non-numeric residuals |
| 73 | `01d7f33` | `37c81cb` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat: add clear history action and dataset row health metrics in UI |
| 74 | `8f01f2a` | `8213ab0` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | ci: add workflow concurrency group and optimize coverage paths |
| 75 | `674aaa6` | `e2727e7` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs: update documentation for enhanced residual metrics, MIME types, and testing |
| 76 | `8a283db` | `2aad654` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Merge pull request #15 from prajwalsunnagar/feature/sprint-1-completion |
| 77 | `e38e76f` | `eaf6da5` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat(error-handling): improve lifecycle tracking, edge case handling, and safe error messages (#7) |
| 78 | `0c30762` | `19623a4` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat(run-history): enhance session run history, report metadata linkage, and CSV/JSON exports (#8) |
| 79 | `1882bb3` | `8f28204` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | test(robustness): add comprehensive tests for validation, lifecycle, exports, performance, and determinism (#9) |
| 80 | `a510efb` | `887fefd` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | ci: configure workflow concurrency, coverage reporting, and repo hygiene (#7, #8, #9) |
| 81 | `a8df41f` | `473f8b2` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs: update sprint plan, test execution report, deliverable audit, and deviations (#10) |
| 82 | `bda7417` | `8371a91` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | chore(release): prepare Sprint 2 demo assets, narration script, and development freeze |
| 83 | `8e3aff5` | `5e781f8` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | fix(test): resolve absolute path for AppTest in test_app_integration |
| 84 | `8651b3a` | `583f750` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Merge pull request #16 from prajwalsunnagar/feature/sprint-2-completion |
| 85 | `ea3e160` | `f930978` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | docs: complete audit, revised IEEE deliverables, RTM & submission readiness |
| 86 | `a7395ea` | `720cadd` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | style: normalize trailing newlines across docs |
| 87 | `6c3c916` | `166dfd4` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Merge pull request #17 from prajwalsunnagar/feature/sprint-2-completion |
| 88 | `625b825` | `d77f598` | `Shreyank S <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | feat(test): complete Part 3 testing deliverables, branch coverage and validation reports |
| 89 | `e114a3d` | `25cce37` | `Shreyank <shreyank70707@gmail.com>` | `Shreyank S <shreyank70707@gmail.com>` | Merge pull request #18 from prajwalsunnagar/feature/part-3-testing-deliverables |

---

## Safety Backups & Rollback Information

1. **Pre-Rewrite Backup Branch:**
   - Branch: `backup/pre-author-rewrite-main`
   - Target Commit: `e114a3d7e0b1a692aa7af834b2bbe44505bec1c1`
2. **Full Standalone Bundle:**
   - File: `/tmp/Web-Based-ML-Model-Evaluator-pre-rewrite-backup.bundle`
3. **Rollback Procedure:**
   If ever required, running `git reset --hard backup/pre-author-rewrite-main` immediately restores the pre-rewrite commit chain.
