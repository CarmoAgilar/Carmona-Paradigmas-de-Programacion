from aplicacion.banco.cliente_bancario import ClienteBancario

#=============================================
# try intenta correr las instrucciones
# except atrapa el error en una variable
# la variable (e) se puede convertir en string
#=============================================

try: #Error por sacar mas dinero del que tiene
    cliente = ClienteBancario("Jaime Andrade", "Hernandez Sanchez", 28, 0.0)
    cliente.guardarDinero(300)
    print(cliente.imprimirInfo())
    cliente.retirarDinero(400)
    print(cliente.imprimirInfo())

# Exception es un objeto general para los errores
except Exception as e:
    print("Error: "+ str(e))


try: # Error por usar atributo privado
    print(cliente.__nombres)
except Exception as ex:
    print("Error: "+ str(ex))

print(cliente.nombres) #asi se imprime
