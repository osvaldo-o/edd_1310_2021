from pilas import Stack

pila = Stack()
pila.push('a')
pila.push('x')
pila.to_string()
pila.push('b')
pila.push('c')
var = pila.pop()
pila.to_string()
print(var)