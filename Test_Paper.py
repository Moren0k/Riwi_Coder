tupla_name = ()

def def_name():
    name = input("Ingresa el nombre a guardar en la tupla: ")
    global tupla_name  # Esto es para modificar la tupla global
    tupla_name = tupla_name + (name,)  # Convertimos tupla en lista, agregamos y convertimos de nuevo a tupla
    
def_name()
print(tupla_name)




import re

# Función que valida que la entrada solo contenga texto
def validar_texto():
    while True:
        # Pedimos al usuario que ingrese un texto
        entrada = input("Ingresa solo texto: ")
        
        # Usamos una expresión regular para verificar que solo contenga letras y espacios
        if re.match("^[A-Za-záéíóúÁÉÍÓÚüÜñÑ ]+$", entrada):
            return entrada  # Si la entrada es válida, la devolvemos
        else:
            print("¡Error! Solo se permiten letras (con tildes y ñ) y espacios. Por favor, intenta de nuevo.")

# Otra función que usa validar_texto
def procesar_datos():
    print("Bienvenido al sistema.")
    nombre = validar_texto()  # Llamamos a la función de validación dentro de otra función
    print(f"¡Hola, {nombre}! La entrada fue procesada correctamente.")

# Llamamos a la función que usa la validación
procesar_datos()
