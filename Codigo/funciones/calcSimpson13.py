import numpy as np
import sympy as sp
from math import *
from funciones import calcDerivadas as cD
def traductor(msj):
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', 'math.sqrt(')

    msj = msj.replace('e(', 'exp(')
    msj = msj.replace('exp(', 'exp(')
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
def f(x):
    return np.exp(x) * np.sin(x)
def returnIntegral(funcion):
    funcion= traductor(funcion)
    funcion=cD.primerDerivada(funcion)
    return funcion
def s13(funcion, a, b):
    funcion=traductor(funcion)
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    m = (a + b) / 2
    integral = (b - a) / 6 * (f(a) + 4 * f(m) + f(b))
    return integral
def calculaRaiz(funcion,a,b,n):
    funcion=traductor(funcion)
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
    funcion=traductor(funcion)
    raiz = calculaRaiz(funcion, a, b,n)
    vt = np.exp(np.pi) / 2 + 1 / 2
    errorport = abs((vt - raiz) / vt)
    return errorport
#calculaError('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)

#calculaRaiz('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)

