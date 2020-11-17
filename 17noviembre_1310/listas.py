class Nodo:
    def __init__(self, value, next=None):
        self.data = value #falta encapsulamiento 
        self.next = next

class LinkedList:
    def __init__(self):
        self.__head = None
    
    def is_empty(self):
        return self.__head == None

    def append(self, value):
        new = Nodo(value)
        if self.is_empty():
            self.__head = new
        else:
            curr_node = self.__head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new
    
    def transversal(self):
        curr_node = self.__head
        while curr_node != None:
            print(f"|{curr_node.data}|->", end="")
            curr_node = curr_node.next
    
    def remove(self, value):
        curr_node = self.__head
        while curr_node.data != value and curr_node.next != None:
            curr_node = curr_node.next
        if curr_node.data == value:
            