import matplotlib.pyplot as plt
from curve import *

t = np.linspace(0., 10., 101)
x = -np.sin(t)+(1/2)*np.sin(2*t)
y = -np.cos(t)

r1 = ROAD(t = t, x1 = x, x2 = y)
x = -np.sin(t)+(1/2)*np.sin(2*t)
y = -np.cos(t)

r2 = ROAD(t = t, x1 = 0.5*x, x2 = 2*y-5)
# r1 = cycloidal(t, 4)

# fig = r1.plot()
# fig = r2.plot(fig=fig)
# plt.show()
 
t = np.linspace(-np.arcsinh(1), np.arcsinh(1), 100)
y = -np.cosh(t-1)


r3 = periodic_road(t, y, n = 10)
fig = r3.plot()

w3 = road2wheel(r3)
fig = w3.plot(fig)

plt.show()

r4 = ngon_road(n=3)
r4.plot()
plt.show()