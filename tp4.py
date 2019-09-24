# TP4 - Cadenas de caracteres
# EJ1
def EsCapicua(cadena):
    
    idx1= 0
    idx2= len(cadena) - 1
    
    while (idx1<idx2):
        if (cadena[idx1] != cadena[idx2]):
            return False
        idx1 = idx1 + 1
        idx2 = idx2 - 1

    return True


print(EsCapicua("NEUQUEN"))
print(EsCapicua("NEAQUEN"))

#EJ 2
print("{0:^40}".format("HolaMundo"))

#EJ 3
claveMaestra = 19283746
clave1= 0
clave2= 0
txtClvMaestra = str(claveMaestra)
txtClave1= ""
txtClave2= ""
for i in range(0, len(txtClvMaestra)):
    if i % 2 == 0:
        txtClave1 = txtClave1 + txtClvMaestra[i]
    else:
        txtClave2 = txtClave2 + txtClvMaestra[i]
        
clave1 = int(txtClave1)
clave2= int(txtClave2)

print(clave1)
print(clave2)

# EJ 6

def ExtraerSubcadena(cadena, inicio, cantidad):
    
    if (inicio + cantidad > len(cadena)):
        print("Error")
        return ""
    
    return cadena[inicio: inicio + cantidad]
    

print(ExtraerSubcadena("Apto para instalaciones electricas", 50, 4))


