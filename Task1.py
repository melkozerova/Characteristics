import math
import pylab
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.colors import LinearSegmentedColormap


def F(U, m, n):
    return U[m][n]**2 / 2

#def C(U, m, n):
#    return -(2*U[m][n] + tn[n])

def df(U, m1, n1):
    return 1/(2*ht) + (U[m1][n1])/(2*hx)

def func(U,m2,n2):
    return (U[m2][n2] + U[m2-1][n2] - U[m2-1][n2-1] - U[m2][n2-1]) / (2*ht) + (F(U,m2,n2) + F(U,m2,n2-1) - F(U,m2-1,n2-1) - F(U,m2-1,n2))/(2*hx)

x1, x2 = 0, 1
t1, t2 = 0, 0.3
Nx, Nt = 100, 100
hx = abs(x2-x1)/Nx
ht = abs(t2-t1)/Nt
eps = 1e-5
xn = np.arange(x1, x2, hx)
tn = np.arange(t1, t2, ht)
U = [[0 for x in xn] for t in tn]

for t in range(Nt):
    U[0][t]= (2 - 4/math.pi * math.atan(2))*math.exp(-tn[t])
for x in range(Nx):
    U[x][0] = 4/math.pi * math.atan(xn[x] - 2) + 2


for t in range(Nt)[1:Nt]:
    for x in range(Nx)[1:Nx]:
        x0 = U[x-1][t-1]
        while abs(func(U,x,t))>eps:
            U[x][t] += - func(U, x, t)/df(U, x, t)

def makeData ():
    xgrid, ygrid = np.meshgrid(xn, tn)
    zgrid = np.array(U)
    return xgrid, ygrid, zgrid

x, y, z = makeData()

fig = pylab.figure()
axes = Axes3D(fig)

axes.plot_surface(x, y, z, rstride=3, cstride=3, cmap = LinearSegmentedColormap.from_list ("flower", ['#d71868', 'w', '#1cac78'], 256))

pylab.show()
