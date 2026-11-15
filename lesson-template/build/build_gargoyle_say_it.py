# -*- coding: utf-8 -*-
"""The Gargoyle House, Part 3: Say It Right (C1). House style 1. FREE.

Built 2026-11-15 from a Gemini Canvas quiz Innes shared ("make this a forbes
english free lesson"): "STUDIO · Pronunciation Brief", 50 four-option items
on an interior-design theme, no teaching, no explanations, one item a screen.
It is the pronunciation companion to The Gargoyle House Parts 1 and 2, so it
is set in the same story (Ashby Hall, Edith, Tom, Bianca, Rex) and reuses
that pair's plates, each once (GargoyleHouse/; no new art owed).

What changed from the source, item by item where it matters:
  - Answer leaks removed. 21 stems printed the stress mark in brackets
    after the word ("'development' (de'velopment)") — the answer, in the
    question.
  - Lazy Susan was unanswerable: it asked what "the 's' in Susan" makes,
    and Susan has two (/s/ then /z/). Now asks about the second.
  - Tactile: "rhymes with Smile / File" — a rhyme on the whole word is
    false; it is the second syllable that sounds like TILE. Re-asked.
  - The /ʒ/ item offered DETRIMENTAL, THRESHOLD, BEIGE, EN ROUTE — three
    filler distractors with no /ʒ/-adjacent sound at all. Now BEIGE against
    BADGE / BRIDGE / LEDGE (/dʒ/), the contrast learners actually miss.
  - "Both equally", "It is unstressed", "Neither", "None of the above" as
    padding are gone: a two-syllable word gets the two real options.
  - US spellings in the stems (color, aluminum) -> British, the site's.
  - Every item now explains itself, and each of the five stages opens with
    a rule slide (two-syllable stress; -TION/-IC/-IAN and -ATE/-ED/-MENT;
    endings that change nothing and syllables that disappear; vowel
    spellings; S, C and CH). The source taught nothing.

Order: the 50 items are regrouped by what they test (stress by word length
and ending, then vowels, then consonants) rather than the source's mix.

Run from the repo root:  py lesson-template/build/build_gargoyle_say_it.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

F = 'GargoyleHouse'
OUT = 'the-gargoyle-house-part-3.html'


def q(stem, options, why):
    return dict(stem=stem, options=options, correct=0, why=why)


B = '<strong>%s</strong>'

# ── 1 · two syllables ──────────────────────────────────────────────────
S1 = [
    (q('Bianca wants the hall to feel %s, like a loft in town. Which syllable is stressed?' % (B % 'urban'),
       ['UR-ban', 'ur-BAN'],
       'UR-ban. Do not confuse it with URBANE (ur-BANE): polite and sophisticated, a different word.'),
     'p1-talk'),
    (q('Strings of dried red %s hang in the new kitchen.' % (B % 'chillies'),
       ['CHIL-lies', 'chil-LIES'],
       'CHIL-lies, exactly like CHILLY (cold). British spelling chillies, American chilies.'),
     'p2-talk'),
    (q('The contract specifies aluminium window %s.' % (B % 'profiles'),
       ['PRO-files', 'pro-FILES'],
       'PRO-files. A PROFILE is a side view, or the shape of a frame seen in cross-section.'),
     'p2-c1-0'),
    (q('For the drawing room Bianca has chosen a %s stone fireplace.' % (B % 'rustic'),
       ['RUS-tic', 'rus-TIC'],
       'RUS-tic. Words ending in -IC stress the syllable just before it: RUS-tic, ar-TIS-tic, ce-RAM-ic.'),
     'p2-c4-4'),
    (q('Tom falls asleep against the train %s.' % (B % 'window'),
       ['WIN-dow', 'win-DOW'],
       'WIN-dow, and the end is a weak /əʊ/, as in SO: never “dow” as in COW.'),
     'p1-c3-4'),
    (q('Edith reads Bianca’s %s on the plans: all forty of them.' % (B % 'comments'),
       ['COM-ments', 'com-MENTS'],
       'COM-ments, noun and verb alike: “She COM-ments on everything.”'),
     None),
    (q('Edith spreads twelve room %s across the studio floor.' % (B % 'layouts'),
       ['LAY-outs', 'lay-OUTS'],
       'LAY-outs. Nouns made from phrasal verbs stress the first part: LAY-out (lay out), SET-up, CHECK-in.'),
     'p1-c4-0'),
    (q('“We’re going to %s the whole east wing.” Here it is a verb.' % (B % 'revamp'),
       ['re-VAMP', 'RE-vamp'],
       're-VAMP as a verb. The noun is often stressed at the front: “The hall needs a total RE-vamp.”'),
     'p2-c2-0'),
    (q('“The shark tank is pure %s,” says Tom. Which part carries the main stress?' % (B % 'Instagram bait'),
       ['INstagram bait', 'Instagram BAIT', 'inSTAgram bait'],
       'In a compound noun the first word carries the beat: INstagram bait, like CLICK bait or a SHARK tank.'),
     None),
]

# ── 2 · endings that tell you ──────────────────────────────────────────
S2 = [
    (q('Edith loves the slow %s of natural materials: oak, wool, linen.' % (B % 'cultivation'),
       ['cul-ti-VA-tion', 'CUL-ti-va-tion', 'cul-TI-va-tion', 'cul-ti-va-TION'],
       '-TION always pulls the stress onto the syllable just before it: cul-ti-VA-tion, re-no-VA-tion, de-co-RA-tion.'),
     None),
    (q('The plainest room in the house is a lesson in %s: nothing without a use.' % (B % 'utilitarianism'),
       ['u-til-i-TAR-i-an-ism', 'u-TIL-i-tar-i-an-ism', 'u-til-i-tar-I-an-ism', 'u-til-i-tar-i-AN-ism'],
       '-IAN pulls the stress onto the syllable before it, and -ISM never moves it: u-til-i-TAR-i-an, u-til-i-TAR-i-an-ism.'),
     'p1-c3-3'),
    (q('At the top of the tower is an %s room with one cushion and a candle.' % (B % 'isolated'),
       ['I-so-la-ted', 'i-SO-la-ted', 'i-so-LA-ted', 'i-so-la-TED'],
       'Words in -ATE stress the syllable two before the ending (I-so-late), and -ED changes nothing: I-so-la-ted.'),
     'p1-c2-2'),
    (q('The great staircase leads up to an %s landing.' % (B % 'elevated'),
       ['EL-e-va-ted', 'e-LE-va-ted', 'e-le-VA-ted', 'e-le-va-TED'],
       'EL-e-vate, EL-e-va-ted: two syllables before -ATE.'),
     'p1-c3-2'),
    (q('For the garden shed, Bianca wants a roof of %s iron.' % (B % 'corrugated'),
       ['COR-ru-ga-ted', 'cor-RU-ga-ted', 'cor-ru-GA-ted', 'cor-ru-ga-TED'],
       'COR-ru-gate: two syllables before -ATE, and the -ED changes nothing.'),
     'p2-c2-1'),
    (q('At the pitch, the model of the hall is %s by tiny lights.' % (B % 'illuminated'),
       ['il-LU-mi-na-ted', 'IL-lu-mi-na-ted', 'il-lu-MI-na-ted', 'il-lu-mi-NA-ted'],
       'il-LU-mi-nate: two syllables before -ATE. Five syllables, one strong beat.'),
     'p1-c4-3'),
    (q('Tom is now Edith’s junior %s (a noun here).' % (B % 'associate'),
       ['as-SO-ci-ate', 'AS-so-ci-ate', 'as-so-CI-ate', 'as-so-ci-ATE'],
       'as-SO-ci-ate, noun or verb. What changes is the end: the noun ends in a weak /ət/, the verb in /eɪt/.'),
     'p2-c1-2'),
    (q('“Who %s this?” asks Tom, staring at the bear in the top hat.' % (B % 'created'),
       ['cre-A-ted', 'CRE-a-ted', 'cre-a-TED'],
       'cre-ATE has only two syllables, so the beat lands on -ATE itself: cre-A-ted. The two-before rule needs three.'),
     'p1-c1-4'),
    (q('Half-built, the floor plan feels %s.' % (B % 'disjointed'),
       ['dis-JOINT-ed', 'DIS-joint-ed', 'dis-joint-ED'],
       'The prefix DIS- is rarely stressed, and -ED never is: dis-JOINT-ed.'),
     'p2-c3-0'),
    (q('Bianca is %s to have marble everywhere.' % (B % 'determined'),
       ['de-TER-mined', 'DE-ter-mined', 'de-ter-MINED'],
       'de-TER-mined, and the end is not “mind”: /dɪˈtɜːmɪnd/.'),
     'p1-c2-0'),
    (q('Across the valley, cranes rise over a new housing %s.' % (B % 'development'),
       ['de-VEL-op-ment', 'DE-vel-op-ment', 'de-vel-OP-ment', 'de-vel-op-MENT'],
       '-MENT is never stressed and never moves the stress: de-VEL-op, de-VEL-op-ment.'),
     'p2-c3-2'),
    (q('Edith explains the %s behind every choice.' % (B % 'rationale'),
       ['ra-tion-ALE', 'RA-tion-ale', 'ra-TION-ale'],
       'ra-tion-ALE: the stressed end sounds like “nahl” (British) or “nal” (American). Stress the front and it becomes RATIONAL.'),
     'p1-c3-1'),
    (q('Next to Bianca’s ideas, Edith’s plan looks very %s.' % (B % 'rational'),
       ['RA-tion-al', 'ra-TION-al', 'ra-tion-AL'],
       'RA-tion-al, with the beat up front: RASH-uh-nl. Compare ra-tion-ALE, the reasons behind a decision.'),
     None),
]

# ── 3 · learn these by heart ───────────────────────────────────────────
S3 = [
    (q('Tom has to %s ninety pages of contract.' % (B % 'interpret'),
       ['in-TER-pret', 'IN-ter-pret', 'in-ter-PRET'],
       'in-TER-pret, in-TER-pre-ter, in-ter-pre-TA-tion: the stress moves only when -TION arrives.'),
     'p2-c1-1'),
    (q('“I’m an %s designer,” Edith tells the planning officer.' % (B % 'interior'),
       ['in-TE-ri-or', 'IN-te-ri-or', 'in-te-RI-or', 'in-te-ri-OR'],
       'in-TE-ri-or de-SIGN-er. Its opposite works the same way: ex-TE-ri-or.'),
     'p2-c3-4'),
    (q('On the roof terrace, linen %s give shade.' % (B % 'canopies'),
       ['CAN-o-pies', 'ca-NO-pies', 'ca-no-PIES'],
       'CAN-o-py, CAN-o-pies: the -IES plural changes nothing.'),
     'p2-c2-3'),
    (q('Bianca asks about the %s of the family portraits.' % (B % 'origins'),
       ['OR-i-gins', 'o-RI-gins', 'o-ri-GINS'],
       'OR-i-gin, OR-i-gins. But o-RI-gi-nal and o-ri-gi-NAL-i-ty: here the stress moves as the word grows.'),
     'p1-c1-3'),
    (q('Rex tries to make the new colour scheme %s to Bianca.' % (B % 'palatable'),
       ['PAL-a-ta-ble', 'pa-LA-ta-ble', 'pa-la-TA-ble'],
       'PAL-a-ta-ble, from PAL-ate, the roof of the mouth. -ABLE does not move the stress of the word it joins.'),
     'p2-c4-2'),
    (q('The marble comes from a dealer who calls himself “the only %s in Carrara”.' % (B % 'foreigner'),
       ['FOR-eign-er', 'for-EIGN-er', 'for-eign-ER'],
       'FOR-eign, FOR-eign-er: -ER changes nothing. The G is silent: /ˈfɒrənə/.'),
     'p2-c3-3'),
    (q('Edith hires only %s contractors.' % (B % 'trustworthy'),
       ['TRUST-wor-thy', 'trust-WOR-thy', 'trust-wor-THY'],
       'TRUST-wor-thy, like PRAISE-wor-thy and NEWS-wor-thy: the first part carries the beat.'),
     'p2-c2-4'),
    (q('Rex keeps up a running %s on everything Edith does.' % (B % 'commentary'),
       ['COM-men-ta-ry', 'com-MEN-ta-ry', 'com-men-TA-ry'],
       'COM-men-ta-ry. In British English it often shrinks to three syllables: COM-men-tree.'),
     'p2-c3-1'),
    (q('Delivery %s block the drive every morning.' % (B % 'vehicles'),
       ['VE-hi-cles', 've-HI-cles', 've-hi-CLES'],
       'VE-hi-cles, and in British English the H is silent: VEE-uh-kls.'),
     None),
    (q('“That third chandelier is %s,” says Edith.' % (B % 'superfluous'),
       ['su-PER-flu-ous', 'SU-per-flu-ous', 'su-per-FLU-ous', 'su-per-flu-OUS'],
       'su-PER-flu-ous: four syllables, the beat on the second. Not “super” + “fluous”.'),
     'p1-c1-1'),
]

# ── 4 · vowels ─────────────────────────────────────────────────────────
S4 = [
    (q('The roof of Ashby Hall has a steep %s. Which word has the same vowel?' % (B % 'pitch'),
       ['itch', 'peach', 'patch', 'pouch'],
       'PITCH and ITCH share the short /ɪ/. PEACH has the long /iː/: the same pair as SHIP and SHEEP.'),
     'p1-c1-0'),
    (q('After the storm the cellar %s. Which word rhymes with FLOOD?' % (B % 'flooded'),
       ['blood', 'food', 'wood', 'mood'],
       'FLOOD and BLOOD are the two common words where OO says /ʌ/, as in CUP. FOOD and MOOD are /uː/; WOOD is /ʊ/.'),
     'p2-c4-3'),
    (q('Edith pins up the colour %s. Which word sounds exactly the same?' % (B % 'palette'),
       ['pallet and palate', 'pallet, a wooden platform', 'palate, the roof of the mouth', 'neither of them'],
       'PALETTE, PALATE and PALLET are all /ˈpælət/. Only the spelling and the context tell them apart.'),
     None),
    (q('Parts of Ashby Hall go back to %s times. FEUDAL begins with the same sound as …' % (B % 'feudal'),
       ['few', 'food', 'fell', 'foil'],
       'FEU- is /fjuː/, with a Y sound before the vowel, as in FEW and FUSE. FOOD has no Y: /fuːd/.'),
     'p1-c1-2'),
    (q('Edith prefers %s materials: stone, iron, untreated oak. RAW has the same vowel as …' % (B % 'raw'),
       ['law', 'row (a boat)', 'cow', 'rough'],
       'RAW and LAW: /ɔː/, the vowel in DOOR and SAW. Never /aʊ/ as in COW.'),
     None),
    (q('The upholsterer will %s the fabric by hand: weave, wove, woven. Which has a long /iː/, as in SEE?' % (B % 'weave'),
       ['weave', 'wove', 'woven', 'none of them'],
       'WEAVE has /iː/ and rhymes with LEAVE. The past forms change the vowel: WOVE, WOVEN.'),
     None),
    (q('Weave, %s, %s: which has the same vowel as COVE?' % (B % 'wove', B % 'woven'),
       ['wove and woven', 'wove only', 'woven only', 'weave and wove'],
       'WOVE and WOVEN both have /əʊ/, as in COVE and STOVE.'),
     None),
    (q('Bianca wants every surface to feel %s. In British English, its second syllable sounds like …' % (B % 'tactile'),
       ['tile', 'till', 'teal', 'tell'],
       'British TAC-tile ends like TILE: /ˈtæktaɪl/. American English often says TAC-tl, like the end of BATTLE.'),
     None),
    (q('The estate agent says the work will add %s. How is the end of VALUE said?' % (B % 'value'),
       ['like YOU', 'like OO in MOON', 'like UH in UP', 'it is silent'],
       'VAL-ue ends in /juː/, like YOU: /ˈvæljuː/. The same Y sound is in MENU and ARGUE.'),
     'p1-c4-1'),
    (q('The rugs are natural %s. How does British FIBRE compare with American FIBER?' % (B % 'fibre'),
       ['exactly the same', 'the RE is said “ray”', 'the I is short', 'the B is silent'],
       'FIBRE and FIBER are one word said one way: /ˈfaɪbə/. Only the spelling changes, as in CENTRE and CENTER.'),
     None),
]

# ── 5 · consonants ─────────────────────────────────────────────────────
S5 = [
    (q('“It %s like a museum,” says Bianca. How is the S in LOOKS said?' % (B % 'looks'),
       ['/s/ as in SNAKE', '/z/ as in ZOO', '/ʃ/ as in SHOE', 'it is silent'],
       'After /k/, /p/, /t/ or /f/ the -S is /s/: LOOKS, LAMPS, ROOFS. After a voiced sound it is /z/: CHAIRS, WALLS.'),
     None),
    (q('Some plaster on the ceiling is %s. How is the SE at the end said?' % (B % 'loose'),
       ['/s/ as in GOOSE', '/z/ as in LOSE', '/ʃ/ as in PUSH', 'it is silent'],
       'LOOSE /luːs/ (not tight) ends in /s/. LOSE /luːz/ (not win, mislay) ends in /z/.'),
     'p2-c4-0'),
    (q('“If we allow a gold lift, we set a %s.” How is the C said?' % (B % 'precedent'),
       ['/s/ as in SIT', '/k/ as in KIT', '/z/ as in ZIP', '/tʃ/ as in CHIP'],
       'C before E, I or Y is /s/: PRESS-i-dent, CEILING, CYPRESS. Before A, O or U it is /k/.'),
     None),
    (q('Edith restores the gothic %s of the chapel. The CH sounds like the CH in …' % (B % 'arches'),
       ['church', 'chorus', 'chef', 'choir'],
       'ARCHES has /tʃ/, as in CHURCH. CH is /k/ in words from Greek (CHORUS, CHOIR, ARCHITECT) and /ʃ/ in words from French (CHEF).'),
     None),
    (q('The bathroom floor is a %s of tiny tiles. How is the S said?' % (B % 'mosaic'),
       ['/z/ as in MAZE', '/s/ as in MASS', '/ʃ/ as in MASH', 'it is silent'],
       'mo-ZAY-ic: the S between two vowels is /z/, and the beat is on the second syllable.'),
     None),
    (q('A %s turns in the middle of the dining table. The first S in SUSAN is /s/. And the second?' % (B % 'lazy Susan'),
       ['/z/, like the Z in LAZY', '/s/, like the S in SUN', '/ʃ/, like the SH in SHE', 'it is silent'],
       'SUSAN is /ˈsuːzən/: /s/ at the start, /z/ between the vowels, the same sound as the Z in LAZY.'),
     None),
    (q('Bianca, born under %s, wants a fish tank in every room. How is the SC said?' % (B % 'Pisces'),
       ['/s/ as in PASS', '/k/ as in SCAN', '/ʃ/ as in FISH', '/sk/ as in DESK'],
       'PIE-seez: the SC is a single /s/, as in SCIENCE and SCENE, and the final S is /z/.'),
     'p1-c2-3'),
    (q('Edith will not use %s. Which word ends in the sound in the middle of MEASURE?' % (B % 'beige'),
       ['beige', 'badge', 'bridge', 'ledge'],
       'BEIGE ends in /ʒ/, the sound in MEASURE and TREASURE. BADGE, BRIDGE and LEDGE end in /dʒ/, as in JAM.'),
     None),
]

STAGES = [
    ('e1', 'r1T', 's1Q', S1, 'p1-c3-0',
     [('p1a', ['b1a'], '<b>UR</b>ban · <b>WIN</b>dow · <b>LAY</b>outs'),
      ('p1b', ['b1b'], 'to re<b>VAMP</b> · a <b>SHARK</b> tank')]),
    ('e2', 'r2T', 's2Q', S2, 'p1-c4-2',
     [('-TION · -IC · -IAN', ['b2a'], 'culti<b>VA</b>tion · <b>RUS</b>tic · utili<b>TAR</b>ian'),
      ('-ATE · -ED · -MENT', ['b2b'], '<b>I</b>solate · <b>I</b>solated · de<b>VEL</b>opment')]),
    ('e3', 'r3T', 's3Q', S3, 'p1-c2-1',
     [('p3a', ['b3a'], '<b>FOR</b>eign → <b>FOR</b>eigner · <b>PAL</b>ate → <b>PAL</b>atable'),
      ('p3b', ['b3b'], 'COM-men-tree · VEE-uh-kls')]),
    ('e4', 'r4T', 's4Q', S4, None,
     [('p4a', ['b4a'], 'f<b>oo</b>d · w<b>oo</b>d · fl<b>oo</b>d'),
      ('p4b', ['b4b'], 'palette = palate = pallet')]),
    ('e5', 'r5T', 's5Q', S5, None,
     [('-S · /s/ or /z/', ['b5a'], 'loo<b>ks</b> /s/ · mo<b>s</b>aic /z/'),
      ('C · CH', ['b5b'], 'pre<b>c</b>edent · <b>ch</b>urch · <b>ch</b>orus · <b>ch</b>ef')]),
]

WARM = ['Which English word do you avoid because you are not sure how to say it?',
        'Has anyone ever misunderstood a word you said?',
        'Which English sounds does your own language not have?',
        'How do you find out how a new word is pronounced?',
        'British or American: which accent do you hear most at work?',
        'Say <strong>interior designer</strong> out loud. Where did you put the beat?']

TALK2 = ['Say <strong>develop</strong>, <strong>development</strong> and <strong>developmental</strong>. Does the beat move?',
         'Which word from today surprised you most?',
         'Use <strong>palette</strong>, <strong>palate</strong> and <strong>pallet</strong> in three sentences your partner can tell apart.',
         'Say <strong>rational</strong> and <strong>rationale</strong>. What changes?',
         'Is <strong>flood</strong> the strangest spelling in English? Can you find a stranger one?',
         'Which word will you now say differently?']

CHIPS = ['de-VEL-op-ment', 'in-TE-ri-or', 'ra-tion-ALE', 'su-PER-flu-ous', 'il-LU-mi-na-ted',
         'PAL-a-ta-ble', 'mo-ZAY-ic', 'TRUST-wor-thy']

# Every plate is a Gargoyle House plate (Parts 1 and 2), shown once here.
PLATES = {
    'p1-results': 'a stone gargoyle with a bright butterfly resting on its nose',
    'p1-talk2': 'two designers talking over fabric samples and a house model at a big table',
    'p2-talk2': 'builders and designers sharing coffee on a scaffold at sunset',
    'p2-results': 'a restored country house glowing at dusk',
}
for _st in STAGES:
    if _st[4]:
        PLATES[_st[4]] = 'Gargoyle House plate'
    for _it, _sl in _st[3]:
        if _sl:
            PLATES[_sl] = 'Gargoyle House plate'

# ── chrome ─────────────────────────────────────────────────────────────
T = {
    'en': dict(
        coverTitle='The Gargoyle House <br><em>Say It Right</em>',
        coverSub='Fifty words from the studio, and where the beat falls in each. Stress, vowels and the sounds that catch out even fluent speakers.',
        chipLevel='C1', chipFocus='Pronunciation · 50 words',
        eW='Warm-up', tk1T='How do you say it?', eT='Let’s talk', tk2T='Over to you',
        e1='1 · Two syllables', e2='2 · Endings that tell you', e3='3 · Learn these by heart',
        e4='4 · Vowels', e5='5 · Consonants',
        r1T='Where the beat falls in short words', r2T='Let the ending tell you',
        r3T='No rule, so learn the word', r4T='Spelling is a poor guide', r5T='S, C and CH',
        s1Q='Where is the stress?', s2Q='Find the stressed syllable', s3Q='Where is the stress?',
        s4Q='Which sound?', s5Q='Which sound?',
        p1a='Nouns and adjectives', p1b='Verbs and compounds',
        p3a='Endings that change nothing', p3b='Syllables that disappear',
        p4a='One spelling, many sounds', p4b='One sound, many spellings',
        b1a='Most two-syllable nouns and adjectives stress the FIRST syllable. An -S ending changes nothing.',
        b1b='Many two-syllable verbs stress the SECOND syllable. In a compound noun the FIRST word takes the beat.',
        b2a='The stress falls on the syllable just BEFORE these endings.',
        b2b='-ATE words stress the syllable two before the ending. -ED and -MENT never move the stress.',
        b3a='-ER, -ABLE, -WORTHY, -IES and -S leave the stress where it was.',
        b3b='Fast British speech drops weak syllables and some letters.',
        b4a='OO can be /uː/ (food), /ʊ/ (wood) or /ʌ/ (flood). Learn the word, not the letters.',
        b4b='Different spellings can share one sound. FIBRE and FIBER are one word in two spellings.',
        b5a='After /p/, /t/, /k/ or /f/ the S is /s/. Between two vowels it is often /z/.',
        b5b='C before E, I or Y is /s/. CH is /tʃ/, but /k/ in Greek words and /ʃ/ in French ones.',
        actTitle='Present it, say it right', actUse='Use at least five:',
        actSpeakBrief='In pairs: one of you presents a room design to a client, the other listens only for stress and sounds.',
        actSpeak1='Designer: present the room in one minute, with at least five words from today.',
        actSpeak2='Listener: note any word where the beat fell in the wrong place, then say it back correctly.',
        actSpeak3='Swap roles. This time the client replies, using three of the words.',
        actWriteBrief='Write a short pitch (150–200 words) for a room you know well. Then write the stressed syllable of every word of three or more syllables in CAPITALS, and read it aloud.',
        actPlaceholder='This room is all about …',
        actWriteKind='Writing', slides='slides',
    ),
    'de': dict(
        coverTitle='The Gargoyle House <br><em>Say It Right</em>',
        coverSub='Fünfzig Wörter aus dem Studio und wo jeweils die Betonung liegt. Wortbetonung, Vokale und die Laute, über die selbst fließende Sprecher stolpern.',
        chipLevel='C1', chipFocus='Aussprache · 50 Wörter',
        eW='Zum Einstieg', tk1T='Wie sagt man das?', eT='Sprechen wir', tk2T='Jetzt du',
        e1='1 · Zwei Silben', e2='2 · Endungen, die es verraten', e3='3 · Auswendig lernen',
        e4='4 · Vokale', e5='5 · Konsonanten',
        r1T='Die Betonung in kurzen Wörtern', r2T='Die Endung verrät es',
        r3T='Keine Regel, also das Wort lernen', r4T='Die Schreibung führt in die Irre', r5T='S, C und CH',
        s1Q='Wo liegt die Betonung?', s2Q='Finde die betonte Silbe', s3Q='Wo liegt die Betonung?',
        s4Q='Welcher Laut?', s5Q='Welcher Laut?',
        p1a='Nomen und Adjektive', p1b='Verben und Komposita',
        p3a='Endungen, die nichts ändern', p3b='Silben, die verschwinden',
        p4a='Eine Schreibung, viele Laute', p4b='Ein Laut, viele Schreibungen',
        b1a='Die meisten zweisilbigen Nomen und Adjektive betonen die ERSTE Silbe. Ein -S am Ende ändert nichts.',
        b1b='Viele zweisilbige Verben betonen die ZWEITE Silbe. In einem zusammengesetzten Nomen trägt das ERSTE Wort die Betonung.',
        b2a='Die Betonung liegt auf der Silbe direkt VOR diesen Endungen.',
        b2b='Wörter auf -ATE betonen die Silbe zwei vor der Endung. -ED und -MENT verschieben die Betonung nie.',
        b3a='-ER, -ABLE, -WORTHY, -IES und -S lassen die Betonung, wo sie war.',
        b3b='Im schnellen britischen Englisch fallen schwache Silben und manche Buchstaben weg.',
        b4a='OO kann /uː/ (food), /ʊ/ (wood) oder /ʌ/ (flood) sein. Lern das Wort, nicht die Buchstaben.',
        b4b='Verschiedene Schreibungen können einen Laut teilen. FIBRE und FIBER sind ein Wort in zwei Schreibungen.',
        b5a='Nach /p/, /t/, /k/ oder /f/ ist das S ein /s/. Zwischen zwei Vokalen ist es oft ein /z/.',
        b5b='C vor E, I oder Y ist /s/. CH ist /tʃ/, aber /k/ in griechischen und /ʃ/ in französischen Wörtern.',
        actTitle='Präsentieren und richtig aussprechen', actUse='Verwende mindestens fünf:',
        actSpeakBrief='Zu zweit: Eine Person präsentiert einer Kundin einen Raumentwurf, die andere achtet nur auf Betonung und Laute.',
        actSpeak1='Designerin: Stell den Raum in einer Minute vor, mit mindestens fünf Wörtern von heute.',
        actSpeak2='Zuhörerin: Notier jedes Wort, bei dem die Betonung falsch lag, und sprich es richtig nach.',
        actSpeak3='Tauscht die Rollen. Diesmal antwortet die Kundin und verwendet drei der Wörter.',
        actWriteBrief='Schreib eine kurze Präsentation (150–200 Wörter) über einen Raum, den du gut kennst. Schreib dann bei jedem Wort mit drei oder mehr Silben die betonte Silbe in GROSSBUCHSTABEN und lies den Text laut vor.',
        actPlaceholder='This room is all about …',
        actWriteKind='Schreiben', slides='Folien',
    ),
    'es': dict(
        coverTitle='The Gargoyle House <br><em>Say It Right</em>',
        coverSub='Cincuenta palabras del estudio y dónde cae el acento en cada una. Acentuación, vocales y los sonidos que confunden incluso a quien habla con fluidez.',
        chipLevel='C1', chipFocus='Pronunciación · 50 palabras',
        eW='Para empezar', tk1T='¿Cómo se dice?', eT='A conversar', tk2T='Te toca',
        e1='1 · Dos sílabas', e2='2 · Terminaciones que lo dicen', e3='3 · Para aprender de memoria',
        e4='4 · Vocales', e5='5 · Consonantes',
        r1T='Dónde cae el acento en palabras cortas', r2T='La terminación lo dice',
        r3T='Sin regla: aprende la palabra', r4T='La ortografía engaña', r5T='S, C y CH',
        s1Q='¿Dónde está el acento?', s2Q='Encuentra la sílaba tónica', s3Q='¿Dónde está el acento?',
        s4Q='¿Qué sonido?', s5Q='¿Qué sonido?',
        p1a='Sustantivos y adjetivos', p1b='Verbos y compuestos',
        p3a='Terminaciones que no cambian nada', p3b='Sílabas que desaparecen',
        p4a='Una grafía, muchos sonidos', p4b='Un sonido, muchas grafías',
        b1a='La mayoría de los sustantivos y adjetivos de dos sílabas acentúan la PRIMERA. Una -S final no cambia nada.',
        b1b='Muchos verbos de dos sílabas acentúan la SEGUNDA. En un sustantivo compuesto, la PRIMERA palabra lleva el acento.',
        b2a='El acento cae en la sílaba justo ANTES de estas terminaciones.',
        b2b='Las palabras en -ATE acentúan la sílaba que está dos antes de la terminación. -ED y -MENT nunca mueven el acento.',
        b3a='-ER, -ABLE, -WORTHY, -IES y -S dejan el acento donde estaba.',
        b3b='En el inglés británico rápido se pierden sílabas débiles y algunas letras.',
        b4a='OO puede ser /uː/ (food), /ʊ/ (wood) o /ʌ/ (flood). Aprende la palabra, no las letras.',
        b4b='Grafías distintas pueden compartir un sonido. FIBRE y FIBER son una palabra con dos grafías.',
        b5a='Después de /p/, /t/, /k/ o /f/ la S es /s/. Entre dos vocales suele ser /z/.',
        b5b='C ante E, I o Y es /s/. CH es /tʃ/, pero /k/ en palabras griegas y /ʃ/ en las francesas.',
        actTitle='Preséntalo y pronúncialo bien', actUse='Usa al menos cinco:',
        actSpeakBrief='En parejas: uno presenta el diseño de una habitación a un cliente; el otro solo escucha el acento y los sonidos.',
        actSpeak1='Diseñador: presenta la habitación en un minuto, con al menos cinco palabras de hoy.',
        actSpeak2='Oyente: apunta cada palabra con el acento en el sitio equivocado y repítela bien.',
        actSpeak3='Cambiad los papeles. Esta vez el cliente responde usando tres de las palabras.',
        actWriteBrief='Escribe una breve presentación (150–200 palabras) de una habitación que conozcas bien. Luego escribe en MAYÚSCULAS la sílaba tónica de cada palabra de tres o más sílabas y léela en voz alta.',
        actPlaceholder='This room is all about …',
        actWriteKind='Escritura', slides='diapositivas',
    ),
}


# Twenty items have no plate of their own, so hs1 puts the mirrored hero
# behind them, fading in from 34% of the width. A full-width stem ran over
# the gargoyle's face. On those slides the question keeps to the clear left
# column (the explanation too, which appears below the options).
WASH_CSS = ('html[data-style="editorial"]:not(.is-flow) .slide[data-wash][data-type="mc"] .slide-body '
            '{ max-width: 520px; }')

# ── audio ──────────────────────────────────────────────────────────────
# Innes, 2026-11-15, "Yes, add audio". Each MC slide gets a button that says
# the word, and the contrast its explanation teaches, in the browser's own
# speech (en-GB voice where the device has one; no files to host). It stays
# hidden until the question is answered: hearing "de-VEL-op-ment" before
# choosing would be the answer key. '|' separates the phrases, spoken in turn.
SAY = [
    # 1 · two syllables
    'urban|urbane', 'chillies|chilly', 'profiles', 'rustic|artistic', 'window', 'comments',
    'layouts', 'to revamp|a revamp', 'Instagram bait',
    # 2 · endings
    'cultivation', 'utilitarian|utilitarianism', 'isolate|isolated', 'elevated', 'corrugated',
    'illuminated', 'an associate|to associate', 'create|created', 'disjointed', 'determined',
    'develop|development', 'rationale|rational', 'rational|rationale',
    # 3 · by heart
    'interpret|interpretation', 'interior designer', 'canopies', 'origins|original', 'palate|palatable',
    'foreign|foreigner', 'trustworthy', 'commentary', 'vehicles', 'superfluous',
    # 4 · vowels
    'pitch|itch|peach', 'flood|blood|food', 'palette|palate|pallet', 'feudal|few|food', 'raw|law|cow',
    'weave|leave', 'wove|woven|cove', 'tactile|tile', 'value|you', 'fibre',
    # 5 · consonants
    'looks|chairs', 'loose|lose', 'precedent', 'arches|church|chorus|chef', 'mosaic', 'lazy Susan',
    'Pisces', 'beige|badge',
]

SAY_CSS = '''
.say { display: none; align-self: flex-start; width: fit-content; align-items: center; gap: 10px; margin-top: 14px; padding: 8px 16px;
  border: 1.5px solid var(--border); border-radius: 999px; background: var(--surface);
  color: var(--text); font: inherit; font-size: 18px; cursor: pointer; }
.say:hover, .say.is-speaking { border-color: var(--accent); }
.say svg { width: 20px; height: 20px; flex: none; fill: currentColor; }
.slide[data-type="mc"]:has(.opt.correct) .say { display: inline-flex; }
html.no-tts .say { display: none !important; }'''

SAY_JS = '''<script>
(function () {
  var S = window.speechSynthesis;
  if (!S || !window.SpeechSynthesisUtterance) { document.documentElement.classList.add('no-tts'); return; }
  var voice = null;
  function pick() {
    var vs = S.getVoices(), gb = vs.filter(function (v) { return /en[-_]GB/i.test(v.lang); });
    voice = gb.filter(function (v) { return /natural|online|google|neural/i.test(v.name); })[0]
      || gb[0] || vs.filter(function (v) { return /^en/i.test(v.lang); })[0] || null;
  }
  pick();
  if (S.addEventListener) S.addEventListener('voiceschanged', pick); else S.onvoiceschanged = pick;
  document.addEventListener('click', function (e) {
    var b = e.target.closest && e.target.closest('.say');
    if (!b) return;
    e.preventDefault(); e.stopPropagation();
    S.cancel();
    var parts = b.getAttribute('data-say').split('|');
    b.classList.add('is-speaking');
    parts.forEach(function (t, i) {
      var u = new SpeechSynthesisUtterance(t);
      if (voice) u.voice = voice;
      u.lang = voice ? voice.lang : 'en-GB';
      u.rate = 0.85;
      if (i === parts.length - 1) u.onend = u.onerror = function () { b.classList.remove('is-speaking'); };
      S.speak(u);
    });
  }, true);
})();
</script>
'''

SPEAKER = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3a4.5 4.5 0 0 0-2.5-4.03v8.05'
           'A4.5 4.5 0 0 0 16.5 12zM14 3.23v2.06a7 7 0 0 1 0 13.42v2.06a9 9 0 0 0 0-17.54z"/></svg>')


def add_audio(path):
    """One .say button per MC slide, in item order, just above its feedback."""
    import re
    html = open(path, encoding='utf-8').read()
    assert 'class="say"' not in html
    parts = re.split(r'(<section class="slide"[^>]*data-type="mc"[^>]*>)', html)
    n = (len(parts) - 1) // 2
    assert n == len(SAY) == 50, '%d MC slides, %d SAY entries' % (n, len(SAY))
    for i, say in enumerate(SAY):
        body = parts[2 * i + 2]
        label = ' · '.join(say.split('|'))
        btn = ('<button class="say" type="button" data-say="%s" aria-label="Listen: %s">%s<span>%s</span></button>\n        '
               % (say, label, SPEAKER, label))
        assert body.count('<p class="feedback"') == 1
        parts[2 * i + 2] = body.replace('<p class="feedback"', btn + '<p class="feedback"', 1)
    html = ''.join(parts)
    assert html.count('</body>') == 1
    html = html.replace('</body>', SAY_JS + '</body>')
    open(path, 'w', encoding='utf-8', newline='').write(html)


def build():
    count = 1 + 1 + sum(1 + len(st[3]) for st in STAGES) + 1 + 2
    Tn = {}
    for c in T:
        d = dict(T[c])
        d['chipCount'] = '%d %s' % (count, d.pop('slides'))
        Tn[c] = d
    flow = [('talk', 'eW', 'tk1T', WARM, 'p1-talk2', 3)]
    for ek, rk, qk, items, rule_slot, cards in STAGES:
        flow += [('stage',),
                 ('rules', ek, rk, cards, rule_slot),
                 ('mc', ek, qk, [it for it, _ in items], [sl for _, sl in items], None)]
    flow += [('stage',), ('talk', 'eT', 'tk2T', TALK2, 'p2-talk2', 3)]
    SPEC = dict(out=OUT, title='The Gargoyle House, Part 3: Say It Right (C1)', folder=F, style='hs1',
                hero='p1-results', cover_name='pop-cover-p3', plates=PLATES, flow=flow, chips=CHIPS,
                results='p2-results', title_px=58, css=WASH_CSS + SAY_CSS)
    H.check_keys(Tn)
    H.build(SPEC, Tn)
    add_audio(OUT)
    assert sum(len(st[3]) for st in STAGES) == 50


if __name__ == '__main__':
    build()
