
class ExceptionAcabaJuego(Exception):
	"""
	value es el mensaje de error en str
	"""
	def __init__(self,value):
		self.value = value

	"""
	https://stackoverflow.com/questions/7784148/understanding-repr-function-in-python
	"""
	def __str__(self):
		return repr(self.value)

class Tablero:

	"""
	width y height del tablero
	x e y posiciones del snake
	o orientación del snake

	"""
	def __init__(self, width, height, x, y, o):
		self._width = width
		self._height = height
		self._manzanas = []
		self._snake = Snake(x,y,o)


	"""
	No comprueba que hayan dos manzanas en un mismo sitio
	"""
	def generarManzana(self, x, y):
		self._manzanas.append(Manzana(x,y))



	"""
	Si hay dos manzanas o más solo se come una
	y pasa por encima de las otras
	"""
	def avanza(self):
		self._snake.avanza()
		cc = self._snake.coord()

		# Miramos si se ha salido del tablero.
		if cc.x() < 0 or cc.y() < 0 or cc.x() >= self._width or cc.y() >= self._height:
			raise ExceptionAcabaJuego("Has salido del escenario")

		# Miramos si se ha chocado con alguna de sus partes
		if self._snake.chocaCabezaConCuerpo():
			raise ExceptionAcabaJuego("Te has chocado contigo mismo")

		n = len(self._manzanas)
		# Miramos si se come una manzana
		for i in range(0, n-1):
			ccmanz = self._manzanas[i].coord()
			if ccmanz.x() == cc.x() and ccmanz.y() == cc.y():
				self._snake.anadeParte(self._width, self._height)





