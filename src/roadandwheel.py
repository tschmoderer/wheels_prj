from road import *
from wheel import *

class ROADandWHEEL:
    __default_road  = ROAD()
    __default_wheel  = WHEEL()

    def __init__(self, **kwargs):
        try:
            self.road = kwargs.get('road')
            self.road2wheel()
        except:
            try:
                self.wheel = kwargs.get('wheel')
                self.wheel2road()
            except:
                exit()

    def road2wheel(self):
        road = self.road

        time = road.t
        x = road.x1
        y = road.x2

        dt = np.gradient(time)
        dx = np.gradient(x)

        f =  -(dx/dt)/y
        df = lambda y, t: np.interp(t, time, f)

        theta  = np.reshape(odeint(df, WHEEL._theta0, time) , len(time))
        R = -y 

        self.wheel = WHEEL(t = time, x1 = R, x2 = theta)

    def wheel2road(self):
        wheel = self.wheel
        time, r, theta = wheel.t, wheel.x1, wheel.x2

        df = lambda y, t: np.interp(t, theta, r)

        new_x = np.reshape(odeint(df, 0, theta) , len(theta))
        new_y = -r
        self.road = ROAD(t = time, x1 = new_x, x2 = new_y)

    def plot(self): 
        fig = self.road.plot()
        fig = self.wheel.plot(fig)
        return fig 

    """
    Define a road by a periodic extension of values, 
        - (t, y(t)): de prexisting road, 
        - n : number of period
    """
    def periodise_road(self, period = 2):
        try:
            assert(self.road.type == CURVE._cartesian)
        except AssertionError:
            exit()
        
        t, x, y = self.road.t, self.road.x1, self.road.x2
        f = interp1d(x, y)

        length = x[-1] - x[0]

        nbt   = len(t)
        new_t = np.linspace(t[0], t[-1]*period, period*nbt)

        nbx   = len(x)
        new_x = np.linspace(x[0], x[-1]*period, period*nbx)

        new_y = f( ((new_x) % length) +  x[0])
        self.road = ROAD(t = new_t, x1 = new_x, x2 = new_y)   

    def animate(self):
        road, wheel = self.road, self.wheel

        xmin, xmax = np.amin(road.x1)*1.1, np.amax(road.x1)*1.1
        ymin, ymax = np.amin(wheel.x2)*1.1, np.amax(wheel.x2)*1.1  

        ## Define the figure, 
        fig = plt.figure()
        ax  = fig.add_subplot(111, autoscale_on = False, xlim = (xmin, xmax), ylim = (ymin, ymax))

        plt.axis('equal')
        ax.grid()

        ## Plot the road 
        plt.plot(road.x1, road.x2)
        ROAD0 = road.x2[0]

        ## Plot the wheel
        t     = wheel.t
        R     = wheel.x1
        theta = wheel.x2

        x0 = R * np.cos(theta)
        y0 = R * np.sin(theta)

        plt.plot(x0, y0)

        ## Define the dynamics part
        lines = []

        ### The wheel
        line, = ax.plot([], [], '-', lw = 1)
        lines.append(line)

        ### The center of the wheel
        line, = ax.plot([], [], 'ro')
        lines.append(line)

        ### The initial point 
        line, = ax.plot([], [], 'bo')
        lines.append(line)

        ### The trace of the initial wheel
        line, = ax.plot([], [], 'b-')
        lines.append(line)

        ## Number of frames
        nb_frames = len(road.t) 

        # fonction à définir quand blit=True
        # crée l'arrière de l'animation qui sera présent sur chaque image
        def init():
            lines[3].set_data([],[])
            return lines

        def animate(i): 
            time  = t[i]
            alpha = theta[i] - WHEEL._theta0

            # compute the wheel
            x1 =  np.cos(alpha) * x0 + np.sin(alpha) * y0 + time
            y1 = -np.sin(alpha) * x0 + np.cos(alpha) * y0 

            ## Plot the wheel
            lines[0].set_data(x1, y1)

            ## Plot the center
            lines[1].set_data(time, 0)
            
            ## Plot the initial point 
            in_x = np.sin(alpha)*ROAD0 + time
            in_y = np.cos(alpha)*ROAD0
            lines[2].set_data(in_x, in_y)

            ## Plot the trace of the initial point 
            lines[3].set_xdata(np.append(lines[3].get_xdata(), in_x))
            lines[3].set_ydata(np.append(lines[3].get_ydata(), in_y))

            return lines

        animation.FuncAnimation(fig, animate, frames = nb_frames, blit = True, init_func = init, repeat = True, interval = 50)
        plt.show()

