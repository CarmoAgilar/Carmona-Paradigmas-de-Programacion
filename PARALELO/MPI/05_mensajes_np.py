#=============================
# mpi optimizado para calculos
#=============================
from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self,rank):
        # arreglo de numpy optimizado
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "vengo del proceso " +str(rank)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    #====================================
    # arreglo para enviar
    #====================================
    m = s.x

    comm.Isend(m, dest=dst)

    #=====================================
    # arreglo vacio para recibir
    # con dimension 10 y tipo de datos
    # float64
    #=====================================
    a = np.zeros(10,dtype=np.float64)
    req = comm.Irecv(a, source=src)
    req.Wait()

    print("Soy el proceso ", rank ,", el resultado es ", a)
