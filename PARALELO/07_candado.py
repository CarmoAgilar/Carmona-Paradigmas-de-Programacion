#===========================================================
# Ejemplo de comunicacion bloqueada a un arreglo compartido
# Uso de candados (locks)
#===========================================================
from multiprocessing import Process, Value, Lock
import time

def sumale100(numero, candado):
    for i in range(100):
        time.sleep(0.01)
        # Poner el candado
        candado.acquire()
        # Hacer la operacion
        numero.value += 1
        # Quitar el candado
        candado.release()

if __name__ == "__main__":
    # el candado evita la "empalmacion" de dos procesos
    candado = Lock()
    # numero común a los procesos, i de entero
    # Value es un objeto de numero compartido
    numero_compartido = Value('i', 0)
    print("Al principio vale =  ", numero_compartido.value)
    p1 = Process(target=sumale100, args=(numero_compartido, candado))
    p2 = Process(target=sumale100, args=(numero_compartido, candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Al final vale ", numero_compartido.value)
