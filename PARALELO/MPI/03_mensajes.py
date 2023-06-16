from mpi4py import MPI

class Mensaje: # onbjeto mensaje
    def __init__(self,rank):
        self.x = range(rank*10) # iterador
        self.p = "vengo del proceso "+ str(rank)

if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)

    fuente = rank-1 if rank!=0 else size-1 #que te mande el anterior y si es cero, que sea el ultimo

    destino = rank+1 if rank!=size-1 else 0 #mandalo al siguiente y si eres el ultimo, mandalo al primero

    #===============================================================
    # send y recv son operaciones bloqueadaas y hacen que el codigo
    # se atore esperando que alguien reciba un mensaje
    # se resuelve enviando con los pares y recibiendo con impares
    #===============================================================

    if rank%2==0:

        comm.send(s, dest=destino) # envia s al destino

        m = comm.recv(source=fuente) # recibe de fuente y lo pone en m
    
    else:

        m = comm.recv(source=fuente) # recibe de fuente y lo pone en m

        comm.send(s, dest=destino) # envia s al destino
    print("Soy el proceso ", rank ,", el resultado es ", len(m.x) ,",", m.p)
