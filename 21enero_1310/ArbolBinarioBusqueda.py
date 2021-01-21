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

    def search( self, value):
        if self.__root == None:
            return None
        else:
            return self.__search(self.__root, value)
    
    def __search( self, nodo, value):
        if nodo == None:
            return None
        elif nodo.data == value:
            return nodo
        elif value < nodo.data:
            return self.__search(nodo.left, value)
        else:
            return self.__search(nodo.right, value)

    def remove(self, value):
        encontrado = self.search(value)
        if encontrado.left == None and encontrado.right == None: # caso 1
            encontrado = None
        elif (encontrado.left != None and encontrado.right == None) or (encontrado.left == None and encontrado.right != None):
            encontrado = encontrado.left

    def __recorrido_in(self, nodo):
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=", ")
            self.__recorrido_in(nodo.right)
        
    def __recorrido_pos( self, nodo ):
        if nodo:
            self.__recorrido_pos(nodo.left)
            self.__recorrido_pos(nodo.right)
            print(nodo.data, end=", ")
    
    def __recorrido_pre( self, nodo ):
        if nodo:
            print(nodo.data, end=", ")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def trasversal(self, format="inorden"):
        if format == "inorden":
            self.__recorrido_in(self.__root)
        elif format == "preorden":
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            self.__recorrido_pos(self.__root)
        else:
            print("Error, ese formato no existe")
        print("")