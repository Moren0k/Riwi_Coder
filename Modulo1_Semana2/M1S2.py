def ingresar_Calificacion(): #Solicitar al usuario ingresar una calificación numérica (de 0 a 100).

    while True:
        calificacion = float(input("\nIngresa la calificación número (de 0 a 100): "))
        print(f"La calificación ingresada es: {calificacion}")
   
        if calificacion < 0 or calificacion > 100:
                print("La calificación debe ser entre 0 y 100.")
        else:
            return calificacion
        print("Por favor, ingresa un número válido.")
    

def evaluar_Calificacion(calificacion): # Validamos si aprobo o reprobo.
     if calificacion >= 60:
          print("aprobado")
     else:
          print("reprobado")

calificaciones = []
contador = 0
while contador < 3:
    print("\nIngresa la calificación número", )
    calificacion = ingresar_Calificacion() #Donde se guarda la calificacion ingresada.


evaluar_Calificacion(calificacion) #Se llama la funcion para evaluar si es mas o menos que 60.
