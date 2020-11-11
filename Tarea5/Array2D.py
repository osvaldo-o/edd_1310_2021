class Array2D:
    def __init__( self, ren, col, valor):
        self.__matriz = [[valor for j in range(col)] for i in range(ren)]
        self.__renglones = ren
        self.__columnas = col

    def get_row_size( self):
        return self.__renglones

    def get_col_size( self):
        return self.__columnas

    def set_item( self, ren, col, dato):
        try:
            self.__matriz[ren][col] = dato 
        except Exception as e:
            print("No exite ese renglon o columna")

    def get_item( self, ren, col):
        try:
            return self.__matriz[ren][col]
        except Exception as e:
            return "No exite ese renglon o columna"

    def clear( self, dato):
        for r in range(self.__renglones):
            for c in range(self.__columnas):
                self.__matriz[r][c] = dato
    
    def to_string( self):
        for r in range(self.__renglones):
            for c in range(self.__columnas):
                print(self.__matriz[r][c], end=" ")
            print()