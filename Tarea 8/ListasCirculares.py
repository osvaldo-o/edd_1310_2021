class Nodo:
    def __init__(self, value, siguiente):
        self.data = value
        self.next = siguiente

class CircularList:
    def __init__(self):
        self.__ref = None

    def is_empty(self):
        return self.__ref == None

    def insert(self, value):
        if self.is_empty():
            nuevo = Nodo(value, None)
            nuevo.next = nuevo
            self.__ref = nuevo
        elif self.search(value) == False:
            if value < self.__ref.next.data:
                self.__ref.next = Nodo(value, self.__ref.next)
            elif value > self.__ref.data:
                self.__ref.next = Nodo(value, self.__ref.next)
                self.__ref = self.__ref.next
            else:
                curr_node = self.__ref
                while value > curr_node.next.data:
                    curr_node = curr_node.next
                curr_node.next = Nodo(value, curr_node.next)
        else:
            print("El valor ya existe")
    
    def transversal(self):
        curr_node = self.__ref.next
        while curr_node.data != self.__ref.data:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.next
        print(f"|{self.__ref.data}|->")
    
    def search(self, value):
        curr_node = self.__ref.next
        while curr_node.data != value and curr_node.data != self.__ref.data:
            curr_node = curr_node.next
        if curr_node.data == value:
            return True
        else:
            return False
    
    def remove(self, value):
        if self.search(value):
            prev = self.__ref
            curr_node = self.__ref.next
            while curr_node.data != value:
                prev = curr_node
                curr_node = curr_node.next
            prev.next = curr_node.next
            if value == self.__ref.data:
                self.__ref = prev