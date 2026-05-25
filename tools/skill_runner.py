import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"


def find_skill_dir(name: str):
    for p in SKILLS_ROOT.rglob("skill.json"):
        if p.parent.name == name:
            return p.parent
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_name")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    skill_dir = find_skill_dir(args.skill_name)
    if not skill_dir:
        print(f"Skill not found: {args.skill_name}")
        sys.exit(1)

    subprocess.run([sys.executable, str(skill_dir / "scripts" / "run.py"), "--input", args.input], check=True)

if __name__ == "__main__":
    main()
