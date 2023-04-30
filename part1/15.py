while True:
    edad = int(input("Ingrese la edad: "))
    nombre = input("Ingrese el nombre: ")
    if edad > 15:
        regalo = input("¿Trae regalo? (s/n): ")
        if regalo == "s":
            print(f"Invitado..: {nombre} \nEstado....: Puede ingresar")
        else:
            print(f"Invitado..: {nombre} \nEstado....: No puede ingresar")
    elif edad == 15:
        print(f"Invitado..: {nombre} \nEstado....: Puede ingresar")
    elif edad < 15:
        print(f"Invitado..: {nombre} \nEstado....: No puede ingresar")
