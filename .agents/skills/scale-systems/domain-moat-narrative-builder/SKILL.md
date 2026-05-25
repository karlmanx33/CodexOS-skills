---
name: domain-moat-narrative-builder
description: Develop a narrative and audit that demonstrates your defensible moat through edge cases, proprietary data and deep workflow integrations.
---

# Domain Moat Narrative Builder

## Purpose

Craft a compelling narrative explaining **why your product will be difficult to replicate**. In the Scale stage, your moat derives from accumulated domain knowledge, proprietary data, unique edge cases and deep integration into customer workflows【112456722640317†L1651-L1663】. This skill helps you identify those sources of defensibility, audit integration depth and design a feedback loop that turns ongoing usage into a self‑reinforcing advantage【112456722640317†L1670-L1683】.

## When to use

Use this skill during the Scale stage or when preparing investor pitches, enterprise sales decks or strategic planning documents. It is also useful after major product milestones when you want to articulate how your advantage has grown and plan how to strengthen it further.

## Inputs

- List of proprietary datasets, edge cases and domain knowledge captured so far
- Summary of user interaction data and behavioural signals collected over time
- Integration audit for top customers: automations built, tools integrated, workflows dependent on your product
- Competitive landscape assessment
- Timeline of data collection and product usage

## Process

1. **Capture and classify edge cases.** Review support tickets, user feedback and test failures to compile unique or rare scenarios your product has encountered. For each, document the context, resolution and how it informed product improvements. Add these scenarios to your automated test suite—each new test becomes a “map” of your moat and makes it harder for competitors to replicate【112456722640317†L1648-L1653】.
2. **Audit behavioural data and design feedback loops.** Summarise the behavioural signals collected from users (e.g. which outputs they accept or reject, how often they engage with key features, patterns of usage over time). Ask AI to identify the highest‑signal patterns and propose feedback loops that turn ongoing usage into systematic model and product improvements【112456722640317†L1651-L1678】. Note how this data is time‑locked and context‑specific, making it difficult for copycats to obtain【112456722640317†L1661-L1663】.
3. **Map integration depth and workflow lock‑in.** For your top customers or segments, conduct an integration audit: document the automations they have built, the external tools and data sources connected, the team workflows that depend on your product and your estimate of their switching cost. Ask AI to identify patterns: which types of integrations or workflows create the deepest lock‑in and where you can go deeper【112456722640317†L1686-L1728】. Plan new integrations (APIs, webhooks, SDKs) that would deepen lock‑in for customers currently at the surface【112456722640317†L1698-L1719】.
4. **Synthesize the moat narrative.** Draft a one‑page narrative explaining:
   - **Data flywheel:** how user interactions generate data, how that data improves the product and why the resulting behavioural fingerprint is impossible to replicate quickly【112456722640317†L1651-L1683】.
   - **Edge case library:** how your growing library of edge cases and tests protects against competitors who lack this knowledge【112456722640317†L1648-L1653】.
   - **Workflow lock‑in:** how deep integrations embed your product in customer operations, increasing switching costs and making you a critical part of their stack【112456722640317†L1686-L1729】.
   - **Comparison to competitors:** why a well‑funded competitor starting today couldn't recreate these assets in under two years【112456722640317†L1680-L1683】.
5. **Recommend next steps.** Based on the audit, list concrete actions to strengthen your moat: capturing additional edge cases, deepening integrations in high‑value workflows, expanding your analytics and feedback loops, and communicating the moat narrative internally and externally.

## Output

This skill produces a **moat narrative package** consisting of:

- A catalogue of domain‑specific edge cases and their corresponding test suite entries
- A behavioural data analysis with high‑signal patterns and recommended feedback loops
- An integration audit summarising workflow depth, automations and switching costs per customer or segment
- A one‑page narrative describing the data flywheel, edge case library and workflow lock‑in with comparisons to competitors
- A set of recommended actions to further strengthen the moat

## Quality checklist

- [ ] Purpose emphasises defensibility through data and integration
- [ ] Inputs include datasets, behavioural signals, integration audits and competitive context
- [ ] Steps cover edge case capture, data analysis, integration mapping, narrative synthesis and next actions
- [ ] Output includes both narrative and analytical artefacts
- [ ] Failure modes consider common misunderstandings about moats

## Failure modes

- Focusing solely on features without capturing and utilising user data, resulting in a shallow moat.
- Neglecting to collect and integrate edge cases into the product and test suite, leaving gaps competitors can exploit.
- Overstating defensibility without evidence, leading to skepticism from investors or customers.
- Ignoring workflow integration depth and assuming that data alone will create lock‑in.
- Failing to update the moat narrative and audit as the product and user base evolve, resulting in outdated claims.

## Example prompt

```shell
$domain-moat-narrative-builder
```



