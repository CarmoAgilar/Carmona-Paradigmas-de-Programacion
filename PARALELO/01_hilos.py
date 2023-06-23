from threading import Thread
import os
import math
import time

def calc():
    for i in range(0,4000000):
        math.sqrt(i)

threads = []
cpus = os.cpu_count()
print("Nucleos de tu cpu: ", cpus)
for i in range(cpus):
    print("registrado el hilo %d" %i)
    threads.append(Thread(target=calc))

start = time.time()

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

end = time.time()
print("Se tardo: ",end-start)
