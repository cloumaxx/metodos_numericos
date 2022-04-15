# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'polinomios.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from funciones import calcPolinomiosRaices as calP
from interfazcalculadoras import ScrollLabel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(744, 590)
        Form.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.BotonValor = QtWidgets.QTextEdit(Form)
        self.BotonValor.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.BotonValor.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(170, 170, 255);")
        self.BotonValor.setObjectName("BotonValor")
        self.BotonValorCu = QtWidgets.QTextEdit(Form)
        self.BotonValorCu.setGeometry(QtCore.QRect(20, 70, 181, 31))
        self.BotonValorCu.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "background-color: rgb(170, 170, 255);")
        self.BotonValorCu.setObjectName("BotonValorCu")
        self.BotonValorLi = QtWidgets.QTextEdit(Form)
        self.BotonValorLi.setGeometry(QtCore.QRect(20, 120, 181, 31))
        self.BotonValorLi.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "background-color: rgb(170, 170, 255);")
        self.BotonValorLi.setObjectName("BotonValorLi")
        self.BotonValorIn = QtWidgets.QTextEdit(Form)
        self.BotonValorIn.setGeometry(QtCore.QRect(20, 170, 181, 31))
        self.BotonValorIn.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "background-color: rgb(170, 170, 255);")
        self.BotonValorIn.setObjectName("BotonValorIn")
        self.x3 = QtWidgets.QTextEdit(Form)
        self.x3.setGeometry(QtCore.QRect(490, 20, 61, 31))
        self.x3.setStyleSheet("font: 12pt \"Arial\";\n"
                              "\n"
                              "background-color: rgb(101, 255, 175);")
        self.x3.setObjectName("x3")
        self.x2 = QtWidgets.QTextEdit(Form)
        self.x2.setGeometry(QtCore.QRect(490, 70, 61, 31))
        self.x2.setStyleSheet("font: 12pt \"Arial\";\n"
                              "\n"
                              "background-color: rgb(101, 255, 175);")
        self.x2.setObjectName("x2")
        self.x = QtWidgets.QTextEdit(Form)
        self.x.setGeometry(QtCore.QRect(490, 120, 61, 31))
        self.x.setStyleSheet("font: 12pt \"Arial\";\n"
                             "\n"
                             "background-color: rgb(101, 255, 175);")
        self.x.setObjectName("x")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 220, 565, 203))
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
        self.botonDos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDos.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                    "font: 87 14pt \"Arial Black\";")
        self.botonDos.setObjectName("botonDos")
        self.gridLayout.addWidget(self.botonDos, 0, 1, 1, 1)
        self.botonTres = QtWidgets.QPushButton(self.layoutWidget)
        self.botonTres.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonTres.setObjectName("botonTres")
        self.gridLayout.addWidget(self.botonTres, 0, 2, 1, 1)
        self.botonCuatro = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCuatro.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.botonCuatro.setObjectName("botonCuatro")
        self.gridLayout.addWidget(self.botonCuatro, 1, 0, 1, 1)
        self.botonCinco = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCinco.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonCinco.setObjectName("botonCinco")
        self.gridLayout.addWidget(self.botonCinco, 1, 1, 1, 1)
        self.botonSeis = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSeis.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonSeis.setObjectName("botonSeis")
        self.gridLayout.addWidget(self.botonSeis, 1, 2, 1, 1)
        self.botonSiete = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSiete.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonSiete.setObjectName("botonSiete")
        self.gridLayout.addWidget(self.botonSiete, 2, 0, 1, 1)
        self.botonOcho = QtWidgets.QPushButton(self.layoutWidget)
        self.botonOcho.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonOcho.setObjectName("botonOcho")
        self.gridLayout.addWidget(self.botonOcho, 2, 1, 1, 1)
        self.botonNueve = QtWidgets.QPushButton(self.layoutWidget)
        self.botonNueve.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonNueve.setObjectName("botonNueve")
        self.gridLayout.addWidget(self.botonNueve, 2, 2, 1, 1)
        self.botonCabierto = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonCabierto.setObjectName("botonCabierto")
        self.gridLayout.addWidget(self.botonCabierto, 3, 0, 1, 1)
        self.botonCero = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
                                     "font: 87 14pt \"Arial Black\";")
        self.botonCero.setObjectName("botonCero")
        self.gridLayout.addWidget(self.botonCero, 3, 1, 1, 1)
        self.botonCerrado = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCerrado.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                        "font: 87 14pt \"Arial Black\";")
        self.botonCerrado.setObjectName("botonCerrado")
        self.gridLayout.addWidget(self.botonCerrado, 3, 2, 1, 1)
        self.botonCabierto_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonCabierto_2.setObjectName("botonCabierto_2")
        self.gridLayout.addWidget(self.botonCabierto_2, 4, 0, 1, 1)
        self.botonPunto = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPunto.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.botonPunto.setObjectName("botonPunto")
        self.gridLayout.addWidget(self.botonPunto, 4, 1, 1, 1)
        self.botonCabierto_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_3.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonCabierto_3.setObjectName("botonCabierto_3")
        self.gridLayout.addWidget(self.botonCabierto_3, 4, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 5, 1)
        self.botonMas = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                    "background-color: rgb(0, 170, 127);")
        self.botonMas.setObjectName("botonMas")
        self.gridLayout_2.addWidget(self.botonMas, 0, 1, 1, 1)
        self.botonMas_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_2.setObjectName("botonMas_2")
        self.gridLayout_2.addWidget(self.botonMas_2, 0, 2, 1, 1)
        self.botonMas_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_3.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_3.setObjectName("botonMas_3")
        self.gridLayout_2.addWidget(self.botonMas_3, 0, 3, 1, 1)
        self.botonMas_11 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_11.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_11.setObjectName("botonMas_11")
        self.gridLayout_2.addWidget(self.botonMas_11, 0, 4, 1, 1)
        self.botonMenos = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMenos.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMenos.setObjectName("botonMenos")
        self.gridLayout_2.addWidget(self.botonMenos, 1, 1, 1, 1)
        self.botonMas_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_4.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_4.setObjectName("botonMas_4")
        self.gridLayout_2.addWidget(self.botonMas_4, 1, 2, 1, 1)
        self.botonMas_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_8.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_8.setObjectName("botonMas_8")
        self.gridLayout_2.addWidget(self.botonMas_8, 1, 3, 1, 1)
        self.botonMas_12 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_12.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_12.setObjectName("botonMas_12")
        self.gridLayout_2.addWidget(self.botonMas_12, 1, 4, 1, 1)
        self.BotonMulti = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonMulti.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                      "font: 87 14pt \"Arial Black\";")
        self.BotonMulti.setObjectName("BotonMulti")
        self.gridLayout_2.addWidget(self.BotonMulti, 2, 1, 1, 1)
        self.botonMas_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_7.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_7.setObjectName("botonMas_7")
        self.gridLayout_2.addWidget(self.botonMas_7, 2, 2, 1, 1)
        self.botonMas_9 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_9.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_9.setObjectName("botonMas_9")
        self.gridLayout_2.addWidget(self.botonMas_9, 2, 3, 1, 1)
        self.botonMas_13 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_13.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_13.setObjectName("botonMas_13")
        self.gridLayout_2.addWidget(self.botonMas_13, 2, 4, 1, 1)
        self.botonDivision = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDivision.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                         "background-color: rgb(0, 170, 127);")
        self.botonDivision.setObjectName("botonDivision")
        self.gridLayout_2.addWidget(self.botonDivision, 3, 1, 1, 1)

        self.botonMas_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_5.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_5.setObjectName("botonMas_5")
        self.gridLayout_2.addWidget(self.botonMas_5, 3, 2, 1, 1)
        self.botonMas_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_10.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_10.setObjectName("botonMas_10")
        self.gridLayout_2.addWidget(self.botonMas_10, 3, 3, 1, 1)
        self.botonMas_14 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_14.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "background-color: rgb(0, 170, 127);")
        self.botonMas_14.setObjectName("botonMas_14")
        self.gridLayout_2.addWidget(self.botonMas_14, 3, 4, 1, 1)
        self.botonPorcentaje = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPorcentaje.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                           "background-color: rgb(0, 170, 127);")
        self.botonPorcentaje.setObjectName("botonPorcentaje")
        self.gridLayout_2.addWidget(self.botonPorcentaje, 4, 1, 1, 1)
        self.botonMas_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_6.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                      "background-color: rgb(0, 170, 127);")
        self.botonMas_6.setObjectName("botonMas_6")
        self.gridLayout_2.addWidget(self.botonMas_6, 4, 2, 1, 1)
        self.BotonBorrar = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonBorrar.setStyleSheet("background-color: rgb(0, 170, 127);\n"
                                       "font: 87 14pt \"Arial Black\";")
        self.BotonBorrar.setObjectName("BotonBorrar")
        self.gridLayout_2.addWidget(self.BotonBorrar, 4, 3, 1, 1)
        self.botonAC = QtWidgets.QPushButton(self.layoutWidget)
        self.botonAC.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
                                   "background-color: rgb(0, 170, 127);")
        self.botonAC.setObjectName("botonAC")
        self.gridLayout_2.addWidget(self.botonAC, 4, 4, 1, 1)
        self.Raices = QtWidgets.QTextEdit(Form)
        self.Raices.setGeometry(QtCore.QRect(20, 450, 181, 31))
        self.Raices.setStyleSheet("font: 12pt \"Arial\";\n"
                                  "background-color: rgb(170, 170, 255);")
        self.Raices.setObjectName("Raices")
        #self.pushButton_11 = QtWidgets.QPushButton(Form)
        #self.pushButton_11.setGeometry(QtCore.QRect(600, 380, 91, 41))
        #self.pushButton_11.setStyleSheet("background-color: rgb(225, 225, 225);\n"
        #                                 "font: 87 12pt \"Arial Black\";")

        #self.pushButton_11.setObjectName("pushButton_11")

        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(600, 230, 91, 41))
        self.pushButton_12.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 87 12pt \"Arial Black\";")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.eventoCalcular)# esta linea dice que cunado se haga click en un boton, va hacer lo que diga la funcion "eventoCalcular"
        self.label = QtWidgets.QLineEdit(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 251, 31))
        self.label.setObjectName("label")
        self.label.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_2 = QtWidgets.QLineEdit(Form)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 251, 31))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_3 = QtWidgets.QLineEdit(Form)
        self.label_3.setGeometry(QtCore.QRect(220, 120, 251, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_4 = QtWidgets.QLineEdit(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 170, 251, 31))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-radius: 25px;border: 1px solid black;")

        self.label_5 = ScrollLabel.ScrollLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(220, 450, 400, 100))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def eventoCalcular(self):
        try:
            self.valorAlCubo = self.label.text()
            self.valorAlCuadrado = self.label_2.text()
            self.valorLineal = self.label_3.text()
            self.valorIdependitente = self.label_4.text()
            raiz = calP.returnRaices(self.valorAlCubo,self.valorAlCuadrado,self.valorLineal,self.valorIdependitente )
            #entrada=str(raiz)
            #raices = " ".join(raiz)
            msj=""
            print('...>>>',msj)
            for i in range(0,len(raiz)):
                usar = str(raiz[i])
                usar = usar.replace('j','i')
                usar = usar.replace('(','')
                usar = usar.replace(')', '')
                msj+=str(i+1)+") "+str(usar)+"\n"
            self.label_5.setText(msj)

        except:

            print('ocurrio un error')
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Revisa los datos ingresados")
            msg.setWindowTitle("Error")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "polinomios"))
        self.BotonValor.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ingresa el valor de X:</p></body></html>"))
        self.BotonValorCu.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Valor cuadratico:</p></body></html>"))
        self.BotonValorLi.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Valor lineal:</p></body></html>"))
        self.BotonValorIn.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                     "p, li { white-space: pre-wrap; }\n"
                                                     "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Valor independiente:</p></body></html>"))
        self.x3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X<span style=\" vertical-align:super;\">3</span></p></body></html>"))
        self.x2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X<span style=\" vertical-align:super;\">2</span></p></body></html>"))
        self.x.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">X</p></body></html>"))
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
        self.botonCabierto.setShortcut(_translate("Form", "("))
        self.botonCero.setText(_translate("Form", "0"))
        self.botonCero.setShortcut(_translate("Form", "0"))
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
        self.botonMas_2.setText(_translate("Form", "√"))
        self.botonMas_2.setShortcut(_translate("Form", "+"))
        self.botonMas_3.setText(_translate("Form", "exp"))
        self.botonMas_3.setShortcut(_translate("Form", "+"))
        self.botonMas_11.setText(_translate("Form", "tan"))
        self.botonMas_11.setShortcut(_translate("Form", "+"))
        self.botonMenos.setText(_translate("Form", "-"))
        self.botonMenos.setShortcut(_translate("Form", "-"))
        self.botonMas_4.setText(_translate("Form", "^"))
        self.botonMas_4.setShortcut(_translate("Form", "+"))
        self.botonMas_8.setText(_translate("Form", "log"))
        self.botonMas_8.setShortcut(_translate("Form", "+"))
        self.botonMas_12.setText(_translate("Form", "sec"))
        self.botonMas_12.setShortcut(_translate("Form", "+"))
        self.BotonMulti.setText(_translate("Form", "x"))
        self.BotonMulti.setShortcut(_translate("Form", "*"))
        self.botonMas_7.setText(_translate("Form", "π"))
        self.botonMas_7.setShortcut(_translate("Form", "+"))
        self.botonMas_9.setText(_translate("Form", "sin"))
        self.botonMas_9.setShortcut(_translate("Form", "+"))
        self.botonMas_13.setText(_translate("Form", "csc"))
        self.botonMas_13.setShortcut(_translate("Form", "+"))
        self.botonDivision.setText(_translate("Form", "÷"))
        self.botonDivision.setShortcut(_translate("Form", "/"))
        self.botonMas_5.setText(_translate("Form", "ln"))
        self.botonMas_5.setShortcut(_translate("Form", "+"))
        self.botonMas_10.setText(_translate("Form", "cos"))
        self.botonMas_10.setShortcut(_translate("Form", "+"))
        self.botonMas_14.setText(_translate("Form", "cot"))
        self.botonMas_14.setShortcut(_translate("Form", "+"))
        self.botonPorcentaje.setText(_translate("Form", "%"))
        self.botonPorcentaje.setShortcut(_translate("Form", "%"))
        self.botonMas_6.setText(_translate("Form", "="))
        self.botonMas_6.setShortcut(_translate("Form", "+"))
        self.BotonBorrar.setText(_translate("Form", "C"))
        self.BotonBorrar.setShortcut(_translate("Form", "Esc"))
        self.botonAC.setText(_translate("Form", "AC"))
        self.Raices.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
                                               "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Raices:</p></body></html>"))
        #self.pushButton_11.setText(_translate("Form", "Salir"))
        self.pushButton_12.setText(_translate("Form", "Calcular"))
        self.label.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "0"))
        self.label_4.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

