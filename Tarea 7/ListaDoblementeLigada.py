class NodoDoble:
    def __init__(self, value=None, siguiente=None, anterior=None):
        self.data = value
        self.next = siguiente
        self.prev = anterior

class DoubleLinkedList:
    def __init__(self):
        self.__head = NodoDoble()
        self.__tail = NodoDoble()
        self.__head.next = self.__tail
        self.__tail.prev = self.__head
        self.__size = 0
    
    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.__head.data == None and self.__tail.data == None

    def append(self, value):
        if self.is_empty():
            self.__head = NodoDoble(value=value)
            self.__tail = self.__head
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            new = NodoDoble(value=value, anterior=curr_node)
            curr_node.next = new
            self.__tail = new
        self.__size += 1

    def find_from_tail(self, value):
        curr_node = self.__tail
        posc = 0
        while curr_node.prev != None and curr_node.data != value:
            curr_node = curr_node.prev
            posc+=1
        return posc

    def find_from_head(self, value):
        curr_node = self.__head
        posc = 0
        while curr_node.next != None and curr_node.data != value:
            curr_node = curr_node.next
            posc+=1
        return posc

    def remove_from_tail(self, value):
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size-=1
        elif self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size-=1
        else:    
            curr_node = self.__tail
            while curr_node.data != value and curr_node.prev != None:
                curr_node = curr_node.prev
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                self.__size-=1
            else:
                print("Valor no encontrado")
    
    def remove_from_head(self, value):
        if self.__tail.data == value:
            self.__tail = self.__tail.prev
            self.__tail.next = None
            self.__size-=1
        elif self.__head.data == value:
            self.__head = self.__head.next
            self.__head.prev = None
            self.__size-=1
        else:    
            curr_node = self.__head
            while curr_node.data != value and curr_node.next != None:
                curr_node = curr_node.next
            if curr_node.data == value:
                curr_node.prev.next = curr_node.next
                curr_node.next.prev = curr_node.prev
                self.__size-=1
            else:
                print("Valor no encontrado")

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.next
        print("")

    def reverse_transversal(self):
        curr_node = self.__tail
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.prev
        print("")