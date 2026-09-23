#!/usr/bin/env python3
"""THE KRAKEN: A TALE OF THE DEEP — Present Perfect / Continuous saga (B1).

    py lesson-template/build/build_kraken_saga.py

Builds kraken-black-tide-rpg.html at the repo ROOT from
lesson-template/build/rpg/kraken-saga/data.json.

**Not a Block Camp RPG.** Innes said so plainly on 2026-09-17 — "this isn't
block camp", "it's just RPG" — so the page sits at the root beside
stranger-gears-rpg.html and forbes-dnd-rpg.html, with its plates in a sibling
folder the way last-train-home-rpg.html carries its own. No hub card in
block-camp-hub/build.py, no camp colour, no Monocraft. rpg/README.md binds
"anything under block-camp/" and this is not that. The engine is still rpg.py,
because the nine-language gloss and the `--u` type scale are precisely the two
complaints this rebuild exists to answer: ChatGPT's version had no
translations at all and hardcoded 12-13px for its HUD, kickers and page
counts.

**Three chapters on one page.** Each part is its own game — 14 questions on
either branch, max 70, three chances, four collectibles, four endings — and
they are reached from a chapter picker, which is the shape Innes chose on
2026-09-17 over three separate library cards. `chapters` and the `hub` scene
kind went into rpg.py for this; before that the engine held one start, one max
and one endings map per page.

**Where the text came from.** ChatGPT was given this repo's STORY.md and
IMAGES.md and asked for the pictures and the hotspot boxes only. What came
back was a saved web page rather than a standalone file, so the game text is
already clean JSON in `content.js` and the hotspot centres are in `spots.js`.
rpg/kraken-saga/extract-export.py is the one that reads them; its docstring
calls this a fifth kind of export and says why.

**State as of 2026-09-23.** All nine gloss languages ship, 524 strings each
(`--strings` regenerates strings.json from this spec). The export's
per-outcome consequence lines ship as `fbRight`/`fbWrong`. Every hotspot was
checked: the sixty scene plates and twenty inserts on contact sheets, and
every page of every scene in every language under Playwright at 16:9,
1920x940 and phone width for overflow and for a panel hiding its own glow.
Corrections live in SCENE_HOT and INSERT_HOT below, with the reason for each.
"""
import json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'kraken-saga', 'data.json'), encoding='utf-8'))
SLUG = 'kraken-black-tide-rpg'
NAME = 'The Kraken: A Tale of the Deep'
LANGS = ['es', 'de', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']

# The export's own gold, which came off the artwork's one sodium-amber light —
# the thing IMAGES.md required in every frame so the glow marker has a colour
# to take. Not a camp colour: this game is not in a camp.
ACCENT, ACCENT_INK = '#efbb64', '#10222c'
DEEP, PANEL = '#08131c', 'rgba(8,19,28,.88)'

# a panel is 46% of the frame and the objects sit right of x=60 on every plate
# (IMAGES.md's composition contract), so every scene takes a left panel.
# The compass rose (77.9, 83.7) was the glow until 2026-09-23, when the hub
# panel had grown to 74 wide for Russian: with any gloss on, the open chapter
# list covered it 88-100%. The far-right sailing ship, x 84-92% on the plate,
# is the one object on the cover the wide panel leaves clear.
HOME_HOT = [88.0, 67.0, 8.0, 14.0]
ENDING_HOT = [80.0, 55.0, 14.0, 18.0]

# The glow on each insert plate, [cx, cy, w, h] in picture percent. Nine of the
# twenty inserts came from the export with a `spot` centre; eleven did not and
# were measured by eye off the plate on 2026-09-22. An insert needs one because
# the closed view of a scene is now the PAGE the reader is on, not the scene's
# own plate — see authored_pages() for why. This table wins over the export's
# `spot`: two of the nine spots were checked on a contact sheet and were off
# the object (the barrel's sat in the water under the buoy, the collie's on
# the pier edge below the dog), so they are corrected here.
INSERT_HOT = {
    'insert_barrel_insert.webp':  [72.0, 42.0, 14.0, 20.0],   # the buoy itself, not the water under it
    'insert_collie.webp':         [63.0, 40.0, 12.0, 16.0],   # the dog's face, not the pier edge
    # These two had their object dead centre, where an open panel covers it
    # from either side (the kayak rescue 100% under a glossed left panel, the
    # gaff 68%): Playwright, every page, 2026-09-23. The glow moves to the man
    # doing the thing, who stands in the half the panel leaves clear.
    'insert_gaff.webp':           [69.0, 53.0, 12.0, 16.0],   # Tulloch's hand on the gaff
    'insert_regatta_before.webp': [65.0, 54.0, 12.0, 16.0],   # the girl in 723
    'insert_regatta_prank.webp':  [80.0, 54.0, 12.0, 16.0],   # the boys' motorboat
    'insert_brannan_bell.webp':   [88.0, 32.0, 12.0, 16.0],   # the bell
    'insert_bell_strike.webp':    [70.0, 45.0, 12.0, 16.0],   # the clapper
    'insert_kayak_before.webp':   [65.0, 38.0, 12.0, 16.0],   # the kayaker
    'insert_kayak_shadow.webp':   [78.0, 32.0, 12.0, 16.0],   # the kayaker, from above
    'insert_kayak_rescue.webp':   [70.0, 22.0, 12.0, 16.0],   # Tulloch hauling him in
    'insert_beak_detail.webp':    [72.0, 51.0, 14.0, 18.0],   # the beak in the jar
    'insert_tulloch_close.webp':  [68.0, 44.0, 14.0, 20.0],   # Tulloch's face
    'insert_tide_detail.webp':    [74.0, 21.0, 12.0, 16.0],   # the finger on the black band
    'insert_cage_descent.webp':   [66.0, 35.0, 14.0, 20.0],   # the diver in the cage
}
DEFAULT_BOX = (12.0, 16.0)

# Scene plates whose export hotspot misses the object, found on a contact sheet
# of all sixty plates on 2026-09-23. The other fifty-seven land on their object.
SCENE_HOT = {
    '2.2':  [72.0, 10.0, 10.0, 12.0],   # the wheelhouse radio; the export put the
                                        # box half off the top of the frame
    '2.4':  [81.0, 33.0, 12.0, 18.0],   # the sonar screen, not the console under it
    '2.6b': [82.0, 48.0, 14.0, 18.0],   # the dinghy, not the water beneath it
}


def scene_hot(s):
    return list(SCENE_HOT.get(s['id'], s['hot']))


WORDS_PER_PAGE = 42              # what a 46% panel holds at 1.65 units without scrolling

# Two engine defaults are wrong for this game and are overridden here rather
# than in rpg.py, where they would change eleven other pages:
#   progress — the badge counts questions, not Wonderland's SPELLS.
#   visual   — the clue is a harbour log, a radio call or a line of speech, not
#              something seen. The export's own word for the block was THE
#              SCENE, so that is the word.
LABELS = {
    'progress': {'en': 'QUESTIONS', 'es': 'PREGUNTAS', 'de': 'FRAGEN', 'fr': 'QUESTIONS',
                 'it': 'DOMANDE', 'pt': 'PERGUNTAS', 'ru': 'ВОПРОСЫ', 'ar': 'أسئلة',
                 'zh': '题目', 'ja': '問題'},
    'visual':   {'en': 'THE SCENE', 'es': 'LA ESCENA', 'de': 'DIE SZENE', 'fr': 'LA SCÈNE',
                 'it': 'LA SCENA', 'pt': 'A CENA', 'ru': 'СЦЕНА', 'ar': 'المشهد',
                 'zh': '场景', 'ja': 'シーン'},
    # the engine says TILE RECOVERED, which is Block Camp's word; this game's
    # collectibles are evidence, marker barrels and the last four
    'relic':    {'en': 'SECURED · +{p} POINTS', 'es': 'CONSEGUIDO · +{p} PUNTOS',
                 'de': 'GESICHERT · +{p} PUNKTE', 'fr': 'OBTENU · +{p} POINTS',
                 'it': 'OTTENUTO · +{p} PUNTI', 'pt': 'CONSEGUIDO · +{p} PONTOS',
                 'ru': 'ПОЛУЧЕНО · +{p} ОЧКОВ', 'ar': 'حصلتِ عليه · +{p} نقاط',
                 'zh': '已到手 · +{p} 分', 'ja': '確保 · +{p} ポイント'},
}


def T(s):
    return {'en': s}


def plain(s):
    """The export writes Markdown; the engine escapes HTML and knows only its
    own [[a]]/[[b]] tone marks, so asterisks would print as asterisks."""
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s, flags=re.S)
    s = re.sub(r'\*(.+?)\*', r'\1', s, flags=re.S)
    s = re.sub(r'^\s*>\s?', '', s, flags=re.M)
    return s.strip()


