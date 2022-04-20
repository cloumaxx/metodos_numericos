import numpy as np
import sympy as sp
from math import *
def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion


def secante(funcion1, inferior, superior, tolerancia, repeticiones):
    x = sp.symbols('x')  # Crea variable x
    funcion = sp.lambdify(x, funcion1)
    error = abs(superior - inferior)
    print('Iteracion {:<2}: p_{:<2}={:.7f}'.format(0, 0, inferior))
    print('Iteracion {:<2}: p_{:<2}={:.7f},error={:.7f}'.format(1, 1, superior, error))
    i = 2
    while i <= repeticiones:
        if funcion(superior) == funcion(inferior):
            print('Solucion no encontrada')
            return None

        aux = inferior - (funcion(inferior) * (superior - inferior)) / (funcion(superior) - funcion(inferior))
        error = abs(aux - superior)
        print('Iteracion {:<2}: p_{:<2}={:.7f},error={:.7f}'.format(i, i, aux, error))

        if error < tolerancia:
            print('Solucion encontrada x={:.7f} , iteraciones: {}'.format(aux, i))
            return aux

        inferior = superior
        superior = aux
        i += 1
    print('Solucion no encontrada, iteraciones agotadas: {}'.format(i - 1))
    return None


def funcion2(x):
    return x ** x - 100


#secante(funcion2, 3, 4.2, 0.001, 10)
#print(secante(funcion, 3, 4.2, 0.001, 10))
"""
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
"""