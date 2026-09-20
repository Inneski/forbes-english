#!/usr/bin/env python3
"""Block Camp Village — a walkable top-down camp where the weather teaches.

    python3 lesson-template/build/block-camp-village/build.py

Writes block-camp/village.html. Innes sent undead-fish.com/en on 2026-09-20 —
a pixel town you walk round with the arrow keys, "press space" to talk,
"MET 0/7" in the corner — and asked how Block Camp could be that. This is
the prototype: a camp drawn in code (no tileset, no sprite sheet yet), one
ranger per tense standing by their cabin, three questions each, and the
reward for getting them right is the weather doing the sentence in that
ranger's tense — clouds gather under "It is going to rain.", rain falls
under "It is raining.", it clears under "It has stopped raining." His
words: "the snow isn't important, maybe 'it is raining' and 'it is going
to rain' can be written into the game and appear briefly."

Everything a learner reads is in this file (RANGERS), so a wording change
is a rebuild, not a hunt through the page. The camps come from the hub
builder's tables so the cabin links and colours cannot drift from the hub.
The world is the hub's own trail painting (BlockCamp/hub-hero.jpg): the
hiker walks the painted path from the tent, over the bridge and up to the
lookout tower, shrinking with depth, and the camera zooms to follow. The
path is `TRAIL` in template.html, in picture pixels; the rangers stand at
even spacings along it. The first build drew a tile map in code and Innes
called the graphics "pants" — rightly. Walking on the real art is the fix.

Save state: CampSave.get('village') → {met:{camp:true}, best:{camp:n}}.
"""
import importlib.util, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
HUB = os.path.join(HERE, '..', 'block-camp-hub')
spec = importlib.util.spec_from_file_location('hub', os.path.join(HUB, 'build.py'))
hub = importlib.util.module_from_spec(spec); spec.loader.exec_module(hub)

