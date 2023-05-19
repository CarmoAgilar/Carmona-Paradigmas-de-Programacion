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
        s.longitud()

    def lista_de_puntos(s) -> str:

        print(f"Numero de puntos = {str(s.n)}")

        s.formato = "" #formato de datos
        for j in range(s.dim):
            s.formato += "%15.8e"
        s.formato += "\n"

        for i in range(0,s.n): # tupla de variables a imprimir
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
                d += (s.x[ip1+j*s.n]-s.x[i+j**s.n])**2
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
        elif p == 1:
            ip1:np.int32 = i+1
            ip2:np.int32 = i+2
            if i == s.n-1:
                ip1=0
                ip2=1
            if i == s.n-2:
                ip2=0
            im1:np.int32 = i-1
            if i == 0:
                im1 = s.n-1
            am1:np.float64 = a+1.0
            ap1:np.float64 = 1.0-a
            ap2:np.float64 = 2.0-a
            z:np.float64 = 1.0 - 2.5*a*a + 1.5*a*a*a
            zp1:np.float64 = 1.0 - 2.5*ap1*ap1 + 1.5*ap1*ap1*ap1
            zp2:np.float64 = 0.5*(2.0-ap2)*(2.0-ap2)*(1.0-ap2)
            zm1:np.float64 = 0.5*(2.0-am1)*(2.0-am1)*(1.0-am1)
            xi.append(zp1*s.x[ip1]+z*s.x[i]+zp2*s.x[ip2]+zm1*s.x[im1])
            for j in range(1,s.dim):
                xi.append(zp1*s.x[ip1+j*s.n]+z*s.x[i+j*s.n]+zp2*s.x[ip2+j*s.n]+zm1*s.x[im1+j*s.n])

        #=========================
        # Interpolacion quintica C2
        #=========================

        elif p == 2:
            ip1:np.int32 = i+1
            ip2:np.int32 = i+2
            ip3:np.int32 = i+3
            if i == s.n-1:
                ip1=0
                ip2=1
                ip3=2
            if i == s.n-2:
                ip2=0
                ip3=1
            if i == s.n-3:
                ip3=0
            im1:np.int32 = i-1
            im2:np.int32 = i-2
            if i == 0:
                im1 = s.n-1
                im2 = s.n-2
            if i == 1:
                im2 = s.n-1
            u12:np.float64 = 1.0/12.0    
            am1:np.float64 = a+1.0
            am2:np.float64 = a+2.0
            ap1:np.float64 = 1.0-a
            ap2:np.float64 = 2.0-a
            ap3:np.float64 = 3.0-a
            z:np.float64 = 1.0 + a*a*u12*(-15.0+a*(-35.0+a*(63.0+a*(-25.0))))
            zp1:np.float64 = 1.0 + ap1*ap1*u12*(-15.0+ap1*(-35.0+ap1*(63.0+ap1*(-25.0))))
            zp2:np.float64 = -4.0 + u12*ap2*(225.0+ap2*(-367.5+ap2*(272.0+ap2*(-94.5+12.5*ap2))))
            zp3:np.float64 = 18.0 + u12*ap3*(-459.0+ap3*(382.5+ap3*(-156.5+ap3*(31.5-2.5*ap3))))
            zm1:np.float64 = -4.0 + u12*am1*(225.0+am1*(-367.5+am1*(272.0+am1*(-94.5+12.5*am1))))
            zm2:np.float64 = 18.0 + u12*am2*(-459.0+am2*(382.5+am2*(-156.5+am2*(31.5-2.5*am2))))
            xi.append(zp1*s.x[ip1]+z*s.x[i]+zp2*s.x[ip2]+zp3*s.x[ip3]+zm1*s.x[im1]+zm2*s.x[im2])
            for j in range(1,s.dim):
                xi.append(zp1*s.x[ip1+j*s.n]+z*s.x[i+j*s.n]+zp2*s.x[ip2+j*s.n]+zp3*s.x[ip3+j*s.n]+zm1*s.x[im1+j*s.n]+zm2*s.x[im2+j*s.n])

        else:
            print("La suavidad debe ser 0, 1 o 2")

        return xi

#=========================================================
# Crea el Z-spline de los puntos en dim dimensiones
# n segmentos y continuidad (aprox) cont)
#x,y = zspline(conjunto de puntos, dim, n, continuidad)
#=========================================================

def zspline(puntos,dim,n,cont):

    curva = Curva(puntos,dim)
    dx:np.float64 = 1.0/float(n)
    x = np.zeros(n,dtype=np.float64)
    y = np.zeros(n,dtype=np.float64)

    for i in range(0,n):
        r:np.float64 = float(i)*dx
        [x[i],y[i]] = curva.interpolacion(cont,r)

    return x,y
