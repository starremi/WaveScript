from pathlib import Path

PITCH_MAP = {
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

DURATION_MAP = {
    1.0: "4",   # quarter
    0.5: "8",   # eighth
    2.0: "2",   # half
    4.0: "1",   # whole
}


def export_lilypond(events, filename="outputs/score.ly"):
    if not events:
        raise ValueError("No events provided.")

    notes = []

    for event in events:
        pitch = event["pitch"]
        duration = event["duration"]

        lily_pitch = PITCH_MAP.get(pitch)
        if lily_pitch is None:
            raise ValueError(f"Unsupported pitch for LilyPond export: {pitch}")

        lily_duration = DURATION_MAP.get(duration)
        if lily_duration is None:
            raise ValueError(f"Unsupported duration for LilyPond export: {duration}")

        notes.append(f"{lily_pitch}{lily_duration}")

    score_body = " ".join(notes)

    lilypond_text = f'''\\version "2.24.0"
\\score {{
  \\new Staff {{
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
