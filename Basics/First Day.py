"""
#Hola mundo
print("Hola mundo")
#Area dun Triangulo
a = int(input("Ingrese la base: "))
b = int(input("Ingrese la altura: "))
c = a + b
atriangulo = c / 2
print("El area del triangulo es", atriangulo)
"""

monto = float(input("Ingresa el monto: "))

if monto > 100:

    descuento = monto * .10

else:

    descuento = monto * .02

print(f"El descuento aplicado es: ${descuento}")