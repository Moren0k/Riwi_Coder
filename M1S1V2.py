#crear un programa que calcule el costo total de una compra en una tienda.

#Primero paso: Solicitar al usuario que ingrese el nombre del producto.
nombre = input("Ingrese el nombre del producto: ")

while len(nombre) == 0: ##Si el nombre contiene 0 caracteres.
    print("El nombre no puede estar vacío. Intente nuevamente.") ### Mostramos un mensaje de error.
    nombre = str(input("Ingrese el nombre del producto: ")) ####Pedimos nuevamente el nombre del producto.
print("El nombre del producto es:", nombre) #####Mostramos el nombre del producto.

#Segundo paso: Solicitar al usuario que ingrese el precio del producto.
precio = input("Ingrese el precio del producto: ") ##Precio del producto.

while not precio > 0: ##Mientras el precio no sea mayor que 0.
    print("El precio debe ser un número positivo. Intente nuevamente.") ### Mostramos un mensaje de error.
    precio = input("Ingrese el precio del producto: ") ####Pedimos nuevamente el precio del producto.
print("El precio del producto es:", precio) #####Mostramos el precio del producto.

#Tercer paso: Solicitar al usuario que ingrese la cantidad del producto.
cantidad = input("Ingrese la cantidad del producto: ") ##Cantidad del producto.
while not cantidad <= 0: ##Mientras la cantidad no sea mayor que 0.
    print("La cantidad debe ser un número positivo. Intente nuevamente.") ### Mostramos un mensaje de error.
    cantidad = input("Ingrese la cantidad del producto: ") ####Pedimos nuevamente la cantidad del producto.
print("La cantidad del producto es:", cantidad) #####Mostramos la cantidad del producto.

#Cuarto paso: Solicitar al usuario que ingrese el descuento del producto.
descuento = input("Ingrese el descuento del producto; ") ##Descuento del producto.
while not descuento < 0 or (descuento) > 100: ##Mientras el descuento no sea menor que 0 o mayor que 100.
    print("El descuento debe ser un número entre 0 y 100. Intente nuevamente.") ### Mostramos un mensaje de error.
    descuento = input("Ingrese el descuento del producto: ") ####Pedimos nuevamente el descuento del producto.
print("El descuento del producto es:", descuento) #####Mostramos el descuento del producto.

