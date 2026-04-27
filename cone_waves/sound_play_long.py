import numpy as np
import sounddevice as sd


def play_tone(frequency, duration, samplerate):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(tone, samplerate)
    sd.wait()


def sweep_tone(start, end, duration, samplerate):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    tone = 1 * np.sin(2 * np.pi * (start + t*(end - start)/duration) * t)
    sd.play(tone, samplerate)
    sd.wait()


play_tone(440, 1000, 44100)
