# for data transformation 
import numpy as np 
# for visualizing the data 
import matplotlib.pyplot as plt 
# for opening the media file 
import scipy.io.wavfile as wavfile

Fs, aud = wavfile.read('okay-3.wav')
aud = aud[:,0] # select left channel only
first = aud[:int(Fs*125)] # trim the first 125 seconds

powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs) 
plt.show()
