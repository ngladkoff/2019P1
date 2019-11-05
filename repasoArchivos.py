# Repaso Archivos

class Alumno:
    def __init__(self, dni_alumno, apellido_alumno, nombre_alumno):
        self.dni= dni_alumno
        self.apellido= apellido_alumno
        self.nombre = nombre_alumno
    def __repr__(self):
        return "{0} - {1}, {2}".format(self.dni, self.apellido, self.nombre)

#lstAlumnos= [Alumno(1,"Gladkoff", "Nicolas"), Alumno(2, "Perez", "Juan"), Alumno(3, "Ape3", "Nomb3")]
lstAlumnos = []



"""
with open("ListaAlumnos.csv", "w") as a1: #, encoding="utf-8"
        for i in range(0,3):
            a1.write(str(lstAlumnos[i].dni) + "|" + lstAlumnos[i].apellido + "|" + lstAlumnos[i].nombre + "\n")
"""        
with open("ListaAlumnos.csv", "r") as a1: #, encoding="utf-8"
    for linea in a1:
        print(linea[0:-1])
        a = linea[0:-1].split("|")
        lstAlumnos.append(Alumno(a[0], a[1], a[2]))


print(lstAlumnos)

