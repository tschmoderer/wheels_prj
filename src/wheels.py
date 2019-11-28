
class WHEEL:
    """
    define by a polar equation r = f(theta)
    """
    def __init__(self, r = 1, theta = 0):
        self._r = r
        self._theta = theta

    def _get_r(self):
        return self._r

    def _get_theta(self):
        return self._theta

    def _set_r(self, _r_new):
        self._r = _r_new
    
    def _set_theta(self, _theta_new):
        self._theta = _theta_new


    r     = property(_get_r, _set_r)
    theta = property(_get_theta, _set_theta)