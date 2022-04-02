# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'integracionporRectangulos.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    funcionLabel1 = []
    funcionLabel2 = []
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 861)
        Form.setStyleSheet("\n"
"background-color: rgb(250, 250, 250);")

        self.Funcion = QtWidgets.QLabel(Form)
        self.Funcion.setGeometry(QtCore.QRect(20, 60, 111, 31))
        self.Funcion.setAcceptDrops(True)
        self.Funcion.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Funcion.setAutoFillBackground(False)
        self.Funcion.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Funcion.setAlignment(QtCore.Qt.AlignCenter)
        self.Funcion.setWordWrap(False)
        self.Funcion.setOpenExternalLinks(True)
        self.Funcion.setObjectName("Funcion")
        self.labelIngreso = QtWidgets.QLabel(Form)
        self.labelIngreso.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.labelIngreso.setAcceptDrops(True)
        self.labelIngreso.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelIngreso.setAutoFillBackground(False)
        self.labelIngreso.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 11pt \"Arial\";\n"
"")
        self.labelIngreso.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIngreso.setWordWrap(False)
        self.labelIngreso.setOpenExternalLinks(True)
        self.labelIngreso.setObjectName("labelIngreso")
        self.labelIntervalo = QtWidgets.QLabel(Form)
        self.labelIntervalo.setGeometry(QtCore.QRect(20, 110, 111, 31))
        self.labelIntervalo.setAcceptDrops(True)
        self.labelIntervalo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelIntervalo.setAutoFillBackground(False)
        self.labelIntervalo.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 11pt \"Arial\";\n"
"")
        self.labelIntervalo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelIntervalo.setWordWrap(False)
        self.labelIntervalo.setOpenExternalLinks(True)
        self.labelIntervalo.setObjectName("labelIntervalo")
        self.Extremoizq = QtWidgets.QLabel(Form)
        self.Extremoizq.setGeometry(QtCore.QRect(20, 160, 111, 31))
        self.Extremoizq.setAcceptDrops(True)
        self.Extremoizq.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Extremoizq.setAutoFillBackground(False)
        self.Extremoizq.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Extremoizq.setAlignment(QtCore.Qt.AlignCenter)
        self.Extremoizq.setWordWrap(False)
        self.Extremoizq.setOpenExternalLinks(True)
        self.Extremoizq.setObjectName("Extremoizq")

        self.Extremodere = QtWidgets.QLabel(Form)
        self.Extremodere.setGeometry(QtCore.QRect(20, 210, 111, 31))
        self.Extremodere.setAcceptDrops(True)
        self.Extremodere.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Extremodere.setAutoFillBackground(False)
        self.Extremodere.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.Extremodere.setAlignment(QtCore.Qt.AlignCenter)
        self.Extremodere.setWordWrap(False)
        self.Extremodere.setOpenExternalLinks(True)
        self.Extremodere.setObjectName("Extremodere")

        self.particiones = QtWidgets.QLabel(Form)
        self.particiones.setGeometry(QtCore.QRect(20, 260, 141, 31))
        self.particiones.setAcceptDrops(True)
        self.particiones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.particiones.setAutoFillBackground(False)
        self.particiones.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.particiones.setAlignment(QtCore.Qt.AlignCenter)
        self.particiones.setWordWrap(False)
        self.particiones.setOpenExternalLinks(True)
        self.particiones.setObjectName("particiones")

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 60, 251, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.labelestremoizq = QtWidgets.QLineEdit(Form) # ingreso de A
        self.labelestremoizq.setGeometry(QtCore.QRect(140, 160, 251, 31))
        self.labelestremoizq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelestremoizq.setObjectName("labelestremoizq")

        self.labelextremodere = QtWidgets.QLineEdit(Form) # ingreso de b
        self.labelextremodere.setGeometry(QtCore.QRect(140, 210, 251, 31))
        self.labelextremodere.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelextremodere.setObjectName("labelextremodere")

        self.labelParticiones = QtWidgets.QLineEdit(Form) # @mensaje ingreso de las particiones
        self.labelParticiones.setGeometry(QtCore.QRect(170, 260, 251, 31))
        self.labelParticiones.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelParticiones.setText("")
        self.labelParticiones.setObjectName("labelParticiones")

        self.botonCalcular = QtWidgets.QPushButton(Form)
        self.botonCalcular.setGeometry(QtCore.QRect(30, 320, 91, 41))
        self.botonCalcular.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 87 12pt \"Arial\";")

        self.botongrafica = QtWidgets.QPushButton(Form)
        self.botongrafica.setGeometry(QtCore.QRect(270, 320, 91, 41))
        self.botongrafica.setStyleSheet("background-color: rgb(225, 225, 225);\n"
"font: 87 12pt \"Arial\";")
        self.botongrafica.setObjectName("botongrafica")

        self.labelsalida = QtWidgets.QLabel(Form)
        self.labelsalida.setGeometry(QtCore.QRect(20, 380, 111, 31))
        self.labelsalida.setAcceptDrops(True)
        self.labelsalida.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelsalida.setAutoFillBackground(False)
        self.labelsalida.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 11pt \"Arial\";\n"
