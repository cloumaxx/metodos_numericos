import numpy as np
import sympy as sp
from math import *


def f(x):
    return 2*np.pi*x*np.cos(x**2+1)*(x**2+1)#np.exp(-0.85*x)+np.cos(x)-0.95*x**2+3.25*x

def calcularRaiz(funcion,a,b,n):
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    h = (b - a) / n
    suma = 0

    for i in range(n):
        b = a + h
        area = s38(funcion, a, b)
        suma += area
        a = b
    return suma

def s38(funcion, a, b):
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    m1 = (2 * a + b) / 3
    m2 = (a + 2 * b) / 3
    integral = (b - a) / 8 * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
    return integral

def calcularError(funcion,a,b,n):
    raiz = calcularRaiz(funcion,a,b,n)

    vt = np.exp(np.pi) / 2 + 1 / 2
    errorport = abs((vt - raiz) / vt)
    return  errorport
    #print('Error % =', errorport)

#calcularError('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)
#calcularRaiz('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)
"""

a = 0.75551  # Limite inferior
b = 1.92676  # Limite superior
n = 50  # Intervalos
h = (b - a) / n
suma = 0

for i in range(n):
    b = a + h
    area = s38(f, a, b)
    suma += area
    a = b

print(suma)
vt = np.exp(np.pi) / 2 + 1 / 2
errorport = abs((vt - suma) / vt)
print('Error % =', errorport)"""