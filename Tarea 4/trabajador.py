class Trabajador:
    PAGO_HORA_EXTRA = 276.5

    def __init__( self, tr):
        self.__num_trabajador = tr[0]
        self.__nombre = tr[1].capitalize()
        self.__paterno = tr[2].capitalize()
        self.__materno = tr[3].capitalize()
        self.__hr_extra = int(tr[4])
        self.__sueldo_base = int(tr[5])
        self.__ANTIGUEDAD = 2020 - int(tr[6])

    def get_ANTIGUEDAD( self):
        return self.__ANTIGUEDAD

    def nom_Completo( self):
        return self.__nombre +" "+ self.__paterno +" "+self.__materno

    def sueldo( self):
        return self.__sueldo_base + (self.__hr_extra*self.PAGO_HORA_EXTRA) + ((self.__sueldo_base/100)*3)*(self.__ANTIGUEDAD)
