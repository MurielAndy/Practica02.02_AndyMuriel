#Cesta de la compra

productos = input("Inserte por favor los productos que quiere comprar en la cesta")
lista = productos.split(",")
N = int(len(lista))
for i in range (0,N,1):
    print(lista[i])