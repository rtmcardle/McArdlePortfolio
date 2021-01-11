from __future__ import division
from math import *
from scipy import *
import matplotlib.pyplot as plt
from numpy import linspace
 

f=[0,1]
phi=[0,1]
i=1
  
while (abs((phi[i]-phi[i-1]))>10**-20) or (i<7):
    f.append(f[i]+f[i-1])
    print ("f_"+str(i)+": "+str(f[-1]))
    phi.append(f[-1]/f[-2])
    print ("phi_"+str(i)+": "+str(phi[-1]))
    print ()
    i+=1

print ("i: "+str(i))

plt.figure(1)
plt.subplot(211)
plt.plot(linspace(0,i,i+1), f, 'ro')
plt.yscale('log')

plt.subplot(212)
plt.plot(linspace(0,i,i+1), phi, 'bo')
plt.axis([20,i,phi[20],phi[21]])
#ply.xaxis()

plt.show()