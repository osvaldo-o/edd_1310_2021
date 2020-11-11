from Array2D import Array2D

class JuegoDeLaVida:
    CELULA_VIVA = 1
    CELULA_MUERTA = 0

    def __init__( self, rens, cols, generaciones, poblacion):
        self.__rens = rens
        self.__cols = cols
        self.__grid = Array2D(rens, cols, 0)
        self.__generaciones = generaciones+1
        for celula in poblacion:
            self.__grid.set_item(celula[0], celula[1], self.CELULA_VIVA)
        
    def get_num_rows( self):
        return self.__grid.get_row_size()

    def get_num_cols( self):
        return self.__grid.get_row_size()

    def set_celula_viva( self, row, col):
        self.__grid.set_item(row, col, self.CELULA_VIVA)

    def get_celula_viva( self, row, col):
        return self.__grid.get_item(row, col)

    def set_celula_muerta( self, row, col):
        self.__grid.set_item(row, col, self.CELULA_MUERTA)

    def get_celula_muerta( self, row, col):
        return self.__grid.get_item(row, col)

    def get_is_viva( self, row, col):
        return self.__grid.get_item(row, col) == self.CELULA_VIVA

    def get_is_muerta( self, row, col):
        return self.__grid.get_item(row, col) == self.CELULA_MUERTA

    def get_numero_vecinos_vivos( self, row, col):
        conteoVivos = 0
        vecinos =[(row, col+1),(row, col-1),(row+1, col),(row+1, col+1),(row+1, col-1),(row-1, col),(row-1, col+1),(row-1, col-1)]#son todas las coordenadas de los vecinos de una celula
        for vecino in vecinos:
            try:
                if self.get_is_viva(vecino[0], vecino[1]):
                    conteoVivos+=1
            except Exception as e:
                conteoVivo+=0
        return conteoVivos

    def evolucionar( self):
        nuevaGeneracion = Array2D(self.__rens, self.__cols, 0)
        for r in range(self.__rens):
            for c in range(self.__cols):
                conteo = self.get_numero_vecinos_vivos(r,c)
                if (self.get_is_viva(r,c)):  
                    if conteo >= 2 and conteo <= 3:
                        nuevaGeneracion.set_item(r , c, self.CELULA_VIVA)
                    if conteo <= 1:
                        nuevaGeneracion.set_item(r, c, self.CELULA_MUERTA)
                    if conteo >= 4:
                        nuevaGeneracion.set_item(r, c, self.CELULA_MUERTA)
                else:
                    if conteo == 3:
                        nuevaGeneracion.set_item(r, c, self.CELULA_VIVA)
        self.__actualizarGrid__(nuevaGeneracion)

    def imprime_grid( self,gen):
        print(f"Generación {gen}")
        gridString = Array2D(self.__rens, self.__cols,"░░")
        for r in range(self.__rens):
            for c in range(self.__cols):
                if self.__grid.get_item(r, c) == 1:
                    gridString.set_item(r, c, "▓▓")
        gridString.to_string()
        self.evolucionar()
                              
    def __actualizarGrid__( self ,nuevaGeneracion: Array2D):
        for r in range(self.__rens):
            for c in range(self.__cols):
                self.__grid.set_item(r, c, nuevaGeneracion.get_item(r,c))

    def jugar(self):
        for generacion in range(self.__generaciones):
            self.imprime_grid(generacion)