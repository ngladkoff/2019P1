#Primer Parcial Tema 1

ambulancias = [[1,2,5,9],[2,2,4,8],[3,4,6,5],[1,4,4,9],[1,6,5,8],[2,3,5,10],[3,5,5,7],[2,4,4,11],[3,6,4,10]]

class ambulancia:
    def __init__(self, nro, servicios, kilometros):
        self.nro= nro
        self.servicios= servicios
        self.kilometros= kilometros
    def __repr__(self):
        return "[%i,%s,%s]" % (self.nro, self.servicios, self.kilometros)

# Ejercicio 1

def CargarListaAmbulancias(vector, lista):
    
    for i in range(0,3):
        lista[i].nro= i + 1
    
    for i in range(0,9):
        pos = vector[i][0] - 1
        lista[pos].servicios = lista[pos].servicios + vector[i][2]
        lista[pos].kilometros = lista[pos].kilometros + vector[i][3]

lstAmbulancias = [ambulancia(0,0,0) for i in range(3)]
CargarListaAmbulancias(ambulancias,lstAmbulancias)
print(lstAmbulancias)

# Ejercicio 2

posMayor= 0
for i in range(0,9):
    if (ambulancias[i][3] / ambulancias[i][2]) > (ambulancias[posMayor][3]/ambulancias[posMayor][2]):
        posMayor= i

print("Mayor km/s -> día: ", ambulancias[posMayor][1], " móvil: ", ambulancias[posMayor][0])

# Ejercicio 3

def IngresarDia():
    while True:
        try:
            nro= int(input("Ingrese el día: "))
            if nro < 1 or nro > 31:
                raise Exception("Ingrese día entre 1 y 31")
            return nro
        except ValueError:
            print("Ingrese un numero")
        except Exception as ex:
            print(ex.args[0])
            
dia = IngresarDia()
print("Dia: ", dia)

# Ejercicio 4

cantSrv= 0
posMayor= 0

for i in range(0,9):
    if ambulancias[i][1] == dia:
        if ambulancias[i][2] > cantSrv:
            cantSrv= ambulancias[i][2]
            posMayor= i
            
print("El móvil con mayor cantidad de servicios el día: ", dia, " es el nro.: ", ambulancias[posMayor][0])

# Ejercicio 5

def MayorCantKm(lista):
    posMayor= 0
    for i in range(0,3):
        if lista[i].kilometros > lista[posMayor].kilometros:
            posMayor = i
    return posMayor

mayor= MayorCantKm(lstAmbulancias)
print("El movil que recorrió mayor cantidad de km es: ", lstAmbulancias[mayor].nro)
    

