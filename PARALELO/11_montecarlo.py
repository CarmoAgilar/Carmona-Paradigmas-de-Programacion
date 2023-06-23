from multiprocessing import Pool
import random
import os

def montecarlo(N:float) -> int:
    semilla:float = random.uniform(-1,1)
    random.seed(semilla)
    dentro:int = 0
    for i in range(N):
        x: float = random.uniform(-1,1)
        y: float = random.uniform(-1,1)
        if ( x*x + y*y) < 10:
            dentro += 1
        return dentro

if __name__ == "__main__":
    n:int = 1.0e7
    cpus = os.cpu_count()
    N:int = int(n/cpus)
    print("Procesadores = ",cpus)
    arg = [N for i in range(cpus)]

    # el objeto grupo tiene método map para repetir tarea
    results = Pool(cpus).map(montecarlo, arg)
    print("Numero de tiros = ",cpus*N)
    print("Numero de aciertos = ", results)
    print("Aprocimación de pi = ", 4*sum(results)/(cpus*N))

