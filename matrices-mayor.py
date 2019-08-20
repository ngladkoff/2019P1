# MatricesMayor
import random

filas = 5
col= 5

m = [[0] * col for i in range(filas)]

for f in range(0,filas):
    for c in range(0,col):
        m[f][c]= random.randint(0,100)
        
def imprimir(m,f,c):
    for fila in range(0,f):
        for columna in range(0,c):
            print('{:4d}'.format(m[fila][columna]), end='')
        print()







def buscarMayor(m,f,c):
    fmayor = 0
    cmayor = 0
    for fila in range(0,f):
        for columna in range(0,c):
            if m[fila][columna] > m[fmayor][cmayor]:
                fmayor= fila
                cmayor=columna
                
    print ("Mayor: ", m[fmayor][cmayor])
    print ("Fila mayor: ", fmayor)
    print ("Col mayor: ", cmayor)
    
    


imprimir(m, filas, col)
buscarMayor(m,filas,col)
