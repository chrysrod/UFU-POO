from datetime import datetime

class Tempo():

    def __init__(self):
        self.hora = ''
        self.min = ''
        self.seg = ''
        self.horario = ''

    def get(self):
        self.horario = input("Insira o horário na forma hh:mm:ss : ")
        self.hora, self.min, self.seg = self.horario.split(':')
        self.tratamento()

    def tratamento(self):
        if int(self.hora) >= 0 and int(self.hora) <= 23:
            if len(self.hora) == 1:
                self.hora = '0' + self.hora
        else:
            print("Horário inválido")
            self.get()
        if int(self.min) >= 0 and int(self.min) <= 59:
            if len(self.min) == 1:
                self.min = '0' + self.min
        else:
            print("Horário inválido")
            self.get()
        if int(self.seg) >= 0 and int(self.seg) <= 59:
            if len(self.seg) == 1:
                self.seg = '0' + self.seg
        else:
            print("Horário inválido")
            self.get()

        self.horario = datetime.strptime(self.hora + ':' + self.min + ':' + self.seg, '%H:%M:%S')

    def printHora(self):
        print(self.horario)

    def soma(self, tempo2):
        self.soma = Tempo()
        self.soma.horario = tempo2.horario + self.horario
        return self.soma.horario

    def sub(self, tempo2):
        self.sub = Tempo()
        self.sub.horario = tempo2.horario - self.horario
        return self.sub.horario
        
class Estacionamento():

    def __init__(self):
        self.get()

    def get(self):
        self.placa = str(input("Insira a placa do carro: "))
        self.marca = str(input("Insira a marca do carro: "))
        self.tempo1 = Tempo()
        self.tempo1.get()
        self.tempo2 = Tempo()
        self.tempo2.get()
        self.preco()

    def preco(self):
        self.duracao = str(self.tempo1.sub(self.tempo2))
        if self.duracao.find(':') == 1:
            self.valor = int(self.duracao[:1]) * 7
        else:
            self.valor = int(self.duracao[:2]) * 7

tabela = [['Placa', 'Marca', 'Entrada', 'Saída', 'Valor']]

for i in range(0,5):
    carro = Estacionamento()
    tabela.append([carro.placa, carro.marca, str(carro.tempo1.horario), str(carro.tempo2.horario), carro.valor])

for line in tabela:
    print(line)
