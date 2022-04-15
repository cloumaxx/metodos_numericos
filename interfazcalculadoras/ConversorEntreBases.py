# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConversorEntreBases.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from funciones import calcBases
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import *

from interfazcalculadoras import menuPrincipal


class Ui_ConversorEntreBases(object):
    estadoNum="Decimal"
    def setupUi(self, ConversorEntreBases):
        ConversorEntreBases.setObjectName("ConversorEntreBases")
        ConversorEntreBases.resize(800, 800)
        ConversorEntreBases.setStyleSheet("\n"
                                          "background-color: rgb(250, 250, 250);")
        self.TextCon = QtWidgets.QLabel(ConversorEntreBases)
        self.TextCon.setGeometry(QtCore.QRect(20, 25, 350, 31))
        self.TextCon.setStyleSheet("font: 12pt \"Arial\";\nbackground-color: rgb(170, 170, 255);")
        self.TextCon.setObjectName("TextCon")

        self.label1 = QtWidgets.QLabel(ConversorEntreBases)
        self.label1.setGeometry(QtCore.QRect(20, 140, 350, 31))
        self.label1.setObjectName("label1")
        self.label1.setStyleSheet(
            "font: 12pt \"Arial\";\nbackground-color: rgb(170, 170, 255);")  ##################################################################################################

        self.BotonNum = QtWidgets.QLabel(ConversorEntreBases)
        self.BotonNum.setGeometry(QtCore.QRect(20, 90, 200, 31))
        self.BotonNum.setStyleSheet("font: 12pt \"Arial\";\nbackground-color: rgb(0, 170, 255);")
        self.BotonNum.setObjectName("BotonNum")

        self.Binario = QtWidgets.QRadioButton(ConversorEntreBases)
        self.Binario.setGeometry(QtCore.QRect(40, 180, 81, 41))
        self.Binario.setStyleSheet("font: 75 12pt \"Arial\";\nbackground-color: rgb(101, 255, 175);")
        self.Binario.setObjectName("Binario")
        self.Binario.clicked.connect(self.estadoBinario)

        self.Octal = QtWidgets.QRadioButton(ConversorEntreBases)
        self.Octal.setGeometry(QtCore.QRect(160, 180, 81, 41))
        self.Octal.setStyleSheet("font: 75 12pt \"Arial\";\nbackground-color: rgb(101, 255, 175);")
        self.Octal.setObjectName("Octal")
        self.Octal.clicked.connect(self.estadoOctal)
        self.Decimal = QtWidgets.QRadioButton(ConversorEntreBases)
        self.Decimal.setGeometry(QtCore.QRect(280, 180, 81, 41))
        self.Decimal.setStyleSheet("font: 75 12pt \"Arial\";\nbackground-color: rgb(101, 255, 175);")
        self.Decimal.setObjectName("Decimal")
        self.Decimal.clicked.connect(self.estadoDecimal)
        self.Hexadecimal = QtWidgets.QRadioButton(ConversorEntreBases)
        self.Hexadecimal.setGeometry(QtCore.QRect(400, 180, 120, 41))
        self.Hexadecimal.setStyleSheet("font: 75 12pt \"Arial\";\nbackground-color: rgb(101, 255, 175);")
        self.Hexadecimal.setObjectName("Hexadecimal")
        self.Hexadecimal.clicked.connect(self.estadoHexadecimal)

        self.botonCalcular = QtWidgets.QPushButton(ConversorEntreBases)
        self.botonCalcular.setGeometry(QtCore.QRect(550, 180, 120, 41))
        self.botonCalcular.setStyleSheet("font: 75 12pt \"Arial\";\nbackground-color: rgb(101, 255, 175);")
        self.botonCalcular.setObjectName("botonCalcular")
        self.botonCalcular.setText('Calcular')
        self.botonCalcular.clicked.connect(self.eventCalcular)

        self.BotonBin = QtWidgets.QLabel(ConversorEntreBases)
        self.BotonBin.setGeometry(QtCore.QRect(20, 240, 130, 31))
        self.BotonBin.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonBin.setObjectName("BotonBin")

        self.BotonOctal = QtWidgets.QLabel(ConversorEntreBases)
        self.BotonOctal.setGeometry(QtCore.QRect(20, 290, 130, 31))
        self.BotonOctal.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonOctal.setObjectName("BotonOctal")
        self.BotonDec = QtWidgets.QLabel(ConversorEntreBases)
        self.BotonDec.setGeometry(QtCore.QRect(20, 340, 130, 31))
        self.BotonDec.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonDec.setObjectName("BotonDec")
        self.BotonHex = QtWidgets.QLabel(ConversorEntreBases)
        self.BotonHex.setGeometry(QtCore.QRect(20, 400, 130, 31))
        self.BotonHex.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonHex.setObjectName("BotonHex")

        self.layoutWidget = QtWidgets.QWidget(ConversorEntreBases)
        self.layoutWidget.setGeometry(QtCore.QRect(17, 440, 320, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.botonUno = QtWidgets.QPushButton(self.layoutWidget)
        self.botonUno.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonUno.setObjectName("botonUno")
        self.botonUno.clicked.connect(self.eventBoton1)

        self.gridLayout.addWidget(self.botonUno, 0, 0, 1, 1)
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

        self.BotonC = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonC.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                  "font: 87 14pt \"Arial Black\";")
        self.BotonC.setObjectName("BotonC")
        self.gridLayout.addWidget(self.BotonC, 0, 3, 1, 1)
        self.BotonC.clicked.connect(self.eventBotonC)

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

        self.botonD = QtWidgets.QPushButton(self.layoutWidget)
        self.botonD.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonD.setObjectName("botonD")
        self.gridLayout.addWidget(self.botonD, 1, 3, 1, 1)
        self.botonD.clicked.connect(self.eventBotonD)
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

        self.botonE = QtWidgets.QPushButton(self.layoutWidget)
        self.botonE.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonE.setObjectName("botonE")
        self.gridLayout.addWidget(self.botonE, 2, 3, 1, 1)
        self.botonE.clicked.connect(self.eventBotonE)
        self.botonCero = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.gridLayout.addWidget(self.botonCero, 3, 0, 1, 1)
        self.botonCero.clicked.connect(self.eventBoton0)

        self.botonA = QtWidgets.QPushButton(self.layoutWidget)
        self.botonA.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonA.setObjectName("botonA")
        self.gridLayout.addWidget(self.botonA, 3, 1, 1, 1)
        self.botonB = QtWidgets.QPushButton(self.layoutWidget)
        self.botonB.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonB.clicked.connect(self.eventBotonB)
        self.botonA.clicked.connect(self.eventBotonA)
        self.botonB.setObjectName("botonMenos")
        self.gridLayout.addWidget(self.botonB, 3, 2, 1, 1)
        self.botonF = QtWidgets.QPushButton(self.layoutWidget)
        self.botonF.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                  "background-color: rgb(0, 170, 127);")
        self.botonF.setObjectName("botonF")
        self.botonF.clicked.connect(self.eventBotonF)
        self.gridLayout.addWidget(self.botonF, 3, 3, 1, 1)
        self.BotonBorrar = QtWidgets.QPushButton(ConversorEntreBases)
        self.BotonBorrar.setGeometry(QtCore.QRect(20, 610, 75, 35))
        self.BotonBorrar.setStyleSheet("background-color: rgb(85, 170, 127);\n"
                                       "font: 75 10pt \"Arial\";")
        self.BotonBorrar.setObjectName("BotonBorrar")
        self.BotonBorrar.clicked.connect(self.eventoBorrar)

        self.BotonPunto = QtWidgets.QPushButton(ConversorEntreBases)
        self.BotonPunto.setGeometry(QtCore.QRect(100, 610, 75, 35))
        self.BotonPunto.setStyleSheet("background-color: rgb(85, 170, 127);\n"
                                       "font: 90 10pt \"Arial\";")
        self.BotonPunto.setObjectName("BotonPunto")
        self.BotonPunto.clicked.connect(self.eventoPunto)
        ##################################################################
        self.label = QtWidgets.QLabel(ConversorEntreBases)
        self.label.setGeometry(QtCore.QRect(250, 90, 230, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "border-radius: 25px;border: 1px solid black;")  ##################################################################################################

        self.label_3 = QtWidgets.QLabel(ConversorEntreBases)
        self.label_3.setGeometry(QtCore.QRect(180, 240, 230, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_4 = QtWidgets.QLabel(ConversorEntreBases)
        self.label_4.setGeometry(QtCore.QRect(180, 290, 230, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_5 = QtWidgets.QLabel(ConversorEntreBases)
        self.label_5.setGeometry(QtCore.QRect(180, 340, 230, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_6 = QtWidgets.QLabel(ConversorEntreBases)
        self.label_6.setGeometry(QtCore.QRect(180, 390, 230, 31))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.retranslateUi(ConversorEntreBases)
        #
        QtCore.QMetaObject.connectSlotsByName(ConversorEntreBases)

    # Creacion Botones Teclado
    def estadoDecimal(self):
        self.estadoNum = "Decimal"
    def estadoBinario(self):
        self.estadoNum="Binario"
    def estadoOctal(self):
        self.estadoNum="Octal"
    def estadoHexadecimal(self):
        self.estadoNum="Hexadecimal"

    def eventoBorrarTotal(self):
        try:
            self.entrada = self.label.text()
            tamaño = len(self.entrada)
            self.label.setText(self.entrada[:tamaño - tamaño])
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)

            msg.setText("No hay mas datos que borrar")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)

            retval = msg.exec_()
    def eventoBorrar(self):
        self.entrada = self.label.text()
        self.label.setText(self.entrada[:len(self.entrada)-1])
    def eventoPunto(self):
        print('.')
        self.entrada = self.label.text()
        self.entrada += "."
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

    def eventCalcular(self):
        estado=self.validarNumero()
        if estado==True:
            if self.estadoNum=="Decimal":
                self.eventBotonDecimal()
            elif self.estadoNum=="Binario":
                self.eventBotonBinario()
            elif self.estadoNum == "Octal":
                self.eventBotonOctagonal()
            elif self.estadoNum == "Hexadecimal":
                self.eventBotonHexagecimal()
            print('entro')
        else:
            print('salio')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Hubo Algun error, revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    def eventBotonDecimal(self):
        self.entrada = self.label.text()
        try:
            respuesta = self.entrada

            mostrarBinario = calcBases.algoritmoAbase(respuesta, 2)
            mostrarOctal = calcBases.algoritmoAbase(respuesta, 8)
            mostrarHexal = calcBases.algoritmoAbase(respuesta, 16)

            self.label_3.setText(str(mostrarBinario))
            self.label_4.setText(str(mostrarOctal))
            self.label_5.setText(str(respuesta))
            self.label_6.setText(str(mostrarHexal))
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    def validarNumero(self):
        numero = self.label.text()
        valido = True
        if self.estadoNum=="Decimal":
            try:
                numero = numero.replace('.', '')
                for i in range(0, len(numero)):
                    print(type(numero[i]))
            except:
               valido = False
        elif self.estadoNum=="Binario":
            try:
                numero = numero.replace('.', '')
                i=0
                while i <len(numero) and valido==True:
                    num = float(numero[i])
                    if num < 0 or num > 1:
                        valido = False
                    i+=1
            except:
                valido = False
        elif self.estadoNum == "Octal":
            try:
                numero = numero.replace('.', '')
                print(numero)
                for i in range(0, len(numero)):
                    num = float(numero[i])
                    if num < 0 or num > 8:
                        valido = False
            except:
                valido = False
        elif self.estadoNum == "Hexadecimal":
            try:
                numero = numero.replace('.', '')
                numero = numero.replace('A', '')
                numero = numero.replace('a', '')
                numero = numero.replace('B', '')
                numero = numero.replace('b', '')
                numero = numero.replace('c', '')
                numero = numero.replace('C', '')
                numero = numero.replace('D', '')
                numero = numero.replace('d', '')
                numero = numero.replace('E', '')
                numero = numero.replace('e', '')
                numero = numero.replace('F', '')
                numero = numero.replace('f', '')
                print(numero)
                for i in range(0, len(numero)):
                    num = float(numero[i])
                    if num < 0 :
                        valido = False
            except:
                valido = False

        return valido
    def eventBotonBinario(self):
        self.entrada = self.label.text()
        try:
            respuesta = self.entrada
            decimal = calcBases.algoritmoAdecimal(respuesta, 2)

            mostrarOctal = calcBases.algoritmoAbase(decimal, 8)
            mostrarHexal = calcBases.algoritmoAbase(decimal, 16)

            self.label_3.setText(str(respuesta))
            self.label_4.setText(str(mostrarOctal))
            self.label_5.setText(str(decimal))
            self.label_6.setText(str(mostrarHexal))
        except:
            self.label.setText("Error")

    def eventBotonOctagonal(self):
        self.entrada = self.label.text()
        try:
            respuesta = self.entrada
            decimal = calcBases.algoritmoAdecimal(respuesta, 8)
            mostrarBinario = calcBases.algoritmoAbase(decimal, 2)
            mostrarHexal = calcBases.algoritmoAbase(decimal, 16)

            self.label_3.setText(str(mostrarBinario))  # binario
            self.label_4.setText(str(respuesta))  # octal
            self.label_5.setText(str(decimal))  # decimal
            self.label_6.setText(str(mostrarHexal))  # hexagecimal
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def eventBotonHexagecimal(self):
        self.entrada = self.label.text()
        try:
            respuesta = self.entrada
            decimal = calcBases.algoritmoAdecimal(respuesta, 16)
            mostrarBinario = calcBases.algoritmoAbase(decimal, 2)
            mostrarOctal = calcBases.algoritmoAbase(decimal, 8)

            self.label_3.setText(str(mostrarBinario))  # binario
            self.label_4.setText(str(mostrarOctal))  # octal
            self.label_5.setText(str(decimal))  # decimal
            self.label_6.setText(str(respuesta))  # hexagecimal
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def retranslateUi(self, ConversorEntreBases):
        _translate = QtCore.QCoreApplication.translate
        ConversorEntreBases.setWindowTitle(_translate("ConversorEntreBases", "Conversor Entre Bases"))
        self.TextCon.setText(_translate("ConversorEntreBases", "  Digita el numero a convertir"))
        self.BotonNum.setText(_translate("ConversorEntreBases", "  Numero a Convertir:"))
        self.label1.setText(_translate("ConversorEntreBases", "  ¿En que base se encuentra?"))

        self.Binario.setText(_translate("ConversorEntreBases", "Binario"))
        self.Octal.setText(_translate("ConversorEntreBases", "Octal"))
        self.Decimal.setText(_translate("ConversorEntreBases", "Decimal"))
        self.Hexadecimal.setText(_translate("ConversorEntreBases", " Hexadecimal"))
        self.BotonBin.setText(_translate("ConversorEntreBases", "  Binario:"))
        self.BotonOctal.setText(_translate("ConversorEntreBases", "  Octal:"))
        self.BotonDec.setText(_translate("ConversorEntreBases", "  Decimal:"))
        self.BotonHex.setText(_translate("ConversorEntreBases", "  Hexadecimal:"))
        self.botonUno.setText(_translate("ConversorEntreBases", "1"))
        self.botonUno.setShortcut(_translate("ConversorEntreBases", "1"))
        self.botonDos.setText(_translate("ConversorEntreBases", "2"))
        self.botonDos.setShortcut(_translate("ConversorEntreBases", "2"))
        self.botonTres.setText(_translate("ConversorEntreBases", "3"))
        self.botonTres.setShortcut(_translate("ConversorEntreBases", "3"))
        self.BotonC.setText(_translate("ConversorEntreBases", "C"))
        self.botonCuatro.setText(_translate("ConversorEntreBases", "4"))
        self.botonCuatro.setShortcut(_translate("ConversorEntreBases", "4"))
        self.botonCinco.setText(_translate("ConversorEntreBases", "5"))
        self.botonCinco.setShortcut(_translate("ConversorEntreBases", "5"))
        self.botonSeis.setText(_translate("ConversorEntreBases", "6"))
        self.botonSeis.setShortcut(_translate("ConversorEntreBases", "6"))
        self.botonD.setText(_translate("ConversorEntreBases", "D"))
        self.botonSiete.setText(_translate("ConversorEntreBases", "7"))
        self.botonSiete.setShortcut(_translate("ConversorEntreBases", "7"))
        self.botonOcho.setText(_translate("ConversorEntreBases", "8"))
        self.botonOcho.setShortcut(_translate("ConversorEntreBases", "8"))
        self.botonNueve.setText(_translate("ConversorEntreBases", "9"))
        self.botonNueve.setShortcut(_translate("ConversorEntreBases", "9"))
        self.botonE.setText(_translate("ConversorEntreBases", "E"))
        self.botonCero.setText(_translate("ConversorEntreBases", "0"))
        self.botonCero.setShortcut(_translate("ConversorEntreBases", "0"))
        self.botonA.setText(_translate("ConversorEntreBases", "A"))
        self.botonB.setText(_translate("ConversorEntreBases", "B"))
        self.botonF.setText(_translate("ConversorEntreBases", "F"))
        self.BotonBorrar.setText(_translate("ConversorEntreBases", "<-"))
        self.BotonPunto.setText(_translate("ConversorEntreBases", "."))
        self.label.setText(_translate("ConversorEntreBases", ""))
        self.label_3.setText(_translate("ConversorEntreBases", ""))  # binario
        self.label_4.setText(_translate("ConversorEntreBases", ""))  # octal
        self.label_5.setText(_translate("ConversorEntreBases", ""))  # decimal
        self.label_6.setText(_translate("ConversorEntreBases", ""))  # hexagecimal



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bases = QtWidgets.QWidget()
    ui = Ui_ConversorEntreBases()
    ui.setupUi(Bases)
    Bases.show()
    sys.exit(app.exec_())

