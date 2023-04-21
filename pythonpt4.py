#============
# POO
#============

class ObjetoVacio:
    pass # Para ser vacion necesita esta palabra

nada = ObjetoVacio()
print(type(nada))

class Llanta:
    
    cuenta = 0 #variable de toda la clase

    def __init__(mi,radio=50,ancho=30,presion=1.5):
        """Funcion constructora, reservada 
        comienca con uno mismo: self o mi"""
        Llanta.cuenta += 1
        #Variables exclusivas de cada objeto
        mi.radio = radio
        mi.ancho = ancho
        mi.presion = presion

#======================
# Objetos instanciados
#======================
Llanta1 = Llanta(50,30,1.5)
Llanta2 = Llanta(presion=1.2)
Llanta3 = Llanta()
Llanta4 = Llanta(40,30,1.6)

class Coche: #Objeto que contiene otros objetos
    def __init__(mi,ll1,ll2,ll3,ll4):
        mi.llanta1 = ll1
        mi.llanta2 = ll2
        mi.llanta3 = ll3
        mi.llanta4 = ll4

micoche = Coche(Llanta1,Llanta2,Llanta3,Llanta4)

print("Total de llantas: ",Llanta.cuenta)
print("Presion de la llanta 4 = ",Llanta4.presion)
print("Radio de la llanta 4 = ",Llanta4.radio)
print("Radio de la llanta 3 = ",Llanta3.radio)
print("Presion de la llanta 1 de micoche = ",micoche.llanta1.presion)

#===========================
# Encapsulamiento
#===========================
# Uso de la funcion de python property para poner y obtener atributos

class Estudiante:
    def __init__(mi):
        mi.__nombre = ""
    def ponerme_nombre(mi, nombre):
        print("se llamó a ponerme_nombre")
        mi.__nombre = nombre
    def obtener_nombre(mi):
        print("se llamó a obtener nombre")
        return mi.__nombre
    nombre = property(obtener_nombre,ponerme_nombre)

estudiante = Estudiante() #objeto estudiante sin nombre
estudiante.nombre = "Diego" #(yo)

#Obtener nombre sin llamar a la funcion explicitamente
# __nombre es una variable privada y print(estudiante.__nombre) no sirve)
print(estudiante.nombre)

#==========================
# Herencia de clases
#==========================
class Cuadrilatero:
    def __init__(mi, a, b, c, d):
        mi.lado1=a
        mi.lado2=b
        mi.lado3=c
        mi.lado4=d

    def perimetro(mi):
        p= mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
        print("Perimetro = ",p)
        return p

class Rectangulo(Cuadrilatero): #hijo de cuadrilatero
    def __init_(self, a, b):
        super().__init__(a ,b ,a ,b) # constructor de su madre

class Cuadrado(Rectangulo): #nieto de cuadrilatero
    def __init__(self, a):
        super().__init__(a,a)

    def area(self):
        area = self.lado1**2
        return area

cuadrado1 = Cuadrado(5)

print("Perimetro = ", cuadrado1.perimetro())
print("Area = ", cuadrado1.area())





