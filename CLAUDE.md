# Working on this repo

This is forbesenglish.com — an ESL lesson site. Read this file before doing
anything. It exists because sessions cannot talk to each other, so the repo is
the only shared memory. Anything a future session needs to know belongs here or
in one of the two documents below, not in a chat.

## The default action

**A forbesenglish.com URL means: rebuild that lesson as a 16:9 deck, to house
style. Start immediately.** An attached image is the hero for it. Two or more
images: the landscape one is the cover, the rest become per-slide backgrounds.

This is a standing instruction, not a per-request one. Innes sends a URL and a
picture and expects to get a finished deck back. **Do not open with a round of
questions about audience, level, tone, length or scope** — the audience is his
students, the level is on the lesson, the tone and length are defined in the
house style, and the scope is "the whole lesson, brought up to standard."

**A standalone RPG export (one HTML file, pictures inlined, a
`window.*_GAME_DATA` object) means: rebuild it as a Block Camp RPG.** The
standard — glowing object on every picture, text that pops out of it,
Monocraft, big type, hub card, library entry — and the pipeline are in
`lesson-template/build/rpg/README.md`; the step-by-step walk-through for a
fresh session is `docs/HANDOFF-rpg.md`; the brief Innes gives ChatGPT to
produce the export in the first place is `docs/CHATGPT-RPG-BRIEF.md`. Same
rule: start immediately.

Read the lesson, audit it, build it, check it, ship it, then report what you
found and what you changed. `lesson-template/HOUSE-STYLE.md` §14 lists the four
situations that genuinely warrant a question. Everything else: apply the
standard and say what you did.

## Handing a file to a cloud session

A cloud session cannot see Innes's Downloads folder, and the Google Drive
connector cannot move a file of any real size (a 7.5 MB RPG export killed
the connection three times on 2026-09-05; drive.google.com itself is blocked
by the sandbox proxy). Two routes work, and nothing else does:

- **Attach the file to the chat message** — drag it into the message box.
  This is how the 4 MB Oz export arrived, and it is the fastest.
- **Upload it to the repository** on GitHub ("Add files via upload", as with
  `61a32b2`) and say which file. Anything in the repo a session can fetch.

A forbesenglish.com URL works because the site is public. A link to a file
on Innes's machine never will.

## Read these two, in this order

1. **`lesson-template/HOUSE-STYLE.md`** — binding. The six rules, the palette
   method, the slide budget, the activation stage, translation, QA.
2. **`docs/HANDOFF.md`** — the live queue, per-lesson audits, and the recurring
   defect pattern to check for in anything not yet rebuilt.

## The pipeline

```bash
python3 lesson-template/extract-palette.py <hero.jpg> [--light]   # every row must PASS
python3 lesson-template/build/build_<name>.py                     # builders live here
node   lesson-template/check-lesson.js <lesson>.html               # must exit clean
python3 tools/seo.py                                              # ALWAYS last
```

**On Windows there is no `python3`.** Use `py` (the launcher) or `python`, or
add an alias — every command in this file and in the docs is written `python3`
because the builders were authored on Linux. `node` is the same on both.

**`tools/seo.py` runs after every build, without exception.** It writes the
title, description, canonical, Open Graph and JSON-LD into each page, plus
`sitemap.xml`, `robots.txt` and `lesson-meta.json` — the last of which the
Worker reads to build a real gate page per Pro lesson. A builder re-run
overwrites the generated HTML and takes the SEO block with it, so a deck
shipped without this step goes out with no metadata at all. It is idempotent;
run it twice if you are unsure. `--check` reports without writing.

**In a cloud session, `seo.py` cannot reach Supabase and falls back to
`tools/lessons.json`. Anything added since that cache was written is
DELETED from `library.html`, `llms.txt`, `lesson-meta.json` and the
sitemap — silently, and the run still reports success.** It happened on
2026-09-02: a `seo.py` run after pulling Innes's newly pushed
`long-way-home-rpg` stripped the lesson out of all four indexes. The
failure looks exactly like a normal run; the only sign is the diff.

