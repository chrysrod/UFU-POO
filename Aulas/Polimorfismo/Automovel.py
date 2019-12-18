from Veiculo import *

class Automovel(Veiculo):
    def __init__(self, qte_rodas, tipo):
        Veiculo.__init__(self, tipo)
        self.qte_rodas = qte_rodas

    def mover(self):
        print("Acelerando o automovel")

    def parar(self):
        print("Brecando o automovel")
