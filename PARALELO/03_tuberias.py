from multiprocessing import Process, Pipe

def f(extremo):
    extremo.send([0,1,2,3,4])
    extremo.close()

def g(extremo):
    a = extremo.recv()
    for i in a:
        a[i] += 100
    print(a)

if __name__=="__main__":
    extremo1, extremo2 = Pipe()
    proceso1 = Process(target=f, args=(extremo1,))
    proceso2 = Process(target = g, args = (extremo2, ))
    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

