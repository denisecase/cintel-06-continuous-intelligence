# Glossary

## Quick Lookup

Common terms used in this module:

- **System Monitoring** - observing system behavior using operational metrics
- **Signal** - a raw or derived metric used to understand system behavior
- **Anomaly** - an observation or condition that deviates from expectations
- **System State** - an overall assessment of system condition
- **Operational Decision** - an action informed by monitoring evidence

## System Monitoring

The practice of observing system behavior using measurements.
Monitoring systems help **detect issues early** and maintain **reliability**.
Examples:

- request volume
- error rates
- response times

## Signal

A **signal** is a raw or derived metric used to understand system behavior.

Signals may be direct measurements or values calculated from other metrics.
Well-designed signals help analysts recognize patterns, detect anomalies,
and assess system performance.

Examples include:

- request volume
- error rate
- average latency
- throughput

## Anomaly

An **anomaly** is an observation or condition that deviates from
expected system behavior.

Anomalies depend on context, domain knowledge, and defined expectations.

An anomaly does not necessarily indicate a failure.
It identifies a condition that may warrant investigation.

Examples include:

- unusually high error rates
- unusually slow response times
- unexpected drops in requests

## System State

The **system state** summarizes the overall condition of a monitored system.

System states translate monitoring signals into interpretable assessments.

State classifications depend on the monitoring rules and operational context.

Example classifications include:

- **STABLE** - system behavior is within defined expectations
- **DEGRADED** - system performance or reliability is reduced
- **FAILURE** - the system cannot provide one or more required functions

An overall stable state does not necessarily mean that every
individual observation is free of anomalies.

## Operational Decision

An action taken in response to monitoring information.
Examples include:

- investigating system errors
- scaling infrastructure
- rolling back a deployment

Continuous intelligence systems support operational decisions by providing timely information about system behavior.

---

[◄ Back to 🏠 Home](index.md)
