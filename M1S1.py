##Soliciamos al usuario que ingrese el nombre de un producto.
nombre = input("Ingrese el nombre del producto: ") ##Nombre del producto
while len(nombre) == 0: ##Mientras el nombre no tenga 0 caracteres.
    print("El nombre no puede estar vacío. Intente nuevamente.")
    nombre = input("Ingrese el nombre del producto: ")
print("El nombre del producto es:", nombre)

##Solicitamos al usuario que ingrese el precio de el producto.
precio = input("Ingrese el precio del producto: ") ##Precio del producto
while not precio.isdigit() <= 0: ##isdigit() verifica si el precio es un número positivo.
    print("El precio debe ser un número positivo. Intente nuevamente.")
    precio = input("Ingrese el precio del producto: ")
print("El precio del producto es:", precio)

##Solicitamos al usuario que ingrese la cantidad de el producto.
cantidad = input("Ingrese la cantidad del producto: ") ##Cantidad del producto
while not cantidad.isdigit() or int(cantidad) <= 0: ##int(cantidad) verifica si la cantidad es un número entero positivo.
    print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
    cantidad = input("Ingrese la cantidad del producto: ")
print("La cantidad del producto es:", cantidad)

##Solicitamos al usuario que ingrese el descuento de el producto.
descuento = input("Ingrese el descuento del producto: ") ##Descuento del producto
while not descuento.isdigit() < 0 or (descuento) > 100:
    print("El descuento debe ser un número entre 0 y 100. Intente nuevamente.")
    descuento = input("Ingrese el descuento del producto: ")
print("El descuento del producto es:", descuento)

total = float(precio) * int(cantidad)##Calulamos el total sin descuento.
descuento = float(descuento) / 100 ##Convertimos el descuento a decimal.
total_con_descuento = total - (total * descuento) ##Calculamos el total con descuento.
print("El total de:", nombre, "sin descuento es:", total) ##Mostramos el total sin descuento.
print("El total con descuento es:", total_con_descuento) ##Mostramos el total con descuento.
descuento_total = total * descuento ##Calculamos el descuento total.
print("El descuento total es:", descuento_total) ##Mostramos el descuento total.