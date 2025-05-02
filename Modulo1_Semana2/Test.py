entrada = input("Ingresa una lista de números separados por comas: ").strip()
if "," in entrada:
    print("Esto es una lista")
    lista_notas = entrada.split(",")
    print("Lista de números:", lista_notas)
else:
    print("Esto no es una lista")

for lista_notas in lista_notas:
    numero = float(lista_notas.strip())
    print(numero)