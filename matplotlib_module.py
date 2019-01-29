from matplotlib import pyplot as plt
import numpy as np
import wave
import sys

spf = wave.open('ehsan.wav','r')
print
signal = spf.readframes(spf.getnframes())
signal = np.fromstring(signal,'int16')
plt.figure(1)
plt.title('signal wave ehsan.wav')
plt.plot(signal)
plt.show()
