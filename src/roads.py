import numpy as np 
import matplotlib.pyplot as plt

""" Create a road for a periodic wheel """
def periodic_cos(t, n): 
    return ROAD(t = t, x1 = t, x2 = -np.sqrt(1 + np.square(n)) + np.cos(t))

def cycloidal(t, n):
    return ROAD(t = t, x1 = t + np.sin(t), x2 = np.cos(t) - 1 - 2*np.square(n)/(2*n + 1))

class ROAD:
    """ Default Values """
    __default_t = np.linspace(0., 1., 11)
    __default_x = np.linspace(0., 1., 11)
    __default_y = - np.ones(11)

    """
    Class defining a road: 
    - discrete values (t, x(t), y(t))
    """
    def __init__(self, t = __default_t, x1 = __default_x, x2 = __default_y):
        self.__t = t 
        self.__x = x1
        self.__y = x2

    # private 


    def plot(self, fig = None):
        xmin, xmax = np.amin(self.__x) - 2, np.amax(self.__x) + 2
        ymin, ymax = np.amin(self.__y) - 2, np.amax(self.__y) + 2
        
        ## Plot the road 
        if fig == None:
            fig = plt.subplot(111, xlim = (xmin, xmax), ylim = (ymin, ymax))
            fig.grid()
        
        fig.plot(self.__x, self.__y)

        ## TODO: Plot the extended road 
        return fig
    
    # Getters 
    def __get_t(self):
        return self.__t

    def __get_x(self):
        return self.__x

    def __get_y(self):
        return self.__y   

    def __get_xy(self): 
        return np.vstack((self.__x, self.__y))
    
    def __get_txy(self): 
        return np.vstack((self.__t, self.__x, self.__y))
    
    # Setters   
    # Warning: Assume keep the same space curve
    def __set_t(self, _t_new):
        self.__t = _t_new

    # Warning: Assume keep the same time discretization and y coordinate
    def __set_x(self, _x_new): 
        self.__x = _x_new
    
    # Warning: Assume keep the same time discretization and x coordinate
    def __set_y(self, _y_new): 
        self.__y = _y_new   

    # Warning: Assume keep the same time discretization
    def __set_xy(self, _x_new, _y_new):
        self.__x = _x_new
        self.__y = _y_new

    def __set_txy(self, _t_new, _x_new, _y_new):
        self.__t = _t_new
        self.__x = _x_new
        self.__y = _y_new

    # public
    t   = property(__get_t, __set_t)
    x   = property(__get_x, __set_x)
    y   = property(__get_y, __set_y)
    xy  = property(__get_xy, __set_xy)
    txy = property(__get_txy, __set_txy)

if __name__ == "__main__":
    pass