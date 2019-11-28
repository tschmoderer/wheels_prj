import os
import math
import numpy as np 
import scipy.integrate as integrate 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from roads import *
from wheels import *

def road2wheel(road):
    df = lambda x, tt: np.interp(tt, road.t, road.deriv)
    w = WHEEL()
    w.theta  = np.reshape(integrate.odeint(df, -np.pi/2, road.t) , len(t))
    w.r      = -road.y
    return w

t = np.linspace(0, 60, 1001)
y = -np.sqrt(2) + np.cos(t)
y = -1.887365 - (2./3.)*np.cos(t) + np.sin(t) - 0.5*np.sin(2.*t)

r1 = ROAD(t = t, x1 = t, x2 = y)
w1 = road2wheel(r1)

## Define the figure, 
xmin = np.amin(r1.x) - 2
xmax = np.amax(r1.x) + 2
ymin = np.amin(r1.y) - 2
ymax = np.amax(r1.y) + 2 

fig = plt.figure()
ax  = fig.add_subplot(111, autoscale_on = False, xlim = (xmin, xmax), ylim = (ymin, ymax))
plt.axis('equal')
ax.grid()

## Plot the road 
plt.plot(r1.x, r1.y)

## Plot the wheel
x0 = w1.r * np.cos(w1.theta)
y0 = w1.r * np.sin(w1.theta)

plt.plot(x0, y0)

## Define the dynamics part
lines = []

### The wheel
line, = ax.plot([], [], '-', lw = 1)
lines.append(line)

### The center of the wheel
line, = ax.plot([], [], 'ro')
lines.append(line)

### The initial point 
line, = ax.plot([], [], 'bo')
lines.append(line)

### The trace of the initial wheel
line, = ax.plot([], [], 'b-')
lines.append(line)

## Number of frames
nb_frames = 1000

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    lines[3].set_data([],[])
    return lines

def animate(i): 
    time = t[i]
    ROAD0 = r1.y[0]
    theta0 = -np.pi/2
    alpha = w1.theta[i]

    # compute the wheel
    x1 =  np.cos(alpha-theta0) * x0 + np.sin(alpha-theta0) * y0 + time
    y1 = -np.sin(alpha-theta0) * x0 + np.cos(alpha-theta0) * y0 

    ## Plot the wheel
    lines[0].set_data(x1, y1)

    ## Plot the center
    lines[1].set_data(time, 0)
    
    ## Plot the initial point 
    in_x = np.sin(alpha-theta0)*ROAD0 + time
    in_y = np.cos(alpha-theta0)*ROAD0
    lines[2].set_data(in_x, in_y)

    ## Plot the trace of the initial point 
    lines[3].set_xdata(np.append(lines[3].get_xdata(), in_x))
    lines[3].set_ydata(np.append(lines[3].get_ydata(), in_y))

    return lines

anim = animation.FuncAnimation(fig, animate, frames = nb_frames, blit = True, init_func = init, repeat = True, interval = 50)
plt.show()



