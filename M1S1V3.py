# Bienvenida
print("Bienvenido al sistema de compra de productos")

# 1. Pedimos el nombre del producto
nombre = input("Ingresa el nombre del producto: ")

# 2. Pedimos el precio unitario
precio = float(input("Ingresa el precio del producto: "))

# 3. Pedimos la cantidad
cantidad = int(input("Ingresa la cantidad que vas a comprar: "))

# 4. Pedimos el porcentaje de descuento
descuento = float(input("Ingresa el descuento (0 si no hay): "))

# 5. Calculamos el precio sin descuento
total_sin_descuento = precio * cantidad

# 6. Calculamos cuánto se descuenta
cantidad_descuento = total_sin_descuento * (descuento / 100)

# 7. Calculamos el total final
total_final = total_sin_descuento - cantidad_descuento

# 8. Mostramos el resultado
print("\n--- RESUMEN DE COMPRA ---")
print("Producto:", nombre)
print("Precio unitario: $", round(precio, 2))
print("Cantidad:", cantidad)
print("Descuento:", str(descuento) + "%")
print("Total a pagar: $", round(total_final, 2))
