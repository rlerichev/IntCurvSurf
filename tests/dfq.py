#!/usr/bin/env python3

#
# Diferencial de la parametrización de una superficie (esfera)
#

from math import sin, cos, pi
import numpy as np # Biblioteca "numérica", de arreglos n-dimensionales
import scipy.linalg as la # Biblioteca de álgeba lineal


def vec2(u,v):
    return np.array( [u,v] )

def vec3(x,y,z):
    return np.array( [x,y,z] )

def f(u,v):
    """Parametrización de la esfera unitaria."""
    return vec3( cos(u) * sin(v), sin(u) * sin(v), cos(v) )
    
def dfu(u,v):
    """Derivada con respecto a u de la parametrización de la esfera unitaria."""
    return vec3( -sin(u) * sin(v), cos(u) * sin(v), 0. )

def dfv(u,v):
    """Derivada con respecto a v de la parametrización de la esfera unitaria."""
    return vec3( cos(u) * cos(v), sin(u) * cos(v), -sin(v) )
    

# Punto en R2
u = pi/4.0
v = pi/3.0

# Derivadas de la parametrización evaluadas en el punto
fu = dfu(u,v)
fv = dfv(u,v)
print( "dfu =", fu )
print( "dfv =", fv )

# Matriz de la diferencial, 3 renglones x 2 columnas
dfq = np.empty( (3,2) )
dfq[:,0] = fu
dfq[:,1] = fv
print( "dfq =\n", dfq )

# Matriz extendida de la diferencial, con la columna 3 dada como el producto
# cruz de las derivadas en u y v
dfq_ext = np.empty( (3,3) )
dfq_ext[:,:2] = dfq
dfq_ext[:,2] = np.cross( fu, fv )
print( "dfq_ext =\n", dfq_ext )
#print( "|dfq_ext| =", la.det( dfq_ext ) ) # determinante

# Inversa de la matriz de la diferencial extendida, mapea el plano tangente
# a el plano UV
dfq_inv = la.inv( dfq_ext )
print( "dfq_1 =\n", dfq_inv )

# Otro punto en R2
q = vec2( 0.2, -2.1 )
print( "q =", q )

# w es un vector tangente a la esfera en el punto f(q)
w = dfq.dot( q )
print( "w =", w )

# Comprobación, la inversa aplicada a w da q
print( "dfq_1(w)=", dfq_inv.dot(w) )

# (Todo) vector en el plano tengente es combinación lineal de las derivadas de
# la parametrización, la inversa aplicada a la combinación da los coeficientes
w2 = 3.2*fu - 0.5*fv
print( "dfq_1(w2)=", dfq_inv.dot(w2) )
