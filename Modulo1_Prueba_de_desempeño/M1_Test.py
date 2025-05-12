shop_name = ()
inventory = [
    {"title": "p1", "price": 10.0, "quantity": 100},
    {"title": "p2", "price": 15.0, "quantity": 50},
    {"title": "p3", "price": 20.0, "quantity": 30},
    {"title": "p4", "price": 25.0, "quantity": 10},
    {"title": "p5", "price": 30.0, "quantity": 5},
    ]

def def_shop_name():#Nombre de la tienda
    global shop_name
    shop = input("Ingresa el nombre de la tienda: ").strip()
    shop_name = (shop,)
def_shop_name()

def validate_price():#Funcion para verificar que el precio sea correcto
    while True:
        price = input("Introduzca el precio del producto:")
        if not price:
            print("\n---El campo no puede estar vacío. Por favor, introduzca un número.")
            continue
        try:
            price = float(price)
            if price > 0:
                return price
            else:
                print("\n---Debes ingresar un número positivo.")
        except ValueError:
            print("\n---¡ERROR! Está introduciendo datos no válidos. Introduzca un número válido.")

def validate_quantity():#Funcion para verificar que la cantidad sea correcta
    while True:
        quantity = input("Introduzca la cantidad del producto: ")
        if not quantity:
            print("\n---El campo no puede estar vacío. Por favor, introduzca un número.")
            continue
        try:
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                print("\n---Debes ingresar un número positivo.")
        except ValueError:
            print("\n---¡ERROR! Está introduciendo datos no válidos. Introduzca un número válido.")
            
def add():#Agregar Productos
    """Nombre, Precio y Cantidad Disponible"""
    while True:
        try:
            title = input("Ingresa el nombre de el producto: ")
            if not title:
                print("¡ERROR! Este espacio no puede estar vacío.")
                continue
            
            price = validate_price()
            quantity = validate_quantity()
            
            new_product = {"title":title, "price":price, "quantity":quantity}
            inventory.append(new_product)
            print(f"El producto {title} Se agregó exitosamente al inventario.")      
            break
        except:
            print("¡ERROR!")

    
def search():#Buscar Producto
    """Buscar un producto por su nombre y
    Mostrar sus detalles(Nombre, Precio, Cantidad)"""
    while True:
        search_product = input("Ingresa el nombre de el producto que quieres buscar: ").strip().lower()
        for i in inventory:
            if i["title"] == search_product:
                print("\n--- - ---")
                print(f"\nEl producto {search_product} fue encontrado")
                print(f"--{i}--")
                return
        else:
            print(f"El producto { search_product}no se encuentra en el inventario")

def update():#Actualizar Producto
    """Modificar el precio/cantidad de un producto"""
    while True:
            update_to_product = input("Ingrese el nombre de el producto que desea actualizar: ").strip().lower()
            if not update_to_product:
                print("¡ERROR! Este espacio no puede estar vacío.")
                continue
            
            for i in inventory:
                if i["title"] == update_to_product:
                    new_price = validate_price()
                    new_quiantity = validate_quantity()
                    i["price"] = new_price
                    i["quantity"] = new_quiantity
                    print(f"El producto {update_to_product} se actualizó correctamente")
                    return
            else:
                print(f"El producto {update_to_product} no fue encontrado en el inventario.")
            
def remove():#Eliminar Producto
    """Eliminar un producto que ya no esta disponible"""
    while True:
        try:
            remove_to_product = input("Ingresa el nombre de el producto que deseas eliminar: ").strip().lower()
            if not remove_to_product:
                print("¡ERROR! Este espacio no puede estar vacío.")
                
            for i in inventory:
                if i["title"] == remove_to_product:
                    inventory.remove(i)
                    print(f"El producto {remove_to_product} se eliminó correctamente.")
                    return
                else:
                    print(f"El producto {remove_to_product} no fue encontrado en el inventario.")
        except ValueError:
            print("")
    
def calculate_inventory():#Calcular el valor total de el inventario
    value_calculate = lambda inventory: inventory["price"] * inventory["quantity"]
    value = map(value_calculate, inventory)
    total_value = sum(value)
    print(f"\nEl valor total del inventario es: {total_value}")

def view_inventory():#Ver el inventario completo //FUNCIONA
    """Mostrar el inventario completo de productos"""
    print(f"\n===== El inventario de la tienda {shop_name[0]} =====")
    for (i) in inventory:
        print(i)

def main_menu():
    while True:
        print(f"\n--- Menu Principal De La Tienda {shop_name[0]} ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. valor total del inventario")
        print("6. Ver el inventario")
        print("0. ¡Salir!")
        print("\n--- - ---")
        option = input("Selecciona un opción: ")
        
        if option == "1":
            print("\n--- Agregar Un Producto ---")
            add()
        elif option == "2":
            print("\n--- Buscar Un Producto ---")
            search()
        elif option == "3":
            print("\n--- Actualizar Un Producto ---")
            update()
        elif option == "4":
            print("\n--- Eliminar Un Producto ---")
            remove()
        elif option == "5":
            print("\n--- Valor Total Del Inventario ---")
            calculate_inventory()
        elif option == "6":
            print("\n--- Ver El Inventario ---")
            view_inventory()
        elif option == "0":
            print("\n--- SALISTE DE EL SISTEMA ---")
            break
        else:
            print("\n--- -Opción no válida, inténtelo nuevamente.- ---")
main_menu()