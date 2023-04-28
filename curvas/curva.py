#=======================================
# Codigo gigante de curvas
#=======================================
# Hecho por Julian Sagredo y entendido
#   por Diego Carmona
#=======================================
import numpy as np

class Curva:
    """================================================
       Objeto curva
       ================================================
       Parametros: x coordenada ordenada ((x1),(x2)...)
                   f propiedades  f1(x),f2(x)...)
                   dim dimensiones
       ================================================
    """
    def __init__(s, x:float=[], dim:int=3):

        s.x = np.array(x,dtype=np.float64)
        s.dim = dim
        s.n:np.int32 = int(len(s.x)/s.dim) # numero de puntos que hay
        s.l=[]      # longitud sobre la curva
        s.lista_de_puntos()
        s.longitud

    def lista_de_puntos(s) -> str:

        print(f"Numero de puntos = {str(s.n)}")

        s.formato = "" #formato de datos
        for j in range(s.dim):
            s.formato += "%15.8e"
        s.formato += "\n"

        for i in range(0,s.n):
            s.tup = (s.x[i],)

            for ii in range(1,s.dim):
                s.tup = s.tup + (s.x[i+ii*s.n],)
            print(s.formato % s.tup)

    def longitud(s) -> None: # longitud punto a punto
        t:np.float64 = 0.0
        for i in range(0,s.n):
            ip1 =i+1
            if i == s.n-1:
                ip1 = 0
            d:np.float64 = (s.x[ip1]-s.x[i])**2
            for j in range(1,s.dim):
                d += (s.x[ip1+j*s.n]-s.x[i+j*s.n])**2
            t += d**0.5
            s.l.append(t)
        s.L = t
        s.dx = t/float(s.n)

    def interpolacion(s,p:int=0,r:float=0.0) -> list:
        """ r es el parametro sobre la curva [0,1)
            p es la suavidad de la curva
        """

        rdx:np.float64 = 1.0/s.dx
        xi:float = []
        i:np.int32 = int(r*s.L*rdx)
        a:np.float64 = r*s.L*rdx - float(i) # distancia normalizada

        #=========================
        # Interpolacion lineal C0
        #=========================
        if p == 0:
            ip1:np.int32 = i+1
            if i == s.n-1:
                ip1 = 0
            xi.append(a*s.x[ip1] + (1.0-a)*s.x[i])
            for j in range(1,s.dim):
                xi.append(a*s.x[ip1+j*s.n] + (1.0-a)*s.x[i+j*s.n])

        #=========================
        # Interpolacion cubica C1
        #=========================

def zspline(puntos,dim,n,cont):

    curva = Curva(puntos,dim)
    dx:np.float64 = 1.0/float(n)
    x = np.zeros(n,dtype=np.float64)
    y = np.zeros(n,dtype=np.float64)

    for i in range(0,n):
        r:np.float64 = float(i)*dx
        [x[i],y[i]] = curva.interpolacion(cont,r)

    return x,y
