import sympy as sp

import math
from funciones import graficadora,calcDerivadas as calD
import matplotlib.pyplot as plt


# vx= valor inicial de x
# tol= rango de tolerancia (error maximo)
# n= numero de iteraciones
def NewtonRaphson():
    x0 = 2#input('Diga el valor de x  ')  # Se ingresa el valor de x
    tol = 0.001#input('Diga el rango maximo de tolerancia:  ')  # Se ingresa el rango de tolerancia
    n = 50
    x0 = float(x0)
    tol = float(tol)
    n = int(n)

    x = sp.symbols('x')  # Crea variable x
    f = 'x**2+2'#input('Diga la funcion en variable x:  ')  # Se ingresa la funcion a evaluar
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
    #print('-->',x1)

def calculoRaiz(funcion,x_0,Error_t):
    raiz=0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = calD.primerDerivada(funcion)
    df = str(df).replace('atan','math.atan')
    df = str(df).replace('pi','math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')
    df = str(df).replace('sqrt', 'math.sqrt')
    funcion = str(funcion).replace('atan', 'math.atan')
    funcion = str(funcion).replace('asin', 'math.asin')
    funcion = str(funcion).replace('acos', 'math.acos')
    funcion = str(funcion).replace('sqrt', 'math.sqrt')
    funcion = str(funcion).replace('pi', 'math.pi')
    #sp.diff(funcion)  # Sacamos la derivada de la funcion

    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    contador=1
    i=1
    ri_arreglo=[]
    ri_arreglo.append(0)

    salir = False
    while salir == False :
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salir = True
        else:
            x0=xr
            i += 1

    return raiz

def calculoError(funcion,x_0,Error_t):
    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = calD.primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')
    df = str(df).replace('sqrt', 'math.sqrt')
    df = str(df).replace('pi','math.pi')
    funcion = str(funcion).replace('atan', 'math.atan')
    funcion = str(funcion).replace('asin', 'math.asin')
    funcion = str(funcion).replace('acos', 'math.acos')
    funcion = str(funcion).replace('sqrt', 'math.sqrt')
    funcion = str(funcion).replace('pi', 'math.pi')

    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    salida=0
    salir = False
    while salir == False:
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salida = E_r
            salir = True
        else:
            x0 = xr
            i += 1

    return salida

EjeTama = 500
ejeTama2 = -500
def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion
def graficaTotal(funcion,x_0 ,Error_t):
    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = calD.primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('pi', 'math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')
    df = str(df).replace('sqrt', 'math.sqrt')
    df = str(df).replace('log','math.log')
    funcion = str(funcion).replace('log','math.log')
    funcion = str(funcion).replace('atan', 'math.atan')
    funcion = str(funcion).replace('asin', 'math.asin')
    funcion = str(funcion).replace('acos', 'math.acos')
    funcion = str(funcion).replace('sqrt', 'math.sqrt')
    funcion = str(funcion).replace('pi', 'math.pi')
    # sp.diff(funcion)  # Sacamos la derivada de la funcion

    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f

    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    contador = 1
    i = 1
    ri_arreglo = []
    ri_arreglo.append(0)

    salir = False
    while salir == False:
        xr = x0 - (f(x0) / df(x0))
        ri_arreglo.append(xr)
        E_r = abs((ri_arreglo[i - 1] - ri_arreglo[i]) / ri_arreglo[i])
        if i >= 50 or E_r < float(Error_t):
            raiz = xr
            salir = True
        else:
            x0 = xr
            i += 1
    f=str(eval(remplazoFuncion(funcion,x_0)))
    y = "(("+''+")*(x-("+")))+("+f+")"
    #graficadora.graficadoraRecta(y)
    #plt.plot(raiz,0, marker="X", color="green", label=("Raiz: "+str(raiz)))
    plt.ylim(-200,200)
    plt.xlim(-200,200)

    #plt.legend()
    plt.show()
def funcionPrincipal(funcion, intervaloA):
    intervaloA=int(intervaloA)
    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    return plt