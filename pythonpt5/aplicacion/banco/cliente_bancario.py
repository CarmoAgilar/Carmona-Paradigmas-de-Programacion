#=============================
# Clase ClienteBancario
#============================

class ClienteBancario:
    __nombres:str = None
    __apellidos:str = None
    __edad:int = 0
    __balanceDeCuenta:float = 0.0

    def __init__(self, nombres:str, apellidos:str, edad:int=0, bakanceDeCuenta:float=0.0):
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.nombres = nombres
        self.apellidos = apellidos
        self.__edad = edad
        self.balanceDeCuenta = balanceDeCuenta

    def getNombreCompleto(self) -> str:
        return self.nombres + " " + self.apellidos

    def __mandarEmail(self titulo:str, texto:str) -> None:
        print("mandar email: " + titulo + " contenido: " + texto)

    def __enviarBalanceAlBanco(self, cantidad:float) -> None:
        print("Enviar cantidad: " + str(cantidad) + " al banco...")

    def __validarEdad(self, edad:int) -> None:
        if edad < 18:
            raise Exception("Es menor de edad") #genera un error

    def imprimirInfo(self) -> str:
        return "Nombre: " + self.getNombreCompleto() + ", Edad: " + str(self.__edad) + ", Balance: " + str(self.__balanceDeCuenta)

    minuto 2:07 labo 6
