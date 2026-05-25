---
name: lightweight-prototype-planner
description: Define the smallest possible prototype that demonstrates the core value hypothesis.
---

# Lightweight Prototype Planner

## Purpose

Design a **minimal, focused prototype** that validates your core value hypothesis without committing to full product development.  The aim is to test whether users value the proposed solution enough to use it, return to it and ultimately pay for it.

## When to use

Use this skill after your problem hypothesis has been sharpened and you have a tentative solution concept.  It should precede any production coding and can be repeated for subsequent hypotheses or segments.

## Inputs

- Core user journey
- Critical assumptions
- Existing assets (if any)

## Process

1. **Define the core interaction.**  Based on your solution concept, identify the single most critical user interaction or workflow that embodies the value proposition.  This should be the activity that must be delightful or efficient for users to adopt the product.
2. **List critical assumptions.**  Document what must be true for this interaction to succeed (e.g. users are willing to provide data, integrate with existing tools, or change their behaviour).  Ask AI to enumerate potential failure points and consequences if assumptions do not hold.
3. **Select a prototyping method.**  Choose the lowest fidelity medium capable of demonstrating the core interaction: hand‑drawn wireframes, clickable mockups, Wizard‑of‑Oz prototypes where a human simulates backend functionality, or simple spreadsheets.  Avoid building full backend systems at this stage.
4. **Scope minimal features.**  List only the screens, inputs and outputs necessary to support the core interaction.  Exclude non‑essential features such as dashboards, onboarding flows or authentication unless they are critical to test.
5. **Define success criteria and feedback mechanisms.**  Clarify what constitutes success (e.g. user completes the task, expresses delight, indicates willingness to pay) and how you will measure it.  Plan to collect both qualitative feedback (comments, emotional reactions) and quantitative metrics (completion time, error rate).
6. **Recruit and test.**  Identify at least five target users who match your persona and schedule prototype sessions.  Ask them to complete the core interaction while you observe and ask follow‑up questions.  Use AI to help automate outreach and scheduling if needed.
7. **Synthesize and iterate.**  After testing, summarise findings, identify which assumptions were validated or invalidated, and decide whether to iterate, pivot or proceed to MVP development.

## Output

This skill returns a **prototype plan** that includes:

- The identified core interaction and associated critical assumptions.
- The chosen prototyping method and rationale.
- A list of minimal features/screens required.
- Defined success criteria and feedback collection methods.
- A testing plan with target user profile and next steps after testing.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Over‑scoping the prototype by including features unrelated to the core interaction.
- Skipping the documentation of assumptions, leading to unclear learning goals.
- Recruiting participants who do not match the target persona, resulting in misleading feedback.
- Treating positive reactions from a handful of users as proof of product‑market fit.

## Example prompt

```shell
$lightweight-prototype-planner
```



