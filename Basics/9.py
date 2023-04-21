cantidad = int(input("Ingrese la cantidad de productos comprados: "))

docenas = cantidad // 12

precio_unitario = 10

monto_parcial = cantidad * precio_unitario

if docenas > 3:
    descuento = 0.15 * monto_parcial
else:
    descuento = 0.1 * monto_parcial

monto_a_pagar = monto_parcial - descuento

if docenas > 3:
    unidades_obsequio = 5
else:
    unidades_obsequio = 0

print("Monto parcial de la compra:", monto_parcial)
print("Descuento:", descuento)
print("Monto a pagar:", monto_a_pagar)
print("Unidades de obsequio:", unidades_obsequio)
