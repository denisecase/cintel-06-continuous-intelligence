# Project Instructions

## WEDNESDAY: Complete Workflow Phase 1-3

Follow the instructions in
[⭐ **Workflow: Apply Example**](https://denisecase.github.io/pro-analytics-02/workflow-b-apply-example-project/).

Complete:

1. Phase 1. **Start & Run**
2. Phase 2. **Read & Understand**
3. Phase 3. **Take Ownership**

## FRIDAY/SUNDAY: Complete Workflow Phases 4-5

Complete:

1. Phase 4. **Make a Technical Modification**
2. Phase 5. **Apply the Skills to a New Problem**

## Topic

System assessment using continuous intelligence techniques.

In this project, you combine several techniques introduced earlier
in the course to interpret the **current state of a monitored system**.

Continuous intelligence systems often:

- measure system activity
- transform raw data into useful signals
- detect unusual behavior
- summarize the overall state of the system

This project demonstrates how those steps work together.

## Learning Objectives

After completing this project, you should be able to:

- interpret signals that describe system behavior
- detect anomalous conditions in system metrics
- summarize system health using derived signals
- communicate system state clearly through data artifacts and documentation

## Example Code

The example file is located in:

```text
src/cintel/continuous_intelligence.py
```

It demonstrates:

- reading system metrics from a dataset
- designing signals from raw system measurements
- detecting anomalous signal values
- summarizing system metrics
- assigning a simple system health state

Run the example and review the code before creating your own version.

## Dataset

The example dataset is located in the `data/` folder.

Example fields include:

- `requests`
- `errors`
- `total_latency_ms`

Each row represents one observation of system behavior.

Signals such as **error rate** and **average latency**
help analysts interpret system performance.

## Your Phase 4: Technical Modification Task

Using the example as a guide:

1. Copy `src/cintel/continuous_intelligence_case.py`.
2. Rename the copy to `src/cintel/continuous_intelligence_yourname.py`.
3. Run your copied file to confirm it executes correctly.
4. Make a small modification to the pipeline.

Examples of modifications include:

- adding an additional monitoring signal
- adding another anomaly condition
- adjusting system thresholds
- improving logging or output structure

Run the program again and verify that your modification works.

## Phase 5: Apply the Skills

In this phase, apply the techniques from this course
to your own monitoring scenario.

You may choose to:

- extend the current monitoring pipeline
- apply the techniques to a different dataset
- add new signals or anomaly logic
- experiment with different system health rules

Describe your approach on the `docs/index.md` page.

Explain:

- what signals you used
- how anomalies were detected
- how the system state was determined
- what the results suggest about system behavior

Continuous intelligence systems help organizations
monitor complex systems and make **informed operational decisions**.

If you would like to apply these skills to a real dataset
instead of the provided example data, see suggested datasets:

https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/
