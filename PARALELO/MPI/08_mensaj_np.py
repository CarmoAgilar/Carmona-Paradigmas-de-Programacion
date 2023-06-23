#=========================
# forma compacta de 06
#=========================
from mpi4py import MPI
import numpy
comm = MPI.COMM_WORLD
rank = comm.Get_rank()


if rank == 0:
    
    data = numpy.arange(10, dtype='i') # arreglo de numeros del 0 al 9
    comm.Send([data, MPI.INT], dest = 1, tag= 77)

elif rank == 1:

    data = numpy.arange(10, dtype='i') # arreglo de numeros del 0 al 9
    comm.Recv([data, MPI.INT], source = 0, tag= 77)
    print(data)

# EJEMPLO 2

if rank == 0:
    data = numpy.arange(10, dtype=numpy.float64)
    comm.Send(data, dest = 1, tag = 13)
elif rank == 1:
    data = numpy.empty(10, dtype=numpy.float64)
    comm.Recv([data, MPI.INT], source = 0, tag = 13)
    print(data)
