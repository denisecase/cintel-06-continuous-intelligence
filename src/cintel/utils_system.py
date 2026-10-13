"""utils_system.py.

Shared helper functions
for the system-metrics monitoring domain.

Used by:
- src/cintel/signal_design.py (cintel-03)
- src/cintel/rolling_monitor.py (cintel-04)
- src/cintel/drift_detector.py (cintel-05)
- src/cintel/continuous_intelligence.py (cintel-06)
- app.py in each of the above

All four projects share the same schema (requests, errors,
total_latency_ms), so their functions live together here.
"""

from pathlib import Path

import polars as pl


def load_system_metrics(data_file: Path) -> pl.DataFrame:
    """Read raw system metrics (requests, errors, total_latency_ms) from a CSV file.

    Used for plain snapshots (cintel-03, cintel-06) and for the reference/
    current period files in cintel-05, which share the same three columns.
    """
    return pl.read_csv(data_file)


def load_timeseries_metrics(data_file: Path) -> pl.DataFrame:
    """Read time-series system metrics from a CSV file, sorted by timestamp."""
    return pl.read_csv(data_file).sort("timestamp")


# === cintel-03: SIGNAL DESIGN ===


def design_signals(df: pl.DataFrame) -> pl.DataFrame:
    """Add derived signal columns: error_rate, avg_latency_ms, throughput.

    Per-request signals are only computed when requests > 0, to avoid
    dividing by zero; otherwise they default to 0.0.
    """
    is_requests_positive = pl.col("requests") > 0

    return df.with_columns(
        [
            pl.when(is_requests_positive)
            .then(pl.col("errors") / pl.col("requests"))
            .otherwise(0.0)
            .alias("error_rate"),
            pl.when(is_requests_positive)
            .then(pl.col("total_latency_ms") / pl.col("requests"))
            .otherwise(0.0)
            .alias("avg_latency_ms"),
            pl.col("requests").alias("throughput"),
        ]
    ).select(
        [
            "requests",
            "errors",
            "total_latency_ms",
            "error_rate",
            "avg_latency_ms",
            "throughput",
        ]
    )


# === cintel-04: ROLLING MONITORING ===


def compute_rolling_metrics(df: pl.DataFrame, window_size: int) -> pl.DataFrame:
    """Add rolling-mean columns for requests, errors, and total_latency_ms.

    Assumes df is already sorted by timestamp (see load_timeseries_metrics).
    """
    return df.with_columns(
        [
            pl.col("requests").rolling_mean(window_size).alias("requests_rolling_mean"),
            pl.col("errors").rolling_mean(window_size).alias("errors_rolling_mean"),
            pl.col("total_latency_ms")
            .rolling_mean(window_size)
            .alias("latency_rolling_mean"),
        ]
    )


# === cintel-05: DRIFT DETECTION ===


def compute_drift_summary(
    reference_df: pl.DataFrame,
    current_df: pl.DataFrame,
    requests_threshold: float,
    errors_threshold: float,
    latency_threshold: float,
) -> pl.DataFrame:
    """Compare mean requests/errors/latency between two periods and flag drift.

    Returns a one-row summary with each period's averages, the difference
    between them, and a boolean drift flag per metric.
    """
    reference_summary = reference_df.select(
        [
            pl.col("requests").mean().alias("reference_avg_requests"),
            pl.col("errors").mean().alias("reference_avg_errors"),
            pl.col("total_latency_ms").mean().alias("reference_avg_latency_ms"),
        ]
    )
    current_summary = current_df.select(
        [
            pl.col("requests").mean().alias("current_avg_requests"),
            pl.col("errors").mean().alias("current_avg_errors"),
            pl.col("total_latency_ms").mean().alias("current_avg_latency_ms"),
        ]
    )
    combined = pl.concat(
        [reference_summary, current_summary], how="horizontal"
    ).with_columns(
        [
            (pl.col("current_avg_requests") - pl.col("reference_avg_requests"))
            .round(2)
            .alias("requests_mean_difference"),
            (pl.col("current_avg_errors") - pl.col("reference_avg_errors"))
            .round(2)
            .alias("errors_mean_difference"),
            (pl.col("current_avg_latency_ms") - pl.col("reference_avg_latency_ms"))
            .round(2)
            .alias("latency_mean_difference_ms"),
        ]
    )

    return combined.with_columns(
        [
            (pl.col("requests_mean_difference").abs() > requests_threshold).alias(
                "requests_is_drifting_flag"
            ),
            (pl.col("errors_mean_difference").abs() > errors_threshold).alias(
                "errors_is_drifting_flag"
            ),
            (pl.col("latency_mean_difference_ms").abs() > latency_threshold).alias(
                "latency_is_drifting_flag"
            ),
        ]
    )
