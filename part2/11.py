areas = {
    "Jefe": {"Area": "Oficina central", "Sueldo": 2500},
    "Analista": {"Área": "Sistemas", "Sueldo": 2100},
    "Operario": {"Área": "Ventas", "Sueldo": 1950},
    "Empleado": {"Área": "Oficina sucursal", "Sueldo": 1870}}

cargo = input("Ingrese el cargo (Jefe, Analista, Operario o Empleado): ")
while cargo not in areas.keys():
    print("Error: cargo invalido")
    cargo = input("Ingrese el cargo (Jefe, Analista, Operario o Empleado): ")

area = areas[cargo]["Area"]
sueldo = areas[cargo]["Sueldo"]
print(f"Cargo....: {cargo}")
print(f"Area.....: {area}")
print(f"Sueldo...: {sueldo}")
