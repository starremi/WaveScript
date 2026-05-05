
import numpy as np
from scipy.io.wavfile import write
from pathlib import Path

SAMPLE_RATE = 44100
AMPLITUDE = 0.5


def generate_audio(events, filename="outputs/audio.wav"):
    if not events:
        raise ValueError("No events provided.")

    total_duration = max(event["start"] + event["duration"] for event in events)
    total_samples = int(total_duration * SAMPLE_RATE)

    audio_buffer = np.zeros(total_samples)

    for event in events:
        frequency = event["frequency"]
        start_time = event["start"]
        duration = event["duration"]

        start_sample = int(start_time * SAMPLE_RATE)
        num_samples = int(duration * SAMPLE_RATE)
        end_sample = start_sample + num_samples

        t = np.linspace(0, duration, num_samples, endpoint=False)
        wave = AMPLITUDE * np.sin(2 * np.pi * frequency * t)

        audio_buffer[start_sample:end_sample] += wave

    max_val = np.max(np.abs(audio_buffer))
    if max_val > 0:
        audio_buffer = audio_buffer / max_val

    audio_int16 = np.int16(audio_buffer * 32767)

    Path(filename).parent.mkdir(parents=True, exist_ok=True)
    write(filename, SAMPLE_RATE, audio_int16)

    return audio_buffer
