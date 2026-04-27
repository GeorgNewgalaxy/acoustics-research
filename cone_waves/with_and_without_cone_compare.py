from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

with_cone_file = open("pedal_1_max_hold.txt")
with_cone = with_cone_file.read()
with_cone_file.close()
with_cone_split = with_cone.split(", ")
with_cone = [float(with_cone_split[i]) for i in range(0, len(with_cone_split))]

without_cone_file = open("pedal_2_max_hold.txt")
without_cone = without_cone_file.read()
without_cone_file.close()
without_cone_split = without_cone.split(", ")
without_cone = [float(without_cone_split[i]) for i in range(0, len(without_cone_split))]

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

samplerate_cone, data_cone = wavfile.read("with_cone.wav")
length_cone = data_cone.shape[0] / samplerate_cone
samples_cone = int(length_cone*samplerate_cone)

samplerate_coneless, data_coneless = wavfile.read("without_cone.wav")
length_coneless = data_coneless.shape[0] / samplerate_coneless
samples_coneless = int(length_coneless*samplerate_coneless)

# data_cone = data_cone[0:int(0.5*len(data_cone))]
# data_coneless = data_cone[0:int(0.5*len(data_coneless))]

seconds_per_part = 0.1
samples_per_part_cone = (seconds_per_part/length_cone)*samples_cone
samples_per_part_coneless = (seconds_per_part/length_coneless)*samples_coneless

fft_freqs_cone = np.fft.fftfreq(int(samples_per_part_cone), d=1/samplerate_cone)
fft_freqs_coneless = np.fft.fftfreq(int(samples_per_part_coneless), d=1/samplerate_coneless)

least_size_cone = min(len(fft_freqs_cone), len(with_cone)) - 1
least_size_coneless = min(len(fft_freqs_coneless), len(without_cone)) - 1


# plt.plot(fft_freqs_cone[0:least_size_cone], with_cone[0:least_size_cone], label="With cone")
# plt.plot(fft_freqs_coneless[0:least_size_coneless], without_cone[0:least_size_coneless], label="Without cone")

all_tones = [frequency/tones for frequency in range(int(tone_min*tones), int(tone_max*tones + tones), int(tone_max - tone_min))]

factor = 1
real_fft_freqs = ["NOPE"]
if len(fft_freqs_cone) < len(fft_freqs_coneless):
    minimal_array = [factor*with_cone[i]/without_cone[i] for i in range(0, least_size_cone)]
    real_fft_freqs = fft_freqs_cone.copy()
    plt.plot(fft_freqs_cone[0:least_size_cone], minimal_array, label=f'With cone/Without cone (x{factor})')
else:
    minimal_array = [factor*with_cone[i]/without_cone[i] for i in range(0, least_size_coneless)]
    real_fft_freqs = fft_freqs_coneless.copy()
    plt.plot(fft_freqs_coneless[0:least_size_coneless], minimal_array, label=f'With cone/Without cone (x{factor})')

plt.legend()
plt.show()

idx = -1
for i in range(0, len(real_fft_freqs)):
    if real_fft_freqs[i] == 440:
        idx = i
print(idx)
print(minimal_array[idx])
