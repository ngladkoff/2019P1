#Simulacro 1er Parcial
import random

# Ej 1
def IngresarNumero(minimo, maximo, pregunta, error):
    while True:
        try:
            nro= int(input(pregunta))
            
            if nro < minimo or nro > maximo:
                raise Exception(error)
            
            return nro
        except ValueError:
            print(error)
        except Exception as ex:
            print(ex.args[0])
            
# a= IngresarNumero(1, 100, "Ing nro de 1 a 100: ", "Ingreso no valido")

#Ej2
def BusquedaMayorTmp(m):
    diasSemana= ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    periodos= ["Mañana", "1/2dia", "Tarde", "Noche"]
    
    fMayor= 0
    cMayor= 0
    for f in range(0,4):
        for c in range(0,7):
            if m[f][c] > m[fMayor][cMayor]:
                fMayor= f
                cMayor= c
    print("La temperatura mas alta es: ", m[fMayor][cMayor])
    print("el dia ", diasSemana[cMayor])
    print("durante el/la ", periodos[fMayor])
    

temperaturas= [[0] * 7] * 4

for i in range(0,4):
    for j in range(0,7):
        temperaturas[i][j]= random.randint(0,40)

#print(temperaturas)
#BusquedaMayorTmp(temperaturas)

#Ej 3
class Alumno:
    def __init__(self, nombreApellido, edad, carrera, materias):
        self.nombreApellido= nombreApellido
        self.edad= edad
        self.carrera= carrera
        self.materias= materias
    def __repr__(self):
        return "%s %i" % (self.nombreApellido, self.edad)
  
def InformeAlumnos(alumnos):
    for f in range(0,10):
        if alumnos[f].carrera == 3 and alumnos[f].materias > 10:
            print(alumnos[f].nombreApellido)
  
    acumulador=0
    contador= 0
    
    for i in range(0,10):
        if alumnos[i].edad < 21:
            contador = contador + 1
            acumulador= acumulador + alumnos[i].materias
    
    print("Promedio: ", acumulador/contador)
    
    contador = 0
    acumulador = 0
    for i in range(0,10):
        if alumnos[i].carrera == 4:
            contador = contador + 1
            acumulador = acumulador + alumnos[i].edad
    
    print("Promedio edad: ", acumulador/contador)
    print("Cantidad: ", contador)
  
  
lstAlumnos= [Alumno("",0,0,0) for i in range(10)]

for i in range(0,10):
    lstAlumnos[i]= Alumno("Alumno" + str(i+1), random.randint(18, 99), random.randint(1,4), random.randint(0, 25))

# print(lstAlumnos)
InformeAlumnos(lstAlumnos)