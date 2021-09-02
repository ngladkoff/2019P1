# Recursividad

# Cuenta Regresiva
def cuenta_regresiva(nro):
    nro -= 1
    if nro > 0:
        print(nro)
        cuenta_regresiva(nro)
    else:
        print("Fin")

cuenta_regresiva(5)


# Factorial
def fact(n):
    cuenta= 1
    for i in range(1,(n+1)):
        cuenta = cuenta * i
    return cuenta

# definimos funcion factorial
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


## principal
print (factorial(1), " ", fact(1))
print (factorial(2), " ", fact(2))
print (factorial(3), " ", fact(3))
print (factorial(4), " ", fact(4))

# Fibonacci
def fibonacci(n):    
    if n <= 1:
        return 1    
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(0,11):
    print(fibonacci(i), end= " ")
    
print("")

# Hanoi    
def moverTorre(altura, a, b, c):
    if altura == 0:
        return    
    moverTorre(altura-1, a, c, b)
    moverDisco(a, c)
    moverTorre(altura-1, b, a, c)

def moverDisco(desde, hasta):
    print("mover disco de {0} a {1}".format(desde, hasta))
    
moverTorre(4, "A", "B", "C")