# AI‑Native Startup Codex Skills 🚀

[![Star Repo](https://img.shields.io/github/stars/yourusername/ai-native-startup-codex-skills?style=social)](https://github.com/yourusername/ai-native-startup-codex-skills/stargazers) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE) [![Release](https://img.shields.io/badge/release-v0.1.0-blue.svg)](/CHANGELOG.md)

Welcome to **AI‑Native Startup Codex Skills**, a curated collection of reusable Codex skills for founders, indie hackers and lean teams building AI‑native products.  
This project transforms the frameworks from the founders' playbook into concrete, repeatable workflows that guide you from idea validation to MVP architecture, launch readiness, scale systems, GTM and defensible moats.  
Use these skills to systematize your product thinking, automate tedious tasks and let Codex become a reliable co‑founder.

## ✨ Why this repository exists

Building an AI‑native startup isn't about hacking together code as quickly as possible. It's about **validating before you build**【444692062822150†screenshot】, **architecting before you code**, **launching safely** and **scaling deliberately**.  
This repository packages those principles into individual skills. Each skill defines inputs, process, decision rules and expected outputs so Codex can perform like an experienced operator rather than a generic chat agent.

### What you can do with these skills

- **Validate ideas** – pressure‑test your problem hypothesis, map competitors and run customer discovery interviews.
- **Design MVPs** – scope your minimal product, draft architecture briefs and prepare security reviews.
- **Plan launches** – audit technical debt, define production checklists and automate reporting.
- **Scale responsibly** – assess enterprise readiness, codify institutional knowledge and design data moats.
- **Drive growth** – craft GTM strategies, messaging architectures and launch playbooks.

## 🧭 Repository structure

Skills are organised by lifecycle stage. Each skill lives in its own folder under `.agents/skills/<category>/<skill‑name>` and contains a `SKILL.md` file describing how Codex should execute it.

| Stage | Folder | Purpose |
|------|------|-------|
| **Founder OS** | `.agents/skills/founder-os/` | The founder’s operating system: decision logs, bottleneck audits and weekly reviews |
| **Idea Validation** | `.agents/skills/idea-validation/` | Sharpen problem hypotheses, validate solution fit, analyse competitors and run customer interviews |
| **MVP Build** | `.agents/skills/mvp-build/` | Define scope, write architecture briefs, prepare Codex sessions and write feature specs |
| **Launch Systems** | `.agents/skills/launch-systems/` | Ensure launch readiness: production hardening, ops audits and automation blueprints |
| **Scale Systems** | `.agents/skills/scale-systems/` | Prepare for hyper‑growth: enterprise gaps, observability, institutional knowledge and moats |
| **GTM & Growth** | `.agents/skills/gtm-growth/` | Build go‑to‑market strategies, messaging, positioning and sales playbooks |
| **Technical Operations** | `.agents/skills/technical-ops/` | Audit your repo structure, API contracts, tests, refactoring plans and docs |
| **Security & Compliance** | `.agents/skills/security-compliance/` | Review authentication, secrets exposure, data privacy and remediation sequencing |
| **Workflow Automation** | `.agents/skills/workflow-automation/` | Automate CRM updates, reports, ticket routing and documentation sync |
| **Investor Readiness** | `.agents/skills/investor-readiness/` | Craft investor memos, pitch decks, traction narratives and unit economics briefs |

## 🚀 Quick start

Clone the repository and explore the skills:

```bash
git clone https://github.com/yourusername/ai-native-startup-codex-skills.git
cd ai-native-startup-codex-skills
```

Each skill is loaded automatically by Codex when you reference it in a session.  
For example, to sharpen a vague idea into a testable problem hypothesis:

```shell
$problem-hypothesis-sharpener "I want to build an app that helps remote teams bond."
```

Codex will prompt you for additional context, run through the skill’s process and output a refined problem hypothesis, assumption map and validation plan.

## 🛠️ How to use a skill

1. **Identify your need.** Decide whether you’re validating an idea, building an MVP, preparing to launch, scaling, pursuing growth, or raising investment.
2. **Locate the skill.** Navigate to the appropriate stage and folder.
3. **Read the `SKILL.md`.** Understand the purpose, when to use it, required inputs and process.
4. **Invoke in your Codex session.** Use the `$` prefix followed by the skill name (e.g. `$mvp-architecture-brief-generator`).  
   Codex will guide you through the workflow defined in `SKILL.md`.
5. **Iterate.** Review the output, refine your inputs and rerun or adjust as needed.

## 📚 Included skills (v0.1.0)

The first release contains a focused set of twenty skills covering the entire lifecycle. Explore the folders under `.agents/skills/` to see their definitions:

- **Founder OS:** `codex-startup-lifecycle-mapper`, `founder-operating-system-designer`
- **Idea Validation:** `problem-hypothesis-sharpener`, `devils-advocate-idea-reviewer`, `competitive-landscape-mapper`, `customer-discovery-script-builder`, `post-interview-synthesis-generator`, `lightweight-prototype-planner`
- **MVP Build:** `mvp-scope-definer`, `mvp-architecture-brief-generator`, `project-context-file-generator`, `codex-session-planner`, `codex-session-log-updater`, `feature-spec-writer`, `pre-launch-security-reviewer`, `mvp-measurement-framework-builder`, `technical-debt-audit-runner`
- **Launch & Growth:** `product-management-os-builder`, `gtm-strategy-builder`, `domain-moat-narrative-builder`

You can add more skills by following the template in `templates/SKILL_TEMPLATE.md`.  
Run the scripts in `scripts/` to validate metadata and regenerate indexes.

## 🤝 Contributing

Pull requests are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes, write new skills and comply with our quality checklist.  
Before submitting, run `npm run validate:skills` to lint your skill front matter and ensure it passes basic checks.

## 📄 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
