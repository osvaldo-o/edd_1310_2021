
class PriorityQueue:
    def __init__( self):
        self.__cola = list()

    def is_empty( self):
        return len(self.__cola) == 0
    
    def length( self):
        return len(self.__cola)

    def enqueue( self, prioridad, valor):
        if not self.__hay_prioridad__(prioridad):
            self.__cola.append((prioridad, valor))
            for i in range(self.length()):
                pos = i
                aux = self.__cola[i]
                while pos > 0 and self.__cola[pos-1] > aux:
                    self.__cola[pos] = self.__cola[pos-1]
                    pos-=1
                self.__cola[pos] = aux
        else:
            pos = self.__hay_prioridad__(prioridad)
            self.__cola.insert(pos, (prioridad, valor))

    def __hay_prioridad__(self, prioridad):
        pos = 0
        for elem in self.__cola:
            if elem[0] > prioridad:
                return pos
            pos+=1
        return False
    
    def to_string( self):
        for elem in self.__cola:
            print(f"|{elem}|-",end="")

