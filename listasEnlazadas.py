# Listas enlazadas

class Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox= prox
    def __repr__(self):
        return self.dato 

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud= 0
    def Agregar(self, dato):
        nodo= Nodo(dato, None)
        nodo.prox= self.primero
        self.primero = nodo
        self.longitud += 1
    def Remover(self):
        segundo= self.primero.prox
        self.primero = segundo
        self.longitud -= 1
    def AgregarAlFinal(self, dato):
        nodo = Nodo(dato, None)
        if self.longitud == 0:
            self.primero = nodo
            self.longitud += 1
        else:
            actual= self.primero
            for i in range(0, self.longitud - 1):
                actual = actual.prox
            ultimo = actual
            ultimo.prox = nodo
            self.longitud += 1


    def RemoverDelFinal(self):
        if self.longitud <= 1:
            self.primero = None
            self.longitud = 0
        else:
            actual= self.primero
            for i in range(0, self.longitud - 2):
                actual = actual.prox
            actual.prox= None
            self.longitud -= 1

    def Imprimir(self):
        nodo = self.primero
        while nodo:
            print(nodo.dato)
            nodo= nodo.prox

v1 = Nodo("Banana", None)
v2 = Nodo("Pera", None)
v1.prox= v2
v3 = Nodo("Manzana", None)
v2.prox= v3



print(v1.dato)
print(v1.prox.dato)
print(v1.prox.prox.dato)

print("----------------------")

lst = ListaEnlazada()
lst.Agregar("N1")
lst.Agregar("N2")
lst.Agregar("N3")

print(lst.primero)
print(lst.primero.prox.prox)

print("----------------------")

lst.Imprimir()

print("----------------------")

#lst.Remover()
#lst.Imprimir()

print("----------------------")

lst.AgregarAlFinal("N4")
lst.Imprimir()
print("----------------------")
lst.RemoverDelFinal()
lst.Imprimir()