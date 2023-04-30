cantidad = int(input("Cantidad: "))

num = 0
pares = []
impares = []

while cantidad > 0:
    num = num + 1
    cantidad = cantidad - 1
    numeros = int(input(f"Numero {num}: "))
    if numeros % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print("\nR E S U L T A D O S")
print("=======================")
print(f"Suma de los num. pares es.....: {sum(pares)}")
print(f"Suma de los num. impares es...: {sum(impares)}")
