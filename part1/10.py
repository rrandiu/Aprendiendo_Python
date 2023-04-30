import random

numero = random.randint(1, 20)
print("El número aleatorio es:", numero)

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

if numero % 5 == 0:
    print("El número es múltiplo de 5")
else:
    print("El número no es múltiplo de 5")
