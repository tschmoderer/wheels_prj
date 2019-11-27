import os
import math
import numpy as np 
import scipy.integrate as integrate 
import matplotlib.pyplot as plt
from roads import *
from wheels import *

r1 = ROAD()
w1 = WHEEL()

t = np.linspace(0, 10, 100)
theta = np.linspace(0, 2*np.pi, 100) 

plt.plot(r1.x(t), r1.y(t))
plt.show()

plt.polar(theta, w1.r(theta))
plt.show()