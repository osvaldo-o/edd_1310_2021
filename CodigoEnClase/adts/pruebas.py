from arrays import Array

algo = Array(10)
print(algo.get_item(11))
algo.set_item(555, 5)
print(algo.get_item(5))
print(f"El tamaño del arreglo es: {algo.get_length()}")
algo.clear(777)
print("Prueba iterador")
for x in algo:
    print(x)