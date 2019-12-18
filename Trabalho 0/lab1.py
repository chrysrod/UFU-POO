import math as m

class Vetor2D():

    def __init__(self):
        print("Laboratório 1 - Disciplina de Programação Orientada a Objetos - Prof. Edgard Lamounier")
        print("Nome: Chrystian Rodrigues Campos | Matrícula: 11721ECP006")

    def create(self, vectorNumber):
        self.vector = []
        self.vectorNumber = vectorNumber
        self.vector.append(input("Insira as coordenadas x y do vetor {}: " .format(self.vectorNumber)).split())
        if len(self.vector[0]) == 2:
            print("Vetor {0} criado com sucesso -> {1}" .format(self.vectorNumber, self.vector))
            return self.vector
        else:
            print("Coordenadas incorretas, por favor, insira as coordenadas na forma x y")
            return self.create(vectorNumber)

    def escalar(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.escalar = ((int(v1[0][0])*int(v2[0][0])) + (int(v1[0][1])*int(v2[0][1])))
        return print("O produto escalar dos vetores é: " + str(self.escalar))

    def modulo(self, v1, v2):
        self.modulo = m.sqrt(m.pow((int(v1[0][0])-int(v2[0][0])),2) + m.pow((int(v1[0][1])-int(v2[0][1])),2))
        return print("O módulo (distância entre os vetores) é: " + str(self.modulo))

    def angulo(self, v1, v2):
        self.angulo = self.escalar / (m.sqrt(m.pow((int(v1[0][0])),2) + m.pow((int(v1[0][1])),2)) * m.sqrt(m.pow((int(v2[0][0])),2) + m.pow((int(v2[0][1])),2)))
        return print("O ângulo é: " + str(m.degrees(m.acos(self.angulo))))

    def projecao(self, v1, v2):
        self.projecao = []
        self.projecao.append((self.escalar / m.pow((m.pow(m.sqrt(m.pow(int(v1[0][0]), 2) + m.pow(int(v1[0][1]),2)), 2)), 2)))
        self.projecao.append((self.escalar / m.pow((m.pow(m.sqrt(m.pow(int(v1[0][0]), 2) + m.pow(int(v1[0][1]),2)), 2)), 2)))
        return print("A projeção é: " + str(self.projecao[0] * int(v1[0][0])) + " " + str(self.projecao[1] * int(v1[0][1])))

vector = Vetor2D()
v1 = vector.create(1)
v2 = vector.create(2)

vector.escalar(v1, v2)
vector.modulo(v1, v2)
vector.angulo(v1, v2)
vector.projecao(v1, v2)
