"""
3.1.2 Actividad listas (Clase 1)
Ejercicio 2
Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
los nombres y apellidos.
"""
#Crear listas
nombres = ["Juan", "Pedro", "Maria"]
apellidos = ["Perez", "Gomez", "Gonzalez"]

#Mostrar nombres y apellidos ordenados
for i in range(len(nombres)):
    print(f"{nombres[i]} {apellidos[i]}")
