from aplicacion.modelos.usuario import Usuario
from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios

#===================
# clase storemanager
# no tiene variables
#===================
class ManejoDeInscripciones:

    #decorador:
    @staticmethod
    #envuelve la funcion sin llamar variables locales
    def inscribirUsuario(usuario: Usuario, repositorioDeUsuarios: RepositorioDeUsuarios) -> None:
        print("------> Guardandousuario ... \n")
        repositorioDeUsuarios.abrir()
        repositorioDeUsuarios.guardar(usuario)
        repositorioDeUsuarios.cerrar()
