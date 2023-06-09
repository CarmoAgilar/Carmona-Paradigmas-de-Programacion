#===============
# Uso de filtros
#===============

# Hacer una lista de los numeros por arriba del promedio

import statistics

bigdata = [1.3,2.7,0.8,4.1,4.3,-0.1]
promedio = statistics.mean(bigdata)
print(promedio)


# Hace una lista con elementos que cumplen la condicion
# filter( condicion, datos)
print(list(filter(lambda x: x > promedio, bigdata)))

paises=["","Argentina","","Brasil","","Chile","México","","Colombia","","","Cuba","Venezuela"]

print(list(filter(None, paises)))

