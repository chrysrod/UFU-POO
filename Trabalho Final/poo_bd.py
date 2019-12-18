from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3

class Inicia():
    def __init__(self):
        self.conn=sqlite3.connect("poo.db")
        self.c = self.conn.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS aluno(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT NOT NULL, matricula TEXT NOT NULL, endereco TEXT NOT NULL)""")
        self.c.close()
        self.conn.close()


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        Window.resize(self, 549, 573)
        self.setWindowTitle("POO")

        self.Buttoninsert = QtWidgets.QPushButton("insert", self)
        self.Buttoninsert.setGeometry(QtCore.QRect(90, 270, 89, 25))
        self.Buttoninsert.setObjectName("Buttoninsert")
        self.Buttoninsert.clicked.connect(self.insert)

        self.Buttonselect = QtWidgets.QPushButton("select", self)
        self.Buttonselect.setGeometry(QtCore.QRect(200, 270, 89, 25))
        self.Buttonselect.setObjectName("Buttonselect")
        self.Buttonselect.clicked.connect(self.select)

        self.Buttonupdate = QtWidgets.QPushButton("update", self)
        self.Buttonupdate.setGeometry(QtCore.QRect(300, 270, 89, 25))
        self.Buttonupdate.setObjectName("Buttonupdate")
        self.Buttonupdate.clicked.connect(self.up)

        self.Buttondelete = QtWidgets.QPushButton("delete", self)
        self.Buttondelete.setGeometry(QtCore.QRect(400, 270, 89, 25))
        self.Buttondelete.setObjectName("Buttondelete")
        self.Buttondelete.clicked.connect(self.excluir)

        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(25, 40, 451, 201))
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Id")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Nome")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("email")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("matricula")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("endereco")

        self.labelnome = QtWidgets.QLabel("nome:", self)
        self.labelnome.setGeometry(QtCore.QRect(30, 310, 51, 17))
        self.labelnome.setObjectName("labelnome")

        self.lineEditnome = QtWidgets.QLineEdit(self)
        self.lineEditnome.setGeometry(QtCore.QRect(120, 310, 291, 25))
        self.lineEditnome.setObjectName("lineEditnome")

        self.labelemail = QtWidgets.QLabel("email", self)
        self.labelemail.setGeometry(QtCore.QRect(30, 350, 51, 17))
        self.labelemail.setObjectName("labelemail")

        self.lineEditemail = QtWidgets.QLineEdit(self)
        self.lineEditemail.setGeometry(QtCore.QRect(120, 350, 291, 25))
        self.lineEditemail.setObjectName("lineEditemail")

        self.labelmatricula = QtWidgets.QLabel("matricula:", self)
        self.labelmatricula.setGeometry(QtCore.QRect(30, 400, 67, 17))
        self.labelmatricula.setObjectName("labelmatricula")

        self.lineEditmatricula = QtWidgets.QLineEdit(self)
        self.lineEditmatricula.setGeometry(QtCore.QRect(120, 400, 291, 25))
        self.lineEditmatricula.setObjectName("lineEditmatricula")

        self.labelend = QtWidgets.QLabel("endereço:", self)
        self.labelend.setGeometry(QtCore.QRect(30, 450, 71, 17))
        self.labelend.setObjectName("labelend")

        self.lineEditend = QtWidgets.QLineEdit(self)
        self.lineEditend.setGeometry(QtCore.QRect(120, 450, 291, 25))
        self.lineEditend.setObjectName("lineEdit")

        self.tabela()

    def insert(self):
        
        nome = self.lineEditnome.text()
        email = self.lineEditemail.text()
        matricula = self.lineEditmatricula.text()
        end = self.lineEditend.text() 
                
        try:
            self.conn=sqlite3.connect("poo.db")
            self.c = self.conn.cursor()

            self.c.execute("""INSERT INTO aluno(nome, email, matricula, endereco) VALUES (?, ?, ?, ?)""", (nome, email, matricula, end))
            self.conn.commit()
            QMessageBox.information(QMessageBox(), 'Cadastro', 'Dados Salvos Com Sucesso!')
            self.c.close()
            self.conn.close()
            
        
        except Exception as e:
            
            QMessageBox.warning(QMessageBox(), 'Erro', 'Não foi Possível Cadastrar os Dados!')

        self.lineEditnome.setText("")
        self.lineEditemail.setText("")
        self.lineEditmatricula.setText("")
        self.lineEditend.setText("")
        self.tabela()


    def tabela(self):
        item = QTableWidgetItem
        

        self.conn = sqlite3.connect("poo.db")
        self.c = self.conn.cursor()

        
        # lendo os dados
        self.c.execute("""SELECT id FROM aluno""")
        row = self.c.fetchall()
        x = int(len(row))
        for i in range(0, x):
            for linha in row:
                ro = row[i]
                self.tableWidget.setItem(i, 0, item(str(ro[0])))

        self.c.execute("""SELECT nome FROM aluno""")

        row = self.c.fetchall()
        x = int(len(row))
        for i in range(0, x):
            for linha in row:
                ro = row[i]
                self.tableWidget.setItem(i, 1, item(str(ro[0])))

        self.c.execute("""SELECT email FROM aluno""")

        row = self.c.fetchall()
        x = int(len(row))
        for i in range(0, x):
            for linha in row:
                ro = row[i]
                self.tableWidget.setItem(i, 2, item(str(ro[0])))

        self.c.execute("""SELECT matricula FROM aluno""")

        row = self.c.fetchall()
        x = int(len(row))
        for i in range(0, x):
            for linha in row:
                ro = row[i]
                self.tableWidget.setItem(i, 3, item(str(ro[0])))

        self.c.execute("""SELECT endereco FROM aluno""")
        row = self.c.fetchall()
        x = int(len(row))
        for i in range(0, x):
            for linha in row:
                ro = row[i]
                self.tableWidget.setItem(i, 4, item(str(ro[0])))
        

        self.c.close()
        self.conn.close()

    def select(self):
        matricula = self.lineEditmatricula.text()
        self.conn = sqlite3.connect("poo.db")
        self.c = self.conn.cursor()

        if(matricula == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite a matricula!')

        else:
            self.c.execute("""SELECT nome FROM aluno WHERE matricula=?""", [matricula])
            row = self.c.fetchall()
            nome = row[0][0]
            self.lineEditnome.setText(str(nome))
            self.c.execute("""SELECT email FROM aluno WHERE matricula=?""", [matricula])
            row = self.c.fetchall()
            email = row[0][0]
            self.lineEditemail.setText(email)
            self.c.execute("""SELECT endereco FROM aluno WHERE matricula=?""", [matricula])
            row = self.c.fetchall()
            endereco= row[0][0]
            self.lineEditend.setText(endereco)

        self.c.close()
        self.conn.close()

    def up(self):
        nome = self.lineEditnome.text()
        email = self.lineEditemail.text()
        matricula = self.lineEditmatricula.text()
        end = self.lineEditend.text() 
        self.conn = sqlite3.connect("poo.db")
        self.c = self.conn.cursor()
        self.c.execute("""SELECT nome FROM aluno WHERE matricula=?""", [matricula])
        row = self.c.fetchall()
        x = int(len(row))
        if (nome == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite o nome!')

        elif (email == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite o email!')

        elif (matricula == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite a matricula!')

        elif (end == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite o endereço!')

        elif(x == 0):
            QMessageBox.warning(QMessageBox(), 'Erro', 'matricula não existe!')

        else:
            try:
                self.conn = sqlite3.connect("poo.db")
                self.c = self.conn.cursor()
                self.c.execute("""UPDATE aluno SET nome=?, email= ?, endereco= ? where matricula=?""", (nome, email, end, matricula))   
                self.conn.commit()
                QMessageBox.information(QMessageBox(), 'Cadastro', 'Dados Alterados Com Sucesso!')
                self.lineEditnome.setText("")
                self.lineEditemail.setText("")
                self.lineEditmatricula.setText("")
                self.lineEditend.setText("")
            except Exception as e:
                print(e)
                QMessageBox.warning(QMessageBox(), 'Erro', 'Não foi Possível Alterar os Dados!')

        self.c.close()
        self.conn.close()
        self.tabela()

    def excluir(self):
        matricula = self.lineEditmatricula.text()
        self.conn = sqlite3.connect("poo.db")
        self.c = self.conn.cursor()
        if(matricula == ""):
            QMessageBox.warning(QMessageBox(), 'Erro', 'Digite a matricula!')

        else:
            try:
                self.c.execute("""DELETE FROM aluno WHERE matricula = ?""", [matricula])
                QMessageBox.information(QMessageBox(), 'Cadastro', 'Dados deletados Com Sucesso!')
                self.conn.commit()
                self.lineEditnome.setText("")
                self.lineEditemail.setText("")
                self.lineEditmatricula.setText("")
                self.lineEditend.setText("")
            except Exception as e:
                print(e)
                QMessageBox.warning(QMessageBox(), 'Erro', 'Não foi Possível deletar os Dados!')
        
            


if __name__ == "__main__":
    import sys
    Inicia()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
