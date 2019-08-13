# Ventana Login

from tkinter import *
from tkinter import messagebox


def Aceptar(usuario, clave):
    print(usuario, '//', clave)
    messagebox.showinfo(message="Usuario: " + usuario + " // Clave: " + clave, title="Proceso Login...")


root = Tk()
root.title("Login")

varUsuario = StringVar()
varClave = StringVar()


lblUsuario = Label(root, text="Usuario")
txtUsuario = Entry(root, textvariable=varUsuario, width=50)
lblClave = Label(root, text="Clave")
txtClave = Entry(root, textvariable=varClave, width=50)

boton = Button(root, text="Aceptar", command=lambda: Aceptar(varUsuario.get(), varClave.get()))


lblUsuario.pack()
txtUsuario.pack()
lblClave.pack()
txtClave.pack()
boton.pack()
root.mainloop()

