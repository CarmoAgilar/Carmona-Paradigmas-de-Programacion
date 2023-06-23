from multiprocessing import Process
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

procesos = []
cpus = os.cpu_count()
print("Nucleos de tu cpu: ", cpus)
for i in range(cpus):
    print("registrado el proceso %d" %i)
    procesos.append(Process(target=calc))

start = time.time()

for proceso in procesos:
    proceso.start()
for proceso in procesos:
    proceso.join()

end = time.time()
print("Se tardo: ",end-start)
