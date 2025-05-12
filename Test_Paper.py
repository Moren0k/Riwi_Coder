# Test paper para probar fragmentos de código, solo pruebas rápidas y ajustes.
inventory = [
    {"title": "p1", "price": 10.0, "quantity": 100},
    {"title": "p2", "price": 15.0, "quantity": 50},
    {"title": "p3", "price": 20.0, "quantity": 30},
    {"title": "p4", "price": 25.0, "quantity": 10},
    {"title": "p5", "price": 30.0, "quantity": 5},
    {"title": "p5", "price": 30.0, "quantity": 5}

    ]

def contador():
        nm = len(inventory)
        print(nm)
    
    
    
contador()






def start_data():
    data_number = len(inventory)
    print(f"\n---Bienvenido al sistema, Actualmente tienes {data_number} productos en el inventario---")
    if data_number < 5:
        for i in range(5):
            add()
start_data()
