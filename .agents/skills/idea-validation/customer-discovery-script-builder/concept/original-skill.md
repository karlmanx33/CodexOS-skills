---
name: customer-discovery-script-builder
description: Generate a neutral, non‑leading interview script for customer discovery.
---

# Customer Discovery Script Builder

## Purpose

Create a robust customer discovery interview guide that uncovers genuine behaviour, pain points and context without leading or biasing respondents.  Good scripts focus on how people currently solve the problem rather than hypothetical future behaviour, enabling you to validate your hypothesis objectively.

## When to use

Use this skill **before each round** of customer discovery interviews.  Update the script as your hypothesis evolves, and tailor question sets for different personas or segments.  It is also useful when training other team members on how to conduct interviews.

## Inputs

- Target persona description
- Problem hypothesis
- Interview goals

## Process

1. **Clarify goals and persona.**  Define what you want to learn from the interview (behaviour patterns, pain severity, alternatives, decision criteria) and profile the target participant (job title, seniority, company size, industry).  Ensure the persona aligns with your hypothesis.
2. **Draft open‑ended questions.**  Start with broad context questions (e.g. “Walk me through how you currently do X”), then probe into frequency, severity, time spent, costs and emotional impact.  Avoid asking about hypothetical future behaviour (“Would you use…”); focus on what they actually do today.
3. **Avoid bias and leading language.**  Review each question to remove loaded terms or suggestions.  Replace phrases like “Wouldn’t it be easier if…” with neutral alternatives (“How do you feel about…”).  Use AI to audit the script and flag leading, vague or socially desirable questions.
4. **Design follow‑up probes.**  For each core question, prepare clarifying probes to dig deeper: “Why?,” “How often?,” “What tools do you use?,” “What happens if you don’t do this?”  These prompts help interviewers uncover root causes without improvising.
5. **Sequence logically.**  Group questions into opening (rapport building and role context), core (problem exploration and workaround) and closing (summary and referrals) sections.  Ensure the flow encourages storytelling and gradually narrows to the specific problem area.
6. **Customise for personas.**  Create alternate question sets or variations for different user segments (e.g. executives vs. individual contributors) while preserving the core structure.

## Output

This skill returns a **structured interview guide** that includes:

- A summary of research goals and target persona.
- Opening questions to establish rapport and understand the participant’s role.
- Core questions exploring current processes, pain points, frequency, severity and workarounds.
- Follow‑up probes for deeper insight.
- Closing questions to wrap up, solicit referrals and invite further contact.

## Quality checklist

- [ ] Purpose is clear and specific
- [ ] Inputs are identified and complete
- [ ] Steps are actionable and unambiguous
- [ ] Expected output is well defined
- [ ] Failure modes are considered

## Failure modes

- Mixing exploratory and pitch‑selling questions in the same interview, which biases responses.
- Asking hypothetical questions about future adoption instead of probing current behaviour.
- Using jargon or leading language that confuses or pushes participants toward a predetermined answer.
- Failing to tailor the script to the persona, resulting in irrelevant or shallow answers.

## Example prompt

```shell
$customer-discovery-script-builder
```



