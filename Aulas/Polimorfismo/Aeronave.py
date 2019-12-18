from Veiculo import *

class Aeronave(Veiculo):
    def __init__(self, qte_turbinas, tipo):
        Veiculo.__init__(self, tipo)
        self.qte_turbinas = qte_turbinas

    def mover(self):
        print("Acelerando o aeronave")

    def parar(self):
        print("Brecando o aeronave")
