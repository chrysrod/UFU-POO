class Pagtos():

    def __init__(self, _cpf, _valor, _cod):
        self.cpf = _cpf
        self.valor = _valor
        self.cod = _cod
    
    def faturar(self):
        return self.valor

    def getCpf(self):
        return self.cpf

    def getValor(self):
        return self.valor
    
    def getCod(self):
        return self.cod

    def setCpf(self, _cpf):
        self.cpf = _cpf

    def setValor(self, _valor):
        self.valor = _valor

    def setCod(self, _cod):
        self.cod = _cod

class Alimentacao(Pagtos):

    def __init__(self, cpf, valor, cod):
        Pagtos.__init__(self, cpf, valor, cod)
        self.descricao = ''
        self.vlFatAliment = 0
        self.faturar()

    def faturar(self):
        vlFatAliment = self.valor * 1.12
        return self.setVlFatAliment(vlFatAliment)

    def getDescricao(self):
        return self.descricao

    def getVlFatAliment(self):
        return self.vlFatAliment

    def setDescricao(self, _descricao):
        self.descricao = _descricao

    def setVlFatAliment(self, _vlFatAliment):
        self.vlFatAliment = _vlFatAliment
        
class Saude(Pagtos):

    def __init__(self, cpf, valor, cod):
        Pagtos.__init__(self, cpf, valor, cod)
        self.estabelecimento = ''
        self.vlFatSaude = 0
        self.faturar()
    
    def faturar(self):
        vlFatSaude = self.valor * 1.05
        return self.setVlFatSaude(vlFatSaude)

    def getEstabelecimento(self):
        return self.estabelecimento

    def getVlFatSaude(self):
        return self.vlFatSaude

    def setEstabelecimento(self, _estabelecimento):
        self.estabelecimento = _estabelecimento

    def setVlFatSaude(self, _vlFatSaude):
        self.vlFatSaude = _vlFatSaude

class Programa():

    def __init__(self):
        self.apresentacao()
        self.bd = []
        self.cadastro()

    def apresentacao(self):
        print("Prova 1 - Questão 2 - Programação Orientada a Objetos")
        print("Professores: Edgard Lamounier e Windysson de Souza")
        print("Aluno: Chrystian R. Campos - Matrícula: 11721ECP006")

    def cadastro(self):
        self.cadastroFaturamentoAlimentacao(11640234521, 1000, 1, 'Compras 1')
        self.cadastroFaturamentoAlimentacao(11640234522, 2000, 2, 'Compras 2')
        self.cadastroFaturamentoAlimentacao(11640234523, 3000, 3, 'Compras 3')
        self.cadastroFaturamentoSaude(11640234531, 1000, 4, 'Consultório 1')
        self.cadastroFaturamentoSaude(11640234532, 2000, 5, 'Consultório 2')
        self.cadastroFaturamentoSaude(11640234533, 3000, 6, 'Consultório 3')

    def cadastroFaturamentoAlimentacao(self, cpf, valor, cod, desc):
        self.cadastro = []
        self.dados = Alimentacao(cpf, valor, cod)
        self.dados.setDescricao(desc)
        self.cadastro.append(self.dados.getCpf())
        self.cadastro.append(self.dados.getValor())
        self.cadastro.append(self.dados.getCod())
        self.cadastro.append(self.dados.getDescricao())
        self.cadastro.append(self.dados.getVlFatAliment())

        self.bd.append(self.cadastro)

    def cadastroFaturamentoSaude(self, cpf, valor, cod, est):
        self.cadastro = []
        self.dados = Saude(cpf, valor, cod)
        self.dados.setEstabelecimento(est)
        self.cadastro.append(self.dados.getCpf())
        self.cadastro.append(self.dados.getValor())
        self.cadastro.append(self.dados.getCod())
        self.cadastro.append(self.dados.getEstabelecimento())
        self.cadastro.append(self.dados.getVlFatSaude())

        self.bd.append(self.cadastro)

    def relatorio(self):
        for line in self.bd:
            print(line)

Programa().relatorio()