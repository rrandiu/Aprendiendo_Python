num = int(input("Ingrese un numero entre 1 y 10: "))

while num < 1 or num > 10:
    print("Numero incorrect, solo entre 1 y 10.")
    num = int(input("Ingrese un numero entre 1 y 10: "))

print(f"{num} es correcto")