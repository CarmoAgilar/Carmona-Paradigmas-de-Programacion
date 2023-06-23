from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10
x = range(n)
m = int(math.ceil(float(len(x)) / size))
x_chunk = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(math.sqrt, x_chunk))

#lista de todos los datos
r = comm.allreduce(r_chunk)

#matriz con todos los datos
rr = comm.allgather(r_chunk)

rrr = comm.gather(r_chunk, root=1)

if rank == 0:
    print(r)
    print(rr)
    print(rrr)
if rank == 1:
    print(rrr)

