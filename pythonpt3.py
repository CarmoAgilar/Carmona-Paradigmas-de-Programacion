""" ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
"""
#============================
# Carmona Aguilar Diego
#     Curso python 3
#============================

#=========================
# Condicionales
#=========================
precio = 50

if precio < 50: 
    print("El precio es menor a 50")
elif precio > 50: # si lo de arriba no, pero esto si
    print("El precio es mayor a 50")
else: # si nada anterior
    print("El precio es 50")

#=============================
#Condicionales anidados
#=============================
cantidad = 5
total = cantidad*precio
if total > 100:
    if total > 500:
        print("El total es mayor a 500")
    else:
        if total < 500 and total > 400:
            print("El total es menor que 500 y mayor que 400")
        elif total < 500 and total > 300:
            print("El total es menor que 500 y mayor que 300")
        else:
            print("El total es menor que 500 y mayor que 100")
elif total == 100:
    print("El total el 100")
else:
    print("El total es menor que 100")

#===========================
# Ciclo while
#===========================
num = 0
while num < 5: # Repite el ciclo mientras la condicion sea verdad
    num = num + 1
    print("num = ",num)

num = 0
while num < 5:
    num += 1 # lo mismo que num = num + 1
    print("num = ",num)
    if num == 3:
        break # salir del bucle
num = 0
while num < 5:
    num += 1 # lo mismo que num = num + 1
    if num > 3:
        continue # evitar lo que sigue sin salr del bucle
    print("num = ", num)

#====================
# Bucles sobre cosas
#====================
nums = [10, 20, 30, 40, 50] 
for i in nums: # sobre lista
    print(i)

for char in "Hello": # sobre string
    print(char)

numNames = {1:"One", 2:"Two", 3:"Three"}
for pair in numNames.items(): # sobre diccionarios
    """ items() = elementos"""
    print(pair)


for k,v in numNames.items():
    print("Key = ", k , " value = ", v)


#_______________________________________________________
#|                                                      |
#|                  Inicio de funciones                 |
#|______________________________________________________|

def saludo():
    ### Esta funcion saluda
    print("Hola")

### LLamado de una funcion
saludo()

saludo = saludo() #Esto no se asigna
print(saludo) # no sirve

"""Mostrar documentacion:"""
#help(saludo)

def salu2(nombre): # funcion con argumento
    """Funcion que saluda pero ahora por tu nombre"""
    print("Hola", nombre)

salu2("Julian")
salu2("Diego")

