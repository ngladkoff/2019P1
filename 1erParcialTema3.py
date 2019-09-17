#Primer Parcial Tema 3

ambulancias=[[1,6,9,18],[2,6,7,16],[3,12,11,10],[1,12,7,18],[1,18,9,16],[2,9,9,20],[3,15,9,14],[2,12,7,22],[3,18,7,20]]

class ambulancia:
    def __init__(self, nro, servicios, kilometros):
        self.nro= nro
        self.servicios= servicios
        self.kilometros= kilometros
    def __repr__(self):
        return "[%i,%s,%s]" % (self.nro, self.servicios, self.kilometros)

# Ejercicio 1

def CargarListaAmbulancias(vector, lista):
    
    for i in range(0,9):
        pos = vector[i][0] - 1
        lista[pos].servicios = lista[pos].servicios + vector[i][2]
        lista[pos].kilometros = lista[pos].kilometros + vector[i][3]

    for i in range(0,3):
        lista[i].nro= i + 1
        lista[i].kilometros = lista[i].kilometros / lista[i].servicios

lstAmbulancias = [ambulancia(0,0,0) for i in range(3)]
CargarListaAmbulancias(ambulancias,lstAmbulancias)
print(lstAmbulancias)

# Ejercicio 2

posMayor= 0
for i in range(0,9):
    if ambulancias[i][3] > ambulancias[posMayor][3]:
        posMayor= i

print("Mayor kms -> día: ", ambulancias[posMayor][1], " móvil: ", ambulancias[posMayor][0])

# Ejercicio 3

def IngresarMovil():
    while True:
        try:
            nro= int(input("Ingrese el movil: "))
            if nro < 1 or nro > 3:
                raise Exception("Ingrese nro entre 1 y 3")
            return nro
        except ValueError:
            print("Ingrese un numero")
        except Exception as ex:
            print(ex.args[0])
            
movil = IngresarMovil()
print("Movil: ", movil)

# Ejercicio 4

cantSrv= 0
posMayor= 0

for i in range(0,9):
    if ambulancias[i][0] == movil:
        if ambulancias[i][2] > cantSrv:
            cantSrv= ambulancias[i][2]
            posMayor= i
            
print("El día con mayor cantidad de servicios el movil: ", movil, " es el dia: ", ambulancias[posMayor][1])

# Ejercicio 5

def MayorCantSrv(lista):
    posMayor= 0
    for i in range(0,3):
        if lista[i].servicios > lista[posMayor].servicios:
            posMayor = i
    return posMayor

mayor= MayorCantSrv(lstAmbulancias)
print("El movil que realizo mayor cantidad de servicios es: ", lstAmbulancias[mayor].nro)
    
