"""Evaluation run lifecycle and safe result serialization."""
from __future__ import annotations

import math
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from uuid import uuid4

import pandas as pd

from evaluator.metrics import calculate_metrics


@dataclass
class EvaluationRun:
    source_file: str
    task_type: str
    actual_column: str
    predicted_column: str
    selected_metrics: list[str]
    average: str = "weighted"
    positive_label: object | None = None
    run_id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    status: str = "pending"
    sample_count: int = 0
    results: dict[str, float | None] = field(default_factory=dict)
    error_message: str | None = None
    confusion_matrix: list[list[int]] | None = None
    confusion_labels: list[str] | None = None

    def execute(self, actual: pd.Series, predicted: pd.Series) -> None:
        self.status = "running"
        try:
            self.results, matrix, self.sample_count = calculate_metrics(
                self.task_type,
                actual,
                predicted,
                self.selected_metrics,
                average=self.average,
                positive_label=self.positive_label,
            )
            if matrix is not None:
                self.confusion_labels = [str(value) for value in matrix.index]
                self.confusion_matrix = matrix.values.tolist()
            self.status = "completed"
        except (ValueError, TypeError) as exc:
            self.error_message = str(exc)
            self.status = "failed"
        except Exception:
            self.error_message = "Evaluation failed. Check the selected columns and input values."
            self.status = "failed"

    def to_dict(self) -> dict:
        result = asdict(self)
        if self.positive_label is not None:
            result["positive_label"] = str(self.positive_label)
        if "results" in result and isinstance(result["results"], dict):
            clean_results = {}
            for k, v in result["results"].items():
                if isinstance(v, float) and (math.isnan(v) or math.isinf(v)):
                    clean_results[k] = None
                else:
                    clean_results[k] = v
            result["results"] = clean_results
        return result
