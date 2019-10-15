# Ejercicio Integrador
class Departamento:
    def __init__(self, numero, descripcion, mts2, estado, precio):
        self.numero= numero
        self.descripcion= descripcion
        self.mts2 = mts2
        self.estado = estado
        self.precio = precio

    def __repr__(self):
        return "{0}-{1}-{2}".format(self.numero, self.descripcion, self.estado)

def ReservarDpto(departamentos):
    nro= int(input("Ingrese nro de dpto.: "))
    pcio= float(input("Ingrese precio pactado: "))
    encontrado = False
    for i in range(0, len(departamentos)):
        if departamentos[i].numero == nro:
            departamentos[i].estado = 1
            departamentos[i].precio= pcio
            encontrado= True
    if encontrado == False:
        print("No se encontró el departamento")

    

def ExportarDptosLibres(departamentos):
    
    for k in range(0, len(departamentos) -1 ):
        for j in range(0, len(departamentos) -1):
            if (departamentos[j + 1].mts2 < departamentos[j].mts2):
                aux= departamentos[j + 1]
                departamentos[j + 1]= departamentos[j]
                departamentos[j]= aux

    with open('deptos.txt', 'w') as deptos:
        for i in range(0, len(departamentos)):
            if departamentos[i].estado == 0:
                # escribir al archivo
                deptos.write("{0} - {1}: {2}\n".format(departamentos[i].numero, departamentos[i].descripcion, departamentos[i].mts2))            


def CantDptosPorEstado(departamentos):
    cantLibres= 0
    cantReservados= 0
    cantVendidos= 0
    for i in range(0,len(departamentos)):
        c= departamentos[i]
        if c.estado == 0:
            cantLibres += 1
        if c.estado == 1:
            cantReservados += 1
        if c.estado == 2:
            cantVendidos += 1
    print("Libres: ", cantLibres)
    print("Reservados: ", cantReservados)
    print("Vendidos: ", cantVendidos)

def cantDtos(departamentos):
    cantidades= [0] * 3
    for i in range(0, len(departamentos)):
        estado = departamentos[i].estado
        cantidades[estado] = cantidades[estado] + 1
    print("Libres: ", cantLibres)
    print("Reservados: ", cantReservados)
    print("Vendidos: ", cantVendidos)

def CargarCSV(departamentos):
    try:
        with open('deptos.csv', 'r') as deptos:        
            for linea in deptos:
                cnt= linea.split('|')
                departamentos.append(Departamento(int(cnt[0]), cnt[1], int(cnt[2]), int(cnt[3]), float(cnt[4])))
    except:
        with open('deptos.csv', 'w') as deptos:
            deptos.write('')


def GuardarCSV(departamentos):
    with open('deptos.csv', 'w') as deptos:
        for i in range(0, len(departamentos)):
            deptos.write("{0}|{1}|{2}|{3}|{4}\n".format(departamentos[i].numero, departamentos[i].descripcion, departamentos[i].mts2, departamentos[i].estado, departamentos[i].precio))


def menu():
    op = -1
    while op < 0 or op > 5:
        print ("""
###########################################
###########################################
###                                     ###
### M E N U :                           ###
###                                     ###
###           1. RESERVAR DPTO          ###
###           2. EXPORTAR DPTOS LIBRES  ###
###           3. CANT DPTOS POR ESTADO  ###
###           4. CARGAR DATOS CSV       ###
###           5. EXPORTAR DATOS CSV     ###
###           0. SALIR                  ###
###                                     ###
###########################################
###########################################
""")
        try:
            op = int(input("Ingrese opción:"))
            if (op < 0 or op > 5):
                print("Ingrese una opción válida [0-5]")
        except:
            op = -1
    return op

def main():
    departamentos= []

    #departamentos.append(Departamento(1, "Dto1", 90, 0, 120000))
    #departamentos.append(Departamento(2, "Dto2", 90, 0, 120000))
    #departamentos.append(Departamento(3, "Dto3", 90, 0, 120000))

    op= 1
    while op != 0:
        op = menu()
        if op == 0:
            print(departamentos)
            return
        elif op == 1:
            ReservarDpto(departamentos)
        elif op == 2:
            ExportarDptosLibres(departamentos)
        elif op == 3:
            CantDptosPorEstado(departamentos)
        elif op == 4:
            CargarCSV(departamentos)
        elif op == 5:
            GuardarCSV(departamentos)
    
main()