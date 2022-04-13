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
    print('funcion: ',funcion)
    funcion=funcion.replace('math.exp','exp')
    print('funcion: ', funcion)
    df = calD.primeraDerivadaNewton(funcion)#sp.diff(funcion)  # Sacamos la derivada de la funcion
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
    df = sp.diff(funcion)  # Sacamos la derivada de la funcion
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
    accion = elemeto.replace('x', usar)
    return accion
def graficaTotal(funcion,intervaloA ,error ):
    funcion=funcion.replace('exp','math.exp')
    raiz = 0
    x = sp.symbols('x')  # Crea variable x
    df = sp.diff(funcion)  # Sacamos la derivada de la funcion
    f = sp.lambdify(x, funcion)  # Creamos simbolicamente a f
    df = sp.lambdify(x, df)  # Creamos simbolicamente a df
    i = 1
    funcionPrincipal(funcion,intervaloA)
    j=str(df(intervaloA))
    f=str(eval(remplazoFuncion(funcion,intervaloA)))
    y = "(("+j+")*(x-("+intervaloA+")))+("+f+")"
    #graficadora.graficadoraRecta(y)
    raiz =calculoRaiz(funcion,intervaloA,error )
    plt.plot(raiz,0, marker="X", color="green", label=("Raiz: "+str(raiz)))

    if raiz<=0:
        dimEjeY1= raiz-20
        dimEjeY2= raiz+20
        dimEjeX1= raiz-20
        dimEjeX2= raiz+20
    else:
        dimEjeY1 = raiz + 20
        dimEjeY2 = raiz - 20
        dimEjeX1 = raiz + 20
        dimEjeX2 = raiz - 20
    plt.xlim(dimEjeX1, dimEjeX2)
    plt.ylim(dimEjeY1 ,dimEjeY2)
    plt.legend()

    plt.show()
def funcionPrincipal(funcion, intervaloA):
    intervaloA=int(intervaloA)
    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    return plt