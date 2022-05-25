import numpy as np


def suma(m,n):
    salida = np.array(m)+np.array(n)
    return salida


def resta(m,n):
    salida = np.array(m)-np.array(n)
    return salida


def producto(m,n):
    salida= np.dot(m,n)
    return salida


def determinante(m):
    return np.linalg.det(m)


def inversa(m):
    return np.linalg.inv(m)


def transpuesta(m):
    return np.transpose(m)
a=np.array([[3,4,-1],[2,0,1],[1,3,-2]])
