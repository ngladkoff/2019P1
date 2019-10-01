# Manejo de Archivos - Clase

class Alumno:
    def __init__(self, dni_alumno, apellido_alumno, nombre_alumno, provincia_examen,id_provincia, localidad, sede_nombre, sede_direccion, llamado_certificacion):
        self.dni= dni_alumno
        self.apellido= apellido_alumno
        self.nombre = nombre_alumno
        self.provincia= provincia_examen
        self.idProvincia= id_provincia
        self.localidad= localidad
        self.sede= sede_nombre
        self.direccion= sede_direccion
        self.llamado= llamado_certificacion
    def __repr__(self):
        return "{0} - {1}, {2} - {3} - {4}".format(self.dni, self.apellido, self.nombre, self.provincia, self.localidad)


with open('miArchivo.txt', 'r', encoding='utf-8') as arch:
    texto = arch.read()
    #print(texto)
    
with open('miArchivo.txt', 'r', encoding='utf-8') as arch:
    linea1= arch.readline()
    #print(linea1)
    linea2= arch.readline()
    #print(linea2)
  
with open('miArchivo.txt', 'r', encoding='utf-8') as arch:
    for i in range(0,4):
        a=1
        #print(arch.readline())

with open('miArchivo.txt', 'r', encoding='utf-8') as arch:
    for linea in arch:
        print(linea)

lista= []
#with open('miArchivo.txt', 'r', encoding='utf-8') as arch:
#    for linea in arch:
#        lista.append(linea)

alumno= Alumno(1234, "Juan", "Perez", '','','','','','')

#with open('miArchivo.csv', 'w', encoding='utf-8') as arch:
#    arch.write("{0},{1},{2}".format(alumno.dni, alumno.nombre, alumno.apellido))
    
listaAlumnos= []

idx= 0
cba= 0
with open('personas-certificadas.csv', 'r', encoding='utf-8') as arch:
    for linea in arch:
        if idx== 0:
            idx = idx + 1
            continue
        
        al= linea.split(',')
        
        if (al[4] == '14'):
            cba = cba + 1        
        
        listaAlumnos.append(Alumno(al[0], al[1], al[2], al[3], al[4], al[5], al[6], al[7], al[8]))
        
    

for i in range(0, 20):
    print(listaAlumnos[i])

cantBuenosAires = 0
for i in range(0,len(listaAlumnos)):
    if (listaAlumnos[i].idProvincia == '06'):
        cantBuenosAires = cantBuenosAires + 1

print("Cant. BA: ", cantBuenosAires)
print("Cant. cba: ", cba)    