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
        edad = input("Edad del trabajador: ")
        genero = input("Genero del tranajador (Masculino/Femenino): ")
        #
        #M = "Masculino"
        #F = "Femenino"
        #
        tservicio = int(input("Ingrese los años de servicio: "))
        htrabajadas = int(input("Ingrese el numero de hora trabajas: "))
        sueldo = float(input("Ingrese el sueldo del trabajador: "))
        if htrabajadas >= 40:
            sueldo = sueldo + 50
        elif genero == "Femenino":
            if tservicio > 30:
                sueldo = sueldo + 300
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
        for list2 in empresa1:
            print(list2)
    else:
        selection = input("Seleciona una opcion: ") 