import numpy as np
import sympy as sp
from sympy import *
import math
import matplotlib.pyplot as plt
from funciones import calcDerivadas as clD
def traductor(msj):
    print('entro:',msj)
    msj=msj.replace('e(','exp(')
    msj=msj.replace('exp(','math.exp(')
    msj = msj.replace('sin(', 'math.sin(')
    msj = msj.replace('sen(', 'math.sin(')
    msj = msj.replace('cos(', 'math.cos(')
    msj = msj.replace('tan(', 'math.tan(')
    msj = msj.replace('sec(', 'math.asin(')
    msj = msj.replace('csc(', 'math.acos(')
    msj = msj.replace('cot(', 'math.atan(')
    msj = msj.replace('log(', 'math.log(')
    msj = msj.replace('π','math.pi')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', 'math.sqrt(')
    msj = msj.replace('^', '**')
    return msj

def returnIntegral(expresionf,LimInf,LimSup,NumPar):
    expresionf= traductor(expresionf)
    expresionf = str(expresionf).replace('f', 'x')
    expresionf = str(expresionf).replace('math.', '')

    x = symbols('x')
    f = sp.lambdify(x, expresionf)
    funcion = clD.primerDerivada(expresionf)
    return str(funcion)
def returnRaiz(expresionf,LimInf,LimSup,NumPar):
    expresionf = traductor(expresionf)
    expresionf = str(expresionf).replace('f', 'x')
    expresionf = str(expresionf).replace('math.', '')

    x = symbols('x')
    f = sp.lambdify(x, expresionf)
    Pab = np.linspace(LimInf, LimSup, NumPar, endpoint=True)
    hPm = ((Pab[0] + Pab[1]) / 2) - LimInf
    PmPab = Pab + hPm
    fPm = f(PmPab)
    ARect = 2 * hPm * fPm
    IntegralNum = np.sum(ARect)
    return IntegralNum
def ecuacion(funcion, x):
    usar= funcion.replace('f',str(x))
    return eval(usar)
def mostrarGrafica(fx,a,b,tramos):
    fx = traductor(fx)
    print(fx)
    fx = str(fx).replace('math.', '')
    fx = str(fx).replace('f','x')
    print(fx)
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)  # Creamos simbolicamente a f

    muestras = tramos + 1
    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    # Linea suave
    muestraslinea = tramos * 10 + 1
    xk = np.linspace(a, b, muestraslinea)
    fk = fx(xk)
    lugar = str(fx).find('acos')
    lugar2 = str(fx).find('asin')

    # Graficando
    plt.plot(xk, fk, label='f(x)')
    plt.plot(xi, fi, marker='o',
             color='orange', label='muestras')

    plt.xlabel('x')
    plt.ylabel('f(x)')

    plt.title('Integral: Regla de Rectangulos')
    plt.legend()

    plt.fill_between(xi, 0, fi, color='g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')
    xPositivo = np.arange(-200, 200, 0.01)
    ecuacionEje = 'x*0'
    plt.plot(xPositivo, [ecuacion(ecuacionEje, i) for i in xPositivo], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xPositivo], xPositivo, color='black', label='eje y')
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