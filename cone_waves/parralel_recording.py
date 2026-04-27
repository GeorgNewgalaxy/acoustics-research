from time import *
import sounddevice as sd
import soundfile as sf
import matplotlib.pyplot as plt

print(sd.query_devices())

samplerate = 44100  # samples per second
duration = 10  # seconds to record
channels = 1  # mono audio
device_index = 0  # Replace with your identified input device index

print("Recording")
audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=channels, dtype='float32', device=device_index)

sd.wait()
plt.plot(range(0, len(audio_data)), audio_data)

sf.write('parralel.wav', audio_data, samplerate)

print("Soon playback will start!")
sleep(5)
sd.play(audio_data, samplerate, device=1)

plt.show()
