def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")


divide(2, 1)
divide(2, 0)




while True:
    try:
        x = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("No es un número válido. Intente nuevamente...")

