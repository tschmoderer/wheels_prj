import numpy as np 

def derivate(t, x, y):
    # error here
    dx = np.gradient(x) 
    dt = np.gradient(t)
    dx = np.gradient(x) / np.gradient(t)
    return - dx / y

def periodic_cos(t, n): 
    return -np.sqrt(1 + np.square(n)) + np.cos(t)

class ROAD:
    """Class defining a road: 
    - discrete values (t, x(t), y(t))
    - """

    def __init__(self, t, x1, x2):
        self._t = t 
        self._x = x1
        self._y = x2
        self._deriv = derivate(t, x1, x2)

    def _plot_(self):
        pass

    def _from_wheel(self, w):
        pass
    
    def __repr__(self):
        return ""
    
    def __str__(self):
        return ""
    
    def _get_x(self):
        return self._x
    
    def _get_t(self):
        return self._t
        
    def _set_x(self, x_new): 
        self._x = x_new
    
    def _get_y(self):
        return self._y

    def _get_deriv(self):
        return self._deriv
        
    def _set_y(self, y_new): 
        self._y = y_new    
    
    def _set_t(self, _t_new):
        self._t = _t_new


    t = property(_get_t, _set_t)
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    deriv = property(_get_deriv)