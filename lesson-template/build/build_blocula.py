#!/usr/bin/env python3
"""Rebuild block-camp/dracula-castle-of-if.html — "Grammar Stoker's Blocula".

Blocula predates the rpg.py engine (its hotspots and glosses were the thing
that *set* the Block Camp RPG standard, `e6056ab`), so it has no `assemble()`
spec. This builder is the successor to `rebuild_blocula.py`, which did string
surgery against a `/root/work/original.html` that no longer exists anywhere.
This one is self-contained: the text lives in `blocula/scenes.json`, the
hotspot table in `HOT` below, and the page's own CSS in `STYLE`. Everything
else — the head, the SEO block, the markup, the engine — is carried over from
the file on disk, so a re-run keeps the metadata `tools/seo.py` wrote.

It replaces four regions and is idempotent; run it as often as you like:

    py lesson-template/build/build_blocula.py
    node lesson-template/check-glosses.js block-camp/dracula-castle-of-if.html
    py tools/seo.py                                    # always last

What this revision (the V7 draft, 2026-09-07) changed:

1. **Five new scenes**, and the continuity edits that make them land. The
   draft is a narrative revision, not just an append: `dinner` now hands over
   a ring of brass guest keys, which is why `locked_room` fails and why the
   iron west-door key matters; both act-two routes converge on the new
   `servant_stair`; `choice3` now happens halfway down the sheet-rope, which
   is what gives the crypt and courtyard branches somewhere to come back to.
   Twenty existing strings were rewritten for that; each was re-glossed in
   all nine non-source languages rather than left behind in English.

       vampire_brides → fallen_key → servant_stair → shipping_plan
       stolen_key ----------------→ servant_stair → shipping_plan
       earth_boxes → box_moved → stolen_clothes
       stake_decision → crypt_chase → final_escape → resolve
       carriage_sabotage → courtyard_escape → resolve

   The courtyard branch now ends on its own question instead of borrowing
   the rope scene, so both routes still run to seventeen questions and the
   85-point total is unchanged.

2. **The panel is glass, not a black box.** The old layout stacked opaque
   plates — a near-solid panel, and inside it another plate per option, per
   route card, per rule card, per feedback line. Everything below the panel
   now sits directly on its glass: options and routes are translucent with a
   hairline, the feedback and rule notes are an accent rule and no fill at
   all. The panel itself lost its border and gained a corner radius and a
   real blur. All of it is mixed from the existing palette tokens, so the
   colours are still the ones the hero gave us.

3. **The three route-choice scenes are centred**, as the RPG standard has
   it — choice1 and choice2 were still pinned to a corner.

4. **A shipped translation defect**, found by `check-glosses.js`: the Russian
   glosses for two of the `wolves` options were byte-identical, so a Russian
   reader was picking between two identical lines. Russian carries the
   came/had-come contrast on aspect; it now does.
"""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PAGE = os.path.join(ROOT, 'block-camp', 'dracula-castle-of-if.html')
DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'blocula', 'scenes.json')
IMG_DIR = 'dracula-castle-of-if'

LANGS = ['en', 'es', 'de', 'fr', 'it', 'pt', 'pl', 'zh', 'ja', 'tr', 'ar', 'ru']

