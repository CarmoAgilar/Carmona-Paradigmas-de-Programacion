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

def saludos(nombre:str): # ahorramos trabajo al interprete con el str
    """Funcion que saluda pero ahora por tu nombre:str"""
    print("Hola", nombre)

salu2("Julian")
a = 123
print(type(a))
saludos(a)

#=========================================
# Funciones con muchos argumentos
#=========================================
def saludos_multiples(nombre1,nombre2,nombre3):
    """Funcion que saluda a tres gentes"""
    print("Hola", nombre1, ", ", nombre2, " y ", nombre3)

saludos_multiples("Esteban","Daniel", "Luis")

def muchos_saludos(*nombres):
    """Funcion que saluda a muchas personas a la vez"""
    i = 0
    print("Hola ", end="") # end= es para ponerlo de corrido
    while len(nombres) > i:
        if (i==len(nombres)-1):
            print(nombres[i])
        else:
            print(nombres[i], end=",")
        i+=1
muchos_saludos("Juan","Emilio","Luis","Pablo","Arturo","Miguel","Manuel","Gabriel","Gael")


def greet(firstname, lastname):
    print("Hello", firstname, lastname)

greet(lastname="Jobs", firstname="Steve") # Llamamos la funciom con argumentos desordenados

#========================================
# Funcion con argumentos escondidos
#========================================
def greet(**person):
    print("Hello", person["firstname"], person["lastname"])

greet(lastname="Jobs", firstname="Steve") 
greet(firstname="Steve", lastname="Jobs")
greet(lastname="Escobar", firstname="Pablo", age=99) # podemops pasar mas argumentos y no se rompe

#=======================================
# Funcion con valores por defecto
#0======================================
def greet(name = "Guest"):
    print("Hello", name)
greet() # Guest
greet("Juan")

#==========================
# Funcion que retorna algo
#==========================
def suma(a, b):
    return a + b

total=suma(5, suma(10, 20)) #Podemos llamaar a la funcion para otro resultado de la funcion
print(total)

#===============================================
# Lambda
# nombre_funcion = lambda variable : funcion
#===============================================
x_al_cuadrado = lambda x : x * x

a1 = x_al_cuadrado(5)
print(a1)

suma = lambda x1, x2, x3 : x1+x2+x3
print(suma(99,98,97))

sumas = lambda *x : x[0]+x[1]+x[2]+x[3]
print(sumas(100,200,300,400))


print((lambda x: x*x)(6)) # Funcion anonima

#============================
# Funcion con variable global
#============================
name="Steve"
def greet():
    global name
    name = "Bill"
    print("Hello", name)

greet()

#_______________________________________________________
#|                                                      |
#|                  Inicio de Algoritmo                 |
#|______________________________________________________|
# Serie exponencial
# Factorizacion de x
# Negativos con funcion inversa 

n = 200
x = -100.0
flag = False
if x<0:
    flag = True
    x = -x
s = 1.0
for i in range(n,0,-1):
    s *= x/float(i)
    s+= 1.0
if flag == True:
    s = 1/s
print(s)


