# Función para determinar el estado de aprobación
def estado_aprobacion():
    calificacion = float(input("Ingresa tu calificación (de 0 a 100): "))
    
    if calificacion >= 60:
        print("¡Aprobado!")
    else:
        print("Reprobado.")

# Función para calcular el promedio de una lista de calificaciones
def calcular_promedio():
    calificaciones = input("Ingresa las calificaciones separadas por comas: ")
    
    # Convertimos las calificaciones en una lista de números
    lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]
    
    # Calculamos el promedio
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    
    print(f"El promedio de las calificaciones es: {promedio:.2f}")

# Función para contar cuántas calificaciones son mayores que un valor dado
def contar_mayores():
    calificaciones = input("Ingresa las calificaciones separadas por comas: ")
    valor_comparar = float(input("Ingresa el valor con el que comparar las calificaciones: "))
    
    lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]
    
    # Contamos cuántas calificaciones son mayores que el valor dado
    count = sum(1 for calificacion in lista_calificaciones if calificacion > valor_comparar)
    
    print(f"Hay {count} calificaciones mayores que {valor_comparar}.")

# Función para verificar y contar calificaciones específicas
def verificar_calificaciones():
    calificaciones = input("Ingresa las calificaciones separadas por comas: ")
    
    lista_calificaciones = [float(calificacion) for calificacion in calificaciones.split(",")]
    
    # Calculamos el promedio
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)
    
    print(f"El promedio de las calificaciones es: {promedio:.2f}")
    
    # Aquí podrías añadir más lógica, como contar una calificación específica si lo deseas.

# Menú interactivo para ejecutar las funciones
def menu():
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Determinar estado de aprobación")
        print("2. Calcular promedio de calificaciones")
        print("3. Contar calificaciones mayores que un valor específico")
        print("4. Verificar y contar calificaciones específicas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            estado_aprobacion()
        elif opcion == "2":
            calcular_promedio()
        elif opcion == "3":
            contar_mayores()
        elif opcion == "4":
            verificar_calificaciones()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")

# Ejecutamos el programa
menu()