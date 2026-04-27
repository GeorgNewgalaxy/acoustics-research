import numpy as np
import sounddevice as sd

settings_file = open("settings")
settings = settings_file.read()
settings_file.close()
settings_array = settings.split("\n")
settings_array = [float(settings_array[i].split(" ")[0]) for i in range(0, len(settings_array))]

seconds_per_tone = settings_array[0]
tone_min = settings_array[1]
tone_max = settings_array[2]
tones = settings_array[3]
samplerate = settings_array[4]


def play(start_tone, end_tone, tones, time, samplerate):
    t = np.linspace(0, time, int(samplerate * time), endpoint=False)
    freqs = [frequency/tones for frequency in range(int(start_tone*tones), int(end_tone*tones), int(end_tone - start_tone))]
    sound = 0.0 * np.sin(2 * np.pi * freqs[0] * t)
    for i in range(0, len(freqs)):
        sound += 0.5 * np.sin(2 * np.pi * freqs[i] * t)

    sd.play(sound, samplerate)
    sd.wait()


play(tone_min, tone_max, tones, 4, samplerate)
