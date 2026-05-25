import argparse
from pathlib import Path
import sys

REQUIRED = ["## Objective", "## Inputs summary", "## Analysis", "## Proposed output", "## Risks", "## Next actions"]
BANNED = ["TODO", "TBD", "lorem", "placeholder"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()

    text = Path(args.file).read_text(encoding="utf-8", errors="ignore")

    missing = [h for h in REQUIRED if h not in text]
    banned = [b for b in BANNED if b.lower() in text.lower()]

    if missing or banned:
        if missing:
            print("Missing sections:", ", ".join(missing))
        if banned:
            print("Banned placeholders found:", ", ".join(banned))
        sys.exit(1)

    print("PASS")

if __name__ == "__main__":
    main()
