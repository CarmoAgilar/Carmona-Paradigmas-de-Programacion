#==============
# clase Usuario
#==============
class Usuario:
    __nombre: str
    __apellido: str
    __edad: int

    def __init__(mi, nombre: str, apellido: str, edad: int):
        mi.__nombre = nombre
        mi.__apellido = apellido
        mi.__edad = edad

    # Getters
    def getNombre(mi) -> str:
        return mi.__nombre

    def getApellido(mi) -> str:
        return mi.__apellido

    def getEdad(mi) -> int:
        return mi.__edad

