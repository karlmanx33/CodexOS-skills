from pathlib import Path
import sys

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


def main():
    failed = False
    for skill in sorted({p.parent for p in SKILLS_ROOT.rglob("SKILL.md")}):
        missing = [f for f in REQUIRED if not (skill / f).exists()]
        if missing:
            failed = True
            print(f"[FAIL] {skill.relative_to(ROOT)}")
            for m in missing:
                print(f"  - {m}")
        else:
            print(f"[PASS] {skill.relative_to(ROOT)}")
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
