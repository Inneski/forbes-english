# Monocraft subsets

`Monocraft-Regular.woff2` and `Monocraft-Bold.woff2` are subsets of Monocraft
v4.0 by Idrees Hassan (https://github.com/IdreesInc/Monocraft), licensed under
the SIL Open Font License 1.1. Each carries Basic Latin, Latin-1, Latin
Extended-A, general punctuation and the HUD glyphs (◆ ◇ ♥ ♡ ✕ ⛶ arrows) — 364
glyphs, about 8 KB per face. Every RPG built by `rpg.py` embeds both as data
URIs, so a deck is self-contained and has no font request.

The full family covers Latin and Cyrillic only: no Arabic, no CJK. A gloss
language outside that falls back to the system monospace, which is why the
RPG standard keeps the menu to what the spec actually ships.

To rebuild the subsets (needs `pip install fonttools brotli`):

    curl -L -o Monocraft.ttc https://github.com/IdreesInc/Monocraft/releases/download/v4.0/Monocraft.ttc
    python3 lesson-template/build/rpg/subset_monocraft.py Monocraft.ttc
