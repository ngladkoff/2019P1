class Semana:
    def __init__(self, lunes, miercoles, viernes):
        self.lunes= lunes
        self.miercoles= miercoles
        self.viernes= viernes
    def __repr__(self):
        return "[" + str(self.lunes) + ", " + str(self.miercoles) + ", " + str(self.viernes) + "]"

# Repaso matrices
produccion = [[50,15,20],[20,10,15],[25,25,25],[15,10,20]]
semanas= [Semana(0,0,0) for i in range(4)]

aux= []

# intercambiar semana 2 con semana 3
aux = produccion[1]
produccion[1]= produccion[2]
produccion[2] = aux

# intercambiar M con V
aux2= 0
for i in range(0,4):
    aux2= produccion[i][2]
    produccion[i][2] = produccion[i][1]    
    produccion[i][1] = aux2
    
for s in range(0,4):
    semanas[s]= Semana(produccion[s][0], produccion[s][1], produccion[s][2])

print(semanas)


print ("L   M   V")
for j in range(0,4):
    for i in range(0,3):
        print(produccion[j][i], end=" ")
    print("")
    
# L = 0
# M = 1
# V = 2
    
suma= [0,0,0]
promedio = [0,0,0]
contador= [0,0,0]

for dia in range(0,3):
    for j in range(0,4):
        suma[dia]= suma[dia] + produccion[j][dia]
        contador[dia]= contador[dia] + 1

for dia in range(0,3):
    promedio[dia] = suma[dia]/contador[dia]

for dia in range(0,3):
    print (promedio[dia])
    
mayor = 0
for dia in range(0,3):
    if promedio[dia] > promedio[mayor]:
        mayor= dia
    
def DiaATexto(dia):
    if dia == 0:
        return "Lunes"
    if dia == 1:
        return "Miercoles"
    if dia == 2:
        return "Viernes"

print("Mayor: ", DiaATexto(mayor))