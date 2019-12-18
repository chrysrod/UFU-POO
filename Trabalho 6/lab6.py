from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        self.fila = []
        super().__init__()
        Window.resize(self, 513, 401)
        self.setWindowTitle("Fila de Inteiros")
        self.gui()

    def is_int(self, s):
        try: 
            int(s)
            return True
        except ValueError:
            return False

    def insere(self):
        if self.is_int(self.lineEditinsere.text()):
            self.lista.append(int(self.lineEditinsere.text()))
        else:
            self.lineEditinsere.setText("SÓ INT")

    def remove(self):
        if self.is_int(self.lineEditremove.text()):
            if int(self.lineEditremove.text()) in self.lista:
                self.lista.remove(int(self.lineEditremove.text()))
            else:
                self.lineEditremove.setText("N INSERIDO")
        else:
            self.lineEditremove.setText("SÓ INT")

    def maior(self):
        self.lista.sort(reverse=True)
        self.labelmaior.setText(str(self.lista[0]))

    def menor(self):
        self.lista.sort()
        if len(self.lista) >= 1:
            self.labelmenor.setText(str(self.lista[0]))

    def imprimir(self):
        if len(self.lista) >= 1:
            self.lineEditlista.setText(str(self.lista))

    def gui(self):
        self.labellista = QtWidgets.QLabel("Lista:", self)
        self.labellista.setGeometry(QtCore.QRect(80, 50, 41, 17))
        self.labellista.setObjectName("labellista")

        self.lineEditlista = QtWidgets.QLineEdit(self)
        self.lineEditlista.setGeometry(QtCore.QRect(130, 50, 341, 25))
        self.lineEditlista.setObjectName("lineEditlista")

        self.Buttoninsere = QtWidgets.QPushButton("INSERE", self)
        self.Buttoninsere.setGeometry(QtCore.QRect(130, 120, 89, 25))
        self.Buttoninsere.setObjectName("Buttoninsere")
        self.Buttoninsere.clicked.connect(self.insere)

        self.lineEditinsere = QtWidgets.QLineEdit(self)
        self.lineEditinsere.setGeometry(QtCore.QRect(250, 120, 113, 25))
        self.lineEditinsere.setObjectName("lineEditinsere")

        self.Buttonremove = QtWidgets.QPushButton("REMOVE", self)
        self.Buttonremove.setGeometry(QtCore.QRect(130, 160, 89, 25))
        self.Buttonremove.setObjectName("Buttonremove")
        self.Buttonremove.clicked.connect(self.remove)

        self.lineEditremove = QtWidgets.QLineEdit(self)
        self.lineEditremove.setGeometry(QtCore.QRect(250, 160, 113, 25))
        self.lineEditremove.setObjectName("lineEditremove")

        self.Buttonmaior = QtWidgets.QPushButton("MAIOR", self)
        self.Buttonmaior.setGeometry(QtCore.QRect(130, 240, 89, 25))
        self.Buttonmaior.setObjectName("Buttonmaior")
        self.Buttonmaior.clicked.connect(self.maior)
        
        self.Buttonmenor = QtWidgets.QPushButton("MENOR", self)
        self.Buttonmenor.setGeometry(QtCore.QRect(130, 280, 89, 25))
        self.Buttonmenor.setObjectName("Buttonmenor")
        self.Buttonmenor.clicked.connect(self.menor)

        self.Buttonimprimir = QtWidgets.QPushButton("IMPRIME", self)
        self.Buttonimprimir.setGeometry(QtCore.QRect(130, 200, 89, 25))
        self.Buttonimprimir.setObjectName("Buttonimprimir")
        self.Buttonimprimir.clicked.connect(self.imprimir)

        self.labelmaior = QtWidgets.QLabel(self)
        self.labelmaior.setGeometry(QtCore.QRect(250, 240, 111, 17))
        self.labelmaior.setText("")
        self.labelmaior.setObjectName("labelmaior")

        self.labelmenor = QtWidgets.QLabel(self)
        self.labelmenor.setGeometry(QtCore.QRect(250, 280, 111, 17))
        self.labelmenor.setText("")
        self.labelmenor.setObjectName("labelmenor")

        self.Buttoninverte = QtWidgets.QPushButton("INVERTE", self)
        self.Buttoninverte.setGeometry(QtCore.QRect(130, 320, 89, 25))
        self.Buttoninverte.setObjectName("Buttoninverte")
        #self.Buttoninverte.clicked.connect()

        self.Buttontamanho = QtWidgets.QPushButton("TAMANHO", self)
        self.Buttontamanho.setGeometry(QtCore.QRect(130, 360, 89, 25))
        self.Buttontamanho.setObjectName("Buttontamanho")
        #self.Buttoninsere.clicked.connect()

        self.lineEditinsere = QtWidgets.QLineEdit(self)
        self.lineEditinsere.setGeometry(QtCore.QRect(250, 360, 113, 25))
        self.lineEditinsere.setObjectName("lineEdittamanho")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
