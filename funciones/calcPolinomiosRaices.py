import numpy as np

from numpy.polynomial import Polynomial as pl
def calcularRaiz():
    arreglo = []
    arreglo.append(float(input('Ingresa el valor x al cubo (x^3): ')))
    arreglo.append(float(input('Ingresa el valor cuadratico(x^2): ')))
    arreglo.append(float(input('Ingresa el valor lineal ( x ):    ')))
    arreglo.append(float(input(('Ingresa el valor independiente:  '))))
    aux = np.roots(arreglo)

"""    print(aux,type(aux))
    try:
        print('-->', aux[0])
    except:
        print()

    try:
        print('-->', aux[1])
    except:
        print()


    try:
        print('-->', aux[2])
    except:
        print()

        try:
            print('-->', aux[3])
        except:
            print()
"""

#calcularRaiz()
def returnRaices(x3,x2,x1,i):
    print('entro')

    arreglo = []
    arreglo.append(float(x3))
    arreglo.append(float(x2))
    arreglo.append(float(x1))
    arreglo.append(float(i))
    print(arreglo)

    aux = np.roots(arreglo)
    print(aux)
    return aux