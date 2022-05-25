# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajusteMinimosCuadrados.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from  interfazcalculadoras import ScrollLabel
from funciones import calcArregloCurvas as curvas
import os, sys
def resolver_ruta(ruta_relativa):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)

class Ui_Form(object):
    coordenadaX = []
    coordenadaY = []
    contador = 0
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 900)
        Form.setStyleSheet("background-color: rgb(250, 250, 250);")
        Form.setWindowIcon(
            QtGui.QIcon(resolver_ruta('imagenes/icono.png')))  # se copia y pega esta linea en todas  las interfaces
        self.imagenFondo = QtWidgets.QLabel(Form)
        pixmap = QPixmap(resolver_ruta('imagenes/fondo1.png'))
        self.imagenFondo.setPixmap(pixmap)
        self.imagenFondo.setGeometry(0, 0, 270, 120)
        self.imagenFondo.resize(pixmap.width(), pixmap.height())
        self.label = QtWidgets.QLineEdit(Form)
        self.label.setGeometry(QtCore.QRect(200, 20, 290, 31))
        self.label.setObjectName("label")
        self.labelTexto = QtWidgets.QLabel(Form)
        self.labelTexto.setGeometry(QtCore.QRect(15, 69, 170, 31))
        self.labelTexto.setObjectName("labelTexto")
        self.labelTexto.setText("  Ingresa la coordenada a grafica: ")
        self.labelTexto.setStyleSheet("background-color: rgb(170, 170, 255)")
        self.labelTextoParentesis = QtWidgets.QLabel(Form)
        self.labelTextoParentesis.setGeometry(QtCore.QRect(190, 69, 10, 31))
        self.labelTextoParentesis.setObjectName("labelTextoParentesis")
        self.labelTextoParentesis.setStyleSheet("background-color: rgb(31, 195, 153);\n")
        self.labelTextoParentesis.setText(" ( ")

        self.textinput1 = QtWidgets.QLineEdit(Form)
        self.textinput1.setGeometry(QtCore.QRect(205, 69, 51, 31))
        self.textinput1.setObjectName("textinput")
        self.textinput1.setText('0')

        self.labelTextoComa = QtWidgets.QLabel(Form)
        self.labelTextoComa.setGeometry(QtCore.QRect(260, 69, 10, 31))
        self.labelTextoComa.setObjectName("labelTextoComa")
        self.labelTextoComa.setStyleSheet("background-color: rgb(31, 195, 153);\n")
        self.labelTextoComa.setText(" , ")

        self.labelTextoParentesis2 = QtWidgets.QLabel(Form)
        self.labelTextoParentesis2.setGeometry(QtCore.QRect(335, 69, 10, 31))
        self.labelTextoParentesis2.setObjectName("labelTextoParentesis")
        self.labelTextoParentesis2.setStyleSheet("background-color: rgb(31, 195, 153);\n")
        self.labelTextoParentesis2.setText(" ) ")

        self.textinput2 = QtWidgets.QLineEdit(Form)
        self.textinput2.setGeometry(QtCore.QRect(275, 69, 51, 31))
        self.textinput2.setObjectName("textinput")
        self.textinput2.setText('0')

        self.botonAgregarCoordenada = QtWidgets.QPushButton(Form)
        self.botonAgregarCoordenada.setGeometry(QtCore.QRect(350, 69, 100, 31))
        self.botonAgregarCoordenada.setObjectName("botonAgregarCoordenada")
        self.botonAgregarCoordenada.setText("Agregar")
        self.botonAgregarCoordenada.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                         "font: 87 12pt \"Arial Black\";")
        self.botonAgregarCoordenada.clicked.connect(self.agregarPunto)

        self.botonGrafica = QtWidgets.QPushButton(Form)
        self.botonGrafica.setGeometry(QtCore.QRect(370, 265, 100, 31))
        self.botonGrafica.setObjectName("botonAgregarCoordenada")
        self.botonGrafica.setText("Grafica")
        self.botonGrafica.setStyleSheet("background-color: rgb(225, 225, 225);\n"
                                                  "font: 87 12pt \"Arial Black\";")
        self.botonGrafica.clicked.connect(self.grafica)

        self.mostrarPosPuntos = ScrollLabel.ScrollLabel(Form)
        self.mostrarPosPuntos.setGeometry(QtCore.QRect(15, 110, 400, 45))
        self.mostrarPosPuntos.setObjectName("textinputPos")
        self.mostrarPosPuntos.setStyleSheet("font: 35 12pt \"Arial Black\";")
        self.mostrarPosPuntos.setText("Pos|")

        self.mostrarPuntosX = ScrollLabel.ScrollLabel(Form)
        self.mostrarPuntosX.setGeometry(QtCore.QRect(15, 150, 400, 50))
        self.mostrarPuntosX.setObjectName("textinputX")
        self.mostrarPuntosX.setStyleSheet("font: 40 12pt \"Arial Black\";")
        self.mostrarPuntosX.setText(" X   |")
        self.mostrarPuntosY = ScrollLabel.ScrollLabel(Form)
        self.mostrarPuntosY.setGeometry(QtCore.QRect(15, 200, 400, 50))
        self.mostrarPuntosY.setObjectName("textinputY")
        self.mostrarPuntosY.setStyleSheet("font: 40 12pt \"Arial Black\";")
        self.mostrarPuntosY.setText(" Y  |")

        self.botoncalcular = QtWidgets.QPushButton(Form)
        self.botoncalcular.setGeometry(QtCore.QRect(60, 265, 111, 31))
        self.botoncalcular.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 87 12pt \"Arial Black\";")
        self.botoncalcular.setObjectName("botoncalcular")
        self.botoncalcular.clicked.connect(self.calcular)
        self.botonActualizar = QtWidgets.QPushButton(Form)
        self.botonActualizar.setGeometry(QtCore.QRect(200, 265, 150, 31))
        self.botonActualizar.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 87 12pt \"Arial Black\";")
        self.botonActualizar.setObjectName("botonActualizar")


        self.textejemplo = QtWidgets.QLabel(Form)
        self.textejemplo.setGeometry(QtCore.QRect(20, 300, 481, 41))
        self.textejemplo.setObjectName("textejemplo")
        self.textejemplo.setStyleSheet("background-color: rgb(31, 195, 153);\n")
        self.gradounoedit = QtWidgets.QLineEdit(Form)
        self.gradounoedit.setGeometry(QtCore.QRect(130, 350, 261, 31))
        self.gradounoedit.setObjectName("gradounoedit")
        self.gradodosedit = QtWidgets.QLineEdit(Form)
        self.gradodosedit.setGeometry(QtCore.QRect(130, 400, 261, 31))
        self.gradodosedit.setObjectName("gradodosedit")
        self.gradotresedit = QtWidgets.QLineEdit(Form)
        self.gradotresedit.setGeometry(QtCore.QRect(130, 450, 261, 31))
        self.gradotresedit.setObjectName("gradotresedit")
        self.gradocuatroedit = QtWidgets.QLineEdit(Form)
        self.gradocuatroedit.setGeometry(QtCore.QRect(130, 500, 261, 31))
        self.gradocuatroedit.setObjectName("gradocuatroedit")
        self.gradocincoedit = QtWidgets.QLineEdit(Form)
        self.gradocincoedit.setGeometry(QtCore.QRect(130, 550, 261, 31))
        self.gradocincoedit.setObjectName("gradocincoedit")
        self.gradoseisedit = QtWidgets.QLineEdit(Form)
        self.gradoseisedit.setGeometry(QtCore.QRect(130, 600, 261, 31))
        self.gradoseisedit.setObjectName("gradoseisedit")
        self.CCunoedit = QtWidgets.QLineEdit(Form)
        self.CCunoedit.setGeometry(QtCore.QRect(480, 350, 151, 31))
        self.CCunoedit.setObjectName("CCunoedit")
        self.gradouno = QtWidgets.QLabel(Form)
        self.gradouno.setGeometry(QtCore.QRect(20, 350, 101, 31))
        self.gradouno.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradouno.setObjectName("gradouno")
        self.gradodos = QtWidgets.QLabel(Form)
        self.gradodos.setGeometry(QtCore.QRect(20, 400, 101, 31))
        self.gradodos.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradodos.setObjectName("gradodos")
        self.gradotres = QtWidgets.QLabel(Form)
        self.gradotres.setGeometry(QtCore.QRect(20, 450, 101, 31))
        self.gradotres.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradotres.setObjectName("gradotres")
        self.gradocuatro = QtWidgets.QLabel(Form)
        self.gradocuatro.setGeometry(QtCore.QRect(20, 500, 101, 31))
        self.gradocuatro.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradocuatro.setObjectName("gradocuatro")
        self.gradocinco = QtWidgets.QLabel(Form)
        self.gradocinco.setGeometry(QtCore.QRect(20, 550, 101, 31))
        self.gradocinco.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradocinco.setObjectName("gradocinco")
        self.gradoseis = QtWidgets.QLabel(Form)
        self.gradoseis.setGeometry(QtCore.QRect(20, 600, 101, 31))
        self.gradoseis.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.gradoseis.setObjectName("gradoseis")
        self.numpuntos = QtWidgets.QLabel(Form)
        self.numpuntos.setGeometry(QtCore.QRect(20, 20, 171, 31))
        self.numpuntos.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.numpuntos.setObjectName("numpuntos")
        self.CCuno = QtWidgets.QLabel(Form)
        self.CCuno.setGeometry(QtCore.QRect(420, 350, 51, 31))
        self.CCuno.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCuno.setObjectName("CCuno")
        self.CCdos = QtWidgets.QLabel(Form)
        self.CCdos.setGeometry(QtCore.QRect(420, 400, 51, 31))
        self.CCdos.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCdos.setObjectName("CCdos")
        self.CCtres = QtWidgets.QLabel(Form)
        self.CCtres.setGeometry(QtCore.QRect(420, 450, 51, 31))
        self.CCtres.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCtres.setObjectName("CCtres")
        self.CCcinco = QtWidgets.QLabel(Form)
        self.CCcinco.setGeometry(QtCore.QRect(420, 550, 51, 31))
        self.CCcinco.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCcinco.setObjectName("CCcinco")
        self.CCcuatro = QtWidgets.QLabel(Form)
        self.CCcuatro.setGeometry(QtCore.QRect(420, 500, 51, 31))
        self.CCcuatro.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCcuatro.setObjectName("CCcuatro")
        self.CCseis = QtWidgets.QLabel(Form)
        self.CCseis.setGeometry(QtCore.QRect(420, 600, 51, 31))
        self.CCseis.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(170, 170, 255);")
        self.CCseis.setObjectName("CCseis")
        self.CCdosedit = QtWidgets.QLineEdit(Form)
        self.CCdosedit.setGeometry(QtCore.QRect(480, 400, 151, 31))
        self.CCdosedit.setObjectName("CCdosedit")
        self.CCtresedit = QtWidgets.QLineEdit(Form)
        self.CCtresedit.setGeometry(QtCore.QRect(480, 450, 151, 31))
        self.CCtresedit.setObjectName("CCtresedit")
        self.CCcuatroedit = QtWidgets.QLineEdit(Form)
        self.CCcuatroedit.setGeometry(QtCore.QRect(480, 500, 151, 31))
        self.CCcuatroedit.setObjectName("CCcuatroedit")
        self.CCcincoedit = QtWidgets.QLineEdit(Form)
        self.CCcincoedit.setGeometry(QtCore.QRect(480, 550, 151, 31))
        self.CCcincoedit.setObjectName("CCcincoedit")
        self.CCseisedit = QtWidgets.QLineEdit(Form)
        self.CCseisedit.setGeometry(QtCore.QRect(480, 600, 151, 31))
        self.CCseisedit.setObjectName("CCseisedit")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(600, 10, 731, 207))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(170, 170, 255)")

        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.botoneliminartodo = QtWidgets.QPushButton(self.widget)
        self.botoneliminartodo.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botoneliminartodo.setObjectName("botoneliminartodo")
        self.gridLayout_4.addWidget(self.botoneliminartodo, 2, 1, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.botonC = QtWidgets.QPushButton(self.widget)
        self.botonC.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonC.setObjectName("botonC")
        self.botonC.clicked.connect(self.eventBotonC)

        self.gridLayout_2.addWidget(self.botonC, 2, 1, 1, 1)
        self.botonS = QtWidgets.QPushButton(self.widget)
        self.botonS.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonS.setObjectName("botonS")
        self.gridLayout_2.addWidget(self.botonS, 3, 4, 1, 1)
        self.botonS.clicked.connect(self.eventBotonS)

        self.botonA = QtWidgets.QPushButton(self.widget)
        self.botonA.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonA.setObjectName("botonA")
        self.gridLayout_2.addWidget(self.botonA, 0, 1, 1, 1)
        self.botonA.clicked.connect(self.eventBotonA)

        self.botonH = QtWidgets.QPushButton(self.widget)
        self.botonH.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonH.setObjectName("botonH")
        self.gridLayout_2.addWidget(self.botonH, 2, 2, 1, 1)
        self.botonH.clicked.connect(self.eventBotonH)

        self.botonG = QtWidgets.QPushButton(self.widget)
        self.botonG.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonG.setObjectName("botonG")
        self.gridLayout_2.addWidget(self.botonG, 1, 2, 1, 1)
        self.botonG.clicked.connect(self.eventBotonG)

        self.botonM = QtWidgets.QPushButton(self.widget)
        self.botonM.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonM.setObjectName("botonM")
        self.gridLayout_2.addWidget(self.botonM, 2, 3, 1, 1)
        self.botonM.clicked.connect(self.eventBotonM)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.botonCuatro = QtWidgets.QPushButton(self.widget)
        self.botonCuatro.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonCuatro.setObjectName("botonCuatro")
        self.gridLayout.addWidget(self.botonCuatro, 1, 0, 1, 1)
        self.botonCuatro.clicked.connect(self.eventBoton4)

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

        self.botonmultiplicacion = QtWidgets.QPushButton(self.widget)
        self.botonmultiplicacion.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonmultiplicacion.setObjectName("botonmultiplicacion")
        self.gridLayout.addWidget(self.botonmultiplicacion, 4, 2, 1, 1)
        self.botonmultiplicacion.clicked.connect(self.eventBotonMulti)

        self.botonsuma = QtWidgets.QPushButton(self.widget)
        self.botonsuma.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonsuma.setObjectName("botonsuma")
        self.gridLayout.addWidget(self.botonsuma, 4, 1, 1, 1)
        self.botonsuma.clicked.connect(self.eventBotonSuma)

        self.botonElevado = QtWidgets.QPushButton(self.widget)
        self.botonElevado.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonElevado.setObjectName("botonElevado")
        self.botonElevado.clicked.connect(self.eventBotonElevado)

        self.gridLayout.addWidget(self.botonElevado, 4, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 5, 1)
        self.botonN = QtWidgets.QPushButton(self.widget)
        self.botonN.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonN.setObjectName("botonN")
        self.gridLayout_2.addWidget(self.botonN, 3, 3, 1, 1)
        self.botonN.clicked.connect(self.eventBotonN)

        self.botonK = QtWidgets.QPushButton(self.widget)
        self.botonK.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonK.setObjectName("botonK")
        self.gridLayout_2.addWidget(self.botonK, 0, 3, 1, 1)
        self.botonK.clicked.connect(self.eventBotonK)

        self.botonQ = QtWidgets.QPushButton(self.widget)
        self.botonQ.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonQ.setObjectName("botonQ")
        self.gridLayout_2.addWidget(self.botonQ, 1, 4, 1, 1)
        self.botonQ.clicked.connect(self.eventBotonQ)

        self.botonF = QtWidgets.QPushButton(self.widget)
        self.botonF.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonF.setObjectName("botonF")
        self.gridLayout_2.addWidget(self.botonF, 0, 2, 1, 1)
        self.botonF.clicked.connect(self.eventBotonF)

        self.botonI = QtWidgets.QPushButton(self.widget)
        self.botonI.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonI.setObjectName("botonI")
        self.gridLayout_2.addWidget(self.botonI, 3, 2, 1, 1)
        self.botonI.clicked.connect(self.eventBotonI)

        self.botonD = QtWidgets.QPushButton(self.widget)
        self.botonD.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonD.setObjectName("botonD")
        self.gridLayout_2.addWidget(self.botonD, 3, 1, 1, 1)
        self.botonD.clicked.connect(self.eventBotonD)

        self.botonL = QtWidgets.QPushButton(self.widget)
        self.botonL.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonL.setObjectName("botonL")
        self.gridLayout_2.addWidget(self.botonL, 1, 3, 1, 1)
        self.botonL.clicked.connect(self.eventBotonL)

        self.botonR = QtWidgets.QPushButton(self.widget)
        self.botonR.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonR.setObjectName("botonR")
        self.gridLayout_2.addWidget(self.botonR, 2, 4, 1, 1)
        self.botonR.clicked.connect(self.eventBotonR)

        self.botonP = QtWidgets.QPushButton(self.widget)
        self.botonP.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonP.setObjectName("botonP")
        self.gridLayout_2.addWidget(self.botonP, 0, 4, 1, 1)
        self.botonP.clicked.connect(self.eventBotonP)

        self.botonB = QtWidgets.QPushButton(self.widget)
        self.botonB.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonB.setObjectName("botonB")
        self.gridLayout_2.addWidget(self.botonB, 1, 1, 1, 1)
        self.botonB.clicked.connect(self.eventBotonB)

        self.botonT = QtWidgets.QPushButton(self.widget)
        self.botonT.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonT.setObjectName("botonT")
        self.gridLayout_2.addWidget(self.botonT, 4, 4, 1, 1)
        self.botonT.clicked.connect(self.eventBotonT)

        self.botonO = QtWidgets.QPushButton(self.widget)
        self.botonO.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonO.setObjectName("botonO")
        self.gridLayout_2.addWidget(self.botonO, 4, 3, 1, 1)
        self.botonO.clicked.connect(self.eventBotonO)

        self.botonJ = QtWidgets.QPushButton(self.widget)
        self.botonJ.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonJ.setObjectName("botonJ")
        self.gridLayout_2.addWidget(self.botonJ, 4, 2, 1, 1)
        self.botonJ.clicked.connect(self.eventBotonJ)

        self.botonE = QtWidgets.QPushButton(self.widget)
        self.botonE.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonE.setObjectName("botonE")
        self.gridLayout_2.addWidget(self.botonE, 4, 1, 1, 1)
        self.botonE.clicked.connect(self.eventBotonE)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 5, 1)
        self.botonU = QtWidgets.QPushButton(self.widget)
        self.botonU.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonU.setObjectName("botonU")
        self.gridLayout_3.addWidget(self.botonU, 0, 1, 1, 1)
        self.botonU.clicked.connect(self.eventBotonU)

        self.botonV = QtWidgets.QPushButton(self.widget)
        self.botonV.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonV.setObjectName("botonV")
        self.gridLayout_3.addWidget(self.botonV, 1, 1, 1, 1)
        self.botonV.clicked.connect(self.eventBotonV)

        self.botonW = QtWidgets.QPushButton(self.widget)
        self.botonW.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonW.setObjectName("botonW")
        self.gridLayout_3.addWidget(self.botonW, 2, 1, 1, 1)
        self.botonW.clicked.connect(self.eventBotonW)

        self.botonX = QtWidgets.QPushButton(self.widget)
        self.botonX.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonX.setObjectName("botonX")
        self.gridLayout_3.addWidget(self.botonX, 3, 1, 1, 1)
        self.botonX.clicked.connect(self.eventBotonX)

        self.botonY = QtWidgets.QPushButton(self.widget)
        self.botonY.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonY.setObjectName("botonY")
        self.gridLayout_3.addWidget(self.botonY, 4, 1, 1, 1)
        self.botonY.clicked.connect(self.eventBotonY)

        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 4, 1)
        self.eliminaruno = QtWidgets.QPushButton(self.widget)
        self.eliminaruno.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.eliminaruno.setObjectName("eliminaruno")
        self.gridLayout_4.addWidget(self.eliminaruno, 1, 1, 1, 1)
        self.botonZ = QtWidgets.QPushButton(self.widget)
        self.botonZ.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonZ.setObjectName("botonZ")
        self.gridLayout_4.addWidget(self.botonZ, 0, 1, 1, 1)
        self.botonZ.clicked.connect(self.eventBotonZ)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def agregarPunto(self):

        try:
            limite = int(self.label.text())
            print("limte:",limite)
            x = int(self.textinput1.text())
            y = int(self.textinput2.text())
            if self.contador <= limite:
                self.coordenadaX.append(x)
                self.coordenadaY.append(y)
                msj = "Pos| "
                for i in range(0,len(self.coordenadaX)):
                    msj += str(i)+" | "
                self.mostrarPosPuntos.setText(msj)
                msj1 = " X   | "
                for i in range(0,len(self.coordenadaX)):
                    if (len(str(self.coordenadaX[i])))==1:
                        msj1 +=str(self.coordenadaX[i])+" | "
                    else:
                        msj1 += str(self.coordenadaX[i])+" | "
                msj2 = " Y   | "
                for i in range(0,len(self.coordenadaY)):
                    if (len(str(self.coordenadaY[i]))) == 1:
                        msj2 += str(self.coordenadaY[i]) + " | "
                    else:
                        msj2 += str(self.coordenadaY[i]) + " | "
                self.mostrarPuntosY.setText(msj2)
                self.mostrarPuntosX.setText(msj1)
                self.contador += 1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(" Cambia el limite de puntos")
                msg.setWindowTitle("Error")
                msg.setStandardButtons(QMessageBox.Ok)
                retval = msg.exec_()

        except:
            print("")
    def abrirTabla(self):
        try:
            filas = 2
            columnas = 10#int(self.label.text())
            self.interfaz = QApplication(sys.argv)
            arr = []
            self.objeto = IngresarMatriz()
            sys.exit(self.interfaz.exec_())
        except:
            print('revisa')
    def grafica(self):
        from funciones import graficadora
        graficadora.graficaCurvas(self.coordenadaX,self.coordenadaY)
    def calcular(self):
        arregloX= self.coordenadaX
        arregloY= self.coordenadaY
        grado1 = curvas.ajusteCurvasGrado1(arregloX,arregloY,int(self.label.text()))
        grado2 = curvas.ajusteCurvasGrado2(arregloX, arregloY, int(self.label.text()))
        grado3 = curvas.ajusteCurvasGrado3(arregloX, arregloY, int(self.label.text()))
        grado4 = curvas.ajusteCurvasGrado4(arregloX, arregloY, int(self.label.text()))
        grado5 = curvas.ajusteCurvasGrado5(arregloX, arregloY, int(self.label.text()))
        grado6 = curvas.ajusteCurvasGrado6(arregloX, arregloY, int(self.label.text()))
        gradoCC1 = curvas.ajusteCurvasGrado1CC(arregloX,arregloY,int(self.label.text()))
        gradoCC2 = curvas.ajusteCurvasGrado2CC(arregloX, arregloY, int(self.label.text()))
        gradoCC3 = curvas.ajusteCurvasGrado3CC(arregloX, arregloY, int(self.label.text()))
        gradoCC4 = curvas.ajusteCurvasGrado4CC(arregloX, arregloY, int(self.label.text()))
        gradoCC5 = curvas.ajusteCurvasGrado5CC(arregloX, arregloY, int(self.label.text()))
        gradoCC6 = curvas.ajusteCurvasGrado6CC(arregloX, arregloY, int(self.label.text()))

        self.gradounoedit.setText(str(grado1))
        self.gradodosedit.setText(str(grado2))
        self.gradotresedit.setText(str(grado3))
        self.gradocuatroedit.setText(str(grado4))
        self.gradocincoedit.setText(str(grado5))
        self.gradoseisedit.setText(str(grado6))

        #self.CCunoedit.setText(str(gradoCC1))
    def eventBotonElevado(self):
        print('^')
        self.entrada = self.label.text()
        self.entrada += "^"
        self.label.setText(self.entrada)
    def eventBotonSuma(self):
        print('+')
        self.entrada = self.label.text()
        self.entrada += "+"
        self.label.setText(self.entrada)
    def eventBotonMulti(self):
        print('*')
        self.entrada = self.label.text()
        self.entrada += "*"
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
        Form.setWindowTitle(_translate("Form", "Ajuste por mínimos cuadrados"))
        self.botoncalcular.setText(_translate("Form", "Calcular"))
        self.botonActualizar.setText(_translate("Form", "Actualizar Tabla"))
        self.textejemplo.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Ajuste por grados </span><span style=\" font-size:12pt; font-style:italic;\">f </span><span style=\" font-size:12pt;\">(x) = a</span><span style=\" font-size:12pt; vertical-align:sub;\">0 </span><span style=\" font-size:12pt;\">+</span><span style=\" font-size:12pt; vertical-align:sub;\"> </span><span style=\" font-size:12pt;\">a</span><span style=\" font-size:12pt; vertical-align:sub;\">1</span><span style=\" font-size:12pt;\">x + a</span><span style=\" font-size:12pt; vertical-align:sub;\">2</span><span style=\" font-size:12pt;\">x</span><span style=\" font-size:12pt; vertical-align:super;\">2</span><span style=\" font-size:12pt;\"> + a</span><span style=\" font-size:12pt; vertical-align:sub;\">3</span><span style=\" font-size:12pt;\">x</span><span style=\" font-size:12pt; vertical-align:super;\">3</span><span style=\" font-size:12pt;\"> +....+ a</span><span style=\" font-size:12pt; vertical-align:sub;\">n</span><span style=\" font-size:12pt;\">x</span><span style=\" font-size:12pt; vertical-align:super;\">n</span><span style=\" font-size:12pt;\">0</span></p></body></html>"))
        self.gradouno.setText(_translate("Form", "     Grado 1 :"))
        self.gradodos.setText(_translate("Form", "     Grado 2 :"))
        self.gradotres.setText(_translate("Form", "     Grado 3 :"))
        self.gradocuatro.setText(_translate("Form", "     Grado 4 :"))
        self.gradocinco.setText(_translate("Form", "     Grado 5 :"))
        self.gradoseis.setText(_translate("Form", "     Grado 6 :"))
        self.numpuntos.setText(_translate("Form", "    Numero de puntos:"))
        self.CCuno.setText(_translate("Form", "   CC :"))
        self.CCdos.setText(_translate("Form", "   CC :"))
        self.CCtres.setText(_translate("Form", "   CC :"))
        self.CCcinco.setText(_translate("Form", "   CC :"))
        self.CCcuatro.setText(_translate("Form", "   CC :"))
        self.CCseis.setText(_translate("Form", "   CC :"))
        self.botoneliminartodo.setText(_translate("Form", "AC"))
        self.botoneliminartodo.setShortcut(_translate("Form", "("))
        self.botonC.setText(_translate("Form", "C"))
        self.botonC.setShortcut(_translate("Form", "*"))
        self.botonS.setText(_translate("Form", "S"))
        self.botonS.setShortcut(_translate("Form", "+"))
        self.botonA.setText(_translate("Form", "A"))
        self.botonA.setShortcut(_translate("Form", "+"))
        self.botonH.setText(_translate("Form", "H"))
        self.botonH.setShortcut(_translate("Form", "+"))
        self.botonG.setText(_translate("Form", "G"))
        self.botonG.setShortcut(_translate("Form", "+"))
        self.botonM.setText(_translate("Form", "M"))
        self.botonM.setShortcut(_translate("Form", "+"))
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
        self.botonmultiplicacion.setText(_translate("Form", "*"))
        self.botonmultiplicacion.setShortcut(_translate("Form", "("))
        self.botonsuma.setText(_translate("Form", "+"))
        self.botonsuma.setShortcut(_translate("Form", "."))
        self.botonElevado.setText(_translate("Form", "^"))
        self.botonElevado.setShortcut(_translate("Form", "("))
        self.botonN.setText(_translate("Form", "N"))
        self.botonN.setShortcut(_translate("Form", "+"))
        self.botonK.setText(_translate("Form", "K"))
        self.botonK.setShortcut(_translate("Form", "+"))
        self.botonQ.setText(_translate("Form", "Q"))
        self.botonQ.setShortcut(_translate("Form", "+"))
        self.botonF.setText(_translate("Form", "F"))
        self.botonF.setShortcut(_translate("Form", "+"))
        self.botonI.setText(_translate("Form", "I"))
        self.botonI.setShortcut(_translate("Form", "+"))
        self.botonD.setText(_translate("Form", "D"))
        self.botonD.setShortcut(_translate("Form", "/"))
        self.botonL.setText(_translate("Form", "L"))
        self.botonL.setShortcut(_translate("Form", "+"))
        self.botonR.setText(_translate("Form", "R"))
        self.botonR.setShortcut(_translate("Form", "+"))
        self.botonP.setText(_translate("Form", "P"))
        self.botonP.setShortcut(_translate("Form", "+"))
        self.botonB.setText(_translate("Form", "B"))
        self.botonB.setShortcut(_translate("Form", "-"))
        self.botonT.setText(_translate("Form", "T"))
        self.botonO.setText(_translate("Form", "O"))
        self.botonO.setShortcut(_translate("Form", "Esc"))
        self.botonJ.setText(_translate("Form", "J"))
        self.botonJ.setShortcut(_translate("Form", "+"))
        self.botonE.setText(_translate("Form", "E"))
        self.botonE.setShortcut(_translate("Form", "%"))
        self.botonU.setText(_translate("Form", "U"))
        self.botonV.setText(_translate("Form", "V"))
        self.botonW.setText(_translate("Form", "W"))
        self.botonX.setText(_translate("Form", "X"))
        self.botonY.setText(_translate("Form", "Y"))
        self.eliminaruno.setText(_translate("Form", "Del"))
        self.eliminaruno.setShortcut(_translate("Form", "("))
        self.botonZ.setText(_translate("Form", "Z"))
        self.botonZ.setShortcut(_translate("Form", "("))

# ====================================================================


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget, QTableWidgetItem, QVBoxLayout, \
    QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot


class IngresarMatriz(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 tabla'
        self.left = 200
        self.top = 200
        self.width = 300
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createTable()

        # Añadir diseño de caja(Box Layout), agregue la tabla al diseño de la caja y agregue el diseño de la caja al widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)

        # Mostrar Widget
        self.show()

    def createTable(self):
        # Crea Tabla
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2, 0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2, 1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3, 0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3, 1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0, 0)

        # cambio de selección de tabla
        self.tableWidget.doubleClicked.connect(self.on_click)

    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print("->",currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


# ====================================================================


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

