while True:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    operacion = int(input("1 (Suma) \n2 (Resta) \n3 (Producto) \n4 (División) \n5 (Promedio) \n6 (Mayor), \n7 (Menor) \n8 (Suma de cuadrados) \nIngrese la operación a realizar: "))

    if operacion == 1:
        resultado = num1 + num2
        print("La suma es:", resultado)
    elif operacion == 2:
        resultado = num1 - num2
        print("La resta es:", resultado)
    elif operacion == 3:
        resultado = num1 * num2
        print("El producto es:", resultado)
    elif operacion == 4:
        if num2 == 0:
            print("No se puede dividir entre cero")
        else:
            resultado = num1 / num2
            print("La división es:", resultado)
    elif operacion == 5:
        resultado = (num1 + num2) / 2
        print("El promedio es:", resultado)
    elif operacion == 6:
        resultado = max(num1, num2)
        print("El número mayor es:", resultado)
    elif operacion == 7:
        resultado = min(num1, num2)
        print("El número menor es:", resultado)
    elif operacion == 8:
        resultado = num1**2 + num2**2
        print("La suma de los cuadrados es:", resultado)
    else:
        print("Operación inválida")
