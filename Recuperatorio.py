# Recuperatorio

# Ejercicio 1
def SumaFila(matriz, fila):
    suma = 0
    for col in range(0,10):
        suma = suma + matriz[fila][col]
    return suma

m = [[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10],[1,2,3,4,5,6,7,8,9,10]]
f = 5
print("Ej1")
resultado = SumaFila(m,5)
print(resultado)

# Ejercicio 2
def BuscarMayor(vector):
    mayor = 0
    for i in range(0, len(vector)):
        if vector[i] > mayor:
            mayor = vector[i]
    return mayor

v = [1,2,3,4,5,60,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
resultado = BuscarMayor(v)
print("Ej2")
print(resultado)

# Ejercicio 3
def BuscarValor(vector, nro):
    contador = 0
    for i in range(0,len(vector)):
        if vector[i] == nro:
            contador += 1
    
    if contador == 0:
        return -1
    else:
        return contador

v = [1,2,2,4,5]
print("Ej 3")
print(BuscarValor(v,6))
print(BuscarValor(v,2))
print(BuscarValor(v,4))

# Ejercicio 4a
produccion = [[1,1,120,3], [1,2,115,5], [1,3,118,6], [1,4,113,2], [1,5,100,2], [2,1,340,18], [2,2,300,16], [2,3,350,18], [2,4,330, 15], [2,5,325, 12]]

nro= int(input("Nro maq: "))
dia= int(input("Dia: "))
print("Ej 4a")
total = 0
defect = 0

for i in range(0, 10):
    if produccion[i][0] == nro and produccion[i][1] == dia:
        total= produccion[i][2]
        defect = produccion[i][3]

print("Total U. Prod.: ", total)
print("Total U. Def.: ", defect)

# Ejercicio 4b
print("Ej 4b")


for maq in range(1,3):
    mayor= 0
    for i in range(0,10):
        if produccion[i][0] == maq :
            if (produccion[i][2] > mayor):
                mayor= produccion[i][2]
    print("Maq ", maq, ": ", mayor)
    
    
    