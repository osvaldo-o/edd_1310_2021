from Ejercicios import pila_posicion_media_rec, contador_reversible_rec
from pila import Stack

print("Prueba ejercicio 3:")
cuenta_regresiva = contador_reversible_rec(3)
print("")

print("Prueba ejercicio 2:")
pila = Stack()
pila.push(2)
pila.push(8)
pila.push(4)
pila.to_string()
elem_medio, pila = pila_posicion_media_rec(pila, pila.length())
print(f"El elemento medio de la pila es {elem_medio} y la pila queda asi:")
pila.to_string()
