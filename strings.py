vocales= "aeiou"
txtHola = "Hola"
txtMundo= "Mundo"
texto = txtHola + " " + txtMundo
print(texto)
contador = 0

for i in range(0,len(texto)):
    if texto[i] in vocales:
        print("vocal")

for i in range(0,len(texto)):
    for f in range(0,5):
        if(texto[i] == vocales[f]):
            contador = contador + 1
         
for j in texto:
    print("-" + j + "-")
         
print(texto[0:])
            
print("vocales: " + str(contador))

variable1 = "5"
variable2 = 4
variable3 = "10.5"
print(type(variable1))
print(type(variable2))
print(int(variable1) + 10) # CAST
print(float(variable3))
print(variable1 + str(variable2))

textoNvo = "Apto para instalaciones electricas"
textocsv = "10|Juan Perez|40001001|7"
lstTexto = textoNvo.split("t")
alumno= textocsv.split("|")
print(lstTexto)
print("Legajo: ", int(alumno[0][0]) * 100)
print("Alumno: ", alumno[1])
print(textocsv)
print(alumno)
print("||".join(alumno))

print(textoNvo.upper())
minusculas= textoNvo.lower()
print(minusculas)
print(textoNvo.replace("a", "@").replace("0", "O"))
print(textocsv.replace("|", ",").replace("Juan", "Carlos"))

print("{0:>6} | {1:15} | {2:^10} | {3}".format("Legajo", "Nombre", "DNI", "Materias Aprobadas"))
print("{0:>6} | {1:15} | {2:010d} | {3:6.3f}".format(alumno[0], alumno[1], int(alumno[2]), float(alumno[3])))
