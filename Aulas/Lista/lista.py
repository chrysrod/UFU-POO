from node import Node


class List:
    def __init__(self): #construtor
        self.head = None #cabeça da lista
        self._size = 0 #tamanho da lista

    def append(self, elem): #inserir elementos no final da lista
        if self.head: #inserção quando a lista já possui elementos
            pointer = self.head  
            while(pointer.next): #avança enquanto a variavel ponteiro tiver um proximo
                pointer = pointer.next
            pointer.next = Node(elem)
        else: #primeira inserção
            self.head = Node(elem)
        self._size = self._size + 1 #incrementar o valor do size

    def __len__(self): #retorna o tamanho da lista
        return self._size

    def _getnode(self, index): #retorna o nó daquele indice
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def __getitem__(self, index): #retorna um dado elemento do indice
        pointer = self._getnode(index)
        if pointer: #se o indice retorna o elemento
            return pointer.data
        else: #se não tiver ele retorna o erro
            raise IndexError("list index out of range")

    def __setitem__(self, index, elem): #modifica o valor de um elemento em um indice
        pointer = self._getnode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem): #retorna o indice do elemento na lista
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i+1
        raise ValueError("{} is not in list".format(elem))

    def insert(self, index, elem): #inserir elemento em qualquer lugar da lista
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elem): #remove elemento da lista
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(elem))

    def __repr__(self): #percorre a lista transformando em string
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + "->"
            pointer = pointer.next
        return r

    def __str__(self): #converte a lista em string para poder utilizar o print
        return self.__repr__()
