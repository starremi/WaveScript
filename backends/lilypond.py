from pathlib import Path

PITCH_MAP = {
    "C3": "c",
    "D3": "d",
    "E3": "e",
    "F3": "f",
    "G3": "g",
    "A3": "a",
    "B3": "b",

    "C4": "c'",
    "D4": "d'",
    "E4": "e'",
    "F4": "f'",
    "G4": "g'",
    "A4": "a'",
    "B4": "b'",

    "C5": "c''",
    "D5": "d''",
    "E5": "e''",
    "F5": "f''",
    "G5": "g''",
    "A5": "a''",
    "B5": "b''",
}


def duration_to_lilypond(duration, tempo=140):
    quarter_seconds = 60 / tempo

    ratio = duration / quarter_seconds

    if abs(ratio - 0.5) < 0.15:
        return "8"   # eighth note
    elif abs(ratio - 1.0) < 0.15:
        return "4"   # quarter note
    elif abs(ratio - 2.0) < 0.25:
        return "2"   # half note
    elif abs(ratio - 4.0) < 0.35:
        return "1"   # whole note
    else:
        return "4"   # fallback to quarter note


def export_lilypond(events, filename="outputs/score.ly", tempo=140):
    if not events:
        raise ValueError("No events provided.")

    notes = []

    for event in events:
        pitch = event["pitch"]
        duration = event["duration"]

        lily_pitch = PITCH_MAP.get(pitch)
        if lily_pitch is None:
            raise ValueError(f"Unsupported pitch for LilyPond export: {pitch}")

        lily_duration = duration_to_lilypond(duration, tempo)

        notes.append(f"{lily_pitch}{lily_duration}")

    score_body = " ".join(notes)

    lilypond_text = f'''\\version "2.24.0"
\\score {{
  \\new Staff {{
    \\tempo 4 = {tempo}
    {score_body}
  }}
  \\layout {{ }}
  \\midi {{ }}
}}
'''

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(lilypond_text)

    return lilypond_text