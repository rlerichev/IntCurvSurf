#
# Util vectorial functions and classes using NumPy
#

import numpy as np
from math import sqrt


def vec2(x, y):
	"""Shortcut to create a 2D numpy array"""
	return np.array( (x, y) )

def vec3(x, y, z):
	"""Shortcut to create a 3D numpy array"""
	return np.array( (x, y, z) )

def length(v):
	"""Vector's euclidean length"""
	return sqrt( sum( r*r for r in v ) )
		
def length2(v):
	"""Vector's squared euclidean length"""
	return sum( r*r for r in v )



if __name__ == "__main__":

	v2 = vec2(0.1, -0.2)
	print( "v2 =", v2 )

	v3 = vec3(0.2, -1.3, 4.0)
	print( "v3 =", v3 )

	print( "|v2| =", length(v2) )

	print( "|v3|^2 =", length2(v3) )
