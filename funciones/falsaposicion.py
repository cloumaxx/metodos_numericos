import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import scipy.optimize as rs
import math


from funciones import graficadora

EjeTama = 500
ejeTama2 = -500

def remplazoFuncion(funcion, ele):
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
def funcionPrincipal(funcion, intervaloA, intervaloB):
    intervaloA=int(intervaloA)
    intervaloB=int(intervaloB)
    plt = graficadora.graficarFuncion(funcion)
    plt.plot(intervaloA, 0, marker="o", color="red", label="Coordenada A")
    plt.plot(intervaloB, 0, marker="o", color="orange", label="Coordenada B")
    return plt

def graficaTotal(funcion,intervaloA,intervaloB ,error ):
    funcionPrincipal(funcion,intervaloA,intervaloB)
    raiz =calculoRaiz(funcion,intervaloA,intervaloB ,error )
    plt.plot(raiz,0, marker="X", color="green", label="Raiz")
    coordenada1 = eval(remplazoFuncion(funcion,intervaloA))
    coordenada2 = eval(remplazoFuncion(funcion,intervaloB))
    l = ejeTama2


    dimEje1 = 0
    dimEje2 = 0
    mayor = intervaloA
    menor = intervaloB
    if intervaloA < intervaloB:
        mayor = intervaloB
        menor = intervaloA

    if menor <= 0:
        dimEje1 = menor - 10
    if mayor <= 0:
        dimEje2 = mayor - 10
    else:
        dimEje2 = mayor + 10
    plt.xlim(dimEje1, dimEje2)

    # plt.xlim(-4, 4)
    # ejes Y
    dimEjeY1 = 0
    dimEjeY2 = 0
    mayorY = coordenada1
    menorY = coordenada2
    if coordenada1 < coordenada2:
        mayorY = coordenada2
        menorY = coordenada1
    if menor <= 0:
        dimEjeY1 = (menorY - 10)
    if mayorY <= 0:
        dimEjeY2 = mayorY - 10
    else:
        dimEjeY2 = mayorY + 10

    plt.ylim((dimEjeY1 * -1), dimEjeY2)
    plt.legend()

    plt.show()



def creacionTabla():
    arreglo = [[], []]
    titulos = []
    titulos.append("iteracion")
    titulos.append("Funcion")
    titulos.append("A")
    titulos.append("B")
    titulos.append("F(ri)")
    titulos.append("E_t")
    titulos.append("E_ri")
    titulos.append("Raiz")
    arreglo.append(titulos)
    return arreglo
def calculoRaiz(funcion,intervaloA,intervaloB,E_t):
    tabla = creacionTabla()
    fila = []
    salir = False
    raiz = 0


    a = float(intervaloA)
    b = float(intervaloB)
    iteracion = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    F_a = eval(remplazoFuncion(funcion, a))
    F_b = eval(remplazoFuncion(funcion, b))

    if (F_a * F_b) < 0:
        while salir == False:
            ri = ((a * F_b) - (b * F_a)) / (F_b - F_a)  # raiz
            F_ri = eval(remplazoFuncion(funcion, ri))

            if (F_ri * F_b) < 0:
                a = ri
            else:
                b = ri
            # error
            ri_arreglo.append(ri)
            E_r = abs((ri_arreglo[iteracion - 1] - ri_arreglo[iteracion]) / ri_arreglo[iteracion])
            if iteracion >= 50 or E_r < float(E_t):
                raiz = ri
                salir = True
            else:
                iteracion += 1

    else:
        raiz=0

    return raiz
def calculoError(funcion,intervaloA,intervaloB,E_t):
    salida=0
    salir = False
    raiz = 0


    a = float(intervaloA)
    b = float(intervaloB)
    iteracion = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    F_a = eval(remplazoFuncion(funcion, a))
    F_b = eval(remplazoFuncion(funcion, b))

    if (F_a * F_b) < 0:
        while salir == False:
            ri = ((a * F_b) - (b * F_a)) / (F_b - F_a)  # raiz
            F_ri = eval(remplazoFuncion(funcion, ri))

            if (F_ri * F_b) < 0:
                a = ri
            else:
                b = ri
            # error
            ri_arreglo.append(ri)
            E_r = abs((ri_arreglo[iteracion - 1] - ri_arreglo[iteracion]) / ri_arreglo[iteracion])
            if iteracion >= 50 or E_r < float(E_t):
                salida=E_r
                raiz = ri
                salir = True
            else:
                iteracion += 1

    else:
        salida=0

    return salida

