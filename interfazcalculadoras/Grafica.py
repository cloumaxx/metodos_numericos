# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Grafica.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from funciones import graficadora as gf
import matplotlib.pyplot as plt
import math
import numpy as np


class Ui_Form(object):
    funcionLabel1 = []
    funcionLabel2 = []
    listadoFunciones = []
    listadoPuntosX = []
    listadoPuntosY = []
    plt.plot(0,0)
    def setupUi(self, Grafica):
        Grafica.setObjectName("Grafica")
        Grafica.resize(800, 419)
        Grafica.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.funcion = QtWidgets.QTextEdit(Grafica)
        self.funcion.setGeometry(QtCore.QRect(20, 20, 111, 31))
        self.funcion.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "background-color: rgb(170, 170, 255);")
        self.funcion.setObjectName("funcion")
        self.label_5 = QtWidgets.QLabel(Grafica)
        self.label_5.setGeometry(QtCore.QRect(140, 20, 251, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.label = QtWidgets.QLabel(Grafica)
        self.label.setGeometry(QtCore.QRect(0, 0, 0 , 0)) #*****
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.punto = QtWidgets.QTextEdit(Grafica)
        self.punto.setGeometry(QtCore.QRect(20, 70, 81, 31))
        self.punto.setStyleSheet("font: 12pt \"Arial\";\n"
                                 "background-color: rgb(170, 170, 255);")
        self.punto.setObjectName("punto")
        self.parentesisabre = QtWidgets.QTextEdit(Grafica)
        self.parentesisabre.setGeometry(QtCore.QRect(110, 70, 21, 31))
        self.parentesisabre.setStyleSheet("font: 12pt \"Arial\";")
        self.parentesisabre.setObjectName("parentesisabre")
        self.textinput = QtWidgets.QLineEdit(Grafica)
        self.textinput.setGeometry(QtCore.QRect(140, 69, 51, 31))
        self.textinput.setObjectName("textinput")
        self.coma = QtWidgets.QTextEdit(Grafica)
        self.coma.setGeometry(QtCore.QRect(200, 70, 21, 31))
        self.coma.setStyleSheet("font: 12pt \"Arial\";")
        self.coma.setObjectName("coma")
        self.textinput2 = QtWidgets.QLineEdit(Grafica)
        self.textinput2.setGeometry(QtCore.QRect(230, 70, 51, 31))
        self.textinput2.setObjectName("textinput2")
        self.textinput.setText('0')
        self.textinput2.setText('0')
        self.parentesiscierra = QtWidgets.QTextEdit(Grafica)
        self.parentesiscierra.setGeometry(QtCore.QRect(290, 70, 21, 31))
        self.parentesiscierra.setStyleSheet("font: 12pt \"Arial\";")
        self.parentesiscierra.setObjectName("parentesiscierra")
        self.botonagregaruno = QtWidgets.QPushButton(Grafica)
        self.botonagregaruno.setGeometry(QtCore.QRect(430, 20, 150, 31))
        self.botonagregaruno.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 87 12pt \"Arial\";")
        self.botonagregaruno.setObjectName("botonagregaruno")
        self.botonagregaruno.clicked.connect(self.agregarFuncion)
        self.botonagregardos = QtWidgets.QPushButton(Grafica)
        self.botonagregardos.setGeometry(QtCore.QRect(430, 70, 150, 31))
        self.botonagregardos.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 87 12pt \"Arial\";")
        self.botonagregardos.setObjectName("botonagregardos")
        self.botonagregardos.clicked.connect(self.agregarPunto)
        self.botonvergrafica = QtWidgets.QPushButton(Grafica)
        self.botonvergrafica.setGeometry(QtCore.QRect(430, 120, 150, 31))
        self.botonvergrafica.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 87 12pt \"Arial\";")
        self.botonvergrafica.setObjectName("botonvergrafica")
        self.botonvergrafica.clicked.connect(self.graficar)
        self.layoutWidget = QtWidgets.QWidget(Grafica)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 160, 565, 203))
        self.layoutWidget.setObjectName("layoutWidget")
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

        self.botonMas_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_2.setObjectName("botonMas_2")
        self.gridLayout_2.addWidget(self.botonMas_2, 0, 2, 1, 1)
        self.botonMas_2.clicked.connect(self.eventRaiz)

        self.botonMas_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_3.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_3.setObjectName("botonMas_3")
        self.gridLayout_2.addWidget(self.botonMas_3, 0, 3, 1, 1)
        self.botonMas_3.clicked.connect(self.eventBotonExp)

        self.botonMas_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_11.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_11.setObjectName("botonMas_11")
        self.gridLayout_2.addWidget(self.botonMas_11, 0, 4, 1, 1)
        self.botonMas_11.clicked.connect(self.eventBotonTan)

        self.botonMenos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMenos.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMenos.setObjectName("botonMenos")
        self.gridLayout_2.addWidget(self.botonMenos, 1, 1, 1, 1)
        self.botonMenos.clicked.connect(self.eventBotonMenos)

        self.botonMas_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_4.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_4.setObjectName("botonMas_4")
        self.gridLayout_2.addWidget(self.botonMas_4, 1, 2, 1, 1)
        self.botonMas_4.clicked.connect(self.eventoExponente)

        self.botonMas_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_8.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_8.setObjectName("botonMas_8")
        self.gridLayout_2.addWidget(self.botonMas_8, 1, 3, 1, 1)
        self.botonMas_8.clicked.connect(self.eventBotonLog)

        self.botonMas_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_12.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_12.setObjectName("botonMas_12")
        self.gridLayout_2.addWidget(self.botonMas_12, 1, 4, 1, 1)
        self.botonMas_12.clicked.connect(self.eventBotonSec)

        self.BotonMulti = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonMulti.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.BotonMulti.setObjectName("BotonMulti")
        self.gridLayout_2.addWidget(self.BotonMulti, 2, 1, 1, 1)
        self.BotonMulti.clicked.connect(self.eventBotonMultiplicar)

        self.botonMas_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_7.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_7.setObjectName("botonMas_7")
        self.gridLayout_2.addWidget(self.botonMas_7, 2, 2, 1, 1)
        self.botonMas_7.clicked.connect(self.eventPi)

        self.botonMas_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_9.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_9.setObjectName("botonMas_9")
        self.gridLayout_2.addWidget(self.botonMas_9, 2, 3, 1, 1)
        self.botonMas_9.clicked.connect(self.eventBotonSin)

        self.botonMas_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_13.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_13.setObjectName("botonMas_13")
        self.gridLayout_2.addWidget(self.botonMas_13, 2, 4, 1, 1)
        self.botonMas_13.clicked.connect(self.eventBotonCsc)

        self.botonDivision = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDivision.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonDivision.setObjectName("botonDivision")
        self.gridLayout_2.addWidget(self.botonDivision, 3, 1, 1, 1)
        self.botonDivision.clicked.connect(self.eventDiv)

        self.botonMas_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_5.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_5.setObjectName("botonMas_5")
        self.gridLayout_2.addWidget(self.botonMas_5, 3, 2, 1, 1)
        self.botonMas_5.clicked.connect(self.eventBotonln)

        self.botonMas_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_10.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_10.setObjectName("botonMas_10")
        self.gridLayout_2.addWidget(self.botonMas_10, 3, 3, 1, 1)
        self.botonMas_10.clicked.connect(self.eventBotonCos)

        self.botonMas_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_14.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_14.setObjectName("botonMas_14")
        self.gridLayout_2.addWidget(self.botonMas_14, 3, 4, 1, 1)
        self.botonMas_14.clicked.connect(self.eventBotonCot)

        self.botonPorcentaje = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPorcentaje.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonPorcentaje.setObjectName("botonPorcentaje")
        self.gridLayout_2.addWidget(self.botonPorcentaje, 4, 1, 1, 1)
        self.botonPorcentaje.clicked.connect(self.eventBotonPorcentaje)

        self.botonMas_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_6.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_6.setObjectName("botonMas_6")
        self.gridLayout_2.addWidget(self.botonMas_6, 4, 2, 1, 1)
        self.botonMas_6.clicked.connect(self.eventBotonIgual)

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
        self.retranslateUi(Grafica)
        QtCore.QMetaObject.connectSlotsByName(Grafica)

        # creacion de botones
    def agregarFuncion(self):
        self.entrada = self.label.text()
        self.listadoFunciones.append(self.entrada)
        print('funcion: ',self.entrada)
    def agregarPunto(self):
        self.entrada= self.textinput.text()
        self.entrada2 = self.textinput2.text()
        self.listadoPuntosX.append(float(self.entrada))
        self.listadoPuntosY.append(float(self.entrada2))
        print(self.entrada,',',self.entrada2)
    def colorAleatorio(self):
        import random
        color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
        return color # fuente: https://www.delftstack.com/es/howto/python/generate-random-colors-python/
    def graficar(self):
        print('grafico')
        fig,ax = plt.subplots()
        print(self.listadoPuntosX)
        print(self.listadoPuntosY)
        ax.scatter(x=self.listadoPuntosX,y=self.listadoPuntosY)
        for i in range(0,len(self.listadoFunciones)):
            print(self.listadoFunciones[i])
            color =self.colorAleatorio()[0]
            print(color,type(self.colorAleatorio()))
            gf.graficaParaGraficador(self.listadoFunciones[i],color)
        plt.legend()

        #print(self.listadoFunciones)
        plt.show()
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
            print('√')
            Ui_Form.funcionLabel1.append('isqrt(')
            Ui_Form.funcionLabel2.append('√')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'isqrt('
            self.entrada2 += "√"
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
            Ui_Form.funcionLabel1.append('pi')
            Ui_Form.funcionLabel2.append('π')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += "pi"
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
            print('f')
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
            Ui_Form.funcionLabel1.append('sin(')
            Ui_Form.funcionLabel2.append('sin(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'sin('
            self.entrada2 += 'sin('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonCos(self):
            print('cos')
            Ui_Form.funcionLabel1.append('cos(')
            Ui_Form.funcionLabel2.append('cos(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'cos('
            self.entrada2 += 'cos('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonTan(self):
            print('tan')
            Ui_Form.funcionLabel1.append('tan(')
            Ui_Form.funcionLabel2.append('tan(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'tan('
            self.entrada2 += 'tan('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonSec(self):
            print('asin')
            Ui_Form.funcionLabel1.append('asin(')
            Ui_Form.funcionLabel2.append('sec(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'asin('
            self.entrada2 += 'sec('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonCsc(self):
            print('acos')
            Ui_Form.funcionLabel1.append('csc(')
            Ui_Form.funcionLabel2.append('csc(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'csc('
            self.entrada2 += 'csc('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonCot(self):
            print('atan')
            Ui_Form.funcionLabel1.append('atan(')
            Ui_Form.funcionLabel2.append('tan(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'atan('
            self.entrada2 += 'cot('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonLog(self):
            print('log')
            Ui_Form.funcionLabel1.append('log(')
            Ui_Form.funcionLabel2.append('log(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'log('
            self.entrada2 += 'log('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonExp(self):
            print('exp')
            Ui_Form.funcionLabel1.append('exp(')
            Ui_Form.funcionLabel2.append('e(')
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            self.entrada += 'exp('
            self.entrada2 += 'e('
            self.label.setText(self.entrada)
            self.label_5.setText(self.entrada2)

    def eventBotonln(self):
            print('log(')
            Ui_Form.funcionLabel1.append('log(')
            Ui_Form.funcionLabel2.append('ln(')
            self.entrada = self.label.text()
            self.entrada += 'log('
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

    def retranslateUi(self, Grafica):
        _translate = QtCore.QCoreApplication.translate
        Grafica.setWindowTitle(_translate("Grafica", "Grafica"))
        self.funcion.setHtml(_translate("Grafica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; color:#000000;\">Función </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-weight:600; color:#000000;\">F(x):</span></p></body></html>"))
        self.punto.setHtml(_translate("Grafica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Punto: </p></body></html>"))
        self.parentesisabre.setHtml(_translate("Grafica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                          "p, li { white-space: pre-wrap; }\n"
                                                          "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(</p></body></html>"))
        self.coma.setHtml(_translate("Grafica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">,</p></body></html>"))
        self.parentesiscierra.setHtml(_translate("Grafica", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">)</p></body></html>"))
        self.botonagregaruno.setText(_translate("Grafica", "Agregar funcion"))
        self.botonagregardos.setText(_translate("Grafica", "Agregar punto"))
        self.botonvergrafica.setText(_translate("Grafica", "Ver Grafica"))
        self.botonUno.setText(_translate("Grafica", "1"))
        self.botonUno.setShortcut(_translate("Grafica", "1"))
        self.botonDos.setText(_translate("Grafica", "2"))
        self.botonDos.setShortcut(_translate("Grafica", "2"))
        self.botonTres.setText(_translate("Grafica", "3"))
        self.botonTres.setShortcut(_translate("Grafica", "3"))
        self.botonCuatro.setText(_translate("Grafica", "4"))
        self.botonCuatro.setShortcut(_translate("Grafica", "4"))
        self.botonCinco.setText(_translate("Grafica", "5"))
        self.botonCinco.setShortcut(_translate("Grafica", "5"))
        self.botonSeis.setText(_translate("Grafica", "6"))
        self.botonSeis.setShortcut(_translate("Grafica", "6"))
        self.botonSiete.setText(_translate("Grafica", "7"))
        self.botonSiete.setShortcut(_translate("Grafica", "7"))
        self.botonOcho.setText(_translate("Grafica", "8"))
        self.botonOcho.setShortcut(_translate("Grafica", "8"))
        self.botonNueve.setText(_translate("Grafica", "9"))
        self.botonNueve.setShortcut(_translate("Grafica", "9"))
        self.botonCabierto.setText(_translate("Grafica", "("))
        self.botonCabierto.setShortcut(_translate("Grafica", "("))
        self.botonCero.setText(_translate("Grafica", "0"))
        self.botonCero.setShortcut(_translate("Grafica", "0"))
        self.botonCerrado.setText(_translate("Grafica", ")"))
        self.botonCerrado.setShortcut(_translate("Grafica", ")"))
        self.botonCabierto_2.setText(_translate("Grafica", "["))
        self.botonCabierto_2.setShortcut(_translate("Grafica", "("))
        self.botonPunto.setText(_translate("Grafica", "."))
        self.botonPunto.setShortcut(_translate("Grafica", "."))
        self.botonCabierto_3.setText(_translate("Grafica", "]"))
        self.botonCabierto_3.setShortcut(_translate("Grafica", "("))
        self.botonMas.setText(_translate("Grafica", "+"))
        self.botonMas.setShortcut(_translate("Grafica", "+"))
        self.botonMas_2.setText(_translate("Grafica", "√"))
        self.botonMas_2.setShortcut(_translate("Grafica", "+"))
        self.botonMas_3.setText(_translate("Grafica", "exp"))
        self.botonMas_3.setShortcut(_translate("Grafica", "+"))
        self.botonMas_11.setText(_translate("Grafica", "tan"))
        self.botonMas_11.setShortcut(_translate("Grafica", "+"))
        self.botonMenos.setText(_translate("Grafica", "-"))
        self.botonMenos.setShortcut(_translate("Grafica", "-"))
        self.botonMas_4.setText(_translate("Grafica", "^"))
        self.botonMas_4.setShortcut(_translate("Grafica", "+"))
        self.botonMas_8.setText(_translate("Grafica", "log"))
        self.botonMas_8.setShortcut(_translate("Grafica", "+"))
        self.botonMas_12.setText(_translate("Grafica", "sec"))
        self.botonMas_12.setShortcut(_translate("Grafica", "+"))
        self.BotonMulti.setText(_translate("Grafica", "*"))
        self.BotonMulti.setShortcut(_translate("Grafica", "*"))
        self.botonMas_7.setText(_translate("Grafica", "π"))
        self.botonMas_7.setShortcut(_translate("Grafica", "+"))
        self.botonMas_9.setText(_translate("Grafica", "sin"))
        self.botonMas_9.setShortcut(_translate("Grafica", "+"))
        self.botonMas_13.setText(_translate("Grafica", "csc"))
        self.botonMas_13.setShortcut(_translate("Grafica", "+"))
        self.botonDivision.setText(_translate("Grafica", "÷"))
        self.botonDivision.setShortcut(_translate("Grafica", "/"))
        self.botonMas_5.setText(_translate("Grafica", "ln"))
        self.botonMas_5.setShortcut(_translate("Grafica", "+"))
        self.botonMas_10.setText(_translate("Grafica", "cos"))
        self.botonMas_10.setShortcut(_translate("Grafica", "+"))
        self.botonMas_14.setText(_translate("Grafica", "cot"))
        self.botonMas_14.setShortcut(_translate("Grafica", "+"))
        self.botonPorcentaje.setText(_translate("Grafica", "%"))
        self.botonPorcentaje.setShortcut(_translate("Grafica", "%"))
        self.botonMas_6.setText(_translate("Grafica", "x"))
        self.botonMas_6.setShortcut(_translate("Grafica", "+"))
        self.BotonBorrar.setText(_translate("Grafica", "C"))
        self.BotonBorrar.setShortcut(_translate("Grafica", "Esc"))
        self.botonAC.setText(_translate("Grafica", "AC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Grafica = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Grafica)
    Grafica.show()
    sys.exit(app.exec_())

