---
name: publish
description: Publish whatever is in incoming/ to forbesenglish.com — artwork, an HTML lesson, or both. Run from a LOCAL session in this clone.
---

# /publish — from a drop folder to the live site

Innes drops files in `incoming/` and runs this. Nothing else should be
needed. If a step needs a decision from him, ask that one question and stop;
do not open with a round of questions.

**This runs in a local session on Innes's machine** (Claude Code CLI or the
Claude desktop app opened on this clone). A cloud session cannot see
`incoming/` — the folder is gitignored precisely so that raw Midjourney PNGs
never reach git, and a cloud session only sees git.

## 0. Look at what arrived

```
ls incoming/
```

- `*.png / *.jpg` → artwork. Group by Midjourney prompt in the filename.
- `*.html` → a lesson. A `window.*_GAME_DATA` object means an RPG export
  (see `docs/HANDOFF-rpg.md`); otherwise it is a lesson to rebuild as a deck.
- A `.txt` or `.md` note → Innes's instructions for this batch. Read it first.

Work out the lesson name from the note, the HTML, or the filenames. Folder
names are PascalCase (`CarryingTheLoad/`); page names are kebab-case
(`carrying-the-load.html`).

## 1. Artwork — use the existing tool, never hand-roll a crop

```
python3 tools/prep-artwork.py incoming/ --into <Folder> --dry-run
python3 tools/prep-artwork.py incoming/ --into <Folder> --names hero,bg02,bg03,...
```

It resizes to house spec (~300 KB JPEGs), rejects duplicates against the
whole repo and within the batch, and flags anything that is not 16:9. The
`--dry-run` first: Midjourney's four-up variants are near-identical and it
will tell you which to keep.

Pick the hero: landscape, negative space for the logo and title. Library
card: `LibraryCards/<page-name>.jpg` at 1200x512, cut from the hero.

Then the palette, which is derived, never chosen:

```
python3 lesson-template/extract-palette.py <Folder>/hero.jpg [--light]
```

Every row must PASS. Paste the block into the builder.

## 2. The lesson

Builders live in `lesson-template/build/`. Read `lesson-template/HOUSE-STYLE.md`
and the top of `docs/HANDOFF.md` before writing one. Then:

```
python3 lesson-template/build/build_<name>.py
node   lesson-template/check-lesson.js <page-name>.html     # must exit clean
```

Branching lessons also run their own measurements — see
`build_fireshield.py` for `simulate_` and `fit_` tools and why they exist.

## 3. The catalogue row — this is what makes it appear in the library

`tools/seo.py` only writes metadata for lessons that are in the catalogue,
and the library is built from the catalogue, not from the repo. A page that
is merged but has no row is live at its URL and invisible everywhere else.

Insert one row in `public.lessons` (Supabase project `tusioporxpjtegjlqkkb`):

| column       | value                                                    |
|--------------|----------------------------------------------------------|
| `file`       | `<page-name>.html` — unique, exactly the filename        |
| `title`      | the lesson title as it should read on the card           |
| `level`      | `A1` … `C2`                                              |
| `access`     | `pro` (default) or `free`                                |
| `deck`       | `true` for a 16:9 deck                                   |
| `video`      | `false` unless it is                                     |
| `sort_order` | leave NULL unless Innes wants it pinned                  |

Use the Supabase MCP connector if the session has it; otherwise the
dashboard. **Then mirror the row into `tools/lessons.json`** so a cloud
session's fallback cache is not stale — see the `seo.py` warning in
`CLAUDE.md`.

If the lesson REPLACES old pages (a merge, a rebuild under a new name):
delete their rows, or the library shows both.

## 4. SEO — always last, always checked

```
python3 tools/seo.py
git diff --stat library.html llms.txt lesson-meta.json sitemap.xml
```

Read that diff. If any line was REMOVED that you did not intend, the cache
was stale — `git checkout --` the file, fix the cache, run again.

## 5. Old URLs, if any

A page that is replaced gets a redirect in `src/index.js`, not deletion —
students have bookmarks. Drop it from the catalogue (step 3) so it leaves
the library.

## 6. Ship

```
node lesson-template/check-library.js --vs-origin     # must PASS
git add -A
git status --short          # no incoming/, no PNGs, no node_modules
git commit
git push origin main
```

The site follows `origin/main` within a few minutes. Open the live URL and
click through it before saying it is done.

## 7. Clear the drop folder and report

`rm incoming/*` once everything is in git. Then say what shipped, what you
found, and what you changed — including anything in the source lesson that
was wrong and got fixed.

## What NOT to do

- Do not commit `incoming/` or any raw PNG. `.git` is ~700 MB with no LFS
  and never forgets a blob: 15 PNGs cost 73 MB permanently on 2026-09-07.
- Do not hand-pick a colour.
- Do not ship EN-only. English, German and Spanish is the minimum.
- Do not skip step 3. A merged page with no row is not published.
