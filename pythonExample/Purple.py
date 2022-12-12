import librosa
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from numpy.fft import *
import math
import wave
import struct
from scipy.io import wavfile

x, sr = librosa.load('notesMusiques/gamme.wav', sr=None)
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.show()