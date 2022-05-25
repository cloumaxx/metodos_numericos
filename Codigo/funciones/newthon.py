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
            #print('x', i + 1, ' = ', x1, ": Mejor aproximacion.")
            return
        x0 = x1
        #print('x', i + 1, ' = ', x1)
def traductor(msj):
    msj = msj.replace('math.','')
    msj = msj.replace('e(','exp(')
    msj = msj.replace('exp(', '<!>')
    msj = msj.replace('math.exp(', '<!>')
    msj = msj.replace('<!>', 'math.exp(')
    msj = msj.replace('sin(', 'math.sin(')
    msj = msj.replace('sen(', 'math.sin(')
    msj = msj.replace('cos(', 'math.cos(')
    msj = msj.replace('tan(', 'math.tan(')
    msj = msj.replace('sec(', 'math.asin(')
    msj = msj.replace('csc(', 'math.acos(')
    msj = msj.replace('cot(', 'math.atan(')
    msj = msj.replace('ln(', 'log(')
    msj = msj.replace('log(', 'math.log(')
    msj = msj.replace('π','pi')
    msj = msj.replace('pi', 'math.pi')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', '√(')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('^', '**')
    return msj

def primerDerivada(funcion1):
        funcion1=funcion1.replace('math.','')
        variable1 = 'x'
        imprimir1 = sp.diff(funcion1, variable1)
        return imprimir1
def calculoRaiz(funcion,x_0,Error_t):
    funcion=traductor(funcion)
    raiz=0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan','math.atan')
    df = str(df).replace('pi','math.pi')
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')

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
    funcion=traductor(funcion)

    raiz = 0
    x0 = float(x_0)
    tol = float(Error_t)
    x = sp.symbols('x')  # Crea variable x
    df = primerDerivada(funcion)
    df = str(df).replace('atan', 'math.atan')
    df = str(df).replace('acos', 'math.acos')
    df = str(df).replace('asin', 'math.asin')
    df = str(df).replace('pi','math.pi')


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
    funcion=traductor(funcion)

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
def funcionPrincipal(funcion, intervaloA):
    funcion=traductor(funcion)
    intervaloA=int(intervaloA)

    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    return plt

def graficaTotal(funcion,intervaloA,error ):
    funcion=traductor(funcion)
    funcionPrincipal(funcion,intervaloA)
    raiz =calculoRaiz(funcion,intervaloA,error )
    plt.plot(raiz,0, marker="X", color="green", label="Raiz")
    funcion=funcion.replace('exp','<!!>')
    funcion = funcion.replace('x', 'f')
    funcion = funcion.replace('<!!>', 'exp')
    coordenada1 = eval(remplazoFuncion(funcion,intervaloA))
    l = ejeTama2


    dimEje1 = 0
    dimEje2 = 0
    mayor = intervaloA

    plt.legend()

    plt.show()

def funcionPrincipal(funcion, intervaloA):
    funcion=traductor(funcion)

    intervaloA=int(intervaloA)
    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    return plt