def calculoIteracion(funcion,intervaloA,intervaloB,E_t):
    salida=0
    salir = False
    raiz = 0


    a = float(intervaloA)
    b = float(intervaloB)
    iteracion = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    F_a = eval(remplazoFuncion(funcion, a))
    F_b = eval(remplazoFuncion(funcion, b))

    if (F_a * F_b) < 0:
        while salir == False:
            ri = ((a * F_b) - (b * F_a)) / (F_b - F_a)  # raiz
            F_ri = eval(remplazoFuncion(funcion, ri))

            if (F_ri * F_b) < 0:
                a = ri
            else:
                b = ri
            # error
            ri_arreglo.append(ri)
            E_r = abs((ri_arreglo[iteracion - 1] - ri_arreglo[iteracion]) / ri_arreglo[iteracion])
            if iteracion >= 50 or E_r < float(E_t):
                salida=iteracion
                raiz = ri
                salir = True
            else:
                iteracion += 1

    else:
        salida=0

    return salida

def errorRelativo(r_i, r_i1):
    resultado = (r_i1 - r_i) / r_i
    if resultado < 0:
        resultado = resultado * (-1)

    return resultado


def controlBisec():
    tabla = creacionTabla()
    fila = []
    f = -2
    #'(x**2)-2'  # "(x**2)-2'  #
    funcion =  '(f**2)-2'  # "(x**2)-2'#input('ingresa la funcion:\n')
    intervaloA = 5# float(input('ingresa el intervalo A: \n(0,'))
    intervaloB =6 #float(input('ingresa el intervalo B: \n(0,'))
    E_t =0.01#float(input('ingresa el error de tolerancia: '))
    salir = False
    raiz = 0
    a = intervaloA
    b = intervaloB
    iteracion = 1
    ri_arreglo = []
    ri_arreglo.append(0)
    F_a=eval(remplazoFuncion(funcion,a))
    F_b=eval(remplazoFuncion(funcion,b))

    if (F_a*F_b)<0:
        while salir == False:
            ri = ((a * F_b) - (b * F_a)) / (F_b - F_a)  # raiz
            F_ri = eval(remplazoFuncion(funcion, ri))

            if (F_ri * F_b) < 0:
                a = ri
            else:
                b = ri
            # error
            ri_arreglo.append(ri)
            E_r = abs((ri_arreglo[iteracion - 1] - ri_arreglo[iteracion]) / ri_arreglo[iteracion])

            fila.append(iteracion)
            fila.append(funcion)
            fila.append(a)
            fila.append(b)
            fila.append(F_ri)
            fila.append(E_t)

            fila.append(E_r)
            if iteracion >= 50 or E_r < E_t:

                raiz = ri
                plt.plot(raiz, 0, marker="x", color="black", label="Raiz", markersize=12)
                fila.append(raiz)
                salir = True
            else:
                iteracion += 1
            tabla.append(fila)
            fila = []
    else:
        print('no hay raices')

    funcionPrincipal(funcion, intervaloA, intervaloB)
    x = intervaloA
    coordenada1 = eval(funcion)
    x = intervaloB
    coordenada2 = eval(funcion)
    l = ejeTama2

    plt.legend()

    dimEje1 = 0
    dimEje2 = 0
    mayor = intervaloA
    menor = intervaloB
    if intervaloA < intervaloB:
        mayor = intervaloB
        menor = intervaloA

    if menor <= 0:
        dimEje1 = menor - 10
    if mayor <= 0:
        dimEje2 = mayor - 10
    else:
        dimEje2 = mayor + 10
    plt.xlim(dimEje1, dimEje2)

    #plt.xlim(-4, 4)
    # ejes Y
    dimEjeY1 = 0
    dimEjeY2 = 0
    mayorY = coordenada1
    menorY = coordenada2
    if coordenada1 < coordenada2:
        mayorY = coordenada2
        menorY = coordenada1
    if menor <= 0:
        dimEjeY1 = (menorY - 10)
    if mayorY <= 0:
        dimEjeY2 = mayorY - 10
    else:
        dimEjeY2 = mayorY + 10

    plt.ylim((dimEjeY1*-1), dimEjeY2)
    #plt.ylim(-3, 5)
    plt.show()
    return plt
    # plt.show()