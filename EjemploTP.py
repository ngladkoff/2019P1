# Ejemplo TP
from tkinter import *
from tkinter import messagebox

## CREO LOS REGISTROS
class local:
    def __init__(self, id, nombre):
        self.id= id
        self.nombre= nombre
    def __repr__(self):
        return "[Local: %i - %s]" % (self.id, self.nombre)

## CREO LOS VECTORES    
lstLocales = []

for i in range(0,10):
    lstLocales.append(local(i + 1, "Local" + str(i + 1)))

## CREO LA PANTALLA PPAL
def mnuABMLocales():
    winABMLocales()
    # refresh
    messagebox.showinfo(message="Ventana Locales Cerrada", title="Titulo")

def mnuABMVendedores():
    messagebox.showinfo(message="", title="")

def main():
    root.title("Menu")

    lblSeleccione = Label(root, text="Seleccione una opción")
    mnuLocales = Button(root, text="Locales", width=40, command=mnuABMLocales)
    mnuVendedores = Button(root, text="Vendedores", width=40, command=mnuABMVendedores)

    lblSeleccione.pack()
    mnuLocales.pack()
    mnuVendedores.pack()
    root.mainloop()

## CREO LA PANTALLA ABMLOCALES
def mnuAgregarLocal():
    winAddLocal()
    
def winABMLocales():
    abmLocales = Toplevel()
    abmLocales.title("Locales")
    abmLocales.grab_set()
    lblLocales = Label(abmLocales, text="Lista de Locales")
    txtLocales = Text(abmLocales, width=40, height=10)
    btnAgregar = Button(abmLocales, text="Nuevo", width=40, command= mnuAgregarLocal)
    
    texto= ""
    for i in range(0,10):
        texto += lstLocales[i].nombre + "\r\n"
    
    txtLocales.insert(END, texto)
    lblLocales.pack()
    txtLocales.pack()
    btnAgregar.pack()
    root.wait_window(abmLocales)
    
## CREO LA PANTALLA ADD LOCAL
def winAddLocal():
    addLocales = Toplevel()
    addLocales.title("Agregar Local")
    addLocales.grab_set()
    lblAlta= Label(addLocales, text= "Alta Local")
    lblAlta.pack()
    root.wait_window(addLocales)
    
    
## CREO LA PANTALLA ABMVENDEDORES
    



root = Tk()
main()

