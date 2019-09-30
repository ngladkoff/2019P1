# Manejo de Archivos de TEXTO

# open('nombre', 'modo')
# modo:
# r -> solo lectura
# w -> escritura, si existe lo borra
# a -> agregar, agrega al final
# r+ -> abre para leer y escribir
# 

# leer archivo completo
with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
    datos= archivo.read()
    
# leer una linea
with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
    linea= archivo.readline()
    
# leer linea a linea
with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
    for linea in archivo:
        print(linea, end='')

# crear una lista con cada una de las lineas
with open('miArchivo.txt', 'r', encoding="utf-8") as archivo:
    lista = list(archivo)
    
# escribir en un archivo
with open('miArchivo.txt', 'a', encoding="utf-8") as archivo:
    archivo.write('Esto es una prueba\n')

# LECTURA DE ARCHIVOS CSV

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

lista = []

with open('personas-certificadas.csv', 'r', encoding='utf-8') as csv:
    for linea in csv:
        a= linea.split(',')
        lista.append(Alumno(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8]))
        
for i in range(1,10):
    print(lista[i])
