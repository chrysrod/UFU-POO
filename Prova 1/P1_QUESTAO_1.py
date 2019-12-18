import math as m

class NumComplexo():

    def __init__(self):
        self.Re = 0
        self.Im = 0

    def getRe(self):
        return self.Re

    def getIm(self):
        return self.Im

    def setRe(self, _Re):
        self.Re =_Re

    def setIm(self, _Im):
        self.Im = _Im

    def soma(self, z1, z2):
        self.somaRe = z1.getRe() + z2.getRe()
        self.somaIm = z1.getIm() + z2.getIm()
        self.setRe(self.somaRe)
        self.setIm(self.somaIm)
        return str(self.Re) + ' + ' + str(self.Im) + 'i'
    
    def vezes(self, z1, z2):
        self.vezesRe = (z1.getRe() * z2.getRe()) - (z1.getIm() * z2.getIm())
        self.vezesIm = (z1.getRe() * z2.getIm()) + (z1.getIm() * z2.getRe())
        self.setRe(self.vezesRe)
        self.setIm(self.vezesIm)
        return str(self.Re) + ' + ' + str(self.Im) + 'i'

    def modulo(self):
        self.modulo = m.sqrt(m.pow(self.getRe(), 2) + m.pow(self.getIm(), 2))
        return self.modulo

    def argumento(self):
        self.argumento = m.asin(self.getIm()    /self.modulo())

    def polar(self):
        return (str(self.modulo()) + '(cos' + self.argumento + '+' + 'i.sen' + self.argumento + ')')

class Programa():

    def __init__(self):
        self.apresentacao()
        self.programa()

    def apresentacao(self):
        print("Prova 1 - Questão 1 - Programação Orientada a Objetos")
        print("Professores: Edgard Lamounier e Windysson de Souza")
        print("Aluno: Chrystian R. Campos - Matrícula: 11721ECP006")

    def programa(self):
        z1 = NumComplexo()
        z1.setRe(1)
        z1.setIm(1)
        z2 = NumComplexo()
        z2.setRe(3)
        z2.setIm(-1)
        z3 = NumComplexo()
        print("A) Soma: ", z3.soma(z1, z2))
        print("B) Multiplicação: ", z3.vezes(z1, z2))
        print("C) Módulo: ", z1.modulo())
        #print("D) Argumento: ", z1.argumento())
        #print("E) Forma Polar: ", z1.polar())
        #z3.soma(z1, z2)
        #print("F) Forma polar do complexo da soma de z1 e z2: ", z3.polar())
        #z3.vezes(z1, z2)
        #print("F) Forma polar do complexo do produto de z1 e z2: ", z3.polar())

Programa()