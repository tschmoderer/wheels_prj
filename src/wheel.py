from curve import *

class WHEEL(CURVE): 
    _theta0 = -np.pi/2.
    __default_t  = np.linspace(0., 1., 11)
    __default_x1 = np.linspace(0., 1., 11)
    __default_x2 = -np.ones(11)

    def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2, tpe = CURVE._cartesian):
    #    if not tpe == CURVE._cartesian:
    #        r, theta = x1, x2
    #        x1 = r * np.cos(theta)
    #        x2 = r * np.sin(theta)
        print("Warning: Curve is given in polar coordinates")
        CURVE.__init__(self, t, x1, x2, tpe = CURVE._polar)

    # """
    # Rotate the wheel by angle alpha
    # """
    # def rotate(self, alpha):
    #     x0, y0 = self.x1, self.x2
    #     alpha = alpha - WHEEL._theta0
    #     self.x1 =  np.cos(alpha) * x0 + np.sin(alpha) * y0
    #     self.x2 = -np.sin(alpha) * x0 + np.cos(alpha) * y0

    # """
    # translate the wheel along x axis
    # """
    # def translate(self, delta):
    #     self.x1 = self.x1 + delta
