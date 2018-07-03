


class Parte:


	def __init__(self, x, y):
		self._coord = Coord(x,y)

"""
https://docs.python.org/3/library/functions.html#property
Aquí está el porqué utilizar el @property

"""
	"""
	dir es la dirección en la que va a avanzar, un vector
	"""
	def avanza(self, dir):
		cc = self._coord
		self._coord.x(cc.x() + dir.x())
		self._coord.y(cc.y() + dir.y())

	@property
	def coord(self):
		return self._coord
	
	@coord.setter
	def coord(self, x, y):
		self._coord = Coord(x,y)

	@coord.deleter
	def coord(self):
		del self._coord