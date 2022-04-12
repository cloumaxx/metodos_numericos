import numpy as np
import sympy as sp
from sympy import *
import matplotlib.pyplot as plt

def returnRaiz(expresionf,LimInf,LimSup,NumPar):
    x = symbols('x')
    f = sp.lambdify(x, expresionf, "numpy")
    Pab = np.linspace(LimInf, LimSup, NumPar, endpoint=True)
    hPm = ((Pab[0] + Pab[1]) / 2) - LimInf
    PmPab = Pab + hPm
    fPm = f(PmPab)
    ARect = 2 * hPm * fPm
    IntegralNum = np.sum(ARect)
    return IntegralNum
def mostrarGrafica(fx,a,b,tramos):
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)
    muestras = tramos + 1
    h = (b - a) / tramos
    xi = a
    suma = 0
    for i in range(0, tramos, 1):
        Atrapecio = h * (fx(xi) + fx(xi + h)) / 2
        suma = suma + Atrapecio
        xi = xi + h
    integral = suma

    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    muestrasLinea = muestras * 10
    xk = np.linspace(a, b, muestrasLinea)
    fk = fx(xk)

    plt.plot(xi, fi, 'ro')
    plt.plot(xk, fk)

    plt.fill_between(xi, 0, fi, color='g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')
    plt.show()
"""
x = symbols('x')
expresionf = input('Intruduce la funcion ')
f = sp.lambdify(x, expresionf, "numpy")

LimInf = float(input('Intruduzca el limite inferior '))

LimSup = float(input('Introduzca el limite superior '))

NumPar = int(input('Introduzca el numero de particiones '))

Pab = np.linspace(LimInf, LimSup, NumPar, endpoint=True)
print(Pab)  # Y

hPm = ((Pab[0] + Pab[1]) / 2) - LimInf
PmPab = Pab + hPm
print(PmPab)

fPm = f(PmPab)
print(fPm)  # x

ARect = 2 * hPm * fPm
print(ARect)

IntegralNum = np.sum(ARect)
print('La aproximacion a la integral es: ', IntegralNum)

# https://es.planetcalc.com/5494/
"""