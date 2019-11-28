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
    wheel = WHEEL()
    wheel.theta  = np.reshape(integrate.odeint(df, -np.pi/2, road.t) , len(road.t))
    wheel.r      = -road.y
    return wheel

def wheel2road(wheel):
    dg = lambda x, tt: np.interp(tt, wheel.theta, wheel.r)
    road = ROAD()
    road.t = wheel.theta
    road.x = np.reshape(integrate.odeint(dg, 0, wheel.theta) , len(wheel.theta))
    road.y = -wheel.r
    road.deriv = derivate(road.t, road.x, road.y)
    return road

theta = np.linspace(-np.pi/2, 9*np.pi / 2, 101)
r     = 4*np.sqrt(5 - 4*np.square(np.sin(theta)))

w1 = WHEEL(r = r, theta = theta)
r1 = wheel2road(w1)

w1 = road2wheel(r1)

t = r1.t
dt = theta[1]- theta[0]

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
nb_frames = len(w1.theta)

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    lines[3].set_data([],[])
    return lines

def animate(i): 
    time   = t[i]
    ROAD0  = r1.y[0]
    theta0 = -np.pi/2
    alpha  = w1.theta[i]

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



