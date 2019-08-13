# Matrices
filas = 6
col= 3
notas = [[0] * col for i in range(filas)]
x= 1
for fila in range(0,filas):
    for columna in range(0,col):
        notas[fila][columna]= x
        x= x + 1

print (notas)

for fila in range(0,filas):
    for columna in range(0,col):
        print('{:4d}'.format(notas[fila][columna]), end='')
    print()
