"""
3.2.3 Guía de ejercicios resueltos (Clase 5)
Ejercicio Adicional 3: Tuplas y Conjuntos en Combinación
Creen un programa que solicite a los usuarios ingresar nombres y edades.
Almacenen estos datos en una lista de tuplas. Luego, utilicen un conjunto para
identificar las edades únicas presentes en la lista.
"""
# Solicitar al usuario que ingrese nombres y edades
personas = []
while True:    
    nombre = input("Ingrese un nombre (Si no ingresa nada el programa termina): ")
    if nombre == "":
        break
    while True:
        try:
            edad = int(input("Ingrese la edad de " + nombre + ": "))
        except ValueError:
            print("Debe ingresar un número entero.")
        else:
            if edad < 0:
                print("La edad debe ser positiva.")
            else:
                personas.append((nombre, edad))
                break

# Crear una lista vacía para almacenar las edades únicas
edades = []
# Recorrer la lista de tuplas
for persona in personas:
    # Extraer la edad de la tupla
    edad = persona[1]
    # Si la edad no está en la lista de edades, agregarla
    if edad not in edades:
        edades.append(edad)

# Mostrar las edades únicas
print("Edades únicas:", edades)
