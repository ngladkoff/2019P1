#TP5 EJ1

def IngresarNumero():
    correcto= False
    while correcto == False:
        try:
            nro= int(input("Ingrese un nro:"))
            if nro < 0:
                raise Exception("el numero tiene que ser mayor a 0")
            correcto = True
        except ValueError:
            print("No ingreso un dato numerico")
        except Exception as ex:
            print(ex.args[0])
    return nro
    
a=IngresarNumero()
b= IngresarNumero()