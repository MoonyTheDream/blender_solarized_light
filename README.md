# Solarized Light for Blender

A [Solarized Light](https://ethanschoonover.com/solarized/) theme for Blender 5.0+,
tuned to stay readable while you actually model.

## Design notes

- Every neutral sits on the Solarized base ramp; accents are the canonical
  Solarized hues.
- The UI chrome follows the VSCode Solarized Light feel: pale-gold selection
  highlights and menu hover with dark labels, instead of loud blue.
- Edit mode comes first. Mid-luma Solarized accents go muddy on gray matcap
  surfaces, so the viewport runs brighter: near-black edit cage (base02), gold
  selected geometry, white active element, pale-gold active object outline.
- Mark colors keep their conventions: seams red, sharp edges cyan.

## Install

Grab `Solarized_Light_Theme.zip` from Releases and drag-and-drop it into Blender
(or use Edit -> Preferences -> Get Extensions -> ⌄ -> Install from Disk…), then pick
the theme under Preferences -> Themes.

## Building & tweaking

The theme source lives in [Solarized_Light_Theme/](Solarized_Light_Theme/)
(manifest + theme XML). Package it with:

```sh
zip -r Solarized_Light_Theme.zip Solarized_Light_Theme
```

[solarize.py](solarize.py) is a bulk recolor tool for palette-wide edits: add
`old-hex → new-hex` entries to its `RECOLOR` table (or `wset()` calls for
single widget blocks) and run it to rewrite the theme XML in place. The scheme
constants at the top document every accent the theme is built on.

## Credits & license

Solarized palette by [Ethan Schoonover](https://ethanschoonover.com/solarized/).
Licensed under GPL-3.0-or-later - see [LICENSE](LICENSE).
