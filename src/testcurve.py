from curve import *
import unittest

class CurveTest(unittest.TestCase):

    def test_curve(self):
        c1 = CURVE()
        c1.cartesian2polar()
        c1.plot()
        c1.polar2cartesian()
        c1.plot()

unittest.main()