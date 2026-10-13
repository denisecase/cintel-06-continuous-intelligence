"""app.py - Reactive marimo app for this project.

Marimo adds reactive controls.
Every function below is a marimo cell.

RUN LOCALLY:

  uv run marimo edit app.py     # edit
  uv run marimo run  app.py     # run as an app (CTRL+c quits)

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment.
This app uses polars in addition to marimo, so the first cell installs
polars with micropip when running under WASM.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (installs WASM deps, returns shared imports and constants)
2. Opening title and introduction (Markdown)
3. Load system metrics and design signals (same cell handles local and
   WASM environments, via cintel.utils_system)
4. Threshold controls (sliders)
5. Detect anomalies and summarize system state (same logic as the CLI
   pipeline)
6. Show the results (state label + summary + anomalies table)
7. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with = "0.25.0"

app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPENDENCIES TO MAKE IT SELF-CONTAINED ===


@app.cell
async def _():
    import sys

    if sys.platform == "emscripten":
        import micropip

        await micropip.install("polars")

    import marimo as mo
    import polars as pl

    from cintel.utils_system import design_signals, load_system_metrics

    return design_signals, load_system_metrics, mo, pl, sys


# === TITLE AND INTRODUCTION ===


@app.cell
def _(mo):
    mo.md(r"""
    # Continuous Intelligence

    Brings together signal design (Module 3) and anomaly detection
    (Module 2) to assess the overall state of a system:
    **STABLE** or **DEGRADED**.

    Move the sliders below to change what counts as degraded.
    """)


# === LOAD SYSTEM METRICS AND DESIGN SIGNALS ===


@app.cell
def _(design_signals, load_system_metrics, mo, sys):
    """Load system metrics and design signals. Two environments, one cell.

    Locally, polars reads the CSV from data/.
    Under WASM (emscripten), Pyodide's open_url() fetches the CSV from
    public/ and load_system_metrics() reads it from there instead.
    """
    notebook_location = mo.notebook_location()

    if notebook_location is None:
        raise RuntimeError("Unable to determine notebook location.")

    filename = "system_metrics.csv"

    if sys.platform == "emscripten":
        from pyodide.http import open_url  # ty: ignore[unresolved-import]

        data_url = notebook_location / "public" / filename
        df = load_system_metrics(open_url(str(data_url)))
    else:
        data_path = notebook_location.parents[1] / "data" / filename
        df = load_system_metrics(data_path)

    df = design_signals(df)
    return (df,)


# === THRESHOLD CONTROLS ===


@app.cell
def _(mo):
    max_error_rate = mo.ui.slider(
        0.0, 0.5, value=0.05, step=0.01, label="Max error rate"
    )
    max_avg_latency = mo.ui.slider(0, 200, value=40, label="Max avg latency (ms)")
    mo.hstack([max_error_rate, max_avg_latency])
    return max_avg_latency, max_error_rate


# === DETECT ANOMALIES AND SUMMARIZE SYSTEM STATE (SAME LOGIC AS THE CLI PIPELINE) ===


@app.cell
def _(df, max_avg_latency, max_error_rate, pl):
    anomalies_df = df.filter(
        (pl.col("error_rate") > max_error_rate.value)
        | (pl.col("avg_latency_ms") > max_avg_latency.value)
    )

    summary_df = df.select(
        [
            pl.col("requests").mean().alias("avg_requests"),
            pl.col("errors").mean().alias("avg_errors"),
            pl.col("error_rate").mean().alias("avg_error_rate"),
            pl.col("avg_latency_ms").mean().alias("avg_latency_ms"),
        ]
    )

    summary_df = summary_df.with_columns(
        pl.when(
            (pl.col("avg_error_rate") > max_error_rate.value)
            | (pl.col("avg_latency_ms") > max_avg_latency.value)
        )
        .then(pl.lit("DEGRADED"))
        .otherwise(pl.lit("STABLE"))
        .alias("system_state")
    )
    return anomalies_df, summary_df


# === SHOW THE RESULTS ===


@app.cell
def _(mo, summary_df):
    state = summary_df.to_dicts()[0]["system_state"]
    mo.md(f"## System state: **{state}**")


@app.cell
def _(mo, summary_df):
    mo.ui.table(summary_df)


@app.cell
def _(anomalies_df, mo):
    mo.md(f"**{anomalies_df.height} anomalous observations** at these thresholds.")


@app.cell
def _(anomalies_df, mo):
    mo.ui.table(anomalies_df)


# === TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


@app.cell
def _(mo):
    mo.md(r"""
    ---
    [😊 Learn more at marimo.io](https://marimo.io/)
    ---

    **Running locally?**
    To stop the app, click in the VS Code terminal,
    then press **CTRL** and **c** together (CTRL+c).
    When it asks "Are you sure you want to quit? (y/N)",
    type **y** and press **Enter**.
    ---
    """)


if __name__ == "__main__":
    app.run()
