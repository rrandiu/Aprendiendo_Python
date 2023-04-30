producto = input("Producto: ")
cantidad = int(input("Ingrese unidades: "))
precio_unitario = float(input("Ingrese el precio: "))

docenas = cantidad // 12



monto_parcial = cantidad * precio_unitario

if docenas >= 3:
    descuento = 0.15 * monto_parcial
else:
    descuento = 0.10 * monto_parcial

monto_a_pagar = monto_parcial - descuento

unidades_obsequio = 0
if docenas >= 3:
    unidades_obsequio = 5
else:
    unidades_obsequio = 0

print("Producto:", producto)
print("Unidades:", cantidad)
print("Docenas:", docenas)
print("Monto parcial de la compra:", monto_parcial)
print("Descuento:", descuento)
print("Monto a pagar:", monto_a_pagar)
print("Unidades de obsequio:", unidades_obsequio)
