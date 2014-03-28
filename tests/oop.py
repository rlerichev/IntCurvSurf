#!/usr/bin/env python3

#
# Ejemplo de programación orientada a objetos
#

from math import pi, sin, cos, tan, exp, sqrt


class Thing:
	pass


class Point:
	"""Clase Punto 3D"""
	#x, y, z = .0, .0, .0

	def __init__(self, x0=.0, y0=.0, z0=.0):
		self.x, self.y, self.z = x0, y0, z0

	#def coords(self):
	#	return self.x, self.y, self.z

	#def length(self):
	#	"""Longitud euclidiana"""
	#	return sqrt( self.x * self.x + self.y * self.y + self.z * self.z )

	#def __add__(self, p):
	#	return Point( self.x + p.x, self.y + p.y, self.z + p.z )

	#def __mul__(self, a):
	#	return Point( self.x * a, self.y * a, self.z * a )

	#def __str__(self):
	#	return "Point = (" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"


#class Curve:
#	"""Curva genérica"""

#	def __init__(self, f0):
#		self.f = f0

#	def point(self, t):
#		return self.f(t)

#	def points(self, a, b, n):
#		return [ self.f(a + (b - a)*i/n) for i in range(0, n+1) ]


#def helix(t):
#	return Point( cos(t), sin(t), t )


class FiniteGroup:
	"""Grupo finito (con un número finito de elementos"""
	
	def __init__(self):
		self.name = "trivial"
		self.elements = [ 0 ]
		self.table_add = { (0,0):0 }

	def add(self, e1, e2):
		return self.table_add[ (e1, e2) ]


class FiniteRing(FiniteGroup):
	"""Anillo finito"""

	def __init__(self):
		FiniteGroup.__init__(self)
		self.elements.append(1)
		self.table_add[ (0,1) ] = 1
		self.table_add[ (1,0) ] = 1
		self.table_add[ (1,1) ] = 0
		self.table_mul = { (0,0):0, (0,1):0, (1,0):0, (1,1):1 }

	def mul(self, e1, e2):
		return self.table_mul[ (e1, e2) ]


class FiniteField(FiniteRing):
	"""Campo finito"""

	def __init__(self):
		FiniteRing.__init__(self)
		self.table_div = { (0,1):0, (1,1):1, }

	def div(self, e1, e2):
		return self.table_div[ (e1, e2) ]
	


if __name__ == "__main__":

	#thing = Thing()
	#thing.n = 7
	#thing.name = "Cosa"
	#thing.l = [1, 0.3, "???"]

	p = Point()
	p.x = 1.0
	p.y = 0.5
	p.z = -0.5

	print( type(p) )
	print( p )
	print( p.x, p.y, p.z )

	#a, b, c = p.coords()
	#print( p.coords() )
	#print( p.length() )

	#q = Point(-1.0, 0.0, 0.75)
	
	#w = p + q * 2
	#print(w)

	#h = Curve(helix)
	#for p0 in h.points(0,pi,10):
	#	print( p0 )

	#fg = FiniteGroup()
	#fr = FiniteRing()
	#ff = FiniteField()	

	#print( fg.add(0,0) )
	#print( fr.add(0,1), fr.mul(1,0) )
	#print( ff.add(1,1), ff.mul(1,1), ff.div(1,1) )


