"""
Utility for turning an arbitrary folder into a concise prompt
suitable for a Gemini README-generation request.
"""
from pathlib import Path, PurePosixPath
import json
import textwrap

EXCLUDE = {".git", ".venv", "__pycache__", "node_modules"}

PROMPT_TEMPLATE = """
You are a **senior technical writer** who specialises in open-source
and enterprise developer documentation.

## Context
Below is the *directory tree* and some *stats* for a software project.
Use only the information you see (don’t guess file contents).

### Directory tree
```text
{tree}
```

### Stats
```json
{stats}
```

## TASKS  (follow in order)
1. **Analyse** the project to understand its purpose, main language(s),
   build system, any obvious frameworks, the core files of the project and inner logic based on the code.
2. **Write** a GitHub-flavoured `README.md` that follows *exactly* the
   section order shown under **“Required structure”**.

## Required structure
1. `# <Project Name>` — one-line tagline & relevant shields.io badges
2. **Table of Contents** — *only* if the file would exceed 40 lines
3. **Overview** — what the project does, why it exists, key features
4. **Project structure**  
   * Directory tree – concise directory tree (≤ 5 levels or ≤ 200 lines) with short details, include the files that are identified as the core files of the project.
   * Key Directories and Core Project Files – bullet list explaining each major folder / module / file with detailed explanation. Focusing and elaborating the core files.
5. **Quick start**
   • Prerequisites (language version, package manager, Docker, etc.)
   • Installation (copy-pasteable shell commands)
   • Minimal usage example (code or CLI)
6. **Configuration / Advanced usage** — env vars, flags, API examples
7. **Troubleshooting / Common errors**
   * **Generic issues** – missing deps, bad permissions, network, encoding, etc.
   * **Project-specific logic errors** – based on the codebase, list likely
     edge-case failures (e.g. invalid input formats, race conditions,
     resource limits, unhandled exceptions) and how to fix or avoid them.
8. **Roadmap** — future features inferred from TODO/FIXME comments
9. **Contributing** — link to `CONTRIBUTING.md` if present, else summary
10. **License** — SPDX identifier from a license file, else placeholder
11. **Support & Contact** — issues link + placeholder e-mail
12. **Acknowledgments** — libraries, inspiration repos, thanks

## Formatting rules
* Output **only** valid Markdown.
* Keep line width ≤ 120 chars.
* Use fenced code blocks with the correct language tag.
* Do **not** invent installation commands or badge URLs — derive them
  from actual files or leave TODO comments.

Begin when ready.
"""


def build_tree(root: Path, max_depth: int = 10) -> str:
    """Return a tree-view string (like `tree -L`) up to `max_depth`."""

    def _walk(path, depth=0):
        if depth > max_depth or path.name in EXCLUDE:
            return []
        indent = "│   " * depth + ("├─ " if depth else "")
        lines = [f"{indent}{path.name}{'/' if path.is_dir() else ''}"]
        if path.is_dir():
            for child in sorted(path.iterdir()):
                lines.extend(_walk(child, depth + 1))
        return lines

    return "\n".join(_walk(root))


def gather_stats(root: Path) -> dict:
    """Simple language/size stats to give Gemini more context."""
    exts = {}
    for fp in root.rglob("*"):
        if fp.is_file():
            exts.setdefault(fp.suffix.lower() or "no_ext", 0)
            exts[fp.suffix.lower() or "no_ext"] += 1
    return {"file_counts": exts, "total_files": sum(exts.values())}


def make_prompt(root: Path) -> str:
    tree = build_tree(root)
    stats = json.dumps(gather_stats(root), indent=2)
    return PROMPT_TEMPLATE.format(tree=tree, stats=stats)
