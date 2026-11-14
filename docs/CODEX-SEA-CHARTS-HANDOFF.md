# Handoff for ChatGPT / Codex: paint the remaining eleven sea charts

Paste everything under the line into one Codex chat opened on the FORBES
folder. It does all eleven charts without further prompting. The Atlas of
THE is already done and is the model for the rest.

---

You are painting eleven illustrated grammar sea charts for this repo. Work through them one at a time, in the order below, and do not stop to ask between charts.

STYLE REFERENCE (image 1, the same for every chart):
sailing-the-seas-of-grammar/hero.jpg

For each chart, image 2 is its coded draft in docs/sea-charts/. Make two pictures per chart.

PICTURE A, the labelled chart. Repaint image 2 in exactly the style of image 1: an antique hand-painted sea chart on parchment with a thin ruled border, watercolour terrain with fine ink hatching, cliffs along the coasts, forests, hills and lakes, a compass rose, a sailing ship, and small waves on a pale blue sea. Landscape, 3:2, 1536 x 1024.
- Keep the layout of image 2 exactly. Coastlines, islands, sandbanks, dashed currents, flags, compass and ships stay in the same places.
- Every harbour dot stays where it is, as a solid black dot about 11 pixels across, on plain paint with nothing dark touching it. Do not add dots. Do not use white markers.
- The colours in image 2 are a code and must not change. Keep each landmass, each coloured line and each coloured disc in the colour drawn in image 2: the same hue, not a parchment version of it. Where a disc is split into two halves, keep both halves and any orange outline round a half.
- Copy every word in image 2 exactly as spelled and in the same place. Serif capitals for titles, plain lettering for place names, as in image 1. Add no other words. British spelling.

PICTURE B, the clean copy. The same picture as A with every word, letter and number removed: no names, no titles, no captions. Generate it from picture A's own file, by its explicit path, so it is the same painting. Keep every harbour dot, every coloured line and every coloured disc exactly where it is in A. Change nothing else.

BEFORE SAVING EACH CHART, CHECK AND FIX:
1. Every word in A matches the draft, letter for letter. Regenerate if any word is wrong.
2. The number of black harbour dots in A and in B equals the number in the draft.
3. B has no lettering left anywhere.
4. A and B are the same painting: coasts and dots in the same places.
5. For the five colour-coded charts (marked below), each coloured land, line and disc is still the draft's colour.

SAVE AS PNG, 1536 x 1024, named exactly as listed:

Into incoming/sea-charts/next-six/
 1. docs/sea-charts/finished-open-time.png     -> finished-open-time.png, finished-open-time-clean.png        COLOUR-CODED: west shore brown, east shore teal
 2. docs/sea-charts/conditional-quadrants.png  -> conditional-quadrants.png, conditional-quadrants-clean.png  COLOUR-CODED: the split discs under the harbours, and the one above MIXED
 3. docs/sea-charts/harbour-of-scale.png       -> harbour-of-scale.png, harbour-of-scale-clean.png
 4. docs/sea-charts/the-voyage.png             -> the-voyage.png, the-voyage-clean.png
 5. docs/sea-charts/er-more-coasts.png         -> er-more-coasts.png, er-more-coasts-clean.png

Into incoming/sea-charts/last-six/
 6. docs/sea-charts/statia-actia.png           -> statia-actia.png, statia-actia-clean.png                    COLOUR-CODED: west shore blue, east shore pink
 7. docs/sea-charts/make-do.png                -> make-do.png, make-do-clean.png
 8. docs/sea-charts/certainty.png              -> certainty.png, certainty-clean.png
 9. docs/sea-charts/passive-ferry.png          -> passive-ferry.png, passive-ferry-clean.png                  COLOUR-CODED: each dashed ferry lane and the disc at each end of it
10. docs/sea-charts/backshift-current.png      -> backshift-current.png, backshift-current-clean.png          COLOUR-CODED: the disc under each harbour
11. docs/sea-charts/the-bridges.png            -> the-bridges.png, the-bridges-clean.png

Do not edit any other file in the repo, do not commit, and do not touch incoming/sea-charts/next-six/atlas-of-the*.png, which are finished.

WHEN ALL ELEVEN ARE DONE, report one line per chart: the two filenames, the dot count in each, and anything you could not get right after two tries. Say plainly if a chart failed; do not save a picture you know is wrong without saying so.
