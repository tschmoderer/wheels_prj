
class WHEEL:
    """
    define by a polar equation r = f(theta)
    """
    def __init__(self, r = lambda t: [1]*len(t)):
        self._r = r

    def _get_r(self):
        return self._r

    def _set_r(self, _r_new):
        self._r = _r_new

    r = property(_get_r, _set_r)