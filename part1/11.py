import random

# Lanzamos tres dados
dados = [random.randint(1, 6) for i in range(3)]

# Contamos cuántos seis obtuvimos
count = dados.count(6)

# Evaluamos el resultado
if count == 3:
    print("Excelente")
elif count == 2:
    print("Muy bien")
elif count == 1:
    print("Regular")
else:
    print("Siga intentando")
