---
name: problem-hypothesis-sharpener
description: Turn vague startup ideas into precise, testable problem hypotheses.
---

# Problem Hypothesis Sharpener

## Purpose

Transform a vague business idea into a precise, falsifiable problem hypothesis.  The goal is to articulate **who** has the problem, **how often** they experience it, **how severe** it is and **why existing solutions are inadequate**.  A well‑sharpened hypothesis anchors discovery and testing and prevents generic, non‑actionable assumptions.

## When to use

Invoke this skill at the start of the Idea Stage or anytime your understanding of the problem evolves.  It should be used **before** drafting interview questions, designing experiments or writing code, and revisited whenever new evidence surfaces that challenges your assumptions.

## Inputs

- Initial idea description
- Target user or segment
- Existing problem statement (optional)

## Process

1. **Decompose the idea.** Identify all vague or hand‑wavy phrases in your initial problem description.  Ask yourself who is implied by “users,” what constitutes “too long,” and what evidence currently supports those claims.
2. **Draft a specific hypothesis.** Rewrite the problem as a falsifiable statement that includes:
   - The **precise persona** (e.g. “in‑house legal teams at mid‑market companies”).
   - A **measurable pain** (e.g. “spend 3+ days per contract review cycle”).
   - The **root cause** or workaround (e.g. “because redlines are managed across email threads instead of a version‑controlled document”).
3. **Generate multiple versions.**  Produce a broad hypothesis, a narrower one and a testable interview hypothesis.  The broad version captures the general direction; the narrow version focuses on a specific segment; the interview version is short and designed to elicit agreement or disconfirmation in a conversation.
4. **Identify assumptions and evidence.**  List your underlying assumptions (e.g. size of companies, legal team structure, current tools).  For each, specify what evidence would validate or invalidate it.  Use AI to act as a devil’s advocate, surfacing disconfirming evidence and negative signals you may have missed.
5. **Plan research actions.**  Based on the riskiest assumptions, outline targeted research tasks (customer interviews, secondary research, competitor analyses) to gather supporting or contradictory data.

## Output

This skill returns:

- A **refined problem hypothesis** expressed as a clear, falsifiable statement.
- A **target user profile** describing the persona affected by the problem.
- An **assumption map** listing key assumptions and the evidence required to test them.
- A set of **research actions** to validate or invalidate the hypothesis.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Choosing a persona that is too broad or too narrow, leading to irrelevant evidence.
- Stopping at a single hypothesis without exploring alternative root causes.
- Failing to document assumptions, which can cause hidden bias during validation.
- Ignoring negative market signals or disconfirming evidence surfaced during the exercise.

## Example prompt

```shell
$problem-hypothesis-sharpener
```



