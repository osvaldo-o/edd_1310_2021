from pila import Stack

def contador_reversible_rec(n):
    if n > -1:
        print(n,end="-")
        contador_reversible_rec(n-1)

# Sacar de un ADT pila el valor en la posición media.
def pila_posicion_media_rec(pila, size, aux=Stack()):
    if pila.length() > medio(size):
        aux.push(pila.pop())
        return pila_posicion_media_rec(pila, size)
    else:
        elem = pila.pop()
        [pila.push(aux.pop()) for i in range(aux.length())]
        return elem, pila

def medio(size):
    if type(size/2) != float:
        return size/2
    else:
        return int((size/2)+0.5)



