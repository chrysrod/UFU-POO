#! /usr/bin/python3
# -*- coding: utf-8 -*-
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys, os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        Window.resize(self, 370, 200)
        Window.setWindowTitle(self, 'Gui')
        self.gui()
        
    def gui(self):
        self.labelExpressao = QtWidgets.QLabel("Digite a expressão:", self)
        self.labelExpressao.setGeometry(QtCore.QRect(16, 30, 141, 20))
        self.labelExpressao.setObjectName("labelExpressao")
        
        self.lineEditExpressao = QtWidgets.QLineEdit(self)
        self.lineEditExpressao.setGeometry(QtCore.QRect(190, 30, 113, 25))
        self.lineEditExpressao.setObjectName("lineEditExpressao")
        
        
        self.Buttonok = QtWidgets.QPushButton("ok", self)
        self.Buttonok.setGeometry(QtCore.QRect(130, 100, 89, 25))
        self.Buttonok.setObjectName("Buttonok")
        self.Buttonok.clicked.connect(self.ok)
        
        self.labelResultado = QtWidgets.QLabel("Resultado:", self)
        self.labelResultado.setGeometry(QtCore.QRect(20, 150, 81, 17))
        self.labelResultado.setObjectName("labelResultado")
        
        self.labelResultadoescrito = QtWidgets.QLabel(self)
        self.labelResultadoescrito.setGeometry(QtCore.QRect(110, 150, 181, 17))
        self.labelResultadoescrito.setText("")
        self.labelResultadoescrito.setObjectName("labelResultadoescrito")

    def ok(self):
        try:
            self.expressao = self.lineEditExpressao.text()
            self.labelResultadoescrito.setText(str(self.testaExpressao()))
        except Exception as e:
            QMessageBox.warning(QMessageBox(),'Erro', str(e))

    def testaExpressao(self):
        self.lista = []
        self.resultado = ''
        self.exp = list(self.expressao)
        for i in self.exp:
            if(i in ['{','[','(',')',']','}']):
                if(len(self.lista) >= 1):
                    if(i == ')' and self.lista[len(self.lista)-1] == '('):
                        self.lista.pop()
                    elif(i == ']' and self.lista[len(self.lista)-1] == '['):
                        self.lista.pop()
                    elif(i == '}' and self.lista[len(self.lista)-1] == '{'):
                        self.lista.pop()
                    else:
                        self.lista.append(i)
                else:
                    self.lista.append(i)
        if(len(self.lista) == 0):
            return 'Expressão matemática bem formulada!'
        else:
            return 'Expressão matemática mal formulada!'

class Programa():

    def __init__(self):
        self.apresentacao()

    def apresentacao(self):
        print("Laboratório 5 - Disciplina de Programação Orientada a Objetos")
        print("Prof. Edgard Lamounier - Prof. Windysson Souza")
        print("Nome: Chrystian Rodrigues Campos | Matrícula: 11721ECP006")

if __name__ == '__main__':
    programa = Programa()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
