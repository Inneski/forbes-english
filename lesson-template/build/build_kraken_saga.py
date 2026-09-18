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

**Known gaps in this pass, deliberately.** English only — the nine languages
are the next and largest job. Hotspot boxes are the extractor's default 12x16
around each centre from spots.js, not yet looked at against their plates, and
docs/HANDOFF-rpg.md section 4 is right that this needs eyes. The export's
per-outcome consequence lines (`right`/`wrong`) are dropped, because the
engine's `fb` is one explanation shown either way; giving it `fbRight`/
`fbWrong` is a small generic change, batched with whatever else comes out of
review rather than spending a second eleven-builder re-run on its own.
"""
import json, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'kraken-saga', 'data.json'), encoding='utf-8'))
SLUG = 'kraken-black-tide-rpg'
NAME = 'The Kraken: A Tale of the Deep'
LANGS = ['es', 'de', 'fr', 'it', 'pt', 'ru']   # rpg.NINE is the target

# The export's own gold, which came off the artwork's one sodium-amber light —
# the thing IMAGES.md required in every frame so the glow marker has a colour
# to take. Not a camp colour: this game is not in a camp.
ACCENT, ACCENT_INK = '#efbb64', '#10222c'
DEEP, PANEL = '#08131c', 'rgba(8,19,28,.88)'

# a panel is 46% of the frame and the objects sit right of x=60 on every plate
# (IMAGES.md's composition contract), so every scene takes a left panel.
# the compass rose, the one object on the cover clear of the panel. Measured
# off 00_home.webp rather than guessed: the gold star's warm pixels centre on
# 77.9%, 83.7%, and the disc around them is about 7% by 12% of a 16:9 frame.
HOME_HOT = [77.9, 83.7, 7.0, 12.0]
ENDING_HOT = [80.0, 55.0, 14.0, 18.0]

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
            base = {'img': s['image'], 'hot': s['hot'], 'title': T(s['title']),
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
        # the cover was redrawn wider on 2026-09-18 and is 16:9, so it fills a
        # widescreen edge to edge while the 58 story plates are still 3:2 and
        # letterbox. ChatGPT is redrawing those wider too; when they land, this
        # override goes and img_w/img_h below become 1536x864 for the whole
        # game — and the spots.js hotspot percentages will need recomputing,
        # because widening a picture moves every x% in it.
        'imgW': 1536, 'imgH': 864,
        # the cover plate carries its own painted title lockup, so no title
        # here: head() would print the name a second time over the art. No
        # story line either — three chapter leads is already a panel's worth,
        # and a fourth paragraph pushed the third chapter off the bottom.
        'k': T('B1 ENGLISH · PRESENT PERFECT · THREE CHAPTERS'),
        # no story line: three chapter leads is already a panel's worth, and an
        # empty one cannot be glossed, so the key goes rather than sitting there
        # as '' for the validator to trip over.
        # 62, not the default 46: three chapter leads is a lot of panel, and
        # with a gloss under each one it overflowed by 78px in Spanish.
        'width': 70,
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
        # the plates are 3:2 and a browser window is 16:9, so `cover` throws
        # away a sixth of every picture's height — and the cover's title lockup
        # and the characters' heads live in exactly the strip it takes.
        'fit': 'contain',
        # the clue gets its own page and the question follows it, the way the
        # export reads ("THE CLUE / 3 OF 3" then "YOUR ANSWER") and the way
        # STORY.md describes a CCQ: you are given the information, then asked
        # about it. Without this, 82 of the 68 scenes' screens overflowed the
        # panel - in English as well as in gloss.
        'page_clues': True,
        'labels': LABELS,
        'start': 'hub', 'scenes': scenes, 'chapters': chapters,
        # page-level defaults, used by the HUD before a chapter is picked
        'endings': chapters[0]['endings'], 'max': 70, 'tiles': 4, 'chances': 3,
        'points': 5, 'complete_score': 60, 'total': 14,
    }


TRANSLATIONS = os.path.join(HERE, 'rpg', 'kraken-saga', 'translations')

if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), TRANSLATIONS))
