# Alumnos Random
import random

class Alumno:
    def __init__(self, lu, nombre):
        self.lu= lu
        self.nombre= nombre
    def __repr__(self):
        return "{0} - {1}".format(self.lu, self.nombre)

listaAlumnos = []

with open('BBDD1.csv', 'r', encoding='ansi') as arch:
    for linea in arch:
        al= linea.split(';')
        if al[0] != '':
            listaAlumnos.append(Alumno(int(al[1].replace('\n', '')), al[0]))

while (True):
    idx = random.randint(0, len(listaAlumnos) - 1)
    print(listaAlumnos[idx])
    cont = input("Continuar?")
    if (cont == "NO"):
        break;
    