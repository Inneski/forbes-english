#!/usr/bin/env python3
"""ChatGPT's export of the Kraken saga -> one data.json per part, plus plates.

    py lesson-template/build/rpg/kraken-saga/extract-export.py <incoming-dir>

**A fifth kind of export.** rpg/README.md section 2 names three (Oz,
Wonderland, patched-DATA) and docs/HANDOFF-rpg.md section 3 adds "a script
written here first", which is what this is: STORY.md and IMAGES.md were
written in this repo on 2026-09-12 and ChatGPT was asked for the pictures and
the hotspot boxes only. What came back is not one standalone HTML file at all
— it is a saved web page, `kraken.htm` plus a `kraken_files/` folder, with the
game split across `content.js` (a clean `window.KRAKEN` object), `spots.js`
(`window.KRAKEN_SPOTS`, one [cx, cy] per picture) and `game.js`. No pictures:
they load from `assets/` on a login-gated ChatGPT site, and were fetched
separately into `incoming/kraken-plates/`.

That makes it the least work of any export so far — the text is already JSON
and needs no regex archaeology — and it is the reason this extractor is
specific to the saga rather than another `extract_*.py` beside the generic
three.

**Three parts, one page.** Each part is its own playable game: 14 questions,
max 70, pass 60, three chances, four collectibles, its own four endings. The
export reaches them from a chapter picker on its home screen, and Innes chose
that shape over three separate library cards on 2026-09-17 — it is one story,
and a learner who finishes Inverbrae should be offered the Narrows rather than
go hunting the shelf for it.

rpg.py could not do that: it held one `start`, one `max` and one `endings` map
per page. `chapters` in the spec is the change that lets one page carry three
games without merging their scores — see rpg.py. Folding the three into a
single 42-question run was the alternative and is not what the export does;
README.md section 1 is explicit that the export's own rules stay.

`spots.js` gives hotspot centres only, as fractions of the picture. The house
wants [cx, cy, w, h] in percent, so a default box goes on here and the
builder's HOT table overrides it per scene — docs/HANDOFF-rpg.md section 4 is
right that this part needs eyes, every time.
"""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
INCOMING = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, 'incoming')

# **Not a Block Camp RPG.** Innes said so on 2026-09-17, twice and plainly:
# "This isn't block camp", "It's just RPG". So the page sits at the repo root
# beside stranger-gears-rpg.html and forbes-dnd-rpg.html, with its plates in a
# sibling folder the way last-train-home-rpg.html carries its own — not under
# block-camp/, no hub card in block-camp-hub/build.py, no camp colour and no
# Monocraft. rpg/README.md binds "anything under block-camp/" and this is not
# that; the engine is still rpg.py, because the nine-language gloss and the
# --u type scale are exactly the two things this rebuild is for.
SLUG = 'kraken-black-tide-rpg'

# The cover Innes drew on 2026-09-18 carries its own painted title lockup —
# THE KRAKEN over A TALE OF THE DEEP — and he chose the artwork over the
# working title rather than have the cover disagree with every chapter header
# under it. STORY.md keeps "The Black Tide" as the name it was written under;
# everything a learner sees uses this.
TITLE = 'THE KRAKEN: A TALE OF THE DEEP'

# The home plate behind the chapter picker. Not in the export's own image map —
# it is the cover, prepped to plate spec from incoming/.
HOME = '00_home.webp'

# spots.js has no box, only a centre. 12 x 16 percent of a 3:2 plate is about
# the size of the objects IMAGES.md asked for (a bell, a jar, a barrel) and is
# a starting point, not an answer: every one gets looked at.
DEFAULT_BOX = (12.0, 16.0)


def read_js_object(path, var):
    """`window.X = {...};` -> dict. The export writes one statement per file."""
    src = open(path, encoding='utf-8').read()
    m = re.search(r'window\.%s\s*=\s*' % re.escape(var), src)
    if not m:
        raise SystemExit('%s: no `window.%s =` in this file' % (path, var))
    return json.loads(src[m.end():].strip().rstrip(';'))


def main():
    kf = os.path.join(INCOMING, 'kraken_files')
    content = read_js_object(os.path.join(kf, 'content.js.download'), 'KRAKEN')
    spots = read_js_object(os.path.join(kf, 'spots.js.download'), 'KRAKEN_SPOTS')
    plates = os.path.join(INCOMING, 'kraken-plates')

    images = content['images']
    missing = [n for n in images.values() if not os.path.exists(os.path.join(plates, n))]
    if missing:
        raise SystemExit('%d plates missing from %s:\n  %s'
                         % (len(missing), plates, '\n  '.join(missing)))

    scenes = content['scenes']
    out = {'saga': TITLE, 'home': HOME, 'workingTitle': content['title'],
           'chapters': [], 'scenes': {}}

    for part in content['parts']:
        # The sequence names the scenes in play order; a ROUTE scene's two
        # paths are not in it, so pull them in from the route itself.
        ids = list(part['sequence'])
        for sid in list(ids):
            for ch in scenes.get(sid, {}).get('choices', []) or []:
                for step in ch['path']:
                    if step not in ids:
                        ids.append(step)

        out['chapters'].append(
            {'part': part['number'], 'title': part['title'], 'label': part['label'],
             'lead': part['lead'], 'cover': part['cover'], 'items': part['items'],
             'rules': part['rules'], 'endings': part['endings'],
             'sequence': part['sequence']})

        for sid in ids:
            s = dict(scenes[sid])
            cx, cy = spots[str(s['picture'])]
            w, h = DEFAULT_BOX
            s['hot'] = [round(cx * 100, 1), round(cy * 100, 1), w, h]
            s['chapter'] = part['number']
            out['scenes'][sid] = s

        q = sum(1 for sid in ids if scenes[sid]['kind'] in ('CCQ', 'GRAMMAR'))
        print('part %d %-12s %2d scenes, %2d questions'
              % (part['number'], part['title'], len(ids), q))

    with open(os.path.join(HERE, 'data.json'), 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=True)
        f.write('\n')

    # Every plate, in one folder beside the page — the covers are reached from
    # the chapter picker, so all 59 ship whichever chapter is played.
    art = os.path.join(REPO, SLUG)
    os.makedirs(art, exist_ok=True)
    for n in sorted(images.values()):
        shutil.copy2(os.path.join(plates, n), os.path.join(art, n))

    # The home plate is prepped from the cover art, not taken from the export,
    # so it is not in `images` and this is the only thing that notices it gone.
    if not os.path.exists(os.path.join(art, HOME)):
        raise SystemExit('%s/%s is missing — prep it from the cover art in incoming/' % (SLUG, HOME))

    print('%s/ — %d plates + %s; data.json — %d scenes, %d chapters'
          % (SLUG, len(images), HOME, len(out['scenes']), len(out['chapters'])))


if __name__ == '__main__':
    main()
