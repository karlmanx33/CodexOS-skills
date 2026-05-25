---
name: mvp-measurement-framework-builder
description: Define metrics to evaluate activation, retention, conversion and referral during MVP testing.
---

# MVP Measurement Framework Builder

## Purpose

Create a data‑driven framework for evaluating whether your MVP delivers real value.  By defining activation, retention, conversion and referral metrics upfront, you avoid chasing vanity numbers and ensure everyone knows how product‑market fit will be measured.

## When to use

Develop this framework **before** releasing your MVP to any external users.  Revisit it after each iteration to refine definitions and targets based on learnings.

## Inputs

- Core user journey(s) you want to measure (e.g. onboarding, core action, referral).
- Business model and revenue assumptions (if monetisation is in scope).
- Existing analytics tooling or instrumentation capabilities (e.g. Segment, PostHog, custom logs).
- Benchmarks or expectations for similar products (optional).

## Process

1. **Map the user journey.**  Break down the key steps a user takes from discovery to becoming a loyal customer.  Identify meaningful actions that indicate value creation (e.g. completing a workflow, saving an item).
2. **Define activation metrics.**  Decide what constitutes a successful activation.  For example, activation may occur when a user completes the core value action within a certain time after signup.  Specify the metric formula (numerator/denominator) and target threshold.
3. **Define retention metrics.**  Decide how you will measure retention at Day 7, Day 14, Day 30 or other intervals.  Consider cohort analysis and whether returning to perform the core action counts as retention.
4. **Define conversion and revenue metrics.**  If monetisation is part of the MVP, identify metrics such as conversion rate from free to paid, average revenue per user (ARPU), or payback period.  If not, note that monetisation metrics will be defined later.
5. **Define referral and virality metrics.**  If referrals are important, decide how to measure word‑of‑mouth (e.g. number of invites sent per active user, Net Promoter Score).
6. **Specify instrumentation and tracking.**  Determine what events need to be tracked, where to place analytics hooks, and how data will be stored (e.g. event logs, database tables).  Consider data privacy and consent requirements.
7. **Set baseline thresholds and hypotheses.**  Establish target values or ranges that would indicate product‑market fit for each metric.  Document assumptions behind these targets.
8. **Plan analysis cadence and tooling.**  Decide how often metrics will be reviewed (daily, weekly) and who will monitor them.  Choose tools or dashboards for visualising metrics.  Schedule regular PMF diagnostic reviews.
9. **Prepare false PMF safeguards.**  Identify patterns that could create a false sense of product‑market fit (e.g. traffic spikes from marketing, friends using the product out of loyalty).  Document rules to adjust metrics accordingly.

## Output

This skill outputs an **MVP measurement plan** that includes:

- Definitions of activation, retention, conversion and referral metrics with formulas and targets.
- Mapping of events and instrumentation needed to capture these metrics.
- Baseline thresholds and hypotheses for product‑market fit.
- Analysis cadence, roles and chosen analytics tools.
- Guidelines to recognise and filter out false PMF signals.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Relying on vanity metrics (e.g. signups) rather than meaningful behaviour metrics.
- Failing to instrument key actions, leading to incomplete data.
- Setting arbitrary targets without benchmarking or linking to hypotheses.
- Ignoring outliers or misinterpreting spikes from marketing or friends as product‑market fit.

## Example prompt

```shell
$mvp-measurement-framework-builder
```



