# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Matrices.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from tkinter import Scale

from PyQt5 import QtCore, QtGui, QtWidgets
from interfazcalculadoras import ScrollLabel
from funciones import calcMatrices
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(732, 1045)
        Form.setStyleSheet("background-color: rgb(250, 250, 250);\n"
                           "")
        self.matrizLabel= QtWidgets.QLabel(Form)
        self.matrizLabel.setGeometry(QtCore.QRect(80, 10, 300, 20))
        self.matrizLabel.setText('Matrices guardadas:')
        self.visor = ScrollLabel.ScrollLabel(Form)
        self.visor.setGeometry(QtCore.QRect(10, 40, 300, 180))

        self.matrizLabel2 = QtWidgets.QLabel(Form)
        self.matrizLabel2.setGeometry(QtCore.QRect(470, 10, 300, 20))
        self.matrizLabel2.setText('Matriz Resultante:')
        self.visor2Resultado = ScrollLabel.ScrollLabel(Form)
        self.visor2Resultado.setGeometry(QtCore.QRect(380, 40, 300, 180))

        self.numerodefilas = QtWidgets.QTextEdit(Form)
        self.numerodefilas.setGeometry(QtCore.QRect(10, 230, 181, 31))
        self.numerodefilas.setStyleSheet("font: 12pt \"Arial\";\n"
                                         "background-color: rgb(170, 170, 255);")
        self.numerodefilas.setObjectName("numerodefilas")
        self.numerdefilasedit = QtWidgets.QLineEdit(Form)
        self.numerdefilasedit.setGeometry(QtCore.QRect(200, 230, 161, 31))
        self.numerdefilasedit.setObjectName("numerdefilasedit")
        self.numcolumnas = QtWidgets.QTextEdit(Form)
        self.numcolumnas.setGeometry(QtCore.QRect(10, 280, 181, 31))
        self.numcolumnas.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.numcolumnas.setObjectName("numcolumnas")
        self.columnasedit = QtWidgets.QLineEdit(Form)
        self.columnasedit.setGeometry(QtCore.QRect(200, 280, 161, 31))
        self.columnasedit.setObjectName("columnasedit")
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


        self.Operaciones = QtWidgets.QTextEdit(Form)
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
        self.botonresta = QtWidgets.QPushButton(Form)
        self.botonresta.setGeometry(QtCore.QRect(110, 400, 75, 35))
        self.botonresta.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonresta.setObjectName("botonresta")
        self.botonmultiplicar = QtWidgets.QPushButton(Form)
        self.botonmultiplicar.setGeometry(QtCore.QRect(200, 400, 75, 35))
        self.botonmultiplicar.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                            "font: 87 14pt \"Arial Black\";")
        self.botonmultiplicar.setObjectName("botonmultiplicar")
        self.botonalfa = QtWidgets.QPushButton(Form)
        self.botonalfa.setGeometry(QtCore.QRect(290, 400, 75, 35))
        self.botonalfa.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonalfa.setObjectName("botonalfa")
        self.botonTranspuesta = QtWidgets.QPushButton(Form)
        self.botonTranspuesta.setGeometry(QtCore.QRect(380, 400, 75, 35))
        self.botonTranspuesta.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                            "font: 87 14pt \"Arial Black\";")
        self.botonTranspuesta.setObjectName("botonTranspuesta")
        self.botoninversa = QtWidgets.QPushButton(Form)
        self.botoninversa.setGeometry(QtCore.QRect(470, 400, 75, 35))
        self.botoninversa.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botoninversa.setObjectName("botoninversa")
        self.Resultado = QtWidgets.QTextEdit(Form)
        self.Resultado.setGeometry(QtCore.QRect(10, 690, 181, 31))
        self.Resultado.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.Resultado.setObjectName("Resultado")
        self.labelresultado = QtWidgets.QLabel(Form)
        self.labelresultado.setGeometry(QtCore.QRect(200, 690, 331, 121))
        self.labelresultado.setText("")
        self.labelresultado.setObjectName("labelresultado")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 400, 91, 41))
        self.pushButton_11.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 87 12pt \"Arial Black\";")
        self.pushButton_11.setObjectName("pushButton_11")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 460, 648, 205))
        self.widget.setObjectName("widget")
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

    def eventResultado(self):
        listado = self.objeto.get_data()#IngresarMatriz.get_data(self)#IngresarMatriz.get_data(self)#ventana.get_data()
        ecuacion ="A+B-C-D+E+F" #self.label.text()
        i =0
        msj =""
        while i<len(ecuacion):
            if ecuacion[i] == "+":
                letra1=ecuacion[i-1]
                letra2=ecuacion[i+1]
                pos1=calcMatrices.returnarPosArregloPorletra(listado,letra1)
                pos2=calcMatrices.returnarPosArregloPorletra(listado,letra2)
                #acum+=listado[pos1]
                #terner en cuenta el .shape de un arreglo ############################################################################33
                i+=3
            elif ecuacion[i] == "-":
                msj += ecuacion[i - 1] +"-"+ ecuacion[i + 1] + "\n"
                i += 3
            else:
                i+=1
        print(msj)
    import sys
    def agregarMatriz(self):
        #salir=False
        #while salir == False:
        try:
                filas = int(self.numerdefilasedit.text())
                columnas = int(self.columnasedit.text())
                self.interfaz = QtWidgets.QWidget()
                arr=[]
                self.objeto = IngresarMatriz(interfazm=self.interfaz,tamaFilas=filas,tamaColum=columnas,arregloMatriz=arr)
                self.ui = self.objeto#IngresarMatriz()#__init__(self,tamaFilas=filas,tamaColum=columnas)#initUI(self,numFilas=filas,numColum=columnas)
                self.ui.initUI(self.interfaz,numColum=columnas,numFilas=filas)
                self.interfaz.show()
        except:
                print('revisa')
    def eventbotonActualizar(self):
        arreglo = self.objeto.get_data()#IngresarMatriz.get_data(self)#IngresarMatriz.get_data(self)#ventana.get_data()
        filas = int(self.numerdefilasedit.text())
        tama=len(arreglo)
        print('tama:',len(arreglo))
        abecedario = "abcdefghijklmnopqrstuvwxyz".upper()
        print(arreglo)
        print(arreglo[0])
        aux=""
        for j in range(0,tama):#len(arreglo[i])):
            matriz = arreglo[j]
            aux += "Matriz: " + abecedario[j] + "\n"
            for i in range(0,filas):
                aux += "["
                aux += ",".join(matriz[i])+"]\n"
            aux+="\n"
        print(aux)
        self.visor.setText(aux)

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
        self.numerodefilas.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                      "p, li { white-space: pre-wrap; }\n"
                                                      "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                      "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numero de filas:</p></body></html>"))
        self.numcolumnas.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Numero de Columnas:</p></body></html>"))
        self.botonagregarvalores.setText(_translate("Form", "Agregar Matriz"))
        self.Operaciones.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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
        self.botonalfa.setText(_translate("Form", "α"))
        self.botonalfa.setShortcut(_translate("Form", "Esc"))
        self.botonTranspuesta.setText(_translate("Form", "A^T"))
        self.botonTranspuesta.setShortcut(_translate("Form", "Esc"))
        self.botoninversa.setText(_translate("Form", "A^-1"))
        self.botoninversa.setShortcut(_translate("Form", "Esc"))
        self.Resultado.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Resultado:</p></body></html>"))
        self.pushButton_11.setText(_translate("Form", "Calcular"))
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
    QPushButton, QLabel, QHBoxLayout, QDialog
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)