"")
        self.labelsalida.setAlignment(QtCore.Qt.AlignCenter)
        self.labelsalida.setWordWrap(False)
        self.labelsalida.setOpenExternalLinks(True)
        self.labelsalida.setObjectName("labelsalida")

        self.labelintegral = QtWidgets.QLabel(Form)
        self.labelintegral.setGeometry(QtCore.QRect(20, 430, 131, 31))
        self.labelintegral.setAcceptDrops(True)
        self.labelintegral.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelintegral.setAutoFillBackground(False)
        self.labelintegral.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"font: 11pt \"Arial\";\n"
"")
        #self.labelintegral.setText("asdasdasdas")

        self.labelintegral.setAlignment(QtCore.Qt.AlignCenter)
        self.labelintegral.setWordWrap(False)
        self.labelintegral.setOpenExternalLinks(True)
        self.labelintegral.setObjectName("labelintegral")

        self.labelpuntoizq = QtWidgets.QLabel(Form)
        self.labelpuntoizq.setGeometry(QtCore.QRect(20, 480, 111, 31))
        self.labelpuntoizq.setAcceptDrops(True)
        self.labelpuntoizq.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelpuntoizq.setAutoFillBackground(False)
        self.labelpuntoizq.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.labelpuntoizq.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpuntoizq.setWordWrap(False)
        self.labelpuntoizq.setOpenExternalLinks(True)
        self.labelpuntoizq.setObjectName("labelpuntoizq")
        self.labelpuntoextremoizq = QtWidgets.QLabel(Form)
        self.labelpuntoextremoizq.setGeometry(QtCore.QRect(140, 480, 251, 31))
        self.labelpuntoextremoizq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelpuntoextremoizq.setText("")
        self.labelpuntoextremoizq.setObjectName("labelpuntoextremoizq")
        self.labelpuntoderecho = QtWidgets.QLabel(Form) #
        self.labelpuntoderecho.setGeometry(QtCore.QRect(20, 530, 111, 31))
        self.labelpuntoderecho.setAcceptDrops(True)
        self.labelpuntoderecho.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelpuntoderecho.setAutoFillBackground(False)
        self.labelpuntoderecho.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.labelpuntoderecho.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpuntoderecho.setWordWrap(False)
        self.labelpuntoderecho.setOpenExternalLinks(True)
        self.labelpuntoderecho.setObjectName("labelpuntoderecho")

        self.labelpuntoderecho2 = QtWidgets.QLabel(Form) # @mensaje label que muestra el extremo derecho
        self.labelpuntoderecho2.setGeometry(QtCore.QRect(140, 530, 251, 31))
        self.labelpuntoderecho2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelpuntoderecho2.setText("")
        self.labelpuntoderecho2.setObjectName("labelpuntoderecho2")
        self.labelpuntoderecho_2 = QtWidgets.QLabel(Form)
        self.labelpuntoderecho_2.setGeometry(QtCore.QRect(20, 580, 111, 31))
        self.labelpuntoderecho_2.setAcceptDrops(True)
        self.labelpuntoderecho_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelpuntoderecho_2.setAutoFillBackground(False)
        self.labelpuntoderecho_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.labelpuntoderecho_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelpuntoderecho_2.setWordWrap(False)
        self.labelpuntoderecho_2.setOpenExternalLinks(True)
        self.labelpuntoderecho_2.setObjectName("labelpuntoderecho_2")

        self.labelmedio = QtWidgets.QLabel(Form) # @mensaje muestra el punto medio
        self.labelmedio.setGeometry(QtCore.QRect(140, 580, 251, 31))
        self.labelmedio.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelmedio.setText("")
        self.labelmedio.setObjectName("labelmedio")

        self.labelintegral_2 = QtWidgets.QLabel(Form)
        self.labelintegral_2.setGeometry(QtCore.QRect(170, 430, 251, 31))
        self.labelintegral_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelintegral_2.setObjectName("labelintegral_2")

        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(500, 10, 565, 203))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.botonUno_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonUno_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonUno_2.setObjectName("botonUno_2")
        self.gridLayout_4.addWidget(self.botonUno_2, 0, 0, 1, 1)
        self.botonUno_2.clicked.connect(self.eventBoton1)

        self.botonDos_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDos_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonDos_2.setObjectName("botonDos_2")
        self.gridLayout_4.addWidget(self.botonDos_2, 0, 1, 1, 1)
        self.botonDos_2.clicked.connect(self.eventBoton2)

        self.botonTres_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonTres_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonTres_2.setObjectName("botonTres_2")
        self.gridLayout_4.addWidget(self.botonTres_2, 0, 2, 1, 1)
        self.botonTres_2.clicked.connect(self.eventBoton3)

        self.botonCuatro_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCuatro_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonCuatro_2.setObjectName("botonCuatro_2")
        self.gridLayout_4.addWidget(self.botonCuatro_2, 1, 0, 1, 1)
        self.botonCuatro_2.clicked.connect(self.eventBoton4)

        self.botonCinco_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCinco_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonCinco_2.setObjectName("botonCinco_2")
        self.gridLayout_4.addWidget(self.botonCinco_2, 1, 1, 1, 1)
        self.botonCinco_2.clicked.connect(self.eventBoton5)

        self.botonSeis_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSeis_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonSeis_2.setObjectName("botonSeis_2")
        self.gridLayout_4.addWidget(self.botonSeis_2, 1, 2, 1, 1)
        self.botonSeis_2.clicked.connect(self.eventBoton6)

        self.botonSiete_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonSiete_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonSiete_2.setObjectName("botonSiete_2")
        self.gridLayout_4.addWidget(self.botonSiete_2, 2, 0, 1, 1)
        self.botonSiete_2.clicked.connect(self.eventBoton7)

        self.botonOcho_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonOcho_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonOcho_2.setObjectName("botonOcho_2")
        self.gridLayout_4.addWidget(self.botonOcho_2, 2, 1, 1, 1)
        self.botonOcho_2.clicked.connect(self.eventBoton8)

        self.botonNueve_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonNueve_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonNueve_2.setObjectName("botonNueve_2")
        self.gridLayout_4.addWidget(self.botonNueve_2, 2, 2, 1, 1)
        self.botonNueve_2.clicked.connect(self.eventBoton9)

        self.botonCabierto_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_4.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonCabierto_4.setObjectName("botonCabierto_4")
        self.gridLayout_4.addWidget(self.botonCabierto_4, 3, 0, 1, 1)
        self.botonCabierto_4.clicked.connect(self.eventBotonParentesis)

        self.botonCero_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCero_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonCero_2.setObjectName("botonCero_2")
        self.gridLayout_4.addWidget(self.botonCero_2, 3, 1, 1, 1)
        self.botonCero_2.clicked.connect(self.eventBoton0)

        self.botonCerrado_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCerrado_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonCerrado_2.setObjectName("botonCerrado_2")
        self.gridLayout_4.addWidget(self.botonCerrado_2, 3, 2, 1, 1)
        self.botonCerrado_2.clicked.connect(self.eventBotonParentesis2)

        self.botonCabierto_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_5.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonCabierto_5.setObjectName("botonCabierto_5")
        self.gridLayout_4.addWidget(self.botonCabierto_5, 4, 0, 1, 1)
        self.botonCabierto_5.clicked.connect(self.eventBotonCorchete)

        self.botonPunto_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPunto_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.botonPunto_2.setObjectName("botonPunto_2")
        self.gridLayout_4.addWidget(self.botonPunto_2, 4, 1, 1, 1)
        self.botonPunto_2.clicked.connect(self.eventBotonPunto)

        self.botonCabierto_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonCabierto_6.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonCabierto_6.setObjectName("botonCabierto_6")
        self.gridLayout_4.addWidget(self.botonCabierto_6, 4, 2, 1, 1)
        self.botonCabierto_6.clicked.connect(self.eventBotonCorchete2)

        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 5, 1)
        self.botonMas_15 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_15.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_15.setObjectName("botonMas_15")
        self.gridLayout_3.addWidget(self.botonMas_15, 0, 1, 1, 1)
        self.botonMas_15.clicked.connect(self.eventBotonSumar)

        self.botonMas_16 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_16.setStyleSheet("font: 75 14pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_16.setObjectName("botonMas_16")
        self.gridLayout_3.addWidget(self.botonMas_16, 0, 2, 1, 1)
        self.botonMas_16.clicked.connect(self.eventRaiz)

        self.botonMas_17 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_17.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_17.setObjectName("botonMas_17")
        self.gridLayout_3.addWidget(self.botonMas_17, 0, 3, 1, 1)
        self.botonMas_17.clicked.connect(self.eventBotonExp)

        self.botonMas_18 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_18.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_18.setObjectName("botonMas_18")
        self.gridLayout_3.addWidget(self.botonMas_18, 0, 4, 1, 1)
        self.botonMas_18.clicked.connect(self.eventBotonTan)

        self.botonMenos_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMenos_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMenos_2.setObjectName("botonMenos_2")
        self.gridLayout_3.addWidget(self.botonMenos_2, 1, 1, 1, 1)
        self.botonMenos_2.clicked.connect(self.eventBotonMenos)

        self.botonMas_19 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_19.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_19.setObjectName("botonMas_19")
        self.gridLayout_3.addWidget(self.botonMas_19, 1, 2, 1, 1)
        self.botonMas_19.clicked.connect(self.eventoExponente)

        self.botonMas_20 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_20.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_20.setObjectName("botonMas_20")
        self.gridLayout_3.addWidget(self.botonMas_20, 1, 3, 1, 1)
        self.botonMas_20.clicked.connect(self.eventBotonLog)

        self.botonMas_21 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_21.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_21.setObjectName("botonMas_21")
        self.gridLayout_3.addWidget(self.botonMas_21, 1, 4, 1, 1)
        self.botonMas_21.clicked.connect(self.eventBotonSec)

        self.BotonMulti_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonMulti_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.BotonMulti_2.setObjectName("BotonMulti_2")
        self.gridLayout_3.addWidget(self.BotonMulti_2, 2, 1, 1, 1)
        self.BotonMulti_2.clicked.connect(self.eventBotonMultiplicar)

        self.botonMas_22 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_22.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_22.setObjectName("botonMas_22")
        self.gridLayout_3.addWidget(self.botonMas_22, 2, 2, 1, 1)
        self.botonMas_22.clicked.connect(self.eventPi)

        self.botonMas_23 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_23.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_23.setObjectName("botonMas_23")
        self.gridLayout_3.addWidget(self.botonMas_23, 2, 3, 1, 1)
        self.botonMas_23.clicked.connect(self.eventBotonSin)

        self.botonMas_24 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_24.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_24.setObjectName("botonMas_24")
        self.gridLayout_3.addWidget(self.botonMas_24, 2, 4, 1, 1)
        self.botonMas_24.clicked.connect(self.eventBotonCsc)

        self.botonDivision_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonDivision_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonDivision_2.setObjectName("botonDivision_2")
        self.gridLayout_3.addWidget(self.botonDivision_2, 3, 1, 1, 1)
        self.botonDivision_2.clicked.connect(self.eventDiv)

        self.botonMas_25 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_25.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_25.setObjectName("botonMas_25")
        self.gridLayout_3.addWidget(self.botonMas_25, 3, 2, 1, 1)
        self.botonMas_25.clicked.connect(self.eventBotonln)

        self.botonMas_26 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_26.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_26.setObjectName("botonMas_26")
        self.gridLayout_3.addWidget(self.botonMas_26, 3, 3, 1, 1)
        self.botonMas_26.clicked.connect(self.eventBotonCos)

        self.botonMas_27 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonMas_27.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonMas_27.setObjectName("botonMas_27")
        self.gridLayout_3.addWidget(self.botonMas_27, 3, 4, 1, 1)
        self.botonMas_27.clicked.connect(self.eventBotonCot)

        self.botonPorcentaje_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonPorcentaje_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonPorcentaje_2.setObjectName("botonPorcentaje_2")
        self.gridLayout_3.addWidget(self.botonPorcentaje_2, 4, 1, 1, 1)
        self.botonPorcentaje_2.clicked.connect(self.eventBotonPorcentaje)

        self.botonintegral = QtWidgets.QPushButton(self.layoutWidget)
        self.botonintegral.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonintegral.setObjectName("botonintegral")
        self.botonintegral.clicked.connect(self.eventBotonIntegral)

        self.gridLayout_3.addWidget(self.botonintegral, 4, 2, 1, 1)
        self.botonAC_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.botonAC_2.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"background-color: rgb(0, 170, 127);")
        self.botonAC_2.setObjectName("botonAC_2")
        self.gridLayout_3.addWidget(self.botonAC_2, 4, 4, 1, 1)
        self.botonAC_2.clicked.connect(self.eventoBorrarTotal)

        self.BotonBorrar_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.BotonBorrar_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 87 14pt \"Arial Black\";")
        self.BotonBorrar_2.setObjectName("BotonBorrar_2")
        self.gridLayout_3.addWidget(self.BotonBorrar_2, 4, 3, 1, 1)
        self.BotonBorrar_2.clicked.connect(self.eventoBorrar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mostrarGrafica(self):

        try:
            #
            self.funcion = self.label.text()  # esta variable toma el valor de lo que este escrito en este label
            self.limite1 = float(self.TextLimIn.text())
            self.limite2 = float(self.TextLim.text())
            self.errorTole = float(self.TextErrorT.text())

            #bss.graficaTotal(self.funcion, self.limite1, self.limite2, self.errorTole)
            # raiz = bss.calculoRaiz(self.funcion,self.limite1,self.limite2,self.errorTole)
            # print(raiz)



        except:
            print('algun error en la grafica')

    def eventCalcular(self):
        try:
            # se inicializan los labels para poder cambiarlos
            self.entrada2 = self.label_2.text()

            # se actualizan los label de los resultados, osea ya muestran los resultados

            print(self.entrada2)
        except:
            print('hubo algun error')

    def eventTabla(self):
        # se inicializan los labels para poder cambiarlos
        self.entrada2 = self.label_2.text()
        self.entrada3 = self.label_3.text()
        self.entrada4 = self.label_4.text()
        # se obtiene cada dato que se digito en la interfaz
        self.funcion = self.label.text()
        self.limite1 = self.TextLimIn.text()
        self.limite2 = self.TextLim.text()
        self.errorTole = self.TextErrorT.text()
        # se hace los calculos respectivos con las variables anteriores
        print('salio')

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
    def eventBotonIntegral(self):
        print('∫')
        Ui_Form.funcionLabel1.append('f')
        Ui_Form.funcionLabel2.append('∫')
        self.entrada = self.label.text()
        self.entrada2 = self.label_5.text()
        self.entrada += "f"
        self.entrada2 += '∫'
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
    def eventoBorrarTotal(self):
        try:
            self.entrada = self.label.text()
            self.entrada2 = self.label_5.text()
            tamaño = len(self.entrada)
            self.label.setText(self.entrada[:tamaño - tamaño])
            self.label_5.setText(self.entrada2[:tamaño - tamaño])
        except:
            print('no hay mas que borrar')
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
            print('no se puede borrar mas')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Integración númerica por rectangulos"))
        self.Funcion.setText(_translate("Form", "Función F(x) ="))
        self.labelIngreso.setText(_translate("Form", "Ingreso:"))
        self.labelIntervalo.setText(_translate("Form", "Intervalo:"))
        self.Extremoizq.setText(_translate("Form", "Extremo Izq  a ="))
        self.Extremodere.setText(_translate("Form", "Extremo Der  b ="))
        self.particiones.setText(_translate("Form", "Numero de Particiones  n ="))
        self.botonCalcular.setText(_translate("Form", "Calcular"))
        self.botongrafica.setText(_translate("Form", "Grafica"))
        self.labelsalida.setText(_translate("Form", "Salida:"))
        self.labelintegral.setText(_translate("Form", "Integral :  "))
        self.labelpuntoizq.setText(_translate("Form", "Punto Extremo Izq ="))
        self.labelpuntoderecho.setText(_translate("Form", "Punto Extremo Der ="))
        self.labelpuntoderecho_2.setText(_translate("Form", "Punto Medio ="))
        self.labelintegral_2.setText(_translate("Form", "∫_a^b▒f(x)dx"))
        self.botonUno_2.setText(_translate("Form", "1"))
        self.botonUno_2.setShortcut(_translate("Form", "1"))
        self.botonDos_2.setText(_translate("Form", "2"))
        self.botonDos_2.setShortcut(_translate("Form", "2"))
        self.botonTres_2.setText(_translate("Form", "3"))
        self.botonTres_2.setShortcut(_translate("Form", "3"))
        self.botonCuatro_2.setText(_translate("Form", "4"))
        self.botonCuatro_2.setShortcut(_translate("Form", "4"))
        self.botonCinco_2.setText(_translate("Form", "5"))
        self.botonCinco_2.setShortcut(_translate("Form", "5"))
        self.botonSeis_2.setText(_translate("Form", "6"))
        self.botonSeis_2.setShortcut(_translate("Form", "6"))
        self.botonSiete_2.setText(_translate("Form", "7"))
        self.botonSiete_2.setShortcut(_translate("Form", "7"))
        self.botonOcho_2.setText(_translate("Form", "8"))
        self.botonOcho_2.setShortcut(_translate("Form", "8"))
        self.botonNueve_2.setText(_translate("Form", "9"))
        self.botonNueve_2.setShortcut(_translate("Form", "9"))
        self.botonCabierto_4.setText(_translate("Form", "("))
        self.botonCabierto_4.setShortcut(_translate("Form", "("))
        self.botonCero_2.setText(_translate("Form", "0"))
        self.botonCero_2.setShortcut(_translate("Form", "0"))
        self.botonCerrado_2.setText(_translate("Form", ")"))
        self.botonCerrado_2.setShortcut(_translate("Form", ")"))
        self.botonCabierto_5.setText(_translate("Form", "["))
        self.botonCabierto_5.setShortcut(_translate("Form", "("))
        self.botonPunto_2.setText(_translate("Form", "."))
        self.botonPunto_2.setShortcut(_translate("Form", "."))
        self.botonCabierto_6.setText(_translate("Form", "]"))
        self.botonCabierto_6.setShortcut(_translate("Form", "("))
        self.botonMas_15.setText(_translate("Form", "+"))
        self.botonMas_15.setShortcut(_translate("Form", "+"))
        self.botonMas_16.setText(_translate("Form", "√"))
        self.botonMas_16.setShortcut(_translate("Form", "+"))
        self.botonMas_17.setText(_translate("Form", "exp"))
        self.botonMas_17.setShortcut(_translate("Form", "+"))
        self.botonMas_18.setText(_translate("Form", "tan"))
        self.botonMas_18.setShortcut(_translate("Form", "+"))
        self.botonMenos_2.setText(_translate("Form", "-"))
        self.botonMenos_2.setShortcut(_translate("Form", "-"))
        self.botonMas_19.setText(_translate("Form", "^"))
        self.botonMas_19.setShortcut(_translate("Form", "+"))
        self.botonMas_20.setText(_translate("Form", "log"))
        self.botonMas_20.setShortcut(_translate("Form", "+"))
        self.botonMas_21.setText(_translate("Form", "sec"))
        self.botonMas_21.setShortcut(_translate("Form", "+"))
        self.BotonMulti_2.setText(_translate("Form", "*"))
        self.BotonMulti_2.setShortcut(_translate("Form", "*"))
        self.botonMas_22.setText(_translate("Form", "π"))
        self.botonMas_22.setShortcut(_translate("Form", "+"))
        self.botonMas_23.setText(_translate("Form", "sin"))
        self.botonMas_23.setShortcut(_translate("Form", "+"))
        self.botonMas_24.setText(_translate("Form", "csc"))
        self.botonMas_24.setShortcut(_translate("Form", "+"))
        self.botonDivision_2.setText(_translate("Form", "÷"))
        self.botonDivision_2.setShortcut(_translate("Form", "/"))
        self.botonMas_25.setText(_translate("Form", "ln"))
        self.botonMas_25.setShortcut(_translate("Form", "+"))
        self.botonMas_26.setText(_translate("Form", "cos"))
        self.botonMas_26.setShortcut(_translate("Form", "+"))
        self.botonMas_27.setText(_translate("Form", "cot"))
        self.botonMas_27.setShortcut(_translate("Form", "+"))
        self.botonPorcentaje_2.setText(_translate("Form", "%"))
        self.botonPorcentaje_2.setShortcut(_translate("Form", "%"))
        self.botonintegral.setText(_translate("Form", "x"))
        self.botonintegral.setShortcut(_translate("Form", "+"))
        self.botonAC_2.setText(_translate("Form", "AC"))
        self.BotonBorrar_2.setText(_translate("Form", "<-"))
        self.BotonBorrar_2.setShortcut(_translate("Form", "Esc"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

