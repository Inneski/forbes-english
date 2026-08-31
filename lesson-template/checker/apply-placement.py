#!/usr/bin/env python3
"""Move text to the quietest placement the deck can express.

Reads the PLACEMENT findings from check-placement.py and rewrites the slide's
own data-side / data-vpos. Slides are addressed by POSITION, matched to the
DOM order the checker measured. Two traps, both hit once each: the template's
own comment contains the string "<section class=\"slide\">", so a naive count
is off by one from the DOM; and a deck can use the same plate on two slides
(Present Perfect Continuous 13 and 20 share bg23), so addressing by plate
silently edits the first one twice.

Usage: python3 apply-placement.py [--min 1.40] <deck.html> [more decks...]
"""
import importlib.util, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PINS = json.load(open(os.path.join(HERE, 'pins.json')))
spec = importlib.util.spec_from_file_location('cp', os.path.join(HERE, 'check-placement.py'))
cp = importlib.util.module_from_spec(spec); spec.loader.exec_module(cp)

MIN = 1.40
args = sys.argv[1:]
if args and args[0] == '--min':
    MIN = float(args[1]); args = args[2:]

for deck in args:
    data = json.loads(subprocess.run(['node', os.path.join(HERE, 'dump-rects.js'), deck],
                                     capture_output=True, text=True).stdout)
    root = os.path.dirname(os.path.abspath(deck))
    src = open(deck, encoding='utf-8').read()

    # Section tags in DOM order. Prose examples of the tag appear in the
    # template's own comments; a real slide always declares data-type, so that
    # is what separates a slide from a sentence about one.
    def section_spans(text):
        return [m for m in re.finditer(r'<section class="slide[^>]*>', text)
                if 'data-type=' in m.group(0)]

    spans = section_spans(src)
    pinned = PINS.get(os.path.basename(deck), {})
    moves, cache, edits, held = [], {}, [], []
    for s in data['slides']:
        if not s['slots'] or not s['bg']:
            continue
        p = os.path.join(root, s['bg'])
        if p not in cache:
            cache[p] = cp.detail_map(p) if os.path.exists(p) else None
        sd = cache[p]
        if sd is None:
            continue
        if str(s['index']) in pinned:
            held.append((s['index'], pinned[str(s['index'])]['why']))
            continue
        cur = f"{s['side']}/{s['vpos'] or 'center'}"
        scores = {k: cp.slot_score(sd, v) for k, v in s['slots'].items() if v}
        if cur not in scores or not scores[cur]:
            continue
        best = min(scores, key=scores.get)
        if best == cur or scores[cur] / scores[best] < MIN:
            continue
        side, vpos = best.split('/')
        if s['index'] > len(spans):
            print(f'  slide {s["index"]}: no matching section'); continue
        m = spans[s['index'] - 1]
        if f'data-bg="{s["bg"]}"' not in m.group(0):
            print(f'  slide {s["index"]}: source and DOM disagree, skipped'); continue
        tag = m.group(0)[:-1]
        tag = re.sub(r' data-side="[^"]*"', f' data-side="{side}"', tag)
        if 'data-side=' not in tag:
            tag += f' data-side="{side}"'
        tag = re.sub(r' data-vpos="[^"]*"', '', tag)
        if vpos != 'center':
            tag += f' data-vpos="{vpos}"'
        edits.append((m.start(), m.end(), tag + '>'))
        moves.append((s['index'], cur, best, scores[cur] / scores[best], s['bg']))
    for a, b, new in sorted(edits, reverse=True):   # back to front, so offsets hold
        src = src[:a] + new + src[b:]
    if moves:
        open(deck, 'w', encoding='utf-8').write(src)
    print(f'{os.path.basename(deck)}: {len(moves)} moved, {len(held)} held by pin')
    for i, why in held:
        print(f'   slide {i:<3} held    {why}')
    for i, a, b, r, bg in moves:
        print(f'   slide {i:<3} {a:<14} -> {b:<14} x{r:.2f}  {os.path.basename(bg)}')