# --------------------------------------------------------------- hotspots
# [x%, y%, w%, h%] of the 1536x1024 picture — the story object the marker
# sits on — then the panel side (left|right|center), its vertical anchor,
# and optionally a panel width % and an inset %.
HOT = {
 # Every marker sits on the object the text actually talks about, read off a
 # gridded contact sheet (rpg/README.md §3). The comment names the object; if
 # you move a picture, re-cut the sheet and re-read it rather than nudging by
 # feel. Order: centre x%, centre y%, w%, h% of the 1536x1024 picture, then
 # the panel side, its vertical anchor, and optionally panel width % + inset.
 'cover':            (75, 35,  7, 15, 'left',   'center'),        # Dracula in the lit archway
 'rules':            (60, 74, 20, 18, 'left',   'center', 58),    # the open journal
 'train':            (67, 54,  8, 11, 'left',   'center'),        # the letter in his hands
 'inn':              (25, 48,  6, 10, 'right',  'center'),        # the crucifix she holds out
 'coach':            (76, 30,  8, 12, 'left',   'top', 36),       # the coachman's red eyes
 'blue_fire':        (75, 66, 12, 18, 'left',   'top'),           # the blue flame itself
 'choice1':          (82, 49,  7, 11, 'center', 'top'),           # the blue fire at the fork
 'blue_treasure':    (80, 74, 13, 14, 'left',   'top', 34),       # the iron chest
 'blue_cross':       (30, 38,  7, 11, 'right',  'center'),        # the crucifix
 'wolves':           (83, 34,  9, 18, 'left',   'center'),        # the coachman's raised hand
 'coach_rescue':     (68, 42,  9, 20, 'left',   'top', 32),       # the coachman, hand raised
 'castle_gate':      (72, 58,  7, 15, 'left',   'top', 38),       # the gate, lit from within
 'dinner':           (84, 60, 12, 18, 'left',   'center'),        # the fireplace
 'mirror':           (54, 33, 11, 20, 'left',   'center', 34),    # the mirror he holds up
 'locked_room':      (38, 72,  7, 11, 'right',  'center'),        # the ring of guest keys
 'choice2':          (80, 22,  9, 15, 'center', 'top'),           # the moonlit tower window
 'forged_letters':   (43, 72, 24, 15, 'left',   'top'),           # the letters on the desk
 'stolen_key':       (33, 35,  7, 12, 'right',  'bottom'),        # the iron key on the coat
 'wall_crawl':       (77, 56, 14, 56, 'left',   'top', 38, 14),   # Dracula down the wall
 'vampire_brides':   (40, 27, 10, 17, 'right',  'top'),           # Dracula in the doorway
 'fallen_key':       (48, 74,  8, 10, 'right',  'center'),        # the iron key in his hand
 'servant_stair':    (85, 53,  6,  9, 'left',   'center'),        # the key turning in the lock
 'shipping_plan':    (46, 72, 22, 15, 'left',   'center'),        # the shipping ledger
 'earth_boxes':      (72, 42,  9, 11, 'left',   'center'),        # the open earth box
 'box_moved':        (56, 53, 15,  9, 'left',   'top', 34),       # the sealed coffin
 'stolen_clothes':   (86, 52,  7, 18, 'left',   'center'),        # the bloodied cuff
 'last_chance':      (33, 42, 10, 22, 'right',  'center'),        # the cliff window
 'escape_plan':      (66, 55,  6, 34, 'left',   'bottom'),        # the sheet-rope
 'choice3':          (15, 45, 15, 32, 'center', 'top'),           # the broken chapel window
 'crypt_tomb':       (72, 55, 16, 14, 'left',   'top'),           # the stone sarcophagus
 'stake_decision':   (75, 63, 12, 13, 'left',   'center'),        # the open coffin
 'crypt_chase':      (17, 22, 10, 14, 'right',  'bottom', 38),    # the dawn through the cracked window
 'courtyard_carts':  (75, 60, 14, 14, 'left',   'bottom', 38),    # the loaded wagon
 'carriage_sabotage':(48, 62, 15, 22, 'left',   'top', 32),       # the wheel and its pin
 'courtyard_escape': (77, 73, 16, 22, 'left',   'top'),           # the broken wheel
 'final_escape':     (87, 14,  9, 13, 'left',   'center'),        # Dracula at the parapet
 'success':          (18, 52, 10, 13, 'right',  'top'),           # the sun reaching the valley
 'failure':          (56, 70, 12, 32, 'left',   'top'),           # Dracula at the closed gate
 'epilogue':         (75, 60, 18, 18, 'left',   'center'),        # the earth boxes on deck
}

# Scenes whose marked object is a blue flame rather than a warm light. The
# marker takes the flame's colour there, so it reads as the fire itself and
# not as a gold pin dropped on top of one.
COOL = ('blue_fire', 'choice1', 'blue_treasure')

