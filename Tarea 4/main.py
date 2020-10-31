from arrays import Array
from trabajador import Trabajador

arch = open('junio.dat','rt')
arch.readline()
trabajadores = Array(14)
mayor_an, tr_mayor = 0, ""
menor_an, tr_menor = 0, ""
[trabajadores.set_item(arch.readline().strip().split(','), i) for i in range(14)]
arch.close()
for trabajador in trabajadores:
    empleado = Trabajador(trabajador)
    print(f"{empleado.nom_Completo()} tiene un sueldo de ${empleado.sueldo()}")
    if (empleado.get_ANTIGUEDAD() > mayor_an):
        mayor_an = empleado.get_ANTIGUEDAD()
    elif (empleado.get_ANTIGUEDAD() < menor_an):
       menor_an = empleado.get_ANTIGUEDAD()
for trabajador in trabajadores:
    empleado = Trabajador(trabajador)
    if (empleado.get_ANTIGUEDAD() == mayor_an):
        tr_mayor += f"{empleado.nom_Completo()}, "
    elif(empleado.get_ANTIGUEDAD() == menor_an):
        tr_menor += f"{empleado.nom_Completo()}, "     
print(f"\nLos trabajadores con mayor antiguedad son: {tr_mayor}\nLos trabajadores con menor antiguedad son: {tr_menor}")