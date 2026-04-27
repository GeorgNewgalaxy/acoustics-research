from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

address = input("Address: ")

# cone stuff
samplerate_cone, data_cone = wavfile.read(address + ".wav")
length_cone = data_cone.shape[0] / samplerate_cone
samples_cone = int(length_cone*samplerate_cone)
# ---------------------------------------------------------
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

tone_step = (tone_max - tone_min)/tones
tones = [frequency/tones for frequency in range(int(tone_min*tones), int(tone_max*tones + tones), int(tone_max - tone_min))]

seconds_per_part = 0.1
samples_per_part = (seconds_per_part/length_cone)*samples_cone

max_frequencies = []
max_amplitudes = []

max_hold = [-1 for i in range(0, int(samples_per_part))]
fft_freqs = np.fft.fftfreq(int(samples_per_part), d=1/samplerate)


for timeframe_idx in range(0, int(length_cone/seconds_per_part - 1)):
    signal_cone = data_cone[int(timeframe_idx*samples_per_part):int((timeframe_idx + 1)*samples_per_part)]
    fft_result_cone = np.fft.fft(signal_cone)
    freq_cone = np.fft.fftfreq(len(signal_cone), d=1/samplerate)
    max_freq = max(fft_result_cone)
    for i in range(0, len(max_hold)):
        if fft_result_cone[i]/max_freq > 0.1:
            if fft_result_cone[i] > max_hold[i]:
                if tone_min <= fft_freqs[i] <= tone_max:
                    max_hold[i] = float(np.abs(fft_result_cone[i]))

# for i in range(0, len(max_hold)):
#     if max_hold[i] < 40000:
#         max_hold[i] = 1

plt.plot(fft_freqs, max_hold)
plt.show()

with_cone_max_hold = open(address + "_max_hold.txt", "x")
with_cone_max_hold.write(str(max_hold)[1:-1])
