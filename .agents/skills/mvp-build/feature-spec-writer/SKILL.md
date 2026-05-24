---
name: feature-spec-writer
description: Write clear, concise specifications for new features before coding begins.
---

# Feature Specification Writer

## Purpose

Convert user stories and high‑level requirements into a detailed specification that guides Codex and human developers.  A good spec defines what to build, how it behaves, why it matters and how success will be measured.

## When to use

Use this skill after the MVP scope has been defined and an architecture brief exists.  It should precede any coding or task decomposition.  Create a feature spec for each significant capability or change.

## Inputs

- User story or requirement description, including the problem it solves and the user persona.
- Acceptance criteria (definition of done).
- Relevant context: architecture brief, project constraints, existing APIs or modules, measurement framework.

## Process

1. **Capture the purpose and user benefit.**  Summarise why this feature matters, which user journey it serves and how it contributes to the product’s value hypothesis.
2. **Define functional requirements.**  Write clear, testable requirements describing what the feature must do.  Include user flows, input/output behaviour, data validation rules and edge cases.
3. **Specify acceptance criteria.**  Create bullet‑point acceptance criteria (Given/When/Then) that delineate success conditions.  Where appropriate, include metrics such as response time thresholds or conversion rates.
4. **Document non‑functional requirements.**  Note performance targets, security and privacy constraints, accessibility standards, reliability requirements and legal/compliance considerations.
5. **Identify dependencies and integrations.**  List other services, APIs, modules, data models or third‑party providers the feature relies on.  Note any sequencing dependencies (e.g. must implement authentication first).
6. **Highlight out‑of‑scope elements.**  Explicitly list features or enhancements that are **not** part of this implementation to prevent scope creep.  Point to your MVP scope document for justification.
7. **Specify instrumentation and metrics.**  Define what should be measured (e.g. feature usage, error rates, conversion), how metrics will be collected and where they will feed into your measurement framework.
8. **Open questions and risks.**  Note any unresolved questions, assumptions or risks that may impact implementation.  Suggest research or experiments needed to resolve them.

## Output

This skill produces a **feature specification document** that includes:

- Purpose and user benefit statement.
- List of functional requirements and user flow descriptions.
- Acceptance criteria formatted for testing.
- Non‑functional requirements (performance, security, accessibility, scalability).
- Dependencies and integration points.
- Out‑of‑scope items.
- Instrumentation and metrics plan.
- Open questions and risks.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Writing vague requirements that cannot be tested or are open to interpretation.
- Omitting performance or security requirements, which may lead to rework.
- Failing to list dependencies, causing build failures or integration issues.
- Allowing scope creep by not explicitly defining what is out of scope.

## Example prompt

```shell
$feature-spec-writer
```)
