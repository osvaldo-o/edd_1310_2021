from colas import BoundedPriorityQueue

pasajeros = ((4,"Maestre"),(2,"Niños"),(4,"Mecanico"),(4, "Mujeres"),(2,"3era edad"),(1,"Niñas"),(3,"Hombres"),(4,"Vigia"),(5,"Capitan"),(4,"Timonel"))
cpa = BoundedPriorityQueue(7)
for pasajero in pasajeros:
    cpa.enqueue(pasajero[0], pasajero[1])
cpa.to_string()
for i in range(len(pasajeros)+1):
    pasajero = cpa.dequeue()
    if pasajero != None:
        print(f"{pasajero} han abandonado el barco")
    else:
        print("El barco ya ha sido evacuado por completo 【ツ】")
cpa.to_string()