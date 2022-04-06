# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interfazcalculadoras import ConversorEntreBases as cEb, Derivadas as der, IEEE as ieee, MetodoBiseccion as mBee, \
    MetodoNewon, MetodoReglaFalsa, metodoSecante, polinomios as mPoli,integracionporRectangulos as intRec,integracionporTrapecios as intTra,  Simpson1_3 as simp13,Simpson3_8 as simp38, Grafica  as grafica


class Ui_interfaz(object):
    def setupUi(self, interfaz):
        interfaz.setObjectName("interfaz")
        interfaz.resize(733, 700)
        interfaz.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.pushButton = QtWidgets.QPushButton(interfaz)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 141, 71))
        self.pushButton.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                      "font: 75 italic 12pt \"Arial Narrow\";")
        self.pushButton.setObjectName("pushButton")  # Boton a cambio bases
        self.pushButton.clicked.connect(self.cambioAbases)
        self.botonDerivadas = QtWidgets.QPushButton(interfaz)
        self.botonDerivadas.setGeometry(QtCore.QRect(50, 180, 141, 71))
        self.botonDerivadas.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonDerivadas.setObjectName("botonDerivadas")
        self.botonDerivadas.clicked.connect(self.cambioADerivadas)
        self.botonBiseccion = QtWidgets.QPushButton(interfaz)
        self.botonBiseccion.setGeometry(QtCore.QRect(50, 270, 141, 71))
        self.botonBiseccion.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonBiseccion.setObjectName("botonBiseccion")
        self.botonBiseccion.clicked.connect(self.cambioABiseccion)

        self.botonRegla = QtWidgets.QPushButton(interfaz)
        self.botonRegla.setGeometry(QtCore.QRect(210, 270, 141, 71))
        self.botonRegla.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                      "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonRegla.setObjectName("botonRegla")
        self.botonRegla.clicked.connect(self.cambioReglaFalsa)
        self.boronNewon = QtWidgets.QPushButton(interfaz)
        self.boronNewon.setGeometry(QtCore.QRect(40, 360, 161, 71))
        self.boronNewon.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                      "font: 75 italic 12pt \"Arial Narrow\";")
        self.boronNewon.setObjectName("boronNewon")
        self.boronNewon.clicked.connect(self.cambioANewon)

        self.botonSecante = QtWidgets.QPushButton(interfaz)
        self.botonSecante.setGeometry(QtCore.QRect(210, 360, 141, 71))
        self.botonSecante.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                        "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonSecante.setObjectName("botonSecante")
        self.botonSecante.clicked.connect(self.cambioSecante)
        self.MenuPrin = QtWidgets.QTextEdit(interfaz)
        self.MenuPrin.setGeometry(QtCore.QRect(50, 30, 311, 41))
        self.MenuPrin.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.MenuPrin.setObjectName("MenuPrin")
        self.Integrantes = QtWidgets.QTextEdit(interfaz)
        self.Integrantes.setGeometry(QtCore.QRect(380, 90, 311, 271))
        self.Integrantes.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Integrantes.setObjectName("Integrantes")

        self.botonIeee = QtWidgets.QPushButton(interfaz)
        self.botonIeee.setGeometry(QtCore.QRect(210, 90, 141, 71))
        self.botonIeee.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                     "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonIeee.setObjectName("botonIeee")
        self.botonIeee.clicked.connect(self.cambioAiee)

        self.botonPolinomio = QtWidgets.QPushButton(interfaz)
        self.botonPolinomio.setGeometry(QtCore.QRect(210, 180, 141, 71))
        self.botonPolinomio.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                          "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonPolinomio.setObjectName("botonPolinomio")
        self.botonPolinomio.clicked.connect(self.cambioPolinomio)

        self.botonInterRec = QtWidgets.QPushButton(interfaz)
        self.botonInterRec.setGeometry(QtCore.QRect(210, 450, 141, 71))
        self.botonInterRec.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                     "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonInterRec.setObjectName("botonIeee")
        self.botonInterRec.clicked.connect(self.cambioRectangulos)

        self.botonInterTrape = QtWidgets.QPushButton(interfaz)
        self.botonInterTrape.setGeometry(QtCore.QRect(50, 450, 141, 71))
        self.botonInterTrape.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonInterTrape.setObjectName("botonTrapecio")
        self.botonInterTrape.clicked.connect(self.cambioATrapecios)

        self.botonInterSimson13 = QtWidgets.QPushButton(interfaz)
        self.botonInterSimson13.setGeometry(QtCore.QRect(50, 540, 141, 71))
        self.botonInterSimson13.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonInterSimson13.setObjectName("botonSimpson13")
        self.botonInterSimson13.clicked.connect(self.cambioSimpson13)

        self.botonInterSimson38 = QtWidgets.QPushButton(interfaz)
        self.botonInterSimson38.setGeometry(QtCore.QRect(210, 540, 141, 71))
        self.botonInterSimson38.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                              "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonInterSimson38.setObjectName("botonSimpson38")
        self.botonInterSimson38.clicked.connect(self.cambioSimpson38)

        self.botonGraficadora = QtWidgets.QPushButton(interfaz)
        self.botonGraficadora.setGeometry(QtCore.QRect(380, 380, 141, 71))
        self.botonGraficadora.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonGraficadora.setObjectName("botonGraficadora")
        self.botonGraficadora.clicked.connect(self.cambioAGrafica)
        self.retranslateUi(interfaz)
        QtCore.QMetaObject.connectSlotsByName(interfaz)

    def cambioAbases(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = cEb.Ui_ConversorEntreBases()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioSimpson13(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = simp13.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioSimpson38(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = simp38.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioAGrafica(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = grafica.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioRectangulos(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = intRec.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioATrapecios(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = intTra.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def cambioADerivadas(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = der.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()


    def cambioAiee(self):
            self.interfaz = QtWidgets.QWidget()
            self.ui = ieee.Ui_Form()
            self.ui.setupUi(self.interfaz)
            self.interfaz.show()

    def cambioABiseccion(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = mBee.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def cambioANewon(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = MetodoNewon.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def cambioReglaFalsa(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = MetodoReglaFalsa.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def cambioSecante(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = metodoSecante.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def cambioPolinomio(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui = mPoli.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()

    def retranslateUi(self, interfaz):
        _translate = QtCore.QCoreApplication.translate
        interfaz.setWindowTitle(_translate("interfaz", "menu principal"))
        self.pushButton.setText(_translate("interfaz", "Convertir entre Bases"))
        self.botonDerivadas.setText(_translate("interfaz", "Calcular Derivadas"))
        self.botonBiseccion.setText(_translate("interfaz", " Metodo de Bisección"))
        self.botonRegla.setText(_translate("interfaz", "Metodo Regla Falsa"))
        self.boronNewon.setText(_translate("interfaz", "Metodo Newton Raphson"))
        self.botonSecante.setText(_translate("interfaz", "Metodo de la Secante"))
        self.botonInterRec.setText(_translate("interfaz", "Integracion por Rectangulos"))
        self.botonInterTrape.setText(_translate("interfaz", "Integracion por Trapecios"))
        self.botonGraficadora.setText(_translate("interfaz", "Graficador"))
        self.botonInterSimson13.setText(_translate("interfaz", "Simpson 1/3"))
        self.botonInterSimson38.setText(_translate("interfaz", "Simpson 3/8"))
        self.MenuPrin.setHtml(_translate("interfaz",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Menu Principal</span></p></body></html>"))
        self.Integrantes.setHtml(_translate("interfaz",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">Integrantes</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">-- Carlos Alvear</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Daniela Guevara</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Cristhian Soto</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Juan Pablo Sanchez</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Julian Andres Castaño</span></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Ashly Fernanda Hoyos</span></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'open sans\'; font-size:8pt; font-weight:600; color:#ffffff;\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'open sans\'; font-size:8pt; font-weight:600; color:#ffffff;\"><br /></p></body></html>"))
        self.botonIeee.setText(_translate("interfaz", "Calculadora IEEE"))
        self.botonPolinomio.setText(_translate("interfaz", "Polinomios"))


def control():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    interfaz = QtWidgets.QWidget()
    ui = Ui_interfaz()
    ui.setupUi(interfaz)
    interfaz.show()
    sys.exit(app.exec_())

#control()
