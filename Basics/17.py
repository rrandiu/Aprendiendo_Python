while True:
    discos = {"Latin Disco": 16.30, "Rock": 23.40, "Pop": 27.80, "Salsa": 19.50}

    cliente = input("Nombre del Cliente: ")
    genero = input("Ingrese el Genero: ")
    cantidad = int(input("Cuantos desea?: "))

    if cantidad <= 3:
        print("====================================")
        print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
        print("Precio............: S/ {:.2f}".format(discos.get(genero)))
        importe = discos.get(genero) * cantidad
        print("Importe...........: S/ {:.2f}".format(importe))
        print("Descuento.........: S/ 00.00")
        print("Importe a pagar...: S/ {:.2f}".format(importe))
        print("Obsequio..........: Ninguno")
    if cantidad >= 4:
        print("====================================")
        print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
        print("Precio............: S/ {:.2f}".format(discos.get(genero)))
        importe = discos.get(genero) * cantidad
        print("Importe...........: S/ {:.2f}".format(importe))
        descuento = importe * 0.052
        print("Descuento.........: S/ {:.2f}".format(descuento))
        subtotal = discos.get(genero) * cantidad
        print("Importe a pagar...: S/ {:.2f}".format(subtotal - descuento))
        print("Obsequio..........: Ninguno")
        print("====================================")
    if cantidad >= 5:
        print("====================================")
        print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
        print("Precio............: S/ {:.2f}".format(discos.get(genero)))
        importe = discos.get(genero) * cantidad
        print("Importe...........: S/ {:.2f}".format(importe))
        descuento = importe * 0.064
        print("Descuento.........: S/ {:.2f}".format(descuento))
        subtotal = discos.get(genero) * cantidad
        print("Importe a pagar...: S/ {:.2f}".format(subtotal - descuento))
        #
        #Preguntar sobre el "AND" y "OR"
        #
        if genero == "Rock" and cantidad >= 6:
            print("Obsequio..........: Poster")
        elif genero == "Pop" and cantidad >= 6:
            print("Obsequio..........: Poster")
        else:
            print("Obsequio..........: Ninguno")
        print("====================================")
    if cantidad >= 10:
        print("====================================")
        print(f"Cliente...........: {cliente} \nGenero............: {genero} \nCantidad..........: {cantidad}")
        print(f"Precio............: S/ {repr(discos.get(genero))}")
        importe = discos.get(genero) * cantidad
        print(f"Importe...........: S/ {importe}")
        print(f"Descuento.........: S/ {importe * 0.082}")
        print(f"Importe a pagar...: {discos.get(genero) * cantidad}")
        #
        #Preguntar sobre el "AND" y "OR"
        #
        if genero == "Rock" and cantidad >= 6:
            print("Obsequio..........: Poster")
        elif genero == "Pop" and cantidad >= 6:
            print("Obsequio..........: Poster")
        else:
            print("Obsequio..........: Ninguno")
        print("====================================")