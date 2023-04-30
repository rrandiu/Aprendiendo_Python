precio_crucero = float(input("Ingrese el precio del crucero: "))
dias_anticipacion = int(input("Ingrese la cantidad de días de anticipación en que pagará: "))
edad = int(input("Ingrese la edad del viajero: "))
otro_crucero = input("¿Ha tomado otro crucero antes? (s/n): ")

descuento = 0.0

if dias_anticipacion >= 17:
    if edad >= 28 and edad <= 30:
        descuento = 0.115
    else:
        descuento = 0.078
elif dias_anticipacion >= 9 and otro_crucero == "s":
    descuento = 0.02

monto_descuento = precio_crucero * descuento
precio_final = precio_crucero - monto_descuento

print("El descuento es de:", monto_descuento)
print("El monto final a pagar es:", precio_final)
