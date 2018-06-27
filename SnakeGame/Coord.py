

class Coord:
	def __init__(self,x,y):
		self._x = x
		self._y = y

	@property
	def x(self)
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@x.deleter
	def x(self):
		del self._x

	@property
	def y(self)
		return self._y

	@y.setter
	def y(self, value):
		self._y = value

	@y.deleter
	def y(self):
		del self._y