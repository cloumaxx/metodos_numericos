# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IEEE.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from funciones import calcIEEE as iee
from interfazcalculadoras import ScrollLabel
import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

class Ui_Form(object):
    estadoNum="Decimal"
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 855)
        Form.setStyleSheet("background-color: rgb(250, 250, 250);")
        Form.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))  # se copia y pega esta linea en todas  las interfaces
        # pero le cambias el inicio segun corresponda
        Form.setWindowIcon(QtGui.QIcon(resolver_ruta('imagenes/icono.png')))  # se copia y pega esta linea en todas  las interfaces
        self.imagenFondo = QtWidgets.QLabel(Form)
        pixmap = QPixmap(resolver_ruta('imagenes/fondo1.png'))
        self.imagenFondo.setPixmap(pixmap)
        self.imagenFondo.setGeometry(0, 0, 270, 120)
        self.imagenFondo.resize(pixmap.width(), pixmap.height())

        self.textEdit_1 = QtWidgets.QLabel(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(600, 500, 300, 120))  # (ancho,largo del cajon)
        self.textEdit_1.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(35, 223, 166 );")
        self.textEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.textEdit_1.setText("En esta opcion de nuestra \n"
                                "calculadora funciona ingresando la\n"
                                "el numero que deses convertir\n"
                                "seleccionando que opcion de las que \n"
                                "estan ahi deseas")

        self.BotonNum = QtWidgets.QLabel(Form)
        self.BotonNum.setGeometry(QtCore.QRect(20, 30, 161, 31))
        self.BotonNum.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonNum.setObjectName("BotonNum")

        self.preguntarBase = QtWidgets.QLabel(Form)
        self.preguntarBase.setGeometry(QtCore.QRect(20, 80, 230, 31))
        self.preguntarBase.setText('  ¿En que base se encuentra?')
        self.preguntarBase.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.preguntarBase.setObjectName("preguntarBase")


        self.botonDecimal = QtWidgets.QRadioButton(Form)
        self.botonDecimal.setGeometry(QtCore.QRect(70, 130, 101, 41))
        self.botonDecimal.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                    "font: 75 10pt \"Arial\";")
        self.botonDecimal.setObjectName("botonDecimal")
        self.botonDecimal.clicked.connect(self.estadoDecimal)

        self.boton32 = QtWidgets.QRadioButton(Form)
        self.boton32.setGeometry(QtCore.QRect(200, 130, 101, 41))
        self.boton32.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                    "font: 75 10pt \"Arial\";")
        self.boton32.setObjectName("32 bits")
        self.boton32.setText('32 bits')
        self.boton32.clicked.connect(self.estado32)

        self.boton64 = QtWidgets.QRadioButton(Form)
        self.boton64.setGeometry(QtCore.QRect(330, 130, 101, 41))
        self.boton64.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                   "font: 75 10pt \"Arial\";")
        self.boton64.setObjectName("64 bits")
        self.boton64.setText('64 bits')
        self.boton64.clicked.connect(self.estado64)

        self.botonCalcular = QtWidgets.QPushButton(Form)
        self.botonCalcular.setGeometry(QtCore.QRect(470, 130, 101, 41))
        self.botonCalcular.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                   "font: 75 10pt \"Arial\";")
        self.botonCalcular.setObjectName("botonCalcular")
        self.botonCalcular.setText('Calcular')
        self.botonCalcular.clicked.connect(self.eventBotonCalcular)

        self.BotonNum_2 = QtWidgets.QLabel(Form)
        self.BotonNum_2.setGeometry(QtCore.QRect(30, 240, 101, 31))
        self.BotonNum_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonNum_2.setObjectName("BotonNum_2")
        self.BotonSig1 = QtWidgets.QLabel(Form)
        self.BotonSig1.setGeometry(QtCore.QRect(30, 290, 101, 31))
        self.BotonSig1.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.BotonSig1.setObjectName("BotonSig1")
        self.BotonExpo = QtWidgets.QLabel(Form)
        self.BotonExpo.setGeometry(QtCore.QRect(30, 340, 101, 31))
        self.BotonExpo.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.BotonExpo.setObjectName("BotonExpo")
        self.BotonSigni = QtWidgets.QLabel(Form)
        self.BotonSigni.setGeometry(QtCore.QRect(30, 390, 101, 31))
        self.BotonSigni.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonSigni.setObjectName("BotonSigni")
        self.BotonValCom = QtWidgets.QLabel(Form)
        self.BotonValCom.setGeometry(QtCore.QRect(30, 440, 121, 31))
        self.BotonValCom.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.BotonValCom.setObjectName("BotonValCom")
        self.BotonNum2 = QtWidgets.QLabel(Form)
        self.BotonNum2.setGeometry(QtCore.QRect(390, 240, 101, 31))
        self.BotonNum2.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "background-color: rgb(170, 170, 255);")
        self.BotonNum2.setObjectName("BotonNum2")

        self.BotonSigni2 = QtWidgets.QLabel(Form)
        self.BotonSigni2.setGeometry(QtCore.QRect(390, 390, 101, 31))
        self.BotonSigni2.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(170, 170, 255);")
        self.BotonSigni2.setObjectName("BotonSigni2")

        self.BotonExpon = QtWidgets.QLabel(Form)
        self.BotonExpon.setGeometry(QtCore.QRect(390, 340, 101, 31))
        self.BotonExpon.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonExpon.setObjectName("BotonExpon")
        self.BotonValor = QtWidgets.QLabel(Form)
        self.BotonValor.setGeometry(QtCore.QRect(390, 440, 121, 31))
        self.BotonValor.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonValor.setObjectName("BotonValor")
        self.BotonSig = QtWidgets.QLabel(Form)
        self.BotonSig.setGeometry(QtCore.QRect(390, 290, 101, 31))
        self.BotonSig.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "background-color: rgb(170, 170, 255);")
        self.BotonSig.setObjectName("BotonSig")
        self.label_2=QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 200, 71, 41))
        self.label_2.setStyleSheet("font: 75 italic 12pt \"Arial\";")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border-radius: 25px;border: 1px solid black;")
        valor = self.label_2
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(530, 200, 71, 41))
        self.label_3.setStyleSheet("font: 75 italic 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(210, 500, 320, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setStyleSheet("background-color: rgb(170, 170, 255)")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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

        self.botonMenos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMenos.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(85, 170, 255);")
        self.botonMenos.setObjectName("botonMenos")
        self.botonMenos.clicked.connect(self.eventoBorrarTotal)

        self.gridLayout.addWidget(self.botonMenos, 3, 2, 1, 1)
        self.botonOcho = QtWidgets.QPushButton(self.layoutWidget)
        self.botonOcho.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonOcho.setObjectName("botonOcho")
        self.gridLayout.addWidget(self.botonOcho, 2, 1, 1, 1)
        self.botonOcho.clicked.connect(self.eventBoton8)

        self.botonSeis = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSeis.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonSeis.setObjectName("botonSeis")
        self.gridLayout.addWidget(self.botonSeis, 1, 2, 1, 1)
        self.botonSeis.clicked.connect(self.eventBoton6)

        self.botonNueve = QtWidgets.QPushButton(self.layoutWidget)
        self.botonNueve.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonNueve.setObjectName("botonNueve")
        self.gridLayout.addWidget(self.botonNueve, 2, 2, 1, 1)
        self.botonNueve.clicked.connect(self.eventBoton9)

        self.botonSiete = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSiete.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonSiete.setObjectName("botonSiete")
        self.gridLayout.addWidget(self.botonSiete, 2, 0, 1, 1)
        self.botonSiete.clicked.connect(self.eventBoton7)

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

        self.botonCero_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.botonCero_2.setObjectName("botonCero_2")
        self.gridLayout.addWidget(self.botonCero_2, 3, 0, 1, 1)
        self.botonCero_2.clicked.connect(self.eventBoton0)

        self.botonPunto = QtWidgets.QPushButton(Form)
        self.botonPunto.setGeometry(QtCore.QRect(100, 650, 75, 35))
        self.botonPunto.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 100 30pt \"Arial\";")
        self.botonPunto.setObjectName("botonPunto")
        self.botonPunto.setText("..")
        self.botonPunto.clicked.connect(self.eventoPunto)

        self.botonCero = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.botonCero.clicked.connect(self.eventoBorrar)


        self.gridLayout.addWidget(self.botonCero, 3, 1, 1, 1)
        self.Borrar = QtWidgets.QPushButton(Form)
        self.Borrar.setGeometry(QtCore.QRect(0, 730, 91, 41))
        self.Borrar.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                  "font: 87 12pt \"Arial Black\";")
        self.Borrar.setObjectName("Borrar")


        self.Salir = QtWidgets.QPushButton(Form)
        self.Salir.setGeometry(QtCore.QRect(330, 730, 91, 41))
        self.Salir.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                 "font: 87 12pt \"Arial Black\";")
        self.Salir.setObjectName("Salir")
        self.Salir_2 = QtWidgets.QPushButton(Form)
        self.Salir_2.setGeometry(QtCore.QRect(460, 730, 91, 41))
        self.Salir_2.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                   "font: 87 12pt \"Arial Black\";")
        self.Salir_2.setObjectName("Salir_2")

        self.label = QtWidgets.QLineEdit(Form)
        self.label.setGeometry(QtCore.QRect(210, 30, 300, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_5 = QtWidgets.QLineEdit(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 240, 201, 31))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLineEdit(Form)
        self.label_6.setGeometry(QtCore.QRect(150, 290, 201, 31))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLineEdit(Form)
        self.label_7.setGeometry(QtCore.QRect(150, 340, 201, 31))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLineEdit(Form)
        self.label_8.setGeometry(QtCore.QRect(160, 390, 201, 31))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLineEdit(Form)
        self.label_9.setGeometry(QtCore.QRect(170, 440, 201, 31))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLineEdit(Form)
        self.label_10.setGeometry(QtCore.QRect(510, 240, 201, 31))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLineEdit(Form)
        self.label_11.setGeometry(QtCore.QRect(510, 290, 201, 31))
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLineEdit(Form)
        self.label_12.setGeometry(QtCore.QRect(510, 340, 201, 31))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLineEdit(Form)
        self.label_13.setGeometry(QtCore.QRect(510, 390, 201, 31))
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLineEdit(Form)
        self.label_14.setGeometry(QtCore.QRect(530, 440, 201, 31))
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def eventDecimalAotras(self,entrada):
        try:
            arreglo= iee.ieee(float(entrada))
            arreglo32=arreglo[0]
            numero="".join(arreglo32)
            ele = numero.split(' ')
            self.label_5.setText(entrada)
            self.label_6.setText(ele[0])
            self.label_7.setText(ele[1])
            self.label_8.setText(ele[2])
            self.label_9.setText(numero)
            arreglo64=arreglo[1]
            num2="".join(arreglo64)
            elem = num2.split(' ')
            self.label_10.setText(entrada)
            self.label_11.setText(elem[0])
            self.label_12.setText(elem[1])
            self.label_13.setText(elem[2])
            self.label_14.setText(numero)
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    def event32Aotras(self,entrada):
        try:
                usar=iee.ieeeInverso('32',entrada)
                arreglo = iee.ieee(float(usar))
                arreglo32 = arreglo[0]
                numero = "".join(arreglo32)
                ele = numero.split(' ')
                self.label_5.setText(str(usar))
                self.label_6.setText(ele[0])
                self.label_7.setText(ele[1])
                self.label_8.setText(ele[2])
                self.label_9.setText(numero)
                arreglo64 = arreglo[1]
                num2 = "".join(arreglo64)
                elem = num2.split(' ')
                self.label_10.setText(str(usar))
                self.label_11.setText(elem[0])
                self.label_12.setText(elem[1])
                self.label_13.setText(elem[2])
                self.label_14.setText(numero)
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    def event64Aotras(self,entrada):
        try:
                usar=iee.ieeeInverso('64',entrada)
                arreglo = iee.ieee(float(usar))
                arreglo32 = arreglo[0]
                numero = "".join(arreglo32)
                ele = numero.split(' ')
                self.label_5.setText(str(usar))
                self.label_6.setText(ele[0])
                self.label_7.setText(ele[1])
                self.label_8.setText(ele[2])
                self.label_9.setText(numero)
                arreglo64 = arreglo[1]
                num2 = "".join(arreglo64)
                elem = num2.split(' ')
                self.label_10.setText(str(usar))
                self.label_11.setText(elem[0])
                self.label_12.setText(elem[1])
                self.label_13.setText(elem[2])
                self.label_14.setText(numero)
        except:
            print('--no se puede borrar mas')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    def eventBotonCalcular(self):
        if self.estadoNum == "Decimal":
            aux = self.label.text()
            self.eventDecimalAotras(aux)
        elif self.estadoNum == "32bits" or self.estadoNum == "64Bits":
            estado=self.validarNumero()
            if estado == True:
                if self.estadoNum == "32bits":
                    self.event32Aotras(self.label.text())
                    print('es 32')
                elif self.estadoNum == "64Bits":
                    print('es 64')
                    self.event64Aotras(self.label.text())
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Revisa los datos ingresados")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()
    def estadoDecimal(self):
        self.estadoNum = "Decimal"
    def estado32(self):
        self.estadoNum="32bits"
    def estado64(self):
        self.estadoNum="64Bits"
    def validarNumero(self):
        numero = self.label.text()
        valido = True
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
        return valido
    def eventoBorrarTotal(self):
            try:
                self.entrada = self.label.text()
                tamaño = len(self.entrada)
                self.label.setText(self.entrada[:tamaño - tamaño])
            except:
                print('--no se puede borrar mas')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Revisa los datos ingresados")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()

    def eventoBorrar(self):
            self.entrada = self.label.text()
            self.label.setText(self.entrada[:len(self.entrada) - 1])
        #creaciondelos botones
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CalculadoraIEEE"))
        self.BotonNum.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Numero a Convertir:</span></p></body></html>"))
        self.botonDecimal.setText(_translate("Form", "Decimal"))
        """ self.Borrar_3.setText(_translate("Form", "32 bits "))
        self.Borrar_4.setText(_translate("Form", "64 bits"))"""
        self.BotonNum_2.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Numero:</span></p></body></html>"))
        self.BotonSig1.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Signo:</span></p></body></html>"))
        self.BotonExpo.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Exponente:</span></p></body></html>"))
        self.BotonSigni.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Significativo:</span></p></body></html>"))
        self.BotonValCom.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Valor completo:</span></p></body></html>"))
        self.BotonNum2.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                  "p, li { white-space: pre-wrap; }\n"
                                                  "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Numero:</span></p></body></html>"))
        self.BotonSigni2.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Significativo:</span></p></body></html>"))
        self.BotonExpon.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Exponente:</span></p></body></html>"))
        self.BotonValor.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Valor completo:</span></p></body></html>"))
        self.BotonSig.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Signo:</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "32 Bits"))
        self.label_3.setText(_translate("Form", "64 Bits"))
        self.botonUno.setText(_translate("Form", "1"))
        self.botonUno.setShortcut(_translate("Form", "1"))
        self.botonDos.setText(_translate("Form", "2"))
        self.botonDos.setShortcut(_translate("Form", "2"))
        self.botonMenos.setText(_translate("Form", "AC"))
        self.botonMenos.setShortcut(_translate("Form", "-"))
        self.botonOcho.setText(_translate("Form", "8"))
        self.botonOcho.setShortcut(_translate("Form", "8"))
        self.botonSeis.setText(_translate("Form", "6"))
        self.botonSeis.setShortcut(_translate("Form", "6"))
        self.botonNueve.setText(_translate("Form", "9"))
        self.botonNueve.setShortcut(_translate("Form", "9"))
        self.botonSiete.setText(_translate("Form", "7"))
        self.botonSiete.setShortcut(_translate("Form", "7"))
        self.botonTres.setText(_translate("Form", "3"))
        self.botonTres.setShortcut(_translate("Form", "3"))
        self.botonCuatro.setText(_translate("Form", "4"))
        self.botonCuatro.setShortcut(_translate("Form", "4"))
        self.botonCinco.setText(_translate("Form", "5"))
        self.botonCinco.setShortcut(_translate("Form", "5"))
        self.botonCero_2.setText(_translate("Form", "0"))
        self.botonCero_2.setShortcut(_translate("Form", "0"))
        self.botonPunto.setShortcut(_translate("Form", "."))
        self.botonCero.setText(_translate("Form", "<--"))
        self.botonCero.setShortcut(_translate("Form", "0"))
        self.Borrar.setText(_translate("Form", "Borrar"))
        self.Salir.setText(_translate("Form", "Salir"))
        self.Salir_2.setText(_translate("Form", "Grafica"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

