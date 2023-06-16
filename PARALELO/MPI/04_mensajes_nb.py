from mpi4py import MPI

class Mensaje: # objeto mensaje
    def __init__(self,rank):
        self.x = [i for i in range(rank*10)] # iterador
        self.p = "vengo del proceso "+ str(rank)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dst = rank+1 if rank!=size-1 else 0

    #====================================
    # Recibir no bloqueante con espera
    # req: request 
    #====================================

    if rank%2==0:

        comm.send(s, dest=destino) # envia s al destino

        m = comm.recv(source=fuente) # recibe de fuente y lo pone en m
    
    else:

        m = comm.recv(source=fuente) # recibe de fuente y lo pone en m

        comm.send(s, dest=destino) # envia s al destino
    print("Soy el proceso ", rank ,", el resultado es ", len(m.x) ,",", m.p)
