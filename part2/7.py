num = int(input("Enter a number: "))

print(f"Tabla de multiplicacion del {num}")
print("=============================")
for i in range(1, 16):
    tabla = num * i
    print(f"{num}     x     {i}  = {tabla}")