# Productos
producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = precio * unidades
print(f"{producto}: {precio}€ x {unidades} unidades = {coste_total}€")
