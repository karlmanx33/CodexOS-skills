# Operational Skill Standard

Every skill under `.agents/skills/<category>/<skill-name>/` must include:

- `SKILL.md` with operational execution instructions.
- `skill.json` manifest.
- `concept/` folder preserving original concept and notes.
- `templates/` with at least `output.md`.
- `scripts/run.py` and `scripts/validate.py`.
- `examples/` with concrete input/output/command examples.
- `tests/test_output_structure.py`.

## Execution baseline

1. Gather required inputs.
2. Inspect relevant repository context.
3. Generate outputs from templates.
4. Validate output sections and placeholder hygiene.
5. Return clear artifacts and decisions.

## Quality rules

- No placeholder content in final outputs.
- Output sections must match the declared contract.
- Concepts remain archived in `concept/original-skill.md`.
