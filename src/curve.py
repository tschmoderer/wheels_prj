import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.interpolate import interp1d
from scipy.integrate import odeint

import traceback

# TODO: bezier curve, 
# TODO: fourier curve
# TODO: 3d curve,

# Solve when t[0] |= 0
# first begin with road with obligation to start from 0

class CURVE:
	"""
	Class define a curve in the plane as a set of three data: 
		- (t, x(t), y(t))
		- # TODO: x(t) and y(t) can be callable
	"""
	
	_cartesian = True
	_polar     = False

	__default_t  = np.linspace(0., 1., 11)
	__default_x1 = np.linspace(0., 1., 11)
	__default_x2 = np.zeros(11)

	def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2, tpe = _cartesian):
		self.t    = t
		self.x1   = x1
		self.x2   = x2
		self.type = tpe

	"""
	Plot the curve 
	"""
	def plot(self, fig = None):
		x,y = self.x1, self.x2
		if self.type == CURVE._polar: 
			print("Warning: converting to cartesian plot")
			x = x * np.cos(y)
			y = x * np.sin(y)

		xmin, xmax = np.amin(x)*1.1, np.amax(x)*1.1
		ymin, ymax = np.amin(y)*1.1, np.amax(y)*1.1
        
        ## Plot the road 
		if fig == None:
			fig = plt.figure()
			ax = fig.add_subplot(111, autoscale_on = False, xlim = (xmin, xmax), ylim = (ymin, ymax))
			ax.grid()
		else: 
			curr_xmin, curr_xmax = plt.xlim()
			curr_ymin, curr_ymax = plt.ylim()
			plt.xlim(min(curr_xmin, xmin), max(curr_xmax, xmax))
			plt.ylim(min(curr_ymin, ymin), max(curr_ymax, ymax))
        
		plt.plot(x, y)
		return fig

	"""
	Convert to cartesian coordinates
	"""
	def polar2cartesian(self):
		try:
			assert(self.type == CURVE._polar)
			r, theta = self.x1, self.x2
			try: 
				for n in range(len(r)):
					assert(r[n] >= 0)
				self.x1 = r * np.cos(theta)
				self.x2= r * np.sin(theta)
				self.type = CURVE._cartesian
			except AssertionError:
				print("Error: your polar curve has negative radius.")
				traceback.print_exc()	
				exit(1)
		except AssertionError:
			print("Warning: the function is already in cartesian coordinates")
			traceback.print_exc()	
	
	"""
	Convert cartesian curve to polar
	"""	
	def cartesian2polar(self):
		try:
			assert(self.type == CURVE._cartesian)
			x, y = self.x1, self.x2
			self.x1 = np.sqrt(np.square(x) + np.square(y)) # new r
			for n in range(len(y)):
				if not x[n] == 0:
					self.x2[n] = np.arctan(y[n] / x[n]) # new theta
				else:
					if y[n] > 0:
						self.x2[n] == np.pi/2
					elif y[n] < 0:
						self.x2[n] == -np.pi/2
					else: # r == 0
						self.x2[n] == 0
			self.type = CURVE._polar

		except AssertionError:
			print("Warning: the curve is already in polar coordinates")
			traceback.print_exc()
	
	"""
	#TODO: compute the curvature 
	"""
	def curvature(self): 
		pass