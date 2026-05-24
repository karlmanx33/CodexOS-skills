---
name: codex-startup-lifecycle-mapper
description: Map your startup to Idea, MVP, Launch or Scale to select the right workflows.
---

# Codex Startup Lifecycle Mapper

## Purpose

Identify which stage of the AI‑native startup lifecycle (Idea, MVP, Launch or Scale) your company, product or feature is currently in.  Knowing your stage ensures you use the right set of Codex skills, avoid premature scaling and focus on the evidence needed to progress.

## When to use

Run this skill whenever you begin a new venture or feature, and again whenever you’re uncertain about your current stage.  Reassessing regularly prevents you from skipping critical steps (like validation) or sticking too long in an exploratory phase.

## Inputs

- Short description of your product
- Current progress: interviews, prototypes, paying users

## Process

1. **Summarise current status.**  Capture a concise description of the product or feature along with evidence of progress: number of customer interviews completed, prototypes tested, active users, paying customers, revenue, engagement and retention metrics.
2. **Apply stage criteria.**  Compare the evidence to the definitions of the four lifecycle stages:
   - **Idea Stage:** You have a problem hypothesis and are conducting research and customer interviews.  No production code has been built.  Exit when a specific, validated problem and solution hypothesis exist.
   - **MVP Stage:** You have built a minimal prototype or MVP to test whether users find value, return, pay and refer.  Evidence is focused on activation, retention and conversion.  Exit when there is strong signal of product‑market fit across your target segment.
   - **Launch Stage:** You have a working product with active or paying users.  Focus is on removing technical debt, hardening infrastructure, instituting processes and establishing go‑to‑market channels.  Exit when the growth engine is repeatable and operations are no longer founder‑driven.
   - **Scale Stage:** You are experiencing or planning rapid growth and must handle larger user bases, enterprise requirements, compliance, reliability and defensible moats.  Focus is on systems, automation and competitive barriers.
3. **Determine stage.**  Match your current evidence to the above criteria to classify your stage.  When in doubt, err on the earlier stage to avoid skipping validation steps.
4. **Recommend next skills.**  Based on the identified stage, list relevant Codex skills to use next (e.g. interview script generation for Idea, scope definition for MVP, security review for Launch, and moat narrative for Scale).

## Output

This skill returns:

- Your current **lifecycle stage** (Idea, MVP, Launch or Scale), with justification based on evidence.
- A **summary of gaps** preventing progression to the next stage (e.g. missing validation, lack of retention data, absence of operational processes).
- A **list of recommended Codex skills** tailored to your stage to help you focus on the right actions.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Misinterpreting prototypes as MVPs and thus skipping core validation work.
- Declaring product‑market fit based on vanity metrics such as signups or downloads.
- Failing to reassess the stage as new evidence arrives, leading to scope creep or premature scaling.

## Example prompt

```shell
$codex-startup-lifecycle-mapper
```)