# Per camp: the ranger's name, their greeting (in the tense), three questions
# (prompt with ___, options, index of the right one, a one-line explanation),
# and the weather reward: [phase, caption]. Phases the engine knows:
# clouds, rain, clear, sun, night, wind. The caption is what appears while
# it happens — the sentence IS the reward.
RANGERS = {
 1: dict(name='Ranger Sam', hi="Morning! I light these lamps every evening. Same time, every day.",
   q=[("The ranger ___ the lamps every evening.", ["lights", "is lighting", "lit"], 0, "A habit, every evening: Present Simple, and he/she/it takes -s."),
      ("Water ___ at 100 degrees.", ["boils", "is boiling", "boiled"], 0, "A fact that is always true takes the Present Simple."),
      ("She ___ coffee.", ["doesn't drink", "don't drink", "not drinks"], 0, "Negative with he/she/it: doesn't + the bare verb.")],
   weather=[('sun', "It rains here every afternoon. Every morning, the sun shines.")]),
 2: dict(name='Ranger Mia', hi="Look at the sky! Something is happening up there right now.",
   q=[("Look! It ___.", ["is raining", "rains", "rained"], 0, "Happening right now, as we watch: Present Continuous."),
      ("They ___ a tent at the moment.", ["are putting up", "put up", "have put up"], 0, "An action in progress at this moment: are + -ing."),
      ("Why ___ you laughing?", ["are", "do", "did"], 0, "Questions in the Present Continuous start with am/is/are.")],
   weather=[('rain', "It is raining.")]),
 3: dict(name='Ranger Tom', hi="It rained all night. I crossed the bridge at dawn and it was still wet.",
   q=[("We ___ the bridge yesterday.", ["crossed", "cross", "have crossed"], 0, "Finished, with a time in the past (yesterday): Past Simple."),
      ("He ___ go to the cinema last night.", ["didn't", "doesn't", "hasn't"], 0, "Past negative: didn't + the bare verb."),
      ("___ you see the tiger?", ["Did", "Do", "Have"], 0, "Past Simple questions start with Did.")],
   weather=[('rain', "It rained."), ('clear', "It rained, and then it stopped.")]),
 4: dict(name='Ranger Ana', hi="When you arrived, I was watching the clouds. They were moving fast.",
   q=[("It ___ when we arrived.", ["was raining", "rained", "is raining"], 0, "In progress at a moment in the past: was/were + -ing."),
      ("They ___ while the ranger talked.", ["were listening", "listened", "are listening"], 0, "A longer action around a shorter one: Past Continuous."),
      ("What ___ you doing at eight o'clock?", ["were", "did", "are"], 0, "Questions: was/were + subject + -ing.")],
   weather=[('rain', "It was raining when you arrived."), ('clear', "")]),
 5: dict(name='Ranger Leo', hi="See those clouds? I know what they mean. Something is going to happen.",
   q=[("Look at those clouds. It ___ rain.", ["is going to", "will", "is"], 0, "Evidence now (the clouds) about the future: going to."),
      ("I ___ climb the tower tomorrow.", ["am going to", "will going to", "going to"], 0, "A plan already made: am/is/are going to."),
      ("___ they going to camp here?", ["Are", "Do", "Will"], 0, "Questions: Are/Is + subject + going to.")],
   weather=[('clouds', "It is going to rain."), ('rain', "It is raining.")]),
 6: dict(name='Ranger Zoe', hi="Don't worry about the weather. I'll tell you what it will do tonight.",
   q=[("Don't worry, I ___ help you.", ["will", "am going to", "would"], 0, "A decision made at the moment of speaking: will."),
      ("It ___ be cold tonight.", ["will", "is", "was"], 0, "A prediction with no evidence in front of us: will."),
      ("I think she ___ come.", ["won't", "willn't", "doesn't will"], 0, "The negative of will is won't.")],
   weather=[('night', "It will be cold tonight."), ('clear', "")]),
 7: dict(name='Ranger Kai', hi="I've climbed that tower three times. I've never seen a view like it.",
   q=[("I ___ the tower three times.", ["have climbed", "climbed", "am climbing"], 0, "Experience up to now, no time given: Present Perfect."),
      ("___ you ever seen snow?", ["Have", "Did", "Do"], 0, "Ever + experience: Have/Has + subject + past participle."),
      ("She ___ just left.", ["has", "have", "had"], 0, "A recent action with 'just': has + past participle.")],
   weather=[('rain', "It has been raining."), ('clear', "It has stopped raining.")]),
 8: dict(name='Ranger Ivy', hi="It's been raining for hours. I've been waiting here since dawn.",
   q=[("It ___ for hours.", ["has been raining", "has rained", "is raining"], 0, "Still going on, with 'for hours': Present Perfect Continuous."),
      ("How long ___ you been waiting?", ["have", "did", "are"], 0, "Questions: How long + have/has + subject + been + -ing."),
      ("They ___ since dawn.", ["have been walking", "walk", "are walking"], 0, "Since dawn until now, still happening: have been + -ing.")],
   weather=[('rain', "It has been raining all day."), ('clear', "")]),
 9: dict(name='Ranger Rex', hi="By the time you got here, the rain had stopped. Lucky you.",
   q=[("When we got there, the rain ___.", ["had stopped", "stopped", "has stopped"], 0, "The earlier of two past events: had + past participle."),
      ("She ___ never seen a tiger before that day.", ["had", "has", "was"], 0, "Before a past moment: Past Perfect."),
      ("___ they left before you arrived?", ["Had", "Did", "Have"], 0, "Questions: Had + subject + past participle.")],
   weather=[('rain', ""), ('clear', "The rain had stopped when you arrived.")]),
}

def present(p): return os.path.exists(os.path.join(REPO, p))

camps = []
for n, name, slug, l1, l2 in hub.CLIMB:
    if not present(f'blockcamp-{slug}.html'): continue
    r = RANGERS[n]
    camps.append({'n': n, 'tense': name, 'colour': hub.CAMP[n], 'ink': hub.INK[n], 'href': f'../blockcamp-{slug}.html',
                  'ranger': r['name'], 'hi': r['hi'], 'weather': r['weather'],
                  'q': [{'p': p, 'o': o, 'a': a, 'fb': fb} for p, o, a, fb in r['q']]})

def build():
    rd = lambda d, n: open(os.path.join(d, n), encoding='utf-8').read()
    nav = rd(HUB, 'nav.html')
    nav = re.sub(r'href="(?!https?:|mailto:|#|\.\./)([^"]+)"', r'href="../\1"', nav)
    nav = re.sub(r'src="(?!https?:|data:|\.\./)([^"]+)"', r'src="../\1"', nav)
    nav = nav.replace('href="../block-camp.html" aria-current="page"', 'href="../block-camp.html"')
    page = (rd(HERE, 'template.html').replace('{{MONOCRAFT}}', rd(HUB, 'monocraft.css')).replace('{{NAV}}', nav)
            .replace('{{CAMPS}}', json.dumps(camps, ensure_ascii=False, separators=(',', ':'))))
    out = os.path.join(REPO, 'block-camp', 'village.html')
    open(out, 'w', encoding='utf-8', newline='\n').write(page)
    print('wrote block-camp/village.html — %d rangers, %d questions' % (len(camps), sum(len(c['q']) for c in camps)))

if __name__ == '__main__':
    build()
