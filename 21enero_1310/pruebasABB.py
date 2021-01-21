from ArbolBinarioBusqueda import BinarySearchTree

abb = BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)

abb.trasversal()
abb.trasversal("preorden")
abb.trasversal("posorden")

print(abb.search(35).data)