"""
3.1.2 Actividad listas (Clase 1)
Ejercicio 3
Cree una lista y comience a almacenar nombres, cada vez que se agregue un
nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar
nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower()
y upper() ) .
Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de
caracteres
"""
# Se inicia lista
nombres = []

# Se pide ingresar nombres
while True:
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)
    respuesta = input("¿Desea ingresar otro nombre? (s/n): ")
    if respuesta.lower() == "n":
        break
    elif respuesta.lower() == "s":
        continue
    else:
        print("Respuesta inválida")
        break

# Se imprime la lista de nombres
print("Nombres ingresados:")
for nombre in nombres:
    print(nombre)

# Se elimina el nombre con menor cantidad de caracteres
min_len = len(nombres[0])
min_name = nombres[0]
for nombre in nombres:
    if len(nombre) < min_len:
        min_len = len(nombre)
        min_name = nombre

nombres.remove(min_name)

# Se imprime la lista de nombres sin el nombre con menor cantidad de caracteres
print("Nombres ingresados sin el nombre con menor cantidad de caracteres:")
for nombre in nombres:
    print(nombre)
