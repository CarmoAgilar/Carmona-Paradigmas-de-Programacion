#=========================
# forma compacta de 06
#=========================
from mpi4py import MPI
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = np.zeros(1)

if rank == 1:
    dst = 0
    src =0

if rank == 0:
    dst = 1
    src = 1

    
randNum = numpy.random.random_sample(1)
print("Soy el proceso ", rank ,", recibio ", randNum[0})
comm.Isend(randNum, dest=dst)
req = comm.Irecv(randNum, source=src)
req.Wait()
print("Soy el proceso ", rank ,", recibio ", randNum[0})

