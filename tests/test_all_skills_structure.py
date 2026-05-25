from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"
REQUIRED = [
    "SKILL.md",
    "skill.json",
    "concept/CONCEPT.md",
    "concept/original-skill.md",
    "templates/output.md",
    "scripts/run.py",
    "scripts/validate.py",
    "examples/input-example.md",
    "examples/output-example.md",
    "tests/test_output_structure.py",
]


def test_all_skills_structure():
    skill_dirs = sorted({p.parent for p in SKILLS_ROOT.rglob("SKILL.md")})
    assert skill_dirs, "No skills found"
    for skill in skill_dirs:
        missing = [f for f in REQUIRED if not (skill / f).exists()]
        assert not missing, f"{skill}: missing {missing}"
