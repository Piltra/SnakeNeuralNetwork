


class Cabeza(Parte):

	def __init__(self, x, y, o):
		self._o = o
		super().__init__(x,y)


	@property
	def o(self)
		return self._o

	@o.setter
	def o(self, value):
		self._o = value

	@o.deleter
	def o(self):
		del self._o
