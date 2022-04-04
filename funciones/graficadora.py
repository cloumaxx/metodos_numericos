import matplotlib.pyplot as plt
import math
import numpy as np


def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion


def ecuacion(funcion, x):
    return eval(remplazoFuncion(funcion, x))

def graficaTriangulo(rectangles,a,b,fx ):
    # GRAFICA
    # Puntos de muestra
    muestras = rectangles + 1
    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    # Linea suave
    muestraslinea = rectangles * 10 + 1
    xk = np.linspace(a, b, muestraslinea)
    fk = fx(xk)

    # Graficando
    plt.plot(xk, fk, label='f(x)')
    plt.plot(xi, fi, marker='o',
             color='orange', label='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Integral: Regla de Rectangulos')
    plt.legend()

    plt.fill_between(xi, 0, fi, color='g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')

    plt.show()
#graficaTriangulo(15,-5,10,lambda x: x**2-2*x+3)
def graficarFuncion(ecuacionUsar):
    msj = str(remplazoFuncion(ecuacionUsar,'x'))
    # Graficar positivamente
    xPositivo = np.arange(-200, 200, 0.1)
    plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo],label=msj,color="blue")

    plt.show()
    return plt
def graficadoraRecta(ecuacionUsar):
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    # Graficar positivamente
    xPositivo = np.arange(-200, 200, 0.1)
    plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj,color="purple")

    return plt

#graficarFuncion('x**2')