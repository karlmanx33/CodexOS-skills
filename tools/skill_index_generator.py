import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / ".agents" / "skills"


def main():
    rows = []
    for m in sorted(SKILLS_ROOT.rglob("skill.json")):
        data = json.loads(m.read_text(encoding="utf-8"))
        rows.append((data.get("category",""), data.get("name",""), data.get("description",""), data.get("type",""), ", ".join(data.get("scripts", {}).keys()), ", ".join(data.get("outputs", []))))

    lines = ["# SKILL_INDEX", "", "| Category | Skill | Description | Type | Scripts | Generated outputs |", "|---|---|---|---|---|---|"]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
    (ROOT / "SKILL_INDEX.md").write_text("\\n".join(lines) + "\\n", encoding="utf-8")

if __name__ == "__main__":
    main()
