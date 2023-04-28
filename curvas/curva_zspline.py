#=====================================
# Curvas Z-splines en n dimensiones
#=====================================
# Diego Carmona
import numpy as np
from curva import Curva, zspline
import matplotlib.pyplot as plt
import math
#=========================
# Conjunto de puntos
#=========================
# numero de puntos
nump:np.int32 = 8
# dimension
dim:np.int32 = 2
# memoria para puntos
puntos = np.zeros(dim*nump,dtype=np.float64)
# paramerizacion
X = np.linspace(0.0,2*np.pi,nump+1)
# coordenada X
puntos[0:nump] = np.cos(X[0:nump]) + 0.0*np.sin(2*X[0:nump])
# coordenada Y
puntos[nump:2*nump] = np.sin(X[0:nump]) + 0.0*np.sin(2*X[0:nump])

#===============================================================
# Curva z-spline de n puntos zspline(p,d,n,m)
# p: puntos, d: dimension, n: segmentos de curva, m: continuidad
#===============================================================
n:np.int32 = 1000
x1,y1 = zspline(puntos,dim,n,2)
x2,y2 = zspline(puntos,dim,n,1)
x3,y3 = zspline(puntos,dim,n,0)
plt.plot(x3,y3,lw=2,color="orange")
plt.plot(x2,y2,lw=2,color="red")
plt.plot(x1,y1,lw=2,color="blue")


