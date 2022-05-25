# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Matrices.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from tkinter import Scale

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QDir

from interfazcalculadoras import ScrollLabel
from funciones import calcMatrices
import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


class Ui_Form(object):
    arregloUtilizar = []

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 1045)
        Form.setWindowIcon(QtGui.QIcon(resolver_ruta('imagenes/icono.png')))  # se copia y pega esta linea en todas  las interfaces

        Form.setStyleSheet("background-color: rgb(250, 250, 250);\n"
                           "")
        self.imagenFondo = QtWidgets.QLabel(Form)
        pixmap = QPixmap(resolver_ruta('imagenes/fondo1.png'))

        self.imagenFondo.setPixmap(pixmap)
        self.imagenFondo.setGeometry(0, 0, 270, 120)
        self.imagenFondo.resize(pixmap.width(), pixmap.height())

        self.matrizLabel = QtWidgets.QLabel(Form)
        self.matrizLabel.setGeometry(QtCore.QRect(80, 10, 150, 20))
        self.matrizLabel.setText('Matrices guardadas:')
        self.matrizLabel.setStyleSheet("background-color: rgb(31, 195, 153);\nfont: 10 10pt \"Arial BLACK\";")
        self.matrizLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.visor = ScrollLabel.ScrollLabel(Form)
        self.visor.setGeometry(QtCore.QRect(10, 40, 300, 180))

        self.textEdit_1 = QtWidgets.QLabel(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(600, 250, 350, 120))  # (ancho,largo del cajon)
        self.textEdit_1.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(35, 223, 166 );")
        self.textEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_1.setText("En esta opcion de nuestra \n"
                                "calculadora podras ingresar el numero \n"
                                "de filas y de columnas que desees, tambien te \n"
                                "permitira agregar una matriz y calcularla con\n"
                                "la operacion que desees")
        self.matrizLabel2 = QtWidgets.QLabel(Form)
        self.matrizLabel2.setGeometry(QtCore.QRect(470, 10, 150, 20))
        self.matrizLabel2.setText('Matriz Resultante:')
        self.matrizLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.matrizLabel2.setStyleSheet("background-color: rgb(31, 195, 153);\nfont: 10 10pt \"Arial BLACK\";")


        self.visor2Resultado = ScrollLabel.ScrollLabel(Form)
        self.visor2Resultado.setGeometry(QtCore.QRect(380, 40, 300, 180))

        self.numerodefilas = QtWidgets.QLabel(Form)
        self.numerodefilas.setGeometry(QtCore.QRect(10, 230, 181, 31))
        self.numerodefilas.setStyleSheet("font: 12pt \"Arial\";\n"
                                         "background-color: rgb(170, 170, 255);")
        self.numerodefilas.setObjectName("numerodefilas")
        self.numerdefilasedit = QtWidgets.QLineEdit(Form)
        self.numerdefilasedit.setGeometry(QtCore.QRect(200, 230, 161, 31))
        self.numerdefilasedit.setObjectName("numerdefilasedit")
        self.numerdefilasedit.setText("2")
        self.numcolumnas = QtWidgets.QLabel(Form)
        self.numcolumnas.setGeometry(QtCore.QRect(10, 280, 181, 31))
        self.numcolumnas.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.numcolumnas.setObjectName("numcolumnas")

        self.columnasedit = QtWidgets.QLineEdit(Form)
        self.columnasedit.setGeometry(QtCore.QRect(200, 280, 161, 31))
        self.columnasedit.setObjectName("columnasedit")
        self.columnasedit.setText("2")
        self.botonagregarvalores = QtWidgets.QPushButton(Form)
        self.botonagregarvalores.setGeometry(QtCore.QRect(400, 225, 151, 41))
        self.botonagregarvalores.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                               "font: 87 12pt \"Arial Black\";")
        self.botonagregarvalores.setObjectName("botonagregarvalores")
        try:
            self.botonagregarvalores.clicked.connect(self.agregarMatriz)
        except:
            print('')
        self.botonActualizar = QtWidgets.QPushButton(Form)
        self.botonActualizar.setGeometry(QtCore.QRect(400, 280, 151, 41))
        self.botonActualizar.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 87 12pt \"Arial Black\";")
        self.botonActualizar.setObjectName("botonActualizar")
        self.botonActualizar.setText('Actualizar')
        self.botonActualizar.clicked.connect(self.eventbotonActualizar)

        self.Operaciones = QtWidgets.QLabel(Form)
        self.Operaciones.setGeometry(QtCore.QRect(10, 340, 181, 31))
        self.Operaciones.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.Operaciones.setObjectName("Operaciones")
        self.label = QtWidgets.QLineEdit(Form)
        self.label.setGeometry(QtCore.QRect(200, 340, 241, 31))
        self.label.setObjectName("label")
        self.botonresultado = QtWidgets.QPushButton(Form)
        self.botonresultado.setGeometry(QtCore.QRect(460, 340, 111, 31))
        self.botonresultado.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 87 12pt \"Arial Black\";")
        self.botonresultado.setObjectName("botonresultado")
        self.botonresultado.clicked.connect(self.eventResultado)
        self.botonsuma = QtWidgets.QPushButton(Form)
        self.botonsuma.setGeometry(QtCore.QRect(20, 400, 75, 35))
        self.botonsuma.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonsuma.setObjectName("botonsuma")
        self.botonsuma.clicked.connect(self.eventBotonSuma)
        self.botonresta = QtWidgets.QPushButton(Form)
        self.botonresta.setGeometry(QtCore.QRect(110, 400, 75, 35))
        self.botonresta.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonresta.setObjectName("botonresta")
        self.botonresta.clicked.connect(self.eventBotonResta)
        self.botonmultiplicar = QtWidgets.QPushButton(Form)
        self.botonmultiplicar.setGeometry(QtCore.QRect(200, 400, 75, 35))
        self.botonmultiplicar.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                            "font: 87 14pt \"Arial Black\";")
        self.botonmultiplicar.setObjectName("botonmultiplicar")
        self.botonmultiplicar.clicked.connect(self.eventBotonMulti)
        self.botonalfa = QtWidgets.QPushButton(Form)
        self.botonalfa.setGeometry(QtCore.QRect(290, 400, 120, 35))
        self.botonalfa.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                     "font: 9 14pt \"Arial \";")
        self.botonalfa.setObjectName("botonalfa")
        self.botonalfa.clicked.connect(self.calcularDeterminante)
        self.botonTranspuesta = QtWidgets.QPushButton(Form)
        self.botonTranspuesta.setGeometry(QtCore.QRect(425, 400, 120, 35))
        self.botonTranspuesta.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                            "font: 10 14pt \"Arial\";")
        self.botonTranspuesta.setObjectName("botonTranspuesta")
        self.botonTranspuesta.clicked.connect(self.calcularTranspuesta)
        self.botoninversa = QtWidgets.QPushButton(Form)
        self.botoninversa.setGeometry(QtCore.QRect(550, 400, 120, 35))
        self.botoninversa.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 10 14pt \"Arial \";")
        self.botoninversa.setObjectName("botoninversa")
        self.botoninversa.clicked.connect(self.calcularInversa)
        self.Resultado = QtWidgets.QLabel(Form)
        self.Resultado.setGeometry(QtCore.QRect(10, 690, 181, 31))
        self.Resultado.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.Resultado.setObjectName("Resultado")
        self.labelresultado = QtWidgets.QLabel(Form)
        self.labelresultado.setGeometry(QtCore.QRect(200, 690, 331, 121))
        self.labelresultado.setText("")
        self.labelresultado.setObjectName("labelresultado")

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 460, 648, 205))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.botonC = QtWidgets.QPushButton(self.widget)
        self.botonC.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                  "font: 87 14pt \"Arial Black\";")
        self.botonC.setObjectName("botonC")
        self.botonC.clicked.connect(self.eventBotonC)

        self.gridLayout_2.addWidget(self.botonC, 2, 1, 1, 1)
        self.botonP = QtWidgets.QPushButton(self.widget)
        self.botonP.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonP.setObjectName("botonP")
        self.gridLayout_2.addWidget(self.botonP, 3, 4, 1, 1)
        self.botonP.clicked.connect(self.eventBotonP)

        self.botonA = QtWidgets.QPushButton(self.widget)
        self.botonA.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonA.setObjectName("botonA")
        self.gridLayout_2.addWidget(self.botonA, 0, 1, 1, 1)
        self.botonA.clicked.connect(self.eventBotonA)

        self.botonG = QtWidgets.QPushButton(self.widget)
        self.botonG.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonG.setObjectName("botonG")
        self.gridLayout_2.addWidget(self.botonG, 2, 2, 1, 1)
        self.botonG.clicked.connect(self.eventBotonG)

        self.botonF = QtWidgets.QPushButton(self.widget)
        self.botonF.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonF.setObjectName("botonF")
        self.gridLayout_2.addWidget(self.botonF, 1, 2, 1, 1)
        self.botonF.clicked.connect(self.eventBotonF)

        self.botonK = QtWidgets.QPushButton(self.widget)
        self.botonK.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonK.setObjectName("botonK")
        self.gridLayout_2.addWidget(self.botonK, 2, 3, 1, 1)
        self.botonK.clicked.connect(self.eventBotonK)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.botonCuatro = QtWidgets.QPushButton(self.widget)
        self.botonCuatro.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.botonCuatro.setObjectName("botonCuatro")
        self.botonCuatro.clicked.connect(self.eventBoton4)

        self.gridLayout.addWidget(self.botonCuatro, 1, 0, 1, 1)
        self.botonSeis = QtWidgets.QPushButton(self.widget)
        self.botonSeis.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonSeis.setObjectName("botonSeis")
        self.gridLayout.addWidget(self.botonSeis, 1, 2, 1, 1)
        self.botonSeis.clicked.connect(self.eventBoton6)

        self.botonCerrado = QtWidgets.QPushButton(self.widget)
        self.botonCerrado.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botonCerrado.setObjectName("botonCerrado")
        self.gridLayout.addWidget(self.botonCerrado, 3, 2, 1, 1)
        self.botonCerrado.clicked.connect(self.eventBotonParentesis2)

        self.botonUno = QtWidgets.QPushButton(self.widget)
        self.botonUno.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonUno.setObjectName("botonUno")
        self.gridLayout.addWidget(self.botonUno, 0, 0, 1, 1)
        self.botonUno.clicked.connect(self.eventBoton1)

        self.botonTres = QtWidgets.QPushButton(self.widget)
        self.botonTres.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonTres.setObjectName("botonTres")
        self.gridLayout.addWidget(self.botonTres, 0, 2, 1, 1)
        self.botonTres.clicked.connect(self.eventBoton3)

        self.botonNueve = QtWidgets.QPushButton(self.widget)
        self.botonNueve.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonNueve.setObjectName("botonNueve")
        self.gridLayout.addWidget(self.botonNueve, 2, 2, 1, 1)
        self.botonNueve.clicked.connect(self.eventBoton9)

        self.botonCero = QtWidgets.QPushButton(self.widget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.gridLayout.addWidget(self.botonCero, 3, 1, 1, 1)
        self.botonCero.clicked.connect(self.eventBoton0)

        self.botonDos = QtWidgets.QPushButton(self.widget)
        self.botonDos.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonDos.setObjectName("botonDos")
        self.gridLayout.addWidget(self.botonDos, 0, 1, 1, 1)
        self.botonDos.clicked.connect(self.eventBoton2)

        self.botonSiete = QtWidgets.QPushButton(self.widget)
        self.botonSiete.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonSiete.setObjectName("botonSiete")
        self.gridLayout.addWidget(self.botonSiete, 2, 0, 1, 1)
        self.botonSiete.clicked.connect(self.eventBoton7)

        self.botonCinco = QtWidgets.QPushButton(self.widget)
        self.botonCinco.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonCinco.setObjectName("botonCinco")
        self.gridLayout.addWidget(self.botonCinco, 1, 1, 1, 1)
        self.botonCinco.clicked.connect(self.eventBoton5)

        self.botonOcho = QtWidgets.QPushButton(self.widget)
        self.botonOcho.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonOcho.setObjectName("botonOcho")
        self.gridLayout.addWidget(self.botonOcho, 2, 1, 1, 1)
        self.botonOcho.clicked.connect(self.eventBoton8)

        self.botonCabierto = QtWidgets.QPushButton(self.widget)
        self.botonCabierto.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonCabierto.setObjectName("botonCabierto")
        self.gridLayout.addWidget(self.botonCabierto, 3, 0, 1, 1)
        self.botonCabierto.clicked.connect(self.eventBotonParentesis)

        self.botonW = QtWidgets.QPushButton(self.widget)
        self.botonW.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonW.setObjectName("botonW")
        self.gridLayout.addWidget(self.botonW, 4, 2, 1, 1)
        self.botonW.clicked.connect(self.eventBotonW)

        self.botonV = QtWidgets.QPushButton(self.widget)
        self.botonV.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                  "font: 87 14pt \"Arial Black\";")
        self.botonV.setObjectName("botonV")
        self.gridLayout.addWidget(self.botonV, 4, 1, 1, 1)
        self.botonV.clicked.connect(self.eventBotonV)

        self.botonU = QtWidgets.QPushButton(self.widget)
        self.botonU.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonU.setObjectName("botonU")
        self.gridLayout.addWidget(self.botonU, 4, 0, 1, 1)
        self.botonU.clicked.connect(self.eventBotonU)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 5, 1)
        self.botonL = QtWidgets.QPushButton(self.widget)
        self.botonL.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonL.setObjectName("botonL")
        self.gridLayout_2.addWidget(self.botonL, 3, 3, 1, 1)
        self.botonL.clicked.connect(self.eventBotonL)

        self.botonI = QtWidgets.QPushButton(self.widget)
        self.botonI.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonI.setObjectName("botonI")
        self.gridLayout_2.addWidget(self.botonI, 0, 3, 1, 1)
        self.botonI.clicked.connect(self.eventBotonI)

        self.botonN = QtWidgets.QPushButton(self.widget)
        self.botonN.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonN.setObjectName("botonN")
        self.gridLayout_2.addWidget(self.botonN, 1, 4, 1, 1)
        self.botonN.clicked.connect(self.eventBotonN)

        self.botonE = QtWidgets.QPushButton(self.widget)
        self.botonE.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonE.setObjectName("botonE")
        self.gridLayout_2.addWidget(self.botonE, 0, 2, 1, 1)
        self.botonE.clicked.connect(self.eventBotonE)

        self.botonH = QtWidgets.QPushButton(self.widget)
        self.botonH.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonH.setObjectName("botonH")
        self.gridLayout_2.addWidget(self.botonH, 3, 2, 1, 1)
        self.botonH.clicked.connect(self.eventBotonH)

        self.botonD = QtWidgets.QPushButton(self.widget)
        self.botonD.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonD.setObjectName("botonD")
        self.gridLayout_2.addWidget(self.botonD, 3, 1, 1, 1)
        self.botonD.clicked.connect(self.eventBotonD)

        self.botonJ = QtWidgets.QPushButton(self.widget)
        self.botonJ.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonJ.setObjectName("botonJ")
        self.gridLayout_2.addWidget(self.botonJ, 1, 3, 1, 1)
        self.botonJ.clicked.connect(self.eventBotonJ)

        self.botonO = QtWidgets.QPushButton(self.widget)
        self.botonO.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonO.setObjectName("botonO")
        self.gridLayout_2.addWidget(self.botonO, 2, 4, 1, 1)
        self.botonO.clicked.connect(self.eventBotonO)

        self.botonM = QtWidgets.QPushButton(self.widget)
        self.botonM.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonM.setObjectName("botonM")
        self.gridLayout_2.addWidget(self.botonM, 0, 4, 1, 1)
        self.botonM.clicked.connect(self.eventBotonM)

        self.botonB = QtWidgets.QPushButton(self.widget)
        self.botonB.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonB.setObjectName("botonB")
        self.gridLayout_2.addWidget(self.botonB, 1, 1, 1, 1)
        self.botonB.clicked.connect(self.eventBotonB)

        self.botonborrar = QtWidgets.QPushButton(self.widget)
        self.botonborrar.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonborrar.setObjectName("botonborrar")
        self.gridLayout_2.addWidget(self.botonborrar, 4, 4, 1, 1)
        self.botonZ = QtWidgets.QPushButton(self.widget)
        self.botonZ.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                  "font: 87 14pt \"Arial Black\";")
        self.botonZ.setObjectName("botonZ")
        self.gridLayout_2.addWidget(self.botonZ, 4, 3, 1, 1)
        self.botonZ.clicked.connect(self.eventBotonZ)

        self.botonY = QtWidgets.QPushButton(self.widget)
        self.botonY.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonY.setObjectName("botonY")
        self.gridLayout_2.addWidget(self.botonY, 4, 2, 1, 1)
        self.botonY.clicked.connect(self.eventBotonY)

        self.botonX = QtWidgets.QPushButton(self.widget)
        self.botonX.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonX.setObjectName("botonX")
        self.gridLayout_2.addWidget(self.botonX, 4, 1, 1, 1)
        self.botonX.clicked.connect(self.eventBotonX)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 5, 1)
        self.botonQ = QtWidgets.QPushButton(self.widget)
        self.botonQ.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonQ.setObjectName("botonQ")
        self.gridLayout_3.addWidget(self.botonQ, 0, 1, 1, 1)
        self.botonQ.clicked.connect(self.eventBotonQ)

        self.botonR = QtWidgets.QPushButton(self.widget)
        self.botonR.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonR.setObjectName("botonR")
        self.gridLayout_3.addWidget(self.botonR, 1, 1, 1, 1)
        self.botonR.clicked.connect(self.eventBotonR)

        self.botonS = QtWidgets.QPushButton(self.widget)
        self.botonS.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonS.setObjectName("botonS")
        self.gridLayout_3.addWidget(self.botonS, 2, 1, 1, 1)
        self.botonS.clicked.connect(self.eventBotonS)

        self.botonT = QtWidgets.QPushButton(self.widget)
        self.botonT.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonT.setObjectName("botonT")
        self.gridLayout_3.addWidget(self.botonT, 3, 1, 1, 1)
        self.botonT.clicked.connect(self.eventBotonT)

        self.botoneliminartodo = QtWidgets.QPushButton(self.widget)
        self.botoneliminartodo.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                             "background-color: rgb(0, 170, 127);")
        self.botoneliminartodo.setObjectName("botoneliminartodo")
        self.gridLayout_3.addWidget(self.botoneliminartodo, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def encontrarPos(self,letra):
        abecedario = 'abcdefghijklmnopqrstuvwxyz'.upper()
        letra= letra.upper()
        pos = abecedario.find(letra[0])
        return pos
    def calcularInversa(self):
        try:
            funcion = self.label.text()
            funcion= funcion[0]
            if len(funcion)==1:
                pos = self.encontrarPos(funcion)
                arreglo = self.arregloUtilizar[pos]
                salida = calcMatrices.inversa(arreglo)
                msj = ""
                for i in range(0,len(salida)):
                    msj+=str(salida[i])+" \n"
                self.visor2Resultado.setText(msj)
            else:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.o)
                msg.setText("Recuerda que solo puedes calcular la inversa a 1 matriz a la vez ")
                msg.setWindowTitle("Error")
                # msg.setStandardButtons(QMessageBox.ok)
                retval = msg.exec_()
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()
    def calcularDeterminante(self):
        try:
            funcion = self.label.text()
            funcion = funcion[0]

            if len(funcion) == 1:
                pos = self.encontrarPos(funcion)
                arreglo = self.arregloUtilizar[pos]
                salida = calcMatrices.determinante(arreglo)

                msj = str(salida) + " \n"
                self.visor2Resultado.setText(msj)
            else:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.o)
                msg.setText("Recuerda que solo puedes calcular el determinante a 1 matriz a la vez ")
                msg.setWindowTitle("Error")
                # msg.setStandardButtons(QMessageBox.ok)
                retval = msg.exec_()
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()
    def calcularTranspuesta(self):
        try:
            funcion = self.label.text()
            funcion = funcion[0]
            if len(funcion) == 1:
                pos = self.encontrarPos(funcion)
                arreglo = self.arregloUtilizar[pos]
                salida = calcMatrices.transpuesta(arreglo)
                msj = ""
                for i in range(0, len(salida)):
                    msj += str(salida[i]) + " \n"
                print('msj:\n' + msj)
                self.visor2Resultado.setText(msj)
            else:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.o)
                msg.setText("Recuerda que solo puedes calcular la Trasnpuesta a 1 matriz a la vez ")
                msg.setWindowTitle("Error")
                # msg.setStandardButtons(QMessageBox.ok)
                retval = msg.exec_()
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()
    def eventResultado(self):
        try:
            funcion = self.label.text()
            funcion = funcion.replace(" ","")
            tamañolimite = len(funcion)-1
            i = 1

            while i <tamañolimite:
                letra1 = funcion[i-1]
                pos1 = self.encontrarPos(letra1)
                letra2= funcion[i+1]
                pos2 = self.encontrarPos(letra2)
                acum = self.arregloUtilizar[pos1]
                siguiente = self.arregloUtilizar[pos2]
                if funcion[i]=="+":
                    acum=calcMatrices.suma(acum,siguiente)
                elif funcion[i]=="-":
                    acum=calcMatrices.resta(acum,siguiente)
                elif funcion[i]=="*":
                    acum = calcMatrices.producto(acum, siguiente)
                i+=1
            msj = ""
            for i in range(0, len(acum)):
                msj += str(acum[i]) + " \n"
            print('msj:\n' + msj)
            self.visor2Resultado.setText(msj)
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()
    import sys
    def actualizarResultado(self, arreglo):
        try:
            tama = len(arreglo)
            aux = ""
            for i in range(0, tama):  # len(arreglo[i])):
                aux += str(arreglo[i]) + "\n"
            self.visor2Resultado.setText(aux)
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()
    def agregarMatriz(self):
        try:
            filas = int(self.numerdefilasedit.text())
            columnas = int(self.columnasedit.text())

            self.interfaz2 = QtWidgets.QWidget()
            arr = []
            objeto = IngresarMatriz(interfazm=self.interfaz2, tamaFilas=filas, tamaColum=columnas, arregloMatriz=arr)

            self.ui = objeto  # IngresarMatriz()#__init__(self,tamaFilas=filas,tamaColum=columnas)#initUI(self,numFilas=filas,numColum=columnas)
            self.nuevo = self.ui.initUI(self.interfaz2, numColum=columnas, numFilas=filas)
            self.interfaz2.show()
            arr = objeto.get_data()
            self.arregloUtilizar.append(arr)

        except:
             msg = QMessageBox()
             # msg.setIcon(QMessageBox.o)
             msg.setText("Revisa los datos ingresados")
             msg.setWindowTitle("Error")
             # msg.setStandardButtons(QMessageBox.ok)
             retval = msg.exec_()
    def eliminarVacias(self):
        for i in range(0,len(self.arregloUtilizar)):
            if len(self.arregloUtilizar[i])==0:
                self.arregloUtilizar.pop(i)
    def eventbotonActualizar(self):
        self.eliminarVacias()
        try:
            msj = ""
            abecedario = "abcdefghijklmnopqrstuvwxyz"

            for i in range(0, len(self.arregloUtilizar)):
                msj += "NOMBRE: " + abecedario[i].upper() + "\n"
                for j in range(0, len(self.arregloUtilizar[i])):
                    msj += str(self.arregloUtilizar[i][j]) + "\n"
                msj += "\n"
            self.visor.setText(msj)
        except:
            msg = QMessageBox()
            # msg.setIcon(QMessageBox.o)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            # msg.setStandardButtons(QMessageBox.ok)
            retval = msg.exec_()

    def eventBotonMulti(self):
        print('*')
        self.entrada = self.label.text()
        self.entrada += "*"
        self.label.setText(self.entrada)
    def eventBotonResta(self):
        print('-')
        self.entrada = self.label.text()
        self.entrada += "-"
        self.label.setText(self.entrada)
    def eventBotonSuma(self):
        print('+')
        self.entrada = self.label.text()
        self.entrada += "+"
        self.label.setText(self.entrada)
    def eventBotonParentesis(self):
        print('(')
        self.entrada = self.label.text()
        self.entrada += "("
        self.label.setText(self.entrada)

    def eventBotonParentesis2(self):
        print(')')
        self.entrada = self.label.text()
        self.entrada += ")"
        self.label.setText(self.entrada)

    def eventBoton0(self):
        print('0')
        self.entrada = self.label.text()
        self.entrada += "0"
        self.label.setText(self.entrada)

    def eventBoton1(self):
        print('1')
        self.entrada = self.label.text()
        self.entrada += "1"
        self.label.setText(self.entrada)

    def eventBoton2(self):
        print('2')
        self.entrada = self.label.text()
        self.entrada += "2"
        self.label.setText(self.entrada)

    def eventBoton3(self):
        print('3')
        self.entrada = self.label.text()
        self.entrada += "3"
        self.label.setText(self.entrada)

    def eventBoton4(self):
        print('4')
        self.entrada = self.label.text()
        self.entrada += "4"
        self.label.setText(self.entrada)

    def eventBoton5(self):
        print('5')
        self.entrada = self.label.text()
        self.entrada += "5"
        self.label.setText(self.entrada)

    def eventBoton6(self):
        print('6')
        self.entrada = self.label.text()
        self.entrada += "6"
        self.label.setText(self.entrada)

    def eventBoton7(self):
        print('7')
        self.entrada = self.label.text()
        self.entrada += "7"
        self.label.setText(self.entrada)

    def eventBoton8(self):
        print('8')
        self.entrada = self.label.text()
        self.entrada += "8"
        self.label.setText(self.entrada)

    def eventBoton9(self):
        print('9')
        self.entrada = self.label.text()
        self.entrada += "9"
        self.label.setText(self.entrada)

    def eventBotonA(self):
        print('A')
        self.entrada = self.label.text()
        self.entrada += "A"
        self.label.setText(self.entrada)

    def eventBotonB(self):
        print('B')
        self.entrada = self.label.text()
        self.entrada += "B"
        self.label.setText(self.entrada)

    def eventBotonC(self):
        print('C')
        self.entrada = self.label.text()
        self.entrada += "C"
        self.label.setText(self.entrada)

    def eventBotonD(self):
        print('D')
        self.entrada = self.label.text()
        self.entrada += "D"
        self.label.setText(self.entrada)

    def eventBotonE(self):
        print('E')
        self.entrada = self.label.text()
        self.entrada += "E"
        self.label.setText(self.entrada)

    def eventBotonF(self):
        print('F')
        self.entrada = self.label.text()
        self.entrada += "F"
        self.label.setText(self.entrada)

    def eventBotonG(self):
        print('G')
        self.entrada = self.label.text()
        self.entrada += "G"
        self.label.setText(self.entrada)

    def eventBotonH(self):
        print('H')
        self.entrada = self.label.text()
        self.entrada += "H"
        self.label.setText(self.entrada)

    def eventBotonI(self):
        print('I')
        self.entrada = self.label.text()
        self.entrada += "I"
        self.label.setText(self.entrada)

    def eventBotonJ(self):
        print('J')
        self.entrada = self.label.text()
        self.entrada += "J"
        self.label.setText(self.entrada)

    def eventBotonK(self):
        print('K')
        self.entrada = self.label.text()
        self.entrada += "K"
        self.label.setText(self.entrada)

    def eventBotonL(self):
        print('L')
        self.entrada = self.label.text()
        self.entrada += "L"
        self.label.setText(self.entrada)

    def eventBotonM(self):
        print('M')
        self.entrada = self.label.text()
        self.entrada += "M"
        self.label.setText(self.entrada)

    def eventBotonN(self):
        print('N')
        self.entrada = self.label.text()
        self.entrada += "N"
        self.label.setText(self.entrada)

    def eventBotonÑ(self):
        print('Ñ')
        self.entrada = self.label.text()
        self.entrada += "Ñ"
        self.label.setText(self.entrada)

    def eventBotonO(self):
        print('O')
        self.entrada = self.label.text()
        self.entrada += "O"
        self.label.setText(self.entrada)

    def eventBotonP(self):
        print('P')
        self.entrada = self.label.text()
        self.entrada += "P"
        self.label.setText(self.entrada)

    def eventBotonQ(self):
        print('Q')
        self.entrada = self.label.text()
        self.entrada += "Q"
        self.label.setText(self.entrada)

    def eventBotonR(self):
        print('R')
        self.entrada = self.label.text()
        self.entrada += "R"
        self.label.setText(self.entrada)

    def eventBotonS(self):
        print('S')
        self.entrada = self.label.text()
        self.entrada += "S"
        self.label.setText(self.entrada)

    def eventBotonT(self):
        print('T')
        self.entrada = self.label.text()
        self.entrada += "T"
        self.label.setText(self.entrada)

    def eventBotonU(self):
        print('U')
        self.entrada = self.label.text()
        self.entrada += "U"
        self.label.setText(self.entrada)

    def eventBotonV(self):
        print('V')
        self.entrada = self.label.text()
        self.entrada += "V"
        self.label.setText(self.entrada)

    def eventBotonW(self):
        print('W')
        self.entrada = self.label.text()
        self.entrada += "W"
        self.label.setText(self.entrada)

    def eventBotonX(self):
        print('X')
        self.entrada = self.label.text()
        self.entrada += "X"
        self.label.setText(self.entrada)

    def eventBotonY(self):
        print('Y')
        self.entrada = self.label.text()
        self.entrada += "Y"
        self.label.setText(self.entrada)

    def eventBotonZ(self):
        print('Z')
        self.entrada = self.label.text()
        self.entrada += "Z"
        self.label.setText(self.entrada)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Calculadora de Matrices"))
        self.numerodefilas.setText(_translate("Form",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numero de filas:</p></body></html>"))
        self.numcolumnas.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numero de Columnas:</p></body></html>"))
        self.botonagregarvalores.setText(_translate("Form", "Agregar Matriz"))
        self.Operaciones.setText(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Operaciones:</p></body></html>"))
        self.label.setText(_translate("Form", " "))
        self.botonresultado.setText(_translate("Form", "Resultado"))
        self.botonsuma.setText(_translate("Form", "+"))
        self.botonsuma.setShortcut(_translate("Form", "Esc"))
        self.botonresta.setText(_translate("Form", "-"))
        self.botonresta.setShortcut(_translate("Form", "Esc"))
        self.botonmultiplicar.setText(_translate("Form", "*"))
        self.botonmultiplicar.setShortcut(_translate("Form", "Esc"))
        self.botonalfa.setText(_translate("Form", "Determinante"))
        self.botonalfa.setShortcut(_translate("Form", "Esc"))
        self.botonTranspuesta.setText(_translate("Form", "Transpuesta"))
        self.botonTranspuesta.setShortcut(_translate("Form", "Esc"))
        self.botoninversa.setText(_translate("Form", "Inversa"))
        self.botoninversa.setShortcut(_translate("Form", "Esc"))
        self.Resultado.setText(_translate("Form",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resultado:</p></body></html>"))
        self.botonC.setText(_translate("Form", "C"))
        self.botonC.setShortcut(_translate("Form", "C"))
        self.botonP.setText(_translate("Form", "P"))
        self.botonP.setShortcut(_translate("Form", "+"))
        self.botonA.setText(_translate("Form", "A"))
        self.botonA.setShortcut(_translate("Form", "+"))
        self.botonG.setText(_translate("Form", "G"))
        self.botonG.setShortcut(_translate("Form", "+"))
        self.botonF.setText(_translate("Form", "F"))
        self.botonF.setShortcut(_translate("Form", "+"))
        self.botonK.setText(_translate("Form", "K"))
        self.botonK.setShortcut(_translate("Form", "+"))
        self.botonCuatro.setText(_translate("Form", "4"))
        self.botonCuatro.setShortcut(_translate("Form", "4"))
        self.botonSeis.setText(_translate("Form", "6"))
        self.botonSeis.setShortcut(_translate("Form", "6"))
        self.botonCerrado.setText(_translate("Form", ")"))
        self.botonCerrado.setShortcut(_translate("Form", ")"))
        self.botonUno.setText(_translate("Form", "1"))
        self.botonUno.setShortcut(_translate("Form", "1"))
        self.botonTres.setText(_translate("Form", "3"))
        self.botonTres.setShortcut(_translate("Form", "3"))
        self.botonNueve.setText(_translate("Form", "9"))
        self.botonNueve.setShortcut(_translate("Form", "9"))
        self.botonCero.setText(_translate("Form", "0"))
        self.botonCero.setShortcut(_translate("Form", "0"))
        self.botonDos.setText(_translate("Form", "2"))
        self.botonDos.setShortcut(_translate("Form", "2"))
        self.botonSiete.setText(_translate("Form", "7"))
        self.botonSiete.setShortcut(_translate("Form", "7"))
        self.botonCinco.setText(_translate("Form", "5"))
        self.botonCinco.setShortcut(_translate("Form", "5"))
        self.botonOcho.setText(_translate("Form", "8"))
        self.botonOcho.setShortcut(_translate("Form", "8"))
        self.botonCabierto.setText(_translate("Form", "("))
        self.botonCabierto.setShortcut(_translate("Form", "("))
        self.botonW.setText(_translate("Form", "W"))
        self.botonW.setShortcut(_translate("Form", "("))
        self.botonV.setText(_translate("Form", "V"))
        self.botonV.setShortcut(_translate("Form", "."))
        self.botonU.setText(_translate("Form", "U"))
        self.botonU.setShortcut(_translate("Form", "("))
        self.botonL.setText(_translate("Form", "L"))
        self.botonL.setShortcut(_translate("Form", "+"))
        self.botonI.setText(_translate("Form", "I"))
        self.botonI.setShortcut(_translate("Form", "+"))
        self.botonN.setText(_translate("Form", "N"))
        self.botonN.setShortcut(_translate("Form", "+"))
        self.botonE.setText(_translate("Form", "E"))
        self.botonE.setShortcut(_translate("Form", "+"))
        self.botonH.setText(_translate("Form", "H"))
        self.botonH.setShortcut(_translate("Form", "+"))
        self.botonD.setText(_translate("Form", "D"))
        self.botonD.setShortcut(_translate("Form", "/"))
        self.botonJ.setText(_translate("Form", "J"))
        self.botonJ.setShortcut(_translate("Form", "+"))
        self.botonO.setText(_translate("Form", "O"))
        self.botonO.setShortcut(_translate("Form", "+"))
        self.botonM.setText(_translate("Form", "M"))
        self.botonM.setShortcut(_translate("Form", "+"))
        self.botonB.setText(_translate("Form", "B"))
        self.botonB.setShortcut(_translate("Form", "-"))
        self.botonborrar.setText(_translate("Form", "<-"))
        self.botonZ.setText(_translate("Form", "Z"))
        self.botonZ.setShortcut(_translate("Form", "Esc"))
        self.botonY.setText(_translate("Form", "Y"))
        self.botonY.setShortcut(_translate("Form", "+"))
        self.botonX.setText(_translate("Form", "X"))
        self.botonX.setShortcut(_translate("Form", "%"))
        self.botonQ.setText(_translate("Form", "Q"))
        self.botonR.setText(_translate("Form", "R"))
        self.botonS.setText(_translate("Form", "S"))
        self.botonT.setText(_translate("Form", "T"))
        self.botoneliminartodo.setText(_translate("Form", "AC"))


# ====================================================================

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QPushButton, QLabel, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from PyQt5.QtWidgets import (QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)


class IngresarMatriz(object):
    arregloClase = []
    tamaFilas = 0
    tamaColumnas = 0
    limiteFilas = 0
    limiteColumnas = 0

    def __init__(self, interfazm, tamaFilas=1, tamaColum=2, arregloMatriz=[]):
        self.arregloAdevolver = arregloMatriz
        self.tamaColumnas = tamaColum
        self.limiteFilas = tamaFilas
        self.limiteColumnas = tamaColum
        self.initUI(interfazm, numFilas=tamaFilas, numColum=tamaColum)

    def initUI(self, interfaz, numFilas, numColum):
        interfaz.setObjectName("Tabla Matriz")
        interfaz.resize(800, 400)
        # Añadir diseño de caja(Box Layout), agregue la tabla al diseño de la caja y agregue el diseño de la caja al widget
        self.visorMatriz = ScrollLabel.ScrollLabel(interfaz)
        self.visorMatriz.setGeometry(10, 10, 400, 380)
        self.visorMatriz.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                       "font:  15pt \"Arial\";")
        self.visorMatriz.setObjectName("visorMatriz")

        self.Agregar_Fila = QPushButton(interfaz)
        self.Agregar_Fila.setGeometry(QtCore.QRect(490, 50, 250, 40))
        self.Agregar_Fila.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.Agregar_Fila.setObjectName("pushButton_10")
        self.Agregar_Fila.setText("Agregar Fila")

        self.Agregar_Fila.clicked.connect(self.agregarFilaMatriz)
        self.eliminarr_Fila = QPushButton(interfaz)
        self.eliminarr_Fila.setGeometry(QtCore.QRect(490, 150, 250, 40))
        self.eliminarr_Fila.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 87 14pt \"Arial Black\";")
        self.eliminarr_Fila.setObjectName("pushButton_10")
        self.eliminarr_Fila.setText("Eliminar Fila")
        self.eliminarr_Fila.clicked.connect(self.eliminar)

        self.BotonActMAtriz = QPushButton(interfaz)
        self.BotonActMAtriz.setGeometry(QtCore.QRect(490, 100, 250, 40))
        self.BotonActMAtriz.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 87 14pt \"Arial Black\";")
        self.BotonActMAtriz.setObjectName("BotonActMAtriz")
        self.BotonActMAtriz.setText("Actualizar Matriz")
        self.BotonActMAtriz.clicked.connect(self.actualizar)

        self.BotonSalir = QPushButton(interfaz)
        self.BotonSalir.setGeometry(QtCore.QRect(490, 200, 250, 40))
        self.BotonSalir.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.BotonSalir.setObjectName("BotonSalir")
        self.BotonSalir.setText("Guardar")
        self.BotonSalir.clicked.connect(interfaz.close)

        return self.arregloAdevolver
        # self.layoutVertical.addWidget(self.Agregar_Fila)
        # self.layoutVertical.addWidget(self.BotonActMAtriz)

        # self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)

    def actualizar(self):
        self.eliminarNoneArray()
        self.rellenarMatriz()
        msj = ""
        for i in range(0, len(self.arregloAdevolver)):
            msj += str(i) + "|  " + str(self.arregloAdevolver[i]) + "\n"
        self.visorMatriz.setText(msj)

    def agregarFilaMatriz(self):
        interfaz = QtWidgets.QWidget()
        text, pressed = QInputDialog.getText(interfaz, "Valores Filas",
                                             "Ingresa los valores de la fila separados por comas (,): ",
                                             QLineEdit.Normal, "")
        text2 = text.replace(",", "")
        if pressed:
            if self.tamaFilas < self.limiteFilas:
                if (len(text2)) <= self.limiteColumnas:
                    self.arregloAdevolver.append(self.ArregloFila(text))
                    self.tamaFilas += 1
                else:
                    msg = QMessageBox()
                    # msg.setIcon(QMessageBox.o)
                    msg.setText("Revisa la entrada de datos ")
                    msg.setWindowTitle("Error")
                    # msg.setStandardButtons(QMessageBox.ok)
                    retval = msg.exec_()
            else:
                msg = QMessageBox()
                # msg.setIcon(QMessageBox.o)
                msg.setText("No puedes agregar mas filas ")
                msg.setWindowTitle("Error")
                # msg.setStandardButtons(QMessageBox.ok)
                retval = msg.exec_()

    def eliminar(self):
        interfaz = QtWidgets.QWidget()
        text, pressed = QInputDialog.getInt(interfaz, "Fila a borrar",
                                            "Ingresa la fila a borrar: ",
                                            QLineEdit.Normal, 0)
        if pressed:
            self.arregloAdevolver.pop(text)

    def guardar(self):
        self.rellenarMatriz()
        return self.arregloAdevolver

    def eliminarNoneArray(self):
        i = 0
        tama = len(self.arregloAdevolver)
        while i < tama:
            if len(self.arregloAdevolver[i]) == 0:
                self.arregloAdevolver.pop(i)
                tama -= 1
            i += 1

    def ArregloFila(self, texto):
        texto = str(texto).split(',')
        numColumnas = self.tamaColumnas
        abecedario = "abcdefghijklmnopqrstuvwxyz"
        arreglo = []
        if len(texto) <= numColumnas:
            for i in range(0, len(texto)):
                valor = texto[i]
                if valor in abecedario or valor in abecedario.upper():
                    msg = QMessageBox()
                    # msg.setIcon(QMessageBox.o)
                    msg.setText("La matriz tiene alguna letra ")
                    msg.setWindowTitle("Error")
                    # msg.setStandardButtons(QMessageBox.ok)
                    retval = msg.exec_()
                else:
                    if "-" in valor:
                        aux = valor.replace("-", "")
                        dato_entrar = float(aux) * -1
                        arreglo.append(dato_entrar)
                    else:
                        arreglo.append(float(valor))
            return arreglo
        else:
            return []

    def get_data(self):
        self.rellenarMatriz()
        return self.arregloAdevolver  # arregloAdevolver

    def rellenarMatriz(self):

        for i in range(0, len(self.arregloAdevolver)):
            for j in range(0, self.limiteColumnas):
                try:
                    print(self.arregloAdevolver[i][j])
                except:
                    self.arregloAdevolver[i].append(0)


# ====================================================================

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

# remplazar la form por una nueva interfaz
