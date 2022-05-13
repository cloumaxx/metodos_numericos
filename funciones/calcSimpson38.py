import numpy as np
import sympy as sp
from math import *
from math import acos
import math

from funciones import  calcDerivadas as cD
#funciona el txt

def traductor(msj):
    msj=msj.replace('e(','exp(')
    msj=msj.replace('exp(','exp(')
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
def returnIntegral(funcion):
    funcion = traductor(funcion)
    funcion=cD.primerDerivada(funcion)
    return funcion

def f(x):
    return 2*np.pi*x*np.cos(x**2+1)*(x**2+1)#np.exp(-0.85*x)+np.cos(x)-0.95*x**2+3.25*x

def calcularRaiz(funcion,a,b,n):
    funcion= traductor(funcion)
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
    funcion = traductor(funcion)
    x = sp.symbols('x')
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    m1 = (2 * a + b) / 3
    m2 = (a + 2 * b) / 3
    integral = (b - a) / 8 * (f(a) + 3 * f(m1) + 3 * f(m2) + f(b))
    return integral

def calcularError(funcion,a,b,n):
    funcion = traductor(funcion)

    raiz = calcularRaiz(funcion,a,b,n)

    vt = np.exp(np.pi) / 2 + 1 / 2
    errorport = abs((vt - raiz) / vt)
    return  errorport
    #print('Error % =', errorport)

#calcularError('2*pi*x*cos(x**2+1)*(x**2+1)',0.75551,1.92676 ,50)
#print('-->',calcularRaiz('2*pi*x*math.acos(1)*(x**2+1)',0.75551,1.92676 ,50))
