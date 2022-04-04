import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QPushButton


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    b = QPushButton(w)
    b.setText("Show message!")

    b.move(50, 50)
    b.clicked.connect(showdialog)
    w.setWindowTitle("PyQt Dialog demo")
    w.show()
    sys.exit(app.exec_())


def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)

    msg.setText("Hubo Algun error, revisa los datos registrados")
    msg.setWindowTitle("Error")
    msg.setStandardButtons(QMessageBox.Ok )

    retval = msg.exec_()



def msgbtn(i):
    print
    "Button pressed is:", i.text()


if __name__ == '__main__':
    window()