def repair_speaker(prompt, dialogue):
    """Twenty-one of the fifty-one prompts come out of the export as `** "..."`
    with the speaker's name gone — a defect in the export, not in the stripping
    here, and it would have printed a bare `**` at learners. The name survives
    in the scene's dialogue, where the same quoted line is attributed, so take
    it from there rather than lose who is talking."""
    if not prompt.startswith('** '):
        return prompt
    key = prompt[3:].strip()[:60]
    for line in (dialogue or '').splitlines():
        if key and key in line:
            m = re.match(r'\s*\*\*(.+?):\*\*', line)
            if m:
                return '**%s:** %s' % (m.group(1), prompt[3:].strip())
    raise SystemExit('prompt with no recoverable speaker: %r' % prompt[:70])


SENT = re.compile('[^.!?]+[.!?]+[\'\"\u00bb\u201d\u2019)]*\\s*')


def pages_of(text):
    """Split an over-long authored panel, at LINE boundaries first.

    pages() splits on sentence ends, which is right for narration and wrong
    here: these panels are runs of dialogue, one speaker to a line, and a
    sentence split cuts a speaker in half and strips the closing quote onto
    the next page (`Not once. "`). So whole lines are kept together, and only
    a single line too long for the panel on its own is sentence-split - with a
    pattern that takes the closing quote with the full stop.
    """
    lines = [l.strip() for l in text.split(chr(10))]
    units = []
    for l in lines:
        if not l:
            continue
        if len(l.split()) > WORDS_PER_PAGE:
            units.extend(x.strip() for x in SENT.findall(l) if x.strip())
        else:
            units.append(l)
    out, cur = [], []
    for u in units:
        if cur and len((' '.join(cur) + ' ' + u).split()) > WORDS_PER_PAGE:
            out.append(' '.join(cur)); cur = [u]
        else:
            cur.append(u)
    if cur:
        out.append(' '.join(cur))
    return [T(x) for x in out] or [T(text)]


