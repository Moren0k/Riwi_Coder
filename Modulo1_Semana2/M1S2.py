"""Jhos Kevin Agudelo Moreno"""
lista_notas_validas = [] # Lista para almacenar calificaciones válidas

while True:
    try:
        evaluo = float(input("Desde qué número de calificación quieres evaluar (1 a 99): "))
        if 1 <= evaluo <= 99:
            break
        print("Error: La calificación de evaluación debe estar entre 1 y 99.")
    except:
        print("Error: Entrada no válida. Debe ser un número entre 1 y 99.")
        
#   Función para guardar, validar y evaluar calificaciones
def calificaciones():
    while True:
        entrada = input("Ingresa una calificación (0 a 100) o 'fin' para terminar: ")
        if entrada.lower() == "fin":#Verificar si el usuario quiere terminar de ingresar calificaciones
            break 
        if "," in entrada:
            partes = entrada.split(",")
        else:
            partes = [entrada]
        for parte in partes:
            try:
                calificacion = float(parte.strip())
                if 0 <= calificacion <= 100:
                    lista_notas_validas.append(calificacion)
                    if calificacion >= evaluo:
                        print(calificacion, "# Aprobado")
                    else:
                        print(calificacion, "# Reprobado")
                else:
                    print("Error: La calificación debe estar entre 0 y 100.")
            except ValueError:
                print("Error: Entrada no válida. Debe ser un número o 'fin'.")
calificaciones()
print("\n--- Calificaciones válidas ---")
print("Calificaciones válidas ingresadas:", lista_notas_validas)

#   Función para calcular el promedio de las calificaciones
def calcular_promedio(lista_notas_validas=[]): 
    if not lista_notas_validas:
        print("No hay calificaciones válidas para calcular el promedio.")
        return
    promedio = sum(lista_notas_validas) / len(lista_notas_validas)
    print("El promedio de las calificaciones es:", round(promedio, 2))
print("\n--- Calcular promedio ---")
calcular_promedio(lista_notas_validas)

#   Función para contar cuántas calificaciones son mayores a un valor dado
def contar_calificaciones_mayoresa (lista_notas_validas): 
    if not lista_notas_validas:
        print("No hay calificaciones válidas para contar.")
        return
    valor = float(input("Ingresa un valor para buscar calificaciones mayores: "))
    contador = sum(1 for calificacion in lista_notas_validas if calificacion > valor)
    print("hay", contador, "calificaciones mayores a", valor)
print("\n--- Contar calificaciones mayores a un valor ---")
contar_calificaciones_mayoresa(lista_notas_validas)