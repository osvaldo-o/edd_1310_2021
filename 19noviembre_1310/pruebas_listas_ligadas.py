from listas import LinkedList

test = LinkedList()
test.append(10)
test.append(20)
test.append(30)
test.append(40)
test.transversal()
test.remove(30)
test.transversal()
test.prepend(50)
test.transversal()
test.add_before(20, 15)
test.transversal()
test.add_after(15, 16)
test.transversal()
test.remove(50)
test.transversal()
print(test.get().data)