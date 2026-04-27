import sounddevice as sd
import numpy as np
import soundfile as sf
from time import *


print(sd.query_devices())

samplerate = 44100
duration_of_recording = 4
channels = 1
recorder_device_index = 0
playback_device_index = 1

t = np.linspace(0, duration_of_recording, int(duration_of_recording*samplerate), endpoint=False)
tone = ((0.05 * np.sin(2 * np.pi * 440 * t)).astype(np.float32))#.reshape((len(t), 1))

print(f"Recording for {duration_of_recording} seconds...")
sd.play(tone, samplerate, device=playback_device_index)
audio_data = sd.rec(int(samplerate * duration_of_recording), samplerate=samplerate, channels=channels, dtype='float32', device=recorder_device_index)
sd.wait()

print("Recording complete.")
sf.write('python_rec_1.wav', audio_data, samplerate)

processed_audio_data = audio_data.reshape(len(audio_data))


t = np.linspace(0, len(audio_data)/samplerate, len(audio_data), endpoint=False)
tone = ((0.05 * np.sin(2 * np.pi * 440 * t)).astype(np.float32))#.reshape((len(t), 1))
new_data = processed_audio_data# + tone


sleep(3)
sd.play(new_data, samplerate, device=playback_device_index)
sd.wait()
