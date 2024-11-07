#Fecha de Nacimiento

fecha_de_nacimiento = input("Por favor,introduce tu fecha de nacimiento en formato dd/mm/aa")
fecha = fecha_de_nacimiento.split("/")
dia = fecha[0]
mes = fecha[1]
año = fecha[2]

print("Dia:",dia)
print("Mes:",mes)
print("Año:",año)