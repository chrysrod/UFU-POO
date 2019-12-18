import sys
from lista import List

l = List()

def menu():
    print("[1] Insere um inteiro na Lista")
    print("[2] Remove um elemento na Lista")
    print("[3] Imprime a Lista")
    print("[4] Sair")

    opcao = int(input("Insira a opção desejada: "))

    if opcao == 1:
        i = input("Digite um inteiro para ser inserido na lista: ")
        l.append(i)
    elif opcao == 2:
        i = input("Digite um inteiro para ser removido da lista: ")
        l.remove(i)
    elif opcao == 3:
        print(l.__repr__())
    elif opcao == 4:
        sys.exit(0)
    else:
        print("Opcão inválida")
        menu()

def insere(i):
    pass

def imprime(i):
    pass

while(True):
    menu()