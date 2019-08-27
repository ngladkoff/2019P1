while True:
    try:
        nro = int(input("ingrese un numero:"))
        print("Sin Error")
        break
    except ValueError:
        print("El dato ingresado no es un numero")
    except:
        print("no se q paso!!")
print("fin")

