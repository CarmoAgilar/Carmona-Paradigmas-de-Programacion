#===================================
# mpirun -n 4 python3 tareas_mpi.py
#===================================
from mpi4py import MPI

comm = MPI.COMM_WORLD # objeto de comunicadores

size = comm.Get_size() # el total

rank = comm.Get_rank() # quien soy

#si soy el proceso que dice ahi, hago lo que dice el if
if rank == 0:
    print("Yo soy el proceso 0")

elif rank == 1:
    print("Soy el proceso 1")
else:
    print("No soy los dos primeros procesos")

print("Reportandose aqui el proceso ",str(rank), " de ",str(size))

