#!/usr/bin/env python3
"""Bulk recolor tool for the Solarized Light Blender theme.

Solarized_Light_Theme/Solarized_Light_Theme.xml is the source of truth; this
script applies palette-wide edits to it in place and is a no-op while the tweak
tables below are empty. Two mechanisms:

  RECOLOR  -- old RGB hex -> new RGB hex, swapped on every #RRGGBB / #RRGGBBAA
              token in the file (alpha preserved). Right tool for palette-wide
              changes: swap one entry, hit every editor at once.
  wset()   -- set attribute colors inside a single <wcol_*> widget block, for
              UI chrome where a global swap would hit too broadly.

Run: python3 solarize.py
"""
import re

# --- Solarized palette (Ethan Schoonover) -------------------------------------
BASE03, BASE02, BASE01, BASE00 = "002b36", "073642", "586e75", "657b83"
BASE0, BASE1, BASE2, BASE3     = "839496", "93a1a1", "eee8d5", "fdf6e3"
YELLOW, ORANGE, RED, MAGENTA   = "b58900", "cb4b16", "dc322f", "d33682"
VIOLET, BLUE, CYAN, GREEN      = "6c71c4", "268bd2", "2aa198", "859900"

# --- Scheme constants the theme is built on -----------------------------------
# UI chrome (VSCode-Solarized-Light flavored)
GOLD   = "d9bd6c"  # selection highlights, menu hover, slider/progress fills
SELTXT = BASE03    # label on gold highlights
GLYPH  = BASE01    # neutral arrows / scrollbar grips
# 3D viewport: mid-luma Solarized accents go muddy on gray matcap surfaces,
# so selection colors run at full value there
VPSEL  = "ffc100"  # selected geometry / objects: yellow at full value
VPACT  = "ffffff"  # active mesh element
VPOBJ  = "ffe066"  # active object / pose bone: pale gold (white vanishes on cream)
WIRE   = BASE02    # edit cage + unselected verts

THEME = "Solarized_Light_Theme/Solarized_Light_Theme.xml"

# Bulk swaps: "old rgb": "new rgb" (lowercase, no '#'; alpha is preserved)
RECOLOR = {
}

tok = re.compile(r"#([0-9a-fA-F]{6})([0-9a-fA-F]{2})?")

def recolor(m):
    rgb, alpha = m.group(1).lower(), m.group(2) or ""
    return "#" + RECOLOR.get(rgb, rgb) + alpha

def wset(text, name, **attrs):
    """Set attribute colors within one <name> widget block."""
    def fix(m):
        b = m.group(0)
        for k, v in attrs.items():
            b = re.sub(rf'({k}=")#[0-9a-fA-F]{{6,8}}(")', rf"\g<1>#{v}\g<2>", b, count=1)
        return b
    return re.sub(rf"<{name}>.*?</{name}>", fix, text, flags=re.S)

with open(THEME, encoding="utf-8") as f:
    out = tok.sub(recolor, f.read())

# Targeted widget tweaks go here, e.g.:
#   out = wset(out, "wcol_menu_item", inner=GOLD + "00", text_sel=SELTXT)

with open(THEME, "w", encoding="utf-8") as f:
    f.write(out)
print("done")
