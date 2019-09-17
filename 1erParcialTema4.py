#Primer Parcial Tema 4

empleados=[[1,2,5,900],[2,2,4,800],[3,4,6,500],[1,4,4,900],[1,6,5,800],[2,3,5,1000],[3,5,5,700],[2,4,4,1100],[3,6,4,1000]]

class empleado:
    def __init__(self, nro, cantidad, importe):
        self.nro= nro
        self.cantidad= cantidad
        self.importe= importe
    def __repr__(self):
        return "[%i,%s,%s]" % (self.nro, self.cantidad, self.importe)

# Ejercicio 1

def CargarListaEmpleados(vector, lista):
    
    for i in range(0,9):
        pos = vector[i][0] - 1
        lista[pos].cantidad = lista[pos].cantidad + vector[i][2]
        lista[pos].importe = lista[pos].importe + vector[i][3]

    for i in range(0,3):
        lista[i].nro= i + 1
        lista[i].importe = lista[i].importe / lista[i].cantidad

lstEmpleados = [empleado(0,0,0) for i in range(3)]
CargarListaEmpleados(empleados,lstEmpleados)
print(lstEmpleados)

# Ejercicio 2

posMayor= 0
for i in range(0,9):
    if (empleados[i][3]) > (empleados[posMayor][3]):
        posMayor= i

print("Mayor importe Ventas -> día: ", empleados[posMayor][1], " empleado: ", empleados[posMayor][0])

# Ejercicio 3

def IngresarNro():
    while True:
        try:
            nro= int(input("Ingrese el empleado: "))
            if nro < 1 or nro > 3:
                raise Exception("Ingrese día entre 1 y 3")
            return nro
        except ValueError:
            print("Ingrese un numero")
        except Exception as ex:
            print(ex.args[0])
            
nro = IngresarNro()
print("Empleado: ", nro)

# Ejercicio 4

mayorCant= 0
posMayor= 0

for i in range(0,9):
    if empleados[i][0] == nro:
        if empleados[i][2] > mayorCant:
            mayorCant= empleados[i][2]
            posMayor= i
            
print("El dia con mayor cantidad de ventas es: ", empleados[posMayor][1])

# Ejercicio 5

def MayorCant(lista):
    posMayor= 0
    for i in range(0,3):
        if lista[i].cantidad > lista[posMayor].cantidad:
            posMayor = i
    return posMayor

mayor= MayorCant(lstEmpleados)
print("El empleado con mayor cantidad de ventas es: ", lstEmpleados[mayor].nro)
    
