#TP3 Ej 1

def imprimir(m):
    for fila in range(0,3):
        for columna in range(0,3):
            print('{:4d}'.format(m[fila][columna]), end='')
        print()

def Transpuesta(m):
    for f in range(0,3):
        for c in range(0,3):
            if c>f:
                a= m[f][c]
                m[f][c]= m[c][f]
                m[c][f]= a
        
def IntercambiarFilaXColumna(m, n):
    
    aux=[0] * 3
    
    for i in range(0,3):
        aux[i]= m[n][i]
        
    for j in range(0,3):
        m[n][j]= m[j][n]
        
    for k in range(0,3):
        m[k][n]= aux[k]
    
matriz= [[1,2,3], [4,5,6], [7,8,9]]
imprimir(matriz)
#IntercambiarFilaXColumna(matriz, 1)
Transpuesta(matriz)
imprimir(matriz)

#Punto f:




#Punto E