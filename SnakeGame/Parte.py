


class Parte:


	def __init__(self, x, y):
		self._coord = Coord(x,y)

"""
https://docs.python.org/3/library/functions.html#property
Aquí está el porqué utilizar el @property

"""

	@property
	def coord(self):
		return self._coord
	
	@coord.setter
	def coord(self, x, y):
		self._coord = Coord(x,y)

	@coord.deleter
	def coord(self):
		del self._coord