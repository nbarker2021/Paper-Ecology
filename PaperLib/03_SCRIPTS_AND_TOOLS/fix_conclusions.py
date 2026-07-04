#!/usr/bin/env python3
"""Fix the conclusion sentence in generated skeletons."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from generate_papers_09_32 import PAPERS, OUT


for p in PAPERS:
    path = OUT / f"{p['slug']}.md"
    text = path.read_text(encoding="utf-8")
    old = f"Paper {p['num']:02d} {p['role_short'].lower()} and preserves"
    new = f"Paper {p['num']:02d} provides the {p['role_short'].lower()} and preserves"
    text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")

print("Fixed conclusions.")
