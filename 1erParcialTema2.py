#Primer Parcial Tema 2

empleados=[[1,2,9,800],[2,2,7,700],[3,4,11,400],[1,4,7,800],[1,6,9,700],[2,3,9,900],[3,5,9,600],[2,4,7,1000],[3,6,7,900]]

class empleado:
    def __init__(self, nro, cantidad, importe):
        self.nro= nro
        self.cantidad= cantidad
        self.importe= importe
    def __repr__(self):
        return "[%i,%s,%s]" % (self.nro, self.cantidad, self.importe)

# Ejercicio 1

def CargarListaEmpleados(vector, lista):
    
    for i in range(0,3):
        lista[i].nro= i + 1
    
    for i in range(0,9):
        pos = vector[i][0] - 1
        lista[pos].cantidad = lista[pos].cantidad + vector[i][2]
        lista[pos].importe = lista[pos].importe + vector[i][3]

lstEmpleados = [empleado(0,0,0) for i in range(3)]
CargarListaEmpleados(empleados,lstEmpleados)
print(lstEmpleados)

# Ejercicio 2

posMayor= 0
for i in range(0,9):
    if (empleados[i][2]) > (empleados[posMayor][2]):
        posMayor= i

print("Mayor cant. Ventas -> día: ", empleados[posMayor][1], " empleado: ", empleados[posMayor][0])

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

mayorImp= 0
posMayor= 0

for i in range(0,9):
    if empleados[i][1] == dia:
        if empleados[i][3] > mayorImp:
            mayorImp= empleados[i][3]
            posMayor= i
            
print("El empleado con mayor importe vendido el día: ", dia, " es el nro.: ", empleados[posMayor][0])

# Ejercicio 5

def MayorImporte(lista):
    posMayor= 0
    for i in range(0,3):
        if lista[i].importe > lista[posMayor].importe:
            posMayor = i
    return posMayor

mayor= MayorImporte(lstEmpleados)
print("El empleado con mayor importe vendido es: ", lstEmpleados[mayor].nro)
    
