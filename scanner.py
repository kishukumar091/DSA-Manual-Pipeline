"""
scanner.py — Scans a screenshots folder and maps problem numbers → image paths.

Supported filename patterns (tried in order):
  1. Pure number         : 1.png  01.png  001.png
  2. Number-prefixed     : 1_two_sum.png  prog_1.png  lc1.png  p1.png
  3. Number-suffixed     : two_sum_1.png  solution1.png
  4. Any embedded number : img_001.png  screenshot_001_ok.png
  
Manual overrides (--map flag) always win and are merged on top.
"""
import os
import re
from pathlib import Path
from typing import Dict, Optional


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp"}

# Ordered list of regex patterns to extract problem number from a filename stem
_PATTERNS = [
    r"^0*(\d+)$",                        # pure number:  "01", "1"
    r"^0*(\d+)[_\-\s]",                  # leading num:  "1_two_sum"
    r"^[a-zA-Z_\-]+0*(\d+)$",           # trailing num: "prog1", "lc_1"
    r"[_\-\s]0*(\d+)[_\-\s]",           # mid num:      "img_001_ok"
    r"0*(\d+)",                           # any digit run (fallback)
]


def _extract_number(stem: str) -> Optional[int]:
    """Try each pattern in order; return first matched number, or None."""
    for pat in _PATTERNS:
        m = re.search(pat, stem, re.IGNORECASE)
        if m:
            return int(m.group(1))
    return None


def scan_folder(folder: str) -> Dict[int, str]:
    """
    Scan *folder* for image files and return {problem_num: abs_image_path}.
    
    If multiple files resolve to the same number, the one with the
    shortest filename wins (usually the cleaner name).
    """
    folder = Path(folder).resolve()
    if not folder.is_dir():
        raise FileNotFoundError(f"Screenshots folder not found: {folder}")

    mapping: Dict[int, str] = {}

    for entry in sorted(folder.iterdir()):
        if entry.suffix.lower() not in IMAGE_EXTS:
            continue
        num = _extract_number(entry.stem)
        if num is None or num < 1 or num > 39:
            print(f"  [scanner] skipped '{entry.name}' (no valid 1-39 number found)")
            continue
        # Keep shortest name when colliding
        if num not in mapping or len(entry.name) < len(Path(mapping[num]).name):
            mapping[num] = str(entry)

    return mapping


def apply_overrides(
    mapping: Dict[int, str],
    overrides: list,          # list of "NUM:PATH" strings from --map flag
    base_folder: str = ".",
) -> Dict[int, str]:
    """
    Merge manual --map overrides into the auto-detected mapping.
    Override format:  "1:image_daac7f.png"  or  "1:/abs/path/img.png"
    """
    base = Path(base_folder).resolve()
    for item in overrides:
        if ":" not in item:
            print(f"  [scanner] bad --map entry (expected NUM:PATH): {item!r}")
            continue
        num_str, path_str = item.split(":", 1)
        try:
            num = int(num_str.strip())
        except ValueError:
            print(f"  [scanner] bad number in --map entry: {item!r}")
            continue
        p = Path(path_str.strip())
        if not p.is_absolute():
            p = base / p
        if not p.exists():
            print(f"  [scanner] image not found for override: {p}")
            continue
        mapping[num] = str(p)
        print(f"  [scanner] override applied: problem {num} → {p.name}")
    return mapping


def report(mapping: Dict[int, str], total: int = 39) -> None:
    """Print a summary table of what was found vs. missing."""
    found = sorted(mapping.keys())
    missing = [i for i in range(1, total + 1) if i not in mapping]
    print(f"\n{'─'*50}")
    print(f"  Images found : {len(found)}/{total}")
    if found:
        print(f"  Problems     : {found}")
    if missing:
        print(f"  Missing      : {missing}")
    print(f"{'─'*50}\n")
