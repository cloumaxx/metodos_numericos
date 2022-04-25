from PyQt5.QtWidgets import QScrollArea, QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ScrollLabel(QScrollArea):

    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        self.setWidgetResizable(True)

        content = QWidget(self)
        self.setWidget(content)

        lay = QVBoxLayout(content)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.label = QLabel(content)
        #setGeometry(QtCore.QRect(190, 70, 261, 31))
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.label.setWordWrap(True)

        lay.addWidget(self.label)

    def setText(self, text):
        self.label.setText(text)
