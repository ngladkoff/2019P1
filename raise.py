try:
    nro= int(input("nro:"))
    if nro < 0:
        raise Exception("Atención!!", "No se admiten nros neg")
except ValueError as ve:
    print(ve)
    print("ingrese un dato numerico")
except Exception as ex:
    print(ex.args[0])
    print(ex.args[1])
    
