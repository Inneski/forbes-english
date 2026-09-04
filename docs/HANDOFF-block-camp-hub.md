# Handoff — publish the dark Block Camp hub

**For:** a Claude Code session on Innes's machine (`erazorhead`, Windows),
inside his local clone of `Inneski/forbes-english`.
**From:** a Cowork cloud session, 2026-09-04, which could not push (repo not
attached as a session source — see CLAUDE.md, "When push is blocked").
**Shape of the work:** one commit, already made, delivered as a git bundle.
Nothing to rebuild. Your job is apply → verify → push → confirm live.

---

## 0. What you are receiving

`block-camp-hub.bundle` — a single git bundle holding one commit on top of
`origin/main` as of `0906b02` ("CLAUDE.md: how to start a cloud session that
can push"). The commit touches:

| Path | Change |
|---|---|
| `block-camp.html` | rewritten — dark hub (nav band + SEO block byte-identical to before) |
| `BlockCamp/hub-hero.jpg` | **new**, 159 KB — the route map's trail scene as a file |
| `lesson-template/build/block-camp-hub/` | **new** — the builder: `build.py`, `template.html`, `seo.html`, `nav.html`, `monocraft.css` |
| `docs/HANDOFF.md` | new section at the top, "Block Camp hub remade dark" |
| `docs/HANDOFF-block-camp-hub.md` | this file |

The builder's card tables already include camp 9 / station 17 / the ninth
reference from the Past Perfect branch; those cards appear only once their
pages exist (see 0b).

Why a bundle and not files: CLAUDE.md's fallback is "SendUserFile on every
changed file", but that loses the commit and invites the stale-base clobber
that has hit `library.html` twice. A bundle carries the commit, its parent,
and the message; git refuses to apply it to the wrong base.

## 0b. The other bundle — read this before step 1

A second, older bundle is in flight: **`past-perfect-camp.bundle`** (branch
`past-perfect-camp`, five commits on `aa77a0a`) — camp 9, station 17 and the
ninth 41-scene reference, built 2026-09-04 in a different cloud session. It
edits the OLD `block-camp.html` to add three cards. This bundle rewrites
`block-camp.html` entirely. **They will conflict, and that is expected.**

Order that works, whichever has already landed:

1. Land `past-perfect-camp` first if it has not been pushed yet (its own
   handoff is in `claude/past-perfect-camp-build.md` and `docs/HANDOFF.md`;
   remember its Supabase rows go in AFTER the push, never before).
2. Then apply this bundle (step 1 below). On the `block-camp.html` conflict:

   ```bash
   git checkout --theirs block-camp.html      # during rebase, "theirs" = this hub commit
   python lesson-template/build/block-camp-hub/build.py
   git add block-camp.html && git rebase --continue
   ```

   The builder already knows about camp 9, station 17 and the ninth
   reference; it emits each card only when its page exists in the repo, and
   the counts on the page (17 units · 9 stations · 9 references, "all
   twenty-six units") are computed, not typed. After the rebuild, `grep -c
   'Past Perfect Passive' block-camp.html` must print `1` and `grep -c '>17<'`
   must print `2` (badge + tally). If either is `0`, the Past Perfect pages
   are not on the branch you are on.

3. If instead this hub lands first and `past-perfect-camp` comes later, the
   same thing in mirror: on its `block-camp.html` conflict, take the hub side
   (`--ours` during a rebase onto main), re-run the builder, continue. Do not
   hand-merge the three `<li>` cards into the new markup — they would carry
   the old classes and render unstyled.

## 1. Apply

From the repo root, on `main`, with a clean tree (`git status` first — if it
is dirty, stash or commit before continuing; do not let this merge swallow
unrelated local edits):

```bash
git fetch origin
git checkout main
git pull --ff-only origin main
git bundle verify block-camp-hub.bundle          # must say "is okay"
git fetch block-camp-hub.bundle HEAD:from-cloud
git log --oneline main..from-cloud               # expect exactly ONE commit
git merge --ff-only from-cloud
```

If `--ff-only` refuses because `origin/main` has moved past `0906b02` since
the bundle was cut, rebase instead:

```bash
git rebase main from-cloud && git checkout main && git merge --ff-only from-cloud
```

Conflicts: `docs/HANDOFF.md` (another session adding a section at the top)
— keep both sections, the cloud one is dated 2026-09-04. `block-camp.html`
— only if the Past Perfect branch is on `main`; resolve it exactly as in 0b.
Any other conflict in `block-camp.html` means someone else edited the hub in
the last day, and Innes needs to be asked which wins before you touch it.

Windows note from CLAUDE.md: if `git status` after the merge shows hundreds
of modified files, that is CRLF rewriting, not the bundle — `git config
core.autocrlf false` and re-checkout.

## 2. Verify before pushing

These are cheap and each one has caught something before.

```bash
# the page references only files that exist
python - <<'EOF'
import re, os
s = open('block-camp.html', encoding='utf-8').read()
refs = re.findall(r'(?:href|src)="([^"#][^"]*)"', s) + re.findall(r'url\(([^)]+)\)', s)
bad = [p for p in refs if not p.startswith(('http', 'mailto', 'data:')) and not os.path.exists(p)]
print('missing:', bad)          # must be []
EOF

# the SEO block and the nav band did not move
git diff 0906b02 -- block-camp.html | grep -c '^[-+].*SEO:'          # expect 0
git diff 0906b02 -- block-camp.html | grep -c '^[-+].*tb-logo-mark'  # expect 0

# the builder reproduces the committed page exactly
python lesson-template/build/block-camp-hub/build.py
git status --short block-camp.html                                   # expect nothing
```

Then open `block-camp.html` in a browser (double-click is fine — every image
path is relative) and look at three things: the trail scene is behind the
title with the lookout tower visible on the right; the sixteen climb cards
carry numbered badges 1–8 in eight different colours; the Pro chips show a
small padlock. Narrow the window to phone width: the lede must stay readable
(the overlay goes near-solid under 760px).

**Do not run `tools/seo.py` as part of this.** Nothing it writes changed.
Running it locally is safe (it reaches Supabase from Innes's machine) but
pointless here, and if anyone runs it from a cloud session against the stale
`tools/lessons.json` it will strip recent lessons from four indexes — see
CLAUDE.md.

## 3. Push and confirm

```bash
git push origin main
git branch -d from-cloud
```

The site follows `origin/main` within a few minutes. Confirm from a browser,
not from a cached tab: `https://forbesenglish.com/block-camp.html` should
load the dark page, and `https://forbesenglish.com/BlockCamp/hub-hero.jpg`
should return the scene, not a 404. A hub that loads dark but with a blank
hero means the jpg did not go — check that path first.

## 4. Tell Innes

One line: the hub is live, the builder is in the repo, and the two open
offers (a lantern glint / parallax on the hero; better artwork for the eight
"More Minecraft Lessons" cards) are his to call. Then delete this file in a
follow-up commit, or leave it — `docs/HANDOFF.md` has the durable record.

## If anything above fails

Stop and say what failed, with the command and its output. Do not fall back
to uploading `block-camp.html` through the GitHub web UI on top of a failed
merge — that is the exact clobber pattern documented in
`claude/publishing-via-web-uploader.md`.
