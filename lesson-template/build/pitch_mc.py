# -*- coding: utf-8 -*-
"""The seven multiple-choice items for The Design Pitch, rebalanced.

Five of the seven keys were the longest option on their slide, and on a lesson
about persuasive language that is close to fatal: the whole point is that the
better phrasing is the more considered one, so "pick the longest" scores five
out of seven while teaching nothing. Every distractor here was lengthened to
sit within a few characters of its key, and each is still wrong for a reason
the lesson names — specification instead of idea, defensiveness instead of
enquiry, jargon instead of translation, deference instead of confidence.
"""

MC = [
    dict(
        ctx='A junior designer is presenting her concept for a cultural centre to a panel of clients. She wants to open with a strong statement about the idea&rsquo;s origin.',
        stem='Which phrase would most effectively open a design narrative?',
        options=[
            'This project is basically about making a fairly large new building somewhere near the waterfront.',
            'The concept grew out of a tension between public accessibility and private contemplation.',
            'We decided to use concrete for the structure because the structural engineer suggested it early on.',
            'The brief asked for a 2,000 square metre building with flexible seating arrangements throughout.',
        ],
        correct=1,
        why='<strong>Grew out of</strong> suggests organic, conceptual development, and framing the idea around a <em>tension</em> gives the narrative somewhere to go. The others open on a specification, a technical decision or the brief itself — none of which is an idea.',
    ),
    dict(
        ctx='A designer is explaining why the spatial layout of her proposal is unconventional. She wants to justify her reasoning without sounding defensive.',
        stem='Which phrase introduces a design decision in the most confident and professional way?',
        options=[
            'We tried to do something a bit different here because the usual approach seemed rather boring to us.',
            'The client did not actually specify any of this, but we thought that it might possibly be worth considering.',
            'Rather than defaulting to a conventional corridor typology, we organised the spaces around a central void.',
            'As you can see, we have moved a few things around to make the whole thing more interesting and modern.',
        ],
        correct=2,
        why='<strong>Rather than defaulting to</strong> is the structure: name the convention, then explain your departure from it. It shows you know the norm and chose against it. The others read as apology, whim, or decoration.',
    ),
    dict(
        ctx='During a pitch, a client interrupts: &ldquo;I&rsquo;m not sure this fits our brand identity.&rdquo; The designer needs to respond constructively.',
        stem='Which response keeps the conversation productive?',
        options=[
            'That is a valid concern. Could you help me understand which elements feel misaligned, so we can refine the direction together?',
            'We actually do think that it fits your brand — the moodboard we showed you earlier in this presentation makes that reasonably clear.',
            'Brand identity is quite a subjective matter, so it is genuinely hard to say definitively whether something fits it or not.',
            'We can change absolutely anything you want — just tell us what you would prefer and we will adjust the whole concept.',
        ],
        correct=0,
        why='It names the concern as valid, asks a clarifying question, and proposes working together. The others are defensive, evasive, or so accommodating that the designer disappears. Inviting dialogue is a sign of confidence, not weakness.',
    ),
    dict(
        ctx='A designer needs to explain an abstract idea — that a building should dissolve into its landscape rather than impose upon it.',
        stem='Which sentence articulates this most clearly to a non-specialist client?',
        options=[
            'We are using low-carbon materials throughout in order to reduce the environmental footprint of the finished structure.',
            'The building is designed to feel as though it has always been part of the site — its edges blur into the terrain.',
            'The roof will be planted and green, and the exterior cladding will be in natural tones chosen from a set palette.',
            'We have referenced a number of precedents drawn from Scandinavian landscape architecture to inform our approach.',
        ],
        correct=1,
        why='It turns an abstract idea into something you can picture: <em>always been part of the site</em>, <em>edges blur</em>. The others describe materials, finishes or references — true, but none of them is the idea.',
    ),
    dict(
        ctx='At the end of a pitch, the designer wants to invite questions and signal that the proposal can still move.',
        stem='Which closing balances confidence in the idea with openness to dialogue?',
        options=[
            'This is our final proposal, and we are confident that it fully meets every single part of the brief exactly as it was originally stated.',
            'We are honestly not sure this is quite the right direction yet, so we would love your thoughts before going further.',
            'We are presenting this as a strong direction rather than a fixed solution, and we look forward to developing it with you.',
            'Please take your time to review all of the drawings, and we will follow up with you by email early next week.',
        ],
        correct=2,
        why='It is precise about the proposal&rsquo;s status — a direction, not a solution — and <em>developing it with you</em> is partnership language. The first is closed, the second undercuts the work, the fourth defers without engaging.',
    ),
    dict(
        ctx='A designer is explaining the thread that connects every decision in a residential project.',
        stem='What does <em>design narrative</em> most accurately mean in a professional context?',
        options=[
            'The chronological story of the construction process, from the planning stage through to completion',
            'A coherent framework of ideas that gives meaning to each design decision',
            'The written description that is included in planning permission applications',
            'The marketing copy used to describe a project in press releases and on social media',
        ],
        correct=1,
        why='The narrative is the <em>why</em> — the thread that makes a set of decisions read as one argument. It is not a literal story, a legal document, or marketing copy, though pieces of it end up in all three.',
    ),
    dict(
        ctx='A product designer tells her team: &ldquo;We need to <em>foreground</em> the material qualities of the object — the tactility is central to the concept.&rdquo;',
        stem='What does <em>foreground</em> mean here?',
        options=[
            'To position the object at the very front of the display table during the presentation itself',
            'To emphasise something, making it the most prominent aspect of the presentation',
            'To photograph the object carefully against a simple and completely neutral background',
            'To carry out research on the materials before the design process properly begins',
        ],
        correct=1,
        why='<strong>To foreground</strong> is a verb borrowed from visual arts theory: to bring something to prominence so it cannot be missed. You foreground an idea, a quality, a tension.',
    ),
]

if __name__ == '__main__':
    import html, re
    for n, q in enumerate(MC, 1):
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', o))) for o in q['options']]
        k = L[q['correct']]
        flag = 'KEY LONGEST' if k == max(L) and L.count(max(L)) == 1 else 'ok'
        print('Q%d key=%d %s ratio=%.2f %s' % (n, k, L, k / min(L), flag))
