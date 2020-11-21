from ListaDoblementeLigada import DoubleLinkedList

l = DoubleLinkedList()
# test append
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.append(50)
l.append(55)
# test transversal
l.transversal()
l.reverse_transversal()
# test find_from
print(f"Buscando a partir de head, la posición del valor 30 es: {l.find_from_head(30)}")
print(f"Buscando a partir de tail, la posición del valor 20 es: {l.find_from_tail(20)}")
# test remove
l.remove_from_head(20)
l.remove_from_tail(40)
l.transversal()
l.reverse_transversal()
# test get size
print(f"El tamaño de la lista es: {l.get_size()}")
