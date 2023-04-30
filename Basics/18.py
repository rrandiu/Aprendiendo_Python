equalbar = "============================="
leavebar = " J |========= ATRAS ========="
invalid = [equalbar, "    Solo numeros enteros!    ", equalbar]
invalid1 = len(invalid)

import requests
url = 'https://v6.exchangerate-api.com/v6/6c006704ae4031680ffd9318/latest/USD'
response = requests.get(url)
data = response.json()
usd = data['conversion_rates']['PEN']

############################
#      Menu Selection      #
############################
selec1 = [equalbar, "      Selecione el Grupo        ", equalbar,
                    " A |Trabajadores                 ", " B |Aspirantes                 ",
                    equalbar]
list1 = len(selec1)

empresa1 = [equalbar, "     Empresa TA & JC S.A.       ", equalbar]
list2 = len(empresa1)

while True:
    for list1 in selec1:
        print(list1)
    selection = input("Seleciona una opcion: ")
    if selection == "A":
        nombre = input("Nombre del trabajador: ")
        edad = int(input("Edad del trabajador: "))
        genero = input("Genero del tranajador (Masculino/Femenino): ")
        #
        #M = "Masculino"
        #F = "Femenino"
        #
        tservicio = int(input("Ingrese los años de servicio: "))
        htrabajadas = int(input("Ingrese el numero de hora trabajas: "))
        sueldo = float(input("Ingrese el sueldo del trabajador: "))
        sueldo_total = sueldo
        if htrabajadas > 40:
            sueldo_total += 50
            for list2 in empresa1:
                print(list2)
            print(f"Empleado...........: {nombre} \nEdad...............: {edad} años")
            #Se puede aregar el formato
            print(f"Genero.............: {genero} \nTiempo de servicio.: {tservicio} años  \nHoras trabajadas...: {htrabajadas} horas")
            print("Sueldo.............: $ {:.2f}".format(sueldo))
            print("Incrememto.........: $ {:.2f} \nNuevo sueldo.......: $ {:.2f}".format(sueldo_total - sueldo, sueldo_total))
            print("USD -> PEN.........: S/ {:.2f} \nSueldo en soles....: S/ {:.2f}".format(usd, sueldo_total * usd))
        if genero == "Femenino" or edad > 25 and tservicio > 30:
            sueldo_total += 300
            for list2 in empresa1:
                print(list2)
            print(f"Empleado...........: {nombre} \nEdad...............: {edad} años")
            #Se puede aregar el formato
            print(f"Genero.............: {genero} \nTiempo de servicio.: {tservicio} años  \nHoras trabajadas...: {htrabajadas} horas")
            print("Sueldo.............: $ {:.2f}".format(sueldo))
            print("Incrememto.........: $ {:.2f} \nNuevo sueldo.......: $ {:.2f}".format(sueldo_total - sueldo, sueldo_total))
            print("USD -> PEN.........: S/ {:.2f} \nSueldo en soles....: S/ {:.2f}".format(usd, sueldo_total * usd))
        else:
            for list2 in empresa1:
                print(list2)
            print(f"Empleado...........: {nombre} \nEdad...............: {edad} años")
            #Se puede aregar el formato
            print(f"Genero.............: {genero} \nTiempo de servicio.: {tservicio} años  \nHoras trabajadas...: {htrabajadas} horas")
            print("Sueldo.............: $ {:.2f}".format(sueldo))
            print(f"Incrememto.........: $ 00.00 \nNuevo sueldo.......: $ {sueldo}")
            print("USD -> PEN.........: S/ {:.2f} \nSueldo en soles....: S/ {:.2f}".format(usd, sueldo * usd))
    elif selection == "B":
        nombre = input("Nombre del postulante: ")
        edad = int(input("Edad del postulante: "))
        puntaje = int(input("Puntaje del postulante: "))
        if edad >= 21 and puntaje > 85:
            for list2 in empresa1:
                print(list2)
            print(f"Postulante........: {nombre}")
            print(f"Edad..............: {edad}")
            print(f"Puntaje...........: {puntaje}")
            print("Estado............: Contratado")
        else:
            for list2 in empresa1:
                print(list2)
            print(f"Postulante........: {nombre}")
            print(f"Edad..............: {edad}")
            print(f"Puntaje...........: {puntaje}")
            print("Estado............: No Contratado")
    else:
        selection = input("Seleciona una opcion: ")