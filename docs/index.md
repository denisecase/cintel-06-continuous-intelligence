# Continuous Intelligence System Assessment

Continuous Intelligence | Project 06 | Example Report

## Overview

This project integrates signal design,
anomaly detection, and system assessment
into a continuous intelligence pipeline.

The objective is to transform operational measurements
into interpretable indicators of system behavior
and produce an overall assessment of system state.

## Data

The example dataset contains 60 observations
of system activity.

Each observation records:

- Requests handled.
- Errors encountered.
- Total response time in milliseconds.

The dataset includes a period of elevated
errors and response times.

[View Example Dataset](https://github.com/denisecase/cintel-06-continuous-intelligence/blob/main/data/system_metrics.csv)

## Methods

The pipeline applies three analytical steps.

### 1. Signal Design

Raw measurements are transformed into:

- Error rate: errors divided by requests.
- Average latency: total latency divided by requests.

### 2. Anomaly Detection

Individual observations are flagged when:

- Error rate exceeds 5%, or
- Average latency exceeds 40 milliseconds.

### 3. System Assessment

The pipeline calculates mean values
across all observations.

It classifies the overall system state as:

- `STABLE` when neither mean signal exceeds its threshold.
- `DEGRADED` when either mean signal exceeds its threshold.

## Results

The example produces the following assessment.

| Metric               |   Result |
| -------------------- | -------: |
| Average requests     |   157.35 |
| Average errors       |     4.43 |
| Average error rate   |    2.65% |
| Average latency      | 33.71 ms |
| Overall system state |   STABLE |

The pipeline also identifies **7 anomalous observations**
using its individual-observation thresholds.

[View System Assessment](https://github.com/denisecase/cintel-06-continuous-intelligence/blob/main/artifacts/system_assessment.csv)

## Interpretation

The overall assessment is `STABLE`
because the average error rate and latency
remain below their configured thresholds.

However, several individual observations
exceed the anomaly thresholds.

This distinction is important.

A system may appear stable when summarized
across an entire observation period
while experiencing shorter episodes
of degraded performance.

Monitoring should consider both overall
conditions and localized anomalies.

## Limitations

The example assessment is based on aggregate
means and fixed thresholds.

It does not yet incorporate rolling-window analysis,
reference-period drift comparisons,
or persistent alerting.

The final assessment artifact contains summary metrics
but does not preserve the individual anomaly records.

A more complete system could retain
observation-level evidence and combine
rolling monitoring, drift detection,
and system-state classification.

## Conclusion

Continuous intelligence connects measurements,
signals, analytical rules, and interpretation.

The example demonstrates how several techniques
can contribute to an assessment of system behavior.

Its most important finding is that
**an overall stable classification does not guarantee
that every observation was within acceptable limits.**

Effective monitoring requires both summary assessments
and sufficient detail to investigate anomalous conditions.

## Documentation Index

- **Home** - this landing page
- [**Project Instructions**](project-instructions.md)
- [**Glossary**](glossary.md)
- [**API**](api.md)
- [**Reactive App**](./app/index.html)

## Project Links

- [GitHub Repository](https://github.com/denisecase/cintel-06-continuous-intelligence)
- [Example Pipeline](https://github.com/denisecase/cintel-06-continuous-intelligence/blob/main/src/cintel/continuous_intelligence.py)
- [Results and Artifacts](https://github.com/denisecase/cintel-06-continuous-intelligence/tree/main/artifacts)

## Project Resources

- [Project Instructions](project-instructions.md)
- [Professional Python Guide](https://denisecase.github.io/pro-analytics-02/)
- [Professional Python Project Explainer](https://pup-pack.github.io/professional-python-project-explainer/).
- [Suggested Datasets](https://denisecase.github.io/pro-analytics-02/reference/datasets/cintel/)
