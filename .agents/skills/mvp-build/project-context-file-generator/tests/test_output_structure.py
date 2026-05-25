from pathlib import Path

REQUIRED = ["## Objective", "## Inputs summary", "## Analysis", "## Proposed output", "## Risks", "## Next actions"]

def test_output_structure():
    p = Path(__file__).resolve().parents[1] / "examples" / "output-example.md"
    text = p.read_text(encoding="utf-8", errors="ignore")
    for section in REQUIRED:
        assert section in text, f"Missing required section: {section}"
