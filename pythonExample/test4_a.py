import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from numpy.fft import *
import math
import wave
import struct
from scipy.io import wavfile

x, sr = librosa.load('okay-3.wav', sr=None)

window_size = 1024
hop_length = 512 
n_mels = 128
time_steps = 384 

window = np.hanning(window_size)
stft= librosa.core.spectrum.stft(x, n_fft = window_size, hop_length = hop_length, window=window)
out = 2 * np.abs(stft) / np.sum(window)

plt.figure(figsize=(12, 4))
ax = plt.axes()
plt.set_cmap('hot')
librosa.display.specshow(librosa.amplitude_to_db(out, ref=np.max), y_axis='log', x_axis='time',sr=sr)
plt.savefig('spectrogramA.png', bbox_inches='tight', transparent=True, pad_inches=0.0 )