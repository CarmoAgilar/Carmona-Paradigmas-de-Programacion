from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get-rank()

data = (rank+1)**2

# Manden sus datos al proceso root=0
# (en orde

datas = comm.gather(data, root=0)

# comprobacion de si todo salio bien
if rank == 0:
    for i in range(size):
        assert data[i] == (i+1)**2
else:
    assert datas is None

print(data)

