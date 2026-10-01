# Lean Six Sigma / DMAIC Case Study

**Status: worked educational case using invented changeover observations.**

## Define

Teaching scenario: a packaging line experiences variable format-change durations. Scope covers the interval from the last good unit of the previous format to the first accepted good unit of the new format. This definition includes quality acceptance, so a faster restart alone is not success.

## Measure

`sample-data.json` contains 12 baseline and 12 illustrative later observations, in minutes. Run `python analyze.py` to reproduce means, medians, sample standard deviations and the descriptive percentage difference. Data quality work for a real case would verify timestamps, format mix, interruptions and consistent acceptance criteria.

## Analyze

Candidate explanations for investigation: readiness of change parts, material availability, adjustment iterations and first-piece approval time. These are **hypotheses**, not demonstrated root causes. A real study would connect each hypothesis to event-level observations and compare like-for-like formats.

## Improve

Proposed teaching interventions: stage approved change parts, clarify task ownership and standardize the handoff to quality. The later synthetic observations illustrate a possible comparison; they do not measure an intervention actually implemented by Mario or any employer.

## Control

Use `control-plan.md` to assign measurement owners, review cadence, reaction responsibilities and evidence. Before interpreting a change, collect an adequate stable series and review product mix and measurement consistency. This small dataset does not establish statistical control or causality.

## Method reference

[ASQ — DMAIC](https://asq.org/quality-resources/dmaic). Accessed 2026-10-01. The scenario and observations here are original synthetic examples.

## Español

Caso didáctico DMAIC de cambios de formato. El análisis es reproducible, pero sus cifras no son logros laborales, ahorros reales ni una certificación Six Sigma. El plan distingue hipótesis, acciones propuestas y evidencia pendiente.
