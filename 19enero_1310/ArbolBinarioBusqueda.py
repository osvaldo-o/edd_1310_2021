class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def insert( self, value):
        if self.__root is None:
            self.__root = NodoArbol(value)
        else:
            self.__insert__(self.__root, value)

    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("Ya esta el valor")
        elif value < nodo.data:
            if nodo.left is None:
                nodo.left = NodoArbol(value)
            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right is None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)
    
    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=" , ")
            self.__recorrido_in(nodo.right)

    def trasversal(self, format="inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            print("Recorrido en pre")
        elif format == "posorden":
            print("Posorden")
        else:
            print("Error, ese formato no existe")