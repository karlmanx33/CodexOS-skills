# Tutorial: Getting started with CodexOS Skills

This tutorial walks you through installing this repository, loading skills into your Codex environment and making the most of the included workflows.
Whether you're sharpening a problem hypothesis, drafting an MVP architecture or designing your GTM strategy, these skills help you move faster with more confidence.

## 1. Installation

1. **Ensure you have Codex access.** You need an OpenAI API key and access to Codex to run these skills.
2. **Clone the repo.**

   ```bash
   git clone https://github.com/karlmanx33/CodexOS-skills.git
   cd CodexOS-skills
   ```

3. **Add to your working directory.** Place the cloned directory somewhere in your Codex working folder so the `.agents/skills/` hierarchy is discoverable, or copy the individual `SKILL.md` files you want into your local Codex skills directory.

## 2. Understanding skill structure

Each skill is defined in a folder under `.agents/skills/<category>/<skill-name>`. The heart of the skill is `SKILL.md`, which includes:

- **Front matter:** name and one-line description used by Codex for discovery.
- **Purpose:** what the skill achieves.
- **When to use:** scenarios where it is appropriate.
- **Inputs:** information you need to provide when invoking the skill.
- **Process:** step-by-step instructions Codex follows.
- **Output:** expected deliverables or artifacts.
- **Quality checklist:** reminders for the author or reviewer.
- **Failure modes:** common pitfalls to avoid.
- **Example prompt:** how to call the skill in a session.

## 3. Running a skill

To run a skill, start a Codex session (via CLI or a client that supports `$` skill syntax) and type the skill name prefixed with a dollar sign:

```shell
$problem-hypothesis-sharpener
```

Codex will read the skill definition, ask for required inputs and execute the process. Outputs may include refined hypotheses, interview scripts, architecture briefs, checklists or other structured artifacts.
Use the results as a starting point for further research, discussion or implementation.

## 4. Best practices

- **Prepare your context.** The more concrete inputs you provide, the better Codex can help. When running `customer-discovery-script-builder`, for example, know your target persona and problem area.
- **Iterate.** Many skills are iterative by design. After you receive an output, refine your inputs and run the skill again.
- **Combine skills.** Often you will chain skills. Start with `problem-hypothesis-sharpener`, then `competitive-landscape-mapper`, followed by `customer-discovery-script-builder`.
- **Update context files.** Skills like `project-context-file-generator` and `codex-session-log-updater` produce files that persist across sessions. Keep them in sync to avoid drift and technical debt.
- **Audit regularly.** Use `technical-debt-audit-runner` and `pre-launch-security-reviewer` to catch issues before they become critical.

## 5. Extending the repository

To create your own skills:

1. Copy `templates/SKILL_TEMPLATE.md` into a new folder under `.agents/skills/<your-category>/<your-skill>`.
2. Fill in the front matter and sections. Be explicit about purpose, inputs and process.
3. Add any supporting templates under `templates/` or `references/` as needed.
4. Manually review the front matter, paths, example prompt, quality checklist and failure modes before publishing.
5. Commit and open a pull request with your new skill.

## 6. Frequently asked questions

### Do I need to install a plugin?

No. Each skill is loaded by Codex when you reference it in a compatible session or copy the relevant `SKILL.md` into your Codex skills directory.

### Can I use these skills with models other than Codex?

These skills are tailored for OpenAI Codex and rely on the `$` invocation mechanism. However, the underlying workflows and templates can inspire custom scripts or prompts for other models.

### Where can I learn more about creating Codex skills?

Start with `templates/SKILL_TEMPLATE.md`, inspect the existing skills under `.agents/skills/`, and adapt the structure to your own workflow.
