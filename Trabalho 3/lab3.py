class Funcionario(object):
    def __init__(self, nome = '', codigo = '', escolaridade = '', salario = 1000):
        self.nome = nome
        self.codigo = codigo
        self.escolaridade = escolaridade
        self.salario = salario

class FuncionarioSemEstudo(Funcionario):
    def __init__(self, nome = '', codigo = '', escolaridade = '', salario = 1000):
        Funcionario.__init__(self, nome, codigo, escolaridade, salario)
        
class FuncionarioEnsinoBasico(Funcionario):
    def __init__(self, nome = '', codigo = '', escolaridade = '',  instituicao = '', salario = 1000 * 1.1):
        Funcionario.__init__(self, nome, codigo, escolaridade, salario)
        self.instituicao = instituicao

class FuncionarioEnsinoMedio(Funcionario):
    def __init__(self, nome = '', codigo = '', escolaridade = '',  instituicao = '', salario = 1000 * 1.5):
        Funcionario.__init__(self, nome, codigo, escolaridade, salario)
        self.instituicao = instituicao

class FuncionarioEnsinoSuperior(Funcionario):
    def __init__(self, nome = '', codigo = '', escolaridade = '',  instituicao = '', curso = '', salario = 1000 * 2):
        Funcionario.__init__(self, nome, codigo, escolaridade, salario)
        self.instituicao = instituicao
        self.curso = curso
    
class Programa():

    def __init__(self):
        self.apresentacao()
        self.funcionarios = []
        for i in range(0,9):
            self.cadastro(i)
        self.relatorio()

    def apresentacao(self):
        print("Laboratório 3 - Disciplina de Programação Orientada a Objetos")
        print("Prof. Edgard Lamounier - Prof. Windysson Souza")
        print("Nome: Chrystian Rodrigues Campos | Matrícula: 11721ECP006")

    def cadastro(self, i):
        self.funcionario = {}
        print("Funcionário ", i)
        self.nome = input("Insira o nome: ")
        self.codigo = input("Insira o código: ")
        self.escolaridade = input("Insira a escolaridade (Não estudou, Ensino básico, Ensino médio, Ensino superior): ")
        
        if self.escolaridade == "Não estudou":
            f = FuncionarioSemEstudo(self.nome, self.codigo, self.escolaridade)
            self.funcionario['Nome'] = f.nome
            self.funcionario['Código'] = f.codigo
            self.funcionario['Escolaridade'] = f.escolaridade
            self.funcionario['Salário'] = f.salario
        elif self.escolaridade == "Ensino básico":
            self.instituicao = input("Insira a instituição de ensino: ")
            f = FuncionarioEnsinoBasico(self.nome, self.codigo, self.escolaridade, self.instituicao)
            self.funcionario['Nome'] = f.nome
            self.funcionario['Código'] = f.codigo
            self.funcionario['Escolaridade'] = f.escolaridade
            self.funcionario['Instituição'] = f.instituicao
            self.funcionario['Salário'] = f.salario
        elif self.escolaridade == "Ensino médio":
            self.instituicao = input("Insira a instituição de ensino: ")
            f = FuncionarioEnsinoMedio(self.nome, self.codigo, self.escolaridade, self.instituicao)
            self.funcionario['Nome'] = f.nome
            self.funcionario['Código'] = f.codigo
            self.funcionario['Escolaridade'] = f.escolaridade
            self.funcionario['Instituição'] = f.instituicao
            self.funcionario['Salário'] = f.salario
        elif self.escolaridade == "Ensino superior":
            self.instituicao = input("Insira a instituição de ensino: ")
            self.curso = input("Insira o curso: ") 
            f = FuncionarioEnsinoSuperior(self.nome, self.codigo, self.escolaridade, self.instituicao, self.curso)
            self.funcionario['Nome'] = f.nome
            self.funcionario['Código'] = f.codigo
            self.funcionario['Escolaridade'] = f.escolaridade
            self.funcionario['Instituição'] = f.instituicao
            self.funcionario['Curso'] = f.curso
            self.funcionario['Salário'] = f.salario
        else:
            print("Escolaridade incorreta")
            exit(1)

        self.funcionarios.append(self.funcionario)

    def relatorio(self):
        self.soma = 0
        self.somaSE = 0
        self.somaEB = 0
        self.somaEM = 0
        self.somaES = 0
        for funcionario in self.funcionarios:
            print(funcionario)
            self.soma += funcionario['Salário']
            
            if funcionario['Escolaridade'] == "Não estudou":
                self.somaSE += funcionario['Salário']
            elif funcionario['Escolaridade'] == "Ensino básico":
                self.somaEB += funcionario['Salário']
            elif funcionario['Escolaridade'] == "Ensino médio":
                self.somaEM += funcionario['Salário']
            elif funcionario['Escolaridade'] == "Ensino superior":
                self.somaES += funcionario['Salário']
            
        print("A soma de gastos é: ", self.soma)
        print("Gastos com funcionários sem estudo: ", self.somaSE)
        print("Gastos com funcionários com ensino básico: ", self.somaEB)
        print("Gastos com funcionários com ensino médio: ", self.somaEM)
        print("Gastos com funcionários com ensino superior: ", self.somaES)

programa = Programa()
