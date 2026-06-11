"""
main.py — CLI entry point for the DSA Manual automation pipeline.

Usage examples
──────────────
# Auto-scan a folder (filenames like 1.png, 01.png, lc1.png …)
  python main.py --screenshots C:/screenshots --output DSA_Manual.docx

# Add manual overrides for opaque filenames (e.g. image_daac7f.png = prog 20)
  python main.py --screenshots C:/screenshots --map 20:image_daac7f.png --output DSA_Manual.docx

# Generate only specific programs (comma-separated)
  python main.py --screenshots C:/screenshots --problems 1,2,3,20 --output DSA_Manual.docx

# Generate the document with NO screenshots (code-only mode)
  python main.py --output DSA_Manual.docx
"""
import argparse
import os
import sys

# Force UTF-8 output on Windows (avoids cp1252 UnicodeEncodeError)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Allow running from any directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scanner import scan_folder, apply_overrides, report
from builder import build_document


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="dsa_pipeline",
        description="DSA Manual Automation Pipeline — generates a styled A4 .docx",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    p.add_argument(
        "--screenshots", "-s",
        metavar="FOLDER",
        default=None,
        help="Path to the folder containing your LeetCode/submission screenshots.",
    )
    p.add_argument(
        "--map", "-m",
        metavar="NUM:PATH",
        nargs="+",
        default=[],
        help=(
            "Manual override(s) for opaque filenames. "
            "Format: NUM:FILENAME  e.g.  --map 20:image_daac7f.png"
        ),
    )
    p.add_argument(
        "--problems", "-p",
        metavar="1,2,3",
        default=None,
        help="Comma-separated list of program numbers to include. Default: all 39.",
    )
    p.add_argument(
        "--output", "-o",
        metavar="FILE",
        default="DSA_39_Programs.docx",
        help="Output .docx filename (default: DSA_39_Programs.docx).",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    print("\n" + "=" * 50)
    print("  DSA Manual Pipeline")
    print("=" * 50)

    # ── Build image map ──────────────────────────────────────────────────────
    image_map: dict = {}

    if args.screenshots:
        print(f"\n[1/3] Scanning screenshots folder: {args.screenshots}")
        try:
            image_map = scan_folder(args.screenshots)
        except FileNotFoundError as e:
            print(f"  ERROR: {e}")
            sys.exit(1)
    else:
        print("\n[1/3] No --screenshots folder provided — code-only mode.")

    # Apply manual overrides
    if args.map:
        print(f"\n[1b]  Applying {len(args.map)} manual override(s)…")
        base = args.screenshots or os.getcwd()
        image_map = apply_overrides(image_map, args.map, base_folder=base)

    report(image_map)

    # ── Parse problem filter ─────────────────────────────────────────────────
    problem_numbers = None
    if args.problems:
        try:
            problem_numbers = [int(x.strip()) for x in args.problems.split(",")]
            print(f"[2/3] Filtering to programs: {problem_numbers}")
        except ValueError:
            print("  ERROR: --problems must be comma-separated integers, e.g. 1,2,3")
            sys.exit(1)
    else:
        print("[2/3] Including all 39 programs.")

    # ── Build document ───────────────────────────────────────────────────────
    print(f"\n[3/3] Building document → {args.output} …")
    build_document(
        image_map=image_map,
        output_path=args.output,
        problem_numbers=problem_numbers,
    )

    print("\n" + "=" * 50)
    print("  Done!  Open your .docx file to review.")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
