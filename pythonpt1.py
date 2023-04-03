""" ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
"""
#============================
# Carmona Aguilar Diego
#============================
#----------------------------
# Primer codigo subido
#---------------------------

print (2+3)    #suma
print (2*2)    #multiplicacion
print (2/3)    #division
print (2**10)  #exponent
print (10%2)   #modulo
print (10%0.1) #quien sabe

#=========================================
# Para saber el tipo de objeto se usa type
#=========================================
t = 0
print(type(t)) # entero
t=3.6
print(type(t)) # real
t=True   #True con T mayuscula
print(type(t)) # booleano

#===================================
# Mensajes a pantalla
#===================================
#(Se pueden poner los parentesis separados a los prints)

print ("Este es un comando de python. ", "Este es otro enunciado.", t)
print("id: ", 1)
print("First Name: ", "Steve")
print("lASt Name: ", "Jobs")
print("vamos a sumar esto" + " con esto otro")

#=============================================
# Continuar una instruccion en varios renglones
#=============================================
if 100 > 99 and \
    200 <= 300 and \
    True !=False:
        print("Hello World!")

#=======================================
# Comandos diferentes en la misma linea
#=======================================
print("Hola "); print("tu!!") # Mala practica 

#======================================
# Listas y matrices
#======================================

list = [1, 2, 3, 4,
        5, 6, 7, 8,
        9, 10, 11, 12]

matriz = [ [1,2,3,4],[5,6,7,8],[9,10,11,12] ]

print(list)
print(matriz)

#========================================================
# Identacion estricta con instrucciones con doble punto :
#========================================================
if 10>5:
    print ("diez es mayor que cinco")
    print("otra identacion")
for i in list:
    print(i)
    print("ok")
if 10>5:
    print("verdadero")
    if 10<20:
        print("verdadero")
elif 5>3:
    print("esto no se imprimira")
else:
    print("Aqui nunca llega")

#============
# Funciones
#============
def say_hello(name):
    print("Hello ", name)
    print("Welcome to pyhton tutorials")

say_hello("Carmo")
#_______________________________________________________
#|                                                      |
#|                  Inicio dee Intro2                   |
#|______________________________________________________|

#input obtiene datos del prompter

nombre = input("Dame tu nombre: ")
print("Hola como estás ", nombre)

#========================================
# los enteros tienen presicion ilimitada
#========================================
y = 500000000000000000000000000000000
print(y)
#se puede escribir el numero separado en miles con _
y=5_000_000
print(y)

#==========================================
# La funcion int() cambia strings a enteros
#==========================================

numero = int(input("Dame tu edad: "))
type(numero)

#La notacion cientifica aparecde como la calculadora del celular

y = 1.2E-09 #== 1.2 x 10**-9
print(y)

#==========================================
# La funcion float() cambia strings a reales
#==========================================

y = float("14.3")
print(y)

#=========================================
# Los complejos se escriben 1+1j
# el numero imaginario es j, no i
#=========================================
z = 1+1j

# Otras funciones:
# // piso
# complex()
# abs()
# round()
# pow()

print(round(3.14159,4))

#==========================================
# strings de varias lineas
#==========================================

parrafo = """En el bosque de la china
 la chinita se perdio """
print(parrafo)

 #funcion len() obtiene el tamaño de un string
print(len(parrafo))

# las letras del string ocupan lugares como en un arreglo

palabra = "hola"
print(palabra[0])
print(palabra[-4])

#________________________________________________________
