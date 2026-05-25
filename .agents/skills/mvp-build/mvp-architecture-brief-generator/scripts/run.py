import argparse
    from pathlib import Path

    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", required=True, help="Input markdown or text file")
        args = parser.parse_args()

        here = Path(__file__).resolve().parent.parent
        templates = here / "templates"
        outputs = here / "outputs"
        outputs.mkdir(exist_ok=True)

        input_text = Path(args.input).read_text(encoding="utf-8", errors="ignore")
        base_template = (templates / "output.md").read_text(encoding="utf-8", errors="ignore")

        body = base_template + "

## Source input

" + input_text.strip() + "
"
        out = outputs / (here.name + "-output.md")
        out.write_text(body, encoding="utf-8")
        print(out)

    if __name__ == "__main__":
        main()
