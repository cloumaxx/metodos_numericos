import numpy as np

from numpy.polynomial import Polynomial as pl
def calcularRaiz():
    arreglo = []
    arreglo.append(float(input('Ingresa el valor x al cubo (x^3): ')))
    arreglo.append(float(input('Ingresa el valor cuadratico(x^2): ')))
    arreglo.append(float(input('Ingresa el valor lineal ( x ):    ')))
    arreglo.append(float(input(('Ingresa el valor independiente:  '))))
    aux = np.roots(arreglo)


#calcularRaiz()
def returnRaices(x3,x2,x1,i):

    arreglo = []
    arreglo.append(float(x3))
    arreglo.append(float(x2))
    arreglo.append(float(x1))
    arreglo.append(float(i))
    print(arreglo)

    aux = np.roots(arreglo)
    return aux