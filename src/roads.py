from wheels import * 

class ROAD:
    """Class defining a road: 
    - either: passing two lambda function t --> (x(t), y(t))
    - or, one function t --> y(t) 
    - optional you can provide the derivative of x(t)
    - """

    def __init__(self, x1 = lambda t: t, x2 = lambda t: [-1]*len(t), dx1 = lambda t: 1):
        self._x  = x1
        self._y  = x2
        self._dx = dx1

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
        
    def _set_x(self, x_new): 
        self._x = x_new
    
    def _get_y(self):
        return self._y
        
    def _set_y(self, y_new): 
        self._y = y_new    

    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)