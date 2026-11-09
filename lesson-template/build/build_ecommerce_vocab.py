# -*- coding: utf-8 -*-
"""E-commerce Vocabulary (B1). House style 1, 25 slides, EN / DE / ES / IT.

Rebuilt 2026-11-06 from `ecommerce-vocabulary-b1.html`, an eighteen-item
one-at-a-time vocabulary check whose feedback gave each word in Italian.
Italian therefore ships alongside the house minimum of German and Spanish,
and every explanation gives the word in the learner's own language.

All eighteen items are kept. Fixed: Q13's key ("subscription", 12 letters)
was the only long option against 6-8; the distractors are now words of the
same length that do not fit ("a monthly registration").
Added: a glossary recap after the items (not before: it would answer
them), a gap slide, two speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_ecommerce_vocab.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='ecommerce-vocabulary-b1.html',
    title='E-commerce Vocabulary (B1)',
    folder='EcommerceVocab',
    scheme='cool',
    langs=('en', 'de', 'es', 'it'),
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    plates={
        'hero': 'a young woman shopping on a laptop on a sofa, cardboard parcels around her',
        'talk': 'cardboard parcels stacked on a front doorstep',
        'a1': 'a laptop screen showing a shopping basket with a pair of shoes and a jacket',
        'a2': 'hands holding a bank card beside a laptop at the payment step',
        'a3': 'a delivery van driving along a dotted route on a map to a house',
        'a4': 'a woman packing a jumper back into a cardboard box',
        'a5': 'a shopper reading star ratings on her phone in a shop',
        'a6': 'a smiling woman typing on a laptop, a price tag cut in half beside her',
        'a7': 'a man paying with his phone held up to a laptop',
        'a8': 'a phone showing a new email next to a newly ordered book',
        'a9': 'an empty space on a shoe shop shelf among rows of trainers',
        'b1': 'a shopper on a laptop walking past a long sign-up form',
        'b2': 'a delivery driver handing over a parcel at a front door',
        'b3': 'a bank card inside a glass box with a padlock',
        'b4': 'a sofa facing a television showing a grid of films, popcorn on the table',
        'b5': 'a dress on a mannequin with a small heart pinned to it',
        'b6': 'a loyalty card and a small wrapped gift box on a shop counter',
        'b7': 'many little market stalls inside a giant open laptop',
        'b8': 'coins flowing back into a wallet from a broken parcel',
        'b9': 'a long paper receipt beside an expenses folder on an office desk',
        'talk2': 'two friends comparing their shopping on their phones on a park bench',
        'results': 'a neat pile of delivered parcels tied with string',
    },
    pop={'hero': (None, 'square'), 'talk2': (None, 'blob')},
    results='results',
)

WORDS = ['basket', 'checkout', 'tracking', 'return', 'reviews', 'discount', 'payment', 'confirmation',
         'out of stock', 'guest', 'free', 'secure', 'subscription', 'wishlist', 'loyalty', 'marketplace',
         'refund', 'receipt']


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


A = [
    q('I put the shoes and the jacket in my online ____ before I paid.', ['basket', 'receipt', 'warehouse', 'invoice'], 1),
    q('Before you pay, you need to go to the ____ page and enter your card details.', ['checkout', 'wishlist', 'catalogue', 'subscription'], 2),
    q('The website sent me a ____ number so I could see exactly where my parcel was.', ['tracking', 'billing', 'loyalty', 'packaging'], 3),
    q('The jumper didn’t fit, so I sent it back using the shop’s ____ policy.', ['return', 'delivery', 'discount', 'security'], 4),
    q('I always read the ____ from other customers before I buy something expensive.', ['reviews', 'invoices', 'warehouses', 'subscriptions'], 5),
    q('I typed a ____ code at checkout and got 20% off my order.', ['discount', 'delivery', 'return', 'guest'], 6),
    q('You can pay by card, but this shop also accepts other ____ methods, like a digital wallet.', ['payment', 'shipping', 'loyalty', 'storage'], 7),
    q('After I ordered the book, I got an email with my order ____.', ['confirmation', 'warehouse', 'refund', 'catalogue'], 8),
    q('I wanted to buy the trainers, but they were ____ in my size.', ['out of stock', 'free shipping', 'best seller', 'on hold'], 9),
]
B = [
    q('I don’t want to create an account, so I’ll use ____ checkout instead.', ['guest', 'loyalty', 'secure', 'wishlist'], 10),
    q('Orders over €50 get ____ shipping, so I didn’t pay anything extra for delivery.', ['free', 'secure', 'express', 'tracked'], 11),
    q('The shop uses ____ payment technology, so my card details are protected.', ['secure', 'guest', 'bulk', 'loyal'], 12),
    q('I pay a monthly ____ for the streaming service; it renews automatically.', ['subscription', 'registration', 'confirmation', 'notification'], 13),
    q('I saved the dress to my ____ because I want to buy it next month.', ['wishlist', 'basket', 'receipt', 'catalogue'], 14),
    q('Because I shop there so often, I’ve collected enough ____ points for a free gift.', ['loyalty', 'guest', 'bulk', 'secure'], 15),
    q('This website isn’t a normal shop; it’s a ____ where lots of different sellers list their products.', ['marketplace', 'warehouse', 'invoice', 'subscription'], 16),
    q('The company kept my money for two weeks before they gave me a ____ for the broken item.', ['refund', 'discount', 'catalogue', 'tracking'], 17),
    q('I need the ____ from my order because my company will pay me back for it.', ['receipt', 'wishlist', 'warehouse', 'loyalty'], 18),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'What was the last thing you bought online?',
        'Do you read reviews before you buy?',
        'Have you ever sent something back?',
        'Which websites do you use most for shopping?',
        'Do you prefer to shop online or in a real shop?',
        'Have you ever had a problem with a delivery?',
    ], 'talk', 3),
    ('stage',),
    ('mc', 'e1', 'mcT', A, ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9'], None),
    ('stage',),
    ('mc', 'e2', 'mcT', B, ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9'], None),
    ('rules', 'eR', 'recT', [
        ('pBuy', ['r1', 'r2', 'r7', 'r12', 'r10', 'r8'], None),
        ('pAfter', ['r3', 'r4', 'r17', 'r18', 'r9', 'r11'], None),
        ('pShop', ['r5', 'r6', 'r13', 'r14', 'r15', 'r16'], None),
    ], None),
    ('gap', 'e3', 'gapT', 'gHint', [
        ('The parcel never arrived, so I asked for a ______.', ['refund'], 'gw1'),
        ('Use the code SPRING10 to get a 10% ______.', ['discount'], 'gw2'),
        ('Sorry, that size is out of ______ at the moment.', ['stock'], 'gw3'),
    ]),
    ('talk', 'eT', 'tk2T', [
        'Does your favourite shop have a <strong>loyalty</strong> card or points?',
        'What is on your <strong>wishlist</strong> at the moment?',
        'Do you usually check out as a <strong>guest</strong>, or create an account?',
        'Which <strong>subscriptions</strong> do you pay for every month?',
        'Have you ever waited a long time for a <strong>refund</strong>?',
        'How do you know a website is <strong>secure</strong>?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['refund', 'tracking number', 'out of stock', 'discount code', 'return policy', 'checkout', 'reviews']

DEF = {  # the glossary line per word: English definition, or the word in the learner's language
    'en': ['BASKET — where items wait until you pay', 'CHECKOUT — the page where you pay',
           'TRACKING — following your parcel', 'RETURN — sending something back',
           'REVIEWS — what other customers say', 'DISCOUNT — money off',
           'PAYMENT — how you pay', 'CONFIRMATION — the email that says “ordered”',
           'OUT OF STOCK — none left', 'GUEST — buying without an account',
           'FREE (shipping) — no delivery cost', 'SECURE — safe, protected',
           'SUBSCRIPTION — a payment that repeats', 'WISHLIST — things you want to buy later',
           'LOYALTY (points) — a reward for coming back', 'MARKETPLACE — many sellers, one site',
           'REFUND — your money back', 'RECEIPT — proof of what you paid'],
    'de': ['BASKET — Warenkorb', 'CHECKOUT — Kasse', 'TRACKING — Sendungsverfolgung', 'RETURN — Rücksendung',
           'REVIEWS — Bewertungen', 'DISCOUNT — Rabatt', 'PAYMENT — Zahlung', 'CONFIRMATION — Bestätigung',
           'OUT OF STOCK — ausverkauft', 'GUEST — Gast (ohne Konto)', 'FREE (shipping) — kostenlos',
           'SECURE — sicher', 'SUBSCRIPTION — Abonnement', 'WISHLIST — Wunschliste',
           'LOYALTY (points) — Treuepunkte', 'MARKETPLACE — Online-Marktplatz', 'REFUND — Rückerstattung',
           'RECEIPT — Quittung, Beleg'],
    'es': ['BASKET — cesta, carrito', 'CHECKOUT — caja, pago', 'TRACKING — seguimiento', 'RETURN — devolución',
           'REVIEWS — reseñas', 'DISCOUNT — descuento', 'PAYMENT — pago', 'CONFIRMATION — confirmación',
           'OUT OF STOCK — agotado', 'GUEST — invitado (sin cuenta)', 'FREE (shipping) — gratis',
           'SECURE — seguro', 'SUBSCRIPTION — suscripción', 'WISHLIST — lista de deseos',
           'LOYALTY (points) — puntos de fidelidad', 'MARKETPLACE — mercado online', 'REFUND — reembolso',
           'RECEIPT — recibo'],
    'it': ['BASKET — carrello', 'CHECKOUT — pagamento, cassa', 'TRACKING — tracciamento', 'RETURN — reso, restituzione',
           'REVIEWS — recensioni', 'DISCOUNT — sconto', 'PAYMENT — pagamento', 'CONFIRMATION — conferma',
           'OUT OF STOCK — esaurito', 'GUEST — ospite (senza account)', 'FREE (shipping) — gratuita',
           'SECURE — sicuro', 'SUBSCRIPTION — abbonamento', 'WISHLIST — lista dei desideri',
           'LOYALTY (points) — punti fedeltà', 'MARKETPLACE — mercato online', 'REFUND — rimborso',
           'RECEIPT — ricevuta'],
}
WHY = {
    'en': ['The BASKET is where your items wait until you pay.', 'The CHECKOUT is the page where you pay.',
           'A TRACKING number lets you follow the parcel.', 'A RETURN policy says how you can send things back.',
           'REVIEWS are what other customers write about a product.', 'A DISCOUNT code gives you money off.',
           'PAYMENT methods: card, digital wallet, bank transfer.', 'The order CONFIRMATION is the email that says the order went through.',
           'OUT OF STOCK: there are none left.', 'GUEST checkout: you buy without creating an account.',
           'FREE shipping: you pay nothing for delivery.', 'SECURE payment: your card details are protected.',
           'A SUBSCRIPTION is a payment that repeats, every month or year.', 'A WISHLIST keeps things you want to buy later.',
           'LOYALTY points reward you for shopping there again.', 'A MARKETPLACE is one site where many sellers list products.',
           'A REFUND is your money back.', 'A RECEIPT is proof of what you paid.'],
}
WHY['de'] = ['%s = „%s“.' % (w.upper(), d.split(' — ')[1]) for w, d in zip(WORDS, DEF['de'])]
WHY['es'] = ['%s = «%s».' % (w.upper(), d.split(' — ')[1]) for w, d in zip(WORDS, DEF['es'])]
WHY['it'] = ['%s = «%s».' % (w.upper(), d.split(' — ')[1]) for w, d in zip(WORDS, DEF['it'])]
# In the learner's language the explanation is the word itself — what the
# old page's feedback gave ("basket = carrello"). English gets what it does.

T = {
    'en': dict(
        coverTitle='E-commerce <br><em>Vocabulary</em>',
        coverSub='Eighteen words you meet when you shop online — basket, checkout, tracking, refunds, discount codes — in sentences, then in your own.',
        chipLevel='B1', chipFocus='online shopping', chipCount='25 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Buying online', e2='After you buy', e3='Your turn',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the right word', recT='The eighteen words',
        pBuy='Buying', pAfter='After you buy', pShop='The shop',
        gapT='Write the missing word', gHint='One word in each gap.',
        gw1='Your money back: a REFUND.', gw2='Money off: a DISCOUNT.', gw3='None left: OUT OF STOCK.',
        actTitle='The online shop', actUse='Use at least three:',
        actSpeakBrief='In pairs: one of you is a customer, the other works in customer service.',
        actSpeak1='Customer: your parcel has not arrived. Ask about TRACKING and a REFUND.',
        actSpeak2='Customer service: offer a DISCOUNT CODE or FREE SHIPPING on the next order.',
        actSpeak3='Swap roles: the jumper does not fit. Ask about the RETURN POLICY.',
        actWriteKind='Writing',
        actWriteBrief='Write an online review of a shop (100–120 words): the CHECKOUT, the DELIVERY, the RETURN POLICY, and whether you would buy there again.',
        actPlaceholder='I ordered a jacket last week and …',
    ),
    'de': dict(
        coverTitle='E-commerce <br><em>Vocabulary</em>',
        coverSub='Achtzehn Wörter, die dir beim Online-Shopping begegnen — Warenkorb, Kasse, Sendungsverfolgung, Rückerstattung, Rabattcode — im Satz und dann in deinen eigenen.',
        chipLevel='B1', chipFocus='Online-Shopping', chipCount='25 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Online kaufen', e2='Nach dem Kauf', e3='Du bist dran',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle das richtige Wort', recT='Die achtzehn Wörter',
        pBuy='Kaufen', pAfter='Nach dem Kauf', pShop='Der Shop',
        gapT='Ergänze das fehlende Wort', gHint='Ein Wort pro Lücke.',
        gw1='Dein Geld zurück: ein REFUND (Rückerstattung).', gw2='Geld weniger: ein DISCOUNT (Rabatt).',
        gw3='Keins mehr da: OUT OF STOCK (ausverkauft).',
        actTitle='Der Onlineshop', actUse='Verwende mindestens drei:',
        actSpeakBrief='Zu zweit: Eine Person ist Kunde, die andere arbeitet im Kundenservice.',
        actSpeak1='Kunde: Dein Paket ist nicht angekommen. Frag nach TRACKING und einem REFUND.',
        actSpeak2='Kundenservice: Biete einen DISCOUNT CODE oder FREE SHIPPING für die nächste Bestellung an.',
        actSpeak3='Tauscht die Rollen: Der Pullover passt nicht. Frag nach der RETURN POLICY.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib eine Online-Bewertung eines Shops (100–120 Wörter): die CHECKOUT, die DELIVERY, die RETURN POLICY und ob du dort wieder kaufen würdest.',
        actPlaceholder='I ordered a jacket last week and …',
    ),
    'es': dict(
        coverTitle='E-commerce <br><em>Vocabulary</em>',
        coverSub='Dieciocho palabras que encuentras al comprar online — carrito, pago, seguimiento, reembolsos, códigos de descuento — en oraciones y después en las tuyas.',
        chipLevel='B1', chipFocus='compras online', chipCount='25 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Comprar online', e2='Después de comprar', e3='Tu turno',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la palabra correcta', recT='Las dieciocho palabras',
        pBuy='Comprar', pAfter='Después de comprar', pShop='La tienda',
        gapT='Escribe la palabra que falta', gHint='Una palabra en cada hueco.',
        gw1='Tu dinero de vuelta: un REFUND (reembolso).', gw2='Dinero menos: un DISCOUNT (descuento).',
        gw3='No queda ninguno: OUT OF STOCK (agotado).',
        actTitle='La tienda online', actUse='Usa al menos tres:',
        actSpeakBrief='En parejas: uno es cliente y el otro trabaja en atención al cliente.',
        actSpeak1='Cliente: tu paquete no ha llegado. Pregunta por el TRACKING y un REFUND.',
        actSpeak2='Atención al cliente: ofrece un DISCOUNT CODE o FREE SHIPPING en el próximo pedido.',
        actSpeak3='Cambien los papeles: el jersey no te queda bien. Pregunta por la RETURN POLICY.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe una reseña online de una tienda (100–120 palabras): el CHECKOUT, la DELIVERY, la RETURN POLICY y si volverías a comprar allí.',
        actPlaceholder='I ordered a jacket last week and …',
    ),
    'it': dict(
        coverTitle='E-commerce <br><em>Vocabulary</em>',
        coverSub='Diciotto parole che incontri facendo acquisti online — carrello, pagamento, tracciamento, rimborsi, codici sconto — in frasi e poi nelle tue.',
        chipLevel='B1', chipFocus='acquisti online', chipCount='25 slide',
        eW='Per cominciare', eT='Parliamo!', eR='Ripasso', e1='Comprare online', e2='Dopo l’acquisto', e3='Tocca a te',
        tk1T='Parliamo!', tk2T='Parliamo!', mcT='Scegli la parola giusta', recT='Le diciotto parole',
        pBuy='Comprare', pAfter='Dopo l’acquisto', pShop='Il negozio',
        gapT='Scrivi la parola mancante', gHint='Una parola per ogni spazio.',
        gw1='I tuoi soldi indietro: un REFUND (rimborso).', gw2='Soldi in meno: uno DISCOUNT (sconto).',
        gw3='Non ce n’è più: OUT OF STOCK (esaurito).',
        actTitle='Il negozio online', actUse='Usane almeno tre:',
        actSpeakBrief='In coppia: uno è il cliente, l’altro lavora nel servizio clienti.',
        actSpeak1='Cliente: il tuo pacco non è arrivato. Chiedi del TRACKING e di un REFUND.',
        actSpeak2='Servizio clienti: offri un DISCOUNT CODE o la FREE SHIPPING sul prossimo ordine.',
        actSpeak3='Scambiatevi i ruoli: il maglione non va bene. Chiedi della RETURN POLICY.',
        actWriteKind='Scrittura',
        actWriteBrief='Scrivi una recensione online di un negozio (100–120 parole): il CHECKOUT, la DELIVERY, la RETURN POLICY e se ci compreresti di nuovo.',
        actPlaceholder='I ordered a jacket last week and …',
    ),
}
for c in T:
    for i, w in enumerate(WHY[c], 1):
        T[c]['w%d' % i] = w
    for i, d in enumerate(DEF[c], 1):
        T[c]['r%d' % i] = d

H.check_keys(T, SPEC['langs'])

if __name__ == '__main__':
    H.build(SPEC, T)
