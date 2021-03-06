# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuPrincipal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap

from interfazcalculadoras import ConversorEntreBases as cEb, Derivadas as der, IEEE as ieee, MetodoBiseccion as mBee, \
    MetodoNewon, MetodoReglaFalsa, metodoSecante, polinomios as mPoli,integracionporRectangulos as intRec,integracionporTrapecios as intTra, \
    Simpson1_3 as simp13,Simpson3_8 as simp38, Grafica  as grafica,Metodo_Montecarlo as Met_Mon,Matrices, \
    ajusteMinimosCuadrados_ui as ajuste
import os, sys
def resolver_ruta(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

class Ui_interfaz(object):
    def setupUi(self, interfaz): # el nombre del dominio de esta pantalla es "interfaz"
        interfaz.setObjectName("interfaz")
        interfaz.resize(1350, 680)
        interfaz.setStyleSheet("background-color: rgb(250, 250, 250);")
        interfaz.setWindowIcon(QtGui.QIcon(resolver_ruta('imagenes/icono.png')))#se copia y pega esta linea en todas  las interfaces
                                                                # pero le cambias el inicio segun corresponda
        self.imagenFondo= QtWidgets.QLabel(interfaz)
        nombreArch = resolver_ruta("imagenes/fondo1.png")
        pixmap = QPixmap(nombreArch)
        self.imagenFondo.setPixmap(pixmap)
        self.imagenFondo.setGeometry(0, 0, 270, 120)
        self.imagenFondo.resize(pixmap.width(), pixmap.height())

        self.imagenUsar = QtWidgets.QLabel(interfaz)
        pixmap2 = QPixmap(resolver_ruta('imagenes/escudoEmpr.png'))
        #pixi = QtGui.QPixmap.fromImage(image).scaledToWidth(150)
        #self.label.setPixmap(pixi)
        self.imagenUsar.setPixmap(pixmap2)
        self.imagenUsar.setStyleSheet("border-image : url(magenes/escudoEmpr.png);")
        self.imagenUsar.setGeometry(0, 0, 0, 0)
        # Opcional, redimensionar la ventana al tama??o de la imagen
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
        self.MenuPrin = QtWidgets.QLabel(interfaz)
        self.MenuPrin.setGeometry(QtCore.QRect(50, 30, 311, 41))
        self.MenuPrin.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.MenuPrin.setObjectName("MenuPrin")
        self.Integrantes = QtWidgets.QLabel(interfaz)
        self.Integrantes.setGeometry(QtCore.QRect(380, 150, 200, 200))
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

        self.botonMonteCarlo = QtWidgets.QPushButton(interfaz)
        self.botonMonteCarlo.setGeometry(QtCore.QRect(380, 470, 141, 71))
        self.botonMonteCarlo.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                            "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonMonteCarlo.setText("Monte Carlo")
        self.botonMonteCarlo.setObjectName("botonMonteCarlo")
        self.botonMonteCarlo.clicked.connect(self.cambioMonteCarlo)

        self.botonMatriz = QtWidgets.QPushButton(interfaz)
        self.botonMatriz.setGeometry(QtCore.QRect(380, 550, 141, 71))
        self.botonMatriz.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                           "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonMatriz.setText("Matrices")
        self.botonMatriz.setObjectName("botonMatriz")
        self.botonMatriz.clicked.connect(self.cambioMatrices)

        self.botonCurvas = QtWidgets.QPushButton(interfaz)
        self.botonCurvas.setGeometry(QtCore.QRect(550, 380, 141, 71))
        self.botonCurvas.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                       "font: 75 italic 12pt \"Arial Narrow\";")
        self.botonCurvas.setText("Ajuste Curvas")
        self.botonCurvas.setObjectName("botonMatriz")
        self.botonCurvas.clicked.connect(self.cambioCurvas)

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

    def cambioMonteCarlo(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui =Met_Mon.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioMatrices(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui =Matrices.Ui_Form()
        self.ui.setupUi(self.interfaz)
        self.interfaz.show()
    def cambioCurvas(self):
        self.interfaz = QtWidgets.QWidget()
        self.ui =ajuste.Ui_Form()
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
        self.botonBiseccion.setText(_translate("interfaz", " Metodo de Bisecci??n"))
        self.botonRegla.setText(_translate("interfaz", "Metodo Regla Falsa"))
        self.boronNewon.setText(_translate("interfaz", "Metodo Newton Raphson"))
        self.botonSecante.setText(_translate("interfaz", "Metodo de la Secante"))
        self.botonInterRec.setText(_translate("interfaz", "Integracion por\n Rectangulos"))
        self.botonInterTrape.setText(_translate("interfaz", "Integracion por\n Trapecios"))
        self.botonGraficadora.setText(_translate("interfaz", "Graficador"))
        self.botonInterSimson13.setText(_translate("interfaz", "Simpson 1/3"))
        self.botonInterSimson38.setText(_translate("interfaz", "Simpson 3/8"))
        self.MenuPrin.setText(_translate("interfaz",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Menu Principal</span></p></body></html>"))
        self.Integrantes.setText(_translate("interfaz",
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
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">--Julian Andres Casta??o</span></p>\n"
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
