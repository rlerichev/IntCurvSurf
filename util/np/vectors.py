#
# Util vectorial functions and classes using NumPy
#

import numpy as np

def vec2(x, y):
	return np.array([x, y])

def vec3(x, y, z):
	return np.array([x, y, z])


if __name__ == "__main__":

	v2 = vec2(0.1, -0.2)
	print( "v2 =", v2 )

	v3 = vec3(0.2, -1.3, 4.0)
	print( "v3 =", v3 )

