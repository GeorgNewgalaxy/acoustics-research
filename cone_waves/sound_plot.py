from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

samplerate_cone, data_cone = wavfile.read("with_cone.wav")
length_cone = data_cone.shape[0] / samplerate_cone
samples_cone = int(length_cone*samplerate_cone)
signal_cone = data_cone

rolling_maximum_length = 200
rolling_maximum = [max(signal_cone[i:i+rolling_maximum_length]) for i in range(0, len(signal_cone) - rolling_maximum_length)]

new_freqency_started = []
for i in range(0, len(rolling_maximum)):
    if rolling_maximum[i] < 1.10e+3:
        new_freqency_started.append(i)

print(new_freqency_started)

plt.plot([i for i in range(0, len(signal_cone))], signal_cone)
plt.plot([i for i in range(0, len(rolling_maximum))], rolling_maximum)
plt.plot([i for i in range(0, len(rolling_maximum))], [1.10e+3 for i in range(0, len(rolling_maximum))])

for i in range(0, len(new_freqency_started)):
    plt.plot([new_freqency_started[i] for j in range(0, len(rolling_maximum))], [j for j in range(0, len(rolling_maximum))])
plt.show()


