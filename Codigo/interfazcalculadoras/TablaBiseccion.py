
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QDialog, QPushButton, QTableWidget,
                             QTableWidgetItem, QAbstractItemView, QHeaderView, QMenu,
                             QActionGroup, QAction, QMessageBox)

from funciones import biseccion as bss
# ======================= CLASE tableWidget ========================

class tableWidget(QDialog):
    def __init__(self, parent=None):
        super(tableWidget, self).__init__(parent)

        self.setWindowTitle("Tabla Datos")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(950, 348)

        self.initUI()

    def initUI(self):

        # ================== WIDGET  QTableWidget ==================

        self.tabla = QTableWidget(self)

        # Deshabilitar edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # Deshabilitar el comportamiento de arrastrar y soltar
        self.tabla.setDragDropOverwriteMode(False)

        # Seleccionar toda la fila
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Seleccionar una fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)

        # Especifica dónde deben aparecer los puntos suspensivos "..." cuando se muestran
        # textos que no encajan
        self.tabla.setTextElideMode(Qt.ElideRight)  # Qt.ElideNone

        # Establecer el ajuste de palabras del texto
        self.tabla.setWordWrap(False)

        # Deshabilitar clasificación
        self.tabla.setSortingEnabled(False)

        # Establecer el número de columnas
        self.tabla.setColumnCount(8)

        # Establecer el número de filas
        self.tabla.setRowCount(0)

        # Alineación del texto del encabezado
        self.tabla.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter | Qt.AlignVCenter |
                                                          Qt.AlignCenter)

        # Deshabilitar resaltado del texto del encabezado al seleccionar una fila
        self.tabla.horizontalHeader().setHighlightSections(False)

        # Hacer que la última sección visible del encabezado ocupa todo el espacio disponible
        self.tabla.horizontalHeader().setStretchLastSection(True)

        # Ocultar encabezado vertical
        self.tabla.verticalHeader().setVisible(False)

        # Dibujar el fondo usando colores alternados
        self.tabla.setAlternatingRowColors(True)

        # Establecer altura de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)

        # self.tabla.verticalHeader().setHighlightSections(True)

        nombreColumnas = ("Iteracion", "Funcion", "Intervalo A", "Intervalo B", "F(ri)", "E_r","E_t","Raiz")

        # Establecer las etiquetas de encabezado horizontal usando etiquetas
        self.tabla.setHorizontalHeaderLabels(nombreColumnas)

        # Menú contextual
        self.tabla.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabla.customContextMenuRequested.connect(self.menuContextual)

        # Establecer ancho de las columnas
        for indice, ancho in enumerate((80, 120, 120, 110, 150), start=0):
            self.tabla.setColumnWidth(indice, ancho)

        self.tabla.resize(900, 240)
        self.tabla.move(20, 56)

        # =================== WIDGETS QPUSHBUTTON ==================

        botonMostrarDatos = QPushButton("Mostrar datos", self)
        botonMostrarDatos.setFixedWidth(140)
        botonMostrarDatos.move(20, 20)

        menu = QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QAction(columna, menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)

            menu.addAction(accion)

        botonMostrarOcultar = QPushButton("Motrar/ocultar columnas", self)
        botonMostrarOcultar.setFixedWidth(180)
        botonMostrarOcultar.setMenu(menu)
        botonMostrarOcultar.move(170, 20)




        # ======================== EVENTOS =========================

        botonMostrarDatos.clicked.connect(self.datosTabla)


        menu.triggered.connect(self.mostrarOcultar)

    # ======================= FUNCIONES ============================


    def datosTabla(self):

        datos = [("1", "Andres", "Niño", "Masculino", "06/12/2019", "Colombia"," "," s"),
                 ("2", "Donald", "Trump", "Masculino", "06/12/1950", "Estados Unidos"),
                 ("3", "María Fernanda", "Espinosa", "Femenino", "06/10/1980", "Ecuador"),
                 ("4", "Alberto", "Canosa", "Masculino", "04/05/1876", "España"),
                 ("5", "Virtud", "Pontes", "Femenino", "23/18/1965", "España"),
                 ("6", "Elon", "Musk", "Masculino", "06/12/1960", "Estados Unidos"),
                 ("7", "Richard", "Branson", "Masculino", "14/12/1956", "Reino Unido"),
                 ("8", "Gabriel", "Garcia Marquez", "Masculino", "19/11/1948", "Colombia"),
                 ("9", "Valentina", "Tereshkova", "Femenino", "06/03/1937", "Rusia"),
                 ("10", "Artur", "Fischer", "Masculino", "31/12/1919", "Alemania"),
                 ("11", "Grace", "Murray Hopper", "Femenino", "09/12/1906", "Estados Unidos"),
                 ("12", "Guido van", "Rossum", "Masculino", "31/01/1956", "Países Bajos")]
        self.tabla.clearContents()
        print('->',type(datos))
        row = 0
        for endian in datos:
            self.tabla.setRowCount(row + 1)

            idDato = QTableWidgetItem(endian[0])
            idDato.setTextAlignment(4)

            self.tabla.setItem(row, 0, idDato)
            self.tabla.setItem(row, 1, QTableWidgetItem(endian[1]))
            self.tabla.setItem(row, 2, QTableWidgetItem(endian[2]))
            self.tabla.setItem(row, 3, QTableWidgetItem(endian[3]))
            self.tabla.setItem(row, 4, QTableWidgetItem(endian[4]))
            self.tabla.setItem(row, 5, QTableWidgetItem(endian[5]))

            row += 1

    def mostrarOcultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)



    def menuContextual(self, posicion):
        indices = self.tabla.selectedIndexes()

        if indices:
            menu = QMenu()

            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)

            menu.addAction(QAction("Copiar todo", itemsGrupo))

            columnas = [self.tabla.horizontalHeaderItem(columna).text()
                        for columna in range(self.tabla.columnCount())
                        if not self.tabla.isColumnHidden(columna)]

            for indice, item in enumerate(columnas, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)


            itemsGrupo.triggered.connect(self.copiarTableWidgetItem)

            menu.exec_(self.tabla.viewport().mapToGlobal(posicion))

    def copiarTableWidgetItem(self, accion):
        filaSeleccionada = [dato.text() for dato in self.tabla.selectedItems()]

        if accion.text() == "Copiar todo":
            filaSeleccionada = tuple(filaSeleccionada)
        else:
            filaSeleccionada = filaSeleccionada[accion.data()]

        print(filaSeleccionada)

        return


# ===============================================================

if __name__ == "__main__":
    import sys

    aplicacion = QApplication(sys.argv)

    fuente = QFont()
    fuente.setPointSize(10)
    aplicacion.setFont(fuente)

    ventana = tableWidget()
    ventana.show()

    sys.exit(aplicacion.exec_())