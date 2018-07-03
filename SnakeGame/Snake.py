


class Orientacion(Enum):
	ARRIBA = 0
	ABAJO = 1
	IZQUIERDA = 2
	DERECHA = 3

	"""
	0 -> arriba ->	(0,-1)
	1 -> abajo ->	(0,1) 
	2 -> izquierda->(-1,0)
	3 -> derecha->	(1,0)
	"""
	def getDireccionByOrientacion(o):
		if o == 0:
			return Coord(0,-1)
		else if o == 1:
			return Coord(0,1)
		else if o == 2:
			return Coord(-1,0)
		return Coord(1,0)


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


	@property
	def coord(self):
		return self._cabeza.coord()



	"""
	pos1 es la posición inicial, pos2 es la posición siguiente
	"""
	def obtenvectordir(pos1, pos2):
		return Coord(pos2.x() - pos1.x(), pos2.y() - pos1.y())

	"""
	Se ha de enfocar de manera, que se avanza la cabeza, y dónde estaba la cabeza va a ir
	la siguiente parte, donde estaba esta siguiente, va a ir la siguiente de la siguientes
	y así sucesivamente.

	Qué se debe de hacer:
		- Avanzar toda la serpiente

		- Si encuentra una manzana, comérsela y llamar a
			anadeParte. !!! NO, ESO LO HACE LA CLASE TABLERO

		- Si avanza y se encuentra consigo misma o con una pared
			entonces lanzar una excepción de acabar partida. !!! NO, ESO LO HACE LA CLASE TABLERO
	"""
	def avanza(self):
		
		antpos = self._cabeza.coord()
		dirv = self._cabeza.o()
		self._cabeza.avanza(dirv)
		n = len(self._partes)
		for i in range(0, n-1):
			dirv = obtenvectordir(self._partes[i].coord(), antpos)
			antpos = self._partes[i].coord()
			self._partes[i].avanza(dirv)


	def chocaCabezaConCuerpo(self):
		cc = self._cabeza.coord()

		for p in self._partes:
			if p.x() == cc.x() and p.y() == cc.y():
				return True
		return False




	"""
	Se ha de mirar que la parte se genere en un espacio libre =>
	se ha de cumplir en alguna de las 4 direcciones:
		- que no haya parte de serpiente
		- que no se salga del escenario
	"""
	def anadeParte(self, width, height):
		p = self._partes[-1]
		x = p.x()
		y = p.y()
		stepsx = [-1, -1, 1, 1]
		stepsy = [-1, 1, -1, 1]
		return self.pruebaCoords(width, height, x, y, stepsx, stepsy)




	def pruebaCoords(self, width, height, x, y, stepsx, stepsy):
		n = len(stepsx)
		for i in range(0, n-1):
			if not self.compruebaCoords(width, height, x + stepsx[i], y + stepsy[i])
				return False
		return True


	"""
	Comprueba si x e y pertenecen a una casilla vacía
	"""
	def compruebaCoords(self, width, height, x, y):
		if x >= 0 and x < width and y >= 0 and y < height and self._cabeza.coord.x() != x and self._cabeza.coord.y() != y:
			"""
			for pm in posicionesManzanas:
				if x == pm.coord.x() and y == pm.coord.y():
					return False
			"""
			return self.existePartePos(x,y)
		else:
			return False


	def existePartePos(self, x, y):
		for p in self._partes:
			if p.coord.x() == x or p.coord.y() == y:
				return False
		return True