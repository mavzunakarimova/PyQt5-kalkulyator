from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class  Oyna(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hisoblagich")
        self.setGeometry(50, 50, 231, 350)
        self.kurinish()
        self.show()

    def kurinish(self):

        self.label = QLabel(self)
        self.label.setGeometry(5, 5, 220, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid pink;"
                                 "background : white;"
                                 "}")

        self.label.setAlignment(Qt.AlignRight)
        son7 = QPushButton("7", self)
        son7.setGeometry(5, 100, 40, 40)
        son8 = QPushButton("8", self)
        son8.setGeometry(50, 100, 40, 40)
        son9=QPushButton("9",self)
        son9.setGeometry(95,100,40,40)
        sonbul=QPushButton("/",self)
        sonbul.setGeometry(140,100,40,40)
        sontoza=QPushButton("C",self)
        sontoza.setGeometry(185,100,40,40)
        son4=QPushButton("4",self)
        son4.setGeometry(5,160,40,40)
        son5=QPushButton("5",self)
        son5.setGeometry(50,160,40,40)
        son6 = QPushButton("6", self)
        son6.setGeometry(95, 160, 40, 40)
        sonkup = QPushButton("*", self)
        sonkup.setGeometry(140, 160, 40, 40)
        sonqov = QPushButton("(", self)
        sonqov.setGeometry(185, 160, 40, 40)
        son1=QPushButton("1",self)
        son1.setGeometry(5,220,40,40)
        son2 = QPushButton("2", self)
        son2.setGeometry(50, 220, 40, 40)
        son3 = QPushButton("3", self)
        son3.setGeometry(95, 220, 40, 40)
        sonmin = QPushButton("-", self)
        sonmin.setGeometry(140, 220, 40, 40)
        sonqav = QPushButton(")", self)
        sonqav.setGeometry(185,220, 40, 40)
        son0 = QPushButton("0", self)
        son0.setGeometry(5, 280, 40, 40)
        son00 = QPushButton("00", self)
        son00.setGeometry(50, 280, 40, 40)
        sonnuq = QPushButton(".", self)
        sonnuq.setGeometry(95, 280, 40, 40)
        sonqush = QPushButton("+", self)
        sonqush.setGeometry(140, 280, 40, 40)
        sonbar = QPushButton("=", self)
        sonbar.setGeometry(185, 280, 40, 40)

App = QApplication(sys.argv)
oyna = Oyna()
# oyna.show()
sys.exit(App.exec())


