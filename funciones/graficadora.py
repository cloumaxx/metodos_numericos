import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sp


def remplazoFuncion(funcion, ele):
    usar = '' + str(ele)
    elemeto = str(funcion)
    accion = elemeto.replace('f', usar)
    return accion


def ecuacion(funcion, x):
    usar = funcion.replace('f', str(x))
    return eval(usar)


def graficaTriangulo(rectangles, a, b, fx):
    plt.clf()
    # GRAFICA
    # Puntos de muestra
    x = sp.symbols('x')  # Crea variable x
    fx = sp.lambdify(x, fx)  # Creamos simbolicamente a f

    muestras = rectangles + 1
    xi = np.linspace(a, b, muestras)
    fi = fx(xi)
    # Linea suave
    muestraslinea = rectangles * 10 + 1
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
        limite = float(fx(xi[i]))
        plt.vlines(xi[i], ymin=0.0, ymax=limite, color='blue')
    xeje = np.arange(-200, 200, 0.01)
    ecuacionEje = 'x*0'
    plt.plot(xeje, [ecuacion(ecuacionEje, i) for i in xeje], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xeje], xeje, color='black', label='eje y')
    plt.grid()
    plt.show()


# graficaTriangulo(25,-25,10, "x**2-2*x+3")
def graficarFuncion(ecuacionUsar):
    plt.clf()
    plt.grid()
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj = msj.replace('math.', '')
    msj = msj.replace('pi', 'π')
    lugar = ecuacionUsar.find('acos')
    lugar2 = ecuacionUsar.find('asin')
    # Graficar positivamente
    if lugar != -1 or lugar2 != -1:
        xPositivo = np.arange(0, 1, 0.01)
        xNegativo = np.arange(-1, 0, 0.01)
    else:
        xPositivo = np.arange(0.001, 200, 0.01)
        xNegativo = np.arange(-200, 0, 0.01)
    ecuacionEje = 'x*0'
    arregloEje = (-5000, 5000, 0.01)
    plt.plot(arregloEje, [ecuacion(ecuacionEje, i) for i in arregloEje], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in arregloEje], arregloEje, color='black', label='eje y')

    try:
        plt.plot(xNegativo, [ecuacion(ecuacionUsar, i) for i in xNegativo])
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj)
    except:
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj)

    return plt


def graficadoraRecta(ecuacionUsar):
    # Graficar positivamente
    plt.grid()
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj = msj.replace('math.', '')
    msj = msj.replace('pi', 'π')

    lugar = ecuacionUsar.find('acos')
    lugar2 = ecuacionUsar.find('asin')
    # Graficar positivamente
    if lugar != -1 or lugar2 != -1:
        xPositivo = np.arange(0, 1, 0.01)
        xNegativo = np.arange(-1, 0, 0.01)
    else:
        xPositivo = np.arange(0.001, 200, 0.01)
        xNegativo = np.arange(-200, 0, 0.01)
    ecuacionEje = 'x*0'
    plt.plot(xPositivo, [ecuacion(ecuacionEje, i) for i in xPositivo], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xPositivo], xPositivo, color='black', label='eje y')

    try:
        plt.plot(xNegativo, [ecuacion(ecuacionUsar, i) for i in xNegativo])
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj)
    except:
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj)
    return plt


def graficarPunto(puntoX, puntoY, color):
    msj = "(" + str(puntoX) + " , " + str(puntoY) + ")"
    plt.grid()
    plt.plot(puntoX, puntoY, marker="o", label=msj, color=color)
    return plt


elec = 0


def traductor(msj):
    msj = msj.replace('e(', 'exp(')
    msj = msj.replace('exp(', 'math.exp(')

    msj = msj.replace('sin(', 'math.sin(')
    msj = msj.replace('sen(', 'math.sin(')
    msj = msj.replace('cos(', 'math.cos(')
    msj = msj.replace('tan(', 'math.tan(')
    msj = msj.replace('sec(', 'math.asin(')
    msj = msj.replace('csc(', 'math.acos(')
    msj = msj.replace('cot(', 'math.atan(')
    msj = msj.replace('log(', 'math.log(')
    msj = msj.replace('π', 'math.pi')
    msj = msj.replace('√(', 'math.sqrt(')
    msj = msj.replace('√', 'math.sqrt(')
    msj = msj.replace('^', '**')
    return msj


def graficaParaGraficador(ecuacionUsar, color, ele):

    ecuacionUsar = traductor(ecuacionUsar)
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj = msj.replace('math.', '')
    msj = msj.replace('pi', 'π')
    lugar = ecuacionUsar.find('acos')
    lugar2 = ecuacionUsar.find('asin')
    lugar3 = ecuacionUsar.find('log')
    # Graficar positivamente
    if lugar != -1 or lugar2 != -1:
        xPositivo = np.arange(0, 1, 0.01)
        xNegativo = np.arange(-1, 0, 0.01)
    else:
        xPositivo = np.arange(0.001, 200, 0.01)
        xNegativo = np.arange(-200, 0, 0.01)
    arregloEje = (-200, 200, 0.01)
    ecuacionEje = 'x*0'
    if ele == 0:
        plt.plot(arregloEje, [ecuacion(ecuacionEje, i) for i in arregloEje], color='black', label='eje x')
        plt.plot([ecuacion(ecuacionEje, i) for i in arregloEje], arregloEje, color='black', label='eje y')
    try:
        plt.plot(xNegativo, [ecuacion(ecuacionUsar, i) for i in xNegativo], color=color)
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj, color=color)
    except:
        plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj, color=color)
    plt.grid()

    return plt

# graficaParaGraficador
# ('((x/2)-(1/3))*(math.exp(1)**(-1/2*(x**2)))+math.sin(math.pi/2*x)','red')#
