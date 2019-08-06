def CalcularDescuento(imp):
    
    if imp > 1000:
        imp = imp * 0.90
    elif imp > 500:
        imp = imp * 0.95
    
    return imp


# importe = int(input("Ingrese importe: "))

# importeConDto = CalcularDescuento(importe)
    
# print ("Importe: ", importeConDto)

edades= [0] * 20
for i in range(0,20):
    edades[i]= i * 2
    
print (edades)

for f in range(0,20):
    print("Edad: ", edades[f])

    
    
