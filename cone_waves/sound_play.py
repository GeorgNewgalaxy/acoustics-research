import numpy as np
import sounddevice as sd
from time import *

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

silence_time = 0.5


def play_tone(frequency, duration, samplerate):
    t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
    tone = 2 * np.sin(2 * np.pi * frequency * t)
    sd.play(tone, samplerate)
    sd.wait()


def sweep_tone(start, end, tones, time_per_tone, samplerate):
    for frequency in range(int(start*tones), int(end*tones), int(end - start)):
        play_tone(frequency/tones, time_per_tone, samplerate)
        sleep(silence_time)


sweep_tone(tone_min, tone_max, tones, seconds_per_tone, samplerate)
# play_tone(400, 5, 44100)
# play_tone(1000, 5, 44100)

