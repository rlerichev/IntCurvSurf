#!/usr/bin/env python3

from math import sin, cos, pi
import numpy as np # Biblioteca "numérica", de arreglos n-dimensionales
import scipy.linalg as la # Biblioteca de álgebra lineal


# Creación de un vector
v3 = np.array( (1.0, 0.1, -0.5 ) )
# vector, número de dimensiones, forma
print( "v3 =\n", v3, "\nD(v3) = ", v3.ndim, ", Sh(v3) = ", v3.shape )

# Creación de una matriz de 2 renglones X 3 columnas
#m = np.array( [ [1.0, 0.0, -0.1], [-0.1, 1.0, 2.0] ] )
#print( "m =\n", m, "\nD(m) = ", m.ndim, ", Sh(m) = ", m.shape )
#print( "m[1,2] =", m[1,2] ) # renglón, columna
#print( "m[1,:] =", m[1,:] ) # renglón
#print( "m[:,1] =", m[:,1] ) # columna
	
#m[:,1] = np.array( (-0.2, 1.25) )
#print( "m =\n", m )

# Multiplicación de matriz por vector entrada a entrada
#v2 = m * v3
#print( "v2 =\n", v2 )

# Multiplicación de matriz por vector
# Recordar: * NO ES dot
#v2 = m.dot( v3 )
#print( "v2 =\n", v2 )

# Operaciones entre vectores
#u3 = np.array( (-1.0, 0.75, 4.5 ) )
#w3 = v3 + u3 * 1.25
#print( "w3 =\n", w3 )
	
# Producto cruz de vectores 3D
#u3 = np.cross( w3, v3 )
#print( "w3 x v3 =\n", u3 )
#print( "w3 x v3 . w3 =\n", u3.dot( w3 ) )
	
# Matriz de llena algo
#m3x3 = np.zeros( (3, 3) ) # Matriz de llena de ceros
#m3x3 = np.ones( (3, 3) ) # Matriz de llena de unos
#m3x3 = np.identity( 3, float ) # Matriz identidad
#m3x3 = np.random.random( (3, 3) ) # Matriz con entradas aleatorias entre 0 y 1
#m3x3 = np.random.random( (3, 3, 3) ) # Cubo con entradas aleatorias entre 0 y 1
#m3x3 = np.random.random( (3, 3, 3, 3) ) # Hipercubo con entradas aleatorias entre 0 y 1
#m3x3 = 4.0 * np.random.random( (3, 3) ) - 2.0 # Matriz con entradas aleatorias entre -2 y 2
#print( "mat =\n", m3x3 )

# Determinante
#d = la.det(m3x3)
#print( "det =\n", d )

#if d > 0.001 or d < -0.001:

	# Inversa
	#print( "mat^-1 =\n", la.inv(m3x3) )
	
	# Solución de un sistema
	#sol = la.inv( m3x3 ).dot( v3 )
	#sol = la.solve( m3x3, v3 )

	#print( "sol =\n", sol )


# Eigen valores y Eigen vectores
#lambs, vs = la.eig( m3x3 )

#print( "Eigens =\n", vs, "\n", lambs )

#for i in range(0,3):
	#v = np.array( vs[:,i] ).T
	#print( i, m3x3.dot( v ) - lambs[i] * v ) # Comprobación, casi da cero

# Lista de N números entre a y b 
#xs = np.linspace(-2*pi, 2*pi, 51)
#print( xs )

#ys = np.sin( xs ) * np.exp( -(xs*xs)/16 )
#print( ys )


#import matplotlib as mpl
#import matplotlib.pyplot as plt

#plt.plot( xs, ys )
#plt.fill( xs, ys, 'r')
#plt.grid(True)
#plt.title( r'$f(x)=sin(x)e^{\frac{-x^2}{16}}$' )
#plt.xlabel( 'x' )
#plt.ylabel( 'y=f(x)' )
#plt.plot( xs, 0.025 * xs, 'g.-' )
#plt.show()