# ------------------------------------------------------------------ style
# One string, replacing everything between `:root{` and `</style>`. The
# translucent shapes are mixed from the palette tokens rather than written as
# raw black — house rule, and it keeps the glass tied to the hero's colours.
STYLE = """:root{--blood:#d21f3c;--deep:#16040a;--bone:#f5ead7;--ice:#a7ddf2;--gold:#f0c878;--muted:#c8b9ad;--shadow:#3c1a66;--ink:#0d0509;
  --veil:color-mix(in srgb,var(--ink) 34%,transparent);
  --veil-lift:color-mix(in srgb,var(--ink) 20%,transparent);
  --veil-deep:color-mix(in srgb,var(--ink) 72%,transparent);
  /* Legibility comes from this halo, not from an opaque plate: every text
     node carries it, so the veil can drop to a third and the picture still
     reads through the panel. */
  --halo:0 1px 2px var(--ink),0 0 .5em var(--ink),0 0 1.1em var(--ink);
  --hair:color-mix(in srgb,var(--bone) 17%,transparent);
  --hair-lit:color-mix(in srgb,var(--bone) 44%,transparent);
  --tint:color-mix(in srgb,var(--blood) 20%,transparent);
  --tint-lit:color-mix(in srgb,var(--blood) 52%,transparent);
  --cast:color-mix(in srgb,var(--deep) 58%,transparent);
  --good:#77efb4;--bad:#ff6f82;--r:.85cqw;
  /* The marker glow. It defaults to the lesson's gold, but a scene whose
     object is itself a light takes that light's colour — the blue fire
     scenes glow blue, so the marker reads as the flame and not as a
     gold pin dropped on top of one. */
  --glow:#f0c878;--glow-core:#fff0be;--glow-sheen:#fffae1}
*{box-sizing:border-box} html,body{width:100%;height:100%;margin:0;overflow:hidden;background:#050306;color:var(--bone);font-family:"Courier New",Courier,monospace}
button{font:inherit}.game{position:fixed;inset:0;background:#050306}.frame{position:absolute;inset:0;overflow:hidden;container-type:inline-size}
.scene-img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;filter:saturate(1.04) contrast(1.03)}
.hud{position:absolute;z-index:5;top:1.4cqw;left:1.5cqw;right:1.5cqw;display:flex;align-items:center;justify-content:space-between;gap:1cqw;pointer-events:none}
.hud-group{display:flex;gap:.55cqw;align-items:center;flex-wrap:wrap}.badge{background:var(--veil);border:1px solid var(--hair);border-radius:999px;box-shadow:0 .3cqw 1.1cqw var(--cast);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);padding:.46cqw .86cqw;font-size:1.05cqw;letter-spacing:.04em;white-space:nowrap}.badge b{color:var(--gold)}
.langs{display:flex;gap:.35cqw;pointer-events:auto}.lang-btn,.utility{border:1px solid var(--hair);border-radius:999px;color:var(--bone);background:var(--veil);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);padding:.46cqw .82cqw;cursor:pointer;font-size:1cqw}.lang-btn.active{color:#fff;background:var(--blood);border-color:#ff7186}.utility:hover,.lang-btn:hover{border-color:var(--hair-lit)}
.zone{position:absolute;z-index:4;top:8%;bottom:3.5%;left:2.2%;right:2.2%;display:flex;pointer-events:none}
.content{--u:calc(1cqw * var(--fit,1));font-size:var(--u);pointer-events:auto;display:flex;flex-direction:column;gap:calc(.8*var(--u));width:42%;max-height:100%;overflow:hidden;padding:calc(1.35*var(--u)) calc(1.5*var(--u));background:var(--veil);border:0;border-radius:var(--r);box-shadow:0 calc(1.2*var(--u)) calc(3.6*var(--u)) var(--cast);backdrop-filter:blur(26px) saturate(1.06) brightness(.62);-webkit-backdrop-filter:blur(26px) saturate(1.06) brightness(.62);text-shadow:var(--halo);transition:transform .38s cubic-bezier(.2,.9,.3,1.15),opacity .22s ease;transform-origin:50% 50%}
.frame:not(.open) .content{opacity:0;transform:scale(.12);pointer-events:none;transition:transform .26s ease-in,opacity .18s ease-in}
.left .zone{justify-content:flex-start}.left .content{text-align:left}.right .zone{justify-content:flex-end}.right .content{text-align:right}.center .zone{justify-content:center}.center .content{width:62%;text-align:center}
.v-top .zone{align-items:flex-start}.v-center .zone{align-items:center}.v-bottom .zone{align-items:flex-end}
.hide-btn{align-self:flex-end;order:-1;margin:calc(-.5*var(--u)) calc(-.6*var(--u)) calc(-.3*var(--u)) 0;border:0;background:none;color:var(--muted);font-size:calc(.82*var(--u));letter-spacing:.08em;cursor:pointer;padding:calc(.25*var(--u)) calc(.4*var(--u))}.hide-btn:hover{color:var(--bone)}.left .hide-btn,.center .hide-btn{align-self:flex-end}.right .hide-btn{align-self:flex-start}
.hot{position:absolute;z-index:6;left:50%;top:50%;width:10%;height:14%;transform:translate(-50%,-50%);border:0;background:none;padding:0;cursor:pointer;transition:opacity .25s;min-width:3.6cqw;min-height:3.6cqw}
.hot i{position:absolute;inset:-.4cqw;border-radius:38%;background:linear-gradient(115deg,transparent 28%,color-mix(in srgb,var(--glow-core) 28%,transparent) 42%,color-mix(in srgb,var(--glow-sheen) 62%,transparent) 50%,color-mix(in srgb,var(--glow-core) 28%,transparent) 58%,transparent 72%);background-size:260% 260%;mix-blend-mode:screen;box-shadow:0 0 0 .14cqw color-mix(in srgb,var(--glow) 90%,transparent),0 0 1.4cqw .25cqw color-mix(in srgb,var(--glow) 55%,transparent),inset 0 0 1.4cqw color-mix(in srgb,var(--glow-core) 35%,transparent);animation:shimmer 2.2s linear infinite,pulse 1.8s ease-in-out infinite}
.hot::before{content:"";position:absolute;inset:-.4cqw;border-radius:38%;border:.16cqw solid color-mix(in srgb,var(--glow-core) 90%,transparent);opacity:0;animation:ring 1.8s ease-out infinite}
.hot:hover i{animation-duration:1s,1.8s;box-shadow:0 0 0 .18cqw var(--glow-core),0 0 2.2cqw .5cqw color-mix(in srgb,var(--glow) 85%,transparent),inset 0 0 1.8cqw color-mix(in srgb,var(--glow-core) 50%,transparent)}
/* A scene whose object is a blue flame: the marker takes the flame's
   colour, and its label with it. */
.hot.cool{--glow:#5fc9f8;--glow-core:#cdeeff;--glow-sheen:#eafaff}
.hot.cool .hot-label{color:var(--ice)}
.hot-label{position:absolute;left:50%;top:calc(100% + .7cqw);transform:translateX(-50%);white-space:nowrap;color:var(--glow);font-family:'Pixelify Sans','Courier New',monospace;font-size:1.15cqw;letter-spacing:.04em;text-shadow:-.09em -.09em 0 var(--deep),0 -.09em 0 var(--deep),.09em -.09em 0 var(--deep),-.09em 0 0 var(--deep),.09em 0 0 var(--deep),-.09em .09em 0 var(--deep),0 .09em 0 var(--deep),.09em .09em 0 var(--deep),0 .14em .5em rgba(5,3,7,.9);pointer-events:none}
.hot.above .hot-label{top:auto;bottom:calc(100% + .7cqw)}
.langs{position:relative}.lang-btn{display:flex;align-items:center;gap:.3cqw;white-space:nowrap}.lang-btn b{color:var(--gold)}
.lang-menu[hidden]{display:none}.lang-menu{position:absolute;right:0;top:calc(100% + .4cqw);z-index:20;display:grid;grid-template-columns:1fr 1fr;gap:.25cqw;min-width:22cqw;padding:.5cqw;background:var(--veil-deep);border:1px solid var(--hair);border-radius:var(--r);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);box-shadow:0 1cqw 3cqw var(--cast)}
.lang-item{display:grid;grid-template-columns:2.6cqw 1fr;align-items:center;gap:.4cqw;border:1px solid transparent;border-radius:calc(var(--r) * .6);background:none;color:var(--bone);padding:.4cqw .5cqw;text-align:left;cursor:pointer;font-size:1cqw}.lang-item b{color:var(--gold);font-size:.9cqw}.lang-item span{font-size:.95cqw}.lang-item:hover{border-color:var(--hair);background:var(--tint)}.lang-item.active{background:var(--blood);color:#fff}.lang-item.active b{color:#fff}
.utility.fs{display:flex;align-items:center;gap:.35cqw;color:#1a0810;background:linear-gradient(180deg,#f7d98c,#d9a94a);border:1px solid #fff0c0;font-weight:700;letter-spacing:.06em;box-shadow:0 0 1cqw rgba(240,200,120,.55);animation:fsglow 2.4s ease-in-out infinite}.utility.fs:hover{filter:brightness(1.1)}
.translation{unicode-bidi:plaintext}.rtl .translation{direction:rtl;text-align:right}.utility{pointer-events:auto}
.frame.open .hot{opacity:0;pointer-events:none}
.tr-on .content{gap:calc(.55*var(--u));padding:calc(1.05*var(--u)) calc(1.25*var(--u))}.tr-on .translation{font-size:calc(.86*var(--u));line-height:1.22;margin-top:calc(.12*var(--u))}.tr-on .option{padding:calc(.44*var(--u)) calc(.7*var(--u))}.tr-on .options{gap:calc(.36*var(--u))}.tr-on .clue{padding:calc(.45*var(--u)) calc(.8*var(--u))}.tr-on .feedback{padding:calc(.5*var(--u)) calc(.8*var(--u))}.tr-on .story{font-size:calc(1.25*var(--u));line-height:1.28}.rules-intro{grid-template-columns:1fr 1fr}.rule-card:last-child{grid-column:1/-1}.tr-on .rules-intro{gap:calc(.32*var(--u))}.tr-on .rule-card{padding:calc(.36*var(--u)) calc(.55*var(--u));font-size:calc(.88*var(--u))}.tr-on .rule-card .translation{font-size:calc(.7*var(--u))}.tr-on .rule-note{font-size:calc(.88*var(--u))}.tr-on .title{font-size:calc(3*var(--u))}
@keyframes shimmer{0%{background-position:110% 110%}100%{background-position:-10% -10%}}
@keyframes pulse{0%,100%{opacity:.8}50%{opacity:1}}
@keyframes ring{0%{transform:scale(1);opacity:.9}100%{transform:scale(1.5);opacity:0}}
@keyframes fsglow{0%,100%{box-shadow:0 0 .6cqw rgba(240,200,120,.4)}50%{box-shadow:0 0 1.6cqw rgba(240,200,120,.9)}}
.kicker{color:#ff8ea0;font-weight:700;font-size:calc(1.15*var(--u));letter-spacing:.14em;text-transform:uppercase}.title{margin:0;color:var(--gold);font-family:'Pixelify Sans','Courier New',monospace;font-size:calc(3.6*var(--u));line-height:1.08;letter-spacing:0;text-shadow:-.05em 0 0 var(--shadow),.05em 0 0 var(--shadow),0 -.05em 0 var(--shadow),0 .05em 0 var(--shadow),-.05em -.05em 0 var(--shadow),.05em -.05em 0 var(--shadow),-.05em .05em 0 var(--shadow),.05em .05em 0 var(--shadow),0 0 .6em rgba(60,26,102,.75)}.story{font-size:calc(1.36*var(--u));line-height:1.34;font-weight:700}
.clue{border-left:calc(.24*var(--u)) solid var(--blood);padding:calc(.6*var(--u)) calc(.9*var(--u));background:var(--tint);border-radius:0 calc(var(--r) * .6) calc(var(--r) * .6) 0;font-size:calc(1.13*var(--u));line-height:1.28}.right .clue{border-left:0;border-right:calc(.24*var(--u)) solid var(--blood);border-radius:calc(var(--r) * .6) 0 0 calc(var(--r) * .6)}.center .clue{border-right:calc(.24*var(--u)) solid var(--blood);border-radius:calc(var(--r) * .6)}
.prompt{color:var(--ice);font-weight:700;font-size:calc(1.35*var(--u));line-height:1.24}.translation{display:block;color:#e5d3c6;font-size:calc(.92*var(--u));line-height:1.28;margin-top:calc(.2*var(--u));font-style:italic}.title .translation{font-size:calc(1.05*var(--u));letter-spacing:0;color:#f0d8dd;margin-top:calc(.4*var(--u));font-family:"Courier New",Courier,monospace}.kicker .translation{font-size:calc(.78*var(--u));letter-spacing:.05em;color:#e5d3c6}
.options{display:grid;gap:calc(.5*var(--u));margin-top:calc(.15*var(--u))}.option{display:grid;grid-template-columns:calc(2.2*var(--u)) 1fr;align-items:center;gap:calc(.6*var(--u));width:100%;border:1px solid var(--hair);border-radius:calc(var(--r) * .7);background:var(--veil-lift);color:var(--bone);padding:calc(.62*var(--u)) calc(.8*var(--u));text-align:left;cursor:pointer;font-size:calc(1.04*var(--u));line-height:1.22;transition:.16s}.option:hover{transform:translateY(-1px);border-color:var(--hair-lit);background:var(--tint)}.option .key{display:grid;place-items:center;width:calc(2*var(--u));height:calc(2*var(--u));border:1px solid var(--hair-lit);border-radius:calc(var(--r) * .45);color:var(--bone);font-weight:700}.option.correct{background:color-mix(in srgb,var(--good) 26%,transparent);border-color:var(--good)}.option.correct .key{border-color:var(--good)}.option.wrong{background:var(--tint-lit);border-color:var(--bad)}.option.wrong .key{border-color:var(--bad)}.option:disabled{cursor:default;transform:none}.option .translation{font-size:calc(.82*var(--u))}
.feedback{display:none;padding:calc(.6*var(--u)) 0 calc(.6*var(--u)) calc(.9*var(--u));border:0;border-left:calc(.24*var(--u)) solid var(--hair-lit);background:none;font-size:calc(1.04*var(--u));line-height:1.28}.feedback.show{display:block}.feedback.good{border-left-color:var(--good)}.feedback.bad{border-left-color:var(--bad)}.feedback strong{color:var(--gold)}.right .feedback{border-left:0;border-right:calc(.24*var(--u)) solid var(--hair-lit);padding:calc(.6*var(--u)) calc(.9*var(--u)) calc(.6*var(--u)) 0}.right .feedback.good{border-right-color:var(--good)}.right .feedback.bad{border-right-color:var(--bad)}.center .feedback{border:0;border-top:calc(.16*var(--u)) solid var(--hair-lit);padding:calc(.7*var(--u)) 0 0}.center .feedback.good{border-top-color:var(--good)}.center .feedback.bad{border-top-color:var(--bad)}
.continue,.start,.restart{align-self:flex-start;border:1px solid #ff8196;border-radius:999px;background:linear-gradient(180deg,#a7102b,#6e071a);color:#fff;font-weight:700;letter-spacing:.07em;padding:calc(.7*var(--u)) calc(1.3*var(--u));cursor:pointer;font-size:calc(1.03*var(--u));box-shadow:0 calc(.5*var(--u)) calc(1.5*var(--u)) var(--cast)}.right .continue,.right .start,.right .restart{align-self:flex-end}.center .continue,.center .start,.center .restart{align-self:center}.continue:hover,.start:hover,.restart:hover{filter:brightness(1.2)}
.route-options{display:grid;grid-template-columns:1fr 1fr;gap:calc(.7*var(--u))}.route{border:1px solid var(--hair);border-radius:calc(var(--r) * .7);background:var(--veil-lift);color:var(--bone);padding:calc(1*var(--u));cursor:pointer;text-align:left;min-height:calc(6.8*var(--u));transition:.16s}.route:hover{border-color:#ff8196;background:var(--tint)}.route b{display:block;color:#ff8ea0;font-size:calc(1.12*var(--u));margin-bottom:calc(.35*var(--u))}.route .translation{font-size:calc(.8*var(--u))}
.rules-intro{display:grid;gap:calc(.5*var(--u))}.rule-card{border:0;border-left:calc(.18*var(--u)) solid var(--hair-lit);border-radius:0;background:none;padding:calc(.2*var(--u)) calc(.7*var(--u));font-size:calc(.94*var(--u));line-height:1.22}.rule-card b{display:block;color:var(--gold);font-size:calc(1.02*var(--u));margin-bottom:calc(.12*var(--u))}.rule-card .translation{font-size:calc(.75*var(--u))}.rule-note{color:var(--ice);font-size:calc(.94*var(--u));line-height:1.25;border-left:calc(.24*var(--u)) solid var(--blood);background:none;padding:calc(.3*var(--u)) calc(.8*var(--u))}.right .rule-card,.right .rule-note{border-left:0;border-right:calc(.18*var(--u)) solid var(--hair-lit)}.right .rule-note{border-right-width:calc(.24*var(--u));border-right-color:var(--blood)}.center .rule-card,.center .rule-note{border:0;padding:calc(.2*var(--u))}
.cover-title{font-size:calc(3.2*var(--u));line-height:1}.cover-title .pre{display:block;font-size:1em;letter-spacing:.04em;color:var(--bone);margin-bottom:.25em}.cover-title .big{display:block;font-size:2.5em;line-height:.92;color:var(--gold)}.final-score{font-size:calc(2*var(--u));color:var(--gold);font-weight:700}.small{font-size:calc(.86*var(--u));color:var(--muted)}
.corner-help{position:absolute;z-index:5;right:1.5cqw;bottom:1.2cqw;color:var(--muted);font-size:.78cqw;background:none;padding:.35cqw .5cqw;text-shadow:0 .1em .5em var(--ink),0 0 .3em var(--ink);pointer-events:none}
@media(max-aspect-ratio:4/3){.content{width:58%}.center .content{width:82%}.hot-label{font-size:1.6cqw}.lang-menu{min-width:30cqw}.lang-item{font-size:1.3cqw}.lang-item b{font-size:1.2cqw}.title{font-size:calc(4.4*var(--u))}.story,.prompt{font-size:calc(1.75*var(--u))}.option,.feedback{font-size:calc(1.4*var(--u))}.translation{font-size:calc(1.15*var(--u))}.badge{font-size:1.35cqw}.lang-btn,.utility{font-size:1.28cqw}}
@media(max-width:calc(700*var(--u))){.hud{top:8px;left:8px;right:8px}.badge{font-size:calc(10*var(--u));padding:calc(5*var(--u)) calc(9*var(--u))}.lang-btn,.utility{font-size:calc(10*var(--u));padding:calc(5*var(--u)) calc(9*var(--u))}.zone{top:calc(58*var(--u));bottom:calc(10*var(--u));left:3%;right:3%;align-items:flex-end!important;justify-content:center!important}.content,.center .content,.tr-on .content{--u:calc(calc(1*var(--u)) * var(--fit,1));width:100%!important;margin:0!important;max-height:100%;text-align:left;padding:calc(14*var(--u));gap:calc(9*var(--u));border-radius:calc(12*var(--u))}.hot{min-width:44px;min-height:44px}.hot i,.hot::before{inset:-4px}.hot i{box-shadow:0 0 0 2px rgba(240,200,120,.9),0 0 14px 3px rgba(240,200,120,.55)}.hot::before{border-width:2px}.hot-label{font-size:calc(12*var(--u))}.lang-menu{min-width:calc(220*var(--u));padding:calc(6*var(--u));gap:calc(3*var(--u));grid-template-columns:1fr}.lang-item{font-size:calc(12*var(--u));padding:calc(5*var(--u)) calc(7*var(--u));grid-template-columns:calc(30*var(--u)) 1fr}.lang-item b,.lang-item span{font-size:12px}.lang-btn{gap:4px}.hide-btn{font-size:calc(11*var(--u))}.title.cover-title{font-size:calc(19*var(--u))}.clue,.route,.rules-intro{font-size:calc(13*var(--u));padding:calc(8*var(--u)) calc(10*var(--u))}.rule-card,.rule-note{font-size:calc(13*var(--u));padding:calc(2*var(--u)) calc(9*var(--u))}.rule-card b,.route b{font-size:calc(13*var(--u))}.final-score{font-size:calc(18*var(--u))}.small{font-size:calc(11*var(--u))}.continue,.start,.restart{font-size:calc(13*var(--u));padding:calc(10*var(--u)) calc(18*var(--u))}.option{grid-template-columns:calc(22*var(--u)) 1fr}.option .key{width:calc(20*var(--u));height:calc(20*var(--u))}.option .translation,.route .translation,.rule-card .translation{font-size:calc(11*var(--u))}.rules-intro{grid-template-columns:1fr}.rule-card:last-child{grid-column:auto}.center .rule-card,.center .rule-note,.right .rule-card,.right .rule-note{border-left:.18cqw solid var(--hair-lit);border-right:0;padding:calc(2*var(--u)) calc(9*var(--u))}.title{font-size:calc(36*var(--u))}.kicker{font-size:calc(12*var(--u))}.story,.prompt{font-size:calc(15*var(--u))}.translation{font-size:calc(12*var(--u))}.option,.feedback{font-size:calc(13*var(--u));padding:calc(8*var(--u)) calc(10*var(--u))}.center .feedback,.right .feedback{border:0;border-left:.24cqw solid var(--hair-lit);padding:calc(8*var(--u)) calc(10*var(--u))}.route-options{grid-template-columns:1fr}.corner-help{display:none}}"""


