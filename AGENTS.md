# AGENTS.md

## Repository purpose

CodexOS Skills is a curated repository of reusable Codex skills for founders, indie hackers, product builders and lean teams building AI-native products.

The repository is not a software application. It is a structured skill library. Most contributions should improve Markdown skill definitions, documentation quality, repository structure, examples and contributor guidance.

## Repository structure

* `.agents/skills/` contains the actual Codex skills.
* Each skill must live in its own folder.
* Each skill folder must contain a `SKILL.md`.
* `templates/SKILL_TEMPLATE.md` is the canonical template for new skills.
* `README.md` explains the repository and public positioning.
* `TUTORIAL.md` explains usage and extension.
* `CONTRIBUTING.md` explains contribution rules.
* `CHANGELOG.md` tracks releases.

## Skill file rules

Every `SKILL.md` must include:

* YAML front matter with `name` and `description`.
* A clear H1 title.
* Purpose.
* When to use.
* Inputs.
* Process.
* Output.
* Quality checklist.
* Failure modes.
* Example prompt.

Keep skills practical, specific and executable by Codex. Avoid vague advice, motivational filler and unsupported claims.

## Writing style

Use clear, direct English.
Prefer concise operational instructions over abstract explanations.
Avoid excessive emojis, hype language or marketing fluff.
Do not include private notes, screenshots references, broken citations or placeholder text.
Do not refer to files, scripts or directories that do not exist.

## Validation checklist

Before committing changes:

1. Search for placeholder text:

   * `yourusername`
   * `Your Name`
   * `TODO`
   * `TBD`
   * `placeholder`
2. Search for broken exported citations:

   * `†`
   * `screenshot`
   * `?`
   * `?`
3. Check Markdown code fences.
4. Check that example prompts match skill names.
5. Check that all referenced paths exist.
6. Run `git diff` and review every changed file.

## Commit style

Use short, clear commit messages:

* `Polish README for public release`
* `Fix skill Markdown examples`
* `Add repository agent instructions`
* `Clean placeholder references`

Do not make unrelated changes in the same commit.
