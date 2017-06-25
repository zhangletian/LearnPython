import scipy as sp
import pylab as pl

#listA = sp.ones(500)
#listA[100:300] = -1
#f = sp.fft(listA)
#pl.plot(f)


import matplotlib.pyplot as plt

listA = sp.ones(500)
listA[100:300] = -1
f = sp.fft(listA)

plt.plot(f)
plt.show()
