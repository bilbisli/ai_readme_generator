#!/usr/bin/env python
"""
CLI: python generate_readme.py /path/to/project [--model gemini-2.5-pro]
Generates README.md inside the target project using Google Gemini via
the *google-generativeai* SDK (pip install google-generativeai).
"""
from __future__ import annotations
import argparse, os, sys
from pathlib import Path

from dotenv import load_dotenv
from tqdm import tqdm
import google.generativeai as genai

from project_scanner import make_prompt

DEFAULT_MODEL = "gemini-2.5-flash"   # change freely on CLI

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create README.md for an existing project via Gemini."
    )
    parser.add_argument("project_dir", type=Path, help="Directory to scan")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Gemini model name")
    args = parser.parse_args()

    root: Path = args.project_dir.expanduser().resolve()
    if not root.is_dir():
        sys.exit(f"Error: {root} is not a directory")

    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        sys.exit("Error: Set GEMINI_API_KEY env variable (see .env.example)")

    # ----------  google-generativeai setup  ----------
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(args.model)
    # -------------------------------------------------

    prompt = make_prompt(root)

    print("⏳ Sending prompt to Gemini…")
    stream = model.generate_content(prompt, stream=True)

    readme_path = root / "README.md"
    readme_lines: list[str] = []

    for chunk in tqdm(stream, unit="chunk"):
        # Each chunk is a `parts` list; join their text
        readme_lines.append("".join(p.text for p in chunk.parts))

    readme_path.write_text("".join(readme_lines).lstrip(), encoding="utf-8")
    try:
        shown = readme_path.relative_to(Path.cwd())
    except ValueError:
        shown = readme_path  # absolute path if it's outside CWD
    print(f"✅ README generated at {shown}")


if __name__ == "__main__":
    main()
