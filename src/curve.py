
class CURVE:
	"""
	either (t, x(t), y(t))
	or (t, r(t), theta(t))
	"""
	def __init__(self):
		self.__is_cartesian = True
		self.__is_polar = False 
		self.__t = t
		

class ROAD(CURVE):
	"""
	A road is a curve such that x(t[0]) = 0, and y(t) < 0
	"""
	pass
	
class WHEEL(CURVE): 
