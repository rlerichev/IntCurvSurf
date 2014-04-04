#!/usr/bin/env python3.3

from math import exp, sin, cos, tan, pi
import numpy as np
import visvis as vv

# App
#  Window
#   Figure
#    Axes
#     Graphics

app = vv.use()
#vv.clf() 

#
# Superficie como gráfica de una función
#
f = lambda x, y: x*y

xs = np.linspace(-2.0,2.0,21)
ys = np.linspace(-2.0,2.0,21)
zs = [ [ f(x,y) for x in xs ] for y in ys ]

graph_surf = vv.grid(xs, ys, zs, axesAdjust=True)
#graph_surf = vv.surf(xs, ys, zs, axesAdjust=True)
graph_surf.colormap = vv.CM_JET


#
# Superficie paramétrica
#
def paramSurf(u,v):
	x = 2.0 * cos(u) * sin(v)
	y = 1.5 * sin(u) * sin(v)
	z = 2.2 * cos(v)
	return np.array( (x, y, z) )

NU = 21
NV = 11
#us = np.linspace(0.0,1.8*pi,NU)
#vs = np.linspace(0.0,0.8*pi,NV)

# Puntos
#ps = np.array( [ paramSurf(u,v) for v in vs for u in us ] )

# Caras
#fs = [ [ i + j*NU,i + j*NU + 1,i + + j*NU + NU + 1,i + j*NU + NU ] for j in range(NV-1) for i in range(NU-1) ] 

#param_surf = vv.mesh( ps, faces=fs, verticesPerFace=4, colormap=vv.CM_HOT, axesAdjust=True )
#param_surf.faceColor = (1,1,0.8,0.95)
#param_surf.ambient = 0.9
#param_surf.diffuse = 0.4
#param_surf.faceShading='smooth'
#param_surf.shininess = 50
#param_surf.specular = 0.35
#param_surf.emission = 0.45
#param_surf.edgeColor = (0.2,0.2,0.4,1)
#param_surf.edgeShading = 'smooth'


#
# Superficie implícita
#
N = 32
#vol = np.empty((N,N,N), dtype='float32')
#for k in range(N):
#		for j in range(N):
#				for i in range(N):
#						vol[i,j,k] = N*2 - 2.0*(i-N/2)*(i-N/2) - (j-N/2)*(j-N/2) - 0.5*(k-N/2)*(k-N/2) # Elipsoide
						#vol[i,j,k] = (2.0/N)*(i-N/2)*(i-N/2) - (1/N)*(j-N/2)*(j-N/2) - (k-N/2) # Paraboloide hiperbolico
						#vol[i,j,k] = cos(i) + cos(j) + cos(k) # Triply periodic minimal surface (Schwarz)

# show
#impl_surf = vv.volshow(vol, renderStyle='iso')
# try the differtent render styles, for examample 
# "t.renderStyle='iso'" or "t.renderStyle='ray'"
# If the drawing hangs, your video drived decided to render in software mode.
# This is unfortunately (as far as I know) not possible to detect. 
# It might help if your data is shaped a power of 2.
#impl_surf.isoThreshold = 0.0
#impl_surf.colormap = vv.CM_WINTER

# Create colormap editor wibject.
#vv.ColormapEditor(axs)


#
# Graficación
#

axs = vv.gca() # "Get Current Axes"
#axs.bgcolor = (0.0, 0.0, 0.0)
axs.camera.fov = 60	

fig = vv.gcf() # "Get Current Figure"
fig._widget.showFullScreen() # Pantalla completa, para RaspberryPi

app.Run() # Corre aplicación/ventana

