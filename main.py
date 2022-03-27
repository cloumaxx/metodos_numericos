import funciones.biseccion as bs
import funciones.falsaposicion as Fb
import funciones.calcBases as metodosBases
import funciones.calcIEEE as cIeee
import funciones.calcDerivadas as cD
import funciones.calcPolinomiosRaices as cPl
import funciones.newthon as cNewt
import funciones.secante as cSec
import matplotlib.pyplot as plt
from tabulate import tabulate
import numpy as np
import scipy.optimize as rs
import math
import sys
import PyQt5
from PyQt5.QtWidgets import *
from interfazcalculadoras.menuPrincipal import control as cl
from PyQt5 import QtGui


def control():
    print(2/2)
    cl()

    """
    if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ui = ventanaMenuPrinc()
    ui.show()
    sys.exit(app.exec_())
        #interDer.creacion()
        """
    """opcion = 0
        while opcion != 6:
            print('////////////////////////////////////////')
            print('////  Bienvenido a la calculadora  /////')
            print('////////////////////////////////////////')
            print(' ¿Que  desea hacer?  ')

            opcion = input('1) Convertir numeros a otras bases\n2) Utilizar el metodo de biseccion\n3) Utilizar el '
                           'metodo de falsa posicion\n4) Convetir a base IEEE\n5) Calcular una detivada\n6)Polinomio \n7) Metodo Nethon\n8)Secante\n9)Salir\n')
            if opcion == '1':
                metodosBases.control()
            elif opcion == '2':
                aux = bs.controlBisec()
                aux.show()

            elif opcion == '3':
                aux = Fb.control()
                aux.show()
            elif opcion == '4':
                numero=float(input('Digita el numero que deseas convertir en base IEEE\n'))
                cIeee.ieeeInverso(numero)
            elif opcion == '5':
                funcion = input('Digita le ecuacion a derivar\n')
                variable = input(' ¿ Cual es la variable a derivar:  ?')
                cD.algoritmoDerivada(funcion,variable)
            elif opcion == '6':
                cPl.calcularRaiz()
            elif opcion == '7':
                cNewt.NewtonRaphson()
            elif opcion == '8':
                cSec.control()
            elif opcion == '9':
                return  0
            else:

                print('*** Digita una opcion valida  ***')"""


control()