# ------------------------------------------------------------ serialising
def jsq(s):
    """A JS single-quoted string literal."""
    return "'" + s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n') + "'"


def emit(node):
    """Render one scene value: a T() call for a gloss dict, JSON otherwise."""
    if isinstance(node, dict):
        if 'en' in node and isinstance(node['en'], str):
            return 'T(' + ','.join(jsq(node[l]) for l in LANGS) + ')'
        return '{' + ','.join(k + ':' + emit(v) for k, v in node.items()) + '}'
    if isinstance(node, list):
        return '[' + ','.join(emit(v) for v in node) + ']'
    if isinstance(node, str):
        return jsq(node)
    if isinstance(node, bool):
        return 'true' if node else 'false'
    return json.dumps(node)


def build():
    scenes = json.load(open(DATA, encoding='utf-8'))
    page = open(PAGE, encoding='utf-8').read()

    # every scene must have a hotspot, and every `next`/`target` must resolve
    for sid, sc in scenes.items():
        assert sid in HOT, 'no hotspot for scene ' + sid
        for tgt in ([sc['next']] if sc.get('next') else []) + \
                   [r['target'] for r in sc.get('routes', [])]:
            assert tgt in scenes or tgt == 'resolve', f'{sid} -> {tgt} does not resolve'
    for sid in HOT:
        assert sid in scenes, 'hotspot for a scene that is gone: ' + sid
    for l in LANGS:
        pass

    imgs = {sc['img']: f"{IMG_DIR}/{sc['img']}.webp" for sc in scenes.values()}
    for name, rel in imgs.items():
        p = os.path.join(ROOT, 'block-camp', rel)
        assert os.path.exists(p), 'missing picture: ' + rel

    # ---- 1. the stylesheet, between `:root{` and `</style>`
    a = page.index(':root{')
    b = page.index('</style>', a)
    page = page[:a] + STYLE + '\n' + page[b:]

    # ---- 2. IMAGES
    page = re.sub(r'const IMAGES = \{.*?\};',
                  'const IMAGES = ' + json.dumps(imgs, ensure_ascii=False) + ';',
                  page, count=1, flags=re.S)

    # ---- 3. scenes
    body = '\n'.join(k + ':' + emit(v) + ',' for k, v in scenes.items())
    body = 'const scenes={\n' + body.rstrip(',') + '\n};'
    a = page.index('const scenes={')
    b = page.index('\nconst HOT=', a)
    page = page[:a] + body + page[b:]

    # ---- 4. HOT, and the scenes whose marker glows blue
    hot = {k: list(v) for k, v in HOT.items()}
    page = re.sub(r'const HOT=\{.*?\};',
                  'const HOT=' + json.dumps(hot, ensure_ascii=False) + ';'
                  + 'const COOL=' + json.dumps(list(COOL)) + ';',
                  page, count=1, flags=re.S)
    page = re.sub(r'const COOL=\[[^\]]*\];(const COOL=\[[^\]]*\];)+',
                  lambda m: m.group(0)[:m.group(0).index('];') + 2], page, flags=re.S)
    if "hot.classList.toggle('cool'" not in page:
        page = page.replace('function placeHot(h){',
                            "function placeHot(h){hot.classList.toggle('cool',COOL.includes(state.scene));", 1)
    assert "hot.classList.toggle('cool'" in page, 'the blue-marker class was not wired in'

    # ---- 5. fit the panel to the frame. The panel must never scroll, so
    # after anything that changes its content — a new scene, a revealed
    # answer, a language switch, a resize — step the text unit down until it
    # fits. --u drives every size inside .content, so one number scales the
    # lot without the glosses compounding (they are nested inside .story and
    # .option, which is why this is a custom property and not `em`).
    fit = ("function fitPanel(){content.style.setProperty('--fit',1);"
           "if(!frame.classList.contains('open'))return;"
           "let f=1;let guard=0;"
           "while(content.scrollHeight>content.clientHeight+1&&f>0.5&&guard++<40){"
           "f-=0.025;content.style.setProperty('--fit',f)}}\n")
    # These are insertions rather than region rewrites, so they are guarded:
    # without this a re-run appends a second copy of fitPanel and a second
    # fitPanel() call, and the build stops being idempotent.
    if 'function fitPanel(' not in page:
        page = page.replace('\nfunction render(){', '\n' + fit + 'function render(){', 1)
        # every path that changes what is in the panel ends by re-fitting
        page = page.replace("content.innerHTML=html;updateHUD();",
                            "content.innerHTML=html;updateHUD();fitPanel();", 1)
        # The panel is measured only once it is actually open, so the fit has
        # to run after setOpen adds the class — render() calls setOpen *after*
        # filling the panel, so wiring render() alone would always measure a
        # closed, zero-height panel.
        page = page.replace("frame.classList.toggle('open',state.open)}",
                            "frame.classList.toggle('open',state.open);if(state.open)fitPanel()}", 1)
    # A resize changes 1cqw, and the text reflows, so the fit is recomputed.
    if "addEventListener('resize',fitPanel)" not in page:
        page = page.replace("hot.addEventListener('click'",
                            "addEventListener('resize',fitPanel);" + chr(10)
                            + "hot.addEventListener('click'", 1)
    for hook, where in [("content.innerHTML=html;updateHUD();fitPanel();", 'render'),
                        ("if(state.open)fitPanel()}", 'setOpen'),
                        ("addEventListener('resize',fitPanel)", 'resize')]:
        assert hook in page, 'fitPanel was not wired into ' + where

    # ---- 6. scroll CONTINUE into view once a question is answered.
    # An answered question is the one panel that can outgrow the frame — the
    # feedback line and the button appear below three options that were
    # already filling it. The panel scrolls, but nothing was scrolling it, so
    # the button simply sat below the fold with no affordance: 39px under on
    # courtyard_escape and vampire_brides, 55 on locked_room, 138 on
    # crypt_tomb. Measured with scrollHeight - clientHeight on each.
    # scrollIntoView does nothing here — .content is a transformed, animated
    # flex container and the browser resolves `block:'nearest'` to no scroll.
    # Setting scrollTop on the panel itself does work, and the bottom is where
    # the feedback and the button both are.
    # Rewritten from the `updateHUD()` call to the end of displayAnswer, so a
    # re-run replaces whatever tail is already there rather than only the
    # original one.
    # Anchored on the line that reveals the feedback — everything after it to
    # the end of displayAnswer is ours, so a re-run replaces whatever tail is
    # already in the file rather than only the original one.
    anchor = "fb.className=`feedback show ${ok?'good':'bad'}`;"
    tail = (anchor + "document.getElementById('continue').hidden=false;updateHUD();"
            "requestAnimationFrame(fitPanel)}"
            "\nfunction answer")
    page, n = re.subn(re.escape(anchor) + r".*?\}\nfunction answer",
                      lambda m: tail, page, count=1, flags=re.S)
    assert n == 1, 'displayAnswer no longer ends the way the CONTINUE scroll patch expects'

    open(PAGE, 'w', encoding='utf-8', newline='\n').write(page)
    nq = sum(1 for s in scenes.values() if s.get('kind') == 'question')
    print(f'wrote {os.path.relpath(PAGE, ROOT)} — {len(scenes)} scenes, '
          f'{nq} question scenes, {len(LANGS)} languages, {len(imgs)} pictures')


if __name__ == '__main__':
    build()
