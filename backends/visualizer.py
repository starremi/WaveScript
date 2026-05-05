import matplotlib.pyplot as plt
from pathlib import Path

def save_waveform(audio_buffer, filename="outputs/waveform.png"):
    if len(audio_buffer) == 0:
        raise ValueError("Audio buffer is empty.")

    Path(filename).parent.mkdir(parents=True, exist_ok=True)

    step = 100
    samples = audio_buffer[::step]
    x = range(len(samples))

    plt.figure(figsize=(12, 4))
    plt.vlines(x, 0, samples)
    plt.axhline(0, linewidth=0.8)

    plt.title("WaveScript Waveform")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()
