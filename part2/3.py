suma = 0
promedio = 0
pos = 0
neg = 0

for i in range(1, 6):
    numero = int(input(f"Ingrese el número {i}: "))
    suma += numero
    if numero > 0:
        pos += 1
    else:
        neg += 1

promedio = suma / 5

print("Suma:", suma)
print("Promedio:", promedio)
print(f"Cantidad de num. positivos: {pos}")
print(f"Cantidad de num. positivos: {neg}")