So in a cloud session: run it, then **read `git diff` on those four files
before committing**, and `git checkout --` any line it removed. The line it
prints, `! supabase unreachable … using tools/lessons.json`, is the warning
that this can happen.

Every deck is **generated**. Edit the builder in `lesson-template/build/` and
re-run it; hand-editing the generated HTML works once and is then overwritten.
`deck.py` and `chrome_i18n.py` are shared — use them, don't rewrite them.

Palettes are derived mechanically from the hero. Never hand-pick a colour.

Slide-count chips take their number from `check-lesson.js`'s header line —
counting `<section class="slide` in the source returns N+1.

## Publishing

**Try `git push` first.** Whether it works depends on where you are running,
so find out rather than assuming:

- **Claude Code on Innes's machine** — push works. It uses his own git
  credentials with no proxy in between. Commit and push; ignore the whole
  uploader section below.
- **A cloud Cowork session** — push works **only if this repository was added
  as a source when the task was created**. The sandbox has no GitHub
  credential of its own; the egress proxy injects one per request, and it
  only does so for repositories in the session's source list. A session
  started without the repo can still *clone* (the repo is public) but every
  push fails with a proxy 403, *"Inneski/forbes-english is not in this
  session's authorized repository set … add the repository to the session's
  sources."* That list is fixed at startup and cannot be changed from inside
  the session — not by a token, not by a remote URL, not by retrying.

  **Innes: when starting a cloud task that will touch this repo, add
  `Inneski/forbes-english` as a GitHub source on the new-task screen before
  sending the first message.** The Claude GitHub app
  (github.com/apps/claude) must have access to the repository for it to be
  offered. If a session started without it, the fastest recovery is to ask
  for a `git bundle` of the commits (one file, applied locally with
  `git fetch <bundle> HEAD:from-cloud && git merge from-cloud && git push`)
  rather than a file-by-file upload.

If you are pushing directly, note that everything downstream is unchanged: the
live site still follows `origin/main`, `tools/seo.py` still runs last, and
`check-library.js --vs-origin` is still worth running before you touch
`library.html` — a stale in-memory copy can drop entries whatever the transport.

### When push is blocked

- **If you have Chrome tools**, use GitHub's web uploader: `/upload/main` for
  root files, `/upload/main/<folder>` for a new directory — one directory per
  commit. Then verify byte-for-byte: `git fetch origin`, compare
  `git hash-object <file>` against `git rev-parse origin/main:<file>`, and only
  then `git reset --hard origin/main`.
- **If you do not**, commit locally and then call **`SendUserFile` on every
  changed file**. That is your sandbox's only exit. Work committed to a local
  branch that is never pushed is lost when the container is reclaimed — this
  has already happened once, to a finished 36-slide rebuild of
  `forbes-nature-agency-part1`.

Do not leave work sitting on an unpushed branch while waiting for a reply.
Deliver the files first, ask afterwards.

The live site follows `origin/main` within a few minutes.

### Driving the web uploader: commits fail silently

`file_upload` accepts container paths directly — anything under
`/mnt/user-data/outputs/` works, so there is no need to route files through the
desktop bridge or a connected folder.

**Keep image batches to five files.** On 2026-08-23 a 21-file, 2.2 MB batch
and then a 10-file, 1.1 MB batch both wedged the tab: `file_upload` timed out
after 45s waiting for document_idle, and every subsequent screenshot failed
with "script injection timed out" until the tab was closed and recreated. Five
files at roughly 500 KB went through every time, eight batches in a row. The
form accumulates across calls, so batching costs nothing — it is still one
commit at the end.

The trap is the commit form. **Clicking the summary field or the Commit
button by element `ref` does nothing, reports success, and leaves the form
untouched.** Three of the six commits in the Carrying the Load upload were lost
this way; the tool output read `Clicked on element ref_148` every time. The
first click after a `file_upload` is also swallowed, so focus stays on
"choose your files" and the typed summary goes nowhere.