class IngresarMatriz(object):
    def __init__(self,interfazm,tamaFilas=0,tamaColum=0,arregloMatriz=[]):
        self.arregloAdevolver=arregloMatriz
        self.initUI(interfazm,numFilas=tamaFilas,numColum=tamaColum)



    def initUI(self,interfaz,numFilas,numColum):
        interfaz.setObjectName("Tabla Matriz")
        interfaz.resize(800,400)
        self.createTable(filas=numFilas,columnas=numColum)
        # Añadir diseño de caja(Box Layout), agregue la tabla al diseño de la caja y agregue el diseño de la caja al widget
        self.layout = QtWidgets.QHBoxLayout(interfaz)#QHBoxLayout(interfaz)
        self.corchete1 = QLabel()
        self.corchete1.setGeometry(0, 0, 91, 41)
        self.corchete1.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font:  120pt \"Arial\";")
        self.corchete1.setObjectName("corchete1")
        self.corchete1.setText("[")
        self.corchete2 = QLabel()
        self.corchete2.setGeometry(0, 0, 91, 41)
        self.corchete2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font:  120pt \"Arial\";")
        self.corchete2.setObjectName("corchete1")
        self.corchete2.setText("]")
        self.layout.addWidget(self.corchete1)
        self.layout.addWidget(self.tableWidget)
        self.layout.addWidget(self.corchete2)
        self.BotonGuardar = QPushButton()
        self.BotonGuardar.setGeometry(10, 10, 91, 41)
        self.BotonGuardar.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.BotonGuardar.setObjectName("pushButton_10")
        self.BotonGuardar.setText("Guardar")
        self.BotonGuardar.clicked.connect(self.agregarNuevaMatriz)
        self.layout.addWidget(self.BotonGuardar)
        interfaz.setLayout(self.layout)
        #self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)



    def createTable(self,filas,columnas):
        # Crea Tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setGeometry(10,45,10,10)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setRowCount(filas)
        self.tableWidget.setColumnCount(columnas)
        #self.tableWidget.setItem(0, 0, QTableWidgetItem("1"))
        #self.tableWidget.setItem(0, 1, QTableWidgetItem("2"))
        #self.tableWidget.setItem(1, 0, QTableWidgetItem("3"))
        #self.tableWidget.setItem(1, 1, QTableWidgetItem("4"))
        #self.tableWidget.setItem(2, 0, QTableWidgetItem("5"))
        #self.tableWidget.setItem(2, 1, QTableWidgetItem("6"))
        #self.tableWidget.setItem(3, 0, QTableWidgetItem("7"))
        #self.tableWidget.setItem(3, 1, QTableWidgetItem("8"))
        #self.tableWidget.move(0, 0)
        #self.tableWidget.adjustSize(True)

        # cambio de selección de tabla
        #self.tableWidget.doubleClicked.connect(self.on_click)

    def agregarNuevaMatriz(self):
        columna = self.tableWidget.columnCount()
        fila=self.tableWidget.rowCount()
        item = []
        for n in range(fila):
            #print('n: ',n)
            fila = []
            for column in range(columna):
                try:
                    #print('n: ', n, ' column: ', column, '  ', self.tableWidget.item(n, column).text())
                    fila.append(self.tableWidget.item(n, column).text())
                except:
                    fila.append('0')
            item.append(fila)
        arregloSalida=[]
        for n in range(0,len(item)):
            arregloAux=[]
            linea=",".join(item[n])
            fila=linea.split(',')
            for i in range(0,len(fila)):
                arregloAux.append(fila[i])
            arregloSalida.append(arregloAux)
            #print(linea)
        #print(arregloSalida)
        msj = ""
        #self.close()
        self.arregloAdevolver.append(arregloSalida)
        msg = QMessageBox()
        #msg.setIcon(QMessageBox.Accepted)
        msg.setText("La matriz fue agregada ")
        msg.setWindowTitle("Clompleto")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
        return arregloSalida

    def get_data(self):
        print(self.arregloAdevolver)
        return self.arregloAdevolver#arregloAdevolver
    # ref: https://pythonlcpa.blogspot.com/p/blog-page_1.html
# ====================================================================
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

