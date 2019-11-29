import numpy as np
from scipy.integrate import odeint
from scipy.interpolate import interp1d


def polar2cartesian(r, t):
    x = r * np.cos(t)
    y = r * np.sin(t)
    return np.vstack((x,y))

def road2wheel(road):

    df = - ( np.gradient(road.x) / np.gradient(road.t) )/ road.y
    f = lambda y, t: np.interp(t, road.t, df)
    
    t0 = road.t[0]
    x0 = road.x[0]

    theta = integrate.odeint(f, -np.pi/2, road.t)
    R     = -road.y

    return wheel

def wheel2road(wheel):
    return road
