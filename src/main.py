import os
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# TODO: 
#    - Define ROAD class, 
#    - Define WHEEL class,


dt = 0.01

xmin = -2
xmax = 10
nbx  = 100

ymin = -3
ymax =  3

x = np.linspace(xmin, xmax, nbx)
ROAD = -1 * np.ones(len(x))

fig = plt.figure()
ax  = fig.add_subplot(111, autoscale_on = False, xlim = (xmin, xmax), ylim = (ymin, ymax))
ax.grid()

line, = ax.plot([], [], '-', lw = 1)

plt.plot(x, ROAD)

theta = np.linspace(0, 2*np.pi, 100)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line.set_data([],[])
    return line,

def animate(i): 
    t = i * dt
    x1 = [1. * np.cos(theta) + t]
    x2 = [1. * np.sin(theta)]
    line.set_data(x1, x2)
    return line,   
 
ani1 = animation.FuncAnimation(fig, animate, init_func = init, frames = 100, blit = False, interval = 20, repeat = False)
plt.show()