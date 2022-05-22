# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MetodoBiseccion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import math
import numpy as np

from PyQt5.QtWidgets import QMessageBox

from funciones import biseccion as bss
from PyQt5 import QtCore, QtGui, QtWidgets
from funciones import graficadora  as graficador
from interfazcalculadoras.IEEE import Ui_Form
from interfazcalculadoras import TablaBiseccion as tablaInter
import tabulate
import numpy as np
import matplotlib.pyplot as plt
import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


class Ui_Form(object):
    funcionLabel1 =[]
    funcionLabel2 =[]
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(616, 655)
        Form.setStyleSheet("\n"
                           "background-color: rgb(250, 250, 250);\n"
                           "font: 75 14pt \"Arial\";\n"
                           "")
        # pero le cambias el inicio segun corresponda
        Form.setWindowIcon(QtGui.QIcon(resolver_ruta('imagenes/icono.png')))  # se copia y pega esta linea en todas  las interfaces
        self.imagenFondo = QtWidgets.QLabel(Form)
        pixmap = QPixmap(resolver_ruta('imagenes/fondo1.png'))
        self.imagenFondo.setPixmap(pixmap)
        self.imagenFondo.setGeometry(0, 0, 270, 120)
        self.imagenFondo.resize(pixmap.width(), pixmap.height())

        self.BotonFunc = QtWidgets.QLabel(Form)
        self.BotonFunc.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.BotonFunc.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.BotonFunc.setObjectName("BotonFunc")
        self.BotonInterv = QtWidgets.QLabel(Form)
        self.BotonInterv.setGeometry(QtCore.QRect(10, 60, 111, 31))
        self.BotonInterv.setStyleSheet("font: 12pt \"Arial\";")
        self.BotonInterv.setObjectName("BotonInterv")
        self.BotonLim = QtWidgets.QLabel(Form)
        self.BotonLim.setGeometry(QtCore.QRect(10, 100, 131, 31))
        self.BotonLim.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonLim.setObjectName("BotonLim")
        self.BotonLimSup = QtWidgets.QLabel(Form)
        self.BotonLimSup.setGeometry(QtCore.QRect(10, 140, 131, 31))
        self.BotonLimSup.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.BotonLimSup.setObjectName("BotonLimSup")
        self.BotonError = QtWidgets.QLabel(Form)
        self.BotonError.setGeometry(QtCore.QRect(10, 180, 181, 31))
        self.BotonError.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonError.setObjectName("BotonError")
        self.BotonRaiz = QtWidgets.QLabel(Form)
        self.BotonRaiz.setGeometry(QtCore.QRect(10, 250, 121, 31))
        self.BotonRaiz.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.BotonRaiz.setObjectName("BotonRaiz")
        self.BotonErrorR = QtWidgets.QLabel(Form)
        self.BotonErrorR.setGeometry(QtCore.QRect(10, 290, 91, 31))
        self.BotonErrorR.setStyleSheet("font: 14pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.BotonErrorR.setObjectName("BotonErrorR")
        self.BotonNum = QtWidgets.QLabel(Form)
        self.BotonNum.setGeometry(QtCore.QRect(10, 330, 131, 31))
        self.BotonNum.setStyleSheet("font: 14pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonNum.setObjectName("BotonNum")
        self.botonGrafica = QtWidgets.QPushButton(Form)
        self.botonGrafica.setGeometry(QtCore.QRect(480, 190, 91, 41))
        self.botonGrafica.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botonGrafica.setObjectName("botonGrafica")
        self.botonGrafica.clicked.connect(self.mostrarGrafica)

        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(480, 260, 91, 41))
        self.pushButton_10.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 87 14pt \"Arial Black\";")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.eventTabla)

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 390, 565, 203))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setStyleSheet("background-color: rgb(170, 170, 255)")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.botonUno = QtWidgets.QPushButton(self.layoutWidget)
        self.botonUno.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonUno.setObjectName("botonUno")
        self.gridLayout.addWidget(self.botonUno, 0, 0, 1, 1)
        self.botonUno.clicked.connect(self.eventBoton1)

        self.botonDos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDos.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonDos.setObjectName("botonDos")
        self.gridLayout.addWidget(self.botonDos, 0, 1, 1, 1)
        self.botonDos.clicked.connect(self.eventBoton2)

        self.botonTres = QtWidgets.QPushButton(self.layoutWidget)
        self.botonTres.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonTres.setObjectName("botonTres")
        self.gridLayout.addWidget(self.botonTres, 0, 2, 1, 1)
        self.botonTres.clicked.connect(self.eventBoton3)

        self.botonCuatro = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCuatro.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.botonCuatro.setObjectName("botonCuatro")
        self.gridLayout.addWidget(self.botonCuatro, 1, 0, 1, 1)
        self.botonCuatro.clicked.connect(self.eventBoton4)

        self.botonCinco = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCinco.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonCinco.setObjectName("botonCinco")
        self.gridLayout.addWidget(self.botonCinco, 1, 1, 1, 1)
        self.botonCinco.clicked.connect(self.eventBoton5)

        self.botonSeis = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSeis.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonSeis.setObjectName("botonSeis")
        self.gridLayout.addWidget(self.botonSeis, 1, 2, 1, 1)
        self.botonSeis.clicked.connect(self.eventBoton6)

        self.botonSiete = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSiete.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonSiete.setObjectName("botonSiete")
        self.gridLayout.addWidget(self.botonSiete, 2, 0, 1, 1)
        self.botonSiete.clicked.connect(self.eventBoton7)

        self.botonOcho = QtWidgets.QPushButton(self.layoutWidget)
        self.botonOcho.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonOcho.setObjectName("botonOcho")
        self.gridLayout.addWidget(self.botonOcho, 2, 1, 1, 1)
        self.botonOcho.clicked.connect(self.eventBoton8)

        self.botonNueve = QtWidgets.QPushButton(self.layoutWidget)
        self.botonNueve.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonNueve.setObjectName("botonNueve")
        self.gridLayout.addWidget(self.botonNueve, 2, 2, 1, 1)
        self.botonNueve.clicked.connect(self.eventBoton9)
        # parentesis abierto
        self.botonCabierto = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonCabierto.setObjectName("botonCabierto")
        self.gridLayout.addWidget(self.botonCabierto, 3, 0, 1, 1)
        self.botonCabierto.clicked.connect(self.eventBotonParentesis)

        self.botonCero = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.gridLayout.addWidget(self.botonCero, 3, 1, 1, 1)
        self.botonCero.clicked.connect(self.eventBoton0)

        self.botonCerrado = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCerrado.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botonCerrado.setObjectName("botonCerrado")
        self.gridLayout.addWidget(self.botonCerrado, 3, 2, 1, 1)
        self.botonCerrado.clicked.connect(self.eventBotonParentesis2)

        # corchete
        self.botonCabierto_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonCabierto_2.setObjectName("botonCabierto_2")
        self.gridLayout.addWidget(self.botonCabierto_2, 4, 0, 1, 1)
        self.botonCabierto_2.clicked.connect(self.eventBotonCorchete)

        self.botonPunto = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPunto.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonPunto.setObjectName("botonPunto")
        self.gridLayout.addWidget(self.botonPunto, 4, 1, 1, 1)
        self.botonPunto.clicked.connect(self.eventBotonPunto)

        self.botonCabierto_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_3.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonCabierto_3.setObjectName("botonCabierto_3")
        self.gridLayout.addWidget(self.botonCabierto_3, 4, 2, 1, 1)
        self.botonCabierto_3.clicked.connect(self.eventBotonCorchete2)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 5, 1)
        self.botonMas = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonMas.setObjectName("botonMas")
        self.gridLayout_2.addWidget(self.botonMas, 0, 1, 1, 1)
        self.botonMas.clicked.connect(self.eventBotonSumar)

        self.botonRaiz = QtWidgets.QPushButton(self.layoutWidget)
        self.botonRaiz.setStyleSheet("ffont: 87 14pt \"Arial Black\";\n"
                                     "background-color: rgb(0, 170, 127);")
        self.botonRaiz.setObjectName("botonRaiz")
        self.gridLayout_2.addWidget(self.botonRaiz, 0, 2, 1, 1)
        self.botonRaiz.clicked.connect(self.eventRaiz)

        self.botonExp = QtWidgets.QPushButton(self.layoutWidget)
        self.botonExp.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonExp.setObjectName("botonExp")
        self.gridLayout_2.addWidget(self.botonExp, 0, 3, 1, 1)
        self.botonExp.clicked.connect(self.eventBotonExp)

        self.botonTan = QtWidgets.QPushButton(self.layoutWidget)
        self.botonTan.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonTan.setObjectName("botonTan")
        self.gridLayout_2.addWidget(self.botonTan, 0, 4, 1, 1)
        self.botonTan.clicked.connect(self.eventBotonTan)

        self.botonMenos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMenos.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMenos.setObjectName("botonMenos")
        self.gridLayout_2.addWidget(self.botonMenos, 1, 1, 1, 1)
        self.botonMenos.clicked.connect(self.eventBotonMenos)

        self.botonExponente = QtWidgets.QPushButton(self.layoutWidget)
        self.botonExponente.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                          "background-color: rgb(0, 170, 127);")
        self.botonExponente.setObjectName("botonExponente")
        self.gridLayout_2.addWidget(self.botonExponente, 1, 2, 1, 1)
        self.botonExponente.clicked.connect(self.eventoExponente)

        self.botonLog = QtWidgets.QPushButton(self.layoutWidget)
        self.botonLog.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonLog.setObjectName("botonLog")
        self.gridLayout_2.addWidget(self.botonLog, 1, 3, 1, 1)
        self.botonLog.clicked.connect(self.eventBotonLog)

        self.botonSec = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSec.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonSec.setObjectName("botonSec")
        self.gridLayout_2.addWidget(self.botonSec, 1, 4, 1, 1)
        self.botonSec.clicked.connect(self.eventBotonSec)

        self.BotonMulti = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonMulti.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.BotonMulti.setObjectName("BotonMulti")
        self.gridLayout_2.addWidget(self.BotonMulti, 2, 1, 1, 1)
        self.BotonMulti.clicked.connect(self.eventBotonMultiplicar)

        self.botonPi = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPi.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                   "background-color: rgb(0, 170, 127);")
        self.botonPi.setObjectName("botonPi")
        self.gridLayout_2.addWidget(self.botonPi, 2, 2, 1, 1)
        self.botonPi.clicked.connect(self.eventPi)

        # boton
        self.botonSeno = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSeno.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                     "background-color: rgb(0, 170, 127);")
        self.botonSeno.setObjectName("botonSeno")
        self.gridLayout_2.addWidget(self.botonSeno, 2, 3, 1, 1)
        self.botonSeno.clicked.connect(self.eventBotonSin)

        self.botonCsc = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCsc.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonCsc.setObjectName("botonCsc")
        self.gridLayout_2.addWidget(self.botonCsc, 2, 4, 1, 1)
        self.botonCsc.clicked.connect(self.eventBotonCsc)

        self.botonDivision = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDivision.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonDivision.setObjectName("botonDivision")
        self.gridLayout_2.addWidget(self.botonDivision, 3, 1, 1, 1)
        self.botonDivision.clicked.connect(self.eventDiv)

        self.botonLogNatural = QtWidgets.QPushButton(self.layoutWidget)
        self.botonLogNatural.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonLogNatural.setObjectName("botonLogNatural")

        self.gridLayout_2.addWidget(self.botonLogNatural, 3, 2, 1, 1)
        self.botonLogNatural.clicked.connect(self.eventBotonln)

        self.botonCoseno = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCoseno.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonCoseno.setObjectName("botonCoseno")
        self.gridLayout_2.addWidget(self.botonCoseno, 3, 3, 1, 1)
        self.botonCoseno.clicked.connect(self.eventBotonCos)

        self.botonCot = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCot.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonCot.setObjectName("botonCot")
        self.gridLayout_2.addWidget(self.botonCot, 3, 4, 1, 1)
        self.botonCot.clicked.connect(self.eventBotonCot)
        self.botonPorcentaje = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPorcentaje.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonPorcentaje.setObjectName("botonPorcentaje")
        self.gridLayout_2.addWidget(self.botonPorcentaje, 4, 1, 1, 1)
        self.botonPorcentaje.clicked.connect(self.eventBotonPorcentaje)

        self.botonIgual = QtWidgets.QPushButton(self.layoutWidget)
        self.botonIgual.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonIgual.setObjectName("botonIgual")
        self.gridLayout_2.addWidget(self.botonIgual, 4, 2, 1, 1)
        self.botonPorcentaje.clicked.connect(self.eventBotonIgual)
        self.botonIgual.clicked.connect(self.eventBotonIgual)
        self.BotonBorrar = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonBorrar.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.BotonBorrar.setObjectName("BotonBorrar")
        self.gridLayout_2.addWidget(self.BotonBorrar, 4, 3, 1, 1)
        self.BotonBorrar.clicked.connect(self.eventoBorrar)
        self.botonAC = QtWidgets.QPushButton(self.layoutWidget)
        self.botonAC.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                   "background-color: rgb(0, 170, 127);")
        self.botonAC.setObjectName("botonAC")
        self.gridLayout_2.addWidget(self.botonAC, 4, 4, 1, 1)
        self.botonAC.clicked.connect(self.eventBorrarTodo)

        self.botonCalcular = QtWidgets.QPushButton(Form)
        self.botonCalcular.setGeometry(QtCore.QRect(480, 120, 91, 41))
        self.botonCalcular.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botonCalcular.setObjectName("botonCalcular")
        self.botonCalcular.clicked.connect(self.eventCalcular)

        self.label = QtWidgets.QLineEdit(Form)
        self.label.setText("")
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLineEdit(Form)
        self.label_2.setText("")##
        self.label_2.setGeometry(QtCore.QRect(150, 250, 221, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_3 = QtWidgets.QLineEdit(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 290, 221, 21))
        self.label_3.setObjectName("label_3")
        self.label_3.setText('')
        self.label_3.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_4 = QtWidgets.QLineEdit(Form)
        self.label_4.setGeometry(QtCore.QRect(160, 330, 221, 21))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_5 = QtWidgets.QLineEdit(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 30, 400, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.TextLimIn = QtWidgets.QLineEdit(Form)
        self.TextLimIn.setGeometry(QtCore.QRect(160, 100, 281, 31))#limite1
        self.TextLimIn.setObjectName("TextLimIn")
        self.TextLimIn.setText("")#$$$

        self.TextLim = QtWidgets.QLineEdit(Form) # ingreso de datos por teclado
        self.TextLim.setGeometry(QtCore.QRect(160, 140, 281, 31))
        self.TextLim.setObjectName("TextLim")
        self.TextLim.setText("")#$$$
        self.TextErrorT = QtWidgets.QLineEdit(Form)
        self.TextErrorT.setGeometry(QtCore.QRect(200, 180, 271, 31))
        self.TextErrorT.setObjectName("TextErrorT")
        self.TextErrorT.setText("")#$$$
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    #
    def mostrarGrafica(self):

        try:
        #
            self.funcion = self.label_5.text() #esta variable toma el valor de lo que este escrito en este label
            self.limite1=float(self.TextLimIn.text())
            self.limite2=float(self.TextLim.text())
            self.errorTole = float(self.TextErrorT.text())

            bss.graficaTotal(self.funcion,self.limite1,self.limite2,self.errorTole)
            #raiz = bss.calculoRaiz(self.funcion,self.limite1,self.limite2,self.errorTole)
            #print(raiz)
        except:
            salida = str(self.label.text())
            salida = salida.replace('f', 'x')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Hay algun error\nfuncion: " + str(salida))
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

            print('algun error en la grafica')
    def eventCalcular(self):
        try:
            #se inicializan los labels para poder cambiarlos
            self.entrada2 = self.label_2.text()
            self.entrada3 = self.label_3.text()
            self.entrada4 = self.label_4.text()
            # se obtiene cada dato que se digito en la interfaz
            self.funcion = self.label_5.text()
            self.limite1=self.TextLimIn.text()
            self.limite2=self.TextLim.text()
            self.errorTole = self.TextErrorT.text()
            #se hace los calculos respectivos con las variables anteriores
            raiz = bss.calculoRaiz(self.funcion,self.limite1,self.limite2,self.errorTole)
            salida = bss.calculoError(self.funcion,self.limite1,self.limite2,self.errorTole)
            numItera = bss.calculoIteracion(self.funcion,self.limite1,self.limite2,self.errorTole)
            #se actualizan los label de los resultados, osea ya muestran los resultados
            self.entrada2= str(raiz)
            self.entrada3 = str(salida)
            self.entrada4 = str(numItera)
            print(self.entrada2)
            self.label_2.setText(self.entrada2)
            self.label_3.setText(self.entrada3)
            self.label_4.setText(self.entrada4)
        except:
                salida = str(self.label_5.text())
                salida = salida.replace('f', 'x')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Hay algun error\nfuncion: " + str(salida))
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()

    def eventTabla(self):
        try:
            #se inicializan los labels para poder cambiarlos
            self.entrada2 = self.label_2.text()
            self.entrada3 = self.label_3.text()
            self.entrada4 = self.label_4.text()
            # se obtiene cada dato que se digito en la interfaz
            self.funcion = self.label_5.text()
            self.limite1=self.TextLimIn.text()
            self.limite2=self.TextLim.text()
            self.errorTole = self.TextErrorT.text()
            #se hace los calculos respectivos con las variables anteriores
            #print(self.funcion)
            tabla = bss.returnTabla(self.funcion,self.limite1,self.limite2,self.errorTole)

            import sys

            self.aplicacion = QApplication(sys.argv)

            self.fuente = QFont()
            self.fuente.setPointSize(10)
            self.aplicacion.setFont(self.fuente)

            self.ventana = tableWidget(arreglo=tabla)
            self.ventana.show()

        except:
                salida = str(self.label_5.text())
                salida = salida.replace('f', 'x')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Hay algun error\nfuncion: " + str(salida))
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()

    # creacion de botones
    def eventBoton0(self):
        print('0')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        Ui_Form.funcionLabel1.append('0')
        Ui_Form.funcionLabel2.append('0')
        self.entrada2 += '0'
        self.entrada += '0'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton1(self):
        print('1')

        Ui_Form.funcionLabel1.append('1')
        Ui_Form.funcionLabel2.append('1')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += '1'
        self.entrada2 += '1'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton2(self):
        print('2')
        Ui_Form.funcionLabel1.append('2')

        Ui_Form.funcionLabel2.append('2')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "2"
        self.entrada2 += '2'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton3(self):
        print('3')
        Ui_Form.funcionLabel1.append('3')
        Ui_Form.funcionLabel2.append('3')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "3"
        self.entrada2 += '3'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton4(self):
        print('4')
        Ui_Form.funcionLabel1.append('4')
        Ui_Form.funcionLabel2.append('4')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "4"
        self.entrada2 += '4'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton5(self):
        print('5')
        Ui_Form.funcionLabel1.append('5')
        Ui_Form.funcionLabel2.append('5')

        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "5"
        self.entrada2 += '5'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton6(self):
        print('6')
        Ui_Form.funcionLabel1.append('6')
        Ui_Form.funcionLabel2.append('6')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "6"
        self.entrada2 += '6'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton7(self):
        print('7')
        Ui_Form.funcionLabel1.append('7')
        Ui_Form.funcionLabel2.append('7')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "7"
        self.entrada2 += '7'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton8(self):
        print('8')
        Ui_Form.funcionLabel1.append('8')
        Ui_Form.funcionLabel2.append('8')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "8"
        self.entrada2 += '8'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBoton9(self):
        print('9')
        Ui_Form.funcionLabel1.append('9')
        Ui_Form.funcionLabel2.append('9')

        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "9"
        self.entrada2 += '9'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonParentesis(self):
        print('(')
        Ui_Form.funcionLabel1.append('(')
        Ui_Form.funcionLabel2.append('(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "("
        self.entrada2 += '('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonParentesis2(self):
        print(')')
        Ui_Form.funcionLabel1.append(')')
        Ui_Form.funcionLabel2.append(')')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada2 += ')'
        self.entrada += ")"
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCorchete(self):
        print('[')
        Ui_Form.funcionLabel1.append('(')
        Ui_Form.funcionLabel2.append('[')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += '('
        self.entrada2 += '['
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCorchete2(self):
        print(')')
        Ui_Form.funcionLabel1.append(')')
        Ui_Form.funcionLabel2.append(']')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada2 += ']'
        self.entrada += ')'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonPunto(self):
        print('.')
        Ui_Form.funcionLabel1.append('.')
        Ui_Form.funcionLabel2.append('.')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += '.'
        self.entrada2 += "."
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventRaiz(self):
        print('√(')
        Ui_Form.funcionLabel1.append('math.sqrt(')
        Ui_Form.funcionLabel2.append('√')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.sqrt('
        self.entrada2 += "√("
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonSumar(self):
        print('+')
        Ui_Form.funcionLabel1.append('+')
        Ui_Form.funcionLabel2.append('+')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += '+'
        self.entrada2 += "+"
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonMenos(self):
        print('-')
        Ui_Form.funcionLabel1.append('-')
        Ui_Form.funcionLabel2.append('-')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "-"
        self.entrada2 += '-'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonPor(self):
        print('*')
        Ui_Form.funcionLabel1.append('*')
        Ui_Form.funcionLabel2.append('*')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "*"
        self.entrada2 += '*'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonPorcentaje(self):
        print('%')
        Ui_Form.funcionLabel1.append('%')
        Ui_Form.funcionLabel2.append('%')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "%"
        self.entrada2 += '%'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventPi(self):
        print('π')
        Ui_Form.funcionLabel1.append('math.pi')
        Ui_Form.funcionLabel2.append('π')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "math.pi"
        self.entrada2 += 'π'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventDiv(self):
        print('/')
        Ui_Form.funcionLabel1.append('/')
        Ui_Form.funcionLabel2.append('/')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "/"
        self.entrada2 += '/'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonIgual(self):
        print('x')
        Ui_Form.funcionLabel1.append('f')
        Ui_Form.funcionLabel2.append('x')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "f"
        self.entrada2 += 'x'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonMultiplicar(self):
        print('*')
        Ui_Form.funcionLabel1.append('*')
        Ui_Form.funcionLabel2.append('*')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "*"
        self.entrada2 += '*'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventoExponente(self):
        print('**')
        Ui_Form.funcionLabel1.append('**')
        Ui_Form.funcionLabel2.append('^')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += '**'
        self.entrada2 += '^'
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonSin(self):
        print('sin')
        Ui_Form.funcionLabel1.append('math.sin(')
        Ui_Form.funcionLabel2.append('sin(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.sin('
        self.entrada2 += 'sin('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCos(self):
        print('cos')
        Ui_Form.funcionLabel1.append('math.cos(')
        Ui_Form.funcionLabel2.append('cos(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.cos('
        self.entrada2 += 'cos('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonTan(self):
        print('tan')
        Ui_Form.funcionLabel1.append('math.tan(')
        Ui_Form.funcionLabel2.append('tan(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.tan('
        self.entrada2 += 'tan('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonSec(self):
        print('asin')
        Ui_Form.funcionLabel1.append('math.asin(')
        Ui_Form.funcionLabel2.append('sec(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.asin('
        self.entrada2 += 'sec('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCsc(self):
        print('acos')
        Ui_Form.funcionLabel1.append('math.acos(')
        Ui_Form.funcionLabel2.append('csc(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.acos('
        self.entrada2 += 'csc('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCot(self):
        print('atan')
        Ui_Form.funcionLabel1.append('math.atan(')
        Ui_Form.funcionLabel2.append('tan(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.atan('
        self.entrada2 += 'cot('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonLog(self):
        print('log')
        Ui_Form.funcionLabel1.append('math.log(')
        Ui_Form.funcionLabel2.append('log(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.log('
        self.entrada2 += 'log('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonExp(self):
        print('exp')
        Ui_Form.funcionLabel1.append('math.exp(')
        Ui_Form.funcionLabel2.append('e(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.exp('
        self.entrada2 += 'e('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonln(self):
        print('log(')
        Ui_Form.funcionLabel1.append('math.log(')
        Ui_Form.funcionLabel2.append('ln(')
        self.entrada = self.label.text()
        self.entrada += 'math.log('
        self.entrada2 += 'ln('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventoBorrar(self):
        try:
            import numpy as np
            # self.label.setText(self.entrada[:len(self.entrada)-1])
            s = ""
            s2 = ""
            elec1 = Ui_Form.funcionLabel1
            elec2 = Ui_Form.funcionLabel2
            elec1.pop(len(elec1) - 1)
            elec2.pop(len(elec2) - 1)
            tama1 = len(Ui_Form.funcionLabel1)

            tama2 = len(Ui_Form.funcionLabel2)
            for i in range(0, tama1):
                s += elec1[i]
            for j in range(0, tama2):
                s2 += elec2[j]
            self.label.setText(s)
            self.label_5.setText(s2)
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("No hay mas datos que borrar")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)

            retval = msg.exec_()

    def eventBorrarTodo(self):
        try:
            s = ""
            s2 = ""
            self.label.setText(s)
            self.label_5.setText(s2)
        except:
            print('no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("No hay mas datos que borrar")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)

            retval = msg.exec_()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Metodo de Bisección"))
        self.BotonFunc.setText(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#000000;\">Función </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#000000;\">F(x):</span></p></body></html>"))
        self.BotonInterv.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Intervalos</span></p></body></html>"))
        self.BotonLim.setText(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">limite inferior </span><span style=\" font-style:italic; color:#000000;\"> a:</span></p></body></html>"))
        self.BotonLimSup.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">limite superior </span><span style=\" font-style:italic; color:#000000;\"> b:</span></p></body></html>"))
        self.BotonError.setText(_translate("Form",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">Error de Tolerancia  Et</span><span style=\" font-style:italic; color:#ffffff;\">:</span></p></body></html>"))
        self.BotonRaiz.setText(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">La raiz es  r:</span></p></body></html>"))
        self.BotonErrorR.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">Error   Er:</span></p></body></html>"))
        self.BotonNum.setText(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#000000;\">N° Iteraciones  #:</span></p></body></html>"))
        self.botonGrafica.setText(_translate("Form", "Grafica"))
        self.pushButton_10.setText(_translate("Form", "Tabla"))
        self.botonUno.setText(_translate("Form", "1"))
        self.botonUno.setShortcut(_translate("Form", "1"))
        self.botonDos.setText(_translate("Form", "2"))
        self.botonDos.setShortcut(_translate("Form", "2"))
        self.botonTres.setText(_translate("Form", "3"))
        self.botonTres.setShortcut(_translate("Form", "3"))
        self.botonCuatro.setText(_translate("Form", "4"))
        self.botonCuatro.setShortcut(_translate("Form", "4"))
        self.botonCinco.setText(_translate("Form", "5"))
        self.botonCinco.setShortcut(_translate("Form", "5"))
        self.botonSeis.setText(_translate("Form", "6"))
        self.botonSeis.setShortcut(_translate("Form", "6"))
        self.botonSiete.setText(_translate("Form", "7"))
        self.botonSiete.setShortcut(_translate("Form", "7"))
        self.botonOcho.setText(_translate("Form", "8"))
        self.botonOcho.setShortcut(_translate("Form", "8"))
        self.botonNueve.setText(_translate("Form", "9"))
        self.botonNueve.setShortcut(_translate("Form", "9"))
        self.botonCabierto.setText(_translate("Form", "("))
        self.botonCero.setText(_translate("Form", "0"))
        self.botonCerrado.setText(_translate("Form", ")"))
        self.botonCerrado.setShortcut(_translate("Form", ")"))
        self.botonCabierto_2.setText(_translate("Form", "["))
        self.botonCabierto_2.setShortcut(_translate("Form", "("))
        self.botonPunto.setText(_translate("Form", "."))
        self.botonPunto.setShortcut(_translate("Form", "."))
        self.botonCabierto_3.setText(_translate("Form", "]"))
        self.botonCabierto_3.setShortcut(_translate("Form", "("))
        self.botonMas.setText(_translate("Form", "+"))
        self.botonMas.setShortcut(_translate("Form", "+"))
        self.botonRaiz.setText(_translate("Form", "√"))
        self.botonExp.setText(_translate("Form", "exp"))
        self.botonTan.setText(_translate("Form", "tan"))
        self.botonMenos.setText(_translate("Form", "-"))
        self.botonMenos.setShortcut(_translate("Form", "-"))
        self.botonExponente.setText(_translate("Form", "^"))
        self.botonLog.setText(_translate("Form", "log"))
        self.botonSec.setText(_translate("Form", "sec"))
        self.BotonMulti.setText(_translate("Form", "*"))
        self.botonPi.setText(_translate("Form", "π"))
        self.botonSeno.setText(_translate("Form", "sin"))
        self.botonCsc.setText(_translate("Form", "csc"))
        self.botonDivision.setText(_translate("Form", "÷"))
        self.botonLogNatural.setText(_translate("Form", "ln"))
        self.botonCoseno.setText(_translate("Form", "cos"))
        self.botonCot.setText(_translate("Form", "cot"))
        self.botonPorcentaje.setText(_translate("Form", "%"))
        self.botonPorcentaje.setShortcut(_translate("Form", "%"))
        self.botonIgual.setText(_translate("Form", "x"))
        self.BotonBorrar.setText(_translate("Form", "<-"))
        self.botonAC.setText(_translate("Form", "AC"))
        self.botonCalcular.setText(_translate("Form", "Calcular"))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "0"))  # Ráiz
        self.label_3.setText(_translate("Form", "0"))  # Error Er
        self.label_4.setText(_translate("Form", "0"))  # Numero iteracion
        self.label_5.setText(_translate("Form", ""))  # ingresoFuncion


from PyQt5.QtGui import QFont, QIcon, QColor, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)

from funciones import biseccion as bss
# ======================= CLASE tableWidget ========================

class tableWidget(QDialog):
    def __init__(self, parent=None,arreglo=[]):
        super(tableWidget, self).__init__(parent)
        self.setWindowTitle("Tabla Datos")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(950, 348)

        self.initUI(listadoUsar=arreglo)

    def initUI(self,listadoUsar):

        # ================== WIDGET  QTableWidget ==================

        self.tabla = QTableWidget(self)

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)  # Qt.ElideNone

        # Establecer el ajuste de palabras del texto
        self.tabla.setWordWrap(False)

        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)

        # Establecer el número de columnas
        self.tabla.setColumnCount(8)

        # Establecer el número de filas
        self.tabla.setRowCount(0)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # self.tabla.verticalHeader().setHighlightSections(True)

        nombreColumnas = ("Iteracion", "Funcion", "Intervalo A", "Intervalo B", "F(ri)", "E_r","E_t","Raiz")

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        # Establecer ancho de las columnas
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(900, 240)
        self.tabla.move(20, 56)

        # =================== WIDGETS QPUSHBUTTON ==================

        botonMostrarDatos = QPushButton("Mostrar datos", self)
        botonMostrarDatos.setFixedWidth(140)
        botonMostrarDatos.move(20, 20)

        menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menu.addAction(accion)

        botonMostrarOcultar = QPushButton("Motrar/ocultar columnas", self)
        botonMostrarOcultar.setFixedWidth(180)
        botonMostrarOcultar.setMenu(menu)
        botonMostrarOcultar.move(170, 20)




        # ======================== EVENTOS =========================

        botonMostrarDatos.clicked.connect(lambda :self.datosTabla(listadoUsar))


        menu.triggered.connect(self.mostrarOcultar)

    # ======================= FUNCIONES ============================


    def datosTabla(self,listar=[]):
        datos = [("1", "Andres", "Niño", "Masculino", "06/12/2019", "Colombia"," "," s"),
                 ("2", "Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos"),
                 ("3", "María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador"),
                 ("4", "Alberto", "Canosa", "Masculino", "04/05/1876", "España"),
                 ("5", "Virtud", "Pontes", "Femenino", "23/18/1965", "España"),
                 ("6", "Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos"),
                 ("7", "Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido"),
                 ("8", "Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia"),
                 ("9", "Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia"),
                 ("10", "Artur", "Fischer", "Masculino", "31/12/1919", "Alemania"),
                 ("11", "Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos"),
                 ("12", "Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos")]
        self.tabla.clearContents()
        row = 0
        tamaño = len(listar[0])
        contador=0

        for i in range(0,tamaño):
            numIteraciones=listar[0]
            numFuncion=listar[1]
            numA=listar[2]
            numB = listar[3]
            numFri=listar[4]
            numEr=listar[5]
            numEt=listar[6]
            numRaiz=listar[7]
            self.tabla.setRowCount(row + 1)

            # idDato = QTableWidgetItem(i[0])
            #idDato.setTextAlignment(4)

            self.tabla.setItem(row, 0, QTableWidgetItem(str(numIteraciones[contador])))
            self.tabla.setItem(row, 1, QTableWidgetItem(str(numFuncion[contador])))
            self.tabla.setItem(row, 2, QTableWidgetItem(str(numA[contador])))
            self.tabla.setItem(row, 3, QTableWidgetItem(str(numB[contador])))
            self.tabla.setItem(row, 4, QTableWidgetItem(str(numFri[contador])))
            self.tabla.setItem(row, 5, QTableWidgetItem(str(numEr[contador])))
            self.tabla.setItem(row, 6, QTableWidgetItem(str(numEt[contador])))
            self.tabla.setItem(row, 7, QTableWidgetItem(str(numRaiz[contador])))
            row += 1
            contador+=1
    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)



    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)


            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        print(filaSeleccionada)

        return

#========================================


# ===============================================================

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
