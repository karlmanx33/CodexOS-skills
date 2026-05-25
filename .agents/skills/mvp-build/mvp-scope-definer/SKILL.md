---
name: mvp-scope-definer
description: Decide what belongs in your MVP and what doesn’t to avoid scope creep.
---

# MVP Scope Definer

## Purpose

Create a clear, evidence‑based boundary around your MVP to ensure you build only what is necessary to validate the value, retention and monetisation hypotheses.  A disciplined scope keeps the team focused and prevents uncontrolled agentic scope creep.

## When to use

Use this skill when transitioning from research and prototype testing to building a functional MVP.  Revisit it whenever new evidence emerges or stakeholders push to add features.

## Inputs

- List of desired features or capabilities gathered from user feedback and internal brainstorming.
- Validated hypotheses (problem and solution statements) and evidence supporting them.
- User feedback from interviews and prototype tests, highlighting the most painful problems and desired outcomes.
- Constraints such as budget, time and technical limitations.

## Process

1. **Map features to hypotheses.**  For each desired feature, articulate which hypothesis or metric it is intended to test (value, retention, monetisation or referral).  Discard features that cannot be tied to a specific learning goal.
2. **Prioritise by evidence.**  Categorise features into:
   - **Must‑have:** directly test the core value hypothesis and provide the minimum path to deliver the promise.
   - **Should‑have:** enhance learning but can be postponed until must‑haves prove valuable.
   - **Nice‑to‑have:** enhancements or optimisations that do not affect early learning; defer until product‑market fit is evident.
3. **Identify dependencies and sequencing.**  Map dependencies among features (e.g. authentication needed before payment) and determine the order of implementation.  Where possible, remove dependencies by simplifying features.
4. **Define out‑of‑scope items.**  Explicitly list features and tasks that will **not** be included in the MVP.  Provide rationale tied to evidence or lack thereof.  This clarity helps push back on scope creep.
5. **Set constraints and exit criteria.**  Define the metrics and signals that will indicate whether the MVP has achieved product‑market fit (e.g. retention rates, willingness to pay).  Note constraints such as maximum build time or budget.
6. **Document the scope.**  Create a written `MVP_SCOPE.md` or similar context file describing the selected features, their rationale, sequencing, out‑of‑scope items, and success criteria.  Store this alongside your architecture and decision logs.
7. **Review and iterate.**  Revisit the scope after each feedback cycle.  Adjust categories based on new evidence or changing hypotheses but maintain discipline against “zero‑friction” additions without supporting data.

## Output

This skill outputs an **MVP scope document** including:

- Categorised list of features (must‑have, should‑have, nice‑to‑have) with rationale.
- Feature sequencing and dependency map.
- List of out‑of‑scope items and reasons for exclusion.
- Constraints and exit criteria for validating product‑market fit.
- Guidance on where to store and maintain the scope file.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Including features based on personal preference rather than evidence from user research.
- Treating market validation as complete after building a feature, rather than measuring actual user behaviour.
- Allowing features to slip into the must‑have category without explicit rationale.
- Failing to revisit the scope as new data emerges, leading to premature scaling or missing critical learning opportunities.

## Example prompt

```shell
$mvp-scope-definer
```



