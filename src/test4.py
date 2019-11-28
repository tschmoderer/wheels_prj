import matplotlib.pyplot as plt
from roads import *

t = np.linspace(0., 10., 101)
x = -np.sin(t)+(1/2)*np.sin(2*t)
y = -np.cos(t)

r1 = ROAD(t = t, x1 = x, x2 = y)
r1 = cycloidal(t, 4)

fig = r1.plot()
plt.show()
 