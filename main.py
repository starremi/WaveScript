import sys
from textx import metamodel_from_file
from interpreter.interpreter import WaveScriptInterpreter
import subprocess
from backends.audio import generate_audio
from backends.visualizer import save_waveform
from backends.lilypond import export_lilypond


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.wave>")
        return

    file_path = sys.argv[1]

    # Load grammar
    mm = metamodel_from_file('grammar/wavescript.tx')

    # Parse program
    model = mm.model_from_file(file_path)

    # Interpret
    interpreter = WaveScriptInterpreter()
    events = interpreter.interpret(model)

# debug taken out for final submission
    #print("\nGenerated Events:")
    #for e in events:
        #print(e)

    # Backend outputs
    audio_buffer = generate_audio(events, "outputs/audio.wav")
    save_waveform(audio_buffer, "outputs/waveform.png")
    export_lilypond(events, "outputs/score.ly", tempo=140)
    subprocess.run(["lilypond", "-o", "outputs/score", "outputs/score.ly"])

if __name__ == "__main__":
    main()
