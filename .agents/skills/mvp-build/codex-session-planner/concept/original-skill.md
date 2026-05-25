---
name: codex-session-planner
description: Plan a Codex implementation session with clear goals, constraints and expected outputs.
---

# Codex Session Planner

## Purpose

Ensure each Codex implementation session is focused and context‑rich.  A good plan prevents the model from meandering, reduces code drift and technical debt, and aligns its actions with your architecture and scope constraints.

## When to use

Use this skill **before every coding or refactoring session**.  It is particularly important when building new features, restructuring the architecture, or applying large‑scale changes.  Small one‑line edits may not require a full plan but still benefit from clarifying the goal.

## Inputs

- Feature specification or ticket
- Relevant files or code snippets
- Constraints (time, languages, frameworks)

## Process

1. **Clarify the objective.**  Write a concise goal for the session.  State what you want Codex to accomplish (e.g. “Implement user login with JWT authentication,” “Refactor the payment service to separate domain logic from controllers”).
2. **Provide context.**  Gather all relevant files, modules, architecture documents and prior decisions.  Include project context files (e.g. `PROJECT_CONTEXT.md`, `ARCHITECTURE.md`, `DECISIONS.md`) so Codex understands the current design and avoids unintended drift.
3. **Define constraints and non‑goals.**  Specify languages, frameworks, coding standards, performance requirements, and items **not** to address in this session (e.g. “Do not implement payment provider integrations yet”).  Include architectural principles (e.g. “keep business logic decoupled from adapters”) and dependencies to avoid.
4. **Describe expected outputs.**  Define what deliverable should result from the session: a pull request, a new module file, a set of unit tests, a refactored component, etc.  Clarify acceptance criteria and metrics for success.
5. **Plan for follow‑up.**  Note where the resulting changes should be documented and what subsequent sessions will be required.  Decide who will review the code (you or another developer) and how the context files will be updated afterward.

## Output

This skill returns a **session plan** containing:

- A succinct objective statement.
- A list of relevant files, modules and context documents for Codex to ingest.
- Clear constraints, non‑goals and coding standards.
- Description of the expected deliverable and acceptance criteria.
- Follow‑up actions and documentation guidelines.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Starting a session without providing enough context, leading Codex to misinterpret architecture or naming conventions.
- Failing to specify non‑goals, causing scope creep or unintended refactoring.
- Omitting acceptance criteria, resulting in output that is difficult to evaluate.

## Example prompt

```shell
$codex-session-planner
```



