class Nodo:
    def __init__(self, value, next=None):
        self.data = value #falta encapsulamiento 
        self.next = next

class LinkedList:
    def __init__(self):
        self.__head = None
    
    def is_empty(self):
        return self.__head == None

    def tail(self):
        curr_node = self.__head
        while curr_node.next != None:
            curr_node = curr_node.next
        return curr_node

    def append(self, value):
        new = Nodo(value)
        if self.is_empty():
            self.__head = new
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new
    
    def prepend(self, value):
        self.__head = Nodo(value, next=self.__head)

    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.next
        print("")
    
    def remove(self, value):
        if self.__head.data == value: #cuando eliminamos head
            self.__head = self.__head.next
        else:
            curr_node = self.__head
            while curr_node.data != value and curr_node.next != None:
                before = curr_node
                curr_node = curr_node.next
            if curr_node.data == value:
                before.next = curr_node.next
            else:
                print("Value no encontrado (ㆆ_ㆆ)")

    def get(self, posicion=None):
        curr_node = self.__head
        cont = 0
        while curr_node.next != None and cont != posicion:
            curr_node = curr_node.next
            cont+=1
        return curr_node.data
    
    def add_before(self, reference_value, value):
        curr_node = self.__head
        while curr_node.data != reference_value and curr_node != None:
            before = curr_node
            curr_node = curr_node.next
        if curr_node.data == reference_value:
            before.next = Nodo(value, next=curr_node)
        
    def add_after(self, reference_value, value):
        curr_node = self.__head
        while curr_node.data != reference_value and curr_node != None:
            curr_node = curr_node.next
        if curr_node.data == reference_value:
            curr_node.next = Nodo(value, curr_node.next)