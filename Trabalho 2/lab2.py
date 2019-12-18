import math as m

class Vetor2D():

    def __init__(self):
        self.x = 0
        self.y = 0

    def setX(self):
        self.x = input("Insira a coordenada x do vetor: ")

    def setY(self):
        self.y = input("Insira a coordenada y do vetor: ")

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def defineVetor2D(self):
        self.setX()
        self.setY()
        
class Vetor3D(Vetor2D):
    
    def __init__(self):
        Vetor2D.__init__(self)
        self.z = 0
        
    def setZ(self):
        self.z = input("Insira a coordenada z do vetor: ")

    def getZ(self):
        return self.z

    def defineVetor3D(self):
        self.defineVetor2D()
        self.setZ()

    def printaVetor3D(self):
        print('[' + str(self.getX()) + ',' + str(self.getY()) + ',' + str(self.getZ()) + ']')

    def modulo3D(self, v2):
        self.modulo3D = m.sqrt(m.pow((int(self.x)-int(v2.x)),2) + m.pow((int(self.y)-int(v2.y)),2) + m.pow((int(self.z)-int(v2.z)),2))
        return print("O módulo (distância entre os vetores) é: " + str(self.modulo3D))

    def vetorial3D(self, v2):
        self.vetorial3D = [(int(self.y) * int(v2.z)) - (int(self.z) * int(v2.y)), (int(self.z) * int(v2.x)) - (int(self.x) * int(v2.z)), (int(self.x) * int(v2.y)) - (int(self.y) * int(v2.x))] 
        return print("O produto vetorial é o vetor: [" + str(self.vetorial3D[0]) + ',' + str(self.vetorial3D[1]) + ',' + str(self.vetorial3D[2]) + ']')

class Programa():

    def __init__(self):
        self.v1 = Vetor3D()
        self.v2 = Vetor3D()
        self.opcao = 0
        self.apresentacao()

    def apresentacao(self):
        print("Laboratório 3 - Disciplina de Programação Orientada a Objetos")
        print("Prof. Edgard Lamounier - Prof. Windysson")
        print("Nome: Chrystian Rodrigues Campos | Matrícula: 11721ECP006")
        while(True):
            self.menu()

    def menu(self):
        print("\n")
        print("========== Menu ==========")
        print("1 - Definir vetor 1")
        print("2 - Definir vetor 2")
        print("3 - Consultar valores")
        print("4 - Módulo")
        print("5 - Produto vetorial")
        print("6 - Sair")
        print("==========================")
        print("\n")
        
        self.opcao = input("Insira a opção desejada (1-6): ")

        if(self.opcao == '1'):
            self.v1.defineVetor3D()
        elif(self.opcao == '2'):
            self.v2.defineVetor3D()
        elif(self.opcao == '3'):
            print("Vetor 1")
            self.v1.printaVetor3D()
            print("Vetor 2")
            self.v2.printaVetor3D()
        elif(self.opcao == '4'):
            self.v1.modulo3D(self.v2)
        elif(self.opcao == '5'):
            self.v1.vetorial3D(self.v2)
        elif(self.opcao == '6'):
            exit(0)
        else:
            print("Opção inválida! Tente novamente.")
            self.menu()

programa = Programa()
