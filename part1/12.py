import random

# Generar 5 números aleatorios entre 10 y 50
numeros = [random.randint(10, 50) for _ in range(5)]

# Calcular el promedio de los números
promedio = sum(numeros) / len(numeros)

# Contar cuántos números son mayores, iguales y menores que el promedio
mayores = 0
iguales = 0
menores = 0

for num in numeros:
    if num > promedio:
        mayores += 1
    elif num == promedio:
        iguales += 1
    else:
        menores += 1

# Imprimir los resultados
print("Los números generados son:", numeros)
print("El promedio es:", promedio)
print("Hay", mayores, "números mayores que el promedio")
print("Hay", iguales, "números iguales al promedio")
print("Hay", menores, "números menores que el promedio")
