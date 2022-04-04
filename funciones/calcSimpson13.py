import numpy as np
import sympy as sp
from math import *


def f(x):
    return np.exp(x) * np.sin(x)


def s13(funcion, a, b):
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    m = (a + b) / 2
    integral = (b - a) / 6 * (f(a) + 4 * f(m) + f(b))
    return integral
def calculaRaiz(funcion,a,b,n):
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    h = (b - a) / n
    suma = 0

    for i in range(n):
        b = a + h
        area = s13(funcion, a, b)
        suma += area
        a = b

    return suma
def calculaError(funcion, a, b,n):
    raiz = calculaRaiz(funcion, a, b,n)
    vt = np.exp(np.pi) / 2 + 1 / 2
    errorport = abs((vt - raiz) / vt)
    return errorport
#calculaError('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)

#calculaRaiz('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)


"""
a = 0  # Limite inferior
b = np.pi  # Limite superior
n = 10  # Intervalos
h = (b - a) / n
suma = 0

for i in range(n):
    b = a + h
    area = s13(f, a, b)
    suma += area
    a = b

print(suma)
vt = np.exp(np.pi) / 2 + 1 / 2
errorport = abs((vt - suma) / vt) * 100
print('Error % =', errorport)"""