def pages(text):
    """Split a story block into panel-sized pages, at paragraph breaks where
    they fall and at sentence ends where a single paragraph is too long."""
    out, cur = [], ''
    for para in [p.strip() for p in plain(text).split('\n\n') if p.strip()]:
        units = [para]
        if len(para.split()) > WORDS_PER_PAGE:
            units = re.findall(r'[^.!?]+[.!?]*\s*', para) or [para]
        for u in units:
            u = u.strip()
            if not u:
                continue
            if cur and len((cur + ' ' + u).split()) > WORDS_PER_PAGE:
                out.append(cur)
                cur = u
            else:
                cur = (cur + ' ' + u).strip() if cur else u
    if cur:
        out.append(cur)
    return [T(p) for p in out] or [T('')]


def clue_pages(text, drop_tail=''):
    """A clue is a log, a radio call or a run of dialogue, and two of them —
    Tulloch's 1998 monologue worst of all — are far longer than a panel holds.
    Pack its lines into panel-sized pages the way pages() does for the story,
    keeping whole lines together so a forecast or a log entry is never split
    down the middle. `drop_tail` is the prompt, which the question asks on its
    own page and would otherwise be printed twice."""
    lines = [l.strip() for l in plain(text).splitlines() if l.strip()]
    if drop_tail:
        tail = [l.strip() for l in plain(drop_tail).splitlines() if l.strip()]
        if tail and lines[-len(tail):] == tail:
            lines = lines[:-len(tail)]
    out, cur = [], []
    for l in lines:
        if cur and len((' '.join(cur) + ' ' + l).split()) > WORDS_PER_PAGE:
            out.append(cur); cur = [l]
        else:
            cur.append(l)
    if cur:
        out.append(cur)
    return [T(join_lines(p)) for p in out]


