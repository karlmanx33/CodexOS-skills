---
name: post-interview-synthesis-generator
description: Turn raw interview notes into actionable insights, patterns and contradictions.
---

# Post‑Interview Synthesis Generator

## Purpose

Transform raw interview notes into actionable insights.  By identifying patterns, contradictions and surprises, this synthesis helps you evaluate whether your problem and solution hypotheses hold up and where to adjust.  It also surfaces gaps and new questions to explore in subsequent research.

## When to use

Run this skill after each set of interviews (e.g. 3–5 sessions).  It is especially important before making any pivot or committing to an MVP scope.  You can also rerun it as new interviews are added to update your evidence base.

## Inputs

- Interview notes or transcripts

## Process

1. **Aggregate and clean notes.**  Collect all interview notes or transcripts into one document.  Highlight direct quotes related to pain points, existing workarounds, desired outcomes and any emotional signals (frustration, delight, indifference).
2. **Identify themes and outliers.**  Group observations by topic (e.g. time spent, costs, tools, blockers).  Note which responses recur across multiple interviews versus outliers that might signal unique contexts or segments.
3. **Map to hypotheses.**  For each key statement, annotate whether it **confirms**, **contradicts** or **surprises** relative to your problem and solution hypotheses.  Pay close attention to evidence that challenges your assumptions; don’t downplay it.
4. **Ask AI for synthesis.**  Have AI summarise patterns, contradictions and surprising findings across interviews.  Ask for potential explanations for outliers and how they might indicate different segments or job‑to‑be‑done.
5. **Evidence weighting.**  After every five interviews, request a list of all evidence that supports or challenges your hypotheses.  Ask whether positive/negative evidence is skewed by selection bias or sample size, and adjust your weighting accordingly.
6. **Define next actions.**  Based on the synthesis, produce a ranked list of top insights, hypotheses to refine, and specific questions to probe in the next round of research.  Highlight any new segments or pain points discovered.

## Output

This skill returns a **post‑interview synthesis report** containing:

- Key themes and supporting quotes across all interviews.
- A table of evidence confirming, contradicting and surprising relative to your hypotheses.
- Analysis of outliers and potential segment differences.
- A list of top insights, revised hypotheses and next research questions.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Ignoring contradictory evidence because it conflicts with the desired narrative.
- Over‑weighting feedback from early adopters or friendly sources.
- Failing to separate signals from noise when sample sizes are small.
- Delaying synthesis, leading to memory bias or loss of context.

## Example prompt

```shell
$post-interview-synthesis-generator
```)
