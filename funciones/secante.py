import numpy as np
import sympy as sp
from math import *


def secante(fx, xa, tolera):

    dx = 4 * tolera
    xb = xa + dx
    tramo = dx
    tabla = []
    while (tramo >= tolera):
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa * (xb - xa) / (fb - fa)
        tramo = abs(xc - xa)

        tabla.append([xa, xb, xc, tramo])
        xb = xa
        xa = xc

    tabla = np.array(tabla)
    return (tabla)
def control():
    tolera = input('Diga el rango maximo de tolerancia:  ')  # Se ingresa el rango de tolerancia
    x = sp.symbols('x')  # Crea variable x
    fx = input('Diga la funcion en variable x:  ')  # Se ingresa la funcion a evaluar
    fx = sp.lambdify(x, fx)  # Creamos simbolicamente a f
    xa = input('Diga el valor de x  ')  # Se ingresa el valor de x
    xa = int(xa)

    tabla = secante(fx, float(xa), float(tolera))
    n = len(tabla)
    raiz = tabla[n - 1, 2]

    np.set_printoptions(precision=4)
    print('[xa ,\t xb , \t xc , \t tramo]')
    for i in range(0, n, 1):
        print(tabla[i])
    print('raiz en: ', raiz)