# """
# Define a road such that the wheel is closed and period = n 
# The cartesian equation of the road is
# y = d + b*cos(c*x)
# avec d = -sqrt(b^2 + n^2/c^2)
# """
# def cos_road(t, n, b = 1, c = 1): 
# 	d = -np.sqrt(np.square(b) + np.square(n)/np.square(c))
# 	return ROAD(t = t, x1 = t, x2 = d + b*np.cos(c*t))

# """
# Define a road 
# """
# def cycloidal_road(t, n):
#     return ROAD(t = t, x1 = t + np.sin(t), x2 = np.cos(t) - 1 - 2*np.square(n)/(2*n + 1))

# """
# Define a road by a periodic extension of values, 
# 	- (t, y(t)): de prexisting road, 
# 	- n : number of period
# """
# def periodic_road(t, y, n = 2):
# 	f = interp1d(t, y) 
# 	nbt = len(t)
# 	period = t[-1] - t[0]
# 	offset = t[-1]
# 	new_t = np.linspace(t[0], t[-1]*n, n*nbt)
# 	new_y = f( ((new_t) % period) +  t[0])
# 	return ROAD(t = new_t, x1 = new_t, x2 = new_y)

# """ 
# Define the road for an n-gon wheel
# """
# def ngon_road(nbt = 100, n = 4, period = 5):
# 	t0 = np.arcsinh(np.tan(np.pi / n))
# 	t = np.linspace(-t0, t0, np.floor(nbt/n))
# 	y = -np.cosh(t)
# 	return periodic_road(t, y, n = period)



# def animate(road, wheel, fig = None):
# 	if fig == None:
# 		fig = road.plot()
# 		fig = wheel.plot(fig)
	
# 	t      = road.t
# 	theta  = np.arctan(wheel.y / wheel.x)
# 	theta0 = -np.pi/2. 
# 	ROAD0  = (road.y)[0]

# 	## Define the dynamics part
# 	lines = []

# 	### The wheel
# 	line, = plt.plot([], [], '-', lw = 1)
# 	lines.append(line)

# 	### The center of the wheel
# 	line, = plt.plot([], [], 'ro')
# 	lines.append(line)

# 	### The initial point 
# 	line, = plt.plot([], [], 'bo')
# 	lines.append(line)

# 	### The trace of the initial wheel
# 	line, = plt.plot([], [], 'b-')
# 	lines.append(line)

# 	## Number of frames
# 	nb_frames = len(t)

# 	def init():
# 		lines[3].set_data([],[])
# 		return lines
	
# 	def animate(i): 
# 		time  = t[i]
# 		alpha = theta[i]

# 		# compute the wheel
# 		# wheel.rotate(alpha)
# 		wheel.translate(time)

# 		## Plot the wheel
# 		lines[0].set_data(wheel.x, wheel.y)

# 		## Plot the center
# 		lines[1].set_data(time, 0)

# 		## Plot the initial point 
# 		in_x = np.sin(alpha-theta0)*ROAD0 + time
# 		in_y = np.cos(alpha-theta0)*ROAD0
# 		lines[2].set_data(in_x, in_y)

# 		## Plot the trace of the initial point 
# 		lines[3].set_xdata(np.append(lines[3].get_xdata(), in_x))
# 		lines[3].set_ydata(np.append(lines[3].get_ydata(), in_y))

# 		return lines
# 	animation.FuncAnimation(fig, animate, frames = nb_frames, blit = True, init_func = init, repeat = True, interval = 50)
# 	plt.show()