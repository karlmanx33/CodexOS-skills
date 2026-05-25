---
name: codex-session-log-updater
description: Update project context after each Codex session to maintain an accurate trail of changes.
---

# Codex Session Log Updater

## Purpose

Maintain a reliable historical record of each Codex session.  By documenting changes, decisions and their rationale, you prevent context drift, reduce duplication of work and make it easier for humans and agents to follow the project’s evolution.

## When to use

Use at the end of any session where Codex writes or modifies code.

## Inputs

- Summary of changes made (files modified, functions added/removed, refactors)
- Rationale for decisions and trade‑offs
- Issues encountered, technical debt introduced, open questions

## Process

1. **Record session summary.**  At the end of the session, summarise what was accomplished: tasks completed, files modified, functions or modules added/removed, dependencies introduced, tests written and bugs fixed.
2. **Document decisions.**  Append an entry to `DECISIONS.md` including the date, context, decision, alternatives considered, assumptions, evidence and rationale.  Note any trade‑offs (e.g. performance vs. simplicity) and deferred considerations.
3. **Update project context.**  Update `PROJECT_CONTEXT.md` and `ARCHITECTURE.md` to reflect new modules, data models, API endpoints, configuration changes or constraints.  Ensure that comments in code and architecture docs remain consistent.
4. **Flag technical debt and risks.**  Identify any shortcuts taken or areas requiring refactor.  Capture these items in a debt/backlog list along with suggested remediation priority.
5. **List follow‑ups.**  Record open questions, blocked tasks, and planned next steps.  Assign owners or schedule subsequent Codex sessions to address them.
6. **Commit and sync.**  Make sure all context files are saved and committed alongside code changes.  This ensures that future sessions have access to up‑to‑date context.

## Output

This skill results in:

- Updated `DECISIONS.md` entries detailing decisions and their rationale.
- Updated `PROJECT_CONTEXT.md` and `ARCHITECTURE.md` reflecting new components and constraints.
- A documented list of technical debt items and follow‑up actions.
- A summary log that can be referenced in subsequent sessions.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Forgetting to document small decisions, which later become sources of confusion or rework.
- Failing to update all relevant context files, resulting in inconsistent or outdated documentation.
- Not flagging introduced technical debt, leading to accumulated structural risk.

## Example prompt

```shell
$codex-session-log-updater
```