What works: click by **coordinate**, and make that click its own tool call
rather than the first item of a batch. Then screenshot and confirm the text is
actually in the field before clicking Commit. The layout shifts by ~17px once
the "ProTip" line appears, so re-read the button position from that screenshot.

Because the failure is silent, **the byte-for-byte check is what tells you
whether you committed at all** — not just whether the bytes are right. Run it
over the full changed-file list, not a sample:

```bash
for f in $(git diff --name-only main <branch>); do
  [ "$(git hash-object "$f")" = "$(git rev-parse "origin/main:$f" 2>/dev/null)" ] \
    && echo "OK   $f" || echo "FAIL $f"
done
```

### Before uploading `library.html`, always run

```bash
node lesson-template/check-library.js --vs-origin     # must PASS
```

**Verifying after the upload is not enough.** A byte-for-byte match against
`origin/main` only proves your bytes landed — which is exactly what a clobber
looks like too. The uploader replaces the file wholesale, so any entry added to
`LESSON_IMAGES` since you last read the file is deleted by your upload, and
nothing errors.

This has now happened twice to the same entry. The second time, `f6be885`
dropped the Stranger Things deck's thumbnail; its parent *did* contain the
commit that added it, so this was not a stale base — it was an in-memory copy
of `library.html` read before that commit and uploaded whole afterwards.
`git fetch` does not help. **Re-read the file from `origin/main` and re-apply
your change to it immediately before uploading.**

The failure is invisible from the front. The lesson keeps working: its row,
its page and its download are all fine. But `comingSoon()` is
`!LESSON_IMAGES[l.file]`, so losing the line turns the card into a disabled
"Coming soon" div and sorts it behind every other lesson. It reports as
"I can't see it", not as an error.

## Standing constraints

- **Every deck ships Spanish and German as a minimum.** Innes said so on
  2026-09-04, after three decks went out EN+DE. `assemble()` still defaults to
  `('en', 'de')`, so pass `langs=('en', 'de', 'es')` explicitly — and write the
  teach cards in the six-item form so the rule text travels with its heading.
- **Learner-facing text must never mention a previous version of the lesson.**
  No "the old version marked this wrong" on a slide. That belongs in the
  builder docstring and the commit message.
- Hamster keeps his name. Do not rename Clarkson, Hammond or May in the
  published Stranger Gears build, and the Stranger Gears front-page image is
  not up for discussion.
- Never hardcode `rgba(0,0,0,…)` or `rgba(255,255,255,…)` in a lesson — use the
  theme primitives in the template.

## Things that have bitten us

- **A grid item wider than its track is aligned to start, not overflowed both
  sides.** This put every deck's stage off the right edge below 1280px — a
  black page on every phone. The stage is now pinned top-left and centred in
  `fitStage()`. Do not reintroduce `place-items: center` on `.stage-wrap`.
- **`--bins-h`-style layout constants belong in one custom property.** The same
  bug class appeared twice: a media query moved one hardcoded `200px` and left
  three others behind.
- A defect class needs a **measurement**, not just a fix. Both the SORT gate and
  the I18N generalisation were verified failing against deliberately broken
  copies before being trusted.

## Before you finish

Update `docs/HANDOFF.md` if you changed the queue, learned something a future
session needs, or found a defect you did not fix. That file is the handover.

## Working from Windows

Innes's machine is Windows (`erazorhead`, win32 x64). Two things bite a repo
that was authored entirely on Linux:

- **`python3` does not exist.** Use `py` or `python`. See the pipeline note.
- **Line endings.** This repo is LF throughout. Clone with
  `git config --global core.autocrlf false` set, or git rewrites every file to
  CRLF on checkout and the first commit shows all 244 pages as modified. If a
  diff ever comes back absurdly large with no visible content change, this is
  why — check `git diff --stat` before believing it.
