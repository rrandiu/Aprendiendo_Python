discos = {"Latin Disco": 16.30,
          "Rock": 23.40, "Pop": 27.80,
          "Salsa": 19.50}

cliente = input("Nombre del Cliente: ")
genero = input("Ingrese el Genero: ")
cantidad = int(input("Cuantos desea?: "))
if cantidad <= 3:
    print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
    print(f"Precio............: S/ {discos.get(genero)}")
    print(f"Importe  : S/ {round(discos.get(genero) * cantidad, 2)}")
    print(f"Descuento : S/ 00.0")
    print(f"Importe  a pagar: {round(discos.get(genero) * cantidad, 2)}")
    if genero == "Rock" or "Pop":
        print("Obsequio   : Poster")
    else:
        print("Obsequio   : Ninguno")
elif cantidad > 3:
    print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
    print(f"Precio............: S/ {discos.get(genero)}")
    importe = round(discos.get(genero) * cantidad, 2)
    print(f"Importe  : S/ {importe}")
    print(f"Descuento : {importe * 0.052}")
    print(f"Importe  a pagar: {round(discos.get(genero) * cantidad, 2)}")
    if genero == "Rock" or "Pop":
        print("Obsequio   : Poster")
    else:
        print("Obsequio   : Ninguno")
