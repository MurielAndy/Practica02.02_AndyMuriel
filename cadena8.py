# Precio de un producto
precio = input("Introduce el precio del producto en euros (con dos decimales):")
division = precio.split(",")

centimos= division[1]
euros= division[0]
print("euros:", euros)
print("centimos:", centimos)
