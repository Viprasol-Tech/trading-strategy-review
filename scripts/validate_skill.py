#!/usr/bin/env python3
"""Validate the trading-strategy-review Agent Skill.

Pure standard library. Exit 0 on success, 1 on failure.

Checks:
  1. skill.md exists and opens with a `---` YAML frontmatter block.
  2. The frontmatter contains `name:` and a `description:` of >= 40 characters.
  3. examples/ contains at least one `.md` file.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIN_DESCRIPTION_LEN = 40


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def parse_frontmatter(text: str) -> dict[str, str]:
    """Extract a minimal key: value map from a leading `---` fenced block."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        fail("skill.md does not start with a '---' frontmatter block")

    fields: dict[str, str] = {}
    closed = False
    key = None
    for line in lines[1:]:
        if line.strip() == "---":
            closed = True
            break
        if line.startswith((" ", "\t")):
            # Continuation of a multi-line value (plain, `>` or `|` scalar).
            if key is not None and line.strip():
                fields[key] = f"{fields[key]} {line.strip()}".strip()
        elif ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            fields[key] = "" if re.fullmatch(r"[|>][-+0-9]*", value) else value
    if not closed:
        fail("skill.md frontmatter block is not closed with '---'")
    return fields


def main() -> None:
    skill = ROOT / "skill.md"
    if not skill.is_file():
        fail("skill.md not found at repo root")

    fields = parse_frontmatter(skill.read_text(encoding="utf-8"))

    name = fields.get("name", "")
    if not name:
        fail("frontmatter is missing a non-empty 'name:'")

    description = fields.get("description", "")
    if len(description) < MIN_DESCRIPTION_LEN:
        fail(
            "frontmatter 'description:' must be >= "
            f"{MIN_DESCRIPTION_LEN} chars (got {len(description)})"
        )

    examples_dir = ROOT / "examples"
    if not examples_dir.is_dir():
        fail("examples/ directory not found")
    md_examples = sorted(examples_dir.glob("*.md"))
    if not md_examples:
        fail("examples/ contains no .md files")

    print("OK: skill.md valid")
    print(f"  name        = {name}")
    print(f"  description  = {len(description)} chars")
    print(f"  examples/    = {len(md_examples)} markdown file(s)")
    for ex in md_examples:
        print(f"    - {ex.name}")
    sys.exit(0)


if __name__ == "__main__":
    main()
