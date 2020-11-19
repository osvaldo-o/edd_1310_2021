from listas import LinkedList

test = LinkedList()
test.append(10)
test.append(20)
test.append(30)
test.append(40)
test.transversal()
#prueba metodo get
print(test.get(2))
print(test.get())# regresa el ultimo valor si no damos la posicion 
#prueba metodo add_before
test.add_before(30, 25)
test.transversal()
#prueba metodo add_after
test.add_after(25, 28)
test.transversal()