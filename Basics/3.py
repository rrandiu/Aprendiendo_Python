while True:
    edad = int(input("Ingrese la edad de la persona: "))

    if edad < 0:
        print("La edad ingresada no es valida. Por favor, ingrese una edad valida.")
    elif edad == 0:
        print("La edad debe ser mayor que cero. Por favor, ingrese otra edad.")
    elif edad >= 60:
        print("Adulto Mayor")
    elif edad >= 30:
        print("Adulto")
    elif edad > 15:
        print("Juventud")
    else:
        print("Niñez")

