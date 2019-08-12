# TP1 EJ1

def Mayor(n1, n2, n3):
    #Buscar mayor
    if n1 > n2:
        if n1 > n3:
            return n1
    if n2 > n1:
        if n2 > n3:
            return n2
    if n3 > n1:
        if n3 > n2:
            return n3
    #No encontrado
    return -1

nro1=int(input("Ingrese nro 1:"))
nro2=int(input("Ingrese nro 2:"))
nro3=int(input("Ingrese nro 3:"))

rta= Mayor(nro1, nro2, nro3)

if rta == -1:
    print("No hay nro mayor")
else:
    print("Mayor: ", rta)
    


