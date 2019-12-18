from lista import List #importa a classe List da biblioteca lista

if __name__ == '__main__':
    l = List() #criar lista vazia(não tem a opção de criar uma lista sem ser vazia)
    l.append(5) #inserção de elemento a lista
    l.append(8)
    l.append(56)
    print(l) #imprimir lista
    print(l[1]) #imprimir o elemento de certo indice da lista
    l.remove(8) #remover elemento da lista
    print(l)
    len(l) #verificar tamanho da lista
    l.index(56) #verificar o indice do elemento
    l.insert(1, 23) #inserção do elemento 23 no indice 1 da lista
        