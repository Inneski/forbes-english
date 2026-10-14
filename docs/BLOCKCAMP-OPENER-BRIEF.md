# Block Camp opener clips — brief

Innes, 2026-10-14: the camps go straight into an animated opener; the rule
pages are a separate option (Rules button on the cover and in the deck bar,
`block-camp/camp-rules.js`).

Each camp's cover already points at its opener. **Dropping the file at the
path below is the whole job** — no deck edit. Until it exists the cover
shows its still, as before.

| Deck | File |
|---|---|
| Present Simple 1 | `BlockCamp/openers/present-simple-1a.mp4` |
| Present Continuous 1 | `BlockCamp/openers/present-continuous-1a.mp4` |
| Past Simple 1 | `BlockCamp/openers/past-simple-1a.mp4` |
| Past Continuous 1 | `BlockCamp/openers/past-continuous-1a.mp4` |

**The clip.** 16:9, 1280x720, 6–10 s, made from the cover still
(`BlockCamp/<camp>-1a.jpg`) as frame 0 so the still → video handover does not
jump. Keep the left-centre calm: the title, chips and buttons sit there.
Plays once, with sound if the browser allows (muted otherwise), and holds its
last frame. Encode as the hub flythrough: H.264 CRF 27, veryslow, faststart.

**Getting it in.** Drop the raw clips in `incoming/block-camp-openers/` on
the desktop and run `/publish` in a local session (cloud sessions cannot see
`incoming/`).

The other 22 camp decks get the same change once these four are approved.
