---
name: product-management-os-builder
description: Design a lightweight, automated product management operating system with cadences, spec templates, bug triage rules and metrics briefs.
---

# Product Management OS Builder

## Purpose

Design a **lightweight product management operating system (OS)** that runs your product cycle without constant founder intervention. By defining cadences, templates, triage rules and automated reporting up front, you build repeatable processes that keep engineering, product and customer feedback in sync as you scale【112456722640317†L1294-L1321】.

## When to use

Develop this OS during the Launch stage or whenever your team begins to feel the pain of ad‑hoc product management. Use it as soon as growth demands structured processes and long before you hire a dedicated product manager. Revisit the OS regularly to refine cadences and metrics as the company scales.

## Inputs

- Team composition and roles (e.g. product owner, engineers, designers, AI agents)
- Current development cadence (weekly, bi‑weekly, monthly)
- Existing tools and processes (issue tracker, docs, analytics)
- Core product metrics to monitor (activation, retention, conversion, NPS)

## Process

1. **Map responsibilities and cadence.** Determine sprint length (e.g. two weeks) and schedule key ceremonies: backlog grooming, sprint planning, daily stand‑ups, demos and retrospectives. Assign clear owners (human or AI) for each ceremony, ensuring someone is accountable for preparing agendas, facilitating discussion and capturing actions.
2. **Define a minimum spec template.** Create a template that every feature or change request must satisfy before coding begins. Include: problem statement and user story, acceptance criteria, assumptions and dependencies, success metrics and instrumentation requirements, and links to the relevant hypotheses or measurement framework【112456722640317†L1294-L1321】. Store this template in your repository and require it as a pre‑condition for AI coding sessions.
3. **Create a bug triage decision tree.** Design a process for classifying incoming issues (e.g. P0‑critical, P1‑major, P2‑minor, enhancement). For each category, define reproduction guidelines, assignment rules and resolution timelines. Specify when a bug triggers an immediate hotfix versus scheduling into the backlog. Document the decision tree so that AI agents can route issues automatically.
4. **Design a weekly metrics brief.** Decide which metrics your team needs to review regularly (activation, retention, conversion, revenue, churn, support volume). Identify data sources (analytics platform, database queries, ticketing system) and define how metrics will be aggregated into a concise report. Ask AI to assemble the brief by pulling data, highlighting anomalies, summarising trends and suggesting actions. Schedule distribution to all stakeholders on a fixed cadence.
5. **Plan backlog and roadmap reviews.** Establish a regular cadence (e.g. each sprint for backlog grooming, monthly or quarterly for roadmap review) to re‑prioritise work based on user feedback, metrics and strategic objectives. Define criteria for adding, removing or reordering items, and ensure decisions are captured in your decision log and context files.
6. **Automate operational elements.** Use AI or workflow tools to schedule sprint ceremonies (e.g. sending calendar invites), route bug reports to the appropriate owner based on the decision tree, compile weekly metrics from connected data sources, and maintain the feedback loop that keeps user signals flowing into product decisions【112456722640317†L1294-L1321】. Integrate with your project management and communication tools to minimise manual effort.
7. **Document and iterate.** Consolidate all processes, templates, decision trees and cadences into a **Product Management OS document**. Include instructions on how to update the OS as the team grows, and cross‑link to `PROJECT_CONTEXT.md` and `DECISIONS.md` so that the system reflects current architecture and scope. Review the OS quarterly to incorporate learnings and adjust cadences.

## Output

This skill returns a **Product Management OS** package comprising:

- A clearly defined sprint cadence and schedule of ceremonies with roles and owners.
- A minimum spec template for features and bug reports, ready to copy into your repo.
- A bug triage decision tree with categories, triggers and routing rules.
- A weekly metrics brief template outlining metrics, data sources and distribution plan.
- A backlog and roadmap review cadence and criteria.
- Instructions for automating recurring tasks and integrating AI into the workflows.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs cover team, cadence, tools and metrics
- [ ] Steps provide clear actions for defining templates, triage rules, metrics and automation
- [ ] Output specifies documents, templates and automation guidelines
- [ ] Failure modes consider common process pitfalls

## Failure modes

- Over‑engineering the process for a small team, resulting in unnecessary meetings and bureaucracy.
- Neglecting to connect specs and backlog priorities to measurement frameworks, causing misaligned work.
- Failing to update the OS as the product and team evolve, leading to outdated cadences and templates.
- Ignoring automation opportunities, leaving the founder to manually schedule ceremonies and compile reports.

## Example prompt

```shell
$product-management-os-builder
```
`)