# -*- coding: utf-8 -*-
"""The Gargoyle House, Part 4: The Designer's Lexicon (C1). House style 1. FREE.

Built 2026-11-15 from a Gemini Canvas quiz Innes shared: "The Designer's
Lexicon", a "Studio Assessment" of 100 definition -> word items in two parts
of 50 (Concept & Drafting, Execution & Staging). His student could not open
the Gemini link, and he asked for it on Forbes English "and make the multiple
choice answers less obvious". The 100 words are the same list as The Gargoyle
House Parts 1 and 2, so this is that story's fourth part, on its plates (no
new art owed).

What changed from the source:
  - Distractors. Gemini drew three other words from the list at random, so
    every item paired, say, "a person who works puppets" with INERT,
    STIMULATOR and AFFILIATION: the word class alone gave the answer. Every
    item now has three hand-written distractors of the SAME word class and
    form (an -ly adverb against -ly adverbs, a phrasal verb against phrasal
    verbs with the same particle or verb), chosen from three kinds of trap:
      look-alikes   decisive/DIVISIVE, oversee/OVERLOOK, confirm/CONFORM,
                    picturesque/GROTESQUE, hearsay/HERESY, simulator/STIMULATOR
      near meanings executor/HEIR, maggot/CATERPILLAR, half-truth/WHITE LIE,
                    grotesque (the carving)/GARGOYLE, eaves/GUTTER
      family sets   put one's foot in it / put one's feet up / PUT ONE'S
                    FOOT DOWN; God forbid / God knows / THANK GOD
    None is a synonym a teacher would have to accept (the synonym ban):
    FACADE and DISGUISE (for GUISE), BENEFICIARY (HEIR), RUN OVER (RUN
    DOWN), BUTTER UP (SUCK UP), FASTIDIOUS (METICULOUS) and the like were
    considered and left out.
  - The key is never the only longest option (hs2quiz's gate), and the
    engine shuffles the options on screen.
  - Every item explains itself, naming the most tempting wrong answer.
  - Two definitions were the same: EXPLOIT and EXPLOITED were both "make
    full use of and derive benefit from (a resource)". EXPLOITED now tests
    the other sense (workers treated unfairly for someone else's profit).
    STIMULANT and STIMULATOR were near-identical too: the stimulator is now
    the device.
  - AFFILIATION was defined by AFFILIATE ("the state of being affiliated"),
    itself on the list: now defined in plain words. TENURE's "the holding of
    an office" read as a building, which made TENANCY right: now "an
    official position". BLINKERED gets its figurative sense beside the
    horse. The OUTSTANDING (1)/(2) labels are gone: each stem now carries
    its context.
  - US spellings -> British (haemophilia, polarise, epitomise, behaviour).

Order: the source's random order is regrouped by word class (eight stages of
12-13), because a learner who knows the class still has to know the word.

Run from the repo root:  py lesson-template/build/build_gargoyle_lexicon.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

F = 'GargoyleHouse'
OUT = 'the-gargoyle-house-part-4.html'


def q(stem, key, d1, d2, d3, why):
    return dict(stem='“%s”' % stem, options=[key, d1, d2, d3], correct=0, why=why)


# ── 1 · people and things ──────────────────────────────────────────────
S1 = [
    q('a person who works puppets',
      'puppeteer', 'marionette', 'stagehand', 'illusionist',
      'PUPPETEER: the person. A MARIONETTE is the puppet itself, the kind worked by strings.'),
    q('a person who conforms to accepted behaviour or established practices',
      'conformist', 'nonconformist', 'perfectionist', 'opportunist',
      'CONFORMIST. A NONCONFORMIST is the opposite: someone who refuses to follow the usual rules.'),
    q('a person new to or inexperienced in a field or situation',
      'novice', 'veteran', 'novelist', 'nominee',
      'NOVICE. Not NOVELIST (a writer of novels), and the opposite of a VETERAN.'),
    q('a person legally entitled to the property or rank of another on that person’s death',
      'heir', 'executor', 'trustee', 'landlord',
      'HEIR (the H is silent: “air”). The EXECUTOR only carries out the will; the heir receives.'),
    q('a woman who is legally entitled to the property or rank of another on that person’s death',
      'heiress', 'governess', 'duchess', 'patroness',
      'HEIRESS. A DUCHESS holds a rank already; a GOVERNESS teaches children in a private house.'),
    q('people who have recently acquired wealth, typically seen as showy or lacking in good taste',
      'nouveau riche', 'old money', 'the jet set', 'the landed gentry',
      'NOUVEAU RICHE (“new rich”, from French). OLD MONEY and THE LANDED GENTRY are the families who have been rich for generations.'),
    q('a grotesque carved face or figure projecting from the gutter of a building, acting as a spout to carry water clear of a wall',
      'gargoyle', 'grotesque', 'corbel', 'finial',
      'GARGOYLE: the spout is the clue. A carved figure that carries no water is a GROTESQUE.'),
    q('a shallow trough fixed beneath the edge of a roof for carrying off rainwater',
      'gutter', 'drainpipe', 'eaves', 'sill',
      'GUTTER: it runs along the roof edge. The EAVES are that edge itself; the DRAINPIPE carries the water down.'),
    q('a pipe for carrying off rainwater or liquid waste from a building',
      'drainpipe', 'gutter', 'flue', 'hosepipe',
      'DRAINPIPE. A GUTTER is an open trough, not a pipe; a FLUE carries smoke up a chimney.'),
    q('a valuable object that has belonged to a family for several generations',
      'heirloom', 'antique', 'keepsake', 'souvenir',
      'HEIRLOOM: the family is the point. An ANTIQUE is simply old and valuable, whoever owned it.'),
    q('the larva of a butterfly or moth: a soft, worm-like creature with many legs',
      'caterpillar', 'chrysalis', 'centipede', 'maggot',
      'CATERPILLAR. The CHRYSALIS is the next stage, in its case; a MAGGOT is the larva of a fly.'),
    q('a compound found especially in tea and coffee plants that stimulates the central nervous system',
      'caffeine', 'nicotine', 'tannin', 'melatonin',
      'CAFFEINE. TANNIN is also in tea (it makes it bitter), but it is not a stimulant; NICOTINE comes from tobacco.'),
    q('a substance that raises levels of physiological or nervous activity in the body',
      'stimulant', 'stimulator', 'stimulus', 'sedative',
      'STIMULANT: a substance, like caffeine. A STIMULUS is anything that causes a reaction; a SEDATIVE calms you down.'),
]

# ── 2 · ideas and situations ───────────────────────────────────────────
S2 = [
    q('a device that raises activity in a nerve, a muscle or another part of the body, for example with small electric pulses',
      'stimulator', 'stimulant', 'simulator', 'regulator',
      'STIMULATOR: a device. A STIMULANT is a substance; a SIMULATOR (no T) imitates real conditions, like a flight simulator.'),
    q('an outward form or appearance, often hiding the true nature of something',
      'guise', 'guile', 'gist', 'poise',
      'GUISE, usually in “under the guise of”. GUILE is cunning; the GIST is the main point of something.'),
    q('the great size or extent of something',
      'magnitude', 'magnificence', 'multitude', 'latitude',
      'MAGNITUDE. MAGNIFICENCE is splendour; a MULTITUDE is a large number of people or things.'),
    q('a thing said or done that serves as a signal to an actor or other performer to enter or to begin',
      'cue', 'queue', 'encore', 'curtain call',
      'CUE. QUEUE sounds the same but is a line of people waiting. An ENCORE comes at the end, when the audience asks for more.'),
    q('a loss of status or importance',
      'comedown', 'comeback', 'downturn', 'letdown',
      'COMEDOWN. A LETDOWN is a disappointment; a DOWNTURN is a fall in business or the economy.'),
    q('the most successful point; the culmination',
      'pinnacle', 'pivot', 'plateau', 'threshold',
      'PINNACLE (also a pointed turret on a roof). A PLATEAU is a long flat stage with no progress.'),
    q('a person or thing that is a perfect example of a particular quality or type',
      'epitome', 'epitaph', 'epiphany', 'episode',
      'EPITOME (four syllables: e-PIT-o-me). An EPITAPH is written on a gravestone; an EPIPHANY is a sudden realisation.'),
    q('a word or phrase that is not formal or literary, typically used in ordinary conversation',
      'colloquialism', 'colloquium', 'euphemism', 'aphorism',
      'COLLOQUIALISM. A COLLOQUIUM is an academic conference; a EUPHEMISM is a gentle word for something unpleasant.'),
    q('a language adopted as a common language between speakers whose native languages are different',
      'lingua franca', 'mother tongue', 'dialect', 'jargon',
      'LINGUA FRANCA. Your MOTHER TONGUE is your first language; JARGON is the special vocabulary of one profession.'),
    q('a unit of grammar below the sentence, which in traditional grammar has a subject and a predicate',
      'clause', 'phrase', 'paragraph', 'syllable',
      'CLAUSE. A PHRASE is a group of words with no subject-and-verb of its own: “in the hall”.'),
    q('an official connection with an organisation, such as a political party, a church or a university',
      'affiliation', 'affiliate', 'affliction', 'affection',
      'AFFILIATION: the connection. An AFFILIATE is the member group or company itself; an AFFLICTION is a cause of suffering.'),
    q('the ability to move quickly and easily',
      'agility', 'agile', 'fragility', 'frugality',
      'AGILITY, the noun. AGILE is the adjective; FRAGILITY is how easily something breaks.'),
]

# ── 3 · nouns and set phrases ──────────────────────────────────────────
S3 = [
    q('praise and honour received for an achievement',
      'kudos', 'credentials', 'karma', 'condolences',
      'KUDOS: always singular, with no “a” (“great kudos”, not “a kudo”). CONDOLENCES are sympathy when someone dies.'),
    q('a set of reasons or a logical basis for a course of action or a belief',
      'rationale', 'rationality', 'rationing', 'ratio',
      'RATIONALE (ra-tion-ALE). RATIONALITY is the quality of thinking with reason, not the reasons themselves.'),
    q('a comic play using clowning and horseplay, with crude characters and ridiculously unlikely situations',
      'farce', 'satire', 'parody', 'melodrama',
      'FARCE. SATIRE mocks people or ideas to criticise them; a PARODY imitates a particular work or style.'),
    q('the holding of an official position, or the time for which it is held',
      'tenure', 'tenancy', 'tenet', 'tenor',
      'TENURE. TENANCY is renting a home or land; a TENET is a principle or belief.'),
    q('a real or imagined wrong that gives cause for complaint, especially unfair treatment',
      'grievance', 'grief', 'vengeance', 'remorse',
      'GRIEVANCE. GRIEF is deep sadness, especially after a death; REMORSE is regret for what you did.'),
    q('belief or opinion contrary to orthodox religious doctrine',
      'heresy', 'hearsay', 'heritage', 'dogma',
      'HERESY. HEARSAY is something you heard from others but cannot prove; DOGMA is the official doctrine itself.'),
    q('a medical condition in which the blood does not clot properly, so that even a slight injury bleeds severely',
      'haemophilia', 'anaemia', 'hypothermia', 'leukaemia',
      'HAEMOPHILIA (US hemophilia). ANAEMIA is a lack of red blood cells; HYPOTHERMIA is a dangerously low body temperature.'),
    q('the full weight of a person or thing that cannot or will not move',
      'dead weight', 'dead end', 'dead heat', 'deadline',
      'DEAD WEIGHT, also used of a person who adds nothing to a team. A DEAD HEAT is a race that ends in a draw.'),
    q('a harmless or trivial lie, especially one told to avoid hurting someone’s feelings',
      'white lie', 'white elephant', 'tall story', 'half-truth',
      'WHITE LIE. A HALF-TRUTH is meant to deceive; a WHITE ELEPHANT is a costly possession nobody can use.'),
    q('a difficult or painful new undertaking or experience',
      'baptism of fire', 'rite of passage', 'leap of faith', 'labour of love',
      'BAPTISM OF FIRE: hard from the very first day. A RITE OF PASSAGE marks a change in life, and need not be painful.'),
    q('a technique for freeing oneself from anxiety and finding inner calm through meditation and the silent repetition of a mantra',
      'Transcendental Meditation', 'Progressive Muscle Relaxation', 'Guided Visualisation', 'Cognitive Behavioural Therapy',
      'TRANSCENDENTAL MEDITATION: the mantra is the clue. PROGRESSIVE MUSCLE RELAXATION tenses and relaxes the body one part at a time.'),
    q('said as an expression of relief',
      'thank God', 'God forbid', 'God knows', 'for God’s sake',
      'THANK GOD. GOD FORBID: I hope that never happens. GOD KNOWS: nobody knows. FOR GOD’S SAKE: I am annoyed.'),
]

# ── 4 · clear or confusing? ────────────────────────────────────────────
S4 = [
    q('not able to be understood; not intelligible',
      'incomprehensible', 'incompatible', 'incomparable', 'inconsequential',
      'INCOMPREHENSIBLE. INCOMPATIBLE things cannot exist or work together; INCONSEQUENTIAL means unimportant.'),
    q('able to be understood; comprehensible',
      'intelligible', 'intelligent', 'eligible', 'legible',
      'INTELLIGIBLE. LEGIBLE handwriting can be READ, which is not the same as understood; INTELLIGENT describes a mind.'),
    q('not capable of being imagined or grasped mentally; unbelievable',
      'inconceivable', 'inconclusive', 'inconsiderate', 'inconsolable',
      'INCONCEIVABLE. INCONCLUSIVE evidence proves nothing; INCONSOLABLE means too sad to be comforted.'),
    q('(of an argument, a story or a sentence) extremely complex and difficult to follow',
      'convoluted', 'contrived', 'consolidated', 'conventional',
      'CONVOLUTED. A CONTRIVED plot feels artificial and forced, but it may be perfectly easy to follow.'),
    q('brief and to the point',
      'concise', 'precise', 'cursory', 'consistent',
      'CONCISE. PRECISE means exact, however long it takes; a CURSORY look is hasty and not thorough.'),
    q('stated clearly and in detail, leaving no room for confusion or doubt',
      'explicit', 'implicit', 'exquisite', 'extensive',
      'EXPLICIT. IMPLICIT is the opposite: suggested but not said directly.'),
    q('unnecessary, especially through being more than enough',
      'superfluous', 'superficial', 'supercilious', 'superlative',
      'SUPERFLUOUS. SUPERFICIAL means only on the surface; SUPERCILIOUS means acting as if you are better than others.'),
    q('showing great attention to detail; very careful and precise',
      'meticulous', 'miraculous', 'ridiculous', 'tedious',
      'METICULOUS. Meticulous work can be TEDIOUS (boring), but the word means careful, not dull.'),
    q('(especially of a position or view) not able to be maintained or defended against attack or objection',
      'untenable', 'unattainable', 'intangible', 'unaccountable',
      'UNTENABLE. An UNATTAINABLE goal cannot be reached; something INTANGIBLE cannot be touched.'),
    q('tending to cause harm',
      'detrimental', 'determined', 'detached', 'deferential',
      'DETRIMENTAL (“detrimental to your health”). DEFERENTIAL means showing polite respect.'),
    q('tending to cause disagreement or hostility between people',
      'divisive', 'decisive', 'derisive', 'divine',
      'DIVISIVE (it divides people). DECISIVE means settling something, or deciding quickly; DERISIVE means mocking.'),
    q('happening again periodically or repeatedly',
      'recurring', 'concurring', 'incurring', 'recruiting',
      'RECURRING. CONCURRING means agreeing; INCURRING costs means bringing them on yourself.'),
]

# ── 5 · people and taste ───────────────────────────────────────────────
S5 = [
    q('held in great respect; admired',
      'esteemed', 'estranged', 'estimated', 'established',
      'ESTEEMED. An ESTABLISHED designer is known and successful, which is not the same as respected; ESTRANGED means no longer close.'),
    q('obedient or attentive to an excessive or servile degree',
      'obsequious', 'oblivious', 'obnoxious', 'ostentatious',
      'OBSEQUIOUS. OBNOXIOUS means extremely unpleasant; OSTENTATIOUS means showy, designed to impress.'),
    q('behaving in an obsequious way in order to gain an advantage',
      'sycophantic', 'sympathetic', 'symptomatic', 'sarcastic',
      'SYCOPHANTIC: flattering the powerful for your own gain. SYMPATHETIC means kind and understanding.'),
    q('given to sudden and unaccountable changes of mood or behaviour',
      'capricious', 'precocious', 'cantankerous', 'conscientious',
      'CAPRICIOUS. CANTANKEROUS people are always bad-tempered, not changeable; PRECOCIOUS children are advanced for their age.'),
    q('not aware of or not concerned about what is happening around one',
      'oblivious', 'obvious', 'obscure', 'obsequious',
      'OBLIVIOUS (“oblivious to the noise”). OBVIOUS means easy to see; OBSCURE means little known or unclear.'),
    q('(of a horse) wearing blinkers; (of a person) seeing only one narrow side of a question',
      'blinkered', 'blindfolded', 'bewildered', 'bloodshot',
      'BLINKERED. A BLINDFOLDED person sees nothing at all; BEWILDERED means completely confused.'),
    q('not willing to listen to or tolerate other people’s views; prejudiced',
      'narrow-minded', 'absent-minded', 'single-minded', 'open-minded',
      'NARROW-MINDED. SINGLE-MINDED is a compliment: completely focused on one goal. ABSENT-MINDED means forgetful.'),
    q('favouring innovation and development; progressive',
      'forward-thinking', 'free-thinking', 'forthcoming', 'far-fetched',
      'FORWARD-THINKING. A FREE-THINKING person rejects accepted beliefs; FORTHCOMING means willing to share information.'),
    q('scholarly or rarefied in taste',
      'highbrow', 'high-handed', 'highly strung', 'high-flying',
      'HIGHBROW. HIGH-HANDED means bossy, using power without thought for others; HIGHLY STRUNG means nervous.'),
    q('(of glue, paint or another substance) slightly sticky; not fully dry',
      'tacky', 'tactile', 'brittle', 'matt',
      'TACKY (it also means cheap and in bad taste). TACTILE means connected with touch; MATT paint is not shiny.'),
    q('comically or repulsively ugly or distorted',
      'grotesque', 'picturesque', 'statuesque', 'grandiose',
      'GROTESQUE. PICTURESQUE is the opposite (pretty as a picture); GRANDIOSE means too grand, showy.'),
    q('very strange or unusual, especially in a way that causes interest or amusement',
      'bizarre', 'banal', 'brazen', 'bashful',
      'BIZARRE. BANAL is the opposite: dull and ordinary. BRAZEN means shameless.'),
    q('very bold, unusual and startling',
      'outrageous', 'outdated', 'outnumbered', 'outgoing',
      'OUTRAGEOUS. OUTGOING means friendly and sociable; OUTDATED means old-fashioned.'),
]

# ── 6 · how it feels, how it goes ──────────────────────────────────────
S6 = [
    q('(of a person or their work) exceptionally good',
      'outstanding', 'upstanding', 'outgoing', 'notorious',
      'OUTSTANDING. An UPSTANDING person is honest and respectable; NOTORIOUS means famous for something bad.'),
    q('(of a bill, a task or a problem) not yet paid, done or dealt with',
      'outstanding', 'outlying', 'overstated', 'understated',
      'OUTSTANDING again, its second meaning: “two invoices are still outstanding”. OUTLYING means far from the centre.'),
    q('very happy, lively and full of energy',
      'exhilarated', 'exasperated', 'exhausted', 'exaggerated',
      'EXHILARATED. EXASPERATED is the opposite feeling: intensely annoyed.'),
    q('(informal) very enthusiastic or excited',
      'pumped', 'puffed', 'pooped', 'peeved',
      'PUMPED. PUFFED means out of breath, POOPED means exhausted, PEEVED means annoyed: all informal.'),
    q('taught to accept a set of beliefs without questioning them',
      'indoctrinated', 'inoculated', 'incorporated', 'invigorated',
      'INDOCTRINATED. INOCULATED means given a vaccine; INVIGORATED means full of new energy.'),
    q('(of project management, especially in software) working in short phases with frequent review and change of plans',
      'agile', 'waterfall', 'fragile', 'hands-on',
      'AGILE. WATERFALL is the opposite method: one long sequence of stages, each finished before the next begins.'),
    q('lacking the ability or strength to move',
      'inert', 'inept', 'alert', 'inherent',
      'INERT. INEPT means unskilled and clumsy; INHERENT means a basic, built-in part of something.'),
    q('like a farce, especially because absurd or ridiculous',
      'farcical', 'fanciful', 'forcible', 'cynical',
      'FARCICAL. FANCIFUL means imaginative or unrealistic, not ridiculous; FORCIBLE means done by force.'),
    q('at the front; in front',
      'upfront', 'upright', 'uptight', 'upbeat',
      'UPFRONT (also: paid in advance, and frank and open). UPTIGHT means tense and anxious; UPBEAT means cheerful.'),
    q('in large quantities; plentifully',
      'abundantly', 'abruptly', 'absently', 'arduously',
      'ABUNDANTLY (“abundantly clear”). ABRUPTLY means suddenly; ARDUOUSLY means with great effort.'),
    q('at the appropriate time',
      'in due course', 'in good faith', 'in short order', 'on the house',
      'IN DUE COURSE: later, when the time is right. IN SHORT ORDER means quickly, without delay.'),
    q('at the height of activity',
      'in full swing', 'in the swing of things', 'in full view', 'in two minds',
      'IN FULL SWING. You GET INTO THE SWING OF THINGS when you get used to an activity; IN TWO MINDS means undecided.'),
]

# ── 7 · actions ────────────────────────────────────────────────────────
S7 = [
    q('discuss someone or something in a way that makes them seem more interesting or attractive',
      'talk up', 'talk down', 'talk over', 'talk round',
      'TALK UP. TALK DOWN is the opposite (or to speak to someone as if they were stupid); TALK ROUND means persuade.'),
    q('behave obsequiously, especially for your own advantage',
      'suck up', 'soak up', 'chat up', 'stick up for',
      'SUCK UP (to someone), informal. SOAK UP means absorb; STICK UP FOR means defend.'),
    q('comply with rules, standards or laws',
      'conform', 'confirm', 'conflate', 'confront',
      'CONFORM (to/with). CONFIRM means say that something is true or definite; CONFRONT means face someone with a problem.'),
    q('admit that something is true or valid after first denying or resisting it',
      'concede', 'conceive', 'conceal', 'contend',
      'CONCEDE. CONTEND means the opposite here: to argue that something is true. CONCEAL means hide.'),
    q('come between so as to prevent or change a result or course of events',
      'intervene', 'convene', 'interrogate', 'intertwine',
      'INTERVENE. CONVENE means call people to a meeting; INTERTWINE means twist together.'),
    q('divide, or cause to divide, into two sharply contrasting groups or sets of opinions',
      'polarise', 'popularise', 'pulverise', 'paralyse',
      'POLARISE (US polarize). POPULARISE means make popular; PULVERISE means crush to powder.'),
    q('change smoothly from one image to another by small gradual steps, using computer animation',
      'morph', 'fade', 'pan', 'render',
      'MORPH. To RENDER is to produce the finished computer image; to FADE is to disappear gradually.'),
    q('make (a complex story or pattern) from a number of connected elements',
      'weave', 'weld', 'wield', 'warp',
      'WEAVE (wove, woven). WELD joins metal with heat; WIELD means hold and use a tool or power.'),
    q('give new and improved form, structure or appearance to; renovate',
      'revamp', 'revoke', 'revert', 'rebuff',
      'REVAMP. REVERT means go back to an earlier state; REVOKE means officially cancel.'),
    q('cause (something) to fall into disrepair or ruin',
      'dilapidate', 'dilate', 'delegate', 'dissipate',
      'DILAPIDATE, used far more as the adjective DILAPIDATED. DISSIPATE means disappear or waste.'),
    q('(of a vehicle or another physical object) begin to move more quickly',
      'accelerate', 'accumulate', 'accentuate', 'alleviate',
      'ACCELERATE. ACCENTUATE means make more noticeable; ALLEVIATE means make pain or a problem less severe.'),
    q('travel regularly between home and your place of work',
      'commute', 'commune', 'compute', 'compete',
      'COMMUTE. To COMMUNE with nature is to feel close to it.'),
    q('breathe with short, quick breaths, typically from exertion or excitement',
      'pant', 'sigh', 'snore', 'sniff',
      'PANT. A SIGH is one long, deep breath out, from sadness or relief.'),
]

# ── 8 · plans, rules and idioms ────────────────────────────────────────
S8 = [
    q('confine prisoners to their cells, especially so as to regain control',
      'lock down', 'lock out', 'crack down', 'shut down',
      'LOCK DOWN. LOCK OUT means keep someone outside; CRACK DOWN (on) means start dealing with something severely.'),
    q('plan a route or a course of action in detail',
      'map out', 'mark out', 'max out', 'phase out',
      'MAP OUT. MARK OUT means draw lines to show an area on the ground; PHASE OUT means stop something gradually.'),
    q('adopt a firm policy when faced with opposition or disobedience',
      'put your foot down', 'put your foot in it', 'put your feet up', 'put your best foot forward',
      'PUT YOUR FOOT DOWN. PUT YOUR FOOT IN IT: say something tactless. PUT YOUR FEET UP: relax.'),
    q('be so satisfied with what you have already achieved that you make no further effort',
      'rest on your laurels', 'keep your head above water', 'sit on the fence', 'take a back seat',
      'REST ON YOUR LAURELS. TAKE A BACK SEAT means choose a less active role; SIT ON THE FENCE means refuse to take sides.'),
    q('cancel or choose not to demand (a debt or a punishment)',
      'remit', 'remand', 'retract', 'reimburse',
      'REMIT (also a noun: your remit is the area you are responsible for). REIMBURSE means pay back money someone has spent.'),
    q('officially attach or connect (a group or a person) to an organisation',
      'affiliate', 'affirm', 'afflict', 'alienate',
      'AFFILIATE. AFFLICT means cause suffering; ALIENATE means make someone feel unwelcome or turn them against you.'),
    q('(of workers) treated unfairly so that someone else can profit from their work',
      'exploited', 'exhausted', 'excluded', 'exported',
      'EXPLOITED in its negative sense. Exploited workers may also be EXHAUSTED, but that only means very tired.'),
    q('make full use of and get benefit from (a resource)',
      'exploit', 'explore', 'expend', 'export',
      'EXPLOIT in its neutral sense: “to exploit the light from the south windows”. EXPLORE means travel through or investigate.'),
    q('be a perfect example of',
      'epitomise', 'emphasise', 'empathise', 'idolise',
      'EPITOMISE (US epitomize). EMPATHISE means share someone’s feelings; IDOLISE means admire too much.'),
    q('put food on (a hook, a trap or a net) to attract fish or animals',
      'bait', 'baste', 'bail', 'bathe',
      'BAIT. To BASTE meat is to pour fat over it while it cooks.'),
    q('fail to notice (something)',
      'overlook', 'oversee', 'overtake', 'overhear',
      'OVERLOOK (also: have a view over, “a room overlooking the garden”). OVERSEE means supervise.'),
    q('(of a vehicle) hit a person or an animal and knock them to the ground',
      'run down', 'run off', 'run up', 'run out',
      'RUN DOWN (also: tired and unwell, or old and in poor condition). RUN UP a bill means let it grow.'),
    q('fall in value, get worse or fail',
      'go south', 'go Dutch', 'go far', 'go public',
      'GO SOUTH, informal. GO FAR means be very successful; GO DUTCH means each person pays for themselves.'),
]

STAGES = [('e1', S1), ('e2', S2), ('e3', S3), ('e4', S4),
          ('e5', S5), ('e6', S6), ('e7', S7), ('e8', S8)]

# Plates: every Gargoyle House chapter plate, dealt in order. The cycle (37)
# is longer than any stage (13), so no plate repeats inside a stage.
CYCLE = ['p1-c%d-%d' % (c, i) for c, n in ((1, 5), (2, 4), (3, 5), (4, 4)) for i in range(n)] + \
        ['p2-c%d-%d' % (c, i) for c, n in ((1, 4), (2, 5), (3, 5), (4, 5)) for i in range(n)]

WARM = ['Which word do you use at work that a friend outside your job would not understand?',
        'How do you learn a new word so that it stays?',
        'Do you guess in a multiple-choice test, or leave it blank?',
        'Which English words look almost the same to you?',
        'Name something in your home that has been in the family a long time.',
        'Describe your ideal room in three adjectives.']

TALK2 = ['Which wrong answer almost fooled you today?',
         'Which pair do you mix up most: <strong>oversee</strong> and <strong>overlook</strong>, or <strong>divisive</strong> and <strong>decisive</strong>?',
         'Describe a building you find <strong>grotesque</strong>, and one you find <strong>picturesque</strong>.',
         'Have you ever had a <strong>baptism of fire</strong> at work?',
         'When did you last have to <strong>put your foot down</strong>?',
         'Which three words from today will you use this week?']

CHIPS = ['meticulous', 'convoluted', 'superfluous', 'untenable', 'heirloom',
         'baptism of fire', 'put your foot down', 'rest on your laurels']

PLATES = {
    'p2-hero': 'Gargoyle House plate (cover)',
    'p1-talk': 'Gargoyle House plate',
    'p2-talk': 'Gargoyle House plate',
    'p2-results': 'a restored country house glowing at dusk',
}
for _p in CYCLE:
    PLATES[_p] = 'Gargoyle House plate'

# ── chrome ─────────────────────────────────────────────────────────────
T = {
    'en': dict(
        coverTitle='The Gargoyle House <br><em>The Designer’s Lexicon</em>',
        coverSub='A hundred words from the studio, one definition at a time. Every wrong answer looks or means almost the same, so you have to know the word.',
        chipLevel='C1', chipFocus='Vocabulary · 100 words',
        eW='Warm-up', tk1T='Words at work', eT='Let’s talk', tk2T='Over to you',
        e1='1 · People and things', e2='2 · Ideas and situations', e3='3 · Nouns and set phrases',
        e4='4 · Clear or confusing?', e5='5 · People and taste', e6='6 · How it feels, how it goes',
        e7='7 · Actions', e8='8 · Plans, rules and idioms',
        sQ='Which word matches the definition?',
        actTitle='Present it in your own words', actUse='Use at least six:',
        actSpeakBrief='In pairs: one of you is a designer presenting a room to a client; the other is the client.',
        actSpeak1='Designer: present the room in one minute, using at least six words from today.',
        actSpeak2='Client: ask two questions, and push back on one idea.',
        actSpeak3='Swap roles. Then tell your partner which of their words was used best.',
        actWriteBrief='Write a short client brief (150–200 words) for a room you know well, using at least six words from today. Underline them.',
        actPlaceholder='The client wants …',
        actWriteKind='Writing', slides='slides',
    ),
    'de': dict(
        coverTitle='The Gargoyle House <br><em>The Designer’s Lexicon</em>',
        coverSub='Hundert Wörter aus dem Studio, eine Definition nach der anderen. Jede falsche Antwort sieht fast gleich aus oder bedeutet fast dasselbe: Du musst das Wort wirklich kennen.',
        chipLevel='C1', chipFocus='Wortschatz · 100 Wörter',
        eW='Zum Einstieg', tk1T='Wörter im Beruf', eT='Sprechen wir', tk2T='Jetzt du',
        e1='1 · Menschen und Dinge', e2='2 · Ideen und Situationen', e3='3 · Nomen und feste Wendungen',
        e4='4 · Klar oder verwirrend?', e5='5 · Menschen und Geschmack', e6='6 · Wie es sich anfühlt, wie es läuft',
        e7='7 · Handlungen', e8='8 · Pläne, Regeln und Redewendungen',
        sQ='Welches Wort passt zur Definition?',
        actTitle='Präsentiere es mit eigenen Worten', actUse='Verwende mindestens sechs:',
        actSpeakBrief='Zu zweit: Eine Person ist Designerin und präsentiert einen Raum, die andere ist die Kundin.',
        actSpeak1='Designerin: Stell den Raum in einer Minute vor und verwende mindestens sechs Wörter von heute.',
        actSpeak2='Kundin: Stell zwei Fragen und widersprich einer Idee.',
        actSpeak3='Tauscht die Rollen. Sagt euch dann, welches Wort die andere Person am besten verwendet hat.',
        actWriteBrief='Schreib ein kurzes Kundenbriefing (150–200 Wörter) für einen Raum, den du gut kennst, mit mindestens sechs Wörtern von heute. Unterstreiche sie.',
        actPlaceholder='The client wants …',
        actWriteKind='Schreiben', slides='Folien',
    ),
    'es': dict(
        coverTitle='The Gargoyle House <br><em>The Designer’s Lexicon</em>',
        coverSub='Cien palabras del estudio, una definición tras otra. Cada respuesta incorrecta se parece mucho en forma o en significado, así que tienes que conocer la palabra.',
        chipLevel='C1', chipFocus='Vocabulario · 100 palabras',
        eW='Para empezar', tk1T='Palabras del trabajo', eT='A conversar', tk2T='Te toca',
        e1='1 · Personas y cosas', e2='2 · Ideas y situaciones', e3='3 · Sustantivos y expresiones fijas',
        e4='4 · ¿Claro o confuso?', e5='5 · Personas y gusto', e6='6 · Cómo se siente, cómo va',
        e7='7 · Acciones', e8='8 · Planes, reglas y modismos',
        sQ='¿Qué palabra corresponde a la definición?',
        actTitle='Preséntalo con tus palabras', actUse='Usa al menos seis:',
        actSpeakBrief='En parejas: uno es diseñador y presenta una habitación a un cliente; el otro es el cliente.',
        actSpeak1='Diseñador: presenta la habitación en un minuto con al menos seis palabras de hoy.',
        actSpeak2='Cliente: haz dos preguntas y pon una objeción a una idea.',
        actSpeak3='Cambiad los papeles. Luego dile a tu compañero qué palabra usó mejor.',
        actWriteBrief='Escribe un breve encargo de cliente (150–200 palabras) para una habitación que conozcas bien, con al menos seis palabras de hoy. Subráyalas.',
        actPlaceholder='The client wants …',
        actWriteKind='Escritura', slides='diapositivas',
    ),
}

# MC slides with no plate get the mirrored hero wash; none here, but the
# Part 3 cap stays in case a slot is ever left empty.
WASH_CSS = ('html[data-style="editorial"]:not(.is-flow) .slide[data-wash][data-type="mc"] .slide-body '
            '{ max-width: 520px; }')


def build():
    items = [it for _, st in STAGES for it in st]
    assert len(items) == 100, len(items)
    keys = [it['options'][0] for it in items]
    long_ = []
    for it in items:
        assert len(set(it['options'])) == 4, it['options']
        L = sorted(len(o) for o in it['options'][1:])
        if len(it['options'][0]) - L[-1] >= 4:
            long_.append(it['options'][0])
    assert not long_, 'key is the only longest option: %s' % long_
    count = 1 + 1 + len(items) + 1 + 2
    Tn = {}
    for c in T:
        d = dict(T[c])
        d['chipCount'] = '%d %s' % (count, d.pop('slides'))
        Tn[c] = d
    flow = [('talk', 'eW', 'tk1T', WARM, 'p1-talk', 3)]
    n = 0
    for ek, st in STAGES:
        slots = [CYCLE[(n + i) % len(CYCLE)] for i in range(len(st))]
        assert len(set(slots)) == len(slots)
        n += len(st)
        flow += [('stage',), ('mc', ek, 'sQ', st, slots, None)]
    flow += [('stage',), ('talk', 'eT', 'tk2T', TALK2, 'p2-talk', 3)]
    SPEC = dict(out=OUT, title='The Gargoyle House, Part 4: The Designer’s Lexicon (C1)', folder=F, style='hs1',
                hero='p2-hero', cover_name='pop-cover-p4', plates=PLATES, flow=flow, chips=CHIPS,
                results='p2-results', title_px=54, css=WASH_CSS)
    H.check_keys(Tn)
    H.build(SPEC, Tn)
    print('keys: %d distinct of %d' % (len(set(keys)), len(keys)))


if __name__ == '__main__':
    build()
