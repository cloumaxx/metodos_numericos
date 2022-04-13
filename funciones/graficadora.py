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
    usar= funcion.replace('f',str(x))
    return eval(usar)

def graficaTriangulo(rectangles,a,b,fx ):
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
    lugar =  str(fx).find('acos')
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
#graficaTriangulo(15,-5,10,lambda x: x**2-2*x+3)
def graficarFuncion(ecuacionUsar):
    plt.clf()
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj = msj.replace('math.', '')
    msj = msj.replace('pi', 'π')
    lugar = ecuacionUsar.find('acos')
    lugar2 = ecuacionUsar.find('asin')
    # Graficar positivamente
    if lugar != -1 or lugar2 != -1:
        xPositivo = np.arange(-1, 1, 0.01)
    else:
        xPositivo = np.arange(-200, 200, 0.01)
    ecuacionEje = 'x*0'
    plt.plot(xPositivo, [ecuacion(ecuacionEje, i) for i in xPositivo], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xPositivo], xPositivo, color='black', label='eje y')
    plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj)



    plt.show()
    return plt
def graficadoraRecta(ecuacionUsar):
    # Graficar positivamente
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj = msj.replace('math.', '')
    msj = msj.replace('pi', 'π')

    lugar = ecuacionUsar.find('acos')
    lugar2 = ecuacionUsar.find('asin')
    # Graficar positivamente
    if lugar != -1 or lugar2 != -1:
        xPositivo = np.arange(-1, 1, 0.01)
    else:
        xPositivo = np.arange(-200, 200, 0.01)
    ecuacionEje = 'x*0'
    plt.plot(xPositivo, [ecuacion(ecuacionEje, i) for i in xPositivo], color='black', label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xPositivo], xPositivo, color='black', label='eje y')
    plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj,color="purple")

    return plt
def graficarPunto(puntoX,puntoY,color):
    msj="("+str(puntoX)+" , "+str(puntoY)+")"
    plt.plot(puntoX,puntoY,marker="o", label=msj, color=color)
    return plt


def graficaParaGraficador(ecuacionUsar,color):
    msj = str(remplazoFuncion(ecuacionUsar, 'x'))
    msj= msj.replace('math.','')
    msj = msj.replace('pi', 'π')
    lugar=ecuacionUsar.find('acos')
    lugar2=ecuacionUsar.find('asin')

    # Graficar positivamente
    if lugar!=-1 or lugar2!=-1:
        xPositivo = np.arange(-1, 1, 0.01)
    else:
        xPositivo = np.arange(-200, 200, 0.01)
    ecuacionEje='x*0'
    plt.plot(xPositivo, [ecuacion(ecuacionEje, i) for i in xPositivo],color='black',label='eje x')
    plt.plot([ecuacion(ecuacionEje, i) for i in xPositivo],xPositivo, color='black', label='eje y')
    plt.plot(xPositivo, [ecuacion(ecuacionUsar, i) for i in xPositivo], label=msj, color=color)

    return plt

#graficaParaGraficador
# ('((x/2)-(1/3))*(math.exp(1)**(-1/2*(x**2)))+math.sin(math.pi/2*x)','red')#