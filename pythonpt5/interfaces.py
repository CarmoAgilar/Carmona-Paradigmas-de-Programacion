from aplicacion.repositorio.basededatos import BaseDeDatos
# busca en el directorio aplicacion basededatos.py, e importa el objeto BaseDeDatos para traerlo

from aplicacion.repositorio.s3 import S3
# ahora busca hasta repositorio para traer de s3.py el objeto S3

from aplicacion.repositorio.sistemadearchivos import SistemaDeArchivos
# lo mismo de arriba para traer SistemaDeArchivos

from aplicacion.modelos.usuario import Usuario
# trae objeto Usuario

from aplicacion.negocios.manejodeinscripciones import ManejoDeInscripciones
# trae objeto ManejoDe...

#====================================
#Creamos los objetos usuarios y s3
usuario = Usuario("Roberto","Jimenez",18)
repositorioS3 = S3("321321321","sdf324223","MiCubeta")

#=======================================================
# interface inscribir usuario del objeto ManejoDeInscripciones
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioS3)
print("\n")

#=========================================================
#objeto sistemadearchivos
repositorioSistemaDeArchivos = SistemaDeArchivos("/home/user")

#=======================================================
# interface inscribir usuario del objeto ManejoDeInscripciones
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioSistemaDeArchivos)
print("\n")

#====================
# objeto basededatos
repositorioBaseDeDatos = BaseDeDatos("localhost","admin","admin123")

#=======================================================
# interface inscribir usuario del objeto ManejoDeInscripciones
ManejoDeInscripciones.inscribirUsuario(usuario,repositorioBaseDeDatos)
print("\n")

