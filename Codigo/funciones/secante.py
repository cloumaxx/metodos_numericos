import numpy as np
import sympy as sp
from math import *
import matplotlib as plt
from funciones import graficadora
def traductor(msj):
    msj = msj.replace('e(', 'exp(')
    msj= msj.replace('exp(','<!>')

    msj = msj.replace('<!>','exp(')
    msj = msj.replace('sin(', 'sin(')
    msj = msj.replace('sen(', 'sin(')
    msj = msj.replace('cos(', 'cos(')
    msj = msj.replace('tan(', 'tan(')
    msj = msj.replace('sec(', 'math.asin(')
    msj = msj.replace('csc(', 'math.acos(')
    msj = msj.replace('cot(', 'math.atan(')
    msj = msj.replace('ln(', 'math.log(')
    msj = msj.replace('π','math.pi')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', 'math.sqrt(')
    msj = msj.replace('^', '**')
    return msj
def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion

def graficaRecta2(x1, y1, x2, y2):
    m = (y2 - y1) / (x2 - x1)
    aux = m * x1
    b = y1 - aux
    funcion = "(" + str(m) + "*x)+" + str(b)
    return funcion
def funcionPrincipal(funcion, intervaloA, intervaloB,raiz ):
    funcion=traductor(funcion)
    intervaloA=int(intervaloA)
    intervaloB=int(intervaloB)

    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    plt.plot(intervaloB, 0, marker="o", color="orange", label="Coordenada B")
    plt.plot(raiz,0, marker="X", color="green", label=("Raiz: "+str(raiz)))

    plt.legend()
    #plt.grid()
    plt.show()


def secante(funcion1, inferior, superior, tolerancia, repeticiones):
        fx=funcion1
        x = sp.symbols('x')  # Crea variable x
        fx = sp.lambdify(x, fx)  # Creamos simbolicamente a f

        xa = inferior
        xb = superior
        tolera = tolerancia
        tramo = repeticiones

        while (tramo >= tolera):
            fa = fx(xa)
            fb = fx(xb)
            xc = xa - fa * (xb - xa) / (fb - fa)
            tramo = abs(xc - xa)
            xb = xa
            xa = xc

        return xc
print(secante('exp(-2*x**2)+sin(x)-0.1*x',-2,-4,0.01,10))
"""funcion1=traductor(funcion1)
    x = sp.symbols('x')  # Crea variable x
    funcion = sp.lambdify(x, funcion1)
    error = abs(superior - inferior)
    i = 2
    while i <= repeticiones:
        if funcion(superior) == funcion(inferior):
            return None

        aux = inferior - (funcion(inferior) * (superior - inferior)) / (funcion(superior) - funcion(inferior))
        error = abs(aux - superior)

        if error < tolerancia:
            return aux

        inferior = superior
        superior = aux
        i += 1
    return None"""


def funcion2(x):
    return x ** x - 100

