


class Manzana:

	def __init__(self, x, y):
		self._coord = Coord(x,y)


	@property
	def coord(self):
		return self._coord
	
	@coord.setter
	def coord(self, x, y):
		self._coord = Coord(x,y)

	@coord.deleter
	def coord(self):
		del self._coord