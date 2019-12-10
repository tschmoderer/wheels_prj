import matplotlib.pyplot as plt
from curve import *
from road import *
from wheel import *
from roadandwheel import * 

t = np.linspace(-np.arcsinh(1), np.arcsinh(1), 100)
y = -np.cosh(t)

# t = np.linspace(0, 20, 100)
# y = -1.887365-(2/3)*np.cos(t)+np.sin(t)-(1/2)*np.sin(2*t)

r3 = ROAD(t = t, x1 = t, x2 = y)
# fig = r3.plot()
# plt.show()

theta = np.linspace(-np.pi/2,  3*np.pi/2, 500)
r = 4*np.sqrt(5-4*np.square(np.sin(theta)))

w1  = WHEEL(t = theta, x1 = r, x2=  theta, tpe=  CURVE._polar)
# fig = w1.plot(fig)

rw = ROADandWHEEL(road = r3)
rw.periodise_road(period = 5) 
rw.road2wheel()

rw = ROADandWHEEL(wheel = w1)
fig = rw.plot()
plt.show

rw.animate()

# r3 = periodic_road(t, y, n = 10)
# fig = r3.plot()

# w3 = road2wheel(r3)
# fig = w3.plot(fig)

plt.show()
