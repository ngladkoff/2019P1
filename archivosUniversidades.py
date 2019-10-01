# TP Archivos - Universidades

class Universidad:
    def __init__(self, codigo, nombre, nombreCorto):
        self.codigo= codigo
        self.nombre= nombre
        self.nombreCorto = nombreCorto
    def __repr__(self):
        return "{0} - {1} - {2}".format(self.codigo, self.nombre, self.nombreCorto)

universidades= []
idx= 0
with open('listado-de-instituciones-estatales.csv', 'r', encoding='utf-8') as arch:
    for linea in arch:
        if idx== 0:
            idx = idx + 1
            continue
        
        un= linea.split(';')        
        universidades.append(Universidad(un[0], un[1], un[2]))

for univ in universidades:
    print(univ)
    