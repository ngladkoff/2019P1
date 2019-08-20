# Registros

class Categoria:
    def __init__(self, nombre):
        self.nombre= nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria= categoria
        
    def __repr__(self):
        return "Producto[%s, %i]" % (self.nombre, self.precio)

p = Producto("Leche", 50.00, Categoria("Almacen"))
print(p)

p.nombre= "Cafe"
p.precio= 200

print(p)

print(p.nombre)
print(p.categoria.nombre)
    