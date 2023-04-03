""" ESTE ES UN SUPERCOMENTARIO
    DE INICIO A NUESTRO RESUMEN
"""
#============================
# Carmona Aguilar Diego
#     Curso python 2
#============================
even_nums = {2, 4, 6, 8, 10} # Conjunto de numeros pares
print(even_nums)

# El bool no es parte del conjunto
emp = {1, "Steve", 10.5, True}
print(emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print(nums)

#===========================================
# Convertir secuencia a conjunto
# No lo genera en orden
#===========================================
s = set("Hello") # conjunto de 5 letras sin orden
print(s)
s = set((1,2,3,4,5)) # tupla
print(s)

#============================================
# Diccionario -> Conjunto: conjunto de llaves
#============================================
d = {1:"One", 2:"Two"}
s = set(d)
print(s)

print("Impresion sin set()", d)

s.add(100) #agregar 100
print(s)

s.update(nums)
print(s)

s.remove(100)
print(s)

s1={1,2,3,4,5}
s2={4,5,6,7,8}

su = s1|s2 # Union
print(su)

si = s1&s2
print(si)

# Diccionarios
capitals = {"USA":"Washington D.C", "France":"Paris", "India":"New Delhi"}
print(capitals)

d = {} # diccionario vacio

# Llave entera: valor string
numMames = {1:"One", 2:"Two", 3:"Three"}

# Llave real: string
decNames = {2.5:"One and half", 2.5:"Two and half", 3.5:"Three amd half"}

# Llave tupla: string
items = {("Parker", "Reynolds", "Camlin"):"pen", ("LG", "Whirlpool", "Samsung"): "Refrigerator"}

# Llave string: entero
romanNums = {"I":1, "II":2, "III":3, "IV":4, "V":5}
print(romanNums)
print(romanNums["I"])

print(capitals.get("India"))
print(capitals.get("India")) # funciona igual

# reportar llave  y valor
for k in capitals:
    print("Key = "+k+", Value = "+capitals[k])

# añadir dato en el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

del capitals["Mexico"] # borrar dato
print(capitals)
del capitals #borrar diccionario
# print(capitals)
"""Ya no hay diccionario que imprimir"""


print(romanNums.keys()) # Reportado de llaves
print(romanNums.values()) # Reportado de valores

# juicio de llaves
print("I" in romanNums)
print("XX" in romanNums)
print("XX" not in romanNums)

#_______________________________________________________
#|                                                      |
#|                  Inicio de segunda parte             |
#|______________________________________________________|

miprimeralista = [] # vacia
print(miprimeralista)

#======================================================
# Llenado de la lista
#======================================================
miprimeralista = [1,"Javier", 1.34,"Bosco","Angel","Abigail", True]
print(miprimeralista)

#### List: hacer una lista

nums = list(range(1,61))
for i in nums:
    print(i) #muchos numeros

nums.append(61)
nums.append(62) # añadir elementos
nums.append(61)
print(nums)

nums.remove(61) # borrar elementos
print(nums)

i=61
del nums[i] # borrar elemento con indice i
print(nums)

del nums #borrar lista

#=================================
# operaciones con listas
#=================================
### Suma
L1 = [1,2,3]
L2 = [4,5,6]
print(L1+L2)
### Llenado
potencial = []
for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])
### "Ordenar" la lista (hacer una tupla)
potencial = tuple(potencial)
print(potencial[100])


