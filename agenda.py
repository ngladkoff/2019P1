# AGENDA

class Contacto:
    def __init__(self, id, nombre, apellido, telefono):
        self.id= id
        self.nombre= nombre
        self.apellido= apellido
        self.telefono= telefono
    def __repr__(self):
        return "{0} - {1} {2}".format(self.id, self.nombre, self.apellido)

listaContactos = []
listaContactos.append(Contacto(1, "Juan", "Perez", "1234"))
listaContactos.append(Contacto(2, "Alberto", "Perez", "1234"))
listaContactos.append(Contacto(3, "Carlos", "Gomez", "1234"))


proximoID= 4

op= 0
txtMenu= """
****************************************
****************************************
**                                    **
**              MENU                  **
**     1- Agregar Contacto            **
**     2- Borrar Contacto             **
**     3- Editar Contacto             **
**     4- Buscar Contacto             **
**     5- Salir                       **
**                                    **
****************************************
****************************************
"""

def AltaContacto(lstCont, proximoID):
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Telefono: ")
    nuevoContacto = Contacto(proximoID, nombre, apellido, telefono) 
    lstCont.append(nuevoContacto)    
    proximoID = proximoID + 1
    return proximoID

def BajaContacto():
    pass

def EditarContacto():
    pass

def BuscarContacto(lstContactos):
    
    apellido = input("Ingrese apellido: ")
    
    encontrado = False
    for i in range(0, len(lstContactos)):
        c= lstContactos[i]
        if c.apellido == apellido:
            print("{0} {1}: {2}".format(c.nombre, c.apellido, c.telefono))
            encontrado= True
    
    if encontrado == False:
        print("No se encontraron contactos con el apellido indicado")
    
    

while (op != 5):
    print(txtMenu)
    op= int(input("Ingrese opción: "))
    if (op == 1):
        proximoID= AltaContacto(listaContactos, proximoID)
    if (op == 2):
        BajaContacto()
    if (op == 3):
        EditarContacto()
    if (op == 4):
        BuscarContacto(listaContactos)

# Salir
