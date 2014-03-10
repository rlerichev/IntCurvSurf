#!/usr/bin/env python3

# Mutables!!!
def putNext(n, s, things):
	n += 1
	s = s*2
	things.append(n)
	things.append(s)
	print( things )


# Riemman's Z
def riemannZ(z, n=3):
	res = 0
	i = 1
	while i <= n:
		res += i**z
		i += 1
	return res


# Evaluar expresión
def feval(expr, x=1.0):
	return eval( expr )



# Fibonacci:
# f_0 = 1
# f_1 = 1
# f_n = f_{n-2} + f_{n-1}

def fibRec(n):
	if n > 1:
		return fibRec(n-2) + fibRec(n-1)
	else:
		return 1

def fib(n):
	i = 1
	n_1 = 1 
	n_2 = 1
	while i < n:
		temp = n_1
		n_1 = n_2 + n_1
		n_2 = temp
		i += 1
	return n_1

def fibPy(n):
	n_2, n_1, i = 1, 1, 1
	while i < n:
		n_2, n_1 = n_1, n_2 + n_1
		#n_1, n_2 = n_2 + n_1, n_1
		i += 1
	return n_1


def numRD(f, delta=0.1):
	def nd(x):
		return ( f(x+delta) - f(x) ) / delta
	return nd

def numLD(f, delta=0.1):
	def nd(x):
		return ( f(x) - f(x-delta) ) / delta
	return nd

def numCD(f, delta=0.1):
	def nd(x):
		return ( f(x+delta/2) - f(x-delta/2) ) / delta
	return nd
	#return lambda x: ( f(x+delta/2) - f(x-delta/2) ) / delta


if __name__ == "__main__":

	m = 5
	name = "Yo"
	ns = [1]
	putNext(m, name, ns)
	print(ns, "with", m, name)
	#putNext(m, name, ns)
	#print(ns, "with:, m, name)
	#putNext(m, name, ns.copy())
	#print(ns, "with:", m, name)

	#print( "Z(1)=", riemannZ( 1.0 ) )
	#print( "Z(2)=", riemannZ( 2.0 ) )
	#14.135, 21.022, 25.011
	print( "Z(z)=", riemannZ( 0.5 + 14.135j, 10 ) )
	#print( [ riemannZ( 0.5 + (i/5)*1j ) for i in range(1,20) ] )

	#n = 10
	#print( [ fibRec(i) for i in range(0,n) ] )
	#print( [ fib(i) for i in range(0,n) ] )
	#print( [ fibPy(i) for i in range(0,n) ] )

	# Time it!!!
	#import timeit

	#print( "x*x:", timeit.timeit( "x*x", setup="x=2", number=10000 ) )
	#print( "x**2:", timeit.timeit( "x**2", setup="x=2", number=10000 ) )
	#print( "eval1:", timeit.timeit( "feval(\"x*x\",x=2.0)", setup="from __main__ import feval", number=10000 ) )
	#print( "eval2:", timeit.timeit( "feval(\"x**2\",x=2.0)", setup="from __main__ import feval", number=10000 ) )

	#print( "fibRec(10):", timeit.timeit( "fibRec(10)", setup="from __main__ import fibRec", number=5000 ) )
	#print( "fib(10):", timeit.timeit( "fib(10)", setup="from __main__ import fib", number=5000 ) )
	#print( "fibPy(10):", timeit.timeit( "fibPy(10)", setup="from __main__ import fibPy", number=5000 ) )

	#print( "for i in range(0,10): fibRec(i):", timeit.timeit( "for i in range(0,10): fibRec(i)", setup="from __main__ import fibRec", number=1000 ) )
	#print( "for i in range(0,10): fib(i):", timeit.timeit( "for i in range(0,10): fib(i)", setup="from __main__ import fib", number=1000 ) )
	#print( "for i in range(0,10): fibPy(i):", timeit.timeit( "for i in range(0,10): fibPy(i)", setup="from __main__ import fibPy", number=1000 ) )


	#from math import pi, sin, cos, tan, exp
	#def f(x):
	#	return x**3 - x**2


	#dfr = numRD(f)
	#dfl = numLD(f)
	#dfc = numCD(f)
	#print( dfr(1.0) )
	#print( dfl(1.0) )
	#print( dfc(1.0) )

	#lderivs = [ numRD(f, 1/(2**n))(1.0) for n in range(0, 5) ] 
	#print( lderivs )

	#lcderivs = [ numCD(f, 1/(2**n))(1.0) for n in range(0, 5) ] 
	#print( lcderivs )

