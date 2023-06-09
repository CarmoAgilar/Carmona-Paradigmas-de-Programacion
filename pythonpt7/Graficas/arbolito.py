#================================================
# Graficas usando la tortuga que pinta al caminar
#0===============================================
import turtle
tortuga = turtle.Turtle()
tortuga.left(90) # giro a la izquierda de 90 grados
tortuga.speed(500) 

# con angulos de 90 es un arbol H
angulo:float = 90

# el arbol se construye con recursividad
def arbol(i:float,angulo:float):
    if i < 10.0:
        return
    else:
        tortuga.forward(i) # avanza i
        tortuga.left(angulo) 
        arbol(3.0*i/4.25,angulo)
        tortuga.left(angulo)
        tortuga.backward(i) # retrocede i

arbol(100,angulo)
turtle.done()
