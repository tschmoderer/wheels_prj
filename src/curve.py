import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.integrate import odeint

# Solve when t[0] |= 0
# first begin with road with obligation to start from 0

class CURVE:
	"""
	Class define a curve in the plane as a set of three data: 
		- (t, x(t), y(t)) 
	"""

	__default_t  = np.linspace(0., 1., 11)
	__default_x1 = np.linspace(0., 1., 11)
	__default_x2 = np.zeros(11)

	def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2):
		self.__t = t
		self.__x = x1
		self.__y = x2
		self.__is_cartesian = True

	def plot(self, fig = None):
		if not self.__is_cartesian: 
			print("Warning: converting to cartesian plot")
			self.polar2cartesian()

		xmin, xmax = np.amin(self.__x) - 2, np.amax(self.__x) + 2
		ymin, ymax = np.amin(self.__y) - 2, np.amax(self.__y) + 2
        
        ## Plot the road 
		if fig == None:
			fig = plt.subplot(111, xlim = (xmin, xmax), ylim = (ymin, ymax))
			fig.grid()
		else: 
			curr_xmin, curr_xmax = plt.xlim()
			curr_ymin, curr_ymax = plt.ylim()
			plt.xlim(min(curr_xmin, xmin), max(curr_xmax, xmax))
			plt.ylim(min(curr_ymin, ymin), max(curr_ymax, ymax))
        
		fig.plot(self.__x, self.__y)

        ## TODO: Plot the extended road 
		return fig

	def polar2cartesian(self):
		try:
			assert(self.is_cartesian)
			r = self.__x
			theta = self.__y
			try: 
				for n in range(len(r)):
					assert(r[n] >= 0)
				self.__x = r * np.cos(theta)
				self.__y = r * np.sin(theta)
				self.__is_cartesian = True
			except AssertionError:
				print("Error your polar curve has negative radius.")
				exit(1)
		except AssertionError:
			print("Warning the function is already cartesian!")

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

	def __get_is_cartesian(self):
		return self.__is_cartesian

	def __get_is_polar(self):
		return not self.__is_cartesian
    
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

	def __set_is_cartesian(self):
		self.__is_cartesian = True

	def __set_is_polar(self):
		self.__is_cartesian = False

    # public
	t   = property(__get_t, __set_t)
	x   = property(__get_x, __set_x)
	y   = property(__get_y, __set_y)
	xy  = property(__get_xy, __set_xy)
	txy = property(__get_txy, __set_txy)	
	is_cartesian = property(__get_is_cartesian, __set_is_cartesian)
	is_polar = property(__get_is_polar, __set_is_polar)	

class ROAD(CURVE):
	"""
	A road is a curve such that x(t[0]) = 0, and y(t) < 0
	"""

	__default_t  = np.linspace(0., 1., 11)
	__default_x1 = np.linspace(0., 1., 11)
	__default_x2 = -np.ones(11)

	def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2, cartesian = True):
		CURVE.__init__(self, t, x1, x2)

		if not cartesian: 
			self.__set_is_polar()
			self.polar2cartesian()
		try: 
			for n in range(len(self.y)):
				assert(self.y[n] < 0)
		except AssertionError:
			print("Warning the road must lies below zero")
	
class WHEEL(CURVE): 
	__default_t  = np.linspace(0., 1., 11)
	__default_x1 = np.linspace(0., 1., 11)
	__default_x2 = -np.ones(11)

	def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2, cartesian = True):
		CURVE.__init__(self, t, x1, x2)
	

"""
Define a road such that the wheel is closed and period = n 
The cartesian equation of the road is
y = d + b*cos(c*x)
avec d = -sqrt(b^2 + n^2/c^2)
"""
def cos_road(t, n, b = 1, c = 1): 
	d = -np.sqrt(np.square(b) + np.square(n)/np.square(c))
	return ROAD(t = t, x1 = t, x2 = d + b*np.cos(c*t))

"""
Define a road 
"""
def cycloidal_road(t, n):
    return ROAD(t = t, x1 = t + np.sin(t), x2 = np.cos(t) - 1 - 2*np.square(n)/(2*n + 1))

"""
Define a road by a periodic extension of values, 
	- (t, y(t)): de prexisting road, 
	- n : number of period
"""
def periodic_road(t, y, n = 2):
	f = interp1d(t, y) 
	nbt = len(t)
	period = t[-1] - t[0]
	offset = t[-1]
	new_t = np.linspace(t[0], t[-1]*n, n*nbt)
	new_y = f( ((new_t) % period) +  t[0])
	return ROAD(t = new_t, x1 = new_t, x2 = new_y)

""" 
Define the road for an n-gon wheel
"""
def ngon_road(nbt = 100, n = 4, period = 5):
	t0 = np.arcsinh(np.tan(np.pi / n))
	t = np.linspace(-t0, t0, np.floor(nbt/n))
	y = -np.cosh(t)
	return periodic_road(t, y, n = period)

def road2wheel(road):
	time = road.t
	x = road.x
	y = road.y 

	dt = np.gradient(time)
	dx = np.gradient(x)

	f =  -(dx/dt)/y
	df = lambda y, t: np.interp(t, time, f)

	theta0 = -np.pi/2
	theta  = np.reshape(odeint(df, theta0, time) , len(time))
	R = -y 

	x1 = R * np.cos(theta)
	x2 = R * np.sin(theta)

	return WHEEL(t = time, x1 = x1, x2 = x2)

def animate(road, wheel, fig = None):
	if fig == None:
		fig = road.plot()
		fig = wheel.plot(fig)
	
