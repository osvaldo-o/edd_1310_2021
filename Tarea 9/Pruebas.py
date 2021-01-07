from Colas import PriorityQueue

# Provandolo con el ejemplo de la clase
cola = PriorityQueue()
cola.enqueue(4, "Maestre")
cola.enqueue(2, "Niños")
cola.enqueue(4, "Mecánico")
cola.enqueue(3, "Hombres")
cola.enqueue(4, "Vigía")
cola.enqueue(5, "Capitan")
cola.enqueue(4, "Timonel")
cola.enqueue(3, "Mujeres")
cola.enqueue(2, "3era edad")
cola.enqueue(1, "Niñas")
cola.to_string()