def join_lines(lines):
    out = ''
    for l in lines:
        if not out:
            out = l
        elif out.endswith(':'):
            out += ' ' + l
        else:
            out += ' · ' + l
    return out


def oneline(text):
    """A clue is a quoted log or radio call: its line breaks carry meaning, but
    .clue does not set white-space, so they become separators. A line that ends
    in a colon is introducing the next one — "You hear:" — and takes a space,
    not a bullet, or the panel reads "You hear: · Brannan:"."""
    out = ''
    for l in [l.strip() for l in plain(text).splitlines() if l.strip()]:
        if not out:
            out = l
        elif out.endswith(':'):
            out += ' ' + l
        else:
            out += ' · ' + l
    return out


def authored_pages(s):
    """The 2026-09-22 export chose the reading pages itself: `panels`, each with
    its own picture and its own label ("THE SCENE", "YOU HEAR", "THE BELL").
    Where a scene has them, they are used as-is and pages()/clue_pages() do not
    run - splitting an author's pages again would cut them in the wrong places.

    A last panel that is only the prompt is dropped: the question has its own
    page and would otherwise print the line twice. Its picture is kept, so the
    question appears over the plate the reader was just looking at rather than
    jumping back to the scene's establishing shot.

    They render as story text under their label, not in the clue box: the box
    was this builder's way of marking quoted information, and the export's own
    labels now do that job better.

    Every page carries a `hot` as well as a picture. Until 2026-09-22 the engine
    showed the scene's own plate whenever the panel was closed, because that
    plate was the only picture with a glow position - and on these scenes that
    plate is the last moment, not the first: a reader arrived at 1.6 to the
    kayak in the tentacle and then read "BEYOND THE MOORINGS", at 1.13 to the
    dinghies over and the children in the water and then read "REGATTA
    SUNDAY". Innes's words for it: "pages jump in like spoilers". Now the
    closed view is the page the reader is on, so each insert needs a glow of
    its own: the export's `spot` where it gave one, INSERT_HOT where it did
    not, and the scene's hotspot where the page is the scene plate itself.
    """
    panels = s.get('panels')
    if not panels:
        return None, None
    prompt = plain(repair_speaker(s['prompt'], s.get('dialogue'))) if s.get('prompt') else None
    pages, ask_img, ask_hot = [], None, None
    for i, pan in enumerate(panels):
        txt = plain(pan['text'])
        hot = panel_hot(s, pan)
        last = i == len(panels) - 1
        if last:
            ask_img, ask_hot = pan['image'], hot
            if prompt and txt == prompt:
                continue
        # A panel the author wrote longer than the panel holds still has to be
        # read. Split it the way any story block is split and carry the picture
        # and the label across the parts, so the grouping survives even though
        # the page does not.
        for j, blk in enumerate(pages_of(txt)):
            pages.append({'t': 'story', 'b': blk, 'img': pan['image'], 'hot': hot,
                          'label': T(pan['label'])})
    return pages, (ask_img, ask_hot)


def panel_hot(s, pan):
    """Where the glow sits on a panel's picture: the scene's own hotspot when
    the picture is the scene plate, the export's `spot` centre (picture
    fractions) in the default box when it gave one, INSERT_HOT otherwise. An
    insert with none of the three is refused rather than left with a glow
    floating over nothing."""
    img = pan['image']
    if img == s['image']:
        return scene_hot(s)
    if img in INSERT_HOT:
        return list(INSERT_HOT[img])
    if pan.get('spot'):
        return [round(pan['spot'][0] * 100, 1), round(pan['spot'][1] * 100, 1), *DEFAULT_BOX]
    raise SystemExit('no hotspot for insert %s (scene %s): add it to INSERT_HOT' % (img, s['title']))


