"""programa en Python que permita al equipo añadir#, consultar#, actualizar# y 
eliminar# productos del inventario de manera eficiente, así como calcular el valor total# del inventario."""

productos = []

def agregar_producto():
    """Agrega un nuevo producto al inventario"""
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    nuevo_producto = {
        "Nombre del producto": nombre,
        "Precio": precio,
        "cantidad": cantidad    
    }
    productos.append(nuevo_producto)
    print(f"Producto {nombre} agregado al inventario.")

def consultar_producto():
    """Consulta un producto en el inventario"""
    nombre = input("Ingrese el nombre del producto a consultar: ")
    for producto in productos:
        if producto["Nombre del producto"] == nombre:
            print(f"Producto encontrado: {producto}")
            return
    print(f"Producto {nombre} no encontrado en el inventario.")
    
def actualizar_producto():
    """Actualiza un producto en el inventario"""
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["Nombre del producto"] == nombre:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            producto["Precio"] = nuevo_precio
            producto["cantidad"] =  nueva_cantidad
            print(f"Producto {nombre} actualizado")
            return
    print(f"Producto {nombre} no encontrado en el inventario.")
    
def eliminar_producto():
    """Elimina un producto del inventario"""
    nombre = input("Ingrese el nombre del producto a eliminar: ")
    for producto in productos:
        if producto["Nombre del producto"] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado del inventario")
            return
    print(f"Producto {nombre} no encontrado en el inventario.")

def calcular_valor_inventario():
    """Calcula el valor total del inventario"""
    calcular_valor = lambda producto: producto["Precio"] * producto["cantidad"]
    valores = map(calcular_valor, productos)
    total = sum(valores)
    print(f"El valor total del inventario es: {total}")    
        
    
def menu():
    """Muestra el menú de opciones"""
    while True:
        print("\nMenu de opciones:")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_producto()
        elif opcion == "3":
            actualizar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            calcular_valor_inventario()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente nuevamente.")
# Llamar a la función del menú para iniciar el programa
menu()