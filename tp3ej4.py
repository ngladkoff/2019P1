
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def __repr__(self):
        return "[%s, %i]" % (self.nombre, self.precio)


lstProductos= [Producto("", 0)] * 20

for f in range(0,10):
    lstProductos[f]= Producto("Producto" + str(10-f), f * 100)
    
##print(lstProductos)

lstProductos[5]= Producto("",0)

for i in range(0, 19):
    for j in range(0,19):
        if lstProductos[j].nombre.lower() > lstProductos[j + 1].nombre.lower():
            if lstProductos[j+1].nombre != "":
                aux= lstProductos[j]
                lstProductos[j]= lstProductos[j + 1]
                lstProductos[j + 1]= aux
        elif lstProductos[j].nombre == "":
                aux= lstProductos[j]
                lstProductos[j]= lstProductos[j + 1]
                lstProductos[j + 1]= aux
            

print(lstProductos)
            