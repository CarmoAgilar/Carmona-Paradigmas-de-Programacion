import random
import matplotlib.pyplot as plt # biblioteca para graficar
import matplotlib.patches as patches

class Partucula():
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
class Nodo():
    def __init__(self, x0:float, y0:float, w:float, h:float, particulas):
        self.x0 = x0
        self.y0 = y0
        self.ancho = w
        self.alto = h
        self.particulas = particulas
        self.hijos = []

    def get_ancho(self):
        return self.ancho
    def get_alto(self):
        return self.alto
    def get_particulas(self):
        return self.particulas


def subdivision_recursiva(nodo:Nodo, k:int):
    if len(nodo.particulas)<=k:
        return

    w_ = float(0.5*nodo.ancho)
    h_ = float(0.5*nodo.alto)

    p = cuantas_contiene(nodo.x0, nodo.y0, w_, h_, nodo.particulas)
    nodo.x1 = Nodo(nodo.x0, nodo.y0, w_, h_, p)
    subdivision_recursiva(nodo.x1, k)

    p = cuantas_contiene(nodo.x0, nodo.y0+h_, w_, h_, nodo.particulas)
    nodo.x2 = Nodo(nodo.x0, nodo.y0+h_, w_, h_, p)
    subdivision_recursiva(nodo.x2, k)

    p = cuantas_contiene(nodo.x0+w_, nodo.y0, w_, h_, nodo.particulas)
    nodo.x3 = Nodo(nodo.x0+w_, nodo.y0, w_, h_, p)
    subdivision_recursiva(nodo.x3, k)

    p = cuantas_contiene(nodo.x0+w_, nodo.y0+h_, w_, h_, nodo.particulas)
    nodo.x4 = Nodo(nodo.x0+w_, nodo.y0+h_, w_, h_, p)
    subdivision_recursiva(nodo.x4, k)

    nodo.hijos = [nodo.x1, nodo.x2, nodo.x3, nodo.x4]

    minuto 1;48 del lab 8.1


