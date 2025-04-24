# ========================================
# Sistema básico de compra de productos
# Autor: Jhos Kevin Agudelo Moreno
# Descripción: Solicita datos del producto, aplica validaciones, calcula el total con descuento y muestra un resumen.
# ========================================

# 1. Saludo inicial al usuario para mejorar la experiencia
print("Bienvenido al sistema de compra de productos")

# 2. Solicita el nombre del producto (tipo: string)
nombre = input("Ingresa el nombre del producto: ")

# 3. Solicita el precio unitario del producto (tipo: float)
#    Se valida que no sea un número negativo mediante un bucle while
while True:
    try:
        precio = float(input("Ingresa el precio del producto: "))
        if precio < 0:
            print("El precio no puede ser negativo. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Ingresa un número decimal.")

# 4. Solicita la cantidad de productos a comprar (tipo: int)
#    Se valida que no sea negativo y que sea un número entero
while True:
    try:
        cantidad = int(input("Ingresa la cantidad que vas a comprar: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Ingresa un número entero.")

# 5. Solicita el porcentaje de descuento (tipo: float)
#    También se valida que no sea negativo
while True:
    try:
        descuento = float(input("Ingresa el descuento (0 si no hay): "))
        if descuento < 0:
            print("El descuento no puede ser negativo. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("Entrada no válida. Ingresa un número decimal.")

# 6. Cálculo del total sin descuento
#    Multiplica el precio unitario por la cantidad solicitada
total_sin_descuento = precio * cantidad

# 7. Cálculo del valor monetario del descuento
#    Se aplica el porcentaje ingresado al total sin descuento
cantidad_descuento = total_sin_descuento * (descuento / 100)

# 8. Cálculo del total final a pagar
#    Se resta el descuento al total sin descuento
total_final = total_sin_descuento - cantidad_descuento

# 9. Presentación del resumen de la compra
#    Se formatea la salida para mostrar solo 2 decimales (formato dinero)
print("\n--- RESUMEN DE COMPRA ---")
print("Producto:", nombre)
print("Precio unitario: $", (precio))
print("Cantidad:", cantidad)
print("Descuento:", str(descuento) + "%")
print("Total a pagar: $", (total_final))