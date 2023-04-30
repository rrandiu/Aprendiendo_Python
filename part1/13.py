# Pedir al usuario el número de horas trabajadas y el turno de trabajo
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
turno_trabajo = input("M: Mañana \nT: Tarde \nN: Noche \nIngrese el turno de trabajo: ")

# Calcular el salario bruto según el turno de trabajo
if turno_trabajo == "M":
    salario_bruto = horas_trabajadas * 37.5
elif turno_trabajo == "T":
    salario_bruto = horas_trabajadas * 37.5 * 1.2
else:
    salario_bruto = horas_trabajadas * 37.5 * 1.35

# Calcular el descuento y el salario neto si el turno es de noche
if turno_trabajo == "N":
    if salario_bruto >= 2000 and salario_bruto <= 5000:
        descuento = salario_bruto * 0.12
    elif salario_bruto > 5000:
        descuento = salario_bruto * 0.19
    else:
        descuento = 0
    salario_neto = salario_bruto - descuento
else:
    salario_neto = salario_bruto

# Imprimir los datos del trabajador
print("Turno de trabajo:", turno_trabajo)
print("Horas trabajadas:", horas_trabajadas)
print("Salario bruto: S/ ", salario_bruto)
print("Salario neto: S/ ", salario_neto)
