import numpy as np
import wave
import struct
from matplotlib import pyplot as plt

freq = 10            
data_size = 1000      # number of sample
fname = 'ehsan.wave'
frate = 1000          # sample frequency
amp = 1              # amplitude
time = [t/frate for t in range(data_size)] # time = 0:1/frate:1 (sec)

sine_list_x = []
for x in range(data_size):
    sine_list_x.append(amp*np.sin(2*np.pi*freq*(x/frate)) )
# another way
# sine_list_x = [np.sin(2*np.pi*freq*(x/frate) for x in range(data_size)]

plt.figure(1,None,None,'g')
plt.plot(time,sine_list_x)
plt.show()
plt.axes()