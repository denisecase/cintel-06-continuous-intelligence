"""app.py - Reactive marimo app for this project.

Marimo adds reactive controls.
Every function below is a marimo cell.

RUN LOCALLY:

  uv run marimo edit app.py     # edit
  uv run marimo run  app.py     # run as an app (CTRL+c quits)

WASM DEPENDENCIES:

Under WebAssembly (emscripten) the browser has no project environment.
This app uses only marimo, which is already present in the marimo WASM
runtime. If a later version adds third-party packages, the first cell
installs them with micropip when running under WASM.

NO LOGGING:

A browser-based WASM app has no persistent Python server to store log files,
so this notebook configures no logging.

PLAN CELLS FIRST

1. Imports (returns shared imports and constants)
2. Opening title and introduction (Markdown)
3. Closing (Markdown)

Note: marimo triggers @app.cell functions automatically; we never call them.
The names starting with "_" are for our own organization; the engine ignores
them.

HOW MARIMO NOTEBOOKS WORK

Each cell is a FUNCTION.
The return value of one cell can be passed as an argument to another cell.
We never call the functions, so they don't need names other than `_` (underscore).
(You can give them names if you want, but the notebook engine ignores them.)

The notebook is REACTIVE: when a cell's code or inputs change,
the notebook engine reruns that cell and every cell that depends on it.

The notebook is always CONSISTENT with outputs reflecting current inputs.

The first cell imports all dependencies, so the notebook is SELF-CONTAINED.

All later cells include their dependencies in their argument list.
Some other cells return values that can be used in other cells.
A cell displays the value of its last expression.

A cell whose last line is an assignment or a bare return
(like data and view cells) displays nothing;
only markdown, control, and render cells are meant to show.

RULE: Each variable must be defined in exactly one cell.
Defining the same name in two cells is a marimo error.

INPUT WIDGETS/CONTROLS: A cell that builds an input widget
resets that widget to its default every time the cell reruns.
marimo reruns a cell whenever any argument in its signature changes.
So a widget-building cell must depend only on what genuinely determines its options.
"""

# === ONLY THIS AT THE TOP OF THE FILE ===

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")

# === FIRST CELL IMPORTS AND RETURNS DEPENDENCIES TO MAKE IT SELF-CONTAINED ===


@app.cell
def _():
    import marimo as mo

    return (mo,)


# ===  TYPICALLY START WITH A MARKDOWN TITLE AND OPENING ===


@app.cell
def _(mo):
    mo.md(r"""
    # I Can Build Web Apps with Marimo!

    Add your special message here:
    """)


# ===  TYPICALLY END WITH A MARKDOWN SOURCE LINK AND CLOSING ===


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
