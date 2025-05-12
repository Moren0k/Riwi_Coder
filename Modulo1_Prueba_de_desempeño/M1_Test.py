shop_name = ()
inventory = [
    {"title": "product 1", "price": 10.0, "quantity": 100},
    {"title": "product 2", "price": 15.0, "quantity": 50},
    {"title": "product 3", "price": 20.0, "quantity": 30},
    {"title": "product 4", "price": 25.0, "quantity": 10},
    {"title": "product 5", "price": 30.0, "quantity": 5}
    ]

def shop_name():#Nombre de la tienda //FUNCIONANDO
    """Definir y guardar el nombre de la tienda"""
    global shop_name
    name =input("Ingresa el nombre de la tienda: ").strip()
    shop_name = (name,)
    
shop_name()
print(shop_name[0])

def add():#Agregar Productos
    """Nombre, Precio y Cantidad Disponible"""
    while True:
        try:
            name = input("Ingresa el nombre de el producto")

        except ValueError:
            print("¡ERROR!")
            
    
def search():#Buscar Producto
    """Buscar un producto por su nombre y
    Mostrar sus detalles(Nombre, Precio, Cantidad)"""

def update():#Actualizar Producto
    """Modificar el precio/cantidad de un producto"""
    
def remove():#Eliminar Producto
    """Eliminar un producto que ya no esta disponible"""
    
def calculate_inventory():#Calcular el valor total de el inventario
    """multiplicar el precio por la cantidad de cada producto
y mostrar el total acumulado."""

def view_inventory():#Ver el inventario completo //FUNCIONA
    """Mostrar el inventario completo de productos"""
    print(f"\n===== El inventario de la tienda {shop_name[0]} =====")
    for (i) in inventory:
        print(i)

def main_menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. valor total del inventario")
        print("6. Ver el inventario")
        print("0. ¡Salir!")
        print("\n--- - ---")
        option = input("Selecciona un opción: ")
        