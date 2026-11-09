# -*- coding: utf-8 -*-
"""Gaming YouTubers (B2). House style 1, 22 slides.

Rebuilt 2026-11-06 from `forbes-gaming-youtube-b2.html`: five multiple
choice on gaming-channel know-how, six vocabulary gaps (walkthrough,
speedrun, commentary, meta, patch, grind) and five step-ordering tasks.
All sixteen are kept.

Fixed:
  * The META item printed its own answer in the stem ("… content about the
    meta always attracts serious gamers"). Cut.
  * The explanation said META is "short for 'most effective tactics
    available'": a backronym. It comes from METAGAME, the game around the
    game.
  * Three of the five ordering tasks had more than one sensible order
    (branding before or after equipment; announcing a stream before or
    after the test run; the "if constructive" and "if toxic" steps are
    alternatives, not a sequence). Those three are now "what comes first /
    last" questions with one answer. The two true sequences (a
    walkthrough, a reaction video) stay as builds.
Added: a recap of the channel words, speaking fields and the activation.

Run from the repo root:  py lesson-template/build/build_gaming_youtube.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hs2quiz as H

SPEC = dict(
    out='forbes-gaming-youtube-b2.html',
    title='Gaming YouTubers (B2)',
    folder='GamingYouTube',
    scheme='cool',
    style='hs1',
    # House style 1 (HOUSE-STYLE §000, 2026-11-09): Midjourney plates, his style
    # images at --stylize 200, one per slide, briefs here.
    # The five scenario items are too long for any frame (texture field).
    plates={
        'hero': 'a teenager streaming a video game in a bedroom lit by screens, headset on',
        'talk': 'a games controller and a headset on a desk beside a microphone',
        'b1': 'a gamer pointing at a map of a game level on a big screen',
        'b2': 'a gamer racing through a level, a stopwatch beside the screen',
        'b3': 'a streamer laughing into a microphone in front of a game',
        'b4': 'a table of game character cards and equipment laid out like a strategy board',
        'b5': 'a game developer fixing glitchy pixel blocks on a monitor',
        'b6': 'a tired gamer playing the same mission again late at night',
        'o1': 'a creator editing gameplay footage on a laptop',
        'o2': 'a gamer reacting with surprise to a new game trailer',
        'c1': 'a young creator planning a channel with sketches pinned on a wall',
        'c2': 'a streamer going live, a chat window glowing beside the game',
        'c3': 'a creator frowning at a comment on a phone',
        'talk2': 'two friends playing a video game together on a sofa',
        'results': 'a games controller resting on a beanbag',
    },
    pop={'hero': (None, 'square'), 'b3': (None, 'free'), 'talk2': (None, 'blob')},
    results='results',
)


def q(stem, options, n):
    return dict(stem=stem, options=options, correct=0, why='w%d' % n)


MC = [
    q('A young gaming YouTuber plays a popular game in their videos. The publisher sends a copyright claim. What does this most likely mean?',
      ['The publisher may claim the advertising revenue from those videos instead of the creator',
       'The channel will be permanently deleted unless all gaming content is removed immediately',
       'The creator must buy a professional licence and pay a monthly fee to keep using the footage',
       'The creator is banned from earning money on any gaming content for twelve months'], 1),
    q('Which kind of gaming video is most often called “evergreen” — it keeps attracting views long after it is published?',
      ['Tutorials explaining the mechanics, secrets or strategies of well-established games',
       'Live-streamed reactions to major gaming events, broadcast to a global audience in real time',
       'News videos about newly announced games or the latest gaming hardware updates',
       'Highlight clips from online tournaments, which trend for about a week after the event'], 2),
    q('A creator’s channel covers only Minecraft. Compared with a general gaming channel, what is the main advantage?',
      ['It builds a more loyal and engaged community of viewers who share one interest',
       'It always earns more advertising money because Minecraft has a bigger audience',
       'The algorithm always recommends single-game channels first, ahead of all others',
       'The creator can upload less often, because the audience watches every video anyway'], 3),
    q('A kids’ gaming YouTuber wants background music. Which is the safest choice to avoid copyright strikes?',
      ['Tracks from YouTube’s Audio Library, or other sources with royalty-free licences',
       'Popular songs from streaming sites, with the volume turned down below fifty per cent',
       'Chart music for under thirty seconds, because short clips are free to use',
       'Any song, as long as the artist is credited in the video description'], 4),
    q('In gaming YouTube culture, what is a “let’s play”?',
      ['A recorded playthrough of a game, with the creator’s commentary all the way through',
       'A competitive multiplayer session recorded so that coaches can analyse the ranking',
       'A short highlights reel that keeps only the most exciting moments of a session',
       'A live event where two creators compete against each other in front of an audience'], 5),
]
VOCAB = [
    q('A ____ is a video that guides viewers step by step through a game: how to complete levels, find secrets and defeat bosses.',
      ['walkthrough', 'speedrun', 'livestream', 'commentary'], 6),
    q('In a ____, a player tries to finish a game as quickly as possible, often using glitches to break the game’s intended design.',
      ['speedrun', 'rage-quit', 'grind', 'commentary'], 7),
    q('A creator’s spoken ____ — live reactions, jokes and explanations — is often what makes a channel more than a screen recording.',
      ['commentary', 'leaderboard', 'soundtrack', 'cutscene'], 8),
    q('In competitive gaming, the ____ is the set of strategies, characters and equipment that work best right now.',
      ['meta', 'grind', 'loot', 'respawn'], 9),
    q('Many YouTubers react to a new game ____ — an update that fixes bugs and changes the balance of characters or weapons.',
      ['patch', 'loot', 'grind', 'respawn'], 10),
    q('To ____ in a game means to repeat the same actions again and again, for example missions for experience points.',
      ['grind', 'loot', 'respawn', 'clip'], 11),
]
STEPS = [
    q('You are starting a gaming channel from scratch. What should you do FIRST?',
      ['Decide your type of content and your audience', 'Film a short trailer that introduces you and your channel',
       'Publish your first three videos', 'Promote your videos in gaming communities'], 14),
    q('You are preparing your first live stream. Which step comes LAST?',
      ['Go live and talk to viewers in the chat', 'Test that your internet connection is stable',
       'Set up streaming software such as OBS', 'Do a short private test stream'], 15),
    q('A viewer leaves a nasty comment under your video. What is the best FIRST step?',
      ['Read it carefully: is it criticism or just abuse?', 'Reply to it straight away, so that it can’t spread',
       'Delete the video and upload it again later', 'Ask your other viewers to answer it for you'], 16),
]

SPEC['flow'] = [
    ('talk', 'eW', 'tk1T', [
        'Which YouTubers or streamers do you watch?',
        'What makes a gaming video worth watching?',
        'Have you ever made a video or a stream?',
        'Would you watch someone else play a game? Why?',
        'Which game would you make videos about?',
        'Should children be YouTubers?',
    ], 'talk', 3),
    ('stage',),
    ('mc', 'e1', 'mcT', MC, None, None),
    ('stage',),
    ('mc', 'e2', 'mcT', VOCAB, ['b1', 'b2', 'b3', 'b4', 'b5', 'b6'], None),
    ('stage',),
    ('order', 'e3', 'orderT', 'orderHint', [
        (['Choose a game and a level,', 'play it through first,', 'record it with commentary,', 'edit out the mistakes,',
          'and upload it with a good title.'], None, 'w12'),
        (['Watch the news for big releases,', 'prepare your talking points,', 'record your first reaction,',
          'edit in the best moments,', 'and publish as soon as the game is out.'], None, 'w13'),
    ], ['o1', 'o2'], None),
    ('stage',),
    ('mc', 'e4', 'mcT', STEPS, ['c1', 'c2', 'c3'], None),
    ('rules', 'eR', 'recT', [
        ('pVideos', [(None, 'a walkthrough · a let’s play'), (None, 'a speedrun · a livestream'), (None, 'evergreen content')], None),
        ('pGame', [(None, 'the meta · a patch'), (None, 'to grind · loot · to respawn'), (None, 'to rage-quit')], None),
        ('pChannel', [(None, 'commentary · a niche'), (None, 'a copyright claim · royalty-free'), (None, 'to monetise')], None),
    ], None),
    ('talk', 'eT', 'tk2T', [
        'Which game would you <strong>speedrun</strong>, if you could?',
        'Is it fun to watch someone <strong>grind</strong>? Why?',
        'What makes good <strong>commentary</strong>?',
        'Which kind of video is the most <strong>evergreen</strong>?',
        'How should a creator answer <strong>toxic</strong> comments?',
        'Would you rather make a <strong>walkthrough</strong> or a <strong>let’s play</strong>?',
    ], 'talk2', 3),
]
SPEC['chips'] = ['walkthrough', 'commentary', 'evergreen', 'the meta', 'a patch', 'royalty-free', 'niche']

W = {
    'en': [
        'A copyright claim usually sends the video’s advertising money to the rights holder. The video and the channel stay.',
        'Tutorials and guides are EVERGREEN: people search for them for years. Streams, news and tournament clips fade fast.',
        'A NICHE channel builds loyalty: viewers know what to expect, so they engage more.',
        'Only properly licensed music is safe: YouTube’s Audio Library or royalty-free tracks. Volume, length and credits change nothing.',
        'A LET’S PLAY is a recorded playthrough where the commentary — the creator’s personality — is the point.',
        'A WALKTHROUGH guides you through a game step by step.',
        'A SPEEDRUN: finishing as fast as possible.',
        'COMMENTARY: the creator talking while playing.',
        'The META, from METAGAME: the strategies that work best right now.',
        'A PATCH: an update that fixes bugs and changes the balance.',
        'To GRIND: repeat the same actions for slow rewards.',
        'You must know a section before you can guide others through it: play it, then record, edit and upload.',
        'Watch for releases, prepare, record, edit — then publish fast, while people are searching.',
        'Everything else depends on the concept: decide the content and the audience first.',
        'Testing comes before going live: going live is the last step.',
        'Decide what kind of comment it is before you do anything else. Reacting emotionally is the most common mistake.',
    ],
    'de': [
        'Eine Urheberrechtsbeschwerde leitet meist die Werbeeinnahmen an den Rechteinhaber weiter. Video und Kanal bleiben.',
        'Tutorials und Anleitungen sind EVERGREEN: Man sucht sie jahrelang. Streams, News und Turnierclips verblassen schnell.',
        'Ein NISCHEN-Kanal schafft Treue: Die Zuschauer wissen, was sie erwartet, und machen mehr mit.',
        'Sicher ist nur richtig lizenzierte Musik: die Audio-Mediathek von YouTube oder lizenzfreie Titel. Lautstärke, Länge und Nennung ändern nichts.',
        'Ein LET’S PLAY ist ein aufgezeichneter Spieldurchgang, bei dem der Kommentar — die Persönlichkeit — das Wichtigste ist.',
        'Ein WALKTHROUGH führt Schritt für Schritt durch ein Spiel.',
        'Ein SPEEDRUN: ein Spiel so schnell wie möglich beenden.',
        'COMMENTARY: der Kommentar beim Spielen.',
        'Das META, von METAGAME: die Strategien, die gerade am besten funktionieren.',
        'Ein PATCH: ein Update, das Fehler behebt und das Gleichgewicht ändert.',
        'GRIND: dieselben Aktionen immer wieder wiederholen, für langsame Belohnungen.',
        'Man muss einen Abschnitt kennen, bevor man andere hindurchführt: spielen, dann aufnehmen, schneiden, hochladen.',
        'Neuerscheinungen verfolgen, vorbereiten, aufnehmen, schneiden — dann schnell veröffentlichen, solange gesucht wird.',
        'Alles andere hängt vom Konzept ab: zuerst Inhalt und Zielgruppe festlegen.',
        'Das Testen kommt vor dem Livegang: Live gehen ist der letzte Schritt.',
        'Erst entscheiden, was für ein Kommentar es ist. Emotional zu reagieren ist der häufigste Fehler.',
    ],
    'es': [
        'Una reclamación de derechos de autor suele enviar los ingresos por publicidad al titular de los derechos. El vídeo y el canal siguen.',
        'Los tutoriales y guías son EVERGREEN: la gente los busca durante años. Directos, noticias y clips de torneos pasan rápido.',
        'Un canal de NICHO crea fidelidad: los espectadores saben qué esperar y participan más.',
        'Solo es segura la música con licencia: la Biblioteca de audio de YouTube o temas libres de derechos. El volumen, la duración o citar al artista no cambian nada.',
        'Un LET’S PLAY es una partida grabada en la que lo importante es el comentario, la personalidad del creador.',
        'Un WALKTHROUGH te guía paso a paso por un juego.',
        'Un SPEEDRUN: terminar un juego lo más rápido posible.',
        'COMMENTARY: el comentario mientras se juega.',
        'El META, de METAGAME: las estrategias que mejor funcionan ahora mismo.',
        'Un PATCH: una actualización que corrige errores y cambia el equilibrio.',
        'GRIND: repetir las mismas acciones una y otra vez para recompensas lentas.',
        'Hay que conocer una parte antes de guiar a otros: jugarla, luego grabar, editar y subir.',
        'Sigue los lanzamientos, prepárate, graba, edita y publica rápido, mientras la gente busca.',
        'Todo lo demás depende del concepto: primero decide el contenido y el público.',
        'Las pruebas van antes de emitir: salir en directo es el último paso.',
        'Primero decide qué tipo de comentario es. Reaccionar con emoción es el error más común.',
    ],
}

T = {
    'en': dict(
        coverTitle='Gaming <br><em>YouTubers</em>',
        coverSub='Channels, copyright and community: the know-how and the vocabulary of gaming video, from walkthroughs and speedruns to patches and the meta.',
        chipLevel='B2', chipFocus='gaming vocabulary · channels', chipCount='22 slides',
        eW='Warm-up', eT='Let’s talk', eR='Review', e1='Channel know-how', e2='Gaming words', e3='The workflow', e4='First and last',
        tk1T='Let’s talk!', tk2T='Let’s talk!', mcT='Choose the best answer',
        orderT='Put the steps in order', orderHint='Click the steps in the order you would do them.',
        recT='The words of the channel', pVideos='Kinds of video', pGame='Inside the game', pChannel='Running a channel',
        actTitle='Pitch your channel', actUse='Use at least four:',
        actSpeakBrief='In pairs: you are planning a gaming channel together.',
        actSpeak1='Agree your NICHE: which game, which audience, and why.',
        actSpeak2='Plan three videos: one WALKTHROUGH, one LET’S PLAY and one that is EVERGREEN.',
        actSpeak3='Decide your rules: music, COPYRIGHT and how you answer toxic comments.',
        actWriteKind='Writing',
        actWriteBrief='Write the “About” text for your new channel (100–130 words): what you play, what kind of videos you make, how often you upload, and what viewers can expect.',
        actPlaceholder='Welcome to the channel! Here you’ll find …',
    ),
    'de': dict(
        coverTitle='Gaming <br><em>YouTubers</em>',
        coverSub='Kanäle, Urheberrecht und Community: das Know-how und das Vokabular von Gaming-Videos, von Walkthroughs und Speedruns bis zu Patches und dem Meta.',
        chipLevel='B2', chipFocus='Gaming-Vokabular · Kanäle', chipCount='22 Folien',
        eW='Zum Einstieg', eT='Sprechen wir!', eR='Wiederholung', e1='Kanal-Know-how', e2='Gaming-Wörter', e3='Der Ablauf', e4='Zuerst und zuletzt',
        tk1T='Sprechen wir!', tk2T='Sprechen wir!', mcT='Wähle die beste Antwort',
        orderT='Bring die Schritte in Ordnung', orderHint='Klicke die Schritte in der Reihenfolge an, in der du sie machen würdest.',
        recT='Die Wörter des Kanals', pVideos='Arten von Videos', pGame='Im Spiel', pChannel='Einen Kanal betreiben',
        actTitle='Stell deinen Kanal vor', actUse='Verwende mindestens vier:',
        actSpeakBrief='Zu zweit: Ihr plant zusammen einen Gaming-Kanal.',
        actSpeak1='Einigt euch auf eure NISCHE: welches Spiel, welches Publikum und warum.',
        actSpeak2='Plant drei Videos: einen WALKTHROUGH, ein LET’S PLAY und eines, das EVERGREEN ist.',
        actSpeak3='Legt eure Regeln fest: Musik, URHEBERRECHT und wie ihr auf toxische Kommentare antwortet.',
        actWriteKind='Schreiben',
        actWriteBrief='Schreib den „Über mich“-Text für deinen neuen Kanal (100–130 Wörter): was du spielst, welche Videos du machst, wie oft du hochlädst und was die Zuschauer erwartet.',
        actPlaceholder='Welcome to the channel! Here you’ll find …',
    ),
    'es': dict(
        coverTitle='Gaming <br><em>YouTubers</em>',
        coverSub='Canales, derechos de autor y comunidad: lo que hay que saber y el vocabulario del vídeo de videojuegos, de los walkthroughs y speedruns a los parches y el meta.',
        chipLevel='B2', chipFocus='vocabulario gamer · canales', chipCount='22 diapositivas',
        eW='Para empezar', eT='¡A conversar!', eR='Repaso', e1='Saber de canales', e2='Palabras del juego', e3='El proceso', e4='Primero y último',
        tk1T='¡A conversar!', tk2T='¡A conversar!', mcT='Elige la mejor respuesta',
        orderT='Ordena los pasos', orderHint='Haz clic en los pasos en el orden en que los harías.',
        recT='Las palabras del canal', pVideos='Tipos de vídeo', pGame='Dentro del juego', pChannel='Llevar un canal',
        actTitle='Presenta tu canal', actUse='Usa al menos cuatro:',
        actSpeakBrief='En parejas: están planeando juntos un canal de videojuegos.',
        actSpeak1='Acuerden su NICHO: qué juego, qué público y por qué.',
        actSpeak2='Planeen tres vídeos: un WALKTHROUGH, un LET’S PLAY y uno EVERGREEN.',
        actSpeak3='Decidan sus normas: música, DERECHOS DE AUTOR y cómo responder a comentarios tóxicos.',
        actWriteKind='Escritura',
        actWriteBrief='Escribe el texto «Acerca de» de tu nuevo canal (100–130 palabras): a qué juegas, qué vídeos haces, cada cuánto subes y qué pueden esperar los espectadores.',
        actPlaceholder='Welcome to the channel! Here you’ll find …',
    ),
}
for c in T:
    for i, w in enumerate(W[c], 1):
        T[c]['w%d' % i] = w

H.check_keys(T)

if __name__ == '__main__':
    H.build(SPEC, T)
