#!/usr/bin/env python3

from math import exp, sin, cos, tan, pi
import numpy as np
import scipy.linalg as la
import scipy.integrate as inte
import matplotlib as mpl
import matplotlib.pyplot as plt


# Función de real de 1 variable
def f(x):
	return x*x + 1
	#return exp(-x*x)

# Integral
area, error = inte.quad( f, 0.0, 2.0 ) #np.inf ) # Gauss–Kronrod quadrature
print( "Int f =", area, ", Error =", error )

xs = np.linspace(-1.0, 3.0, 21)

#ys = np.vectorize(f)(xs)
#plt.plot( xs, ys, 'black', linewidth=2 )
#plt.title( r'$\int_a^b f(x)dx$' )
#plt.grid(True)
#ax = plt.gca()
#ax.fill_between( xs[5:16], 0.0, ys[5:16], facecolor='g' )
#plt.show()


# Función de real de 1 variable con coeficientes variables...
#def f2(x, u, v):
#	return u * x*sin(x) - v * exp(x)

# Integral
#area, error = inte.quad( f2, 0.0, 2.0, args=(3.0, 0.5) )
#print( "Int f =", area, ", Error =", error )

#ys = np.vectorize( lambda x: f2(x, 3.0, 0.5) )(xs)
#plt.plot( xs, ys, 'black', linewidth=2 )
#plt.title( r'$\int_a^b u x sin(x) - v e^x dx$' )
#plt.grid(True)
#ax = plt.gca()
#ax.fill_between( xs[5:16], 0.0, ys[5:16], facecolor='g' )
#plt.show()


# Función de real de 2 variables
#f3 = lambda x, y : x*y

# Integral
#vol, error = inte.dblquad( f3, 0.0, 2.0, lambda y: 0, lambda y: 1.0 - y )
#print( "Int f =", vol, ", Error =", error )

#plt.plot( [-0.5,1.5], [1.5,-0.5], 'black', linewidth=2 )
#plt.title( r'$\int_0^2 \int_0^{1-y} xy dx dy$' )
#plt.grid(True)
#ax = plt.gca()
#ax.fill_between( [0,1], 0.0, [1,0], facecolor='g' )
#plt.show()


# Ecuación diferencial ordinaria 1D:
# x' = f(t,x)
#def f(t, x):
#	return x

# Recordar: La solución es una función x(t)

#ode_solver = inte.ode(f)
#ode_solver.set_integrator( 'dopri5' ) #, method='bdf' )

#t0 = 0.0
#x0 = 1.0
#ode_solver.set_initial_value( x0, t0 ) # x0, t0

N = 20 # número de puntos (pasos de integración)
dt = 0.5 # delta (distancia de separación entre t_n y t_{n+1}

#xs = []
#while ode_solver.successful() and ode_solver.t < N:
#	xs.append( ode_solver.integrate( ode_solver.t + dt ) )
#xs = [ ode_solver.integrate( ode_solver.t + dt ) for i in range(N) if ode_solver.successful() ]

#ts = np.linspace( t0, t0 + N * dt, N )
#plt.plot( ts, xs, 'black', linewidth=2 )
#plt.title( r'$x(t)$' )
#plt.grid(True)
#plt.ylim( ymin=0 )
#plt.show()	


# Ecuación diferencial ordinaria 2D:
# x' = f(t,p)
#def f(t, p):
#	x = -p[1]
#	y = p[0]
#	return np.array( ( x, y ) )

#ode_solver = inte.ode(f)
#ode_solver.set_integrator( 'dopri5' ) #, method='bdf' )

#t0 = 0.0
#p0 = np.array( (1.0, 0.0) )
#ode_solver.set_initial_value( p0, t0 ) # p0, t0

#ps = np.array( [ ode_solver.integrate( ode_solver.t + dt ) for i in range(N) if ode_solver.successful() ] )

#plt.plot( ps[:,0], ps[:,1], 'black', linewidth=2 )
#plt.title( r'$\alpha(t) = (x(t), y(t))$' )
#plt.grid(True)
#plt.xlim( xmin=-1.5, xmax=1.5 )
#plt.ylim( ymin=-1.5, ymax=1.5 )


#ode_solver.set_integrator( 'vode', method='bdf' )
#ode_solver.set_initial_value( p0, t0 )
#ps2 = np.array( [ ode_solver.integrate( ode_solver.t + dt ) for i in range(N) if ode_solver.successful() ] )
#plt.plot( ps2[:,0], ps2[:,1], 'r', linewidth=2 )

#plt.show()	

# Ecuación diferencial ordinaria 3D:
# x' = f(t,p)
#def f(t, p):
#	x = -p[1]
#	y = p[0]
#	z = 1.0
#	return np.array( ( x, y, z ) )

#ode_solver = inte.ode(f)
#ode_solver.set_integrator( 'dopri5' ) #, method='bdf' )

#t0 = 0.0
#p0 = np.array( (1.0, 0.0, 0.0) )
#ode_solver.set_initial_value( p0, t0 ) # p0, t0


#import visvis as vv

#ps = vv.Pointset(3)
#ps.extend( np.array( [ ode_solver.integrate( ode_solver.t + dt ) for i in range(N) if ode_solver.successful() ] ) )

#app = vv.use() # Aplicación/Ventanas
#vv.clf() # "Clear Figure"

#vv.solidLine(ps, axesAdjust=False)
#vv.plot(ps, lw=4, lc=(0.9,0.1,0.5), ms='o', ls='-', axesAdjust=False)

#axs = vv.gca() # "Get Current Axes"
#axs.bgcolor = (0.0, 0.0, 0.0)
#axs.camera.fov = 60	

#fig = vv.gcf() # "Get Current Figure"
#fig._widget.showFullScreen() # Pantalla completa, para RaspberryPi

#app.Run() # Corre aplicación/ventana

