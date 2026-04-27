import sounddevice as sd
import numpy as np
from random import random

fs = 44100
first_sample_time = -1


def callback(indata, outdata, frames, time, status):
    global first_sample_time
    if first_sample_time == -1:
        first_sample_time = time.currentTime
    if status:
        print(status)
    t = []
    for i in range(0, len(indata)):
        t.append(time.currentTime + i/fs)
    t = np.array(t)
    f = 500
    outdata[:] = np.sin(2*f*np.pi*t).reshape((len(indata), 1))


print(sd.query_devices())

try:
    with sd.Stream(device=(0,1), samplerate=fs, dtype='float32', latency=None, channels=1, callback=callback):
        input()
except KeyboardInterrupt:
    pass