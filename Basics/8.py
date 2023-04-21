canciones = int(input("Ingrese el número de canciones: "))
partituras = int(input("Ingrese el número de partituras: "))

if canciones >= 7 and canciones <= 10 and partituras == 0:
    print("Músico naciente")
elif canciones >= 7 and canciones <= 10 and partituras >= 1:
    print("Músico estelar")
elif canciones > 10 and partituras > 5:
    print("Músico consagrado")
else:
    print("Músico en formación")
