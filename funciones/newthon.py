import sympy as sp
from math import *


# vx= valor inicial de x
# tol= rango de tolerancia (error maximo)
# n= numero de iteraciones
def NewtonRaphson():
    x0 = 2#input('Diga el valor de x  ')  # Se ingresa el valor de x
    tol = 0.001#input('Diga el rango maximo de tolerancia:  ')  # Se ingresa el rango de tolerancia
    n = 100#input('Diga la cantidad maxima de iteraciones: ')  # Se ingresa la cantidad de iteraciones
    x0 = float(x0)
    tol = float(tol)
    n = int(n)

    x = sp.symbols('x')  # Crea variable x
    f = '80*exp(-2*x)+20*exp(-0.5*x)'#input('Diga la funcion en variable x:  ')  # Se ingresa la funcion a evaluar
    df = sp.diff(f)  # Sacamos la derivada de la funcion
    f = sp.lambdify(x, f)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df

    for i in range(n):
        x1 = x0 - f(x0) / df(x0)
        if (abs(x1 - x0) < tol):  # If para parar finalizar el programa cuando encontremos una buen rango
            print('x', i + 1, ' = ', x1, ": Mejor aproximacion.")
            return
        x0 = x1
        print('x', i + 1, ' = ', x1)


