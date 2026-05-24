# Contributing to AI‑Native Startup Codex Skills

We welcome contributions of all kinds—new skills, bug fixes, documentation improvements and feedback. This guide explains our process so you can get started quickly.

## 📦 Project structure

Skills live under the `.agents/skills/` directory, grouped by stage. Each skill is a folder containing a `SKILL.md` file and optional subfolders (`templates/`, `references/`, `scripts/`). See existing skills for examples.

Auxiliary files live in:

- `templates/` – reusable Markdown templates (e.g. `SKILL_TEMPLATE.md`)
- `docs/` – guides and process explanations
- `scripts/` – helper scripts for validation and index generation
- `examples/` – illustrative projects using these skills

## 🚀 How to add a new skill

1. **Create a folder.** Inside `.agents/skills/<stage>/<skill-name>/` where `<stage>` matches one of the lifecycle categories.
2. **Copy the template.** Start from `templates/SKILL_TEMPLATE.md` and save it as `SKILL.md`.
3. **Fill in the details.** Give your skill a clear name and description. Be explicit about purpose, when to use it, required inputs, process and output. Include a quality checklist and failure modes.
4. **Add supporting templates.** If your skill generates documents (e.g. architecture briefs or scripts), put templates into a `templates/` subfolder within the skill.
5. **Lint your skill.** Run `npm run validate:skills` (or the equivalent script) to ensure the front matter is present and valid.
6. **Open a pull request.** Target the `main` branch. Briefly describe your skill and link any relevant issues or discussions.

## 🧪 Running tests

If you add validation scripts or tests, document how to run them in the PR description. For now, our repository relies on simple linters.

## 💬 Code of conduct

Be kind, constructive and respectful. We operate under the [Contributor Covenant](https://www.contributor-covenant.org/version/2/1/code_of_conduct/) and expect all contributors to adhere to it.

## 🔐 License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for making AI‑Native startup building more accessible!