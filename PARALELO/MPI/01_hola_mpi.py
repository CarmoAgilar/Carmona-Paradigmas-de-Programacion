#==================================
# mpiexec -n 4 python3 hola_mpi.py
# mpirun  -n 4 python3 hola_mpi.py
#==================================
# para correr en 4 procesos
#==================================
from mpi4py import MPI

comunicadores = MPI.COMM_WORLD # crear un objeto comunicador

n_procesos = comunicadores.Get_size() # numero total de procesos

quien_soy = comunicadores.Get_rank()

print("Saludos desde el proceso ",str(quien_soy)," de ", str(n_procesos))
