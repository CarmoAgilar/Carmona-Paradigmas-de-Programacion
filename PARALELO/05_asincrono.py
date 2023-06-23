import multiprocessing as mp
import numpy as np
import time

def my_function(i, param1, param2, param3):
    # calcula un polinomio
    result = param1**2 + param2 + param3
    # espera dos segundos
    time.sleep(2)
    return(i, result)

def get_result(result):
    # se inscriben en la lista global
    # mala practica
    global results
    results.append(result)

#========================
# Programa principal
#========================
if __name__ == "__main__":
    # matriz de 10x3 numeros al azar
    params = np.random.random((10,3))*100.0
    results = []
    ts = time.time()

    # un grupo de procesos (pool)
    pool = mp.Pool(mp.cpu_count())

    # loop de primera dimension del arreglo
    for i in range(0, params.shape[0]):
        #correr asincrónicamente my_function con argumentos args y cuando termine correr get_result
        pool.apply_async(my_function, args = (i, params[i, 0], params[i,1], params[i,2]), callback = get_result)

    #cerrar el grupo
    pool.close()
    # esperar que termine el grupo
    pool.join()

    print("Tiempo en paralelo = ", time.time()-ts)
    print(results)

