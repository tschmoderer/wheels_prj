from curve import *

## TODO: overload plot method to plot the extended road 
class ROAD(CURVE):
	"""
	A road is a curve such that x(t[0]) = 0, and y(t) < 0
	A road is given in cartesian coordinates
	"""

	__default_t  = np.linspace(0., 1., 11)
	__default_x1 = np.linspace(0., 1., 11)
	__default_x2 = -np.ones(11)

	def __init__(self, t = __default_t, x1 = __default_x1, x2 = __default_x2, tpe = CURVE._cartesian):
		if not x1[0] == 0:
			print("Warning: road begin at x(t0)=0, rescaling x")
			x1 = x1 - x1[0]

		CURVE.__init__(self, t, x1, x2, tpe)

		try: 
			for n in range(len(self.x2)):
				assert(self.x2[n] < 0)
		except AssertionError:
			print("Warning:the road must lies below zero")
			traceback.print_exc()

	"""
	overload plot method from curve
	Road is extended -x_max/2 to the left
	#TODO: change to call the mother function 
	"""
	def plot(self, fig = None):
		x, y = self.x1, self.x2

		if self.type == CURVE._polar: 
			print("Warning: converting to cartesian plot")
			x = x * np.cos(y)
			y = x * np.sin(y)	
			
		dx = x[1]-x[0]
		x_max = x[-1]
		nbx = np.floor(3*x_max/(2*dx))
		new_x = np.linspace(-x_max/2., x_max, nbx)
		new_y = np.zeros(len(new_x))
		f = interp1d(x, y)
		for n in range(len(new_x)):
			if new_x[n] >= 0:
				new_y[n] = f(new_x[n])
			else: 
				new_y[n] = f(-new_x[n])

		# Plot
		x, y = new_x, new_y
		
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
