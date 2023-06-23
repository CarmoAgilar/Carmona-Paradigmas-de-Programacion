#===========================================================
# Ejemplo de comunicacion bloqueada a un arreglo compartido
# Uso de candados (locks)
#===========================================================
from multiprocessing import Process, Array, Lock
import time

def sumale100(numeros,candado):
    for i in range(len(numeros)):
        # lo que este bloqueado no puede ser tocado al mismo tiempo por otro proceso
        with candado:
            numeros[i] += 1
if __name__ == "__main__":
    # el cancado evita la "empalmacion" de dos procesos
    candado = Lock()

    # numero común a los procesos, d de dobles
    numeros_compartidos = Array('d', [0.0, 100.0, 200.0])

    #: quiere decir todos los elementos
    print("Al principio vale =", numeros_compartidos[:])

    #Dos procesos
    p1 = Process(target=sumale100, args=(numeros_compartidos, candado))
    p2 = Process(target=sumale100, args=(numeros_compartidos, candado))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Al final vale = ", numeros_compartidos[:])
