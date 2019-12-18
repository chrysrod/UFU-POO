from node import Node

# inserir na fila
# remover da fila
# observar o primeiro da fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
    
    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size = self._size + 1
    
    def getLast(self):
        return self.last.data

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            if self.first is None:
                self.last = None
            self._size = self._size - 1
            return elem
        raise IndexError("A fila está vazia")


    def peek(self):
        if self._size > 0:
            elem = self.first.data
            return elem
        raise IndexError("A fila está vazia")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Fila vazia"

    def __str__(self):
        return self.__repr__()
