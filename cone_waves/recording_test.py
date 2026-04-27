import sounddevice as sd
import numpy as np
from time import *

sleep(15)
print(sd.query_devices()[0])

samplerate = 44100  # samples per second
duration = 10  # seconds to record
channels = 1  # mono audio
device_index = 0  # Replace with your identified input device index

print(f"Recording for {duration} seconds...")
audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=channels, dtype='float32', device=device_index)
sd.wait()  # Wait until recording is finished
print("Recording complete.")

# 'audio_data' now contains the sampled audio as a NumPy array
# You can process or save this data as needed.
# For example, to save it to a WAV file:
import soundfile as sf
sf.write('python_rec_1.wav', audio_data, samplerate)

print(f"Recording for {duration} seconds...")
audio_data = sd.rec(int(samplerate * duration), samplerate=samplerate,
                    channels=channels, dtype='float32', device=device_index)
sd.wait()  # Wait until recording is finished
print("Recording complete.")

# 'audio_data' now contains the sampled audio as a NumPy array
# You can process or save this data as needed.
# For example, to save it to a WAV file:
sf.write('python_rec_2.wav', audio_data, samplerate)