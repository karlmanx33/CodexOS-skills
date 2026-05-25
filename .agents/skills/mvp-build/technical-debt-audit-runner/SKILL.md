---
name: technical-debt-audit-runner
description: Identify fragile areas, lack of tests and architectural drift before launch.
---

# Technical Debt Audit Runner

## Purpose

Detect structural issues, drift and maintainability risks in the codebase early.  A rigorous audit surfaces areas likely to create bugs, slow down development or break the architecture, enabling you to plan remediation before launching or scaling.

## When to use

Run this audit at regular intervals (e.g. every sprint) during MVP development and always before launch.  Repeat it after major refactors or when new contributors join the project.  Early detection of debt minimises costly fixes later.

## Inputs

- Codebase overview, including repository structure and key modules.
- Test coverage reports from unit, integration and end‑to‑end tests.
- Architecture brief and coding standards to compare against.
- List of dependencies and external services (optional).

## Process

1. **Run static analysis and linting.**  Use tools to detect code smells, high cyclomatic complexity, duplicated code, unused dependencies and inconsistent patterns.  Highlight files or functions with the highest complexity or change frequency.
2. **Check architecture conformance.**  Compare the actual implementation against your architecture brief.  Identify violations such as business logic leaking into controllers, infrastructure modules importing domain modules, or unapproved libraries.  Note any new dependencies added without review.
3. **Assess test coverage and reliability.**  Review coverage reports to find modules with low or zero test coverage.  Identify critical paths that lack integration or end‑to‑end tests.  Note any flaky tests or long execution times that could hinder CI/CD.
4. **Review documentation and comments.**  Check whether modules have up‑to‑date docstrings, comments and context references.  Missing documentation can slow down onboarding and maintenance.
5. **Classify technical debt.**  Categorise findings by severity (critical, high, medium, low) and type (architecture drift, complexity, missing tests, outdated dependencies).  Estimate the impact on user experience, performance, scalability and development velocity.
6. **Prioritise remediation and plan.**  Suggest a remediation plan organised into sprints.  For each debt item, provide actionable steps (e.g. refactor payment module to separate domain logic, write tests for authentication controller, remove unused library X).  Balance quick wins with deeper refactors to avoid burnout.

## Output

This skill produces a **technical debt audit report** that includes:

- A list of code smells, architecture violations, complexity hotspots and missing tests.
- Severity ratings and potential impact for each finding.
- Recommended remediation actions and a proposed sprint plan.
- Summary charts or tables showing coverage gaps and risk distribution.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Running the audit only once, leading to accumulation of debt between reviews.
- Ignoring architecture drift because “it works for now,” resulting in long‑term maintainability issues.
- Treating all debt as equal priority, causing teams to fix low‑impact issues instead of critical risks.

## Example prompt

```shell
$technical-debt-audit-runner
```



