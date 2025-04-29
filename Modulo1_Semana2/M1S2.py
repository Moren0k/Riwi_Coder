lista_notas_validas = [] # Lista para almacenar calificaciones válidas

# Función para guardar calificaciones
def guardar_calificaciones(): 
    while True:
        evaluo = int(input("Desde que numero de calificación quieres evaluar: "))
        entrada = input("Ingresa una calificación (0 a 100) o 'fin' para terminar: ").strip()
        
        # Verificar si el usuario quiere terminar
        if entrada.lower() == "fin":
            break

        try:
            calificacion = float(entrada)
            # Evaluar si el estudiante aprobó o reprobó
            if calificacion <= evaluo:
                print("Reprobado")
            else:
                print("Aprobado")

            # Validar que la calificación esté en el rango de 0 a 100
            if 0 <= calificacion <= 100:
                lista_notas_validas.append(calificacion)
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Error: Debes ingresar un número válido o 'fin' para terminar.")

guardar_calificaciones()
print("Calificaciones válidas ingresadas:", lista_notas_validas)

def calcular_promedio(lista_notas_validas=[]):
    if not lista_notas_validas:
        print("No hay calificaciones válidas para calcular el promedio.")
        return
    promedio = sum(lista_notas_validas) / len(lista_notas_validas)
    print("el promedio de las calificaciones es: ", promedio)
calcular_promedio(lista_notas_validas)