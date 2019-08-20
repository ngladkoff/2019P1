# TP Registros Ej 1
from datetime import datetime 

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia= dia
        self.mes= mes
        self.anio= anio
        
    def __repr__(self):
        return "%i/%i/%i" % (self.dia, self.mes, self.anio)

class Horario:
    def __init__(self, hora, minutos, segundos):
        self.hora= hora
        self.minutos= minutos
        self.segundos= segundos
        
    def __repr__(self):
        return "%i:%i:%i" % (self.hora, self.minutos, self.segundos)

def ValidarFecha(fecha):
    if fecha.anio < 1900:
        return False
    
    if fecha.mes > 12 or fecha.mes < 1:
        return False
    
    if fecha.dia > 31 or fecha.dia < 1:
        return False
    
    if fecha.mes == 4 or fecha.mes == 6 or fecha.mes == 9 or fecha.mes == 11:
        if fecha.dia > 30:
            return False
    
    if fecha.mes == 2 and fecha.dia > 29:
        return False
    
    return True

def CargarFecha():
    esValido= False
    while esValido == False:
        dia= int(input("Dia: "))
        mes= int(input("Mes: "))
        anio= int(input("Año: "))
        f= Fecha(dia,mes,anio)
        esValido= ValidarFecha(f) 
        if esValido == False:
            print("Fecha no valida")
    return f



f1 = Fecha(11,6,2019)
print(f1)

h1= Horario(11,30,20)
print(h1)

listaFechas = [Fecha(0,0,0)] * 3

"""
for i in range(0,3):
    listaFechas[i]= CargarFecha()

for i in range(0,3):
    print(listaFechas[i])
"""

fechaActual= Fecha(datetime.now().day, datetime.now().month, datetime.now().year)
horaActual= Horario(datetime.now().hour, datetime.now().minute, datetime.now().second)
print(fechaActual)
print(horaActual)