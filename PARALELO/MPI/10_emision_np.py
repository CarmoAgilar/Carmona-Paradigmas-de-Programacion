from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#tamaño del arreglo
n = 10

if rank == 0:
    data = numpy.arange(n, dtype='i')
else:
    data = numpy.empty(n, dtype='i')


# enviamos diccionario a todos los procesos desde root
data = comm.bcast(data, root=0)
print(data)

#==========================================
# broadcast pro que indica el tipo de dato
# optimizado para comunicarnos rapida
#==========================================
comm.Bcast([data,MPI.INT], root = 0)

# comprobacion de si todo salio bien
for i in range(n):
    assert data[i] == i
print(data)
