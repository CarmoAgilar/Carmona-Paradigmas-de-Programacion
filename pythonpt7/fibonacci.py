#=============================
# Recursividad y memorizacion
#=============================

from functools import lru_cache # Herramiebta para la memorizacion

def fibonacci_lento(n):
    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return fibonacci_lento(n-1)+fibonacci_lento(n-2)

for i in range(1,36):
    print(str(i) + ": ",fibonacci_lento(i))


# Optimizando con un conjunto de fibonaccis

fibonaccis = {}
def fibonacci(n):

    if n in fibonaccis: #Revisa si ya existe
        return fibonaccis[n]

    if n==1:
        valor = 1
    if n==2:
        valor = 1
    if n>2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    fibonaccis[n] = valor
    return valor

for i in range(1,10001):
    print(str(i) + ": ",fibonacci(i))

# Usando decoradores para la memorizacion
@lru_cache(maxsize = 3) # maxsize es cuantos anteriores guarda
def nfibonacci(n):
    if type(n) != int:
        raise TypeError("n debe ser entero positivo")
    if n<1:
        raise ValueError("n debe ser entero positivo")

    if n==1:
        return 1
    if n==2:
        return 1
    if n>2:
        return nfibonacci(n-1) + nfibonacci(n-2)

for i in range(1,10001):
    print(str(i) + ": ",nfibonacci(i))

