#tp1 ej 4
def ValorTotal(cant, valor):
    valorTotal= valor * cant

    if cant >= 21 and cant <= 30:
        valorTotal= valorTotal* 0.8
    elif cant >= 31 and cant <= 40:
        valorTotal= valorTotal* 0.7
    elif cant > 40:
        valorTotal= valorTotal * 0.6

    return valorTotal

valor= int(input("Valor pasaje: "))
cant= int(input("Cantidad: "))

rta= ValorTotal(cant, valor)
print("Valor total: ", rta)

