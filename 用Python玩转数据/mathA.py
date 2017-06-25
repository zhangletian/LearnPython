import numpy as np
import pylab as pl
import pygal

#x = np.linspace(-np.pi,np.pi,256)
#s = np.sin(x)
#c = np.cos(x)
#pl.title('Trigonometric Function')
#pl.xlabel('X')
#pl.ylabel('Y')
#pl.plot(x,s)
#pl.plot(x,c)

import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,256)
s = np.sin(x)
c = np.cos(x)
plt.title('Trigonometric Function')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x,s)
plt.plot(x,c)
plt.show()
