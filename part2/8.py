num = int(input("Ingrese una edad entre 18 y 30: "))

while num < 18 or num > 30:
    print("Edad incorrecta, solo entre 18 y 30.")
    num = int(input("Ingrese una edad entre 18 y 30: "))

print(f"{num} es correcto")