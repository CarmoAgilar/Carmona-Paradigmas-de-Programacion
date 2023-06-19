from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get-rank()

n = 10

# arreglo de ceros sumado con un escalar
sendarray = numpy.zeros(n, dtype='i')+rank

recvarray = None

# datas = comm.gather(data, root=0)

if rank == 0:
    #matriz vacia de enteros
    recvarray = numpy.empty([size, n], dtype='i')

comm.Gather(sendarray, recvarray, root=0)

if rank == 0:
    for i in range(size):
        # revisar por fila
        # : significa todos los elementos de esa dimension
        # allclose es un metodo de numpy que compara los elementos
        assert numpy.allclose(recvarray[i,:], i)

print(recvarray)

