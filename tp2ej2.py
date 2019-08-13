# TP2 Ej2
import random

def GenerarListaAleatoria():
    lista= [0] * 50
    for i in range(0, 50):
        lista[i]= random.randint(0,100)
    return lista

def ContieneRepetido(lst):
    repetido= False
    
    for i in range(0,50):
        for j in range(0,50):
            if i != j:
                if lst[i] == lst[j]:
                    repetido = True
    
    return repetido
    
def EstaRepetido(i, lst):
    for j in range(0,50):
        if i != j:
            if lst[i] == lst[j]:
                return True
    return False
    
    
def NoRepetidos(lst):
    rta= [-1] * 50
    x= 0
    
    for i in range(0,50):
        if EstaRepetido(i, lst) == False:
            rta[x] = lst[i]
            x = x + 1
    
    return rta

a= GenerarListaAleatoria()
print(a)
b= ContieneRepetido(a)
print(b)
c = NoRepetidos(a)
print(c)
