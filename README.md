# cintel-06-continuous-intelligence

[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://denisecase.github.io/cintel-06-continuous-intelligence/)
[![CI Status](https://github.com/denisecase/cintel-06-continuous-intelligence/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/denisecase/cintel-06-continuous-intelligence/actions/workflows/ci-python-zensical.yml)
[![Python 3.14](https://img.shields.io/badge/python-3.14%2B-blue?logo=python)](pyproject.toml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)

> Professional Python project for continuous intelligence.

Continuous intelligence systems monitor data streams, detect change, and respond in real time.
This course builds those capabilities through working projects.

In the age of generative AI, durable skills are grounded in real work:
setting up a professional environment,
reading and running code,
understanding the logic,
and pushing work to a shared repository.
Each project follows the structure of professional Python projects.
We learn by doing.

## This Project

This project brings together several techniques used in continuous intelligence systems.

The goal is to copy this repository,
set up your environment,
run the example analysis,
and explore how monitoring techniques can be combined
to assess the current state of a system.

Run the example pipeline, read the code, and see how:

- raw system metrics are transformed into useful signals
- anomalies are detected in those signals
- monitoring results are summarized to assess system health

This project demonstrates how monitoring data can support operational awareness and decision-making.

This module serves as a capstone:
it encourages you to combine techniques developed
in earlier modules into a simple continuous intelligence pipeline:

- Module 2. anomaly detection
- Module 3. signal design
- Module 4. rolling monitoring
- Module 5. drift comparison
- Module 6. system assessment (integration).

## Data

The example pipeline reads system metrics from:

`data/system_metrics_case.csv`

Each row represents one observation of system activity.

The pipeline derives signals such as
**error rate** and **average latency**,
checks for anomalous conditions,
and produces a summary assessment of system behavior.

The dataset includes a short period of degraded performance
so that monitoring signals and anomaly detection
produce visible results.

## Working Files

You'll work with just these areas:

- **data/** - it starts with the data
- **docs/** - tell the story
- **src/cintel/** - where the magic happens
- **pyproject.toml** - update authorship & links
- **zensical.toml** - update authorship & links

## Instructions

Follow the [step-by-step workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Read & Understand**
3. Phase 3. **Take Ownership**
4. Phase 4. **Make a Technical Modification**
5. Phase 5. **Apply the Skills to a New Problem**

## Challenges

Challenges are expected.
Sometimes instructions may not quite match your operating system.
When issues occur, share screenshots, error messages, and details about what you tried.
Working through issues is part of implementing professional projects.

## Success

After completing Phase 1. **Start & Run**, you'll have your own GitHub project, running on your machine, and running the example will print out:

```shell
========================
Pipeline executed successfully!
========================
```

And a new file named `project.log` will appear in the project folder.

Once you see it, you're 90% of the way there.
After that, you'll just make the project yours and get started exploring.

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

### Get a Copy of the Project (Once)

Open a **machine terminal** in your `Repos` folder.
Copy and paste one command and hit Enter or Return afterwards to run it.

```shell
git clone https://github.com/username/cintel-06-continuous-intelligence

cd cintel-06-continuous-intelligence
code .
```

See the [workflow guide](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/) to learn more.

### Initialize or Update the Python Environment

With the project open in VS Code, open a VS Code terminal.
Paste each command and hit Enter or Return after to run it.

```shell
uvx pup-clean --delete
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync
uv audit
```

### Set Up and Run Git Hooks

Set up and run the git hooks to perform
some basic checks automatically before
any changes get pushed to GitHub.

In the VS Code terminal,
paste each command and hit Enter or Return after to run it.

```shell
uv run prek install --force
uv run prek update --freeze --cooldown-days 7

git add -A
uv run prek run --all-files
# repeat if changes were made
uv run prek run --all-files
```

### Run the Project as Python Module

Run the project code as a Python module.

```shell
uv run python -m cintel.continuous_intelligence
```

### Run the Project as Reactive App

Run the project app.py.

```shell
uv run marimo run app.py
```

In the terminal, you'll see "Running app.py".
Click the URL: http://localhost:2718 to open your app.

To stop, click in the VS Code terminal.
Then hit **CTRL+c** (**CTRL** key and **c** key simultaneously).

### Run Common Chores

Run linters, formatters, type checks, tests, and
build the documentation.

```shell
uv run ruff check . --fix
uv run ruff format .

uv run ty check
uv run python -m pytest
uv run python -m zensical build
```

### Git add-commit-push to GitHub

After making useful changes, save your work to GitHub.

```shell
git add -A
git commit -m "describe your changes in quotes"
git push -u origin main
```

## Notes

- Use the **UP ARROW** and **DOWN ARROW** in the terminal to scroll through past commands.
- Use `CTRL+f` to find (and replace) text within a file.
