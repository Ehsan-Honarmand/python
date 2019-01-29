import numpy
from matplotlib import pyplot as plt
s = numpy.fromstring(b'\x00\x0a\x0f\x02','int8')
print(s)
plt.figure(1)
plt.show()