def build():
    scenes = {}
    chapters = []

    for ci, ch in enumerate(DATA['chapters']):
        seq = ch['sequence']
        n = ch['part']
        end = {k: 'end%d_%s' % (n, k) for k in ch['endings']}

        # what follows each scene: the next id in the sequence, and for a
        # branch, the scene the branch rejoins.
        nxt = {}
        for i, sid in enumerate(seq):
            after = seq[i + 1] if i + 1 < len(seq) else 'resolve'
            s = DATA['scenes'][sid]
            # a choice scene ignores `next` — its routes say where to go — but
            # it still has to be in the map to be built at all.
            nxt[sid] = after
            if s['kind'] == 'ROUTE':
                for c in s['choices']:
                    for j, step in enumerate(c['path']):
                        nxt[step] = c['path'][j + 1] if j + 1 < len(c['path']) else after

        # the last question on either branch decides finalCorrect
        finals = {sid for sid, v in nxt.items() if v == 'resolve'}

        for sid, v in nxt.items():
            s = DATA['scenes'][sid]
            base = {'img': s['image'], 'hot': scene_hot(s), 'title': T(s['title']),
                    'story': pages(s['narration'])}
            if s.get('act'):
                base['k'] = T(s['act'])
            if s['kind'] in ('CCQ', 'GRAMMAR'):
                prompt = repair_speaker(s['prompt'], s.get('dialogue'))
                base.update({
                    'kind': 'question', 'next': v,
                    'prompt': T(oneline(prompt)),
                    'opts': [{'en': o} for o in s['options']],
                    'answer': s['correct'], 'fb': T(plain(s['why']))})
                # the export's per-outcome consequence lines ("The bell rings.
                # Mrs Rennie sits down on the step." / "Brannan rings it
                # anyway.") — dropped until 2026-09-23 for want of an engine
                # slot; rpg.py now shows them between the verdict and `fb`
                if s.get('right'):
                    base['fbRight'] = T(plain(s['right']))
                if s.get('wrong'):
                    base['fbWrong'] = T(plain(s['wrong']))
                # the dialogue ends with the prompt, which now has a page of
                # its own, so drop it here rather than print it twice
                clue = clue_pages(s['dialogue'], prompt)
                if clue:
                    base['clue'] = clue
                if s.get('item'):
                    base['relic'] = True
                if sid in finals:
                    base['final'] = True
            elif s['kind'] == 'STORY':
                base.update({'kind': 'story', 'next': v})
            elif s['kind'] == 'ROUTE':
                base.update({'kind': 'choice', 'routes': [
                    {'name': T(c['name']), 'desc': T(plain(c['text'])),
                     'target': c['path'][0], 'route': c['name']}
                    for c in s['choices']]})
            # an authored run of panels replaces both the split story and the
            # split clue, and carries the pictures and labels with it
            auth, ask = authored_pages(s)
            if auth:
                base['pages'] = auth
                base.pop('story', None)
                base.pop('clue', None)
                if ask and ask[0]:
                    base['askImg'], base['askHot'] = ask
            scenes[sid] = base

        for key, text in ch['endings'].items():
            # part three's master ending has a plate of its own; the rest close
            # on their chapter's cover.
            img = '59_ending_master.webp' if (n == 3 and key == 'master') else ch['cover']
            scenes[end[key]] = {
                'kind': 'ending', 'img': img, 'hot': ENDING_HOT,
                'k': T('%s · %s' % (ch['title'], key.upper())),
                'title': T(ch['title']),
                'story': pages(re.sub(r'\s+', ' ', text))}

        chapters.append({
            'title': T('%s' % ch['title']), 'lead': T(plain(ch['lead'])),
            'tilesLabel': T(ch['label']),
            'start': seq[0], 'endings': end,
            # the export's own ending rule, kept exactly: pass 60, then the
            # four collectibles, then a perfect 70 for the master ending.
            'max': 70, 'tiles': 4, 'chances': 3, 'passScore': 60,
            'completeScore': 60, 'total': 14, 'bands': []})

    scenes['hub'] = {
        'kind': 'hub', 'img': DATA['home'], 'hot': HOME_HOT,
        # the cover plate carries its own painted title lockup, so no title
        # here: head() would print the name a second time over the art. No
        # story line either — three chapter leads is already a panel's worth,
        # and a fourth paragraph pushed the third chapter off the bottom.
        'k': T('B1 ENGLISH · PRESENT PERFECT · THREE CHAPTERS'),
        # no story line: three chapter leads is already a panel's worth, and an
        # empty one cannot be glossed, so the key goes rather than sitting there
        # as '' for the validator to trip over.
        # 74, not the default 46: three chapter leads is a lot of panel, and
        # with a gloss under each one it overflowed by 78px in Spanish at 62
        # and by 14px in Russian at 70 (measured 2026-09-22 at 16:9; 72 was
        # still 14 over, 74 is the first width that clears it).
        'width': 74,
        'small': T('14 questions a chapter · 4 collectibles · 3 chances · your choices change the route')}

    return {
        'file': '%s.html' % SLUG,
        'img_dir': SLUG,
        # data.json holds the name as it is set on the cover, in capitals; a
        # page title and a library card want it in sentence case.
        'title': '%s — Present Perfect West Highland RPG (B1)' % NAME,
        'description': 'An interactive B1 English lesson from Forbes English: %s, '
                       'a three-chapter Present Perfect RPG on the west coast of Scotland.' % NAME,
        'langs': LANGS,
        'accent': ACCENT, 'accent_ink': ACCENT_INK, 'deep': DEEP, 'panel': PANEL,
        # Every plate is 16:9 as of the 2026-09-22 re-import, so it fills an
        # ordinary window exactly. `contain` stays: it costs nothing when the
        # aspects match and it is what stops an unusual window shape cropping
        # the art rather than letterboxing it.
        'img_w': DATA['imgW'], 'img_h': DATA['imgH'],
        'fit': 'contain',
        # the clue gets its own page and the question follows it, the way the
        # export reads ("THE CLUE / 3 OF 3" then "YOUR ANSWER") and the way
        # STORY.md describes a CCQ: you are given the information, then asked
        # about it. Without this, 82 of the 68 scenes' screens overflowed the
        # panel - in English as well as in gloss.
        'page_clues': True,
        'labels': LABELS,
        # not a Block Camp game: no CAMP MAP button on the endings and no camp
        # save written, both of which it had until 2026-09-23
        'camp': False,
        'start': 'hub', 'scenes': scenes, 'chapters': chapters,
        # page-level defaults, used by the HUD before a chapter is picked
        'endings': chapters[0]['endings'], 'max': 70, 'tiles': 4, 'chances': 3,
        'points': 5, 'complete_score': 60, 'total': 14,
    }


