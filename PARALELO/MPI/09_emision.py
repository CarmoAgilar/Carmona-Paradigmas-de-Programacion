#======================
# Broadcast con MPI
# distribucion de datos
#======================
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# el proceso 0 tiene datos y los demas no
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3],
            'key2' : ( 'abc', 'xyz')}

else:
    data = None

# enviamos diccionario a todos los procesos desde root
data = comm.bcast(data, root=0)
print(data)
