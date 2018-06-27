


class Snake:
	"""
	self.partes es la lista de las partes de la serpiente exceptuando la cola


	"""



	"""
	Se define la posición de la cabeza del snake.
	x e y definen la posición inicial, la o es la orientación
	"""
	def __init__(self, x, y, o):
		self._cabeza = Cabeza(x,y,o)
		self._partes = []

	def cambiaDireccion(self, o):
		self._cabeza.o(o)


	"""
	Se ha de mirar que la parte se genere en un espacio libre =>
	se ha de cumplir en alguna de las 4 direcciones:
		- que no haya parte de serpiente
		- que no se salga del escenario
	"""
	def anadeParte(self, width, height, posicionesManzanas):
		p = self._partes[-1]
		x = p.x()
		y = p.y()
		stepsx = [-1, -1, 1, 1]
		stepsy = [-1, 1, -1, 1]
		return self.pruebaCoords(width, height, x, y, stepsx, stepsy, posicionesManzanas)


	def pruebaCoords(self, width, height, x, y, stepsx, stepsy, posicionesManzanas):
		n = len(stepsx)
		for i in range(0, n-1):
			if not self.compruebaCoords(width, height, x + stepsx[i], y + stepsy[i], posicionesManzanas)
				return False
		return True


	"""
	Comprueba si x e y pertenecen a una casilla vacía
	"""
	def compruebaCoords(self, width, height, x, y, posicionesManzanas):
		if x >= 0 and x < width and y >= 0 and y < height and self._cabeza.coord.x() != x and self._cabeza.coord.y() != y:
			for pm in posicionesManzanas:
				if x == pm.coord.x() and y == pm.coord.y():
					return False
			return self.existePartePos(x,y)
		else:
			return False


	def existePartePos(self, x, y):
		for p in self._partes:
			if p.coord.x() == x or p.coord.y() == y:
				return False
		return True