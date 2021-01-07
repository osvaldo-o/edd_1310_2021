from colas import BoundedPriorityQueue

maestres = {"prioridad":4, "descripcion":"Maestre", "Personas":["Juan P, Diego H"]}
niños = {"prioridad":2, "descripcion":"Niños", "Personas":["Santi H, Angel L"]}
mecanicos = {"prioridad":4, "descripcion":"Mecanicos", "Personas":["Diana T, Mario Z"]}

cpa = BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'],maestres)
cpa.enqueue(niños['prioridad'],niños)
cpa.enqueue(mecanicos['prioridad'],mecanicos)
cpa.to_string()