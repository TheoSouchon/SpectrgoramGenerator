import wave 
import matplotlib.pyplot as plt 
import numpy as np 

obj= wave.open("okay-3.wav","rb")
sample_freq=obj.getframerate()
n_sample= obj.getnframes()
signal_wave = obj.readframes(-1)
obj_ch=obj.getnchannels()
obj_sampwidth = obj.getsampwidth()
print("#######",obj_ch,obj_sampwidth,sample_freq)
frames=obj.readframes(-1)
obj.close()

t_audio=n_sample/sample_freq

#print(t_audio)

signal_array= np.frombuffer(signal_wave,dtype=np.int32)
#print(len(signal_array))
times = np.linspace(0 ,t_audio,num=n_sample)
b =list(times)
a =list(times)
for i in b:
   ##print(i)
   a.append(i)
##print(len(a))
plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio Signal")

plt.ylabel("Signal Wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
plt.show()






new_obj = wave.open("new.wav","wb")
new_obj.setnchannels(2)
new_obj.setsampwidth(2)
new_obj.setframerate(44100)

new_obj.writeframes(frames)

new_obj.close()
