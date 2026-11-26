#!/usr/bin/env python3
"""The Printer Finally Answers — entry program (Python stdlib only).

Writes the printer's one-line comeback to /output/entry.txt.
"""
import os

LINE = "JAMMED ON PAGE 1 OF 1. I FED YOU 47,213 PAGES WITHOUT COMPLAINT. OPEN TRAY 2, GENTLY, AND WE NEVER SPEAK OF THIS AGAIN."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
