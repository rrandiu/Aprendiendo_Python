while True:
    turno = input("Ingrese un turno (M, T, or N): ")
    if turno == "M":
        print(f"M es correcto, corresponde a Mañana")
    if turno == "T":
        print(f"T es correcto, corresponde a Tarde")
    if turno == "N":
        print(f"N es correcto, corresponde a Noche")
    else:
        print("Turno incorrecto. Ingrese un turno M, T, or N.")