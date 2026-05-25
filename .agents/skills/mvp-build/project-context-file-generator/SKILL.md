---
name: project-context-file-generator
description: Produce persistent context files for Codex such as AGENTS.md, PROJECT_CONTEXT.md and DECISIONS.md.
---

# Project Context File Generator

## Purpose

Create and maintain persistent project context files that Codex and human developers can rely on.  These files capture architecture, decisions, constraints, scope and agent instructions, reducing confusion and preventing architectural drift or duplication across sessions.

## When to use

Use this skill when you initialise a new repository, after a major architecture or scope change, or whenever context files become outdated.  It complements the session log updater by periodically consolidating information into authoritative documents.

## Inputs

- The latest architecture brief (from the architecture generator skill).
- Recent decision log entries summarising key product and technical choices.
- Team roles and responsibilities (to define ownership and review processes).
- MVP scope document and other context (optional but recommended).

## Process

1. **Generate/refresh `AGENTS.md`.**  Describe the purpose of the repository, the principles guiding Codex interactions (e.g. validating before building, maintaining context), coding standards and any agent roles (e.g. coding agent vs. review agent).  Include rules on how to update context files and how to handle failures or errors.
2. **Generate/refresh `PROJECT_CONTEXT.md`.**  Summarise the current architecture (from your architecture brief), MVP scope, target user personas, user journeys, constraints, success metrics and known technical limitations.  This file acts as a high‑level briefing for new contributors or agents.
3. **Update `DECISIONS.md`.**  Consolidate recent decision log entries into an ordered list.  For each decision include the date, context, decision statement, alternatives considered, assumptions, evidence, trade‑offs and outcome.  Remove outdated or superseded decisions while preserving historical context.
4. **Generate or update other context files.**  If your repository uses additional documents (e.g. `MVP_SCOPE.md`, `ARCHITECTURE.md`), ensure they are referenced in `PROJECT_CONTEXT.md` and cross‑linked.
5. **Persist the files.**  Save or overwrite the context files in the repository root or `.agents` folder.  Ensure they are version‑controlled so that future Codex sessions load the latest information.
6. **Notify the team.**  Suggest notifying team members about updated context files so everyone uses the latest guidance.  Consider automating a check to ensure these files are present in subsequent sessions.

## Output

This skill produces fresh versions of `AGENTS.md`, `PROJECT_CONTEXT.md` and `DECISIONS.md` (and other context files if provided).  Each file reflects the latest architecture, scope, decisions, principles and roles.  The output should also include a summary of what changed and recommendations for adoption.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Allowing context files to become stale, leading Codex to act on outdated assumptions.
- Omitting key decisions or architecture changes, causing inconsistent design choices.
- Storing context files outside version control, making it hard to track changes over time.

## Example prompt

```shell
$project-context-file-generator
```



