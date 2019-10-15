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
proximoID= 0

try:
    with open('agenda.csv', 'r') as agenda:
    
        for linea in agenda:
            cnt= linea.split('|')
            listaContactos.append(Contacto(int(cnt[0]), cnt[1], cnt[2], cnt[3]))
            if (int(cnt[0]) > proximoID):
                proximoID = int(cnt[0])

except:
    with open('agenda.csv', 'w') as agenda:
        agenda.write('')
        
proximoID = proximoID + 1

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

def BajaContacto(lstContactos):
    BuscarContacto(lstContactos)
    id= int(input("Ingrese ID a borrar: "))
    
    contactoABorrar= Contacto(0,"","","")
    encontrado= False
    for i in range(0,len(lstContactos)):
        if lstContactos[i].id== id:
            contactoABorrar= lstContactos[i]
            encontrado= True
            break
    if encontrado == True:
        lstContactos.remove(contactoABorrar)

def EditarContacto(lstContactos):
    BuscarContacto(lstContactos)
    # idx = BuscarID()
    id= int(input("Ingrese ID a editar: "))
    
    contactoAEditar= Contacto(0,"","","")
    encontrado= False
    for i in range(0,len(lstContactos)):
        if lstContactos[i].id== id:
            # lstContactos[i].nombre = input("Ingrese nombre: ")
            contactoAEditar= lstContactos[i]
            encontrado= True
            break
    if encontrado == True:
        print("{3} - {0} {1}: {2}".format(contactoAEditar.nombre, contactoAEditar.apellido, contactoAEditar.telefono, contactoAEditar.id))
        contactoAEditar.nombre = input("Ingrese nuevo nombre: ")
        contactoAEditar.apellido= input("Ingrese nuevo apellido: ")
        contactoAEditar.telefono= input("Ingrese nuevo telefono: ")
        
    

def BuscarContacto(lstContactos):
    
    apellido = input("Ingrese apellido: ")
    
    encontrado = False
    for i in range(0, len(lstContactos)):
        c= lstContactos[i]
        if c.apellido == apellido:
            print("{3} - {0} {1}: {2}".format(c.nombre, c.apellido, c.telefono, c.id))
            encontrado= True
    
    if encontrado == False:
        print("No se encontraron contactos con el apellido indicado")
    
    

while (op != 5):
    print(txtMenu)
    op= int(input("Ingrese opción: "))
    if (op == 1):
        proximoID= AltaContacto(listaContactos, proximoID)
        input("Presione Enter para continuar...")
    if (op == 2):
        BajaContacto(listaContactos)
        input("Presione Enter para continuar...")
    if (op == 3):
        EditarContacto()
        input("Presione Enter para continuar...")
    if (op == 4):
        BuscarContacto(listaContactos)
        input("Presione Enter para continuar...")

# Salir
with open('agenda.csv', 'w') as agenda:
    for i in range(0, len(listaContactos)):
        agenda.write("{0}|{1}|{2}|{3}\n".format(listaContactos[i].id, listaContactos[i].nombre, listaContactos[i].apellido, listaContactos[i].telefono))
