from numba import jit
import numpy
import time

@jit(nopython=True)
def rapido(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a+t

# con el interprete
def lento(a):
    t = 0.0
    for i in range(a.shape[0]):
        t += numpy.tanh(a[i,i])
    return a+t

x = numpy.arange(10000).reshape(100,100)

# la primera llamada incluye el tiempo de compilacion
start = time.time()
rapido(x)
end = time.time()
print("Tiempo incluyendo compilacion = %s" % (end-start))

# y sin tiempo de compilacion
start = time.time()
rapido(x)
end = time.time()
print("Tiempo usando numba = %s" % (end-start))

# funcion lenta
start = time.time()
lento(x)
end = time.time()
print("Tiempo en python puro = %s" % (end-start))
