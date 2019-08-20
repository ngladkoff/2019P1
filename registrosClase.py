class Categoria:
    def __init__(self, nombre):
        self.nombre= nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.categoria= categoria
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return "[%s, %i]" % (self.nombre, self.precio)

 
c1 = Categoria("Almacen")

p1 = Producto("Leche", 50.00, c1)
p2= Producto("Atun", 150, c1)

print(p1)
print(p2)

p1.precio= 60.50

print(p1.nombre)
print(p1.categoria.nombre)
print(p1.precio)

print(p2.nombre)
print(p2.categoria.nombre)
print(p2.precio)


