"""
config.py — Global design constants for the DSA Manual builder.
"""
from docx.shared import Inches, Pt, RGBColor

# ── Page Layout ────────────────────────────────────────────────────────────────
PAGE_WIDTH  = Inches(8.27)   # A4
PAGE_HEIGHT = Inches(11.69)  # A4
MARGIN      = Inches(1.0)

# ── Fonts ──────────────────────────────────────────────────────────────────────
FONT_BODY   = "Segoe UI"
FONT_CODE   = "Consolas"
FONT_HEAD   = "Segoe UI Semibold"

SIZE_BODY   = Pt(10.5)
SIZE_CODE   = Pt(9.5)
SIZE_H1     = Pt(22)
SIZE_H2     = Pt(14)
SIZE_H3     = Pt(12)
SIZE_CAP    = Pt(8.5)

# ── Colour Palette ─────────────────────────────────────────────────────────────
# Text
COL_TEXT        = RGBColor(0x1F, 0x29, 0x37)   # near-black navy
COL_MUTED       = RGBColor(0x64, 0x74, 0x8B)   # slate-500
# Brand / heading
COL_PRIMARY     = RGBColor(0x0F, 0x17, 0x2A)   # very dark navy
COL_ACCENT      = RGBColor(0x22, 0x8B, 0xE6)   # clear blue
# Code block
COL_CODE_BG     = "1E293B"                      # dark slate (hex, for XML)
COL_CODE_FG     = RGBColor(0xE2, 0xE8, 0xF0)   # slate-200
# Divider / badge
COL_DIV_BG      = "0F172A"                      # midnight
COL_DIV_FG      = RGBColor(0xFF, 0xFF, 0xFF)
# Caption
COL_CAP         = RGBColor(0x94, 0xA3, 0xB8)   # slate-400

# Image max width inside text area (A4 @ 1" margins → 6.27" usable)
IMG_WIDTH = Inches(6.27)

# ── Category → accent colour mapping ──────────────────────────────────────────
# Used to colour-code section heading badges
CATEGORY_COLORS = {
    "Array":        "2563EB",   # blue-600
    "String":       "7C3AED",   # violet-600
    "Linked List":  "059669",   # emerald-600
    "Stack":        "D97706",   # amber-600
    "Tree":         "16A34A",   # green-600
    "Graph":        "DC2626",   # red-600
    "DP":           "9333EA",   # purple-600
    "Greedy":       "0891B2",   # cyan-600
    "Bit":          "C026D3",   # fuchsia-600
    "Other":        "475569",   # slate-600
}
