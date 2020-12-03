from backtraking import LaberintoADT

pasillos = ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
lab = LaberintoADT(6, 6, pasillos, (5,2), (2,5))
lab.to_string()