TRANSLATIONS = os.path.join(HERE, 'rpg', 'kraken-saga', 'translations')
STRINGS = os.path.join(HERE, 'rpg', 'kraken-saga', 'strings.json')
NL = chr(10)


def learner_strings(spec):
    """Every English string a translation file has to cover, in page order:
    exactly the set rpg.validate() checks, so a file that covers this list
    builds. Options are left out because the engine does not gloss them."""
    seen = []
    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get('en'), str):
                if o['en'] not in seen:
                    seen.append(o['en'])
                return
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    keys = set(rpg.TEXT_KEYS) | {'rules', 'routes', 'button', 'routeStory'}
    for s in spec['scenes'].values():
        walk({k: v for k, v in s.items() if k in keys})
    for ch in spec['chapters']:
        walk({k: v for k, v in ch.items() if k in ('title', 'lead', 'tilesLabel')})
    walk(spec['labels'])
    return seen


if __name__ == '__main__':
    # `--strings` rewrites strings.json from the spec, which is what it is: until
    # 2026-09-23 it was hand-kept, and the 101 consequence lines were only found
    # because validate() refused them
    if '--strings' in sys.argv:
        out = learner_strings(build())
        with open(STRINGS, 'w', encoding='utf-8', newline=NL) as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
            f.write(NL)
        print('wrote %s: %d strings' % (os.path.relpath(STRINGS), len(out)))
    else:
        rpg.assemble(rpg.apply_translations(build(), TRANSLATIONS))
