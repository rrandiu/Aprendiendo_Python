while True:
    lado1 = int(input("Ingrese la longitud del primer lado: "))
    lado2 = int(input("Ingrese la longitud del segundo lado: "))
    lado3 = int(input("Ingrese la longitud del tercer lado: "))

    #https://www.diferenciador.com/tipos-de-triangulos/
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        print("R E S U L T A D O S \n===================\n")
        print(f"Lado 1..: {lado1} \nLado 2..: {lado2} \nLado 3..: {lado3} \nEstado..: El triangulo si existe")
        if lado1 == lado2 == lado3:
            print("Tipo....: Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Tipo....: Isosceles")
        else:
            print("Tipo....: Escaleno")
    else:
        print("R E S U L T A D O S \n===================\n")
        print(f"Lado 1..: {lado1} \nLado 2..: {lado2} \nLado 3..: {lado3} \nEstado..: El triangulo no existe")
