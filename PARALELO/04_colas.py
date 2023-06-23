from multiprocessing import Process, Queue
def cuadrado(x,q):
    q.put((x,x*x))

if __name__=="__main__":
    q = Queue()
    procesos = [Process(target=cuadrado, args=(i,q)) for i in range (2, 10)]
    for p in procesos:
        p.start()
    for p in procesos:
        p.join()
    resultado = [q.get() for p in procesos]
    print(resultado)
