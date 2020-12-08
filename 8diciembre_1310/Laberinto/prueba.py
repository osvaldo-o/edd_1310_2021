from backtraking import LaberintoADT

pasillos = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6, 6, pasillos, (5,2), (2,5))

lab.to_string()
# imprimir la Pila
lab.imprimir_camino()

while  not lab.es_salida( lab.get_pos_actual()[0] , lab.get_pos_actual()[1] ) :
    print("probar")
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)

