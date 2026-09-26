"""
continuous_intelligence_case.py - Project script (example).

Author: Denise Case
Date: 2026-03

System Metrics Data

- Data represents recent observations from a monitored system.
- Each row represents one observation of system activity.

- The CSV file includes these columns:
  - requests: number of requests handled
  - errors: number of failed requests
  - total_latency_ms: total response time in milliseconds

Purpose

- Read system metrics from a CSV file.
- Apply multiple continuous intelligence techniques learned earlier:
  - anomaly detection
  - signal design
  - simple drift-style reasoning
- Summarize the system's current state.
- Save the resulting system assessment as a CSV artifact.
- Log the pipeline process to assist with debugging and transparency.

Questions to Consider

- What signals best summarize the health of a system?
- When multiple indicators change at once, how should we interpret the system's state?
- How can monitoring data support operational decisions?

Paths (relative to repo root)

    INPUT FILE: data/system_metrics_case.csv
    OUTPUT FILE: artifacts/system_assessment_case.csv

Terminal command to run this file from the root project folder

    uv run python -m cintel.continuous_intelligence_case

OBS:
  Don't edit this file - it should remain a working example.
  Use as much of this code as you can when creating your own pipeline script,
  and change the logic to match the needs of your project.
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

from datafun_toolkit.logger import get_logger, log_header, log_path
import polars as pl

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P6", level="DEBUG")

# === DEFINE GLOBAL PATHS ===

ROOT_DIR: Final[Path] = Path.cwd()
DATA_DIR: Final[Path] = ROOT_DIR / "data"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts"

DATA_FILE: Final[Path] = DATA_DIR / "system_metrics_case.csv"
OUTPUT_FILE: Final[Path] = ARTIFACTS_DIR / "system_assessment_case.csv"

# === DEFINE THRESHOLDS ===

# Analysts need to know their data and
# choose thresholds that make sense for their specific use case.

MAX_ERROR_RATE: Final[float] = 0.05
MAX_AVG_LATENCY: Final[float] = 40.0

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline.

    log_header() logs a standard run header.
    log_path() logs repo-relative paths (privacy-safe).
    """
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DATA_FILE", DATA_FILE)
    log_path(LOG, "OUTPUT_FILE", OUTPUT_FILE)

    # Ensure artifacts directory exists
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    # ----------------------------------------------------
    # STEP 1: READ SYSTEM METRICS
    # ----------------------------------------------------
    df = pl.read_csv(DATA_FILE)

    LOG.info(f"STEP 1. Loaded {df.height} system records")

    # ----------------------------------------------------
    # STEP 2: DESIGN SIGNALS
    # ----------------------------------------------------
    # This step connects to Module 3: Signal Design.
    # Create useful signals derived from raw system metrics.

    LOG.info("STEP 2. Designing signals from raw metrics...")

    df = df.with_columns(
        [
            (pl.col("errors") / pl.col("requests")).alias("error_rate"),
            (pl.col("total_latency_ms") / pl.col("requests")).alias("avg_latency_ms"),
        ]
    )

    # ----------------------------------------------------
    # STEP 3: DETECT ANOMALIES
    # ----------------------------------------------------
    # This step connects to Module 2: Anomaly Detection.
    # Check whether signal values exceed reasonable thresholds.

    LOG.info("STEP 3. Checking for anomalies in system signals...")

    anomalies_df = df.filter(
        (pl.col("error_rate") > MAX_ERROR_RATE)
        | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
    )
    LOG.info(
        f"STEP 3. Using thresholds: MAX_ERROR_RATE={MAX_ERROR_RATE}, "
        f"MAX_AVG_LATENCY={MAX_AVG_LATENCY}"
    )

    LOG.info(f"STEP 3. Anomalies detected: {anomalies_df.height}")

    # ----------------------------------------------------
    # STEP 4: SUMMARIZE CURRENT SYSTEM STATE
    # ----------------------------------------------------
    # This step brings together ideas from earlier modules:
    # - Module 3: Signal Design
    # - Module 2: Anomaly Detection
    # It then adds the main goal of Module 6:
    # assess the overall state of the system.

    # NOTE: recipes for column creation and filtering
    # can be done in place as we add signals and logic to a DataFrame.
    # When logic is more complex, it can be helpful to
    # break it into multiple steps/recipes
    # for readability and debugging as shown previously.

    LOG.info("STEP 4. Summarizing system state from monitored signals...")

    summary_df = df.select(
        [
            pl.col("requests").mean().alias("avg_requests"),
            pl.col("errors").mean().alias("avg_errors"),
            pl.col("error_rate").mean().alias("avg_error_rate"),
            pl.col("avg_latency_ms").mean().alias("avg_latency_ms"),
        ]
    )

    # Add a simple assessment label
    summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > MAX_ERROR_RATE)
            | (pl.col("avg_latency_ms") > MAX_AVG_LATENCY)
        )
        .then(pl.lit("DEGRADED"))
        .otherwise(pl.lit("STABLE"))
        .alias("system_state")
    )

    LOG.info("STEP 4. System assessment completed")

    # ----------------------------------------------------
    # STEP 5: SAVE SYSTEM ASSESSMENT
    # ----------------------------------------------------
    summary_df.write_csv(OUTPUT_FILE)

    LOG.info(f"STEP 5. Wrote system assessment file: {OUTPUT_FILE}")

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
