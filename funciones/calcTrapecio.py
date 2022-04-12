import numpy as np
import math
import matplotlib.pyplot as plt
import sympy as sp
import random
from funciones import calcDerivadas as der
def mostrarGrafica(fx,a,b,tramos):
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)
    muestras = tramos + 1
    h = (b - a) / tramos
    xi = a
    suma = 0
    for i in range(0, tramos, 1):
        Atrapecio = h * (fx(xi) + fx(xi + h)) / 2
        suma = suma + Atrapecio
        xi = xi + h
    integral = suma

    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    muestrasLinea = muestras * 10
    xk = np.linspace(a, b, muestrasLinea)
    fk = fx(xk)

    plt.plot(xi, fi, 'ro')
    plt.plot(xk, fk)

    plt.fill_between(xi, 0, fi, color='g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='blue')
    plt.show()


def reglaTrapecio(fx, a, b, tramos):
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)
    muestras = tramos + 1
    h = (b - a) / tramos
    xi = a
    suma = 0
    for i in range(0, tramos, 1):
        Atrapecio = h * (fx(xi) + fx(xi + h)) / 2
        suma = suma + Atrapecio
        xi = xi + h
    integral = suma

    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    muestrasLinea = muestras * 10
    xk = np.linspace(a, b, muestrasLinea)
    fk = fx(xk)

    plt.plot(xi, fi, 'ro')
    plt.plot(xk, fk)

    plt.fill_between(xi, 0, fi, color='g')
    for i in range(0, muestras, 1):
        plt.axvline(xi[i], color='w')
    #plt.show()

    return integral
"""
# se inicializan los labels para poder cambiarlos
            self.entrada2 = self.label_2.text() #raiz
            self.entrada3 = self.label_3.text() #error
            # se obtiene cada dato que se digito en la interfaz
            self.funcion = self.label.text()
            self.limite = self.TextPun.text()
            self.errorTole = self.BotonError.text()
            # se hace los calculos respectivos con las variables anteriores
            raiz = nw.calculoRaiz(self.funcion, self.limite, self.errorTole)
            salida = nw.calculoError(self.funcion, self.limite, self.errorTole)
            # se actualizan los label de los resultados, osea ya muestran los resultados
            self.entrada2 = str(raiz)
            self.entrada3 = str(salida)
            print(self.entrada2)
            self.label_2.setText(self.entrada2)
            self.label_3.setText(self.entrada3)

"""

#funcion = '2*math.pi*x*(cos(x**2+1))*(x**2+1)'#'exp(-0.85*x)+cos(x)-(0.95*x*x)+3.25*x'#input('digita la funcion: ')
funcion = 'exp(-0.85*x)+cos(x)-(0.95*x*x)+3.25*x+pi'#input('digita la funcion: ')

intervalob = 3.10659#float(input('digita el intervalo A: '))
intervaloa = -0.65547#float(input('digita el intervalo B: '))
tramos = 2000#int(input('digita los tramos: '))
h = (intervalob - intervaloa) / tramos
#nrandom = random.randint(intervaloa, intervalob,)
#variable = intervaloa + nrandom * (intervalob - intervaloa)
#der2Solu = der.solucionSegundaDerivada(funcion, variable)
#error = -(h**3)/12 * der2Solu


def retornaError():
    return 0#error


#print('-->',reglaTrapecio(funcion, intervaloa, intervalob, tramos))
#print(retornaError())