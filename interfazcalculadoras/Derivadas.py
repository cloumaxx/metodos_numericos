# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Derivadas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import  sys
from funciones import calcDerivadas as calD
class Ui_Form(object):
    funcionLabel1 = []
    funcionLabel2 = []
    def setupUi(self, Derivadas):
        Derivadas.setObjectName("Derivadas")
        Derivadas.resize(745, 611)
        Derivadas.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.textEdit = QtWidgets.QLabel(Derivadas)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 111, 31))
        self.textEdit.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLabel(Derivadas)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 70, 131, 31))
        self.textEdit_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QLabel(Derivadas)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 130, 111, 31))
        self.textEdit_3.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_4 = QtWidgets.QLabel(Derivadas)
        self.textEdit_4.setGeometry(QtCore.QRect(30, 190, 71, 31))
        self.textEdit_4.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QLabel(Derivadas)
        self.textEdit_5.setGeometry(QtCore.QRect(380, 190, 81, 31))
        self.textEdit_5.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QLabel(Derivadas)
        self.textEdit_6.setGeometry(QtCore.QRect(380, 230, 81, 31))
        self.textEdit_6.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_6.setObjectName("textEdit_6")

        self.pushButton_9 = QtWidgets.QPushButton(Derivadas)
        self.pushButton_9.setGeometry(QtCore.QRect(420, 710, 91, 41))
        self.pushButton_9.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 12pt \"Arial Black\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(Derivadas)
        self.pushButton_8.setGeometry(QtCore.QRect(610, 430, 91, 41))
        self.pushButton_8.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 12pt \"Arial Black\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.eventCalcular)
        """self.pushButton_11 = QtWidgets.QPushButton(Derivadas)
        self.pushButton_11.setGeometry(QtCore.QRect(610, 510, 91, 41))
        self.pushButton_11.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 87 12pt \"Arial Black\";")
        self.pushButton_11.setObjectName("pushButton_11")"""
        self.textEdit_7 = QtWidgets.QTextEdit(Derivadas)
        self.textEdit_7.setGeometry(QtCore.QRect(30, 230, 71, 31))
        self.textEdit_7.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(Derivadas)
        self.textEdit_8.setGeometry(QtCore.QRect(30, 270, 71, 31))
        self.textEdit_8.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QLabel(Derivadas)
        self.textEdit_9.setGeometry(QtCore.QRect(30, 310, 71, 31))
        self.textEdit_9.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QLabel(Derivadas)
        self.textEdit_10.setGeometry(QtCore.QRect(380, 270, 81, 31))
        self.textEdit_10.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QLabel(Derivadas)
        self.textEdit_11.setGeometry(QtCore.QRect(380, 310, 81, 31))
        self.textEdit_11.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.textEdit_11.setObjectName("textEdit_11")
        self.layoutWidget = QtWidgets.QWidget(Derivadas)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 350, 565, 203))
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
        self.botonSeis = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCinco.clicked.connect(self.eventBoton5)

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
        self.botonCabierto.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonCabierto.setObjectName("botonCabierto")
        self.gridLayout.addWidget(self.botonCabierto, 3, 0, 1, 1)
        self.botonCabierto.clicked.connect(self.eventBotonParentesis)

        self.botonCero = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 12pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.gridLayout.addWidget(self.botonCero, 3, 1, 1, 1)
        self.botonCero.clicked.connect(self.eventBoton0)

        self.botonCerrado = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCerrado.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 87 12pt \"Arial Black\";")
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
        self.botonMas.clicked.connect(self.eventBotonSumar)
        self.gridLayout_2.addWidget(self.botonMas, 0, 1, 1, 1)
        self.botonMas_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_2.setObjectName("botonMas_2")
        self.gridLayout_2.addWidget(self.botonMas_2, 0, 2, 1, 1)
        self.botonMas_2.clicked.connect(self.eventRaiz)

        self.botonMas_3 = QtWidgets.QPushButton(self.layoutWidget)

        self.botonMas_3.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_3.setObjectName("botonMas_3")
        self.gridLayout_2.addWidget(self.botonMas_3, 0, 3, 1, 1)
        self.botonMas_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_3.clicked.connect(self.eventBotonExp)

        self.botonMas_11.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
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
        self.botonMas_8.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_8.setObjectName("botonMas_8")
        self.gridLayout_2.addWidget(self.botonMas_8, 1, 3, 1, 1)
        self.botonMas_8.clicked.connect(self.eventBotonLog)

        self.botonMas_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_12.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
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
        self.botonMas_9.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_9.setObjectName("botonMas_9")
        self.gridLayout_2.addWidget(self.botonMas_9, 2, 3, 1, 1)
        self.botonMas_9.clicked.connect(self.eventBotonSin)

        self.botonMas_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_13.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_13.setObjectName("botonMas_13")
        self.gridLayout_2.addWidget(self.botonMas_13, 2, 4, 1, 1)
        self.botonMas_13.clicked.connect(self.eventBotonCsc)

        self.botonDivision = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDivision.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonDivision.setObjectName("botonDivision")#################################################3

        self.gridLayout_2.addWidget(self.botonDivision, 3, 1, 1, 1)
        self.botonDivision.clicked.connect(self.eventDiv)

        self.botonMas_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_5.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_5.setObjectName("botonMas_5")
        self.gridLayout_2.addWidget(self.botonMas_5, 3, 2, 1, 1)
        self.botonMas_5.clicked.connect(self.eventBotonln)

        self.botonMas_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_10.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_10.setObjectName("botonMas_10")
        self.gridLayout_2.addWidget(self.botonMas_10, 3, 3, 1, 1)
        self.botonMas_10.clicked.connect(self.eventBotonCos)


        self.botonMas_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_14.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
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
        self.BotonBorrar.clicked.connect(self.eventoBorrar)


        self.gridLayout_2.addWidget(self.BotonBorrar, 4, 3, 1, 1)
        self.botonAC = QtWidgets.QPushButton(self.layoutWidget)
        self.botonAC.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                   "background-color: rgb(0, 170, 127);")
        self.botonAC.setObjectName("botonAC")
        self.botonAC.clicked.connect(self.eventoBorrar)


        self.gridLayout_2.addWidget(self.botonAC, 4, 4, 1, 1)

        self.textEdit_12 = QtWidgets.QLineEdit(Derivadas)
        self.textEdit_12.setGeometry(QtCore.QRect(190, 70, 261, 31))
        self.textEdit_12.setObjectName("textEdit_12")

        self.label = QtWidgets.QLabel(Derivadas)
        self.label.hide()
        self.label.setObjectName("label")
        self.label.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_2 = QtWidgets.QLabel(Derivadas)
        self.label_2.setGeometry(QtCore.QRect(130, 190, 211, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_3 = QtWidgets.QLabel(Derivadas)
        self.label_3.setGeometry(QtCore.QRect(130, 230, 211, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_4 = QtWidgets.QLabel(Derivadas)
        self.label_4.setGeometry(QtCore.QRect(130, 270, 211, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        #
        self.label_5 = QtWidgets.QLabel(Derivadas)
        self.label_5.setGeometry(QtCore.QRect(180, 30, 261, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_10 = QtWidgets.QLabel(Derivadas)
        self.label_10.setGeometry(QtCore.QRect(130, 310, 221, 31))
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_6 = QtWidgets.QLabel(Derivadas)
        self.label_6.setGeometry(QtCore.QRect(480, 190, 211, 31))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_7 = QtWidgets.QLabel(Derivadas)
        self.label_7.setGeometry(QtCore.QRect(480, 230, 211, 31))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_8 = QtWidgets.QLabel(Derivadas)
        self.label_8.setGeometry(QtCore.QRect(480, 270, 211, 31))
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_9 = QtWidgets.QLabel(Derivadas)
        self.label_9.setGeometry(QtCore.QRect(480, 310, 211, 31))
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.retranslateUi(Derivadas)
        #self.pushButton_11.clicked.connect(Derivadas.hide)
        self.pushButton_9.clicked.connect(Derivadas.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Derivadas)

    def eventCalcular(self):
        try:
            self.funcion = self.label.text()
            self.variable =  self.textEdit_12.text()
            derivada1 = calD.primerDerivada(self.funcion)
            derivada2 = calD.segundaDerivada(self.funcion)
            derivada3 = calD.terceraDerivada(self.funcion)
            derivada4 = calD.cuartaDerivada(self.funcion)
            self.entrada = str(derivada1)
            self.entrada2 = str(derivada2)
            self.entrada3 = str(derivada3)
            self.entrada4 = str(derivada4)
            self.label_2.setText(self.entrada)
            self.label_3.setText(self.entrada2)
            self.label_4.setText(self.entrada3)
            self.label_10.setText(self.entrada4)

            solucion1 = calD.solucionPrimeraDerivada(self.funcion,self.variable)
            solucion2 = calD.solucionSegundaDerivada(self.funcion, self.variable)
            solucion3 = calD.solucionTerceraDerivada(self.funcion, self.variable)
            solucion4 = calD.solucionCuartaDerivada(self.funcion, self.variable)

            #self.entrada5 = str(self.textEdit_12.text)
            self.entrada6=str(solucion1)
            self.entrada7 = str(solucion2)
            self.entrada8 = str(solucion3)
            self.entrada9 = str(solucion4)

            self.label_6.setText(self.entrada6)
            self.label_7.setText(self.entrada7)
            self.label_8.setText(self.entrada8)
            self.label_9.setText(self.entrada9)
        except:
            print('algo salio mal')

        # creacion de botones
    def eventBoton0(self):
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
        Ui_Form.funcionLabel1.append('math.isqrt(')
        Ui_Form.funcionLabel2.append('√')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.isqrt('
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
        Ui_Form.funcionLabel1.append('x')
        Ui_Form.funcionLabel2.append('x')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "x"
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
        print('math.sin')
        Ui_Form.funcionLabel1.append('math.sin(')
        Ui_Form.funcionLabel2.append('sin(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.sin('
        self.entrada2 += 'sin('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCos(self):
        print('math.cos')
        Ui_Form.funcionLabel1.append('math.cos(')
        Ui_Form.funcionLabel2.append('cos(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.cos('
        self.entrada2 += 'cos('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonTan(self):
        print('math.tan')
        Ui_Form.funcionLabel1.append('math.tan(')
        Ui_Form.funcionLabel2.append('tan(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.tan('
        self.entrada2 += 'tan('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonSec(self):
        print('math.asin')
        Ui_Form.funcionLabel1.append('math.asin(')
        Ui_Form.funcionLabel2.append('sec(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.asin('
        self.entrada2 += 'sec('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCsc(self):
        print('math.acos')
        Ui_Form.funcionLabel1.append('math.csc(')
        Ui_Form.funcionLabel2.append('csc(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.csc('
        self.entrada2 += 'csc('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonCot(self):
        print('math.atan')
        Ui_Form.funcionLabel1.append('math.atan(')
        Ui_Form.funcionLabel2.append('tan(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.atan('
        self.entrada2 += 'cot('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonLog(self):
        print('math.log')
        Ui_Form.funcionLabel1.append('math.log(')
        Ui_Form.funcionLabel2.append('log(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.log('
        self.entrada2 += 'log('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonExp(self):
        print('math.exp')
        Ui_Form.funcionLabel1.append('math.exp(')
        Ui_Form.funcionLabel2.append('e(')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += 'math.exp('
        self.entrada2 += 'e('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventBotonln(self):
        print('math.log(')
        Ui_Form.funcionLabel1.append('math.log(')
        Ui_Form.funcionLabel2.append('ln(')
        self.entrada = self.label.text()
        self.entrada += 'math.log('
        self.entrada2 += 'ln('
        self.label.setText(self.entrada)
        self.label_5.setText(self.entrada2)

    def eventoBorrar(self):
        import numpy as np
        # self.label.setText(self.entrada[:len(self.entrada)-1])
        try:
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
            print('no se puede borrar mas')

    def retranslateUi(self, Derivadas):

        _translate = QtCore.QCoreApplication.translate
        Derivadas.setWindowTitle(_translate("Derivadas", "Calculadora de Derivadas"))
        self.textEdit.setText(_translate("Derivadas","F(x):"))
        self.textEdit_2.setText(_translate("Derivadas", "Valor de X:"))
        self.textEdit_3.setText(_translate("Derivadas", "Derivadas"))
        self.textEdit_4.setText(_translate("Derivadas", " f \'(x):"))
        self.textEdit_5.setText(_translate("Derivadas", " f \'(x):"))
        self.textEdit_6.setText(_translate("Derivadas", " f \'\'(x):"))
        self.textEdit_7.setText(_translate("Derivadas", " f \'\'(x):"))
        self.textEdit_8.setText(_translate("Derivadas", " f \'\'\'(x):"))
        self.textEdit_9.setText(_translate("Derivadas", " f \'\'\'\'(x):"))
        self.textEdit_10.setText(_translate("Derivadas"," f \'\'\'(x):"))
        self.textEdit_11.setText(_translate("Derivadas"," f \'\'\'\'(x):"))
        self.pushButton_9.setText(_translate("Derivadas", "Borrar"))
        self.pushButton_8.setText(_translate("Derivadas", "Calcular"))
        #self.pushButton_11.setText(_translate("Derivadas", "Salir"))
        self.botonUno.setText(_translate("Derivadas", "1"))
        self.botonUno.setShortcut(_translate("Derivadas", "1"))
        self.botonDos.setText(_translate("Derivadas", "2"))
        self.botonDos.setShortcut(_translate("Derivadas", "2"))
        self.botonTres.setText(_translate("Derivadas", "3"))
        self.botonTres.setShortcut(_translate("Derivadas", "3"))
        self.botonCuatro.setText(_translate("Derivadas", "4"))
        self.botonCuatro.setShortcut(_translate("Derivadas", "4"))
        self.botonCinco.setText(_translate("Derivadas", "5"))
        self.botonCinco.setShortcut(_translate("Derivadas", "5"))
        self.botonSeis.setText(_translate("Derivadas", "6"))
        self.botonSeis.setShortcut(_translate("Derivadas", "6"))
        self.botonSiete.setText(_translate("Derivadas", "7"))
        self.botonSiete.setShortcut(_translate("Derivadas", "7"))
        self.botonOcho.setText(_translate("Derivadas", "8"))
        self.botonOcho.setShortcut(_translate("Derivadas", "8"))
        self.botonNueve.setText(_translate("Derivadas", "9"))
        self.botonNueve.setShortcut(_translate("Derivadas", "9"))
        self.botonCabierto.setText(_translate("Derivadas", "("))
        self.botonCabierto.setShortcut(_translate("Derivadas", "("))
        self.botonCero.setText(_translate("Derivadas", "0"))
        self.botonCero.setShortcut(_translate("Derivadas", "0"))
        self.botonCerrado.setText(_translate("Derivadas", ")"))
        self.botonCerrado.setShortcut(_translate("Derivadas", ")"))
        self.botonCabierto_2.setText(_translate("Derivadas", "["))
        self.botonCabierto_2.setShortcut(_translate("Derivadas", "("))
        self.botonPunto.setText(_translate("Derivadas", "."))
        self.botonPunto.setShortcut(_translate("Derivadas", "."))
        self.botonCabierto_3.setText(_translate("Derivadas", "]"))
        self.botonCabierto_3.setShortcut(_translate("Derivadas", "("))
        self.botonMas.setText(_translate("Derivadas", "+"))
        self.botonMas.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_2.setText(_translate("Derivadas", "√"))
        self.botonMas_2.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_3.setText(_translate("Derivadas", "exp"))
        self.botonMas_3.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_11.setText(_translate("Derivadas", "tan"))
        self.botonMas_11.setShortcut(_translate("Derivadas", "+"))
        self.botonMenos.setText(_translate("Derivadas", "-"))
        self.botonMenos.setShortcut(_translate("Derivadas", "-"))
        self.botonMas_4.setText(_translate("Derivadas", "^"))
        self.botonMas_4.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_8.setText(_translate("Derivadas", "log"))
        self.botonMas_8.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_12.setText(_translate("Derivadas", "sec"))
        self.botonMas_12.setShortcut(_translate("Derivadas", "+"))
        self.BotonMulti.setText(_translate("Derivadas", "*"))
        self.BotonMulti.setShortcut(_translate("Derivadas", "*"))
        self.botonMas_7.setText(_translate("Derivadas", "π"))
        self.botonMas_7.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_9.setText(_translate("Derivadas", "sin"))
        self.botonMas_9.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_13.setText(_translate("Derivadas", "csc"))
        self.botonMas_13.setShortcut(_translate("Derivadas", "+"))
        self.botonDivision.setText(_translate("Derivadas", "÷"))
        self.botonDivision.setShortcut(_translate("Derivadas", "/"))
        self.botonMas_5.setText(_translate("Derivadas", "ln"))
        self.botonMas_5.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_10.setText(_translate("Derivadas", "cos"))
        self.botonMas_10.setShortcut(_translate("Derivadas", "+"))
        self.botonMas_14.setText(_translate("Derivadas", "cot"))
        self.botonMas_14.setShortcut(_translate("Derivadas", "+"))
        self.botonPorcentaje.setText(_translate("Derivadas", "%"))
        self.botonPorcentaje.setShortcut(_translate("Derivadas", "%"))
        self.botonMas_6.setText(_translate("Derivadas", "x"))
        self.botonMas_6.setShortcut(_translate("Derivadas", "+"))
        self.BotonBorrar.setText(_translate("Derivadas", "C"))
        self.BotonBorrar.setShortcut(_translate("Derivadas", "Esc"))
        self.botonAC.setText(_translate("Derivadas", "AC"))
        self.label.setText(_translate("Derivadas", "")) # label de la funcion ingresada
        self.label_2.setText(_translate("Derivadas", "")) # primera derivada
        self.label_3.setText(_translate("Derivadas", "")) # segunda derivada
        self.label_4.setText(_translate("Derivadas", "")) # tercera derivada
        self.label_10.setText(_translate("Derivadas", "")) # cuarta derivada

        self.label_5.setText(_translate("Derivadas", "")) # label a usar nosotros
        self.label_6.setText(_translate("Derivadas", "")) #solucion primera derivada
        self.label_7.setText(_translate("Derivadas", "")) # solucion segunda derivada
        self.label_8.setText(_translate("Derivadas", "")) #solucion tercerea derivada
        self.label_9.setText(_translate("Derivadas", "")) #solucion cuarta derivada


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Derivadas = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Derivadas)
    Derivadas.show()
    sys.exit(app.exec_())
